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

# Affichage des résultats
jour_demande = int(input("Entrez le numéro d'un jour (de 1 à 365) : "))
while jour_demande != 0:
    print(f"Le nombre de personnes infectées le jour {jour_demande} est : {infectes_par_jour[jour_demande - 1]}")
    jour_demande = int(input("Entrez le numéro d'un jour (de 1 à 365) : "))

# Calcul et affichage des moyennes
moyenne_infectes = sum(infectes_par_jour) / len(infectes_par_jour)
print(f"Le nombre moyen de personnes infectées par jour sur l'ensemble de l'année est : {moyenne_infectes}")

moyenne_nouvelles_infections = sum(nouveau_infectes_par_jour) / len(nouveau_infectes_par_jour)
print(f"Le nombre moyen de nouvelles infections par jour sur l'ensemble de l'année est : {moyenne_nouvelles_infections}")