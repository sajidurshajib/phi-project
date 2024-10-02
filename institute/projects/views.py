from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Projects
from .forms import ProjectsForm



def all_projects(request):
    projects = Projects.objects.order_by('-created_at')
    
    title = request.GET.get('title', None)
    if title:
        projects = projects.filter(title__icontains=title)

    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(projects, limit)  
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return projects    

@login_required(login_url='/accounts')
def projects(request):
    rsc = all_projects(request)
    context = {'title': 'Projects', 'projects': rsc}
    return render(request, 'dashboard/projects.html', context)


@login_required(login_url='/accounts')
def projects_add(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-projects')
    else:
        form = ProjectsForm()
        context = {'title': 'Add Projects', 'form': form}
        return render(request, 'dashboard/projects-add.html', context)


@login_required(login_url='/accounts')
def projects_edit(request, id):
    rsc = get_object_or_404(Projects, pk=id)

    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES, instance=rsc)
        if form.is_valid():
            form.save()
            return redirect('dashboard-projects')
    else:
        form = ProjectsForm(instance=rsc)

    context = {'form': form, 'projects': rsc}
    return render(request, 'dashboard/projects-edit.html', context)



@login_required(login_url='/accounts')
def projects_remove(request, id):
    rsc = get_object_or_404(Projects, id=id)
    rsc.delete()
    return redirect('dashboard-projects') 