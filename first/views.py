from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
import json
from .forms import StudentForm





class DocumentView(View):
    def document_list(request):
        url = '/apps/first/documents/add'
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
        return render(request, 'first/documents_list.html', {'context': lst, 'url': url})

    def document_view(request, detail_view_id = 0):
        print(request.POST)
        url = '/apps/first/documents/' + str(detail_view_id)
        doc = Document.objects.get(pk=detail_view_id)
        current = {
            'Type': 'Документ',
            'File Name': doc.file_name,
            'Author': doc.author,
            'Language_ID': doc.language_ID,
            }
        if request.POST.get('action') == 'Delete':
            doc.delete()
            print("its working")
            return redirect('/apps/first/documents')
        elif request.POST.get('action') == 'Edit':
            return redirect(url + '/change')

        return render(request, 'first/document_view_ajax.html', {'context': current, 'url': url})

    def document_add(request):
        url = '/apps/first/documents/add'
        if request.POST.get('action') == 'Save':
            doc = Document(
                file_name = request.POST.get('file_name'),
                author = request.POST.get('author'),
                language_ID = request.POST.get('language_id')
                )
            doc.save()
            return redirect('/apps/first/documents')
        return render(request, 'first/document_add_ajax.html', {'context': url})

    def document_change(request, detail_view_id):
        url = '/apps/first/documents/' + str(detail_view_id)
        doc = Document.objects.get(pk=detail_view_id)

        if request.POST.get('action') == 'Delete':
            doc.delete()
            return redirect('/apps/first/documents')

        if request.POST.get('action') == 'Save':
            doc.file_name = request.POST.get('file_name')
            doc.author = request.POST.get('author')
            doc.language_ID = request.POST.get('language_id')
            doc.save()
            print("DONE!")
            return redirect('/apps/first/documents')

        current = {
            'Type': 'Документ',
            'file_name': doc.file_name,
            'author': doc.author,
            'language_id': doc.language_ID,
            }
        return render(request, 'first/document_change_ajax.html', {'context': current, 'text': url})


class SentenceView(View):
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
        return render(request, 'first/sentences_list.html', {'context': lst})

    def sentence_view(request, detail_view_id):
        url = '/apps/first/sentences/' + str(detail_view_id)
        sentence = Sentence.objects.get(pk=detail_view_id)
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
        current = {
            'Type': 'Предложение',
            'ID': sentence.ID,
            'document_position': sentence.doc_position,
            'text': sentence.text,
            #Document ID ??
            }
        if request.POST.get('action') == 'Delete':
            sentence.delete()
            return redirect('/apps/first/sentences')
        elif request.POST.get('action') == 'Edit':
            return redirect(url + '/change')
        return render(request, 'first/sentence_view_ajax.html', {'context': current, 'choices': arr, 'url': url})

    def sentence_add(request):
        url = "/apps/first/sentences"
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
        return render(request, 'first/sentence_add_ajax.html', {'context': url, 'choices': arr})
    
    def sentence_change(request, detail_view_id):
        url = '/apps/first/documents/' + str(detail_view_id)
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
            return redirect('/apps/first/sentences')
        

        if request.POST.get('action') == 'Save':
            for doc in Document.objects.all():
                if doc.pk == int(number):
                    sentence.ID = doc
                    sentence.doc_position = request.POST.get('file_name')
                    sentence.text = request.POST.get('author')
                    sentence.save()
            return redirect('/apps/first/sentences')

        obj = Sentence.objects.get(pk=detail_view_id)
        current = {
        'type': 'Предложение',
        'doc_position': obj.doc_position,
        'text': obj.text,
        'document_id': obj.document_ID
        }

        return render(request, 'first/sentence_change_ajax.html', {'context': current, 'choices': arr})


class ClauseView(View):
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
        return render(request, 'first/clauses.html', {'context': lst})

    def clause_add(request):
        url = "/apps/first/clauses"
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
        url = '/apps/first/clauses/' + str(detail_view_id)
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
            return redirect('/apps/first/clauses')
        

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
        url = '/apps/first/clauses/' + str(detail_view_id)
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


class SyntaxemeView(View):
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
        url = "/apps/first/syntaxemes"
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

        return render(request, 'first/syntaxemes/syntaxeme_change_ajax.html', {'context': current, 'choices': arr})

    def syntaxeme_view(request, detail_view_id):
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
        return render(request, 'first/syntaxemes/syntaxeme_view_ajax.html', {'context': current, 'choices': arr, 'url': url})


class WordformView(View):
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




    





