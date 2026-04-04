import json

from django.http import JsonResponse

from wuwa.models import Ascension, UserAscension


def get_ascension_api(request, ascension_id):
    ascension = Ascension.objects.get(id=ascension_id)
    return JsonResponse({
        'ascension': {
            'id': ascension.id,
            'lf_name': ascension.lf_name,
            'lf_image': ascension.lf_image,
            'mf_name': ascension.mf_name,
            'mf_image': ascension.mf_image,
            'hf_name': ascension.hf_name,
            'hf_image': ascension.hf_image,
            'ff_name': ascension.ff_name,
            'ff_image': ascension.ff_image,

        }
    })

def update_ascension_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ressource_id = data.get('ressource_id')
            quantity_lf = data.get('quantity_lf')
            quantity_mf = data.get('quantity_mf')
            quantity_hf = data.get('quantity_hf')
            quantity_ff = data.get('quantity_ff')

            ascension = Ascension.objects.get(id=ressource_id)

            obj, created = UserAscension.objects.update_or_create(
                user=request.user, 
                ascension=ascension,
                
                defaults={
                    'quantity_lf': quantity_lf,
                    'quantity_mf': quantity_mf,
                    'quantity_hf': quantity_hf,
                    'quantity_ff': quantity_ff
                }
            )

            return JsonResponse({'status': 'success', 'message': 'Inventaire mis à jour !'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Seul le POST est autorisé'}, status=405)
