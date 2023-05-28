from .models import TaskModel
from .serializer import TaskSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class TaskAPIView(APIView):

    #DOCUMENTATION THE API GET
    @swagger_auto_schema(
        responses={200: TaskSerializer(many=True)},
        operation_description='Descripción de la operación GET'
    )

    #METHOD GET VIEWS LIST TASK
    def get(self, request):
        """
        Descripción general de la vista.
        """
        task = TaskModel.objects.all()
        task_serializer = TaskSerializer(task, many=True)
        return Response(task_serializer.data, status=status.HTTP_200_OK)

    #DOCUMENTATION API POST
    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={201: TaskSerializer()},
        operation_description='Descripción de la operación POST'
    )
    #METHOD POST CREAT NEW TASK
    def post(self, request):
        """
        Descripción general de la vista.
        """
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    
    #DOCUMENTATION THE API GET
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description='ID de la tarea', type=openapi.TYPE_INTEGER),
        ],
        responses={200: TaskSerializer()},
        operation_description='Descripción de la operación GET'
    )

    #METHOD GET VIEWS LIST TASK
    def get(self, request, pk=None):
        """
        Descripción general de la vista.
        """
        task = TaskModel.objects.filter(id=pk).first()
        if task:
            task_serializer = TaskSerializer(task)
            return Response(task_serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No se encontró ninguna tarea con ese nombre'}, status=status.HTTP_400_BAD_REQUEST)

    #DOCUMENTATION THE API PUT
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description='ID de la tarea', type=openapi.TYPE_INTEGER),
        ],
        request_body=TaskSerializer,
        responses={200: TaskSerializer()},
        operation_description='Descripción de la operación PUT'
    )

    #METHOD PUT UPDATE TASK
    def put(self, request, pk=None):
        """
        Descripción general de la vista.
        """
        task = TaskModel.objects.filter(id=pk).first()
        if task:
            task_serializer = TaskSerializer(task, data=request.data)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response(task_serializer.data, status=status.HTTP_200_OK)
            return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'No se encontró ninguna tarea con ese nombre'}, status=status.HTTP_400_BAD_REQUEST)

    #DOCUMENTATION THE API DELETE
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description='ID de la tarea', type=openapi.TYPE_INTEGER),
        ],
        responses={200: 'OK'},
        operation_description='Descripción de la operación DELETE'
    )

    #METHOD DELETE , DELETE TASK    
    def delete(self, request, pk=None):
        """
        Descripción general de la vista.
        """
        task = TaskModel.objects.filter(id=pk).first()
        if task:
            task.delete()
            return Response({'message': 'Tarea eliminada correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'No se encontró ninguna tarea con ese nombre'}, status=status.HTTP_400_BAD_REQUEST)