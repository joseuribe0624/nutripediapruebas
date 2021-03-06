"""historias_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static


def trigger_error(request):
    1 / 0


urlpatterns = (
    [
        url(
            "",
            include(("historias_server.stats.urls", "stats"), namespace="estadisticas"),
        ),
        path("admin/", admin.site.urls),
        path("accounts/", include("allauth.urls")),
        path(
            "usuarios/",
            include(("historias_server.user.urls", "usuarios"), namespace="usuarios"),
        ),
        path(
            "",
            include(
                ("historias_server.historias.urls", "historias"), namespace="historias"
            ),
        ),
        path(
            "",
            include(
                ("historias_server.alimentacion.urls", "alimentacion"),
                namespace="alimentacion",
            ),
        ),
        path(
            "",
            include(
                ("historias_server.medicacion.urls", "medicacion"),
                namespace="medicacion",
            ),
        ),
        path("sentry-debug/", trigger_error),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
