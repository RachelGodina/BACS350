from django.urls import path
from hero.views import blackWidowView, wonderWomanView, gamoraView, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('blackWidow', blackWidowView.as_view()),
    path('wonderWoman', wonderWomanView.as_view()),
    path('gamora', gamoraView.as_view()),
]