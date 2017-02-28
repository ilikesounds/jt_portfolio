from django.shortcuts import render

# Create your views here.


def home_view(request):
    """home view test"""

    context = {
        'page_title': 'HOME',
    }
    return render(request, 'blog/home.html', context)
