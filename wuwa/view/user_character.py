import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from wuwa.models import Character, UserCharacter

@login_required
def get_user_character_api(request, user_character_id):
    uc = UserCharacter.objects.get(id=user_character_id)
    return JsonResponse({
        'id': uc.character.id,
        'name': uc.character.name,
        'image': uc.character.image,
        'min_level': uc.min_level,
        'max_level': uc.max_level,
        'min_normal_attack_level': uc.min_normal_attack_level,
        'max_normal_attack_level': uc.max_normal_attack_level,
        'min_resonance_skill_level': uc.min_resonance_skill_level,
        'max_resonance_skill_level': uc.max_resonance_skill_level,
        'min_resonance_liberation_level': uc.min_resonance_liberation_level,
        'max_resonance_liberation_level': uc.max_resonance_liberation_level,
        'min_forte_circuit_level': uc.min_forte_circuit_level,
        'max_forte_circuit_level': uc.max_forte_circuit_level,
        'min_intro_skill_level': uc.min_intro_skill_level,
        'max_intro_skill_level': uc.max_intro_skill_level,
        'minor_forte_1': uc.character.minor_forte_1,
        'minor_forte_2': uc.character.minor_forte_2,
        'inherent_skill_1': uc.character.inherent_skill_1,
        'inherent_skill_2': uc.character.inherent_skill_2,
        'first_tier_trace1': uc.first_tier_trace1,
        'first_tier_trace2': uc.first_tier_trace2,
        'first_tier_trace3': uc.first_tier_trace3,
        'first_tier_trace4': uc.first_tier_trace4,
        'second_tier_trace1': uc.second_tier_trace1,
        'second_tier_trace2': uc.second_tier_trace2,
        'second_tier_trace3': uc.second_tier_trace3,
        'second_tier_trace4': uc.second_tier_trace4,
        'first_inherent_skill': uc.first_inherent_skill,
        'second_inherent_skill': uc.second_inherent_skill,
    })

@login_required
def update_or_create_user_character_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            character_id = data.get('character_id')

            if not character_id:
                return JsonResponse({'status': 'error', 'message': 'character_id manquant'}, status=400)
            
            char_obj = Character.objects.get(id=character_id)

            update_data = {key: value for key, value in data.items() if key != 'character_id'}

            user_char, created = UserCharacter.objects.update_or_create(
                user=request.user,
                character=char_obj,
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
def remove_user_character_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            character_id = data.get('character_id')

            user_char = UserCharacter.objects.get(user=request.user, character_id=character_id)
            user_char.delete()

            return JsonResponse({
                'status': 'success',
                'message': 'Character deleted !'
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Unauthorized method'}, status=405)
