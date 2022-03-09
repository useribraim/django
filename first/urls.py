from django.contrib import admin
from django.urls import path, re_path
from first import views
from first.views import DocumentView, SentenceView, ClauseView, SyntaxemeView, WordformView



urlpatterns = [
    path('foo', views.foo),

    path('apps/first/documents/upload', views.index),


    path('apps/first/documents', DocumentView.document_list),
    path('apps/first/documents/add', DocumentView.document_add),
    path('apps/first/documents/<int:detail_view_id>', DocumentView.document_view),
    path('apps/first/documents/<int:detail_view_id>/change', DocumentView.document_change),


    path('apps/first/sentences', SentenceView.sentence_list),
    path('apps/first/sentences/add', SentenceView.sentence_add),
    path('apps/first/sentences/<int:detail_view_id>', SentenceView.sentence_view),
    path('apps/first/sentences/<int:detail_view_id>/change', SentenceView.sentence_change),


    path('apps/first/clauses', ClauseView.clause_list),
    path('apps/first/clauses/add', ClauseView.clause_add),
    path('apps/first/clauses/<int:detail_view_id>', ClauseView.clause_view),
    path('apps/first/clauses/<int:detail_view_id>/change', ClauseView.clause_change),

    path('apps/first/syntaxemes', SyntaxemeView.syntaxeme_list),
    path('apps/first/syntaxemes/add', SyntaxemeView.syntaxeme_add),
    path('apps/first/syntaxemes/<int:detail_view_id>', SyntaxemeView.syntaxeme_view),
    path('apps/first/syntaxemes/<int:detail_view_id>/change', SyntaxemeView.syntaxeme_change),

    path('apps/first/wordforms', WordformView.wordform_list),
    path('apps/first/wordforms/add', WordformView.wordform_add),
    path('apps/first/wordforms/<int:detail_view_id>', WordformView.wordform_view),
    path('apps/first/wordforms/<int:detail_view_id>/change', WordformView.wordform_change),


    #path('apps/first/sentences/<int:detail_view_id>/change', SentenceView.sentence_change),
    #path('home/apps/first/<slug:slug>/add', views.add),
    #path('home/apps/first/<slug:slug>/<int:detail_view_id>', views.detail_view, name = 'detail_view'),
    
    

    
    #path('home/apps/first/<slug:slug>/<int:detail_view_id>/add', views.add),
    #path('home/apps/first/<slug:slug>/<int:detail_view_id>/change', views.change, name = 'change'),
       
]