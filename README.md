# Souris_v2
Evolution du prototype de souris - Lauréat ANCT
Suite à la réalisation et mis en test des premiers prototypes de la [souris réalisée par le FabLab UtoPi](https://github.com/FabLabUtoPi/Souris) 
Les évolutions suivantes ont été retenues après analyse des retours des utilisateurs/testeurs  


![Image de la souris dans sa deuxième version : boîtier un peu plus grand et joystick analogique.](https://github.com/FabLabUtoPi/Souris_v2/blob/main/Images/souris_v2_01.jpg)

## Evolutions par rapport au prototype

### Taille du boîtier 
Lors des manipulations du joystick il arrive quel le boîtier se soulève
Deux approches sont possibles : Alourdir le boîtier ou augmenter sa taille 
Le manque de stabilité semble du à la taille du boîtier, la solution retenue  été d'augmenter légèrement la taille du boîtier en conservant le format carré de départ.

### Sensibilité du joystick
![Image de l'intérieur de la souris dans sa deuxième version : boîtier un peu plus grand et joystick analogique.](https://github.com/FabLabUtoPi/Souris_v2/blob/main/Images/souris_v2_04.jpg)  
Le joystick retenu à l'origine est un joystick digital. Les directions de déplacement du curseur de la souris sont commandées par des switchs (des interrupteurs) qui sont activés lorsque l'utilisateur pousse le levier dans une direction. L'accélération de déplacement du curseur est obtenue en maintenant le leviier poussé pendant au moins 0,5 seconde. Si l'utilisateur relache le levier ou change de direction, le déplacement revient en vitesse lente. Il faut de nouveau 0,5 seconde pour accélérer le déplacement. Ceci a conduit à adopter un joystick analogique. le déplacement du levier modifie une tension. En fonction de la position du levier la tension est plus ou moins élevée. Il est possible de définir dans le programme les seuils pour lesquels on passe de la vitesse lente à la vitesse rapide. L'utilisataur peut ainsi doser le déplacement du curseur instantanément, sans devoir respecter un délai.

### Filtrage des mouvements involontaires
La souris peut être utilisée par des personnes présentant des mouvements involontaires (~Parkinson). le joystick analogique permet de filtrer ces mouvements involontaires en filtrant les mouvements pour utiliser une valeur moyenne. 

### Adaptation de la préhension
Le joystick permet de monter un système de préhension adapté à la personne (boule, repose poignet, poignée adaptée après scan de la main)
![Image d'un boule adaptée au joystick analogique.](https://github.com/FabLabUtoPi/Souris_v2/blob/main/Images/boule.jpg)
![Image d'un porte poignet adapté au joystick analogique.](https://github.com/FabLabUtoPi/Souris_v2/blob/main/Images/support_poignet.jpg)

### Réorganisation interne
![Image de l'intérieur de la souris dans sa deuxième version : boîtier un peu plus grand et joystick analogique.](https://github.com/FabLabUtoPi/Souris_v2/blob/main/Images/souris_v2_03.jpg)  
L'augmentation de la taille du boîtier a permis de placer différemment les composants à l'intérieur du boîtier. Le montage de la souris est facilité et le temps de montage a été réduit de 30% environ

### Fixation de la rampe d'interrupteurs
L'augmentation de taille a également permis de repenser la fixation de la plaquette supportant les interrupteurs avec une meilleure solidité de la fixation et un montage plus rapide.

### Abandon du vibreur
![Image de l'intérieur de la souris dans sa deuxième version : boîtier un peu plus grand et joystick analogique.](https://github.com/FabLabUtoPi/Souris_v2/blob/main/Images/souris_v2_02.jpg)  
Pensé pour des non voyants, le premier modèle comportait un buzzer et un vibreur qui fournissait un retour haptique. Il apparait que le buzzer fournit une information suffisante pour un non voyant. Le vibreur a donc été supprimé du schéma mais pourra être ajouté en option pour des personnes mal-entendantes. On garde la possibilité de désactiver le buzzer en appuyant sur une touche au démarrage de la souris.

### Réduction du nombre de pièces à imprimer
La remise en réflexion de la souris et l'augmentation de sa taille ont permis de réduire le nombre de pièces à imprimer à 3 au lieu de 5.

### Augmentation du prix du joystick
Le passage d'un modèle digital (équipé de switchs) à un modèle analogique (équipé de potentiomètres) induit une légère augmentation du coût, le joystick passant de 7€ à 12€ (environ)
