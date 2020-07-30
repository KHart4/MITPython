annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: ​'))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))
down_payment = 0.25 * total_cost
r = 0.04
current_savings = 0
months = 0
while current_savings < down_payment:
    current_savings += portion_saved * annual_salary / 12 + r / 12 * current_savings
    months += 1
    if months % 6 == 0:
        annual_salary += semi_annual_raise * annual_salary
print ('Number of months: ' + str(months))