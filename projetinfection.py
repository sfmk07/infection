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

    # Calcul du nombre de nouvelles infections et mise à jour du nombre total d'infectés
    infectes = infectes * (1 - PG)
    nouveau_infectes = (infectes * (population - infectes) * rencontres * PT) / population
    infectes += nouveau_infectes

    # Enregistrement du nombre total de personnes infectées et de nouvelles infections pour analyse ultérieure
    infectes_par_jour += [infectes]
    nouveau_infectes_par_jour += [nouveau_infectes]

    jour += 1

# Simulation de la guérison avec un vaccin après les 365 jours
jours_apres_365 = 30
taux_guerison_vaccin = 0.01   

jour = 366
while jour < 366 + jours_apres_365:
    # Calcul de la guérison avec le vaccin et mise à jour du nombre total d'infectés
    infectes = infectes * (1 - PG)
    gueris = infectes * taux_guerison_vaccin
    infectes -= gueris

    # Enregistrement du nombre total de personnes infectées pour analyse ultérieure
    infectes_par_jour += [infectes]
    nouveau_infectes_par_jour += [0]  # Aucune nouvelle infection après les 365 jours

    jour += 1