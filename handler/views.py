from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'recipes/error_404.html')
