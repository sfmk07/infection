# Initialisation des paramètres
population = 11500000
infectes = 100
PT = 0.01  # Taux de transmission
PG = 0.05  # Taux de guérison
rencontres = 10
infectes_par_jour = [infectes]  # Liste pour stocker le nombre total de personnes infectées chaque jour
nouveau_infectes_par_jour = [0]  # Liste pour stocker le nombre de nouvelles infections chaque jour

# Modélisation de la propagation de l'infection pendant les 365 premiers jours
jour = 1
while jour < 366:
    # Ajustement du nombre de rencontres pour la période spécifiée
    if 30 <= jour <= 75:
        rencontres = 3
    else:
        rencontres = 10