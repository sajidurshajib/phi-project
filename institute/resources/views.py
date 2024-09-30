from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Resources
from .forms import ResourceForm



def all_resources(request):
    resources = Resources.objects.order_by('-created_at')
    
    title = request.GET.get('title', None)
    if title:
        resources = resources.filter(title__icontains=title)

    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(resources, limit)  
    try:
        resources = paginator.page(page)
    except PageNotAnInteger:
        resources = paginator.page(1)
    except EmptyPage:
        resources = paginator.page(paginator.num_pages)
    return resources    

@login_required(login_url='/accounts')
def resources(request):
    rsc = all_resources(request)
    context = {'title': 'Resources', 'resources': rsc}
    return render(request, 'dashboard/resources.html', context)


@login_required(login_url='/accounts')
def resources_add(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-resources')
    else:
        form = ResourceForm()
        context = {'title': 'Add Resource', 'form': form}
        return render(request, 'dashboard/resources-add.html', context)


@login_required(login_url='/accounts')
def resources_edit(request, id):
    rsc = get_object_or_404(Resources, pk=id)

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=rsc)
        if form.is_valid():
            form.save()
            return redirect('dashboard-resources')
    else:
        form = ResourceForm(instance=rsc)

    context = {'form': form, 'resources': rsc}
    return render(request, 'dashboard/resources-edit.html', context)



@login_required(login_url='/accounts')
def resources_remove(request, id):
    rsc = get_object_or_404(Resources, id=id)
    rsc.delete()
    return redirect('dashboard-resources') 