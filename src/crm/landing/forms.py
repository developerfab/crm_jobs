from django.forms import ModelForm
from models import ContactUser


class ContactUserForm(ModelForm):
    class Meta:
        model = ContactUser
