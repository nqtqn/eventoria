from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from .models import Event, Place
from .forms import EventForm, PlaceForm
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib import messages


@login_required
def register_user(request):
    return redirect('profile')

def new_year(request):
    return redirect(request,'new-year.html')

def prasdniki(request):
    return redirect(request,'prasdniki.html')

def kinoroom(request):
    return render(request, 'kinoroom.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Перенаправьте на нужный URL после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@csrf_protect
def events_list(request):
    city_filter = request.GET.get('city', 'all')
    selected_city = request.GET.get('city', 'All Cities')

    if city_filter == 'all':
        events = Event.objects.all().order_by('-start_datetime')[:16]
    else:
        events = Event.objects.filter(location=city_filter).order_by('-start_datetime')[:16]

    return render(request, 'events_list.html', {'events': events, 'selected_city': selected_city})

@csrf_protect
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

@csrf_protect
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            # Привязываем событие к текущему пользователю перед сохранением
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('user_events')
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})


@csrf_protect
# def add_place(request):
#     if request.method == 'POST':
#         form = PlaceForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('places_list')
#     else:
#         form = PlaceForm()
#     return render(request, 'add_place.html', {'form': form})

def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            # Привязываем место к текущему пользователю перед сохранением
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect('user_places')
    else:
        form = PlaceForm()

    return render(request, 'add_place.html', {'form': form})




@csrf_protect
def places_list(request):
    city_filter = request.GET.get('city')
    selected_city = request.GET.get('city', 'All Cities')
    if city_filter:
        places = Place.objects.filter(city=city_filter).order_by('-id')[:16]
    else:
        places = Place.objects.order_by('-id')[:16]


    return render(request, 'places_list.html', {'places': places, 'selected_city': selected_city})

@csrf_protect
def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return render(request, 'place_detail.html', {'place': place})




def user_events(request):
    user_events = Event.objects.filter(user=request.user)
    return render(request, 'user_events.html', {'user_events': user_events})

def user_places(request):
    user_places = Place.objects.filter(user=request.user)
    return render(request, 'user_places.html', {'user_places': user_places})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('user_events')
    else:
        form = EventForm(instance=event)

    return render(request, 'edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return redirect('user_events')




def edit_place(request, place_id):
    place = get_object_or_404(Place, id=place_id, user=request.user)

    if request.method == 'POST':
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('user_places')
    else:
        form = PlaceForm(instance=place)

    return render(request, 'edit_place.html', {'form': form, 'place': place})

def delete_place(request, place_id):
    place = get_object_or_404(Place, id=place_id, user=request.user)
    place.delete()
    return redirect('user_places')




@login_required
def profile(request):
    # Проверяем, зарегистрирован ли пользователь
    if request.user.is_authenticated:
        # Если пользователь зарегистрирован, получаем его имя
        user_name = request.user.username
    else:
        # В противном случае, устанавливаем имя по умолчанию
        user_name = "Гость"

    # Передаем имя пользователя в шаблон
    return render(request, 'profile.html', {'user_name': user_name})

def logout_user(request):
    logout(request)
    return redirect('home')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Обработка данных формы изменения профиля
        new_password = request.POST.get('new_password')
        username = request.POST.get('username')

        # Обновление данных пользователя
        user = request.user
        if new_password:
            user.set_password(new_password)
        if username:
            user.username = username

        # Сохранение изменений
        user.save()

        messages.success(request, 'Профиль успешно обновлен.')
        return redirect('profile')

    return render(request, 'edit_profile.html')

