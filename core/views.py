from django.shortcuts import render
#from .forms import ContatoForm
from core.models import Curso
from core.forms import ContactForm
from core.backend import GerenciadorBanco

# Create your views here.
def index(request):
    contexto={
        "usuario":"",
        #aluno,professor,sbruble
        "perfil": "aluno",
        # "cursos": Curso.objects.all()
        # "cursos": Curso.objects.raw('SELECT * FROM core_curso')
        "cursos": GerenciadorBanco().select()
    }
    return render(request,"index.html",contexto)

def disciplina(request):
    return render(request,"disciplina.html")

def detalhe_curso(request):
    return render(request,"detalhe_curso.html")

def lista_cursos(request):
    return render(request,"lista_cursos.html")

def noticias(request):
    return render(request,"noticias.html")

def contato(request):
    if request.POST:
        form = ContactForm(request.POST)
        #form.enviar_email()
    else:
        form = ContactForm(request.POST)
    contexto = {
        "form":form
    }
    return render(request,"contato.html",contexto)

def login(request):
    return render(request,"login.html")
