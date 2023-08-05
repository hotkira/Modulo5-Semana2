from django import forms

class FormReserva(forms.Form):
  nomeDoPet = forms.CharField(label="Nome do seu Pet")
  telefone = forms.CharField(label="Telefone")
  diaDaReserva = forms.DateField(label="Dia da reserva", 
                                 widget=forms.widgets.DateInput(attrs={'type': 'date'}))
  observacoes = forms.CharField(label="Obsevações",
                                widget=forms.Textarea)