import argparse


def log(*args, width=50):
    print(width * '=')
    for arg in args:
        print(f"{arg : ^{width}}")
    print(width * '=')
    print()


def get_args():
    parser = argparse.ArgumentParser(description='Show line of the images based on coordinates')

    # Add the arguments
    parser.add_argument('-w', '--width', type=int, required=True, help='width of the line')
    parser.add_argument('-x', type=int, help='x coordinate of middle point of the line')
    parser.add_argument('-y', type=int, help='y coordinate of middle point of the line')
    parser.add_argument('-a', '--alpha', type=int, default=0, help='width of the line')

    args = parser.parse_args()

    width = args.width
    alpha = args.alpha

    x = args.x
    if not x:
        x = width * 1.2

    y = args.y
    if not y:
        y = width * 1.2

    return x, y, width, alpha
