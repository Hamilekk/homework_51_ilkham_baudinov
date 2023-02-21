from django.urls import path

from webapp.views.base import home_view

from webapp.views.cat_stats import cat_stats_view

urlpatterns = [
    path('', home_view),
    path('cat_stats', cat_stats_view)
]
