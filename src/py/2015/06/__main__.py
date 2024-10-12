import sys
import part_a, part_b


def app():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Expected:\n1. operation: 1 or 2\n2. input file')
        return

    if args[0] == '1':
        print(part_a.solver(args[1]))
    elif args[0] == '2':
        print(part_b.solver(args[1]))
    else:
        print('unknown operation')


app()