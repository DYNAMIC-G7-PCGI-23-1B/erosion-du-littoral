# Erosion du littoral : Page d'accueil

**Page d'accueil** <a href="https://dynamic-g7-pcgi-23-1b.github.io/erosion-du-littoral/blog.html"> Blog </a> <a href="https://dynamic-g7-pcgi-23-1b.github.io/erosion-du-littoral/results.html"> Résultats </a>

Le littoral océanique est un environnement fragile qu’il incombe aux institutions de protéger.
Les côtes, de toute la planète, sont sujettes à l’érosion naturelle.
En effet, les vagues, la pluie tout comme l’activité humaine sont de nombreux facteurs qui influent sur la surface littorale.
La ligne de côte recule ou avance et de grands volumes de matière sont déplacés.

Nous avons pour projet de déterminer quels littoraux sont les plus résistants au temps et mettre en lumière les plus vulnérables dans un objectif public de protection et de préservation.
Afin d’arriver à la conclusion désirée, nous nous posons la question suivante, certains littoraux peuvent-ils disposer de caractéristiques capables de réduire grandement l’impact de l’érosion naturelle, si oui, qu’elles sont-elles ?

Nous partons avec une hypothèse principale qui suggère que certains littoraux, formant un certain angle avec l’océan et composés d’une certain façon, sont capables de mieux résister à l’érosion que d’autres.
Nous évaluons cela en prenant en compte deux  grandeurs : le déplacement de la ligne de côte par rapport au temps et le volume de matière déplacée par rapport à la surface et au temps.

## Coastline erosion

The ocean coastline is a fragile environment that institutions have a responsibility to protect.
Coasts around the world are subject to natural erosion.
Waves, rainfall and human activity are many factors that affect the coastal surface.
The coastline retreats or advances and large volumes of material are displaced.

Our project is to determine which shorelines are the most resistant to the impact of time and to highlight the most vulnerable with the public objective of protection and preservation.
In order to reach the desired conclusion, we ask ourselves the following question, can some shorelines have characteristics capable of greatly reducing the impact of natural erosion, if so, what are they?

We start with a main hypothesis that suggests that some shorelines, forming a certain angle with the ocean and composed in a certain way, are able to resist erosion better than others.
We evaluate this by taking into account two quantities: the displacement of the coastline with respect to time and the volume of material displaced with respect to the surface and to time.

## Présentation de l'équipe

|(ᵔᴥᵔ)|( ͡° ͜ʖ ͡°)|ಠ_ಠ|ʕ•ᴥ•ʔ|
|--|--|--|--|
| S. Rey | A. Shindala | M. Khalfaoui | H. Rami |


## Description synthétique du projet

**Problématique :** Certains littoraux peuvent-ils disposer de caractéristiques particulières capables de réduire grandement l'impact de l'érosion naturelle ? 

**Hypothèse principale :** Des littoraux, formant un certain angle avec la mer et composés d'une certaine façon résistent mieux à l'érosion qu'une plage classique.

**Objectifs :** Déterminer quels littoraux sont les plus résistants au temps et mettre en lumière les plus vulnérables afin de les protéger efficacement.

**Critère(s) d'évaluation :** Evaluer le recul de la ligne de côte ainsi que la quantité de matière littorale déplacée par l'érosion naturelle.

## Présentation structurée des résultats

**Fonction *matiere* (en python) (voir erosion.py)**

La fonction *matiere* calcule la quantité de matière déplacée d'un littoral en fonction de nombreux paramètres. Elle renvoie un résultat en t/ha/an

Paramètres utilisés :

	β = pluviométrie annuelle (en mm)
	μ = longueur de la pente (en m)
	ε = inclinaison de la pente (en %)
	τ = type de sol (roche, galets, graviers, terre ou sable)
	κ = couverture végétale (aucune, partielle, totale)
	ɑ = constructions humaines (aucune, aménagements, protections)
	Ω = hauteur moyenne annuelle des vagues (en m)

Formule :

  RUSLE (Revised Universal Soil Loss Equation)

	R*K*LS*C*P (en t/ha/a)
    
R (rainfall-runoff erosivity factor) :
	
	0.04830 * β <sup>1,61</sup>

K (soil erodibility factor) :

