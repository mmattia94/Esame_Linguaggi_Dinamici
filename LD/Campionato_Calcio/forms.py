from Campionato_Calcio.models import Campionato, Calendario, Squadra, Risultati
from django.forms import ModelForm, Form, CharField, ChoiceField, IntegerField


class SquadraSearchform(Form):
    campionato = IntegerField()
    squadra = CharField()

