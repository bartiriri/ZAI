from django.db import models

class Scout(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Team(models.Model):
    team_number = models.IntegerField()
    team_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.team_number) + ' ' + self.team_name



class Degree(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Scout_degree(models.Model):
    degree = models.ForeignKey(Degree, related_name='degrees', on_delete=models.CASCADE)
    scout = models.ForeignKey(Scout, related_name='scouts', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.degree) + ' ' + str(self.scout)

class Allocation(models.Model):
    team = models.ForeignKey(Team, related_name='team', on_delete=models.CASCADE)
    scout = models.ForeignKey(Scout, related_name='scout', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team) + ' ' + str(self.scout)