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
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=0)
		
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "green")
		self.down.grid(row=0,column=1)
		
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "green")
		self.left.grid(row=0,column=2)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "green")
		self.right.grid(row=0,column=3)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.upClicked)
		self.left.bind("<Button-1>", self.leftClicked)
		self.right.bind("<Button-1>", self.rightClicked)
		self.down.bind("<Button-1>", self.downClicked)

		  
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
	   drawpad.move(player,0,-20)
	   self.collisionDetection()
	   
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	   self.collisionDetection()

	   
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	   self.collisionDetection()

	   
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   self.collisionDetection()



		# Ensure that we are doing our collision detection
		# After we move our object!
	def collisionDetection(self):
	    global target
	    global drawpad
	    global player
	    x1,y1,x2,y2 = drawpad.coords(player)
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)
	    if x1 >= tx1 and x2 <= tx2 and y1 >= ty1 and y2 <= ty2:
	        drawpad.itemconfig(target, fill = 'red')
	        return True
	    else:
	        return False
	

		
myapp = MyApp(root)

root.mainloop()