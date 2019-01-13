import os
import sys

class Main:

    def __init__(self, args=[]):
        pass

    def run(self):
        print(args)


if __name__ == "__main__":
    args = sys.argv[1:]

    m = Main(args)
    m.run()
