from django.urls import path
from web.views import home,subscribe


app_name ="web"


urlpatterns = [
    path("",home,name="home"),
    path ("subscribe",subscribe,name="subscribe"),
    
]