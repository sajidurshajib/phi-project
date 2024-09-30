from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Managements
from .forms import ManagementsForm


def all_management(request):
    managements = Managements.objects.order_by('-created_at')
    
    name = request.GET.get('name', None)
    if name:
        managements = managements.filter(name__icontains=name)

    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(managements, limit)  
    try:
        managements = paginator.page(page)
    except PageNotAnInteger:
        managements = paginator.page(1)
    except EmptyPage:
        managements = paginator.page(paginator.num_pages)
    return managements    

@login_required(login_url='/accounts')
def managements(request):
    mng = all_management(request)
    context = {'title': 'Managements', 'managements': mng}
    return render(request, 'dashboard/managements.html', context)


@login_required(login_url='/accounts')
def managements_add(request):
    if request.method == 'POST':
        form = ManagementsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-managements')
    else:
        form = ManagementsForm()
        context = {'title': 'Add Management', 'form': form}
        return render(request, 'dashboard/managements-add.html', context)


@login_required(login_url='/accounts')
def managements_edit(request, id):
    mng = get_object_or_404(Managements, pk=id)

    if request.method == 'POST':
        form = ManagementsForm(request.POST, request.FILES, instance=mng)
        if form.is_valid():
            form.save()
            return redirect('dashboard-managements')
    else:
        form = ManagementsForm(instance=mng)

    context = {'form': form, 'managements': mng}
    return render(request, 'dashboard/managements-edit.html', context)



@login_required(login_url='/accounts')
def managements_remove(request, id):
    notice = get_object_or_404(Managements, id=id)
    notice.delete()
    return redirect('dashboard-managements') 