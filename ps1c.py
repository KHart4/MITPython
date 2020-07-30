salary = float(input('Enter the starting salary: '))
total_cost = 1000000
down_payment = 0.25 * total_cost
r = 0.04
current_savings = 0
semi_annual_raise = 0.07
epsilon = 100
high = 1
low = 0 
savings_rate = (high + low) / 2
steps = 0
while abs(current_savings - down_payment) >= epsilon:
    months = 0
    current_savings = 0
    annual_salary = salary
    while months <= 36:
        current_savings += savings_rate * annual_salary / 12 + r / 12 * current_savings
        months += 1
        if months % 6 == 0:
            annual_salary += semi_annual_raise * annual_salary
    if current_savings > down_payment:
        high = savings_rate
    else:
        low = savings_rate
    if low == 1:
        break
    else:
        savings_rate = (high + low) / 2
        steps += 1
savings_rate = round(savings_rate, 4)
if savings_rate < 1:
    print('Best savings rate: ' + str(savings_rate))
    print('Steps in bisection search: ' + str(steps))
else:
    print('It is not possible to pay the down payment in three years.')