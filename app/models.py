from django.db import models


class Participant(models.Model):
    Username = models.CharField(max_length=30)
    Score = models.IntegerField(default=0)
    School = models.CharField(max_length=30)
    Solved_Problems = models.IntegerField(default=0)
    Number_Of_Tests = models.IntegerField(default=0)

    def __str__(self):
        return self.Username


class Game(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(blank=True, upload_to='Game_image')
    Statement = models.ImageField(blank=True, upload_to='Game_statement')
    Processing_Path = models.CharField(max_length=200)
    Score = models.IntegerField()
    Default_Python_Code = models.TextField()
    Number_Of_Tests = models.IntegerField()

    def __str__(self):
        return self.Name


class Advancement(models.Model):
    Game_Id = models.IntegerField()
    Participant_Id = models.IntegerField()
    Wrote_Code = models.TextField()
    Used_Language = models.CharField(max_length=30)
    Score = models.IntegerField(default=0)
    Percentage = models.IntegerField(default=0)
    Color = models.CharField(max_length=30, default="black")
    Results = models.CharField(max_length=500, default="")
    Number_Of_Tests = models.IntegerField(default=0)

    def __str__(self):
        return "Advancement of {} in {}".format(Participant.objects.get(id=self.Participant_Id),
                                                Game.objects.get(id=self.Game_Id))


class Test(models.Model):

    Game_Id = models.IntegerField()
    Test_Id = models.IntegerField()
    Input = models.CharField(max_length=200)
    Score = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(Game.objects.get(id=self.Game_Id), self.Test_Id)








