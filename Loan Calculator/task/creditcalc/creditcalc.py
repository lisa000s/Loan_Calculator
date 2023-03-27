import math
import argparse


def calculate_monthly_payments(principal, payment, interest):
    principal = int(principal)
    payment = int(payment)
    interest = float(interest)
    interest_rate = interest / (12 * 100)
    periods = math.ceil(math.log((payment / (payment - interest_rate * principal)), (1 + interest_rate)))
    years = periods // 12
    months = periods - (years * 12)
    if months == 0:
        print("It will take", years, ("years" if years > 1 else "year"), "to repay the loan!")
    else:
        print("It will take", years, ("years" if years > 1 else "year"), "and", months,
              ("months" if months > 1 else "month"), "to repay the loan!")
    overpayment = int((payment * periods) - principal)
    print("Overpayment =", overpayment)


def calculate_annuity(principal, periods, interest):
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)
    interest_rate = interest / (12 * 100)
    payment = math.ceil(
        principal * ((interest_rate * (1 + interest_rate) ** periods) / ((1 + interest_rate) ** periods - 1)))
    print("Your annuity payment = {}!".format(payment))
    overpayment = int((payment * periods) - principal)
    print("Overpayment =", overpayment)


def calculate_principal(payment, periods, interest):
    payment = float(payment)
    periods = int(periods)
    interest = float(interest)
    interest_rate = interest / (12 * 100)
    principal = math.floor(
        payment / (((interest_rate * (1 + interest_rate) ** periods)) / (((1 + interest_rate) ** periods - 1))))
    print("Your loan principal = {}!".format(principal))
    overpayment = int((payment * periods) - principal)
    print("Overpayment =", overpayment)


def calculate_diff_payment(principal, periods, interest):
    principal = int(principal)
    periods = int(periods)
    interest = float(interest)
    interest_rate = interest / (12 * 100)
    overpayment = - principal
    for i in range(1, periods + 1):
        diff_payment = math.ceil(
            (principal / periods) + interest_rate * (principal - ((principal * (i - 1)) / periods)))
        overpayment = overpayment + diff_payment
        print("Month {}: payment is {}".format(i, diff_payment))
    print("\nOverpayment =", overpayment)


parser = argparse.ArgumentParser(description="This program calculates loan payment")
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

argument_list = [args.type, args.payment, args.principal, args.periods, args.interest]

if args.type is None or args.type not in ["diff", "annuity"]:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
elif (args.payment is not None and int(args.payment) < 0) or (
        args.principal is not None and int(args.principal) < 0) or (
        args.periods is not None and int(args.periods) < 0) or (args.interest is not None and float(args.interest) < 0):
    print("Incorrect parameters")
elif len(argument_list) < 4:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == "annuity" and args.principal is not None and args.periods is not None:
    calculate_annuity(principal=args.principal, periods=args.periods, interest=args.interest)
elif args.type == "diff":
    calculate_diff_payment(principal=args.principal, periods=args.periods, interest=args.interest)
elif args.type == "annuity" and args.principal is None:
    calculate_principal(payment=args.payment, periods=args.periods, interest=args.interest)
elif args.type == "annuity" and args.periods is None:
    calculate_monthly_payments(principal=args.principal, payment=args.payment, interest=args.interest)
else:
    print("Error")
