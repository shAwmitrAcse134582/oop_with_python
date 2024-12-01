class Shopping:
    cart=[]
    origin='China'

    def __init__(self,name,location) -> None:
        self.name='Jamuna'
        self.location='It is media'

    def purchase(self,item,price,amount):
        remaining=amount-price
        print(f'buying : {item} for price : {price} and remaing: {remaining}')

basundhora=Shopping('basu en dhara','not popular location')
basundhora.purchase('lungi',500,1000)

        
