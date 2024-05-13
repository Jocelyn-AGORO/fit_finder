from django.db import models
from django.contrib.auth import get_user_model
from django_db_views.db_view import DBView


# user profile informations
class UserProfile(models.Model):
    MALE = "H"
    FEMALE = "F"
    OTHER = "OT"
    GENDERS = {
        MALE: "Homme",
        FEMALE: "Femme",
        OTHER: "Autre"
    }
    age = models.IntegerField(max_length=2)
    biography = models.TextField()
    gender = models.CharField(max_length=30, choices=GENDERS)
    city = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=255)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f"{str(self.user)} age : {self.age} gender: {self.gender} city: {self.city}"


class UserView(DBView):
    pass


class Match(models.Model):
    matcher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    matched = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    accepted = models.BooleanField(db_default=False, default=False)
    match_date = models.DateTimeField(null=True, blank=True)


# user profile images
class PictureLibrary(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=False)


# all fitness and sports recorded with their level
class Sports(models.Model):
    BEGINNER = "BE"
    AMATEUR = "AM"
    INTERMEDIATE = "IN"
    ADVANCED = "AD"
    LEVELS = {
        BEGINNER: "Débutant",
        AMATEUR: "Amateur",
        INTERMEDIATE: "Intermédiaire",
        ADVANCED: "Avancé"
    }

    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, choices=LEVELS)

    def __str__(self):
        return f"{self.name} {self.level}"


# avalibiliy of user for fitness
class Avalibiliy(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    day = models.CharField(max_length=255)
    time_of_day = models.CharField(max_length=255)

    def __str__(self):
        return f"Disponible les {self.day} à/entre {self.time_of_day}"


class Goals(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    goal = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.goal}"


# user reviews and marks from each other
class ReviewRatings(models.Model):
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    points = models.SmallIntegerField(max_length=1)
    review = models.TextField()

    def __str__(self):
        return f"{self.points}"


# user particular dispositions
class Particularity(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
