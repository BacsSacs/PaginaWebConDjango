"""
URL configuration for webpersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portafolio import views as portfolio_views


from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.home,name="home"),
    path('about/',core_views.About,name="about"),
    path('portfolio/',portfolio_views.Portafolio,name="portfolio"),
    path('contact/',core_views.Contacto,name="contact"),
]

# Si estamos en modo desarrollador, importamos la configuración
# extendida para que en el panel administrador se puedan
# descargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    # Si alguien intenta acceder al fichero(imagen), le sirva
    # o se la deje ver
    # al urlpatterns lo modificamos para pasarle la raiz de los 
    # ficheros media
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
