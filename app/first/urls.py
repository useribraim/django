from django.contrib import admin
from django.urls import path, re_path
from first import views
from .views import *



urlpatterns = [
    path('', documents.document_list),
    path('example', example.foo),

    path('documents/upload', views.upload, name="file_upload"),

    path('documents', documents.document_list, name="document_list"),
    path('documents/add', documents.document_add, name="document_add"),
    path('documents/<int:detail_view_id>', documents.document_view, name="document_view"),
    path('documents/<int:detail_view_id>/change', documents.document_change, name="document_change"),

    path('sentences', sentences.sentence_list),
    path('sentences/add', sentences.sentence_add),
    path('sentences/<int:detail_view_id>', sentences.sentence_view),
    path('sentences/<int:detail_view_id>/change', sentences.sentence_change),

    path('clauses', clauses.clause_list),
    path('clauses/add', clauses.clause_add),
    path('clauses/<int:detail_view_id>', clauses.clause_view),
    path('clauses/<int:detail_view_id>/change', clauses.clause_change),


    path('syntaxemes', syntaxemes.syntaxeme_list),
    path('syntaxemes/add', syntaxemes.syntaxeme_add),
    path('syntaxemes/<int:detail_view_id>', syntaxemes.syntaxeme_view),
    path('syntaxemes/<int:detail_view_id>/change', syntaxemes.syntaxeme_change),

    path('wordforms', wordforms.wordform_list),
    path('wordforms/add', wordforms.wordform_add),
    path('wordforms/<int:detail_view_id>', wordforms.wordform_view),
    path('wordforms/<int:detail_view_id>/change', wordforms.wordform_change),

]