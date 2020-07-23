
from django.contrib import admin
from django.urls import path,include

from api.views import ApiOverView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ApiOverView),
    path('api/', include('api.urls')),

]
