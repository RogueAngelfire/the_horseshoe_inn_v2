from django.urls import path
from . import views
from .views import PostList, PostDetail

app_name = 'bookings'

urlpatterns = [    
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
]