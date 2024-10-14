from django.urls import path
from app.views import homepage,about,hello, blogs,read,delete, create ,edit,signup,login,logout#or u use *for all
urlpatterns = [
    
      path('homepage', homepage ,name="home"),
      path('about', about, name="about"),
      path('hello/<cap>',hello, name="hello"),
      path('blogs',blogs,name="blogs"),
      path('read/<str:id>',read, name="read"),
      path('delete/<str:id>',delete, name="delete"),
      path('create',create,name="create"),
      path('edit/<str:id>',edit, name="edit"),
      path('signup',signup,name="signup"),
      path('logout',logout,name="logout"),
      
      path('login',login,name="login"),
      
]
