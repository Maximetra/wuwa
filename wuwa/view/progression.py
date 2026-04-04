from django.shortcuts import redirect, render

from wuwa.models import Ascension, UserAscension, Character, Element, ResonatorAscension, Ressource, SkillUpgrade, UserCharacter, UserResonatorAscension, UserRessource, UserSkillUpgrade, UserWeapon, UserWeaponAscension, Weapon, WeaponAscension, WeaponType
from django.db.models import Subquery, OuterRef, Value
from django.db.models.functions import Coalesce

from wuwa.utils import calculer_synthese


def get_progression_view(request):
    if not request.user.is_authenticated:
        return redirect('login_view')

    elements = get_elements()
    weapon_types = get_weapon_types()

    characters = get_characters(request)
    weapons = get_weapons(request)
    ascensions = get_ascensions(request)
    resonator_ascensions = get_resonator_ascensions(request)
    ressources = get_ressources(request)
    weapon_ascensions = get_weapon_ascensions(request)
    skill_upgrades = get_skill_upgrades(request)
    user_characters = get_user_characters(request)
    user_weapons = get_user_weapons(request)

    total_needed = {
        'ressource': {},
        'ascension': {},
        'weapon_ascension': {},
        'resonator_ascension': {},
        'skill_upgrade': {}
    }

    list_user_characters = []
    build_user_characters(list_user_characters, total_needed, ascensions, user_characters, resonator_ascensions, ressources, skill_upgrades, weapon_ascensions)

    list_user_weapons = []
    build_user_weapons(user_weapons, list_user_weapons, total_needed, ascensions, weapon_ascensions)


    build_need_and_quantity_individually(total_needed, ressources, resonator_ascensions, skill_upgrades, ascensions, weapon_ascensions)


    return render(request, '../templates/progression.html', {
        'elements': elements,
        'weapon_types': weapon_types,
        'characters': characters,
        'weapons': weapons,
        'ressources': ressources,
        'ascensions': ascensions,
        'resonator_ascensions': resonator_ascensions,
        'weapon_ascensions': weapon_ascensions,
        'skill_upgrades': skill_upgrades,
        'user_characters': list_user_characters,
        'user_weapons': list_user_weapons,
    })

def get_elements():
    elements = Element.objects.all()
    return elements

def get_weapon_types():
    weapon_types = WeaponType.objects.all()
    return weapon_types

def get_characters(request):
    characters = Character.objects.exclude(
        usercharacter__user = request.user
    ).order_by('-release_date')

    return characters

def get_weapons(request):
    weapons = Weapon.objects.exclude(
        userweapon__user = request.user
    ).order_by('-release_date')

    return weapons

def get_ascensions(request):
    ascensions = Ascension.objects.all()
    
    user_inventory_ascension = UserAscension.objects.filter(
        user = request.user,
        ascension_id = OuterRef('pk')
    )

    ascensions = Ascension.objects.annotate(
        user_ascension_quantity_lf = Coalesce(
            Subquery(user_inventory_ascension.values('quantity_lf')[:1]), 
            Value(0)
        ),
        user_ascension_quantity_mf = Coalesce(
            Subquery(user_inventory_ascension.values('quantity_mf')[:1]), 
            Value(0)
        ),
        user_ascension_quantity_hf = Coalesce(
            Subquery(user_inventory_ascension.values('quantity_hf')[:1]), 
            Value(0)
        ),
        user_ascension_quantity_ff = Coalesce(
            Subquery(user_inventory_ascension.values('quantity_ff')[:1]), 
            Value(0)
        )

    )

    return ascensions

def get_resonator_ascensions(request):
    resonator_ascensions = ResonatorAscension.objects.all()

    user_inventory_resonator_ascension = UserResonatorAscension.objects.filter(
        user = request.user,
        resonator_ascension_id = OuterRef('pk')
    )

    resonator_ascensions = ResonatorAscension.objects.annotate(
        user_resonator_ascension_quantity = Coalesce(
            Subquery(user_inventory_resonator_ascension.values('quantity')[:1]), 
            Value(0)
        )
    )

    return resonator_ascensions

def get_ressources(request):
    user_inventory_ressource = UserRessource.objects.filter(
        user = request.user,
        ressource_id = OuterRef('pk')
    )


    ressources = Ressource.objects.annotate(
        user_ressource_quantity = Coalesce(
            Subquery(user_inventory_ressource.values('quantity')[:1]), 
            Value(0)
        )
    )

    return ressources

