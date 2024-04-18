from django.urls import path

from snippets import views


urlpatterns = [
    path("snippets/", views.snipept_list),
    path("snippets/<int:pk>/", views.snippet_detail),
]