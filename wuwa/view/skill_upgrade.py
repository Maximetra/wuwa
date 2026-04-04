import json

from django.http import JsonResponse

from wuwa.models import SkillUpgrade, UserSkillUpgrade


def update_skill_upgrade_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            skill_upgrade_id = data.get('skill_upgrade_id')
            quantity = data.get('quantity')

            skill_upgrade = SkillUpgrade.objects.get(id=skill_upgrade_id)

            obj, created = UserSkillUpgrade.objects.update_or_create(
                user=request.user, 
                skill_upgrade=skill_upgrade,
                defaults={'quantity': quantity}
            )

            return JsonResponse({'status': 'success', 'message': 'Inventaire mis à jour !'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Seul le POST est autorisé'}, status=405)