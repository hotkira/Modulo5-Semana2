from django.shortcuts import render
from base.forms import FormReserva

# Create your views here.
def reservaBanho(request):
  sucesso = False
#Verifica que o formulário já foi enviado ou a página esta sendo aberta ainda sem o envio
  if request.method == 'GET':
    form = FormReserva()
  else:
    form = FormReserva(request.POST)
    if form.is_valid():
      sucesso = True

  context = {
    "form": form,
    "sucesso": sucesso
  }

  return render(request, 'reserva_de_banho.html', context)