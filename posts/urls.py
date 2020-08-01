from django.urls import path

from . import views

urlpatterns = [
  # posts/が見つかればviews.pyにあるindex関数を実行する
  path('', views.index, name="index"),
  # posts/about/が見つかればviews.pyにあるabout関数を実行する
  path('about/', views.about, name="about"),
]