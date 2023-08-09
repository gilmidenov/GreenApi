from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from GreenApi import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('getsettings/', views.getsettings, name='getsettings'),
    path('GetStateInstance/', views.getstateinstance, name='GetStateInstance'),
    path('sendMessage/', views.sendmessage, name='sendMessage'),
    path('sendFileByUrl/', views.sendfilebyurl, name='sendFileByUrl'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)