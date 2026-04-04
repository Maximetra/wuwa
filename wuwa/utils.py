def calculer_synthese(possede, requis):
    niveaux = len(possede)
    surplus_virtuel = 0
    resultats = []

    for i in range(niveaux):
        own = possede[i]
        need = requis[i]
        
        stock_total_disponible = own + surplus_virtuel
        vrai_manquant = need - own if need > own else 0

        if vrai_manquant > 0:
            give_virtuel = min(vrai_manquant, surplus_virtuel)
        else:
            give_virtuel = 0

        manquant = need - stock_total_disponible
        manque_apres_synthese = manquant if manquant > 0 else 0

        reste = stock_total_disponible - need
        old_surplus_virtuel = surplus_virtuel

        if reste > 0:
            surplus_virtuel = reste // 3
        else:
            surplus_virtuel = 0

        resultats.append({
            'total_virtuel': stock_total_disponible,
            'manque': manque_apres_synthese,
            'suffisant': stock_total_disponible >= need,
            'surplus': old_surplus_virtuel,
            'give_virtuel': give_virtuel,
        })

    return resultats
