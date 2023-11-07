while True:
    sayi1=int(input("Lütfen 1. sayıyı giriniz;"))

    sayi2=int(input("Lütfen 2.sayıyı giriniz;"))

    işlem=input("Yapmak istediğiniz işlem giriniz; ")
    if işlem not in ["+", "-", "*", "/"]:
        "Lütfen +, -, *, veya / işlemlerinden birini giriniz!"

    if işlem == "+":
        print (sayi1 + sayi2)
    elif işlem =="-":
        print(sayi1-sayi2)
    elif işlem =="*":
        print(sayi1*sayi2)
    elif işlem =="/":
        print(sayi1/sayi2)  
    else:
        print("Geçerli bir işlem giriniz!") 
