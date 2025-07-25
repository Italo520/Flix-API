from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/v1/', include('autenticacao.urls')),

    path('api/v1/', include('generos.urls')),

    path('api/v1/', include('filmes.urls')),

    path('api/v1/', include('atores.urls')),

    path('api/v1/', include('reviews.urls')),

]
