import os

from common import parse_instruction

# >>> MEMO
# when using range(min, max) max is not included.

def solver(filepath):

    file = open(os.path.join(filepath))

    # using a set to avoid creating 1000x1000 array
    lights_on = set()

    line = file.readline()
    line_count = 0
    while line:
        instr = parse_instruction(line.strip())

        # Would be cool to have a loading bar or sth
        if instr[0] == 'toggle':
            toggle_lights(instr[1], instr[2], lights_on)
        elif instr[0] == 'on':
            turn_on_lights(instr[1], instr[2], lights_on)
        elif instr[0] == 'off':
            turn_off_lights(instr[1], instr[2], lights_on)
        else:
            break

        line = file.readline()
        line_count += 1
        msg = f"\rProcessed {line_count} lines"
        print(msg, end='', flush=True)
        

    file.close()
    print('\n')

    return len(lights_on)

def toggle_lights(x_bounds: list[int], y_bounds: list[int], lights_on_set: set):
    x_bounds = sorted(x_bounds)
    y_bounds = sorted(y_bounds)

    for x in range(x_bounds[0], x_bounds[1] + 1):
        for y in range(y_bounds[0], y_bounds[1] + 1):
            val = f"{x},{y}"
            if val in lights_on_set:
                lights_on_set.remove(val)
            else:
                lights_on_set.add(val)

def turn_off_lights(x_bounds: list[int], y_bounds: list[int], lights_on_set: set):
    x_bounds = sorted(x_bounds)
    y_bounds = sorted(y_bounds)

    for x in range(x_bounds[0], x_bounds[1] + 1):
        for y in range(y_bounds[0], y_bounds[1] + 1):
            val = f"{x},{y}"
            if val in lights_on_set: lights_on_set.remove(val)

def turn_on_lights(x_bounds: list[int], y_bounds: list[int], lights_on_set: set):
    x_bounds = sorted(x_bounds)
    y_bounds = sorted(y_bounds)

    for x in range(x_bounds[0], x_bounds[1] + 1):
        for y in range(y_bounds[0], y_bounds[1] + 1):
            val = f"{x},{y}"
            lights_on_set.add(val)
