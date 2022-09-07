from rest_framework import serializers
from app_api.models import Document, Sentence, Clause, Syntaxeme, Wordform

# class DocumentSerializer(serializers.Serializer):
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Document.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance = False
#         return instance

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['file_name', 'author', 'language_ID']

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['ID', 'doc_position', 'text', 'document_ID']

class ClauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clause
        fields = ['ID', 'text', 'sentence_ID', 'frame_ID']

class SyntaxemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syntaxeme
        fields = ['ID', 'clause_ID']

class WordformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordform
        fields = ['ID', 'syntaxeme_ID', 'frame_role_ID', 'position_in_document'
        , 'position_in_sentence', 'clause_position', 'text', 'root_morpheme_ID']
