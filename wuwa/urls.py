"""
URL configuration for wuwa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import forms
from django.contrib import admin
from django.urls import path
from wuwa.models import MainForte, MinorForte, UserAscension, Element, Ressource, Ascension, ResonatorAscension, User, UserCharacter, UserResonatorAscension, UserRessource, UserWeapon, UserWeaponAscension, Weapon, WeaponAscension, SkillUpgrade, Character, WeaponType
from wuwa.view.admin import AscensionAdmin, MainForteAdmin, MinorForteAdmin, UserAscensionAdmin, CharacterAdmin, ElementAdmin, ResonatorAscensionAdmin, RessourceAdmin, SkillUpgradeAdmin, UserAdmin, UserCharacterAdmin, UserResonatorAscensionAdmin, UserRessourceAdmin, UserWeaponAdmin, UserWeaponAscensionAdmin, WeaponAdmin, WeaponAscensionAdmin, WeaponTypeAdmin
from wuwa.view.ascension import get_ascension_api, update_ascension_api
from wuwa.view.character import get_character_api
from wuwa.view.progression import get_progression_view
from wuwa.view.resonator_ascension import update_resonator_ascension_api
from wuwa.view.ressource import update_ressource_api
from wuwa.view.skill_upgrade import update_skill_upgrade_api
from wuwa.view.user import login_view, logout_view, register_view
from wuwa.view.user_character import get_user_character_api, remove_user_character_api, update_or_create_user_character_api
from wuwa.view.user_weapon import get_user_weapon_api, remove_user_weapon_api, update_or_create_user_weapon_api
from wuwa.view.weapon import get_weapon_api
from wuwa.view.weapon_ascension import get_weapon_ascension_api, update_weapon_ascension_api

admin.site.register(Ascension, AscensionAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(MainForte, MainForteAdmin)
admin.site.register(MinorForte, MinorForteAdmin)
admin.site.register(Ressource, RessourceAdmin)
admin.site.register(ResonatorAscension, ResonatorAscensionAdmin)
admin.site.register(SkillUpgrade, SkillUpgradeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserAscension, UserAscensionAdmin)
admin.site.register(UserCharacter, UserCharacterAdmin)
admin.site.register(UserRessource, UserRessourceAdmin)
admin.site.register(UserWeapon, UserWeaponAdmin)
admin.site.register(WeaponAscension, WeaponAscensionAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(WeaponType, WeaponTypeAdmin)
admin.site.register(UserWeaponAscension, UserWeaponAscensionAdmin)
admin.site.register(UserResonatorAscension, UserResonatorAscensionAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_progression_view, name='progession_view'),
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('character/<int:character_id>/', get_character_api, name='character_api'),
    path('weapon/<int:weapon_id>/', get_weapon_api, name='weapon_api'),
    path('ascension/<int:ascension_id>/', get_ascension_api, name='ascension_api'),
    path('user_character/<int:user_character_id>/', get_user_character_api, name='user_character_api'),
    path('user_weapon/<int:user_weapon_id>/', get_user_weapon_api, name='user_weapon_api'),
    path('weapon_ascension/<int:weapon_ascension_id>/', get_weapon_ascension_api, name='weapon_ascension_api'),
    path('update_ressource/', update_ressource_api, name='update_ressource_api'),
    path('update_ascension/', update_ascension_api, name='update_ascension_api'),
    path('update_weapon_ascension/', update_weapon_ascension_api, name='update_weapon_ascension_api'),
    path('update_resonator_ascension/', update_resonator_ascension_api, name='update_resonator_ascension_api'),
    path('update_skill_upgrade/', update_skill_upgrade_api, name='update_skill_upgrade_api'),
    path('update_user_character/', update_or_create_user_character_api, name='update_or_create_user_character_api'),
    path('update_user_weapon/', update_or_create_user_weapon_api, name='update_or_create_user_weapon_api'),
    path('remove_user_character/', remove_user_character_api, name='remove_user_character_api'),
    path('remove_user_weapon/', remove_user_weapon_api, name='remove_user_weapon_api'),
]
