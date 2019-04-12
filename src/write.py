import csv
import read


fieldnames = ["Date", "Title", "Time Spent", "Notes"]


def csvwriteReload(entry):
    with open("output/out.csv", 'a', encoding='utf-8') as writefile:
        fieldnames = ["Date", "Title", "Time Spent", "Notes"]
        file = csv.DictWriter(writefile, fieldnames=fieldnames)

        # Check if csv file is Empty
        if read.csvEmpty():
            file.writeheader()

        file.writerow(entry)


def csvWrite(rows):
    with open("output/out.csv", 'w', encoding='utf-8') as writefile:
        fieldnames = ["Date", "Title", "Time Spent", "Notes"]
        file = csv.DictWriter(writefile, fieldnames=fieldnames)

        file.writeheader()

        for row in rows:
            file.writerow(dict(row))
