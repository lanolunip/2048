class Node:
    def __init__(self,data=0):
        self.data = data
        self.over = None
        self.below = None
        self.right = None
        self.left = None 
        self.next = None
    
    # Cornerfikasi
    def cornerUpLeft(self,right,bottom):
        self.right = right
        self.below = bottom 

    def cornerUpRight(self,left,bottom):
        self.left = left
        self.below = bottom
    
    def cornerBottomLeft(self,right,up):
        self.right = right 
        self.over = up

    def cornerBottomRight(self,left,up):
        self.left = left 
        self.over = up

    #Edgefikasi
    def upEdge(self,left,right,below):
        self.left = left
        self.right = right
        self.below = below

    def bottomEdge(self,left,right,up):
        self.left = left
        self.right = right
        self.over = up

    def leftEdge(self,right,up,bottom):
        self.right = right
        self.over = up
        self.below = bottom

    def rightEdge(self,left,up,bottom):
        self.left = left
        self.over = up
        self.below = bottom    

    #Centerfikasi
    def center(self,left = None, right = None, up = None, down = None):
        self.over = up
        self.right = right
        self.left = left
        self.below = down
            
