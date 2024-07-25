#Import the library
from tkinter import *
import time

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of window
win.geometry("800x600")

#Create a canvas object
c= Canvas(win,width=800, height=600, bg = "white")
c.pack()

# positions starts from top left corner
light_1 = c.create_rectangle(600,300,700,550,fill='black')

#Draw an Oval in the canvas
radius = 25 
gx_center_top = 650
gy_center_top = 350

ox_center_top = 650
oy_center_top = 425

rx_center_top = 650
ry_center_top = 500

while True:
    # red
    
    top_light = c.create_oval(rx_center_top-radius,ry_center_top-radius,
                        rx_center_top+radius,ry_center_top+radius, fill = "red")
    win.update()
    print("RED")
    time.sleep(1)
    top_light = c.create_oval(rx_center_top-radius,ry_center_top-radius,
                        rx_center_top+radius,ry_center_top+radius, fill = "black")
    # orange

    top_light = c.create_oval(ox_center_top-radius,oy_center_top-radius,
                        ox_center_top+radius,oy_center_top+radius, fill = "orange")
    win.update()
    print("Orange")
    time.sleep(1)
    top_light = c.create_oval(ox_center_top-radius,oy_center_top-radius,
                        ox_center_top+radius,oy_center_top+radius, fill = "black")

    # green
    top_light = c.create_oval(gx_center_top-radius,gy_center_top-radius,
                        gx_center_top+radius,gy_center_top+radius, fill = "green")
    win.update()
    print("GREEN")
    time.sleep(1)
    top_light = c.create_oval(gx_center_top-radius,gy_center_top-radius,
                        gx_center_top+radius,gy_center_top+radius, fill = "black")
    
    # orange

    top_light = c.create_oval(ox_center_top-radius,oy_center_top-radius,
                        ox_center_top+radius,oy_center_top+radius, fill = "orange")
    win.update()
    print("Orange")
    time.sleep(1)
    top_light = c.create_oval(ox_center_top-radius,oy_center_top-radius,
                        ox_center_top+radius,oy_center_top+radius, fill = "black")

win.mainloop()