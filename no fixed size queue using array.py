class noFixedMyQueue:
    def __init__(self):
        self.names = []

    def isEmpty(self):
        if self.names == []:
            return True
        else:
            return False

    def enqueue(self, data):
        self.names.append(data)
    
    
    
    def dequeue(self):
        if self.isEmpty():
            return "iam Empty"
        else:
            return self.names.pop(0)
        
    
    def peek(self):
        if self.isEmpty():
            return "iam Empty"
        else:
            return self.names[0]
    
    def delete(self):
        self.names = [None]





#FALLOW THIS STEPS TO USE ABOVE THE CODE:-

#First create a object using above class:-
#rootNode = noFixedMyQueue() (object name is your choice).
#After creating the object we can use the functions which are available in the class.
#rootNode.isEmpty() (if queue is empty it will give output has True else give False).
#rootNode.enqueue("data") (By this function we can add the data in to the queue).
#rootNode.dequeue()  (By this function we can access the first data and after accessing the data it will popup that data only first data).
#rootNode.peek()  (this function will show the data which is only available at first index number or first position).
#rootNode.delete()  (By this function we can delete entire data in the Queue)..

        
