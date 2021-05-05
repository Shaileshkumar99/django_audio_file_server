from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from .models import Song, Podcast, Audiobook
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import HttpResponse

# Create your views here.

@api_view(['GET', 'POST'])
def Audio(request):

    if request.method == 'GET':
        song = Song.objects.all()
        song_data = SongSerializer(song, many=True)

        podcast = Podcast.objects.all()
        podcast_data = PodcastSerializer(podcast, many=True)


        audiobook = Audiobook.objects.all()
        audiobook_data = AudiobookSerializer(audiobook, many=True)

        return Response({"Song": song_data.data, "Podcast": podcast_data.data, "Audiobook": audiobook_data.data })

    elif request.method == 'POST':
        if request.data['audioFileType'] == 'Song' or 'song':
            serializer = SongSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.data['audioFileType'] == 'Podcast' or 'podcast':
            serializer = PodcastSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.data['audioFileType'] == 'Audiobook' or 'audiobook':
            serializer = AudiobookSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"Error": "Please Enter Correct Audiotype" } , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Audio_detail(request, audioFileTyp, audioFileID):

    if audioFileTyp not in  ['Song', 'Podcast', 'Audiobook']:
        return Response({"Error": "Audio Type Not Found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        if audioFileTyp == 'Song':
            audio = Song.objects.get(pk=audioFileID)

        elif audioFileTyp == 'Podcast':
            audio = Podcast.objects.get(pk=audioFileID)

        elif audioFileTyp == 'Audiobook':
            audio = Audiobook.objects.get(pk=audioFileID)


    except:
        return Response({"Error": "Audio Detail Found"}, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        if audioFileTyp == 'Song':
            serializer = SongSerializer(audio)

        elif audioFileTyp == 'Podcast':
            serializer = PodcastSerializer(audio)

        elif audioFileTyp == 'Audiobook':
            serializer = AudiobookSerializer(audio)

        return Response(serializer.data)

    elif request.method == 'PUT':

        if audioFileTyp == 'Song':
            serializer = SongSerializer(audio, data=request.data)

        elif audioFileTyp == 'Podcast':
            serializer = PodcastSerializer(audio, data=request.data)

        elif audioFileTyp == 'Audiobook':
            serializer = AudiobookSerializer(audio, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        audio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Audio_get(request, audioFileTyp):
    if request.method == 'GET':

        if audioFileTyp == "Song":
            song = Song.objects.all()
            song_data = SongSerializer(song, many=True)

            return Response(song_data.data)

        elif audioFileTyp == "Podcast":
            podcast = Podcast.objects.all()
            podcast_data = PodcastSerializer(podcast, many=True)

            return Response(podcast_data.data)

        elif audioFileTyp == "Audiobook":
            audiobook = Audiobook.objects.all()
            audiobook_data = AudiobookSerializer(audiobook, many=True)

            return Response(audiobook_data.data)






