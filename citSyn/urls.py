from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CitationViewSet, SynopsisViewSet, RegisterView, ChallengeViewSet, VitesseViewSet
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Création d'un routeur pour gérer les routes automatiquement pour les ViewSets
router = DefaultRouter()
router.register(r'citations', CitationViewSet)
router.register(r'synopsis', SynopsisViewSet)
router.register(r'challenges', ChallengeViewSet)
router.register(r'vitesse', VitesseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Inclure les routes du routeur dans le namespace 'api/'
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/register/', RegisterView.as_view(), name='register'),
]

