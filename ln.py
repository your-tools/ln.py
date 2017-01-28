import argparse
import os
import sys

def ln(*, from_, to, verbose=False):
    if verbose:
        print(from_, "->", to)
    os.symlink(to, from_)


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("first")
    parser.add_argument("second")
    args = parser.parse_args(args)
    first = args.first
    second = args.second

    print("1.", first,  "->", second)
    print("2.", second, "->", first)

    answer = input("Which one? ")
    if answer == "1":
        from_ =args.first
        to = args.second
    elif answer == "2":
        to =args.first
        from_ = args.second
    else:
        sys.exit("Please choose between 1. and 2.")

    if os.path.islink(from_):
        dest = os.readlink(from_)
        message = "{} -> {} already exists. Overwrite? (Y/n) "
        message = message.format(from_, dest)
        answer = input(message)
        if answer == "n":
            sys.exit(1)
        else:
            os.remove(from_)

    if os.path.exists(from_) and not os.path.islink(from_):
        message = "Error: {} already exists and is not a symlink"
        sys.exit(message.format(from_))

    ln(from_=from_, to=to, verbose=True)
