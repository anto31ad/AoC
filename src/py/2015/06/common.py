import re

def parse_instruction(input: str):
    tokens = input.split(' ')

    operation = None
    corners_x = []
    corners_y = []
    
    next_status = 'op'
    for token in tokens:
        if token == 'turn' and next_status == 'op':
            next_status = 'turn'
            continue
        elif token == 'toggle' and next_status == 'op':
            operation = 'toggle'
            next_status = 'c1'
            continue
        elif token == 'on' and next_status == 'turn':
            operation = 'on'
            next_status = 'c1'
            continue
        elif token == 'off' and next_status == 'turn':
            operation = 'off'
            next_status = 'c1'
            continue
        elif next_status == 'c1'\
            and re.search(r'^[0-9]{1,3},[0-9]{1,3}$',token):

            x, y = map(int, token.split(','))
            corners_x.append(x)
            corners_y.append(y)
            next_status = 'div'
            continue
        elif token == 'through' and next_status == 'div':
            next_status = 'c2'
            continue
        elif next_status == 'c2'\
            and re.search(r'^[0-9]{1,3},[0-9]{1,3}$',token):

            x, y = map(int, token.split(','))
            corners_x.append(x)
            corners_y.append(y)
            next_status = 'done'
            continue
        else:
            return None
    return [operation, sorted(corners_x), sorted(corners_y)]
