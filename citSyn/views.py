from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Citation, Synopsis, CustomUser, Challenge, Vitesse
from .serializers import CitationSerializer, SynopsisSerializer, CustomUserSerializer, ChallengeSerializer, VitesseSerializer

class CustomPagination(PageNumberPagination):
    page_size = 6  # Définit la taille de la page par défaut
    page_size_query_param = 'page_size'  # Permet à l'utilisateur de personnaliser la taille de la page
    max_page_size = 100  # Limite le nombre maximum d'éléments par page

class CitationViewSet(ModelViewSet):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    pagination_class = CustomPagination  # Utilise la pagination personnalisée

class SynopsisViewSet(ModelViewSet):
    queryset = Synopsis.objects.all()
    serializer_class = SynopsisSerializer
    pagination_class = CustomPagination  # Utilise la pagination personnalisée


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Créer l'utilisateur sans enregistrer pour hacher le mot de passe
        user = CustomUser(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
        )
        user.set_password(serializer.validated_data['password'])  # Hachage du mot de passe
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    pagination_class = CustomPagination  # Utilise la pagination personnalisée

class VitesseViewSet(ModelViewSet):
    queryset = Vitesse.objects.all()
    serializer_class = VitesseSerializer
    pagination_class = CustomPagination  # Utilise la pagination personnalisée
