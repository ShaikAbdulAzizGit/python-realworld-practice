# Problem 1 — Bank Account Balance Protection

class BankAccount:
    def __init__(self,balance):
        if balance<0:
            raise ValueError('Balance cannot be negative ')
        self._balance=balance
    def deposit(self,amount):
        if amount<0:
            raise ValueError('Depost Amount cannot be negative')
        self._balance+=amount
    def withdraw(self,amount):
        if amount<0:
            raise ValueError('Withdraw Amount cannot be negative')
        if amount>self._balance:
            raise ValueError('Insufficient balance')
        self._balance-=amount
    @property
    def balance(self):
        return self._balance
    


# Problem 2 — User Age Validation

class UserProfile:
    def __init__(self,age):
        if not age>0:
            raise ValueError('Age cannot be negative or 0')
        self._age=age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if not new_age>0:
            raise ValueError('Age cannot be negative or 0')
        self._age=new_age
    def is_adult(self):
        return self._age>=18
    


# Problem 3 — Product Price Control


class Product:
    def __init__(self,price):
        if price<0:
            raise ValueError('Price cannot be negative')
        self._price=price
        
    def update_price(self,new_price):
        if new_price<0:
            raise ValueError('Price cannot be negative')
        self._price=new_price

    def apply_discount(self,percentage):
        if percentage<0:
            raise ValueError('Percentage cannot be negative')
        self._price-= (percentage/100)*self._price
        
    @property
    def price(self):
        return self._price


# Problem 4 — Student Grade Protection

class Student:
    pass_threshold=75
    def __init__(self,marks):
        if not 0<=marks<=100:
            raise ValueError('Marks must be between 0 - 100')
        self._marks=marks
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self,new_marks):
        if not 0<=new_marks<=100:
            raise ValueError('Marks must be between 0 - 100')
        self._marks=new_marks
    def is_pass(self):
        return self._marks>=Student.pass_threshold
    


# Problem 5 — Password Manager (Security-Oriented)

class Account:
    def __init__(self,user_name,password):
        if len(password)<8:
            raise ValueError('Password length must be atleast 8 ')
        self.user_name=user_name
        self._password=password
    def update_password(self,new_password):
        if len(new_password)<8:
            raise ValueError('Password length must be atleast 8 ')
        self._password=new_password
    def verify_password(self,password):
        return self._password==password
    
# Problem 6 — Inventory Stock Guard

class InventoryItem:
    def __init__(self,qty):
        self._qty=qty

    def add_stock(self,qty):
        if not qty>0:
            raise ValueError('Stock quantity cannot be negative or 0')
        self._qty+=qty
    def remove_stock(self,qty):
        if not qty>0:
            raise ValueError('Stock quantity cannot be negative or 0')
        if qty>self._qty:
            raise ValueError('Insufficient funds')
        self._qty-=qty
    @property
    def stock(self):
        return self._qty
    
# Problem 7 — Session State Manager

class Session:
    def __init__(self):
        self._state=None
    def start(self):
        if not self._state:
            self._state=True
    def end(self):
        if self._state:
            self._state=False
    @property
    def is_active(self):
        return self._state
    


        
        
