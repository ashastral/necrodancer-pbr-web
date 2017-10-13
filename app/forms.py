from django import forms
from django.core.validators import RegexValidator

class GenerateForm(forms.Form):
    seed = forms.CharField(
        label='Seed',
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[A-Za-z0-9 ]+$',
                message='Seed can only contain letters, numbers, and spaces',
                code='invalid_seed'
            ),
        ],
        widget=forms.TextInput(attrs={
            'class': 'prism-notch-sm prism-focus-notch-lg',
        }),
    )
