from django.urls import path
# from . import views
from . import views_generic as views

# namespace for app urls
# use with reverse and url tags e.g. reverse("polls:index")
app_name = "polls"

# URLS FOR FUNCTION BASED VIEWS
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("<int:question_id>/", views.detail, name="detail"),
#     path("<int:question_id>/results/", views.results, name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

# URLS FOR GENERIC VIEWS
# NOTE: question_id is now pk
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/",
         views.ResultsView.as_view(), name="results"),
    path("<int:pk>/vote/", views.vote, name="vote"),
]
