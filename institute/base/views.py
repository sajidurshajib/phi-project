from django.shortcuts import render

def main(request):
    context = {'title': 'Home'}
    return render(request, 'main.html', context)

# About 
def about(request):
    context = {'title': 'About', 'title_detail':'About', 'subtitle': 'Get more information about South Sudan Public Health Institute', }
    return render(request, 'about.html', context)

def about_background(request):
    context = {'title': 'Background', 'title_detail':'SSPHI Background information', 'subtitle': 'Get more information about South Sudan Public Health Institute', }
    return render(request, 'about-background.html', context)

def about_history(request):
    context = {'title': 'History', 'title_detail':'PHI History', 'subtitle': 'Get more information about South Sudan Public Health Institute', }
    return render(request, 'about-history.html', context)

def about_partners(request):
    context = {'title': 'SSPHI Partners', 'title_detail':'Partners', 'subtitle': 'Check & view SSPHI Partners', }
    return render(request, 'about-partners.html', context)

# Programms 
def programs_surveillance(request):
    context = {'title': 'Programs', 'title_detail':'PHI Program', 'subtitle': 'Surveillance & Disease Intelligence', }
    return render(request, 'programs-survillance.html', context)


def programs_emergency(request):
    context = {'title': 'Programs', 'title_detail':'PHI Program', 'subtitle': 'Emergency Preparedness, Response & EOC', }
    return render(request, 'programs-emergency.html', context)

def programs_lab(request):
    context = {'title': 'Programs', 'title_detail':'PHI Program', 'subtitle': 'Laboratory Services and Public Health Diagnostics', }
    return render(request, 'programs-lab.html', context)

def programs_workforce(request):
    context = {'title': 'Programs', 'title_detail':'PHI Program', 'subtitle': 'Workforce Development', }
    return render(request, 'programs-workforce.html', context)
