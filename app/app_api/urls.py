from django.urls import path
from app_api import views

urlpatterns = [
    # path('example/', views.example),
    path('documents/', views.document_list),
    path('documents/<int:pk>', views.document_detail),
    path('sentences/', views.sentence_list),
    path('sentences/<int:pk>', views.sentence_detail),
    path('clauses/', views.clause_list),
    path('clauses/<int:pk>', views.clause_detail),
    path('syntaxemes/', views.syntaxeme_list),
    path('syntaxemes/<int:pk>', views.syntaxeme_detail),
    path('wordforms/', views.wordform_list),
    path('wordforms/<int:pk>', views.wordform_detail),
]