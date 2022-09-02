from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.index,name="index"),
    path('signin',views.signin,name="signin"),
    path('logout/',views.logout,name="logout"),
    path('base/',views.base,name="base"),
  
    path('inventory/',views.Inventory,name="inventory"),
   
    path('dashboard/',views.dashboard,name="dashboard"),

     #CREATE
    path('create/',views.data_form,name='data_create'),
    #READ
    path('data/',views.data_read,name='data_read'),
    #UPDATE
    path('<int:id>',views.data_form,name='data_update'),
    #DELETE
    path('data_delete/<str:candidate_id>/',views.data_delete,name='data_delete'),
    

    
   
    
    

]