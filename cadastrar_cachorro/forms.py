from django import forms
import requests

from .models import Cachorro

class CachorroForm(forms.ModelForm):
    raca = forms.ChoiceField(choices=[])

    class Meta:
        model = Cachorro
        fields = ["nome", "raca", "idade"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        url = 'https://dog.ceo/api/breeds/list/all'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['status'] == 'success':
                breeds_list = sorted(data['message'].keys())
                self.fields['raca'].choices = [('', 'Selecione uma raça')] + [(breed, breed.capitalize()) for breed in breeds_list]

        except requests.exceptions.RequestException as e:
            print(f'Erro ao obter a lista de raças: {e}')
            self.fields['raca'].choices = [('','Não foi possível carregar as raças')]