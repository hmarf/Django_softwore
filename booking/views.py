from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms
from django.contrib.auth.models import User
from django.views import generic
from .forms import BooksForm
from .models import Hotel, Booking
from django.utils import timezone

from datetime import datetime as dt

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def index(request):
    logged_in = False
    name = None

    if 'name' in request.POST and 'passwd' in request.POST:
        request.session['name'] = request.POST['name']
        request.session['passwd'] = request.POST['passwd']

    if 'logout' in request.POST:
        request.session.clear()

    if 'name' in request.session and 'passwd' in request.session:
        name = request.session['name']
        logged_in = True

    return render(request, "index.html", {'loggedIn':logged_in, 'name':name})

def home(request):
    form = forms.BooksForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'home.html', d)

def searchHotel(request):
    if request.method == "POST":
        form = BooksForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
        if form.is_valid():  # ← 受け取ったデータの正当性確認
            hotel_data = Hotel.objects.get(
                hotel_name=request.POST['hotel_name'],
                city=request.POST['city'],
                room_type=request.POST['room_type']
                )
            time_str = request.POST['time']
            time_str = time_str + ' 0:0:0'
            time_datatime = dt.strptime(time_str,'%Y-%m-%d %H:%M:%S')
            booking = Booking(user_id=User(id=request.user.id),
                            hotel_id=Hotel(id=hotel_data.id),
                            time_data=time_datatime)
            booking.save()
        else:
            print('not ok')
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        print('error')
    return HttpResponseRedirect('/confirm_booking')

def confirm_booking(request):
    booking_user_data = []
    booking_data = Booking.objects.all().filter(user_id=User(id=request.user.id))
    for booking in booking_data:
        hotel_data = Hotel.objects.all().filter(id=booking.hotel_id_id).values()
        booking_user_data.append([hotel_data,booking.time_data])
    d = {
        'bookingDatas': booking_user_data,
    }
    return render(request, 'confirm.html',d)

def create_query(request):
    hotelName = ['hotel_A','hotel_B','hotel_C','hotel_D','hotel_E']
    cities = ['Tokyo','Kyoto','Sendai','Fukuoka']
    room_type = ['standard','double','deluxe']
    for city in cities:
        for hotel in hotelName:
            for room in room_type:
                a = Hotel(hotel_name=hotel,city=city,room_type=room)
                a.save()
    return HttpResponseRedirect('/admin')

def delete_query(request):
    Hotel.objects.all().delete()
    return HttpResponseRedirect('/admin')