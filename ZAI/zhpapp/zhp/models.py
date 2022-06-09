from django.db import models

class Harcerz(models.Model):
     imie = models.CharField(max_length=45)
     nazwisko = models.CharField(max_length=45)
     telefon = models.CharField(max_length=9)
     plec = models.CharField(max_length=10)
     data_dolaczenia = models.DateField()

     def __str__(self):
        return self.imie +' '+ self.nazwisko


class Druzyna(models.Model):
    nazwa_druzyny = models.CharField(max_length=100)
    numer_druzyny = models.IntegerField()
    data_zalozenia = models.DateField()

    def __str__(self):
        return str(self.numer_druzyny) + ' ' + str(self.nazwa_druzyny)

class Stopien(models.Model):
    nazwa_stopnia = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa_stopnia

class Harcerz_w_druzynie(models.Model):
    id_harcerz = models.ForeignKey(Harcerz, on_delete=models.CASCADE)
    id_druzyna = models.ForeignKey(Druzyna, on_delete=models.CASCADE)
    data_dolaczenia = models.DateField()

    def __str__(self):
        return str(self.data_dolaczenia)

class Stopien_harcerza(models.Model):
    id_harcerz = models.ForeignKey(Harcerz, on_delete=models.CASCADE)
    id_stopien = models.ForeignKey(Stopien, on_delete=models.CASCADE)
    data_zdobycia = models.DateField()

    def __str__(self):
        return str(self.data_zdobycia)