import csv

from charviewer.models import Character


def run():
    fhand = open('/home/tony/code/test_mk/MK11-Characters.csv')
    reader = csv.reader(fhand)

    for row in reader:
        print(row)

        c, created = Character.objects.get_or_create(character_name=row[0])

        c.save()
