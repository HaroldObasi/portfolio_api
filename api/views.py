from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import MessageSerializer, ProjectSerializer
from .models import Message, Project
from .aws_methods import list_resources, put_image, upload_file_to_folder
# Create your views here.

class MessagesListView (generics.ListCreateAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer

  def perform_create(self, serializer):
    return Response({"message": "good"})

class ProjectListCreateView (generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

  def perform_create(self, serializer):
    serializer.data['images'] = "new field init"
    print(serializer.data)
    serializer.save()
    content = { 
      'name': 'successful request'
    }
    
    return Response(content)


class CreateProject(APIView):

  def get(self, request): 
    content = {
      "message": "all is good"
    }
    return Response(content)

  def post(self, request):
    title = request.data.get('title').lower()
    skills = request.data.get('skills')
    images_list = request.data.get('images').split()
    description = request.data.get('description')

    project = request.data
    obj_name = title.split()
    image_urls = []

    for image in images_list:
      image_urls.append(upload_file_to_folder(title, image))
  
    project["images"] = " ".join(image_urls)
    print("Project data to save: ", project)


    serializer = ProjectSerializer(data = project)

    if serializer.is_valid(raise_exception=True):
      saved_project = serializer.save()

    return Response({"message": "success"})

class ExampleView(APIView):
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = []

  def get(self, request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)


class TestingUploadView(APIView):
  def post(self, request):
 
    image_stream = request.data.get('image')

    if image_stream[0:15] == "data:image/jpeg":
      file_type = "jpg"
    else: 
      file_type = "png"

    # res = put_image("trying_extension2", source_data = image_stream, file_ext= file_type)
    img_url = upload_file_to_folder("portfolio project", image_stream)
    return Response({"file path": img_url})