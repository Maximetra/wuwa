from django import forms
from django.contrib import admin
from wuwa.models import Ascension, MainForte, MinorForte, UserAscension, Character, Element, ResonatorAscension, Ressource, SkillUpgrade, User, UserCharacter, UserResonatorAscension, UserRessource, UserWeapon, UserWeaponAscension, Weapon, WeaponAscension, WeaponType

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['name', 'image']
        exclude = []

class ElementAdmin(admin.ModelAdmin):
    form = ElementForm


class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['name', 'image']
        exclude = []

class RessourceAdmin(admin.ModelAdmin):
    form = RessourceForm


class AscensionForm(forms.ModelForm):
    class Meta:
        model = Ascension
        fields = ['lf_name', 'lf_image', 'mf_name', 'mf_image', 'hf_name', 'hf_image', 'ff_name', 'ff_image']
        exclude = []

class AscensionAdmin(admin.ModelAdmin):
    form = AscensionForm


class ResonatorAscensionForm(forms.ModelForm):
    class Meta:
        model = ResonatorAscension
        fields = ['name', 'image']
        exclude = []

class ResonatorAscensionAdmin(admin.ModelAdmin):
    form = ResonatorAscensionForm


class WeaponAscensionForm(forms.ModelForm):
    class Meta:
        model = WeaponAscension
        fields = ['green_name', 'green_image', 'blue_name', 'blue_image', 'purple_name', 'purple_image', 'yellow_name', 'yellow_image']
        exclude = []

class WeaponAscensionAdmin(admin.ModelAdmin):
    form = WeaponAscensionForm


class SkillUpgradeForm(forms.ModelForm):
    class Meta:
        model = SkillUpgrade
        fields = ['name', 'image']
        exclude = []

class SkillUpgradeAdmin(admin.ModelAdmin):
    form = SkillUpgradeForm


class MainForteForm(forms.ModelForm):
    class Meta:
        model = MainForte
        fields = ['name', 'image']
        exclude = []

class MainForteAdmin(admin.ModelAdmin):
    form = MainForteForm


class MinorForteForm(forms.ModelForm):
    class Meta:
        model = MinorForte
        fields = ['name', 'image']
        exclude = []

class MinorForteAdmin(admin.ModelAdmin):
    form = MinorForteForm


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'image', 'rarity', 'ressource', 'ascension', 'skill_upgrade', 'resonator_ascension', 'weapon_type', 'weapon_ascension', 
            'main_forte', 'minor_forte', 'inherent_skill_1', 'inherent_skill_2', 'release_date'
        ]
        exclude = []

class CharacterAdmin(admin.ModelAdmin):
    form = CharacterForm


class WeaponTypeForm(forms.ModelForm):
    class Meta:
        model = WeaponType
        fields = ['name', 'image']
        exclude = []

class WeaponTypeAdmin(admin.ModelAdmin):
    form = WeaponTypeForm


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'image', 'weapon_type', 'weapon_ascension', 'ascension', 'release_date']
        exclude = []

class WeaponAdmin(admin.ModelAdmin):
    form = WeaponForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        exclude = []

class UserAdmin(admin.ModelAdmin):
    form = UserForm

class UserCharacterForm(forms.ModelForm):
    class Meta:
        model = UserCharacter
        fields = [
            'user', 'character',
            'min_level', 'max_level',
            'min_normal_attack_level', 'max_normal_attack_level',
            'min_resonance_skill_level', 'max_resonance_skill_level',
            'min_resonance_liberation_level', 'max_resonance_liberation_level',
            'min_forte_circuit_level', 'max_forte_circuit_level',
            'min_intro_skill_level', 'max_intro_skill_level',
            'first_tier_trace1', 'first_tier_trace2', 'first_tier_trace3', 'first_tier_trace4',
            'second_tier_trace1', 'second_tier_trace2', 'second_tier_trace3', 'second_tier_trace4',
            'active',
            ]
        exclude = []

class UserCharacterAdmin(admin.ModelAdmin):
    form = UserCharacterForm

class UserWeaponForm(forms.ModelForm):
    class Meta:
        model = UserWeapon
        fields = [
            'user', 'weapon',
            'min_level', 'max_level',
            'active',
            ]
        exclude = []

class UserWeaponAdmin(admin.ModelAdmin):
    form = UserWeaponForm

class UserRessourceForm(forms.ModelForm):
    class Meta:
        model = UserRessource
        fields = ['user', 'ressource', 'quantity']
        exclude = []

class UserRessourceAdmin(admin.ModelAdmin):
    form = UserRessourceForm

class UserAscensionForm(forms.ModelForm):
    class Meta:
        model = UserAscension
        fields = ['user', 'ascension', 'quantity_lf', 'quantity_mf', 'quantity_hf', 'quantity_ff']
        exclude = []

class UserAscensionAdmin(admin.ModelAdmin):
    form = UserAscensionForm

class UserWeaponAscensionForm(forms.ModelForm):
    class Meta:
        model = UserWeaponAscension
        fields = ['user', 'weapon_ascension', 'quantity_green', 'quantity_blue', 'quantity_purple', 'quantity_yellow']
        exclude = []

class UserWeaponAscensionAdmin(admin.ModelAdmin):
    form = UserWeaponAscensionForm

class UserResonatorAscensionForm(forms.ModelForm):
    class Meta:
        model = UserResonatorAscension
        fields = ['user', 'resonator_ascension', 'quantity']
        exclude = []

class UserResonatorAscensionAdmin(admin.ModelAdmin):
    form = UserResonatorAscensionForm

