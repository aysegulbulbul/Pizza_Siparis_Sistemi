import csv
import datetime

#Pizza üst sınıfını oluşturuyoruz.

class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost

#Pizza alt sınıflarını oluşturuyoruz.

class Klasik(Pizza):
    cost = 60.0
    #Her alt sınıf için özellikleri yazıyoruz.
    def __init__(self):
        self.description = "Klasik Malzemeler: Sucuk, Salam, Kaşar, Biber, Mısır" 
        print(self.description +"\n")

class Margarita(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Margarita Malzemeler: Domates, Fesleğen, Mozarella"
        print(self.description +"\n")

class TurkPizza(Pizza):
    cost = 100.0

    def __init__(self):
        self.description = "Türk Malzemeler: Soğan, Biber, Sarımsak, Kaşar, Kıyma"
        print(self.description +"\n")

class ItalyanPizza(Pizza):
    cost = 150.0

    def __init__(self):
        self.description = "İtalyan Malzemeler: Mozzarella, Parmesan, Salam, Jambon, Mısır, İstiridye Mantarı"
        print(self.description +"\n")


# Soslar için Decorator üst sınıf oluşturuyoruz.
class Decorator(Pizza):
    def __init__(self, sauces):
        self.component = sauces

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ;' + Pizza.get_description(self)
    
#Soslar için Decorator alt sınıf oluşturuyoruz.
class Zeytin(Decorator):
    cost = 2.0

    def __init__(self, sauces):
        Decorator.__init__(self, sauces)


class Mantar(Decorator):
    cost = 3.0

    def __init__(self, sauces):
        Decorator.__init__(self, sauces)


class Peynir(Decorator):
    cost = 4.0

    def __init__(self, sauces):
        Decorator.__init__(self, sauces)


class Et(Decorator):
    cost = 10.0

    def __init__(self, sauces):
        Decorator.__init__(self, sauces)


class Sogan(Decorator):
    cost = 5.0

    def __init__(self, sauces):
        Decorator.__init__(self, sauces)


class Misir(Decorator):
    cost = 5.0

    def __init__(self, sauces):
        Decorator.__init__(self, sauces)

#Menüyü ekrana yazma işlemleri için main fonksiyonu oluşturuyoruz.
def main():
    with open("Menu.txt") as cust_order: #Menu.txt dosyasından müşterilerin siparişlerini alıyoruz.
        for i in cust_order:
            print(i, end="")

    class_dict = {1: Klasik, 
                  2: Margarita, 
                  3: TurkPizza, 
                  4: ItalyanPizza, 
                  5: Zeytin, 
                  6: Mantar, 
                  7: Peynir, 
                  8: Et, 
                  9: Sogan, 
                  10: Misir}
    
    code = input("Lütfen Pizzanızı Seçiniz: ")
    while code not in ["1", "2", "3", "4"]:
        code = input("Yanlış Tuşlama Yaptınız: ")

    order = class_dict[int(code)]()

    while code != "*":
        code = input("Ek Malzeme Almak İçin Tuşlama Yapınız (Direkt Siparişinizi Onaylamak İçin '*' Tuşuna Basınız): ")
        if code in ["5","6","7","8","9","10"]:
            order = class_dict[int(code)](order)

    print("\n"+order.get_description().strip() +
          "; $" + str(order.get_cost()))
    print("\n")

#Sipariş Bilgilerini oluşturuyoruz.
    print("----------Sipariş Bilgileri----------\n")
    name = input("İsminiz: ")
    ID = input("TC Kimlik Numaranız: ")
    credit_card_no = input("Kredi Kartı Numaranızı Giriniz: ")
    credit_card_psw = input("Kredi Kartı Şifrenizi Giriniz: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',') # Yeni bir csv dosyası oluşturuyoruz.
        orders.writerow([name, ID, credit_card_no, credit_card_psw, order.get_description(), time_of_order])
    print("Siparişiniz Onaylandı.")


main()

