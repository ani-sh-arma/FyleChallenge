import requests
from django.conf import settings
from django.http import JsonResponse


def get_user_data(username):
    user_url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'token {settings.GITHUB_TOKEN}'}
    user_response = requests.get(user_url , headers=headers, timeout=10)
    user_data = user_response.json()
    
    return user_data



import requests

def get_user_repositories(username):
    base_url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {settings.GITHUB_TOKEN}'}
    repositories = []

    # GitHub API returns paginated results
    page = 1
    while True:
        params = {'page': page, 'per_page': 100}  # Adjust per_page based on your needs

        try:
            response = requests.get(base_url, params=params , headers=headers , timeout=20)
            response.raise_for_status()

        except requests.exceptions.ConnectTimeout:
            return JsonResponse({'error': 'Timeout error'})
        
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)})

        if response.status_code == 200:
            current_repositories = response.json()
            if not current_repositories:
                break  # No more repositories, exit the loop
            repositories.extend(current_repositories)
            page += 1
        else:
            print(f"Error fetching repositories for {username}. Status code: {response.status_code}")
            break

    return repositories



# def get_user_repositories(username):
#     repositories_url = f'https://api.github.com/users/{username}/repos'
#     repositories_response = requests.get(repositories_url)
#     repositories_data = repositories_response.json()
    
#     return repositories_data