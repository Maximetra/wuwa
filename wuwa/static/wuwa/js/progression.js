$(document).ready(function () {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    let menu = false

    $("#addCharacterBtn").click(function(e) {
        $('#characterSelectModal').modal('show');
    });

    $("#addWeaponBtn").click(function(e) {
        $('#weaponSelectModal').modal('show');
    });

    $(".ressource_modal").click(function() {
        const current_ressource = $(this);
        
        $('.ressourceModal-image').attr('src', current_ressource.find('.image-item').attr('src'));
        $('.ressourceModal-name').text(current_ressource.find('.image-item').attr('alt'));
        $('.ressourceModal-input').val(current_ressource.find('span.own').text());
        $('#ressourceModalTitle').attr('data-id', current_ressource.attr('data-id'));

        $('.ressourceModal-input').each(function(index) {
            let input_value = $(`.ressource_modal[data-id="${current_ressource.attr('data-id')}"]`).eq(index).find('span.own').text();
            $(this).val(input_value).trigger('input');
        });

        $('#ressourceModal').modal('show');
    });

    $(".resonator_ascension_modal").click(function() {
        const current_resonator_ascension = $(this);
        
        $('.resonatorAscension-image').attr('src', current_resonator_ascension.find('.image-item').attr('src'));
        $('.resonatorAscension-name').text(current_resonator_ascension.find('.image-item').attr('alt'));
        $('.resonatorAscension-input').val(current_resonator_ascension.find('span.own').text());
        $('#resonatorAscensionTitle').attr('data-id', current_resonator_ascension.attr('data-id'));

        $('.resonatorAscension-input').each(function(index) {
            let input_value = $(`.resonator_ascension_modal[data-id="${current_resonator_ascension.attr('data-id')}"]`).eq(index).find('span.own').text();
            
            $(this).val(input_value).trigger('input');
        });

        $('#resonatorAscensionModal').modal('show');
    });

    $(".skill_upgrade_modal").click(function() {
        const current_skill_upgrade = $(this);
        
        $('.skillUpgrade-image').attr('src', current_skill_upgrade.find('.image-item').attr('src'));
        $('.skillUpgrade-name').text(current_skill_upgrade.find('.image-item').attr('alt'));
        $('.skillUpgrade-input').val(current_skill_upgrade.find('span.own').text());
        $('#skillUpgradeTitle').attr('data-id', current_skill_upgrade.attr('data-id'));

        $('.skillUpgrade-input').each(function(index) {
            let input_value = $(`.skill_upgrade_modal[data-id="${current_skill_upgrade.attr('data-id')}"]`).eq(index).find('span.own').text();
            
            $(this).val(input_value).trigger('input');
        });

        $('#skillUpgradeModal').modal('show');
    });

    $(".ascension_modal").click(function() {
        $('#modal-loading').modal('show');
        const current_ascension = $(this);
        
        $.ajax({
            url: '/ascension/' + $(this).data('id'),
            method: 'GET',
            success: function(data) {
                $('#modal-loading').modal('hide');
                let a = data.ascension;
                $('#ascensionModalTitle').attr('data-id', current_ascension.attr('data-id'));
                $('.ascensionModal-image').attr('src', current_ascension.find('.image-item').attr('src'));
                $('.ascensionModal-name').text(current_ascension.find('.image-item').attr('alt'));

                $('#ascensionModal .inv-wrap img').first().attr('src', a.lf_image);
                $('#ascensionModal .inv-wrap label').first().text(a.lf_name);
                $('#ascensionModal .inv-wrap img').eq(1).attr('src', a.mf_image);
                $('#ascensionModal .inv-wrap label').eq(1).text(a.mf_name);
                $('#ascensionModal .inv-wrap img').eq(2).attr('src', a.hf_image);
                $('#ascensionModal .inv-wrap label').eq(2).text(a.hf_name);
                $('#ascensionModal .inv-wrap img').last().attr('src', a.ff_image);
                $('#ascensionModal .inv-wrap label').last().text(a.ff_name);

                $('.ascensionModal-input').each(function(index) {
                    let input_value = $(`.ascension_modal[data-id="${current_ascension.attr('data-id')}"]`).eq(index).find('span.own').text();
                    $(this).val(input_value).trigger('input');
                });

                $('#ascensionModal').modal('show');
            },
            error: function() {
                alert('Failed to load character data.');
            }
        })

        $('.ascensionModal-input').val($(this).find('span.own').text());
        $('#ascensionModalTitle').attr('data-id', $(this).data('id'));
    });

    $(".weapon_ascension_modal").click(function() {
        $('#modal-loading').modal('show');
        const current_weapon_ascension = $(this);
        
        $.ajax({
            url: '/weapon_ascension/' + $(this).data('id'),
            method: 'GET',
            success: function(data) {
                $('#modal-loading').modal('hide');
                let a = data.weapon_ascension;
                $('#weaponAscensionModalTitle').attr('data-id', current_weapon_ascension.attr('data-id'));
                $('.weaponAscensionModal-image').attr('src', current_weapon_ascension.find('.image-item').attr('src'));
                $('.weaponAscensionModal-name').text(current_weapon_ascension.find('.image-item').attr('alt'));

                $('#weaponAscensionModal .inv-wrap img').first().attr('src', a.green_image);
                $('#weaponAscensionModal .inv-wrap label').first().text(a.green_name);
                $('#weaponAscensionModal .inv-wrap img').eq(1).attr('src', a.blue_image);
                $('#weaponAscensionModal .inv-wrap label').eq(1).text(a.blue_name);
                $('#weaponAscensionModal .inv-wrap img').eq(2).attr('src', a.purple_image);
                $('#weaponAscensionModal .inv-wrap label').eq(2).text(a.purple_name);
                $('#weaponAscensionModal .inv-wrap img').last().attr('src', a.yellow_image);
                $('#weaponAscensionModal .inv-wrap label').last().text(a.yellow_name);

                $('.weaponAscensionModal-input').each(function(index) {
                    let input_value = $(`.weapon_ascension_modal[data-id="${current_weapon_ascension.attr('data-id')}"]`).eq(index).find('span.own').text();
                    $(this).val(input_value).trigger('input');
                });

                $('#weaponAscensionModal').modal('show');
            },
            error: function() {
                alert('Failed to load character data.');
            }
        })

        $('.weaponAscensionModal-input').val($(this).find('span.own').text());
        $('#weaponAscensionModalTitle').attr('data-id', $(this).data('id'));
    });

    $(".close, .close-cancel").click(function(e) {
        $(this).closest('.modal').modal('hide');
    });

    $(".character-card").click(function() {
        $('#characterSelectModal').modal('hide');
        $('#modal-loading').modal('show');
        const current_character = $(this);
        $.ajax({
            url: '/character/' + $(this).data('id'),
            method: 'GET',
            success: function(data) {
                $('#modal-loading').modal('hide');
                let c = data.character;
                $('#characterSetupModalTitle').text(c.name);
                $('#characterSetupModalImage').attr('src', c.image).attr('alt', c.name);
                $("#characterSetupModal #stat_bonus .img-fluid").slice(0, 2).attr("src", c.main_forte).attr("alt", c.name + " Minor Forte 1");
                $("#characterSetupModal #stat_bonus .img-fluid").slice(2, 6).attr("src", c.minor_forte).attr("alt", c.name + " Minor Forte 2");
                $("#characterSetupModal #stat_bonus .img-fluid").slice(6, 8).attr("src", c.main_forte).attr("alt", c.name + " Minor Forte 1");

                $("#characterSetupModal #inherent_skill .img-fluid").first().attr("src", c.inherent_skill_1).attr("alt", c.name + " Inherent Skill 1");
                $("#characterSetupModal #inherent_skill .img-fluid").last().attr("src", c.inherent_skill_2).attr("alt", c.name + " Inherent Skill 2");

                $('#characterSetupModal').modal('show').attr('data-id', current_character.attr('data-id'));
            },
            error: function() {
                alert('Failed to load character data.');
            }
        })
    });

    $(".weapon-card").click(function() {
        $('#weaponSelectModal').modal('hide');
        $('#modal-loading').modal('show');
        const current_weapon = $(this);
        $.ajax({
            url: '/weapon/' + $(this).data('id'),
            method: 'GET',
            success: function(data) {
                $('#modal-loading').modal('hide');
                let c = data.weapon;
                $('#weaponSetupModalTitle').text(c.name);
                $('#weaponSetupModalImage').attr('src', c.image).attr('alt', c.name);
                $("#weaponSetupModal #stat_bonus .img-fluid").slice(0, 2).attr("src", c.main_forte).attr("alt", c.name + " Minor Forte 1");
                $("#weaponSetupModal #stat_bonus .img-fluid").slice(2, 6).attr("src", c.minor_forte).attr("alt", c.name + " Minor Forte 2");
                $("#weaponSetupModal #stat_bonus .img-fluid").slice(6, 8).attr("src", c.main_forte).attr("alt", c.name + " Minor Forte 1");

                $("#weaponSetupModal #inherent_skill .img-fluid").first().attr("src", c.inherent_skill_1).attr("alt", c.name + " Inherent Skill 1");
                $("#weaponSetupModal #inherent_skill .img-fluid").last().attr("src", c.inherent_skill_2).attr("alt", c.name + " Inherent Skill 2");

                $('#weaponSetupModal').modal('show').attr('data-id', current_weapon.attr('data-id'));
            },
            error: function() {
                alert('Failed to load weapon data.');
            }
        })
    });

    $(".image-checkbox").each(function () {
        if ($(this).find('input[type="checkbox"]').first().prop("checked")) {
            $(this).addClass("image-checkbox-checked");
            $(this).find(".fa-check").removeClass("d-none");
        } else {
            $(this).removeClass("image-checkbox-checked");
            $(this).find(".fa-check").addClass("d-none");
        }
    });

    $(".image-checkbox").on("click", function (e) {
        var $checkbox = $(this).find('input[type="checkbox"]');

        $checkbox.prop("checked", !$checkbox.prop("checked"));

        $(this).toggleClass("image-checkbox-checked");
        $(this).find(".fa-check").toggleClass("d-none");

        e.preventDefault();
    });

    $(".menu-btn").click(function(e) {
        e.stopPropagation(); 
        
        let $menu = $(this).closest('.plan-header').find('.menu');
        
        $menu.toggleClass('show');
        
        menu = $menu.hasClass('show');
    });

    $(document).on('click', function(e) {
        if ($('.plan-header .menu').hasClass('show')) {
            $('.plan-header .menu').removeClass('show');
            menu = false;
        }
    });

    $(".remove-character_btn").click(function(e) {
        $('#removeCharacterModal-description').text(`Are you sure you want to delete ${$(this).data('name')}?`);
        $("#removeCharacterModal-character").attr('src', $(this).data('image_name')).attr('alt', $(this).data('name'));
        $('#removeCharacterModal').attr('data-id', $(this).data('id')).modal('show');
    });

    $(".remove-weapon_btn").click(function(e) {
        $('#removeWeaponModal-description').text(`Are you sure you want to delete ${$(this).data('name')}?`);
        $("#removeWeaponModal-weapon").attr('src', $(this).data('image_name')).attr('alt', $(this).data('name'));
        $('#removeWeaponModal').attr('data-id', $(this).data('id')).modal('show');
    });

    $(".edit-character_btn").click(function() {
        $('#modal-loading').modal('show');
        const current_character = $(this);
        $.ajax({
            url: '/user_character/' + $(this).data('id'),
            method: 'GET',
            success: function(data) {
                $('#modal-loading').modal('hide');
                let c = data;
                
                $('#characterSetupModalTitle').text(c.name);
                $('#characterSetupModalImage').attr('src', c.image).attr('alt', c.name);

                $("#characterSetupModal #character-min_level").val(parseInt(c.min_level));
                $("#characterSetupModal #character-min_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.min_level));
                $("#characterSetupModal #character-max_level").val(parseInt(c.max_level));
                $("#characterSetupModal #character-max_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.max_level));

                $("#characterSetupModal #min_normal_attack_level").val(parseInt(c.min_normal_attack_level));
                $("#characterSetupModal #min_normal_attack_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.min_normal_attack_level));
                $("#characterSetupModal #max_normal_attack_level").val(parseInt(c.max_normal_attack_level));
                $("#characterSetupModal #max_normal_attack_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.max_normal_attack_level));

                $("#characterSetupModal #min_resonance_skill_level").val(parseInt(c.min_resonance_skill_level));
                $("#characterSetupModal #min_resonance_skill_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.min_resonance_skill_level));
                $("#characterSetupModal #max_resonance_skill_level").val(parseInt(c.max_resonance_skill_level));
                $("#characterSetupModal #max_resonance_skill_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.max_resonance_skill_level));

                $("#characterSetupModal #min_resonance_liberation_level").val(parseInt(c.min_resonance_liberation_level));
                $("#characterSetupModal #min_resonance_liberation_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.min_resonance_liberation_level));
                $("#characterSetupModal #max_resonance_liberation_level").val(parseInt(c.max_resonance_liberation_level));
                $("#characterSetupModal #max_resonance_liberation_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.max_resonance_liberation_level));

                $("#characterSetupModal #min_forte_circuit_level").val(parseInt(c.min_forte_circuit_level));
                $("#characterSetupModal #min_forte_circuit_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.min_forte_circuit_level));
                $("#characterSetupModal #max_forte_circuit_level").val(parseInt(c.max_forte_circuit_level));
                $("#characterSetupModal #max_forte_circuit_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.max_forte_circuit_level));

                $("#characterSetupModal #min_intro_skill_level").val(parseInt(c.min_intro_skill_level));
                $("#characterSetupModal #min_intro_skill_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.min_intro_skill_level));
                $("#characterSetupModal #max_intro_skill_level").val(parseInt(c.max_intro_skill_level));
                $("#characterSetupModal #max_intro_skill_level").closest('.input-container').find('input[type="range"]').val(parseInt(c.max_intro_skill_level));

                if (c.first_tier_trace1) {
                    let $checkbox = $("#first_tier_trace1");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.first_tier_trace2) {
                    let $checkbox = $("#first_tier_trace2");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.first_tier_trace3) {
                    let $checkbox = $("#first_tier_trace3");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.first_tier_trace4) {
                    let $checkbox = $("#first_tier_trace4");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.second_tier_trace1) {
                    let $checkbox = $("#second_tier_trace1");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.second_tier_trace2) {
                    let $checkbox = $("#second_tier_trace2");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.second_tier_trace3) {
                    let $checkbox = $("#second_tier_trace3");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.second_tier_trace4) {
                    let $checkbox = $("#second_tier_trace4");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.first_inherent_skill) {
                    let $checkbox = $("#first_inherent_skill");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }

                if (c.second_inherent_skill) {
                    let $checkbox = $("#second_inherent_skill");
                    $checkbox.prop('checked', true);
                    $checkbox.closest('.image-checkbox').addClass('image-checkbox-checked').find(".fa-check").removeClass("d-none");
                }


                $("#characterSetupModal #stat_bonus .img-fluid").slice(0, 2).attr("src", c.main_forte).attr("alt", c.name + " Minor Forte 1");
                $("#characterSetupModal #stat_bonus .img-fluid").slice(2, 6).attr("src", c.minor_forte).attr("alt", c.name + " Minor Forte 2");
                $("#characterSetupModal #stat_bonus .img-fluid").slice(6, 8).attr("src", c.main_forte).attr("alt", c.name + " Minor Forte 1");

                $("#characterSetupModal #inherent_skill .img-fluid").first().attr("src", c.inherent_skill_1).attr("alt", c.name + " Inherent Skill 1");
                $("#characterSetupModal #inherent_skill .img-fluid").last().attr("src", c.inherent_skill_2).attr("alt", c.name + " Inherent Skill 2");

                $('#characterSelectModal').modal('hide');
                $('#characterSetupModal').modal('show').attr('data-id', current_character.attr('data-characterId'));
            },
            error: function() {
                alert('Failed to load user character data.');
            }
        })
    });

    $(".edit-weapon_btn").click(function() {
        $('#modal-loading').modal('show');
        const current_weapon = $(this);
        $.ajax({
            url: '/user_weapon/' + $(this).data('id'),
            method: 'GET',
            success: function(data) {
                $('#modal-loading').modal('hide');
                const w = data;
                
                $('#weaponSetupModalTitle').text(w.name);
                $('#weaponSetupModalImage').attr('src', w.image).attr('alt', w.name);

                $("#weaponSetupModal #weapon-min_level").val(parseInt(w.min_level));
                $("#weaponSetupModal #weapon-min_level").closest('.input-container').find('input[type="range"]').val(parseInt(w.min_level));
                $("#weaponSetupModal #weapon-max_level").val(parseInt(w.max_level));
                $("#weaponSetupModal #weapon-max_level").closest('.input-container').find('input[type="range"]').val(parseInt(w.max_level));

                $('#weaponSelectModal').modal('hide');
                $('#weaponSetupModal').modal('show').attr('data-id', current_weapon.attr('data-weaponId'));
            },
            error: function() {
                alert('Failed to load user weapon data.');
            }
        })
    });

    $('.character-active').click(function() {
        const character_id = $(this).data('id');
        const isActive = $(this).is(':checked');
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]') ? 
                document.querySelector('[name=csrfmiddlewaretoken]').value : 
                getCookie('csrftoken');

        $('#modal-loading').modal('show');

        $.ajax({
            url: '/update_user_character/',
            method: 'POST',
            contentType: 'application/json',
            headers: {'X-CSRFToken': csrftoken},
            data: JSON.stringify({
                character_id: character_id,
                active: isActive
            }),
            success: function(res) {
                history.go(0);
            },
            error: function(xhr, status, error) {
                alert('Error updating ressource: ' + error);
            }
        });
    })

    $('.weapon-active').click(function() {
        const weapon_id = $(this).data('id');
        const isActive = $(this).is(':checked');
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]') ? 
                document.querySelector('[name=csrfmiddlewaretoken]').value : 
                getCookie('csrftoken');

        $('#modal-loading').modal('show');

        $.ajax({
            url: '/update_user_weapon/',
            method: 'POST',
            contentType: 'application/json',
            headers: {'X-CSRFToken': csrftoken},
            data: JSON.stringify({
                weapon_id: weapon_id,
                active: isActive
            }),
            success: function(res) {
                history.go(0);
            },
            error: function(xhr, status, error) {
                alert('Error updating ressource: ' + error);
            }
        });
    })

    $('.view-details_btn').click(function (e) { 
        $(this).closest('.plans-grid').find('.plan-details').toggleClass('d-none');
    });
});