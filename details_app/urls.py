from django.urls import path
from details_app import views
from .views import ListView,CreateView,EditView,UpdateView,DeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',ListView.as_view(),name='home'),
    path('form/',CreateView.as_view(),name='Create_new'),
    path('edits/<int:pk>/',EditView.as_view(),name='edits'),
    path('update_view/',UpdateView.as_view(),name='update_view'),
    path('delete_view/<int:pk>/',DeleteView.as_view(),name='delete')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
