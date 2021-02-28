import csv


def import_csv(csv_filename):
    """ Function to load Circles through csv file """

    with open(csv_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            circle = Circle(**row)
            if int(circle.members_limit) > 0:
                circle.is_limited = True
            else:
                circle.is_limited = False
            circle.save()
            print(circle.name)
