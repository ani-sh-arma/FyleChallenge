from django.shortcuts import render , redirect
from . import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse



def index(request):

    username = request.GET.get('username', '')
    repo_search = request.GET.get('repo_search', '')
    repos_per_page = request.GET.get('repos_per_page', '')

    if not username:
        username = 'johnpapa'  # Default to johnpapa if no username is provided

    user_data = utils.get_user_data(username)

    if repo_search:
        repo_data = utils.search_repo(username , repo_search)
    else:
        repo_data = utils.get_user_repositories(username)
            
    queryset = list(repo_data)

    if 'error' in repo_data or 'error' in user_data:
        return redirect('error')
    

    if repos_per_page:
        per_page = int(repos_per_page)
    else:
        per_page = 10
    
    
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, per_page)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
        
    return render(request, 'index.html', {'user_data': user_data , 'objects': objects})


def error(requests):
    return render(requests, 'error.html', {'error': 'Oops! Something went wrong'})

