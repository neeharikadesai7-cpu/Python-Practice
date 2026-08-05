class Order:
    def __init__(self, item , price):
        self.item = item
        self.price = price 

    def __gt__(self,order2):
        return self.price > order2.price

        # if self.price < order2.price:
        #     return order2 > self
        
        # elif self.price > order2.price:
        #     return order2 < self
        # else:
        #     return self == order2

    
order1 =Order("Chips", 10)
order2 =Order("Tea", 100)

print(order1 > order2)
    

