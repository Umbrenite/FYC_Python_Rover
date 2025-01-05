"""
### Examen Final - Contrôle des Moteurs

Dans ce fichier, vous allez implémenter deux fonctions :
1. **initialize_motors** :
   - Configurez les moteurs gauche et droit.
   - Assurez-vous que leur position soit réglée sur une valeur infinie (`float('inf')`) pour permettre le contrôle de vitesse.
   - Réglez leur vitesse initiale à 0.

2. **set_motor_speeds** :
   - Permet de définir la vitesse des moteurs gauche et droit.
   - Les vitesses à appliquer seront celles renvoyées par le fichier logic.py

À compléter :
- Utilisez `robot.getDevice(nom_du_moteur)` pour récupérer un moteur.
- À savoir que le moteur gauche s'appelle "left wheel motor" et le moteur droit s'appelle "right wheel motor"
- Appelez les méthodes `setPosition` et `setVelocity` pour configurer les moteurs.
"""

def initialize_motors(robot):
    left_motor = None
    right_motor = None

    return {
        "left_motor": left_motor,
        "right_motor": right_motor
    }

def set_motor_speeds(motors, left_speed, right_speed):

    pass # À retirer pour implémenter votre logique
