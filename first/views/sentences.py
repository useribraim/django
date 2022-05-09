from first.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View

def sentence_list(request):
    all_sentence_obj = Sentence.objects.all()
    lst = []
    for i in all_sentence_obj:
        current = {
        'PK': i.pk,
        'ID': i.ID,
        'doc_position': i.doc_position,
        'text': i.text,
        #'document_ID': i.document_ID
        }
        lst.append(current)
    return render(request, 'first/sentences/sentences_list.html', {'context': lst})

def sentence_view(request, detail_view_id):
    sentence = Sentence.objects.get(pk=detail_view_id)
    current = {
        'Type': 'Предложение',
        'ID': sentence.ID,
        'document_position': sentence.doc_position,
        'text': sentence.text,
        }

    #Sentence Choice Dictionary
    sen_dict = {}
    for s in Sentence.objects.all():
        sen_dict[s] = s.pk

    url = str(detail_view_id)
        
    for doc in Document.objects.all():
        if doc.file_name == str(sentence.ID):
            doc_data = {
            'type': 'Документ',
            'file_name': doc.file_name,
            'author': doc.author,
            'language_id': doc.language_ID,
            }

    ##############################
    choice = Document.objects.all()
    arr = []
    for item in choice:
        var = {
            'id': item.pk,
            'value': item
        }
        arr.append(var)
    ###########################
    
    if request.POST.get('action') == 'Delete':
        sentence.delete()
        return redirect('sentences')
    elif request.POST.get('action') == 'Edit':
        return redirect(url + '/change')
    return render(request, 'first/sentences/sentence_view_ajax.html', {'context': current, 'sentence_list': sen_dict, 'url': url, 'doc_data': doc_data})
    #, 'doc_data': doc_data

def sentence_add(request):
    url = "sentences"
    choice = Document.objects.all()
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

    
    for doc in Document.objects.all():
        if doc.pk == int(number):
            sentence = Sentence(
            #Choice Menu
            ID = doc,
            doc_position = request.POST.get('doc_position'),
            text = request.POST.get('text'),
            document_ID = request.POST.get('document_id')
            )
            sentence.save()
            return redirect(url)
    return render(request, 'first/sentences/sentence_add_ajax.html', {'context': url, 'choices': arr})

def sentence_change(request, detail_view_id):
    url = '/documents/' + str(detail_view_id)
    sentence = Sentence.objects.get(pk=detail_view_id)
    #######
    choice = Document.objects.all()
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
        sentence.delete()
        return redirect('/sentences')
    

    if request.POST.get('action') == 'Save':
        for doc in Document.objects.all():
            if doc.pk == int(number):
                sentence.ID = doc
                sentence.doc_position = request.POST.get('file_name')
                sentence.text = request.POST.get('author')
                sentence.save()
        return redirect('/sentences')

    obj = Sentence.objects.get(pk=detail_view_id)
    current = {
    'type': 'Предложение',
    'doc_position': obj.doc_position,
    'text': obj.text,
    'document_id': obj.document_ID
    }

    return render(request, 'first/sentences/sentence_change_ajax.html', {'context': current, 'choices': arr})
