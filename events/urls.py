from django.urls import path
from .views import events_list, add_event
import os
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import add_place
from .views import places_list
from .views import place_detail
from .views import user_events, user_places, edit_event, delete_event, edit_place, delete_place, logout_user, edit_profile
from .views import profile
from .views import new_year, prasdniki, kinoroom
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('events/', events_list, name='events_list'),
    path('add_event/', add_event, name='add_event'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),  # Новый URL-паттерн для деталей события
    path('add_place/', add_place, name='add_place'),
    path('places/', places_list, name='places_list'),
    path('places/<int:place_id>/', place_detail, name='place_detail'),
    path('user/events/', user_events, name='user_events'),
    path('user/places/', user_places, name='user_places'),
    path('', events_list, name='home'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    # path('logout/', logout_user, name='logout_user'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_user'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout_user'),
    path('login_or_register/', TemplateView.as_view(template_name='login_or_register.html'), name='login_or_register'),
    path('user/events/<int:event_id>/edit/', edit_event, name='edit_event'),
    path('user/events/<int:event_id>/delete/', delete_event, name='delete_event'),
    path('user/places/<int:place_id>/edit/', edit_place, name='edit_place'),
    path('user/places/<int:place_id>/delete/', delete_place, name='delete_place'),
    path('first/', TemplateView.as_view(template_name='new-year.html'), name='new-year'),
    path('second/', TemplateView.as_view(template_name='prasdniki.html'), name='prasdniki'),
    path('third/', TemplateView.as_view(template_name='kinoroom.html'), name='kinoroom'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)