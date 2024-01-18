from django.shortcuts import render , redirect
from . import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse



def index(request):

    username = request.GET.get('username', '')  # Get the username from the request

    if not username:
        username = 'johnpapa'  # Default to johnpapa if no username is provided
    
    user_data = utils.get_user_data(username)
    repo_data = utils.get_user_repositories(username)
    queryset = list(repo_data)

    if 'error' in repo_data or 'error' in user_data:
        return redirect('error')
    
    
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 10)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    

    # Render the template with paginated data
    return render(request, 'index.html', {'user_data': user_data , 'objects': objects})


def error(requests):
    return render(requests, 'error.html', {'error': 'Oops! Something went wrong'})

