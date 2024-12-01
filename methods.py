def call():
    print('calling someone')

class Phone:
    name='xiomi'
    price=19000
    color='red'
    feature=['camera','speaker','battery']

    def call(self):
        print('calling one person to another person')

    def send_sms(self,phone,sms):
        text=f'sending SMS to: {phone} and messeges: {sms}'
        return text

my_phone=Phone()
print(my_phone.feature)
my_phone.call()

result=my_phone.send_sms(8448509,'I hate you')
print(result)