def get_weapon_ascensions(request):
    weapon_ascensions = WeaponAscension.objects.all()

    user_inventory_weapon_ascension = UserWeaponAscension.objects.filter(
        user = request.user,
        weapon_ascension_id = OuterRef('pk')
    )

    weapon_ascensions = WeaponAscension.objects.annotate(
        user_weapon_ascension_quantity_green = Coalesce(
            Subquery(user_inventory_weapon_ascension.values('quantity_green')[:1]), 
            Value(0)
        ),
        user_weapon_ascension_quantity_blue = Coalesce(
            Subquery(user_inventory_weapon_ascension.values('quantity_blue')[:1]), 
            Value(0)
        ),
        user_weapon_ascension_quantity_purple = Coalesce(
            Subquery(user_inventory_weapon_ascension.values('quantity_purple')[:1]), 
            Value(0)
        ),
        user_weapon_ascension_quantity_yellow = Coalesce(
            Subquery(user_inventory_weapon_ascension.values('quantity_yellow')[:1]), 
            Value(0)
        )
    )

    return weapon_ascensions

def get_skill_upgrades(request):
    skill_upgrades = SkillUpgrade.objects.all()

    user_inventory_skill_upgrade = UserSkillUpgrade.objects.filter(
        user = request.user,
        skill_upgrade_id = OuterRef('pk')
    )

    skill_upgrades = SkillUpgrade.objects.annotate(
        user_skill_upgrade_quantity = Coalesce(
            Subquery(user_inventory_skill_upgrade.values('quantity')[:1]), 
            Value(0)
        )
    )

    return skill_upgrades

def get_user_characters(request):
    user_characters = UserCharacter.objects.filter(user=request.user).order_by('-character__release_date')

    return user_characters

def get_user_weapons(request):
    user_weapons = UserWeapon.objects.filter(user=request.user).order_by('-weapon__release_date')

    return user_weapons

