class Ticket():
    price = 100
    def __init__(self,weekend=False,child=False):
        if weekend:
            self.price*=1.2
        if child:
            self.discount=0.5
        else:
            self.discount=1

    def getCost(self,num):
        cost=self.price*self.discount*num
        return cost
    
        
