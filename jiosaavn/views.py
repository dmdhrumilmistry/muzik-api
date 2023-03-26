from django.http import HttpRequest, JsonResponse
from musicapy.saavn_api.api import SaavnAPI

saavn_api = SaavnAPI()

def search(request:HttpRequest):
    status_code = 200
    
    if request.method == 'GET':
        query = request.GET.get('query', 'Justin Bieber')
        search_type = request.GET.get('type', 'all')
        page_no = request.GET.get('page_no',1)
        limit = request.GET.get('limit', 100)

        if search_type == 'all':
            res = saavn_api.search_all(query)

        elif search_type == 'song':
            res = saavn_api.search_song(
                song_query=query,
                page=page_no,
                limit=limit
            )

        elif search_type == 'album':
            res = saavn_api.search_album(
                album_query=query,
                page=page_no,
                limit=limit
            )

        else:
            res = {'msg': 'Invalid type param'}
            status_code = 400

        if not res:
            status_code = 500
            res = {'msg': 'JioSaavn API is facing some issues'}

    else:
        res = {'msg':'method not allowed'}
        status_code = 405

    return JsonResponse(res, status=status_code)


def song_details(request:HttpRequest):
    status_code = 200
    
    if request.method == 'GET':
        query = request.GET.get('query', 'https://www.jiosaavn.com/song/phir-bhi-tumko-chaahunga/OQQJQBJ4fGc')
        q_type = request.GET.get('type', 'song')

        if not query.startswith('https://www.jiosaavn.com/'):
            try:
                query = int(query)
        
            except Exception:
                return JsonResponse(
                    {'msg':'query should be jiosaavn link or integer id'}, 
                    status = 400
                )

        identifier = saavn_api.create_identifier(query, q_type)

        if q_type == 'song':
            res = saavn_api.get_song_details(identifier, False)

        elif q_type == 'playlist':
            res = saavn_api.get_playlist_details(identifier)

        elif q_type == 'album':
            res = saavn_api.get_album_details(identifier)

        else:
            res = {'msg': 'Invalid type param'}
            status_code = 400

        if not res:
            status_code = 500
            res = {'msg': 'JioSaavn API is facing some issues'}

    else:
        res = {'msg':'method not allowed'}
        status_code = 405

    return JsonResponse(res, status=status_code)