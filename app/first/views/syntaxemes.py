from app_api.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View

def syntaxeme_list(request):
    all_syntaxemes_obj = Syntaxeme.objects.all()
    lst = []
    for i in all_syntaxemes_obj:
        current = {
        'PK': i.pk,
        'ID': i.ID,
        'clause_ID': i.clause_ID,
        }
        lst.append(current)
    return render(request, 'first/syntaxemes/syntaxemes.html', {'context': lst})

def syntaxeme_add(request):
    url = "syntaxemes"
    choice = Clause.objects.all()
    arr = []
    for item in choice:
        var = {
            'id': item.pk,
            'value': item
        }
        arr.append(var)
    ### 
    number = 0
    if request.POST.get('select'):
        var = request.POST.get('select')
        if var[8].isdigit():
            number = var[7] + var[8]
        else:
            number = var[7]
    ###   
    
    for clause in Clause.objects.all():
        if clause.pk == int(number):
            print(request.POST)
            syntaxeme = Syntaxeme(
            #Choice Menu
            ID = clause,
            clause_ID = clause,
            )
            syntaxeme.save()
            return redirect(url)
    return render(request, 'first/syntaxemes/syntaxeme_add_ajax.html', {'context': url, 'choices': arr})

def syntaxeme_change(request, detail_view_id):
    url = 'syntaxemes/' + str(detail_view_id)
    syntaxeme = Syntaxeme.objects.get(pk=detail_view_id)
    #######
    choice = Clause.objects.all()
    arr = []
    for item in choice:
        var = {
            'id': item.pk,
            'value': item
        }
        arr.append(var)
    ### 
    number = 0
    if request.POST.get('select'):
        var = request.POST.get('select')
        if var[8].isdigit():
            number = var[7] + var[8]
        else:
            number = var[7]
    ###   
    


    if request.POST.get('action') == 'Delete':
        syntaxeme.delete()
        return redirect('syntaxemes')
    

    if request.POST.get('action') == 'Save':
        for clause in Clause.objects.all():
            if clause.pk == int(number):
                print(request.POST)
                syntaxeme = Syntaxeme(
                #Choice Menu
                ID = clause,
                clause_ID = clause,
                )
                syntaxeme.save()
                return redirect(url)

    syntaxeme = Syntaxeme.objects.get(pk=detail_view_id)
    current = {
        'Type': 'Клауза',
        'clause_id': syntaxeme.ID,
        }

    return render(request, 'first/syntaxemes/syntaxeme_change_ajax.html', {'context': current, 'choices': arr})

def syntaxeme_view(request, detail_view_id):
    url = 'syntaxemes/' + str(detail_view_id)
    syntaxeme = Syntaxeme.objects.get(pk=detail_view_id)
    #######
    choice = Clause.objects.all()
    arr = []
    for item in choice:
        var = {
            'id': item.pk,
            'value': item
        }
        arr.append(var)
        
    number = 0
    if request.POST.get('select'):
        var = request.POST.get('select')
        number = var[7] + var[8]
    #######

    current = {
        'Type': 'Клауза',
        'clause_id': syntaxeme.ID,
        }
    if request.POST.get('action') == 'Delete':
        syntaxeme.delete()
        return redirect('syntaxemes')
    elif request.POST.get('action') == 'Edit':
        return redirect(url + '/change')
    return render(request, 'first/syntaxemes/syntaxeme_view_ajax.html', {'context': current, 'choices': arr, 'url': url})