def handle_uploaded_file(f):  
    with open('first/files/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"first/upload.html",{'form':student})  





def example(request, slug, detail_view_id):
    #Удаляем последний символ
    slug = slug[:len(slug)-1]
    slug = slug.title()
    # current = {
    #     'file_name': 'hello',
    #     'author': 'Paul',
    #     'language_ID': 'Di'
    #     }
    if slug == 'Document':
        obj = Document.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Документ',
        'File Name': obj.file_name,
        'Author': obj.author,
        'Language_ID': obj.language_ID
        }
    elif slug == 'Clause':
        obj = Clause.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Клауза',
        'ID': obj.ID,
        'Text': obj.text,
        'Sentence_ID': obj.sentence_ID,
        'Frame_ID': obj.frame_ID
        }
    elif slug == 'Sentence':
        obj = Sentence.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Предложение',
        'Doc Position': obj.doc_position,
        'Text': obj.text,
        'Document_ID': obj.document_ID
        }
    elif slug == 'Syntaxeme':
        obj = Syntaxeme.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Синтаксема',
        'ID': obj.ID,
        'Clause_ID': obj.clause_ID
        }
    elif slug == 'Wordform':
        obj = Wordform.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Словоформа',
        'ID': obj.ID,
        'Syntaxeme_ID': obj.syntaxeme_ID,
        'Frame_role_ID': obj.frame_role_ID,
        'Position_in_document': obj.position_in_document,
        'Position_in_sentence': obj.position_in_sentence,
        'Clause_position': obj.clause_position,
        'Text': obj.text,
        'Root_morpheme_ID': obj.root_morpheme_ID
        }


    return current
def detail_view(request, slug, detail_view_id):
    if slug == 'documents':
        obj = Document.objects.get(pk=detail_view_id)
    elif slug == 'clauses':
        obj = Clause.objects.get(pk=detail_view_id)
    elif slug == 'sentences':
        obj = Sentence.objects.get(pk=detail_view_id)
    elif slug == 'syntaxemes':
        obj = Syntaxeme.objects.get(pk=detail_view_id)
    elif slug == 'wordforms':
        obj = Wordform.objects.get(pk=detail_view_id)

    # #EDIT AND DELETE кнопки в DETAIL VIEW
    # if request.GET.get('change'):
    if request.GET:
        if "delete" in request.GET:
            obj.delete()
            return HttpResponseRedirect(f'/home/apps/first/{slug}')
        if "Edit" in request.GET.get('change'):
            return HttpResponseRedirect(f'/home/apps/first/{slug}/{detail_view_id}/change')



    if slug == 'documents':
        obj = Document.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Документ',
        'File Name': obj.file_name,
        'Author': obj.author,
        'Language_ID': obj.language_ID
        }
    elif slug == 'clauses':
        obj = Clause.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Клауза',
        'ID': obj.ID,
        'Text': obj.text,
        'Sentence_ID': obj.sentence_ID,
        'Frame_ID': obj.frame_ID
        }
    elif slug == 'sentences':
        obj = Sentence.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Предложение',
        'Doc Position': obj.doc_position,
        'Text': obj.text,
        'Document_ID': obj.document_ID
        }
    elif slug == 'syntaxemes':
        obj = Syntaxeme.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Синтаксема',
        'ID': obj.ID,
        'Clause_ID': obj.clause_ID
        }
    elif slug == 'wordforms':
        obj = Wordform.objects.get(pk=detail_view_id)
        current = {
        'Type': 'Словоформа',
        'ID': obj.ID,
        'Syntaxeme_ID': obj.syntaxeme_ID,
        'Frame_role_ID': obj.frame_role_ID,
        'Position_in_document': obj.position_in_document,
        'Position_in_sentence': obj.position_in_sentence,
        'Clause_position': obj.clause_position,
        'Text': obj.text,
        'Root_morpheme_ID': obj.root_morpheme_ID
        }
    return render(request, 'first/table_view.html', {'context': current})
def change(request, slug, detail_view_id):
    var = request.GET.getlist('search')
    print(var)
    if len(var):
        if slug == 'documents':
            obj = Document.objects.get(pk=detail_view_id)
            obj.file_name = var[1]
            obj.author = var[2]
            obj.language_ID = var[3]
            obj.save()
            next = request.GET.get('next', '/home/apps/first/'+slug)
            return HttpResponseRedirect(next)
        elif slug == 'clauses':
            obj = Clause.objects.get(pk=detail_view_id)
            obj.text = var[1]
            obj.sentence_ID = var[2]
            obj.frame_ID = var[3]
            obj.save()
            next = request.GET.get('next', '/home/apps/first/'+slug)
            return HttpResponseRedirect(next)
        elif slug == 'sentences':
            obj = Sentence.objects.get(pk=detail_view_id)
            obj.doc_position = var[1]
            obj.text = var[2]
            obj.document_ID = var[3]
            obj.save()
            next = request.GET.get('next', '/home/apps/first/'+slug)
            return HttpResponseRedirect(next)
        elif slug == 'syntaxemes':
            obj.clause_ID = var[1]
            obj.save()
            next = request.GET.get('next', '/home/apps/first/'+slug)
            return HttpResponseRedirect(next)
            obj = Syntaxeme.objects.get(pk=detail_view_id)
        elif slug == 'wordforms':
            obj = Wordform.objects.get(pk=detail_view_id)




    current = example(request, slug, detail_view_id)
    print('CHECK')
    return render(request, 'first/document_change.html', {'context': current})

