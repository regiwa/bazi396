from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length =64, unique =True)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    #owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    #settings
    is_full_name_displayed = models.BooleanField(default=True)

    #details
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)
    interests = models.ManyToManyField(UserInterest, blank=True)


class bz_langit(models.Model):
    karakter = models.CharField(max_length=10, unique=True)
    pinyin = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    elemen = models.CharField(max_length=10, blank=True, null=True)
    desc_pos = models.CharField(max_length=500, blank=True, null=True)
    desc_neg = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.karakter


class bz_bumi(models.Model):
    karakter = models.CharField(max_length=10, unique=True)
    pinyin = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    elemen = models.CharField(max_length=10, blank=True, null=True)
    desc_pos = models.CharField(max_length=500, blank=True, null=True)
    desc_neg = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.karakter


class bz_kua(models.Model):
    kua = models.CharField(max_length=10, unique=True)
    hadap = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.kua


class bz_annual(models.Model):
    year = models.IntegerField()
    first = models.ForeignKey(bz_langit, on_delete=models.SET_NULL, blank=True, null=True)
    second = models.ForeignKey(bz_bumi, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.year)

class bz_arti(models.Model):
    harm = models.BooleanField(default=False)
    clash = models.BooleanField(default=False)
    horse = models.BooleanField(default=False)
    peachb = models.BooleanField(default=False)
    grave = models.BooleanField(default=False)
    xing = models.BooleanField(default=False)
    first = models.CharField(max_length=10, blank=True, null=True)
    second = models.CharField(max_length=10, blank=True, null=True)
    mean = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.mean)

class bz_health(models.Model):
    elemen = models.CharField(max_length=10, blank=True, null=True)
    mean = models.CharField(max_length=500, blank=True, null=True)
    kurangi = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.elemen

class bz_story(models.Model):
    dm = models.CharField(max_length=10, blank=True, null=True)
    tubuh = models.CharField(max_length=10, blank=True, null=True)
    too_much = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    yongshen = models.CharField(max_length=64, blank=True, null=True)
    story = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

class bz_persona(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    birthdate = models.DateField()
    birthhour = models.IntegerField()

    kua = models.CharField(max_length=10, blank=True, null=True)
    yya = models.CharField(max_length=10, unique=True)
    yyb = models.CharField(max_length=10, unique=True)
    mma = models.CharField(max_length=10, unique=True)
    mmb = models.CharField(max_length=10, unique=True)
    dda = models.CharField(max_length=10, unique=True)
    ddb = models.CharField(max_length=10, unique=True)
    hra = models.CharField(max_length=10, unique=True)
    hrb = models.CharField(max_length=10, unique=True)

    lucka1 = models.CharField(max_length=10, unique=True)
    luckb1 = models.CharField(max_length=10, unique=True)
    lucka2 = models.CharField(max_length=10, unique=True)
    luckb2 = models.CharField(max_length=10, unique=True)
    lucka3 = models.CharField(max_length=10, unique=True)
    luckb3 = models.CharField(max_length=10, unique=True)
    lucka4 = models.CharField(max_length=10, unique=True)
    luckb4 = models.CharField(max_length=10, unique=True)
    lucka5 = models.CharField(max_length=10, unique=True)
    luckb5 = models.CharField(max_length=10, unique=True)
    lucka6 = models.CharField(max_length=10, unique=True)
    luckb6 = models.CharField(max_length=10, unique=True)
    lucka7 = models.CharField(max_length=10, unique=True)
    luckb7 = models.CharField(max_length=10, unique=True)
    lucka8 = models.CharField(max_length=10, unique=True)
    luckb8 = models.CharField(max_length=10, unique=True)
    lucka9 = models.CharField(max_length=10, unique=True)
    luckb9 = models.CharField(max_length=10, unique=True)

    masfem = models.CharField(max_length=10, blank=True, null=True)
    body = models.CharField(max_length=10, blank=True, null=True)
    bone = models.CharField(max_length=10, blank=True, null=True)
    yongshen = models.CharField(max_length=10, blank=True, null=True)
    xishen = models.CharField(max_length=10, blank=True, null=True)
    notes = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name

