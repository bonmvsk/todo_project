from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from ..models import ToDo
from ..serializers import ToDoSerializer

class ToDoListCreate(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.completed:
            raise PermissionDenied("ไม่สามารถแก้ไข ToDo ที่เสร็จสิ้นแล้วได้")
        return super().update(request, *args, **kwargs)
