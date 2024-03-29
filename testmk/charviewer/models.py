from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):

    character_name = models.CharField(max_length=100)

    class Meta:
        def __str__(self):
            return self.character_name


class Moves(models.Model):

    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    move_name = models.CharField(verbose_name='move', max_length=100)

    move_input = models.CharField(verbose_name='input', max_length=50)

    move_type = models.CharField(verbose_name='type', max_length=50)

    damage = models.CharField(verbose_name='damage', max_length=10)

    block_damage = models.CharField(verbose_name='block damage', max_length=10)

    f_block_damage = models.CharField(verbose_name='flawless block damage',
                                      max_length=10)
    startup = models.CharField(verbose_name='startup', max_length=10)

    Active = models.CharField(verbose_name='active', max_length=10)

    Recovery = models.CharField(verbose_name='recovery', max_length=10)

    cancel_adv = models.CharField(verbose_name='cancel advantage',
                                  max_length=10)

    hit_adv = models.CharField(verbose_name='hit advantage', max_length=10)

    block_adv = models.CharField(verbose_name='block advantage', max_length=10)

    f_block_adv = models.CharField(verbose_name='flawless block advantage',
                                   max_length=10)
    info = models.CharField(verbose_name='information', max_length=250,
                            blank=True)

    equip = models.CharField(verbose_name='equiped move', max_length=250,
                             blank=True)

    classification = models.CharField(verbose_name='move classification',
                                      max_length=50)

    class Meta:
        def __str__(self):
            return self.move_name


class Notes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=300)
    move_id = models.IntegerField()
    # character_id = models.IntegerField(default=1)

    class Meta:
        def __str__(self):
            return self.note

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE)

#     def __str__(self):
#         return f'Profile for user {self.user.username}'
