from django.urls import path
from . import views
urlpatterns = [
    path('emp', views.emp, name='emp'),  
    path('show',views.show, name='show'),    
    path('update/<int:id>', views.update,name='detail'),  
    path('delete/<int:id>', views.destroy,name='delete'), 
]