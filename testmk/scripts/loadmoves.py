import csv

from charviewer.models import Moves, Character

cassie = Character.objects.get(pk=2)


def run():
    file_name = '/home/tony/code/test_mk/testmk/character_frames/Cassie.csv'

    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            c, created = Moves.objects.get_or_create(character=cassie,
                                                    move_name=row['Move'],
                                                    move_input=row['Input'],
                                                    move_type=row['Type'],
                                                    damage=row['Dmg'],
                                                    block_damage=row['Block dmg'],
                                                    f_block_damage=row['F/Block dmg'],
                                                    startup=row['Startup'],
                                                    Active=row['Active'],
                                                    Recovery=row['Recovery'],
                                                    cancel_adv=row['Cancel adv.'],
                                                    hit_adv=row['Hit adv.'],
                                                    block_adv=row['Block adv.'],
                                                    f_block_adv=row['F/Block adv.'],
                                                    info=row['Info'],
                                                    equip=row['Equip'],
                                                    classification=row['Classification'],
                                                    )

            c.save()
