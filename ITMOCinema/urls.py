"""ITMOCinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
	path('',views.aboutCinemas, name='home'),
    path('aboutCinema/<str:id>',views.aboutCinema, name='aboutCinema'),
    path('aboutFilm/<str:id>', views.aboutFilm, name='aboutFilm'),
    path('login/', views.login, name='login'),
    path('login/addCinema', views.addCinema, name='addCinema'),
    path('login/addFilm', views.addFilm, name='addFilm'),
    path('login/addDir', views.addDir, name='addDir'),
    path('login/addActs', views.addActs, name='addActs'),
    path('login/addSessions', views.addSessions, name='addSessions'),
    path('login/addModer', views.addModer, name='addModer'),
    path('login/delCinema', views.delCinema, name='delCinema'),
    path('login/delFilm', views.delFilm, name='delFilm'),
    path('login/delDir', views.delDir, name='delDir'),
    path('login/delActor', views.delActor, name='delActor'),
    path('login/delSession', views.delSession, name='delSession'),
    path('login/delModer', views.delModer, name='delModer'),
    path('admin/', admin.site.urls)
]
