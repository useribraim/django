# from django.shortcuts import render
# from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_api.models import Document, Sentence, Clause, Syntaxeme, Wordform
from app_api.serializers import DocumentSerializer, SentenceSerializer, ClauseSerializer, SyntaxemeSerializer, WordformSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status

@api_view(['GET', 'POST'])
def document_list(request):
    if request.method == 'GET':
        docs = Document.objects.all()
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def document_detail(request, pk):
    try:
        document = Document.objects.get(pk=pk)
    except document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def sentence_list(request):
    if request.method == 'GET':
        s = Sentence.objects.all()
        serializer = SentenceSerializer(s, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SentenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sentence_detail(request, pk):
    try:
        s = Sentence.objects.get(pk=pk)
    except s.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SentenceSerializer(s)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SentenceSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def clause_list(request):
    if request.method == 'GET':
        s = Clause.objects.all()
        serializer = ClauseSerializer(s, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClauseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def clause_detail(request, pk):
    try:
        s = Clause.objects.get(pk=pk)
    except s.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClauseSerializer(s)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClauseSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def syntaxeme_list(request):
    if request.method == 'GET':
        s = Syntaxeme.objects.all()
        serializer = SyntaxemeSerializer(s, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Syntaxeme(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def syntaxeme_detail(request, pk):
    try:
        s = Syntaxeme.objects.get(pk=pk)
    except s.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SyntaxemeSerializer(s)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SyntaxemeSerializer(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        s.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def wordform_list(request):
    if request.method == 'GET':
        w = Wordform.objects.all()
        serializer = WordformSerializer(w, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Syntaxeme(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def wordform_detail(request, pk):
    try:
        w = Wordform.objects.get(pk=pk)
    except w.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordformSerializer(w)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordformSerializer(w, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        w.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)