from django.http import JsonResponse

from wuwa.models import Character, Weapon


def get_weapon_api(request, weapon_id):
    weapon = Weapon.objects.get(id=weapon_id)
    return JsonResponse({
        'weapon': {
            'id': weapon.id,
            'name': weapon.name,
            'image': weapon.image,
        }
    })