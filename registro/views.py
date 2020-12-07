from django.shortcuts import render, redirect

from .models import Aluno,Aula,Registro
from .forms import AlunoModelForm,AulaModelForm,RegistroModelForm,RegistroBuscaModelForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listar_aluno(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
        'aluno_empty': []
    }
    return render(request, 'aluno/list.html', context=context)

def criar_aluno(request):
    if request.method == 'POST':
        # Salvar form
        form = AlunoModelForm(request.POST)
        if form.is_valid():
            # True -> é valido
            form.save()
            return redirect('registro:listaralunos')
    else:
        # Get form
        form = AlunoModelForm()

    context = {
        'form': form
    }
    return render(request, 'aluno/create.html', context=context)

def delete_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    aluno.delete()
    return redirect('registro:listaralunos')

def update_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)

    if request.method == 'POST':
        # salvar form
        form = AlunoModelForm(data=request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('registro:listaralunos')
    else:
        # GET
        form = AlunoModelForm(instance=aluno)

    context = {
        'form': form,
    }

    return render(request, 'aluno/update.html', context=context)



def listar_aula(request):
    aulas = Aula.objects.all()

    context = {
        'aulas': aulas,
        'aula_empty': []
    }
    return render(request, 'aula/list.html', context=context)

def criar_aula(request):
    if request.method == 'POST':
        # Salvar form
        form = AulaModelForm(request.POST)
        if form.is_valid():
            # True -> é valido
            form.save()
            return redirect('registro:listaraulas')
    else:
        # Get form
        form = AulaModelForm()

    context = {
        'form': form
    }
    return render(request, 'aula/create.html', context=context)

def delete_aula(request, aula_id):
    aula = Aula.objects.get(pk=aula_id)
    aula.delete()
    return redirect('registro:listaraulas')

def update_aula(request, aula_id):
    aula = Aula.objects.get(pk=aula_id)

    if request.method == 'POST':
        # salvar form
        form = AulaModelForm(data=request.POST, instance=aula)
        if form.is_valid():
            form.save()
            return redirect('registro:listaraulas')
    else:
        # GET
        form = AulaModelForm(instance=aula)

    context = {
        'form': form,
    }

    return render(request, 'aula/update.html', context=context)






def listar_registro(request):
    registros = Registro.objects.all()
    form = RegistroBuscaModelForm()
    context = {
        'registros': registros,
        'form': form,
        'registro_empty': []
    }
    return render(request, 'registro/list.html', context=context)

def criar_registro(request):
    if request.method == 'POST':
        # Salvar form
        form = RegistroModelForm(request.POST)
        if form.is_valid():
            # True -> é valido
            form.save()
            return redirect('registro:listarregistros')
    else:
        # Get form
        form = RegistroModelForm()

    context = {
        'form': form
    }
    return render(request, 'registro/create.html', context=context)

def delete_registro(request, registro_id):
    registro = Registro.objects.get(pk=registro_id)
    registro.delete()
    return redirect('registro:listarregistros')

def update_registro(request, registro_id):
    registro = Registro.objects.get(pk=registro_id)

    if request.method == 'POST':
        # salvar form
        form = RegistroModelForm(data=request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('registro:listarregistros')
    else:
        # GET
        form = RegistroModelForm(instance=registro)

    context = {
        'form': form,
    }

    return render(request, 'registro/update.html', context=context)

def busca_registro(request):
    
    form = RegistroBuscaModelForm(data=request.POST)
    if form.is_valid():
      aula = form.cleaned_data['aula']
      data = form.cleaned_data['data']
      registros = Registro.objects.filter(aula=aula,data=data)
    context = {
        'registros': registros,
        'form': form,
        'registro_empty': []
    }
    return render(request, 'registro/list.html', context=context)




def registrar_presenca(request, aula_id):
    aula = Aula.objects.get(pk=aula_id)
    alunos = Aluno.objects.all()

    context = {
        'aula': aula,
        'alunos': alunos,
        'registro_empty': []
    }
    return render(request, 'registro/presenca.html', context=context)



