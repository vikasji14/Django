from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm
# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais}) 

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})


def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            Store.objects.filter(chai_varities=chai_varity)

    else:
        form = ChaiVarityForm()
   
    return render(request, 'chai/chai_stores.html', {'stores': stores , 'form': form})     