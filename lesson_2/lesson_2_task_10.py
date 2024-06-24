def bank():
    stavka = 0.1
    n = int(input("Сколько у Вас денег?""\n""-> "))
    years = int(input("На сколько лет хотите сделать вклад?""\n""-> "))

    x = n*(1+stavka)**years
    print("По итогу вы получаете", x , "рублей")
bank()