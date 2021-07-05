from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name = 'holiday_planner'

urlpatterns = [
    path('', views.index, name="index"),
    path('all/', views.locations, name="all"),
    path('tag/<str:tag>/', views.tag, name="tag"),
    path('query/<str:queries>', views.query, name="query"),
    path('location/<int:pk>/', views.location, name="location"),
    path('query/', views.query, name="query"),
    path('visit/<int:pk>/', views.handle_visit, name="visit"),
    path("rem_visit/<int:pk>/", views.remove_visit, name='remove_visit'),
    path("delete_review/<int:pk>/", views.delete_review, name="delete_review"),
    path('favourite/<int:pk>/', views.favourite, name="favourite"),
    path('email/', views.email, name="email")
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

