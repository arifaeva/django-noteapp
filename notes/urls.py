from django.urls import path

from .views import DeleteView, DetailView, EditView, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("notes/<str:id>/", DetailView.as_view(), name="detail-view"),
    path("todos/<str:id>/delete/", DeleteView.as_view(), name="delete"),
    path("todos/<str:id>/edit/", EditView.as_view(), name="edit"),
]
