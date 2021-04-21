import math
import numpy as np
from matplotlib import pyplot as plt

def matiere(beta, mu, epsilon, tau, kappa, alpha, omega) :

    R = 0.04830 * beta**1.61
    
    if tau == "roche" : K = 0.01
    if tau == "galets" : K = 0.02
    if tau == "graviers" : K = 0.03
    if tau == "terre" : K = 0.04
    if tau == "sable" : K = 0.05
    
    if epsilon < 100 and epsilon >= 5 : m = 0.5
    if epsilon < 5 and epsilon >= 3 : m = 0.4
    if epsilon < 3 and epsilon >= 1 : m = 0.3
    if epsilon < 1 and epsilon >= 0 : m = 0.2

    theta = epsilon * 0.571

    LS = (mu/22.1)**m * (65.41 * (math.sin(theta)**2) + 4.56 * math.sin(theta) + 0.065)

    if kappa == "aucune" : C = 1
    if kappa == "partielle" : C = 0.75
    if kappa == "totale" : C = 0.5

    if alpha == "aucune" : P = 1
    if alpha == "aménagements" : P = 0.75
    if alpha == "protections" : P = 0.5

    if omega < 1 : V = 1.2
    if omega >= 1 and omega < 3 : V = 1.4
    if omega >= 3 : V = 1.6

    ero = R*K*LS*C*P*V

    return ero

print (matiere(600, 30, 5, "sable", "aucune", "aucune", 0.5))

def ligne(epsilon, sigma):

  theta = epsilon * 0.571

  S = sigma/1000
  thetaRad = math.radians(theta)

  return S * 1.8748 / math.tan(thetaRad) * 100

print (ligne(5, 3.6))

def traitNiveau(epsilon) :

  n = 0
  res = []

  while n < 50 :
      x = ligne(epsilon, n)
      res.append(x)
      n += 1
      
  t = np.arange(0, 50)
  s = res
  fig, ax = plt.subplots()
  ax.plot(t, s)
  ax.set(xlabel='élévation du niveau de la mer (mm/an)', ylabel='recul du trait de côte (m/an)',
  title='Recul du trait de côte en fonction de la montée du niveau de la mer')
  ax.grid()
  fig.savefig("trait-niveau.png")
  plt.show()

  n = 0
  res = []

print(traitNiveau(5))

def traitPente(sigma) :

  n = 1
  res = []

  while n < 100 :
      x = ligne(n, sigma)
      res.append(x)
      n += 1
      
  t = np.arange(0, 99)
  s = res
  fig, ax = plt.subplots()
  ax.plot(t, s)
  ax.set(xlabel='inclinaison du littoral (%)', ylabel='recul du trait de côte (m/an)',
  title="Recul du trait de côte en fonction de l'intensité de la pente littorale")
  ax.grid()
  fig.savefig("trait-pente.png")
  plt.show()

print(traitPente(3.6))

def matierePluie(mu, epsilon, tau, kappa, alpha, omega) :

  n = 0
  res = []

  while n < 2000 :
      x = matiere(n, mu, epsilon, tau, kappa, alpha, omega)
      res.append(x)
      n += 1
      
  t = np.arange(0, 2000)
  s = res
  fig, ax = plt.subplots()
  ax.plot(t, s)
  ax.set(xlabel='pluviométrie moyenne (mm/an)', ylabel='déplacement de matière littorale (t/ha/an)',
  title='Déplacement annuel de matière littorale en fonction de la quantité de pluie annuelle')
  ax.grid()
  fig.savefig("matiere-pluie.png")
  plt.show()

  n = 0
  res = []

print(matierePluie(30, 5, "sable", "aucune", "aucune", 0.5))

def matierePente(beta, epsilon, tau, kappa, alpha, omega) :

  n = 0
  res = []

  while n < 100 :
      x = matiere(beta, n, epsilon, tau, kappa, alpha, omega)
      res.append(x)
      n += 1
      
  t = np.arange(0, 100)
  s = res
  fig, ax = plt.subplots()
  ax.plot(t, s)
  ax.set(xlabel='longueur de la pente (m)', ylabel='déplacement de matière littorale (t/ha/an)',
  title='Déplacement annuel de matière littorale en fonction de la longueur de la pente littorale')
  ax.grid()
  fig.savefig("matiere-pente.png")
  plt.show()

  n = 0
  res = []

print(matierePente(600, 5, "sable", "aucune", "protections", 0.5))
