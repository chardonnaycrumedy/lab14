#########################################
#
#    70pt - Basic collision detection
#
#########################################

# When the player moves the ball into the rectangle, turn the rectangle red
# You will need to code the movement of the player and the collision detection.

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 1

def animate():
    global direction
    x1, y1, x2, y2 = drawpad.coords(player)
    if y2 > drawpad.winfo_width(): 
        direction = - 5
    elif y1 < 0:
        direction = 5
drawpad.move(player,direction,0)
drawpad.after(1, animate)

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "green")
		self.button1.grid(row=0,column=0)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Down", background= "green")
		self.button2.grid(row=0,column=1)
		
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Left", background= "green")
		self.button3.grid(row=0,column=2)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Right", background= "green")
		self.button4.grid(row=0,column=3)
					
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		self.button2.bind("<Button-1>", self.button1Click)
		self.button3.bind("<Button-1>", self.button1Click)
		self.button4.bind("<Button-1>", self.button1Click)

		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
	    			
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		global targetx1, targety1, targetx2, targety2
		
        def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)


		# Ensure that we are doing our collision detection
		# After we move our object!
	
	
		
myapp = MyApp(root)

root.mainloop()