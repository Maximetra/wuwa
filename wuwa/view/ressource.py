import json

from django.http import JsonResponse

from wuwa.models import Ressource, UserRessource


def update_ressource_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ressource_id = data.get('ressource_id')
            quantity = data.get('quantity')

            ressource = Ressource.objects.get(id=ressource_id)

            obj, created = UserRessource.objects.update_or_create(
                user=request.user, 
                ressource=ressource,
                defaults={'quantity': quantity}
            )

            return JsonResponse({'status': 'success', 'message': 'Inventaire mis à jour !'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Seul le POST est autorisé'}, status=405)