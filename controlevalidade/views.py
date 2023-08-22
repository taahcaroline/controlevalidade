# Createfrom django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



from .models import Cadastroitens
from .forms import CadastroitensForm
from django.db.models import Q



from django.shortcuts import render, get_object_or_404



def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')




# cadastro vagas
@login_required 
def vagascad(request):
    if request.method == 'POST':
            form = CadastroitensForm(request.POST)
            if form.is_valid():
             servicos = form.save(commit=False)
             servicos.user = request.user
             servicos.save()

            return redirect('listaitens')
    else:        
        form = CadastroitensForm()
        return render(request, 'cadservico.html', {'form': form})


#lista de vagas

def vagas(request):
    itens = Cadastroitens.objects.all()
   
    context = {
        'itens': itens
    }

    return render(request, 'servicoscadastrados.html',  context)

def vagasview(request, id):
    cadastroitens = get_object_or_404(Cadastroitens, pk=id)
    return render(request, 'demandas.html', {'cadastroitens': cadastroitens} )


@login_required 
# #editar demandas
@login_required 
def edititens(request, id):
    itens = get_object_or_404(Cadastroitens, pk=id)
    form = CadastroitensForm(instance=itens)
    
    if(request.method == 'POST'):
        form = CadastroitensForm(request.POST, instance=itens)
        if (form.is_valid()):
            itens.save()
            return redirect('listaitens')
        else:
            return render(request, 'editarservico.html', {'form': form, 'itens': itens})
    else: 
        return render(request, 'editarservico.html', {'form': form, 'itens': itens})

            
# # deletar demandas
@login_required 
def itensdelete(request, cadastroitens_pk):
    itens = Cadastroitens.objects.get(pk=cadastroitens_pk)
    itens.delete()

    return redirect('listaitens')





# #lista de produtos
# @login_required 
# def listaprodutos(request):
#     produtos = Nomeproduto.objects.all()
#     # paginator = Paginator(serv, 3)
#     # page = request.GET.get('page')
#     # listademanda = paginator.get_page(page)
#     context = {
#         'produtos': produtos
#     }

#     return render(request, 'produtoscadastrados.html',  context)



# busca
def busca(request):
    query = request.GET.get('q')
    results = Cadastroitens.objects.filter(cargo__icontains=query)
    return render(request, 'resultado.html', {'results': results})
   