def build_user_characters(list_user_characters, total_needed, ascensions, user_characters, resonator_ascensions, ressources, skill_upgrades, weapon_ascensions):
    for uc in user_characters:
        char_needs = uc.get_needed_materials()
        if uc.active:
            for rid, qty in char_needs['ressource'].items():
                total_needed['ressource'][rid] = total_needed['ressource'].get(rid, 0) + qty
                
            for raid, qty in char_needs['resonator_ascension'].items():
                total_needed['resonator_ascension'][raid] = total_needed['resonator_ascension'].get(raid, 0) + qty

            for suid, qty in char_needs['skill_upgrade'].items():
                total_needed['skill_upgrade'][suid] = total_needed['skill_upgrade'].get(suid, 0) + qty

            for aid, tiers in char_needs['ascension'].items():
                total_needed['ascension'].setdefault(aid, {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 0})
                for tier, qty in tiers.items():
                    total_needed['ascension'][aid][tier] += qty

            for waid, colors in char_needs['weapon_ascension'].items():
                total_needed['weapon_ascension'].setdefault(waid, {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 0})
                for color, qty in colors.items():
                    total_needed['weapon_ascension'][waid][color] += qty

        character = Character.objects.filter(id=uc.character.id).first()
        character.rarity_range = range(character.rarity)


        ascension = ascensions.filter(id=character.ascension_id).first()
        if ascension:
            asc_data = char_needs['ascension'].get(ascension.id, {})
            ascension.need_lf = asc_data.get('lf', 0)
            ascension.need_mf = asc_data.get('mf', 0)
            ascension.need_hf = asc_data.get('hf', 0)
            ascension.need_ff = asc_data.get('ff', 0)

        weapon_ascension = weapon_ascensions.filter(id=character.weapon_ascension_id).first()
        if weapon_ascension:
            wa_data = char_needs['weapon_ascension'].get(weapon_ascension.id, {}) if weapon_ascension else {}
            weapon_ascension.need_green = wa_data.get('green', 0)
            weapon_ascension.need_blue = wa_data.get('blue', 0)
            weapon_ascension.need_purple = wa_data.get('purple', 0)
            weapon_ascension.need_yellow = wa_data.get('yellow', 0)

        resonator_ascension = resonator_ascensions.filter(id=character.resonator_ascension_id).first()
        if resonator_ascension:
            resonator_ascension.need = char_needs['resonator_ascension'].get(resonator_ascension.id, 0)

        skill_upgrade = skill_upgrades.filter(id=character.skill_upgrade_id).first()
        if skill_upgrade:
            skill_upgrade.need = char_needs['skill_upgrade'].get(skill_upgrade.id, 0)

        ressource = ressources.filter(id=character.ressource_id).first()
        if ressource:
            ressource.need = char_needs['ressource'].get(ressource.id, 0)


        own_list_asc = [ascension.user_ascension_quantity_lf, ascension.user_ascension_quantity_mf, 
                        ascension.user_ascension_quantity_hf, ascension.user_ascension_quantity_ff] if ascension else [0,0,0,0]
        need_list_asc = [ascension.need_lf, ascension.need_mf, ascension.need_hf, ascension.need_ff] if ascension else [0,0,0,0]

        asc_synthese = calculer_synthese(own_list_asc, need_list_asc)

        if ascension:
            ascension.remains_to_farm_mf = asc_synthese[1]['give_virtuel']
            ascension.remains_to_farm_hf = asc_synthese[2]['give_virtuel']
            ascension.remains_to_farm_ff = asc_synthese[3]['give_virtuel']

        own_list_wa = [weapon_ascension.user_weapon_ascension_quantity_green, weapon_ascension.user_weapon_ascension_quantity_blue, 
                       weapon_ascension.user_weapon_ascension_quantity_purple, weapon_ascension.user_weapon_ascension_quantity_yellow] if weapon_ascension else [0,0,0,0]
        need_list_wa = [weapon_ascension.need_green, weapon_ascension.need_blue, weapon_ascension.need_purple, weapon_ascension.need_yellow] if weapon_ascension else [0,0,0,0]

        wa_synthese = calculer_synthese(own_list_wa, need_list_wa)

        if weapon_ascension:
            weapon_ascension.remains_to_farm_blue = wa_synthese[1]['give_virtuel']
            weapon_ascension.remains_to_farm_purple = wa_synthese[2]['give_virtuel']
            weapon_ascension.remains_to_farm_yellow = wa_synthese[3]['give_virtuel']

        list_user_characters.append({
            'id': uc.id,
            'statisitics': uc,
            'active': uc.active,
            'character': character,
            'ascension': ascension,
            'resonator_ascension': resonator_ascension,
            'ressource': ressource,
            'skill_upgrade': skill_upgrade,
            'weapon_ascension': weapon_ascension,
            'needed_materials': uc.get_needed_materials(),
            'need_list': {
                'ascension': need_list_asc,
                'weapon_ascension': need_list_wa,
                'resonator_ascension': resonator_ascension.need if resonator_ascension else 0,
            },
        })

