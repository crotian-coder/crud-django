from django.urls import path
from crud import views

urlpatterns = [
  
   path('',views.home,name = "home"),
   path('delete/<int:id>/',views.delete,name = "delete"),
   path('<int:id>/',views.Update,name = "update"),
]
