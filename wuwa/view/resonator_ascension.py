import json

from django.http import JsonResponse

from wuwa.models import ResonatorAscension, UserResonatorAscension

def update_resonator_ascension_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            resonator_ascension_id = data.get('resonator_ascension_id')
            quantity = data.get('quantity')

            resonator_ascension = ResonatorAscension.objects.get(id=resonator_ascension_id)

            obj, created = UserResonatorAscension.objects.update_or_create(
                user=request.user, 
                resonator_ascension=resonator_ascension,
                defaults={'quantity': quantity}
            )

            return JsonResponse({'status': 'success', 'message': 'Inventaire mis à jour !'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Seul le POST est autorisé'}, status=405)