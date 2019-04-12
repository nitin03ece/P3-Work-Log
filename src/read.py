import csv


def csvEmpty():
    with open("output/out.csv") as readfile:
        read = csv.DictReader(readfile)
        if len(list(read)) == 0:
            return True
        else:
            return False


def csvRead():
    with open("output/out.csv") as readfile:
        read = csv.DictReader(readfile)
        return list(read)
