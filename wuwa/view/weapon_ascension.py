import json

from django.http import JsonResponse

from wuwa.models import UserWeaponAscension, WeaponAscension


def get_weapon_ascension_api(request, weapon_ascension_id):
    weapon_ascension = WeaponAscension.objects.get(id=weapon_ascension_id)
    return JsonResponse({
        'weapon_ascension': {
            'id': weapon_ascension.id,
            'green_name': weapon_ascension.green_name,
            'green_image': weapon_ascension.green_image,
            'blue_name': weapon_ascension.blue_name,
            'blue_image': weapon_ascension.blue_image,
            'purple_name': weapon_ascension.purple_name,
            'purple_image': weapon_ascension.purple_image,
            'yellow_name': weapon_ascension.yellow_name,
            'yellow_image': weapon_ascension.yellow_image,

        }
    })

def update_weapon_ascension_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            ressource_id = data.get('ressource_id')
            quantity_green = data.get('quantity_green')
            quantity_blue = data.get('quantity_blue')
            quantity_purple = data.get('quantity_purple')
            quantity_yellow = data.get('quantity_yellow')

            weapon_ascension = WeaponAscension.objects.get(id=ressource_id)

            obj, created = UserWeaponAscension.objects.update_or_create(
                user=request.user, 
                weapon_ascension=weapon_ascension,
                
                defaults={
                    'quantity_green': quantity_green,
                    'quantity_blue': quantity_blue,
                    'quantity_purple': quantity_purple,
                    'quantity_yellow': quantity_yellow
                }
            )

            return JsonResponse({'status': 'success', 'message': 'Inventaire mis à jour !'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Seul le POST est autorisé'}, status=405)
