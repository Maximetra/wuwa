from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Element(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Ressource(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Ascension(models.Model):
    lf_name = models.CharField(max_length=50)
    lf_image = models.URLField(max_length=255)
    mf_name = models.CharField(max_length=50)
    mf_image = models.URLField(max_length=255)
    hf_name = models.CharField(max_length=50)
    hf_image = models.URLField(max_length=255)
    ff_name = models.CharField(max_length=50)
    ff_image= models.CharField(max_length=255)

    def __str__(self):
        return self.lf_name

class ResonatorAscension(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class WeaponAscension(models.Model):
    green_name = models.CharField(max_length=50)
    green_image = models.URLField(max_length=255)
    blue_name = models.CharField(max_length=50)
    blue_image = models.URLField(max_length=255)
    purple_name = models.CharField(max_length=50)
    purple_image = models.URLField(max_length=255)
    yellow_name = models.CharField(max_length=50)
    yellow_image = models.URLField(max_length=255)

    def __str__(self):
        return self.green_name

class SkillUpgrade(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class WeaponType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.URLField(max_length=255, unique=True)
    release_date = models.DateField(default='2024-05-23')
    rarity = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    weapon_type = models.ForeignKey(WeaponType, on_delete=models.SET_NULL, null=True)
    weapon_ascension = models.ForeignKey(WeaponAscension, on_delete=models.SET_NULL, null=True)
    ascension = models.ForeignKey(Ascension, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.URLField(max_length=255, unique=True)
    minor_forte_1 = models.URLField(max_length=255)
    minor_forte_2 = models.URLField(max_length=255)
    inherent_skill_1 = models.URLField(max_length=255)
    inherent_skill_2 = models.URLField(max_length=255)
    release_date = models.DateField(default='2024-05-23')
    rarity = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    element = models.ForeignKey(Element, on_delete=models.SET_NULL, null=True)
    weapon_type = models.ForeignKey(WeaponType, on_delete=models.SET_NULL, null=True)
    ressource = models.ForeignKey(Ressource, on_delete=models.SET_NULL, null=True)
    ascension = models.ForeignKey(Ascension, on_delete=models.SET_NULL, null=True)
    skill_upgrade = models.ForeignKey(SkillUpgrade, on_delete=models.SET_NULL, null=True)
    resonator_ascension = models.ForeignKey(ResonatorAscension, on_delete=models.SET_NULL, null=True)
    weapon_ascension = models.ForeignKey(WeaponAscension, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    characters = models.ManyToManyField(Character)
    weapons = models.ManyToManyField(Weapon)
    ressources = models.ManyToManyField(Ressource)
    ascensions = models.ManyToManyField(Ascension)

    def __str__(self):
        return self.username
class UserCharacter(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    character = models.ForeignKey('Character', on_delete=models.CASCADE)

    min_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(90)])
    max_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(90)])

    min_normal_attack_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    max_normal_attack_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    min_resonance_skill_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    max_resonance_skill_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    min_resonance_liberation_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    max_resonance_liberation_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    min_forte_circuit_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    max_forte_circuit_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    min_intro_skill_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    max_intro_skill_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    first_tier_trace1 = models.BooleanField(default=False)
    first_tier_trace2 = models.BooleanField(default=False)
    first_tier_trace3 = models.BooleanField(default=False)
    first_tier_trace4 = models.BooleanField(default=False)

    second_tier_trace1 = models.BooleanField(default=False)
    second_tier_trace2 = models.BooleanField(default=False)
    second_tier_trace3 = models.BooleanField(default=False)
    second_tier_trace4 = models.BooleanField(default=False)

    first_inherent_skill = models.BooleanField(default=False)
    second_inherent_skill = models.BooleanField(default=False)

    active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "character"], name="unique_character_user")
        ]

    def __str__(self):
        return f"{self.user.username} - {self.character.name}"

    def get_needed_materials(self):

        totals = {
            'ressource': {},
            'ascension': {},
            'weapon_ascension': {},
            'resonator_ascension': {},
            'skill_upgrade': {}
        }

        char = self.character
        res_id = char.ressource_id
        asc_id = char.ascension_id
        wa_id = char.weapon_ascension_id
        ra_id = char.resonator_ascension_id
        su_id = char.skill_upgrade_id

        def add_res(qty):
            if res_id and qty > 0: totals['ressource'][res_id] = totals['ressource'].get(res_id, 0) + qty
        def add_ra(qty):
            if ra_id and qty > 0: totals['resonator_ascension'][ra_id] = totals['resonator_ascension'].get(ra_id, 0) + qty
        def add_su(qty):
            if su_id and qty > 0: totals['skill_upgrade'][su_id] = totals['skill_upgrade'].get(su_id, 0) + qty
        def add_asc(tier, qty):
            if asc_id and qty > 0:
                totals['ascension'].setdefault(asc_id, {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 0})
                totals['ascension'][asc_id][tier] += qty
        def add_wa(color, qty):
            if wa_id and qty > 0:
                totals['weapon_ascension'].setdefault(wa_id, {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 0})
                totals['weapon_ascension'][wa_id][color] += qty

        CHARACTER_STEPS = {
            20: {'lf': 4},
            40: {'mf': 4, 'ra': 3, 'res': 4},
            60: {'mf': 8, 'hf': 12, 'ra': 27, 'res': 36},
            80: {'ff': 4, 'ra': 16, 'res': 20},
        }

        for step_lvl, costs in CHARACTER_STEPS.items():
            if self.min_level <= step_lvl < self.max_level:
                add_asc('lf', costs.get('lf', 0))
                add_asc('mf', costs.get('mf', 0))
                add_asc('hf', costs.get('hf', 0))
                add_asc('ff', costs.get('ff', 0))
                add_ra(costs.get('ra', 0))
                add_res(costs.get('res', 0))

        SKILL_STEPS = {
            2: {'lf': 2, 'green': 2},
            3: {'lf': 3, 'green': 3},
            4: {'mf': 2, 'blue': 2},
            5: {'mf': 3, 'blue': 3},
            6: {'hf': 2, 'purple': 3},
            7: {'hf': 3, 'purple': 5, 'su': 1},
            8: {'ff': 2, 'yellow': 2, 'su': 1},
            9: {'ff': 3, 'yellow': 3, 'su': 1},
            10: {'ff': 4, 'yellow': 6, 'su': 1},
        }

        skills_to_calculate = [
            (self.min_normal_attack_level, self.max_normal_attack_level),
            (self.min_resonance_skill_level, self.max_resonance_skill_level),
            (self.min_resonance_liberation_level, self.max_resonance_liberation_level),
            (self.min_forte_circuit_level, self.max_forte_circuit_level),
            (self.min_intro_skill_level, self.max_intro_skill_level),
        ]

        for current_lv, target_lv in skills_to_calculate:
            for lvl, costs in SKILL_STEPS.items():
                if current_lv < lvl <= target_lv:
                    add_asc('lf', costs.get('lf', 0))
                    add_asc('mf', costs.get('mf', 0))
                    add_asc('hf', costs.get('hf', 0))
                    add_asc('ff', costs.get('ff', 0))
                    add_wa('green', costs.get('green', 0))
                    add_wa('blue', costs.get('blue', 0))
                    add_wa('purple', costs.get('purple', 0))
                    add_wa('yellow', costs.get('yellow', 0))
                    add_su(costs.get('su', 0))

        for i in range(1, 5):
            if getattr(self, f'first_tier_trace{i}'):
                add_asc('hf', 3)
                add_wa('purple', 3)
            if getattr(self, f'second_tier_trace{i}'):
                add_asc('ff', 3)
                add_wa('yellow', 3)
                add_su(1)

        if self.first_inherent_skill:
            add_asc('mf', 3)
            add_wa('blue', 3)
            add_su(1)
        if self.second_inherent_skill:
            add_asc('hf', 3)
            add_wa('purple', 3)
            add_su(1)

        return totals

