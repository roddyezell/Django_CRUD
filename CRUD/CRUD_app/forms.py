from django import forms
from CRUD_app.models import User

class NewUser(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'