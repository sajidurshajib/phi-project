from django.shortcuts import render

def main(request):
    context = {'title': 'PHI - Home'}
    return render(request, 'main.html', context)

