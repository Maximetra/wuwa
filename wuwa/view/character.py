from django.http import JsonResponse

from wuwa.models import Character


def get_character_api(request, character_id):
    character = Character.objects.get(id=character_id)
    return JsonResponse({
        'character': {
            'id': character.id,
            'name': character.name,
            'image': character.image,
            'minor_forte_1': character.minor_forte_1,
            'minor_forte_2': character.minor_forte_2,
            'inherent_skill_1': character.inherent_skill_1,
            'inherent_skill_2': character.inherent_skill_2,
        }
    })