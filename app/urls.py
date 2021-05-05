from django.urls import path,include
from rest_framework import routers
from .views import Audio, Audio_detail, Audio_get

# router = routers.DefaultRouter()
# router.register(r'song', views.SongViewSet)
# router.register(r'podcast', views.PodcastViewSet)
# router.register(r'audiobook', views.AudiobookViewSet)

urlpatterns = [
        path('audio/', Audio),
        path('detail/<str:audioFileTyp>/<int:audioFileID>', Audio_detail),
        path('detail/<str:audioFileTyp>/', Audio_get),
]
