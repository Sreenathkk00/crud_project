"""
URL configuration for crud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from details_app import views
from .views import DetailListview,FormView,EditView

urlpatterns = [
    
    path('',DetailListview.as_view(),name='detail_list'),
    path('form/',FormView.as_view(),name='form_page'),
    
    path('edits/<int:pk>/',EditView.as_view(),name='edits'),
    
    
    

]
