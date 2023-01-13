
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from accounting import views

register_router = DefaultRouter()
register_router.register('register', views.UserListCreate)

schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v0.1',
      description="API для интернет магазина",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),

    path('api/register/', include(register_router.urls)),
    path('api/position/', views.PositionListCreateAPIView.as_view(), name='position'),
    path('api/position/<int:pk>/', views.PositionRetrieveUpdateDestroyAPIView.as_view(), name='pos_update'),
    path('api/employee/', views.EmployeeListCreateAPIView.as_view(), name='employee'),
    path('api/employee/<int:pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='em_update'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),

]
