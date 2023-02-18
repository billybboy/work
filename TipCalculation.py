import decimal

bill = decimal.Decimal(input("What is the total bill for today, please?"))

def calculate(arg):
    """
    return the value of tips according to different percentages

    arg(int): percentage of tip
    """
    tips = round(decimal.Decimal(bill * arg / 100), 2)
    total = bill + tips
    return "{} % tips is {}, which brings you total to {}".format(arg, tips, total)

print(calculate(18))
print(calculate(15))
print(calculate(20))