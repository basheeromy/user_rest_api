from django.urls import path, include
from rest_framework.routers import DefaultRouter


from profiles_api import views


router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls))
    
]
