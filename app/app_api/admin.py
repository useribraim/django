from django.contrib import admin
from app_api.models import Document, Sentence, Clause, Syntaxeme, Wordform
# Register your models here.

admin.site.register(Document)
admin.site.register(Sentence)
admin.site.register(Clause)
admin.site.register(Syntaxeme)
admin.site.register(Wordform)
