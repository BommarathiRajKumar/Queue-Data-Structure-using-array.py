class myQueue:
    def __init__(self, qlen):
        self.maxSize = qlen
        self.items = [None] * self.maxSize
        self.start = -1
        self.end = -1
        
        
    #time:O(1)
    def isEmpty(self):
        if self.start == -1:
            return True
        else:
            return False
        
        
    #time:O(1)
    def isFull(self):
        #case-1
        if self.start == 0 and self.end == self.maxSize -1:
            return True
        #case-2
        elif self.end == self.start - 1:
            return True
        else:
            return False   
        
      
    
    
    
    #time&space:O(1)
    def enqueue(self, data):
        if self.isFull() == False:
        
            
            #circular space available
            if self.end + 1 == self.maxSize:
                self.end = 0
            else:
                #applicable when queue is empty
                if self.start == -1:
                    self.start = 0
                self.end = self.end+1
            self.items[self.end] = data
        else:
            print("Sorry No Space left")
    
   


    #time&space=O(1)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty..."
        firstItem = self.items[self.start]
        self.items[self.start] = None
        
        #entire queue is now empty
        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.start +1 == self.maxSize:
            self.start = 0
        #elif self.end == self.maxSize:
         #   self.end = 0
        else:
            self.start +=1
        return firstItem
    
    
   


    #time: O(n)
    def printQueue(self):
        for i in self.items:
            print(i)
    

    def peek(sefl):
        if self.isEmpty():
            return "Queue id Empty..."
        else:
            return self.items[self.start]
        
    

    def delete(self):
        if self.isEmpty == True:
            self.items = None
        else:
            print("Queue is already empty")





#Fallow this steps to use the above code:-

#After compiling the code create a object using above class
#rootNode = myQueue(3)
#After creating the object use the functions which are available in class.
#rootNode.isEmpty()   <this function will tell you whether Queue is empty or not>
#rootNode.enqueu("data")  <by this function we can append the data in to the Queue> 
#rootNode.dequeue()   <by this function we can use the first postion data and popup fron the Queue>
#rootNode.printQueue()  <by this function we can print entire data which is available in Queue>   
