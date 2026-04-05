from django.http import JsonResponse

from wuwa.models import Character


def get_character_api(request, character_id):
    character = Character.objects.get(id=character_id)
    return JsonResponse({
        'character': {
            'id': character.id,
            'name': character.name,
            'image': character.image,
            'main_forte': character.main_forte.image,
            'minor_forte': character.minor_forte.image,
            'inherent_skill_1': character.inherent_skill_1,
            'inherent_skill_2': character.inherent_skill_2,
        }
    })