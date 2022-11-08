class User:
    def __init__(self, nombre, balance):
        self.balance = balance
        self.nombre = nombre
        return

    def hacer_deposito(self, monto):
        self.balance += monto
        return self

    def hacer_retiro(self, monto):
        self.balance -= monto
        return self

    # def tranferir_dinero(self,monto,otro_user):
    #     # if type(otro_user) is not User:
    #     #     print("usuario no existe")
    #     #     return
    
    #     if self.balance < monto:
    #         print("balance insuficiente")
    #         return
        
    #     self.hacer_retiro(monto)
    #     otro_user.hacer_deposito(monto)


    def transferencia(self, monto, user):
        self.balance -= monto
        user.balance += monto
        self.mostrar_balance()
        user.mostrar_balance()
        return self


    def mostrar_balance(self):
        print(f"la persona {self.nombre} tiene $ {self.balance}")
        return self


#primer usuario
Xavier = User("Xavi", 2000).hacer_deposito(500).hacer_deposito(800).hacer_deposito(1500).hacer_retiro(1250).mostrar_balance()
# Xavier.hacer_deposito(500)
# Xavier.hacer_deposito(800)
# Xavier.hacer_deposito(1500)
# Xavier.hacer_retiro(1250)
# Xavier.mostrar_balance()

#segundo usuario
daniela = User("Dani", 1500).hacer_deposito(1800).hacer_deposito(2100).hacer_retiro(800).hacer_retiro(1200).mostrar_balance().transferencia(3000, Xavier)
# daniela.hacer_deposito(1800)
# daniela.hacer_deposito(2100)
# daniela.hacer_retiro(800)
# daniela.hacer_retiro(1200)
# daniela.mostrar_balance()


#tercer usuario
patricia = User("paty", 1000).hacer_deposito(1300).hacer_retiro(800).hacer_retiro(1200).mostrar_balance()
# patricia.hacer_deposito(1300)
# patricia.hacer_retiro(800)
# patricia.hacer_retiro(1200)
# patricia.mostrar_balance()


#hacer transferencia
# daniela.transferencia(3000, Xavier)