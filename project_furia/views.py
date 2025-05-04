from django.shortcuts import render

def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_429(request):
    return render(request, '429.html', status=429)