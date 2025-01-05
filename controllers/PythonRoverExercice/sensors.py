"""
### Examen Final - Configuration des Capteurs

Dans ce fichier, vous allez implémenter une fonction pour initialiser les capteurs du rover.
Vous devez configurer les capteurs suivants :
1. **left_bumper** : Un capteur tactile représentant le pare-chocs gauche.
2. **ground_sensor** : Un capteur de distance ou de lumière mesurant la surface sous le rover.
3. **right_bumper** : Un capteur tactile représentant le pare-chocs droit.

Chaque capteur doit être activé avec une période de mise à jour de 64 ms.

Retour attendu :
- La fonction `initialize_sensors` doit retourner un dictionnaire contenant ces trois capteurs.

À compléter :
- Utilisez `robot.getDevice(nom_du_capteur)` pour récupérer un capteur.
- À savoir que le capteur du bumper gauche s'appelle 'S1', celui du capteur sensoriel est 'S2' et celui du bumper droit est 'S3'.
- Utilisez la méthode `enable(temps_en_milisecondes)` sur chaque capteur pour l'activer.
"""

def initialize_sensors(robot):

    left_bumper = None
    ground_sensor = None
    right_bumper = None

    return {
        "left_bumper": left_bumper,
        "ground_sensor": ground_sensor,
        "right_bumper": right_bumper
    }
