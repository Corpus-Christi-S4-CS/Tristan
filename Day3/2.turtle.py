# from turtle import *

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()


import turtle

def draw_letter_t(t):
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.backward(60)
    t.penup()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(10)

def draw_letter_r(t):
    t.pendown()
    t.left(90)
    t.forward(100)  # Draw the vertical stroke
    t.right(90)
    t.circle(-50, 180)  # Draw the curve
    t.left(135)  # Prepare to draw the leg
    t.forward(70)  # Draw the diagonal leg of R
    t.penup()
    t.left(45)  # Reorient to move to the next letter start position
    t.forward(50)  # Move to the next starting point
    t.right(180)  # Turn around to start next letter correctly


def draw_letter_i(t):
    t.pendown()
    t.forward(60)
    t.backward(30)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.backward(60)
    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(10)

def draw_letter_s(t):
    t.pendown()
    t.circle(-25, -180)
    t.circle(25, -180)
    t.penup()
    t.forward(60)

def draw_letter_a(t):
    t.pendown()
    t.left(60)
    t.forward(115)
    t.right(120)
    t.forward(115)
    t.backward(50)
    t.right(120)
    t.forward(50)
    t.penup()
    t.left(180)
    t.forward(50)
    t.left(60)
    t.forward(60)

def draw_letter_n(t):
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(150)
    t.forward(115)
    t.left(150)
    t.forward(100)
    t.penup()
    t.left(90)
    t.forward(10)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.penup()
    t.backward(300)  # Start position
    t.pendown()
    t.pensize(2)
    
    # Draw each letter
    draw_letter_t(t)
    draw_letter_r(t)
    draw_letter_i(t)
    draw_letter_s(t)
    draw_letter_t(t)
    draw_letter_a(t)
    draw_letter_n(t)
    
    t.hideturtle()
    window.mainloop()

main()
