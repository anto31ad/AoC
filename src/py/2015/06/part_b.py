import os

from common import parse_instruction

# >>> MEMO
# when using range(min, max) max is not included.

def solver(input_path):

    file = open(os.path.join(input_path))

    # using a set to avoid creating 1000x1000 array
    lights = dict()

    line = file.readline()
    line_count = 0
    while line:
        instr = parse_instruction(line.strip())

        # Would be cool to have a loading bar or sth
        if instr[0] == 'toggle':
            step_increase(instr[1], instr[2], lights, 2)
        elif instr[0] == 'on':
            step_increase(instr[1], instr[2], lights, 1)
        elif instr[0] == 'off':
            decrease(instr[1], instr[2], lights)
        else:
            break

        line = file.readline()
        line_count += 1
        msg = f"\rProcessed {line_count} lines"
        print(msg, end='', flush=True)

    print('\n')
    file.close()

    tot_brightness = 0
    for val in lights.values():
        tot_brightness += val

    return tot_brightness

def decrease(x_bounds: list[int], y_bounds: list[int], lights: dict):
    x_bounds = sorted(x_bounds)
    y_bounds = sorted(y_bounds)

    for x in range(x_bounds[0], x_bounds[1] + 1):
        for y in range(y_bounds[0], y_bounds[1] + 1):
            key = f"{x},{y}"
            brightness = lights.get(key)
            if not brightness:
                continue

            brightness -= 1
            if brightness < 1:
                lights.pop(key)
                continue
            lights[key] = brightness
            

def step_increase(x_bounds: list[int], y_bounds: list[int], lights: dict, step: int):
    x_bounds = sorted(x_bounds)
    y_bounds = sorted(y_bounds)

    for x in range(x_bounds[0], x_bounds[1] + 1):
        for y in range(y_bounds[0], y_bounds[1] + 1):
            key = f"{x},{y}"
            brightness = lights.get(key)
            if not brightness:
                brightness = 0
            lights[key] = brightness + step

