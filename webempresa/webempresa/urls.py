"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings # Importar la configuración de Django
 

urlpatterns = [
    # path de admin
    path('admin/', admin.site.urls),
    # path de core
    path('',include('core.urls')),
    # path de services
    path('services/',include('services.urls')),
    # path de blog
    path('blog/',include('blog.urls')),
]

if settings.DEBUG:# Si DEBUG es verdadero, se cargan los archivos estáticos
    from django.conf.urls.static import static # Importar la función static para servir archivos estáticos
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Añadir la ruta de los archivos estáticos a urlpatterns. settings.MEDIA_URL es la url de los archivos estáticos y settings.MEDIA_ROOT es la ruta de los archivos estáticos en el servidor. Esto es para poder ver las imágenes que subimos al servidor desde el admin de django.          
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Añadir la ruta de los archivos estáticos a urlpatterns. settings.STATIC_URL es la url de los archivos estáticos y settings.STATIC_ROOT es la ruta de los archivos estáticos en el servidor. Esto es para poder ver los archivos estáticos que subimos al servidor desde el admin de django. Esto no es necesario si usamos whitenoise para servir los archivos estáticos.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Añadir la ruta de los archivos estáticos a urlpatterns. settings.STATIC_URL es la url de los archivos estáticos y settings.STATIC_ROOT es la ruta de los archivos estáticos en el servidor. Esto es para poder ver los archivos estáticos que subimos al servidor desde el admin de django. Esto no es necesario si usamos whitenoise para servir los archivos estáticos.
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Añadir la ruta de los archivos estáticos a urlpatterns. settings.STATIC_URL es la url de los archivos estáticos y settings.STATIC_ROOT es la ruta de los archivos estáticos en el servidor. Esto es para poder ver los archivos estáticos que subimos al servidor desde el admin de django. Esto no es necesario si usamos whitenoise para servir los archivos estáticos.