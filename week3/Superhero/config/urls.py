from django.urls import path
from hero.views import blackWidowView, wonderWomanView, gamoraView

urlpatterns = [
    path('blackWidow', blackWidowView.as_view()),
    path('wonderWoman', wonderWomanView.as_view()),
    path('gamora', gamoraView.as_view()),
]