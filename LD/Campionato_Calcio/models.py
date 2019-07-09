from django.db import models


# Operazioni = [
#     "Calendario Partite",
#     "Risultati Giornate di Campionato",
#     "Schedina delle Giornate",
#     "Classifica Finale Campionato"
#     "Statistiche Squadre",
# ]


class Opzioni(models.Model):
    nome = models.CharField(max_length=50)
    code = models.CharField(max_length=11)
    icon = models.CharField(max_length=50)


class Campionato(models.Model):
    nome = models.CharField(max_length=20)


class Squadra(models.Model):
    nome = models.CharField(max_length=20)


class Calendario(models.Model):
    campionato = models.ForeignKey(to=Campionato, on_delete=models.CASCADE)
    giornata = models.IntegerField()
    data = models.DateField()
    locali = models.ForeignKey(to=Squadra, on_delete=models.DO_NOTHING, related_name='+')
    ospiti = models.ForeignKey(to=Squadra, on_delete=models.DO_NOTHING, related_name='+')
    AR = models.CharField(max_length=1, default='A')


class Risultati(models.Model):
    partita = models.IntegerField()
    retiLocali = models.IntegerField()
    retiOspiti = models.IntegerField()
