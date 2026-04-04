import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from wuwa.models import Weapon, UserWeapon

@login_required
def get_user_weapon_api(request, user_weapon_id):
    uw = UserWeapon.objects.get(id=user_weapon_id)
    return JsonResponse({
        'id': uw.weapon.id,
        'name': uw.weapon.name,
        'image': uw.weapon.image,
        'min_level': uw.min_level,
        'max_level': uw.max_level,
    })

@login_required
def update_or_create_user_weapon_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            weapon_id = data.get('weapon_id')

            if not weapon_id:
                return JsonResponse({'status': 'error', 'message': 'weapon_id manquant'}, status=400)
            
            char_obj = Weapon.objects.get(id=weapon_id)

            update_data = {key: value for key, value in data.items() if key != 'weapon_id'}

            user_char, created = UserWeapon.objects.update_or_create(
                user=request.user,
                weapon=char_obj,
                defaults=update_data
            )

            needed = user_char.get_needed_materials()

            return JsonResponse({
                'status': 'success', 
                'message': 'Planner updated!',
                'needed': needed
            })
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Unauthorized method'}, status=405)


@login_required
def remove_user_weapon_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            weapon_id = data.get('weapon_id')

            user_char = UserWeapon.objects.get(user=request.user, weapon_id=weapon_id)
            user_char.delete()

            return JsonResponse({
                'status': 'success',
                'message': 'Weaponn delected !'
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Unauthorized method'}, status=405)
