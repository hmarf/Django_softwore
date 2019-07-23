from django import forms
from .models import Booking

HOTEL_NAME = (
    ('hotel_A','hotel_A'),
    ('hotel_B','hotel_B'),
    ('hotel_C','hotel_C'),
    ('hotel_D','hotel_D'),
    ('hotel_E','hotel_E'),
)

CITY = (
    ('Tokyo','Tokyo'),
    ('Kyoto','Kyoto'),
    ('Sendai','Sendai'),
    ('Fukuoka','Fukuoka'),
)

ROOM_TYPE = (
    ('standard','standard'),
    ('double','double'),
    ('deluxe','deluxe'),
)

class BooksForm(forms.Form):
    city = forms.ChoiceField(
        label='土地',
        widget=forms.Select,
        choices=CITY,
        required=True,
    )
    hotel_name = forms.ChoiceField(
        label='ホテル名',
        widget=forms.Select,
        choices=HOTEL_NAME,
        required=True,
    )
    room_type = forms.ChoiceField(
        label='部屋タイプ',
        widget=forms.Select,
        choices=ROOM_TYPE,
        required=True,
    )
