from app_api.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View

def clause_list(request):
    clauses = Clause.objects.all()
    lst = []
    for i in clauses:
        current = {
        'PK': i.pk,
        'ID': i.ID,
        'Text': i.text,
        'Sentence_ID': i.sentence_ID,
        'Frame_ID': i.frame_ID
        }
        lst.append(current)
    return render(request, 'first/clauses/clauses.html', {'context': lst})

def clause_add(request):
    url = "clauses"
    choice = Sentence.objects.all()
    arr = []
    print(request.POST)
    for item in choice:
        var = {
            'id': item.pk,
            'value': item
        }
        arr.append(var)
        
    number = 0
    if request.POST.get('doc_select'):
        var = request.POST.get('doc_select')
        number = var[7] + var[8]

    
    for sentence in Sentence.objects.all():
        if sentence.pk == int(number):
            print(request.POST)
            clause = Clause(
            #Choice Menu
            ID = sentence,
            text = request.POST.get('text'),
            sentence_ID = sentence,
            frame_ID = request.POST.get('frame_id')
            )
            clause.save()
            return redirect(url)
    return render(request, 'first/clauses/clause_add_ajax.html', {'context': url, 'choices': arr})

def clause_change(request, detail_view_id):
    url = 'clauses/' + str(detail_view_id)
    clause = Clause.objects.get(pk=detail_view_id)
    #######
    choice = Sentence.objects.all()
    arr = []
    for item in choice:
        var = {
            'id': item.pk,
            'value': item
        }
        arr.append(var)
        
    number = 0
    if request.POST.get('document_id'):
        var = request.POST.get('document_id')
        number = var[7] + var[8]
    #######


    if request.POST.get('action') == 'Delete':
        clause.delete()
        return redirect('clauses')
    

    if request.POST.get('action') == 'Save':
        for sentence in Sentence.objects.all():
            if sentence.pk == int(number):
                print(request.POST)
                clause = Clause(
                #Choice Menu
                ID = sentence,
                text = request.POST.get('text'),
                sentence_ID = sentence,
                frame_ID = request.POST.get('frame_id')
                )
                clause.save()
                return redirect(url)

    clause = Clause.objects.get(pk=detail_view_id)
    current = {
        'Type': 'Клауза',
        'sentence_id': clause.ID,
        'text': clause.text,
        'frame_id': clause.frame_ID,
        
        }

    return render(request, 'first/clauses/clause_change_ajax.html', {'context': current, 'choices': arr})

def clause_view(request, detail_view_id):
    url = 'clauses/' + str(detail_view_id)
    clause = Clause.objects.get(pk=detail_view_id)
    ##############################
    choice = Sentence.objects.all()
    arr = []
    for item in choice:
        var = {
            'id': item.pk,
            'value': item
        }
        arr.append(var)
    ###########################
    current = {
        'Type': 'Клауза',
        'sentence_id': clause.ID,
        'text': clause.text,
        'frame_id': clause.frame_ID,
        
        #Document ID ??
        }
    if request.POST.get('action') == 'Delete':
        clause.delete()
        return redirect('/apps/first/clauses')
    elif request.POST.get('action') == 'Edit':
        return redirect(url + '/change')
    return render(request, 'first/clauses/clause_view_ajax.html', {'context': current, 'choices': arr, 'url': url})