def build_user_weapons(user_weapons, list_user_weapons, total_needed, ascensions, weapon_ascensions):
    for uw in user_weapons:
        weapon_needs = uw.get_needed_materials()
        if uw.active:
            for aid, tiers in weapon_needs['ascension'].items():
                total_needed['ascension'].setdefault(aid, {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 0})
                for tier, qty in tiers.items():
                    total_needed['ascension'][aid][tier] += qty

            for waid, colors in weapon_needs['weapon_ascension'].items():
                total_needed['weapon_ascension'].setdefault(waid, {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 0})
                for color, qty in colors.items():
                    total_needed['weapon_ascension'][waid][color] += qty

        weapon = Weapon.objects.filter(id=uw.weapon.id).first()
        weapon.rarity_range = range(weapon.rarity)


        ascension = ascensions.filter(id=weapon.ascension_id).first()
        if ascension:
            asc_data = weapon_needs['ascension'].get(ascension.id, {})
            ascension.need_lf = asc_data.get('lf', 0)
            ascension.need_mf = asc_data.get('mf', 0)
            ascension.need_hf = asc_data.get('hf', 0)
            ascension.need_ff = asc_data.get('ff', 0)

        weapon_ascension = weapon_ascensions.filter(id=weapon.weapon_ascension_id).first()
        if weapon_ascension:
            wa_data = weapon_needs['weapon_ascension'].get(weapon_ascension.id, {}) if weapon_ascension else {}
            weapon_ascension.need_green = wa_data.get('green', 0)
            weapon_ascension.need_blue = wa_data.get('blue', 0)
            weapon_ascension.need_purple = wa_data.get('purple', 0)
            weapon_ascension.need_yellow = wa_data.get('yellow', 0)


        own_list_asc = [ascension.user_ascension_quantity_lf, ascension.user_ascension_quantity_mf, 
                        ascension.user_ascension_quantity_hf, ascension.user_ascension_quantity_ff] if ascension else [0,0,0,0]
        need_list_asc = [ascension.need_lf, ascension.need_mf, ascension.need_hf, ascension.need_ff] if ascension else [0,0,0,0]

        asc_synthese = calculer_synthese(own_list_asc, need_list_asc)

        if ascension:
            ascension.remains_to_farm_mf = asc_synthese[1]['give_virtuel']
            ascension.remains_to_farm_hf = asc_synthese[2]['give_virtuel']
            ascension.remains_to_farm_ff = asc_synthese[3]['give_virtuel']

        own_list_wa = [weapon_ascension.user_weapon_ascension_quantity_green, weapon_ascension.user_weapon_ascension_quantity_blue, 
                       weapon_ascension.user_weapon_ascension_quantity_purple, weapon_ascension.user_weapon_ascension_quantity_yellow] if weapon_ascension else [0,0,0,0]
        need_list_wa = [weapon_ascension.need_green, weapon_ascension.need_blue, weapon_ascension.need_purple, weapon_ascension.need_yellow] if weapon_ascension else [0,0,0,0]

        wa_synthese = calculer_synthese(own_list_wa, need_list_wa)

        if weapon_ascension:
            weapon_ascension.remains_to_farm_blue = wa_synthese[1]['give_virtuel']
            weapon_ascension.remains_to_farm_purple = wa_synthese[2]['give_virtuel']
            weapon_ascension.remains_to_farm_yellow = wa_synthese[3]['give_virtuel']

        list_user_weapons.append({
            'id': uw.id,
            'active': uw.active,
            'statisitics': uw,
            'weapon': weapon,
            'ascension': ascension,
            'weapon_ascension': weapon_ascension,
            'needed_materials': uw.get_needed_materials(),
            'need_list': {
                'ascension': need_list_asc,
                'weapon_ascension': need_list_wa,
            },
        })

def build_need_and_quantity_individually(total_needed, ressources, resonator_ascensions, skill_upgrades, ascensions, weapon_ascensions):
    for r in ressources:
        r.need = total_needed['resonator_ascension'].get(r.id, 0)

    for ra in resonator_ascensions:
        ra.need = total_needed['resonator_ascension'].get(ra.id, 0)

    for su in skill_upgrades:
        su.need = total_needed['skill_upgrade'].get(su.id, 0)

    for a in ascensions:
        asc_data = total_needed['ascension'].get(a.id, {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 0})
        a.need_lf = asc_data['lf']
        a.need_mf = asc_data['mf']
        a.need_hf = asc_data['hf']
        a.need_ff = asc_data['ff']

        own_list = [a.user_ascension_quantity_lf, a.user_ascension_quantity_mf, 
                    a.user_ascension_quantity_hf, a.user_ascension_quantity_ff]

        need_list = [a.need_lf, a.need_mf, a.need_hf, a.need_ff]
        
        synthese = calculer_synthese(own_list, need_list)

        a.remains_to_farm_mf = synthese[1]['give_virtuel']
        a.remains_to_farm_hf = synthese[2]['give_virtuel']
        a.remains_to_farm_ff = synthese[3]['give_virtuel']

    for wa in weapon_ascensions:
        wa_data = total_needed['weapon_ascension'].get(wa.id, {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 0})
        wa.need_green = wa_data['green']
        wa.need_blue = wa_data['blue']
        wa.need_purple = wa_data['purple']
        wa.need_yellow = wa_data['yellow']

        own_list = [wa.user_weapon_ascension_quantity_green, wa.user_weapon_ascension_quantity_blue, 
                    wa.user_weapon_ascension_quantity_purple, wa.user_weapon_ascension_quantity_yellow]

        need_list = [wa.need_green, wa.need_blue, wa.need_purple, wa.need_yellow]

        synthese = calculer_synthese(own_list, need_list)

        wa.remains_to_farm_blue = synthese[1]['give_virtuel']
        wa.remains_to_farm_purple = synthese[2]['give_virtuel']
        wa.remains_to_farm_yellow = synthese[3]['give_virtuel']
