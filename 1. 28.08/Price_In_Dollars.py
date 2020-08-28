print("Hello, Coach")
rate = float (input("Введіть курс долара в гривнях "))
price_in_dollar = float (input("Введіть ціну в доларах "))
price_in_hr = rate*price_in_dollar
print("Ціна в гривнях відносно поточного курсу %f" % price_in_hr)