import math
def RUSLEV (pluie, pente, longueur, sol, couverture, construction, vagues) :
    # pluie en mm, par défaut 600 (pluie moyenne dans le sud de la France)
    # pente en pourcentage, par défaut 5 (pente moyenne d'une plage)
    # longueur en m, par défaut 30 (largeur moyenne d'une plage)
    # type en string (roche, graviers, galets, sable fin, sable) # joindre image
    # couverture en string (nu, broussaille, foret) # joindre image
    # construction (fragilisant, nu, renforcant) # joindre image
    # vagues (pas l'océan, faibles, moyennes, fortes) # pas l'océan == par exemple une vallée # joindre image
    
    R = 0.04830 * pluie^1.610
    if pente < 9 : S = 10.8 math.sin(pente*0.571) + 0.03
    if pente >= 9 and pente < 17.6 : S = 16.8 math.sin(pente*0.571) - 0.5
    if pente >= 17.6 : S = 21.9 math.sin(pente*0.571) - 0.96
    if pente <= 1.7 : L = (longueur/221)^0.2
    if pente > 1.7 and pente <= 5.2 : L = (longueur/221)^0.3
    if pente > 5.2 and pente <= 9 : L = (longueur/221)^0.4
    if pente > 9 : L = (longueur/221)^0.5
    if sol == "sable fin" : K == 0.0875
    if sol == "sable classique" : K = 0.1625
    if sol == "graviers" : K == 0.2875
    if sol == "galets" : K == 0.3625
    if sol == "roche" : K == 0.66
    if couverture == "nu" : C = 1
    if couverture == "broussaille" : C = 0.66
    if couverture == "bois" : C = 0.33
    if construction == "nu" : P = 1
    if construction == "renforcement faible" : P = 0.66
    if construction == "renforcement fort" : P = 0.33
    if vagues == "pas l'océan" : V=1
    if vagues == "faibles" : V=1.33
    if vagues == "moyennes" : V=1.66
    if vagues == "fortes" : V=1.99

    return R*S*L*K*C*P*V