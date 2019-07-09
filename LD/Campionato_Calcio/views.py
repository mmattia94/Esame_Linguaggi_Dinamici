import operator
from collections import OrderedDict

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse
from .models import Opzioni, Campionato, Calendario, Squadra, Risultati
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    options_list = Opzioni.objects.all()
    context = {'options_list': options_list}
    return render(request, 'home.html', context)


@login_required
def sel_calendario(request):
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'calendario':
            url = reverse('Campionato_Calcio:calendario', args=[request.POST['campionato']]) + '?page=1'
            return HttpResponseRedirect(url)
        if 'action' in request.POST and request.POST['action'] == 'classifica':
            url = reverse('Campionato_Calcio:classifica', args=[request.POST['campionato']])
            return HttpResponseRedirect(url)
    campionati = Campionato.objects.all()
    options_list = Opzioni.objects.all()
    action = request.META["PATH_INFO"].replace("/Campionato/", "")
    action = action[:action.find("/")]
    # action = 'classifica'
    context = {'campionati': campionati,
               'options_list': options_list,
               'action': action}
    return render(request, 'Campionato/sel_campionato.html', context)


@login_required
def sel_giornata(request):
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'risultati':
            url = reverse('Campionato_Calcio:giornata', args=[request.POST['campionato'],
                                                              request.POST['giornata'], request.POST['ar']])
            return HttpResponseRedirect(url)
        if 'action' in request.POST and request.POST['action'] == 'schedina':
            url = reverse('Campionato_Calcio:schedina', args=[request.POST['campionato'],
                                                              request.POST['giornata'], request.POST['ar']])
            return HttpResponseRedirect(url)
    campionati = Campionato.objects.all()
    giornate = range(1, 20)
    options_list = Opzioni.objects.all()
    action = request.META["PATH_INFO"].replace("/Campionato/", "")
    action = action[:action.find("/")]
    context = {'campionati': campionati,
               'options_list': options_list,
               'action': action,
               'giornate': giornate}
    return render(request, 'Campionato/sel_giornata.html', context)


@login_required
def sel_squadra(request):
    if request.method == 'POST':
        if all(k in request.POST for k in ('squadra', 'campionato')):
            url = reverse('Campionato_Calcio:squadra', args=[request.POST['campionato'], request.POST['squadra']])
            return HttpResponseRedirect(url)
        else:
            raise Http404
    campionati = Campionato.objects.all()
    squadre = Squadra.objects.all().order_by('nome')
    options_list = Opzioni.objects.all()
    context = {'campionati': campionati,
               'squadre': squadre,
               'options_list': options_list}
    return render(request, 'Campionato/sel_squadra.html', context)


@login_required
def calendario(request, camp_id):
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'calendario':
            url = reverse('Campionato_Calcio:calendario', args=[request.POST['campionato']]) + '?page=1'
            return HttpResponseRedirect(url)
    cal = Calendario.objects.filter(campionato_id=camp_id)
    campionati = Campionato.objects.all()
    paginator = Paginator(cal, 25)
    page = request.GET.get('page')
    cal = paginator.get_page(page)
    options_list = Opzioni.objects.all()
    context = {'calendario': cal,
               'campionati': campionati,
               'current_camp': Campionato.objects.get(id=camp_id),
               'options_list': options_list,
               'action': 'calendario'}
    return render(request, 'Campionato/calendario.html', context)


@login_required
def classifica(request, camp_id):
    if request and request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'classifica':
            url = reverse('Campionato_Calcio:classifica', args=[request.POST['campionato']])
            return HttpResponseRedirect(url)
    cal = Calendario.objects.filter(campionato_id=camp_id)
    squadre = cal.values_list('locali_id', flat=True)
    classifica_finale = OrderedDict()
    for s in Squadra.objects.filter(id__in=squadre):
        classifica_finale[s.nome] = 0

    for c in cal:
        ris = Risultati.objects.get(partita=c.id)
        reti_locali, reti_ospiti = ris.retiLocali, ris.retiOspiti
        sq_locale, sq_ospiti = Squadra.objects.get(id=c.locali_id).nome, Squadra.objects.get(id=c.ospiti_id).nome
        if reti_locali > reti_ospiti:
            classifica_finale[sq_locale] += 3
        elif reti_locali != reti_ospiti:
            classifica_finale[sq_ospiti] += 3
        else:
            classifica_finale[sq_locale] += 1
            classifica_finale[sq_ospiti] += 1

    classifica_finale = sorted(classifica_finale.items(), key=operator.itemgetter(1), reverse=True)
    if request:
        options_list = Opzioni.objects.all()
        context = {'classificaFinale': classifica_finale,
                   'current_camp': Campionato.objects.get(id=camp_id),
                   'options_list': options_list,
                   'campionati': Campionato.objects.all(),
                   'action': 'classifica'}
        return render(request, 'Campionato/classifica.html', context)
    else:
        return classifica_finale