def add(request, slug):
    obj = ''
    if slug == 'sentences':
        obj = Document.objects.all()
    elif slug == 'clauses':
        obj = Sentence.objects.all()
    elif slug == 'syntaxemes':
        obj = Clause.objects.all()
    elif slug == 'wordforms':
        obj = Syntaxeme.objects.all()

    if request.GET.get('add') and slug == 'documents':
        q = request.GET.getlist('add')
        doc = Document(file_name = q[0], author = q[1], language_ID = q[2])
        doc.save()
        return HttpResponseRedirect(f'/home/apps/first/{slug}')
    elif request.GET.get('add') and slug == 'sentences':
        q = request.GET.getlist('add')
        number = ''
        #Взять из запроса Число
        for word in q[0]:
            if word.isdigit():
                number += word

        for doc in Document.objects.all():
            if doc.pk == int(number):
                s = Sentence(ID = doc, doc_position = q[1], text = q[2], document_ID = q[3])
                s.save()
        return HttpResponseRedirect(f'/home/apps/first/{slug}')

    elif request.GET.get('add') and slug == 'clauses':
        q = request.GET.getlist('add')
        number = ''
        for letter in q[0]:
            if letter.isdigit():
                number += letter
        for doc in Sentence.objects.all():
            if doc.pk == int(number):
                c = Clause(ID = doc, text = q[1], sentence_ID = q[2], frame_ID = q[3])
                c.save()
        return HttpResponseRedirect(f'/home/apps/first/{slug}')

    elif request.GET.get('add') and slug == 'syntaxemes':
        q = request.GET.getlist('add')
        number = ''
        for letter in q[0]:
            if letter.isdigit():
                number += letter
        for doc in Clause.objects.all():
            if doc.pk == int(number):
                s = Syntaxeme(ID = doc, clause_ID = q[1])
                s.save()
        return HttpResponseRedirect(f'/home/apps/first/{slug}')


    return render(request, "first/add.html", {'choice': obj, 'context': slug})

def documents(request):

    #Обработка Запроса Add
    if request.GET.get('add'):
        return HttpResponseRedirect(f'documents/add')
    # elif request.GET.get('search'):
    #     return HttpResponseRedirect(f'documents/{detail_view_id}/change')

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

    return render(request, 'first/documents.html', {'context': lst})

def clauses(request):
    #Обработка Запроса Add
    if request.GET.get('add'):
        return HttpResponseRedirect(f'clauses/add')

    all_clauses_obj = Clause.objects.all()
    lst = []
    for i in all_clauses_obj:
        current = {
        'PK': i.pk,
        'ID': i.ID,
        'Text': i.text,
        'Sentence_ID': i.sentence_ID,
        'Frame_ID': i.frame_ID
        }
        lst.append(current)
    return render(request, 'first/clauses.html', {'context': lst})

def sentences(request):
    if request.GET.get('add'):
        return HttpResponseRedirect(f'sentences/add')

    all_sentence_obj = Sentence.objects.all()
    lst = []
    for i in all_sentence_obj:
        current = {
        'PK': i.pk,
        'ID': i.ID,
        'doc_position': i.doc_position,
        'text': i.text,
        'document_ID': i.document_ID
        }
        lst.append(current)
    return render(request, 'first/sentences.html', {'context': lst})

def syntaxemes(request):

    if request.GET.get('add'):
        return HttpResponseRedirect(f'syntaxemes/add')

    all_syntaxemes_obj = Syntaxeme.objects.all()
    lst = []
    for i in all_syntaxemes_obj:
        current = {
        'PK': i.pk,
        'ID': i.ID,
        'clause_ID': i.clause_ID,
        }
        lst.append(current)
    return render(request, 'first/syntaxemes.html', {'context': lst})

def wordforms(request):
    if request.GET.get('add'):
        return HttpResponseRedirect(f'wordforms/add')

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
    return render(request, 'first/wordforms.html', {'context': lst})