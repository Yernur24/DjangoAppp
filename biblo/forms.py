from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['cat'].empty_label="Категория не выбрана"

  class Meta:
     model=Product
     fields=['name','slug','content','image','author','is_published', 'cat']
     widgets = {
         'name': forms.TextInput(attrs={'class':'form-input'}),
         'content': forms.Textarea(attrs={'cols':60, 'rows':10}),
     }

  def clean_title(self):
      name=self.cleaned_data['name']
      if len(name)>200:
          raise ValidationError('Длина превышает 200 символов')

      return name