@login_required
def risultati(request, camp_id, giornata_id, ar):
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'risultati':
            url = reverse('Campionato_Calcio:giornata', args=[request.POST['campionato'],
                                                              request.POST['giornata'], request.POST['ar']])
            return HttpResponseRedirect(url)
    partite = Calendario.objects.filter(campionato_id=camp_id, giornata=giornata_id, AR=ar)
    ris = Risultati.objects.filter(id__in=partite.values_list('id', flat=True))
    options_list = Opzioni.objects.all()
    context = {'partite': zip(partite, ris),
               'current_camp': Campionato.objects.get(id=camp_id),
               'g': giornata_id,
               'ar': ar,
               'options_list': options_list,
               'campionati': Campionato.objects.all(),
               'giornate': range(1,20),
               'action': 'risultati'}
    return render(request, 'Campionato/risultati.html', context)


@login_required
def schedina(request, camp_id, giornata_id, ar):
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'schedina':
            url = reverse('Campionato_Calcio:schedina', args=[request.POST['campionato'],
                                                              request.POST['giornata'], request.POST['ar']])
            return HttpResponseRedirect(url)
    partite = Calendario.objects.filter(campionato_id=camp_id, giornata=giornata_id, AR=ar)
    ris = Risultati.objects.filter(id__in=partite.values_list('id', flat=True))
    d = OrderedDict()
    for p, r in zip(partite, ris):
        if r.retiLocali > r.retiOspiti:
            d[p.id] = 1
        elif r.retiLocali < r.retiOspiti:
            d[p.id] = 2
        else:
            d[p.id] = "X"
    options_list = Opzioni.objects.all()
    context = {'partite': zip(partite, d.values()),
               'current_camp': Campionato.objects.get(id=camp_id),
               'g': giornata_id,
               'ar': ar,
               'options_list': options_list,
               'campionati': Campionato.objects.all(),
               'giornate': range(1, 20),
               'action': 'schedina'}
    return render(request, 'Campionato/schedina.html', context)


@login_required
def squadra(request, camp_id, nome_squadra):
    if request.method == 'POST':
        if all(k in request.POST for k in ('squadra', 'campionato')):
            url = reverse('Campionato_Calcio:squadra', args=[request.POST['campionato'], request.POST['squadra']])
            return HttpResponseRedirect(url)
        else:
            raise Http404
    team = get_object_or_404(Squadra, nome=nome_squadra)
    # recupero le giornate dove è presente la squadra selezionata per il calendario selezionato
    cal = Calendario.objects.filter(Q(campionato_id=camp_id) & (Q(locali=team.id) | Q(ospiti=team.id)))
    ris = Risultati.objects.filter(partita__in=cal.values_list('id'))
    reti_totali = 0
    reti_subite_totali = 0
    vittorie = 0
    sconfitte = 0
    pareggi = 0
    for c in cal:
        reti_locali = ris.get(partita=c.id).retiLocali
        reti_ospiti = ris.get(partita=c.id).retiOspiti

        if c.locali_id == team.id:
            reti_totali = reti_totali+ris.get(partita=c.id).retiLocali
            reti_subite_totali = reti_subite_totali+ris.get(partita=c.id).retiOspiti

            if reti_locali > reti_ospiti:
                vittorie = vittorie+1
            elif reti_locali != reti_ospiti:
                sconfitte = sconfitte + 1
            else:
                pareggi = pareggi + 1

        else:
            reti_totali = reti_totali + ris.get(partita=c.id).retiOspiti
            reti_subite_totali = reti_subite_totali + ris.get(partita=c.id).retiLocali

            if reti_locali > reti_ospiti:
                sconfitte = sconfitte + 1
            elif reti_locali != reti_ospiti:
                vittorie = vittorie + 1
            else:
                pareggi = pareggi + 1

    c = classifica(None, camp_id=camp_id)
    matchlist = [item for item in c if item[0] == nome_squadra]
    if not matchlist:
        raise Http404
    punteggio_finale = matchlist[0][1]
    posizione_classifica = c.index(matchlist[0]) + 1
    options_list = Opzioni.objects.all()
    context = {'squadra': team,
               'campionato': Campionato.objects.get(id=camp_id),
               'retiTotali': reti_totali,
               'retiSubite': reti_subite_totali,
               'vittorie': vittorie,
               'sconfitte': sconfitte,
               'pareggi': pareggi,
               'punteggioFinale': punteggio_finale,
               'posizione_classifica': posizione_classifica,
               'options_list': options_list,
               'campionati': Campionato.objects.all(),
               'squadre': Squadra.objects.all().order_by('nome')}
    return render(request, 'Campionato/squadra.html', context)
