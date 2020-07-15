import csv


def save_to_file(data):
    file_name = input("input file name :")
    file = open(f"{file_name}.csv", mode="w", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "rate", "comment"])
    for review in data:
        writer.writerow(list(review.values()))
    return
