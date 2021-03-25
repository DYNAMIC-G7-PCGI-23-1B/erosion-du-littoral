import math
def erosion(beta, mu, epsilon, tau, kappa, alpha, omega) :

    #print("Merci de vous rapporter au document joint pour plus d'informations sur les paramètres")
    #beta = float(input("Pluviométrie annuelle (en mm)"))
    #mu = float(input("Longueur de la pente (en m)"))
    #epsilon = float(input("Inclinaison de la pente (en %)"))
    #tau = str(input("Type de sol (roche, galets, graviers, terre ou sable)"))
    #kappa = str(input("Couverture végétale (aucune, partielle, totale)"))
    #alpha = str(input("Constructions humaines (aucune, aménagements, protections)"))
    #omega = float(input("Hauteur moyenne annuelle des vagues (en m)"))

    R = 0.04830 * beta**1.61
    
    #if tau != "roche" or tau != "galets" or tau != "graviers" or tau != "terre" or tau != "sable" :
     #   print("Erreur, type de sol non pris en charge")
      #  return None
    if tau == "roche" : K = 0.01
    if tau == "galets" : K = 0.02
    if tau == "graviers" : K = 0.03
    if tau == "terre" : K = 0.04
    if tau == "sable" : K = 0.05
    
    #if epsilon >= 100 or epsilon < 0 :
     #   print("Erreur, inclinaison de la pente non prise en charge")
      #  return None
    if epsilon < 100 and epsilon >= 5 : m = 0.5
    if epsilon < 5 and epsilon >= 3 : m = 0.4
    if epsilon < 3 and epsilon >= 1 : m = 0.3
    if epsilon < 1 and epsilon >= 0 : m = 0.2

    theta = epsilon * 0.571

    LS = (mu/22.1)**m * (65.41 * (math.sin(theta)**2) + 4.56 * math.sin(theta) + 0.065)

    #if kappa != "nu" or kappa != "partielle" or kappa != "totale" :
     #   print("Erreur, couverture végétale non prise en charge")
      #  return None
    if kappa == "aucune" : C = 1
    if kappa == "partielle" : C = 0.75
    if kappa == "totale" : C = 0.5

    #if alpha != "aucune" or alpha != "aménagements" or alpha != "protections" :
     #   print("Erreur, construction(s) non prise(s) en charge")
      #  return None
    if alpha == "aucune" : P = 1
    if alpha == "aménagements" : P = 0.75
    if alpha == "protections" : P = 0.5

    if omega < 1 : V = 1.2
    if omega >= 1 and omega < 3 : V = 1.4
    if omega >= 3 : V = 1.6

    print(R, K, LS, C, P, V)
    ero = R*K*LS*C*P*V
    #print("Pour un hectare de littoral avec ces caractéristiques, chaque année, plus de ", math.floor(ero), " tonnes de sédiments se retrouvent dans l'océan")
    return ero

print (erosion(600, 30, 5, "sable", "aucune", "aucune", 0.5))