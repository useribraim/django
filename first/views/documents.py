from first.models import *
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View


def document_list(request):
    url = 'documents/add'
    all_document_obj = Document.objects.all()
    lst = []
    for i in all_document_obj:
        current = {
        'PK': i.pk,
        'file_name': i.file_name,
        'author': i.author,
        'language_ID': i.language_ID
        }
        lst.append(current)
    return render(request, 'first/documents/documents_list.html', {'context': lst, 'url': url})

def document_view(request, detail_view_id = 0):
    doc = Document.objects.get(pk=detail_view_id)
    current = {
        'Type': 'Документ',
        'File Name': doc.file_name,
        'Author': doc.author,
        'Language_ID': doc.language_ID,
        }
    if request.POST.get('action') == 'Delete':
        doc.delete()
        return redirect(reverse("document_list"))
    elif request.POST.get('action') == 'Edit':
        return redirect(f'{detail_view_id}/change')
    return render(request, 'first/documents/document_view.html', {'context': current})

def document_add(request):
    if request.method == 'POST':
        doc = Document(
            file_name = request.POST.get('file_name'),
            author = request.POST.get('author'),
            language_ID = request.POST.get('language_id')
            )
        doc.save()
        return redirect('/documents')
        #return redirect(reverse("document_list"))
    return render(request, 'first/documents/document_add.html')

def document_change(request, detail_view_id):
    print(request.POST)
    doc = Document.objects.get(pk=detail_view_id)
    current = {
        'Type': 'Документ',
        'file_name': doc.file_name,
        'author': doc.author,
        'language_id': doc.language_ID,
        }
    print(request.method)
    if request.method == 'DELETE':
        doc.delete()
        return redirect(reverse("document_list"))
    if request.method == 'POST':
        doc.file_name = request.POST.get('file_name')
        doc.author = request.POST.get('author')
        doc.language_ID = request.POST.get('language_id')
        doc.save()
        return redirect(reverse("document_list"))
    return render(request, 'first/documents/document_change_ajax.html', {'context': current})