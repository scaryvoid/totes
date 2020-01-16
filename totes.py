#!/usr/bin/env python3

# return sum of numbers piped to this program

import sys, argparse
listCounters = []


class Counter(object):
    def __init__(self, column):
        self.column = column
        self.count = 0

    def increment(self, num):
        self.count += float(num)


def getsum():
    listTotals = []
    for obj in listCounters:
        listTotals.append(str(obj.count))

    print(" ".join(listTotals))


def main():
    parser = argparse.ArgumentParser(description='Add columns of data.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', metavar='<n>', nargs=1, default=' ', type=str, help='Delimiter')
    parser.add_argument('-f', nargs='+', default='1', help='Space separated list of colums to total')
    parser.add_argument('-p', help='Print input', action='store_true')
    parser.add_argument('-r', help='Print running total', action='store_true')
    args = parser.parse_args()

    for column in args.f:
        if column.isdigit():
            listCounters.append(Counter(int(column) - 1))
        else:
            print("Error: Column must be a list of space separated integers. \"{0}\"".format(column))
            sys.exit()

    for line in sys.stdin:
        listNums = line.strip().split(args.d[0])
        for obj in listCounters:
            # index out of range protection
            if len(listNums) < int(obj.column):
                continue

            newnum = listNums[int(obj.column)]
            try:
                newnum = float(newnum)
            except:
                print("Error: {0} is not an integer. Total may be wrong! Is your delimiter correct?".format(newnum.strip()))
                continue

            obj.increment(newnum)
        if args.p:
            print(line.strip())
        if args.r:
            getsum()
    if not args.r:
        getsum()


if __name__ == "__main__":
    main()
