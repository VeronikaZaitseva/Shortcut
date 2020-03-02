from django import forms
from .models import CuttedUrl
from django.core.exceptions import ValidationError


class URLForm(forms.Form):
    url = forms.URLField(label='Вставьте ссылку:')

    def clean_code(self):
        urls = CuttedUrl.objects.all()
        verifiable_code = self.cleaned_data.get('code')
        codes = []
        for obj in urls:
            codes.append(obj.code)
        if verifiable_code in codes:
            raise ValidationError('Такой код уже существует!')
        return verifiable_code
