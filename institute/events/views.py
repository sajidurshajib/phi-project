from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Events
from .forms import EventForm



def all_events(request):
    events = Events.objects.order_by('-created_at')
    
    name = request.GET.get('name', None)
    if name:
        events = events.filter(name__icontains=name)

    page = request.GET.get('page')
    limit = request.GET.get('limit', 6)
    paginator = Paginator(events, limit)  
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return events    

@login_required(login_url='/accounts')
def events(request):
    events = all_events(request)
    context = {'title': 'Events', 'events': events}
    return render(request, 'dashboard/events.html', context)


@login_required(login_url='/accounts')
def events_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-events')
    else:
        form = EventForm()
        context = {'title': 'Add Events', 'form': form}
        return render(request, 'dashboard/events-add.html', context)


@login_required(login_url='/accounts')
def events_edit(request, id):
    events = get_object_or_404(Events, pk=id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=events)
        if form.is_valid():
            form.save()
            return redirect('dashboard-events')
    else:
        form = EventForm(instance=events)

    context = {'form': form, 'events': events}
    return render(request, 'dashboard/events-edit.html', context)



@login_required(login_url='/accounts')
def events_remove(request, id):
    notice = get_object_or_404(Events, id=id)
    notice.delete()
    return redirect('dashboard-events') 