
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from .serializers import LoginSerializer,UserSerializer,ContentSerializer,TagSerializer,ContentCreateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import *

@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)  
        refresh = RefreshToken.for_user(user)
        return Response({
            'status': 'success',
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'status': 'error', 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def refresh_token(request):
    refresh_token = request.data.get('refresh')
    try:
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)
        return Response({'access': access_token}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)
        



@login_required
@api_view(['POST'])
def create_snippet(request):
    serializer = ContentCreateSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    tag_title = serializer.validated_data.get('tag')
    created_by = request.user

    tag, _ = TagTable.objects.get_or_create(title=tag_title)
    snippet = ContentTable.objects.create(
        title=title,
        content=content,
        created_by=created_by,
        tag=tag
    )
    return Response({'message': 'Snippet saved successfully'}, status=201)
    


@api_view(['GET'])
def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(ContentTable, pk=snippet_id)
    serializer = ContentSerializer(snippet)
    return Response(serializer.data)



@api_view(['GET'])
def get_all_snippets(request):
    snippets = ContentTable.objects.all()
    snippet_count = snippets.count()
    
    snippet_data = []
    for snippet in snippets:
        snippet_url = reverse('snippet_detail', args=[snippet.id])
        snippet_data.append({
            'title': snippet.title,
            'detail_url': request.build_absolute_uri(snippet_url)
        })
    
    return Response({
        'total_snippets': snippet_count,
        'snippets': snippet_data
    })




@login_required
@api_view(['POST'])
def update_snippet(request, snippet_id):
    serializer = ContentCreateSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    title = request.data.get('title')
    content = request.data.get('content')
    tag_title = request.data.get('tag')
    
    snippet = get_object_or_404(ContentTable, pk=snippet_id)
    
    snippet.title = title
    snippet.content = content
    
    tag, _ = TagTable.objects.get_or_create(title=tag_title)
    snippet.tag = tag
    
    snippet.save()
    
    serializer = ContentSerializer(snippet)
    
    return Response(serializer.data)


@api_view(['POST'])
def delete_snippets(request):
    snippet_ids = request.data.get('ids', [])
    snippets = ContentTable.objects.filter(pk__in=snippet_ids)
    snippets.delete()

    remaining_snippets = ContentTable.objects.all()
    serializer = ContentSerializer(remaining_snippets, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def get_all_tags(request):
    tags = TagTable.objects.all()
    serializer = TagSerializer(tags, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def snippets_by_tag_id(request, tag_id):
    tag = get_object_or_404(TagTable, pk=tag_id)
    snippets = ContentTable.objects.filter(tag=tag)
    serializer = ContentSerializer(snippets, many=True)
    return Response(serializer.data)

