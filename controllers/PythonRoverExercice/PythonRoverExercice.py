"""
### Examen Final - Programme Principal

Dans ce fichier, vous devez implémenter la classe principale du rover. 

Étapes à suivre :
1. Configurez les capteurs et moteurs en utilisant les fonctions des fichiers `sensors.py` et `motors.py`.
2. Implementez une boucle principale qui :
   - Utilise la fonction `avoidance_logic` (déjà implémentée dans `logic.py`) pour calculer les vitesses des moteurs.
   - Applique ces vitesses via la fonction `set_motor_speeds`.
3. Assurez-vous que le compteur d'évitement (`avoidance_counter`) est correctement mis à jour.

Conseils :
- Utilisez les méthodes `step(64)` pour gérer la simulation.
- Récupérez et manipulez les capteurs et moteurs via les fonctions importées.

Bon courage !
"""

from controller import Robot
from sensors import initialize_sensors
from motors import initialize_motors, set_motor_speeds
from logic import avoidance_logic

class Rover(Robot):
    def __init__(self):
        """
        Le init n'a pas besoin d'être touché.
        """
        super().__init__()
        self.sensors = None
        self.motors = None
        self.avoidance_counter = 0

    def run(self):
        """
        Boucle principale du rover.
        - La partie de run doit configurer les capteurs et moteurs.
        - Elle doit aussi gèrer la logique d'évitement avec l'application des vitesses.
        """
        self.sensors = None
        self.motors = None

        while self.step(64) != -1:
            pass # À retirer pour implémenter votre logique

if __name__ == "__main__":
    rover = Rover()
    rover.run()
