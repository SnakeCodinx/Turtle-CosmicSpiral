import turtle as tur

tur.bgcolor("black")
tur.speed(0)
tur.hideturtle()

colors = ['yellow','green','blue','red']
for i in range(500):
    for c in colors:
        tur.color(c)
        tur.forward(i)
        tur.left(91)
        tur.tracer(10)
tur.mainloop()