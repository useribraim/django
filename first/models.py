from django.db import models

class Document(models.Model):
    file_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    language_ID = models.CharField(max_length=50)

    def __str__(self):
        return self.file_name
class Sentence(models.Model):
    ID = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )
    doc_position = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    document_ID = models.CharField(max_length=50)
    def __str__(self):
        return self.text


class Clause(models.Model):
    ID = models.ForeignKey(
        Sentence,
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=50)
    sentence_ID = models.CharField(max_length=50)
    frame_ID = models.CharField(max_length=50)
    def __str__(self):
        return self.text

class Syntaxeme(models.Model):
    ID = models.ForeignKey(
        Clause,
        on_delete=models.CASCADE,
    )
    clause_ID = models.CharField(max_length=50)
    def __str__(self):
        return self.ID


class Wordform(models.Model):
    ID = models.ForeignKey(
        Syntaxeme,
        on_delete=models.CASCADE,
    )
    syntaxeme_ID = models.CharField(max_length=50)
    frame_role_ID = models.CharField(max_length=50)
    position_in_document = models.CharField(max_length=50)
    position_in_sentence = models.CharField(max_length=50)
    clause_position = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    root_morpheme_ID = models.CharField(max_length=50)



