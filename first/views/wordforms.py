from first.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View

def wordform_list(request):
    all_wordform_obj = Wordform.objects.all()
    lst = []
    for i in all_wordform_obj:
        current = {
        'PK': i.pk,
        'ID': i.ID,
        'syntaxeme_ID': i.syntaxeme_ID,
        'frame_role_ID': i.frame_role_ID,
        'position_in_document': i.position_in_document,
        'position_in_sentence': i.position_in_sentence,
        'clause_position': i.clause_position,
        'text': i.text,
        'root_morpheme_ID': i.root_morpheme_ID
        }
        lst.append(current)
    return render(request, 'first/wordforms/wordforms_list_ajax.html', {'context': lst})

def wordform_add(request):
    url = "/apps/first/wordforms"
    choice = Syntaxeme.objects.all()
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
    print(request.POST)
    print(number)
    for syntaxeme in Syntaxeme.objects.all():
        if syntaxeme.pk == int(number):
            wordform = Wordform(
            #Choice Menu
            ID = syntaxeme,
            syntaxeme_ID = syntaxeme,
            frame_role_ID = request.POST.get('framerole_id'),
            position_in_document = request.POST.get('doc_position'),
            position_in_sentence = request.POST.get('sentence_position'),
            clause_position = request.POST.get('clause_position'),
            text = request.POST.get('text'),
            root_morpheme_ID = request.POST.get('root_morpheme_id'),
            )
            print("HELLLO")
            wordform.save()
            return redirect(url)
    return render(request, 'first/wordforms/wordforms_add_ajax.html', {'context': url, 'choices': arr})

def wordform_change(request, detail_view_id):
    url = '/apps/first/syntaxemes/' + str(detail_view_id)
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
        return redirect('/apps/first/syntaxemes')
    

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

    return render(request, 'first/wordforms/wordform_change_ajax.html', {'context': current, 'choices': arr})

def wordform_view(request, detail_view_id):
    url = '/apps/first/syntaxemes/' + str(detail_view_id)
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
        return redirect('/apps/first/syntaxemes')
    elif request.POST.get('action') == 'Edit':
        return redirect(url + '/change')
    return render(request, 'first/wordforms/wordform_view_ajax.html', {'context': current, 'choices': arr, 'url': url})