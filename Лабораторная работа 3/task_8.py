money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

money_capital -= spend
while money_capital >= 0:
    spend += spend * increase
    money_capital += salary
    money_capital -= spend
    month += 1

print(month)
