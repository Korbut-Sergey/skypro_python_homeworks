def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print (i)
n = int (input("До кокого числа проверить?: "))
print (f"Проверяем до: {n}")
fizz_buzz(n)