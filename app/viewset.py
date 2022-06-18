from rest_framework import generics

from app.models import Currency

# from .permissions import IsOwnerOrReadOnly
from .serializers import CurrencySerializer


class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyCreateView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class CurrencyDetailView(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class CurrencyUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = (IsOwnerOrReadOnly,)


class CurrencyDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = (IsOwnerOrReadOnly,)
