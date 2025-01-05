"""
### Examen Final - Logique d'Évitement

Dans ce fichier, vous allez implémenter la fonction `avoidance_logic` pour gérer la logique d'évitement des obstacles du rover.  
La logique est basée sur les capteurs du rover :
1. **Capteurs de pare-chocs (left_bumper et right_bumper que vous retrouvez dans le fichier sensors.py)** :
   - Si un obstacle est détecté, le rover doit reculer et amorcer une manœuvre d'évitement.
2. **Capteur de sol (ground_sensor)** :
   - Si la zone d'arrivée est détectée (valeur du ground_sensor située entre 48 et 50, qui correspond à la couleur vert de l'arrivée), 
      le rover doit s'arrêter.
   - Si la valeur dépasse 43 (qui correspond à une couleur plus claire que noir, ici on définit le 43 comme étant un passage sur la couleur 
      blanc), le rover doit tourner pour revenir à la ligne noire.
   - Sinon, avancer en ligne droite.

Le compteur `avoidance_counter` est utilisé pour gérer les étapes d'évitement dans le temps, ce dernier est défini en fonction de si le rover
   a touché un obstacle ou non :
- Lorsqu'il est supérieur à 0 c'est qu'il a touché un obstacle, et qu'il doit reculer pour l'éviter (On peut définir une valeur à 1000 
   qui décrémente à chaque miliseconde qui passe)
- Sinon, s'il vaut 0, c'est qu'il suit la ligne noire qui est tracée dans le plan.

À compléter :
- Analysez les valeurs des capteurs pour définir `left_speed`, `right_speed` et mettre à jour `avoidance_counter` en fonction de comment 
   le robot doit bouger.
- Respectez la logique d'évitement décrite ci-dessus.
"""

def avoidance_logic(sensors, avoidance_counter):
    left_bumper_value = sensors["left_bumper"].getValue()
    right_bumper_value = sensors["right_bumper"].getValue()
    ground_sensor_value = sensors["ground_sensor"].getValue()

    left_speed = 1
    right_speed = 1
    avoidance_counter = 0

    return left_speed, right_speed, avoidance_counter
