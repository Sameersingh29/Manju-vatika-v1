from django import forms
from django.core.validators import RegexValidator, EmailValidator
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Enter a valid email address")]
    )
    phone = forms.CharField(
        validators=[RegexValidator(regex=r'^\d{10}$', message="Enter a valid phone number with exactly 10 digits.")]
    )
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date', 
            'class': 'datepicker',
            'placeholder': 'YYYY-MM-DD'
        })
    )
    event_type = forms.ChoiceField(choices=(
        ('Wedding', 'WEDDING'),
        ('Engagement', 'ENGAGEMENT'),
        ('Birthday', 'BIRTHDAY'),
        ('Conference(Corporate meeting)', 'CONFERENCE'),
        ('Anniversary', 'ANNIVERSARY'),
        ('Other', 'OTHER'),
    ))

    class Meta:
        model = Enquiry
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'event_date', 'guest_count', 'event_type', 'comments'
        ]
