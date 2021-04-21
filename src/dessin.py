import turtle

def dessin(beta, epsilon, tau, kappa, alpha, sigma) :

  theta = epsilon * 0.571

  turtle.Screen().setup(404, 408)
  turtle.Screen().bgcolor("white")

  mer = turtle.Turtle()
  plage = turtle.Turtle()
  pluie = turtle.Turtle()
  vege = turtle.Turtle()
  const = turtle.Turtle()

  mer.hideturtle()
  plage.hideturtle()
  pluie.hideturtle()
  vege.hideturtle()
  const.hideturtle()

  mer._delay(0)
  plage._delay(0)
  pluie._delay(0)
  vege._delay(0)
  const._delay(0)

  mer.pensize(5)
  plage.pensize(5)
  pluie.pensize(3)
  vege.pensize(3)
  const.pensize(5)

  mer.color("cyan")
  if tau == "roche" : plage.color("#2d2f33") and plage.fillcolor("#2d2f33")
  if tau == "galets" : plage.color("#44474d") and plage.fillcolor("#44474d")
  if tau == "graviers" : plage.color("#62666e") and plage.fillcolor("#62666e")
  if tau == "terre" : plage.color("#A0522D") and plage.fillcolor("#A0522D")
  if tau == "sable" : plage.color("#F5DEB3") and plage.fillcolor("#F5DEB3")
  pluie.color("blue")
  const.color("gray")

  mer.penup()
  mer.forward(200)
  mer.right(90)
  mer.forward(90-sigma)
  mer.pendown()

  mer.begin_fill()
  mer.right(90)
  mer.forward(400)
  mer.left(90)
  mer.forward(400)
  mer.setx(200)
  mer.sety(-90+sigma)
  mer.end_fill()

  plage.penup()
  plage.forward(200)
  plage.right(90)
  plage.forward(100)
  plage.pendown()

  plage.begin_fill()
  plage.right(90+theta)
  plage.forward(25)
  m, n = plage.pos()
  plage.forward(175)
  u, v = plage.pos()
  plage.forward(100)
  a, b = plage.pos()
  plage.forward(25)
  c, d = plage.pos()
  plage.forward(25)
  e, f = plage.pos()
  plage.forward(25)
  g, h = plage.pos()
  plage.forward(191)
  plage.left(90+theta)
  plage.forward(400)
  plage.setx(200)
  plage.sety(-100)
  plage.end_fill()

  if beta == 0 : x = 0
  if beta > 0 and beta <= 300 : x = 400/4
  if beta > 300 and beta <= 600 : x = 400/8
  if beta > 600 and beta <= 900 : x = 400/12
  if beta > 900 and beta <= 1200 : x = 400/16
  if beta > 1200 and beta <= 1500 : x = 400/20
  if beta > 1200 : x = 400/24

  i = 0

  while i < 400 :
    pluie.penup()
    pluie.setheading(300)
    pluie.setx(-200 + i)
    pluie.sety(200)
    pluie.pendown()
    pluie.forward(20)
    i += x
  
  def tree(x, y) :
    vege.penup()
    vege.setheading(90-theta)
    vege.setx(x)
    vege.sety(y)
    vege.pendown()
    vege.color("brown")
    vege.forward(20)
    vege.color("green")
    vege.right(90)
    vege.left(45)
    vege.forward(5)
    vege.left(180)
    vege.forward(5)
    vege.right(180)
    vege.left(45)
    vege.forward(5)
    vege.left(180)
    vege.forward(5)
    vege.right(180)
    vege.left(45)
    vege.forward(5)
  
  def bush(x, y) :
    vege.penup()
    vege.setheading(90-theta)
    vege.setx(x)
    vege.sety(y)
    vege.pendown()
    vege.color("green")
    vege.right(90)
    vege.left(45)
    vege.forward(8)
    vege.left(180)
    vege.forward(8)
    vege.right(180)
    vege.left(45)
    vege.forward(8)
    vege.left(180)
    vege.forward(8)
    vege.right(180)
    vege.left(45)
    vege.forward(8)

  if kappa == "partielle" : bush(a, b), bush(c, d), bush(e, f), bush(g, h)
  if kappa == "totale" : tree(a, b), tree(c, d), tree(e, f), tree(g, h)

  if alpha == "protections" :
    const.pensize(8)
    const.setheading(270)
    const.penup()
    const.setx(m)
    const.sety(n)
    const.pendown()
    const.forward(20)
    
  if alpha == "aménagements" :
    const.setheading(270)
    const.penup()
    const.setx(u)
    const.sety(v)
    const.pendown()
    const.forward(5)

  turtle.Screen().exitonclick()

print(dessin(1800, 5, "sable", "totale", "protections", 3.6))