class UserRessource(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ressource = models.ForeignKey(Ressource, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "ressource"], name="unique_ressource_user"
            )
        ]

    def __str__(self):
        return self.user.username + " - " + self.ressource.name

class UserAscension(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ascension = models.ForeignKey(Ascension, on_delete=models.SET_NULL, null=True)
    quantity_lf = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])
    quantity_mf = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])
    quantity_hf = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])
    quantity_ff = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "ascension"], name="unique_ascension_user"
            )
        ]

    def __str__(self):
        return self.user.username + " - " + self.ascension.lf_name + " | " + self.ascension.mf_name + " | " + self.ascension.hf_name + " | " + self.ascension.ff_name

class UserWeaponAscension(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    weapon_ascension = models.ForeignKey(WeaponAscension, on_delete=models.SET_NULL, null=True)

    quantity_green = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])
    quantity_blue = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])
    quantity_purple = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])
    quantity_yellow = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "weapon_ascension"], name="unique_weapon_ascension_user"
            )
        ]

    def __str__(self):
        return self.user.username + " - " + self.weapon_ascension.green_name + " | " + self.weapon_ascension.blue_name + " | " + self.weapon_ascension.purple_name + " | " + self.weapon_ascension.yellow_name

class UserWeapon(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    weapon = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True)

    min_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(90)])
    max_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(90)])

    active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "weapon"], name="unique_weapon_user"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.weapon.name}"
    
    def get_needed_materials(self):
        base_return = {
            'weapon_ascension': {self.weapon.weapon_ascension_id: {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 0}},
            'ascension': {self.weapon.ascension_id: {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 0}}
        }

        if not self.active or self.min_level >= self.max_level:
            return base_return

        LEVEL_STEPS = {
            20: {
                'asc': {'lf': 6, 'mf': 0, 'hf': 0, 'ff': 0},
                'wa': {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 0}
            },
            40: {
                'asc': {'lf': 0, 'mf': 6, 'hf': 0, 'ff': 0},
                'wa': {'green': 6, 'blue': 0, 'purple': 0, 'yellow': 0}
            },
            50: {
                'asc': {'lf': 0, 'mf': 0, 'hf': 4, 'ff': 0},
                'wa': {'green': 0, 'blue': 8, 'purple': 0, 'yellow': 0}
            },
            60: {
                'asc': {'lf': 0, 'mf': 0, 'hf': 6, 'ff': 0},
                'wa': {'green': 0, 'blue': 0, 'purple': 6, 'yellow': 0}
            },
            70: {
                'asc': {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 4},
                'wa': {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 8}
            },
            80: {
                'asc': {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 8},
                'wa': {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 12}
            },
        }

        needed_wa = {'green': 0, 'blue': 0, 'purple': 0, 'yellow': 0}
        needed_asc = {'lf': 0, 'mf': 0, 'hf': 0, 'ff': 0}

        for step_level, costs in LEVEL_STEPS.items():
            if step_level > self.min_level and step_level <= self.max_level:
                for key in needed_wa:
                    needed_wa[key] += costs['wa'].get(key, 0)
                
                for key in needed_asc:
                    needed_asc[key] += costs['asc'].get(key, 0)

        return {
            'weapon_ascension': {
                self.weapon.weapon_ascension_id: needed_wa
            },
            'ascension': {
                self.weapon.ascension_id: needed_asc
            }
        }

class UserResonatorAscension(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resonator_ascension = models.ForeignKey(ResonatorAscension, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "resonator_ascension"], name="unique_resonator_ascension_user"
            )
        ]

    def __str__(self):
        return self.user.username + " - " + self.resonator_ascension.name

class UserSkillUpgrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill_upgrade = models.ForeignKey(SkillUpgrade, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(9999)
    ])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "skill_upgrade"], name="unique_skill_upgrade_user"
            )
        ]

    def __str__(self):
        return self.user.username + " - " + self.skill_upgrade.name