![K](https://raw.githubusercontent.com/DYNAMIC-G7-PCGI-23-1B/erosion-du-littoral/main/images/K.png)

LS (length-slope factor) :

	(μ/22.1) <sup>m</sup> * (65.41sin <sup>2</sup> θ + 4.56sinθ + 0.065)
	θ (°) = ε * 0.571

![m](https://raw.githubusercontent.com/DYNAMIC-G7-PCGI-23-1B/erosion-du-littoral/main/images/m.png)

C (vegetative cover factor) :

![C](https://raw.githubusercontent.com/DYNAMIC-G7-PCGI-23-1B/erosion-du-littoral/main/images/C.png)

P (erosion control practice factor) :

![P](https://raw.githubusercontent.com/DYNAMIC-G7-PCGI-23-1B/erosion-du-littoral/main/images/P.png)

Ajout de l'impact des vagues en fonction de la hauteur annuelle moyenne de celles-ci :

![waves](https://raw.githubusercontent.com/DYNAMIC-G7-PCGI-23-1B/erosion-du-littoral/main/images/waves.png)

Remarque :

Les tableaux de valeurs de K, C, P et du facteur vagues sont purement théoriques et supposés.

En réalité, les valeurs de ces facteurs ne peuvent être universelles et sont usuellement issues de mesures précises en fonction de l’objet géologique étudié.

De nombreux autres paramètres entrent en compte pour K, C, P et le facteur vagues comme la rugosité du terrain, la profondeur, la densité du sol et bien d’autres.

On peut s’en passer pour comprendre l’origine générale de l’érosion et l’appliquer à un système informatique.

**Fonction *ligne* (en python) (voir erosion.py)**

La fonction *ligne* calcul le recul du trait de côte en fonction de plusieurs paramètres. Elle renvoie un résultat en cm/an

Paramètres :

	ε = inclinaison de la pente (en %)
	Σ = élévation annuelle du niveau de la mer (en mm)
	
Exemples de plusieurs valeurs de sigma :

	Actuellement, en 2020 : 3,6
	En 2050, si faible émission de gaz à effet de serre : 5,3
	En 2050, si forte émission de gaz à effet de serre : 10,1
	En 2050, si forte émission de gaz à effet de serre et prise en compte de la fonte des glaces de l'Antarctique : 49,4
	
Formule :

  Règle de Bruun
  
  	S / tanθ <sub> R </sub>
	
S (Sea level rise) :

	Σ / 1000 * 1.8748

θ <sub> R </sub> (Active profile average slope) :

	ε * 0.571 * π / 180
	
**Fonction *dessin* (en python) (voir erosion.py)**

La fonction *dessin* dessine une représentation graphique des paramètres choisis par l'utilisateur ainsi que le déplacement de la ligne de côte

Paramètres utilisés :

	β = pluviométrie annuelle (en mm)
	ε = inclinaison de la pente (en %)
	τ = type de sol (roche, galets, graviers, terre ou sable)
	κ = couverture végétale (aucune, partielle, totale)
	ɑ = constructions humaines (aucune, aménagements, protections)
	Σ = élévation annuelle du niveau de la mer (en mm)

## Bibliographie :

![Mind map](https://raw.githubusercontent.com/DYNAMIC-G7-PCGI-23-1B/erosion-du-littoral/main/images/mind_map.png)

*Exlibris :*

[1] FOX Denis, MORSCHEL Jean, 2004, Une méthode de cartographie du risque érosif : application aux collines du Terrefort lauragais. Mappemonde

*Google :*

[2] HEDOU François, ROCHE Amélie, TRMAL Céline, MORAUD Sabine, DENIAUD Yann, 2018, Elaboration de l’indicateur national de l’érosion côtière. Paralia

[3] HANSON Hans, 2020, Littoral drift and shoreline modelling. http://www.coastalwiki.org/wiki/Littoral_drift_and_shoreline_modelling

[4] SHARMA Ashok, GARDNER Ted, BEGBIE Don, 2019, Approached to Water Sensitive Urban Design. Elsevier

*Researchgate :*

[5] BENASSAI Guido, 2006, Introduction to Coastal Dynamics and Shoreline Protection. WIT Press

### Zoom sur le document [2]

*Référence bibliographique du document :*

	HEDOU François, ROCHE Amélie, TRMAL Céline, MORAUD Sabine, DENIAUD Yann, 2018, Elaboration de l’indicateur national de l’érosion côtière. Paralia

*Qui sont les auteurs du documents ? :*

	-HEDOU François : Responsable d’études au CEREMA (direction eau, mer et fleuves)
	-ROCHE Amélie : Chargée d’études au CEREMA (direction eau, mer et fleuves)
	-TRMAL Céline : Chargée d’études au CEREMA (direction Méditerranée)
	-MORAUD Sabine : Adjointe au chef du bureau des espaces maritimes et littoraux au Ministère de la Transition Écologique et Solidaire
	-DENIAUD Yann : Responsable d’études au CEREMA (direction eau, mer et fleuves)

*Par quelle structure ce document a-t-il été publié ?*

	Document de conférence publié via la maison d’éditions Paralia (documents scientifiques portant sur l’étude du littoral)

*Les auteurs citent-ils leurs sources ?*

	Citation des sources avec présence d’une bibliographie.

*Quand le document a-t-il été publié ? L’information est-elle datée pour le sujet ?*

	Publication en 2018, par conséquent document à jour.

*Quel est l’objectif de ce document ?*

	Document informatif produisant un indicateur national de l’érosion côtière.

*Quel est le niveau de spécialisation du document ?*

	Document hautement spécialisé.

### Zoom sur le document [5]

*Référence bibliographique du document :*

	BENASSAI Guido, 2006, Introduction to Coastal Dynamics and Shoreline Protection. WIT Press
	
*Qui sont les auteurs du documents ? :*

	-BENASSAI Guido : Professeur en dynamique côtière et protection du littoral à l’Université de Naples

*Par quelle structure ce document a-t-il été publié ?*

	Livre publié via la maison d’éditions WIT Press (recherches en sciences et ingénierie)

*Les auteurs citent-ils leurs sources ?*

	Citation des sources avec présence d’une bibliographie.

*Quand le document a-t-il été publié ? L’information est-elle datée pour le sujet ?*

	Publication en 2006, par conséquent document moyennement à jour.

*Quel est l’objectif de ce document ?*

	Document éducatif portant sur la dynamique côtière et la protection du littoral.

*Quel est le niveau de spécialisation du document ?*

	Document spécialisé.
