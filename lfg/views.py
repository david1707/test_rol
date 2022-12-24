from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import LFG_Post
from .serializers import LFGSerializer


class LFGList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = LFG_Post.objects.all()
    serializer_class = LFGSerializer


class LFGDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = LFG_Post.objects.all()
    serializer_class = LFGSerializer
