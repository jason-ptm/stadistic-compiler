"""
This module represents the behavior of an assembler.
It converts intermediate representation into assembly-like instructions
and simulates their execution to produce the final results.
It also handles leap years correctly when calculating maturity dates.

Authors: Jason Stevens Solarte Herrera, Andrés Felipe Vanegas Bogotá
"""

import datetime

def is_leap_year(year):
    """
    Check if a year is a leap year.
    A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

class Assembler:
    def __init__(self, intermediate_representation):
        self.intermediate_rep = intermediate_representation
        self.assembly_code = []

    def get_assembly_code(self):
        return self.assembly_code

    def assemble(self):
        # Convert intermediate representation to assembly instructions
        for line in self.intermediate_rep:
            for command in line:
                if command.startswith('INTEREST_CALCULATION'):
                    self.assembly_code.append("LOAD_I INT_CALC")
                elif command.startswith('AMOUNT'):
                    _, amount_value = command.split()
                    self.assembly_code.append(f"PUSH_AMNT {amount_value}")
                elif command.startswith('RATE'):
                    _, rate_value = command.split()
                    self.assembly_code.append(f"PUSH_RATE {rate_value}")
                elif command.startswith('TIME'):
                    _, time_value = command.split()
                    self.assembly_code.append(f"PUSH_TIME {time_value}")
                elif command.startswith('YEARS'):
                    self.assembly_code.append("EXEC_INT_CALC")
                elif command.startswith('PAYMENT'):
                    _, payment_value = command.split()
                    self.assembly_code.append(f"PUSH_PAY {payment_value}")
                elif command.startswith('BALANCE'):
                    self.assembly_code.append("CALC_BAL")
                elif command.startswith('DEFINE_RATE'):
                    _, rate_value = command.split()
                    self.assembly_code.append(f"SET_RATE {rate_value}")
                elif command.startswith('DATE_VALUE'):
                    _, date_value = command.split()
                    self.assembly_code.append(f'SET_DATE {date_value}')
                elif command.startswith('PERIOD'):
                    _, period_value = command.split()
                    self.assembly_code.append(f'SET_PERIOD {period_value}')
                elif command.startswith('MATURITY_CALCULATION'):
                    self.assembly_code.append("CALCULATE_MATURITY")

    def execute(self):
        # Variables to store execution state
        amount = 0
        rate = 0
        time = 0
        payment = 0
        balance = 0
        total_amount = 0  # Variable to store the total amount after interest
        maturity_date = None
        period_days = 0

        # Execute the generated assembly instructions
        for instr in self.assembly_code:
            if instr.startswith("PUSH_AMNT"):
                _, amount = instr.split()
                amount = float(amount)
            elif instr.startswith("PUSH_RATE"):
                _, rate = instr.split()
                rate = float(rate)
            elif instr.startswith("PUSH_TIME"):
                _, time = instr.split()
                time = float(time)
            elif instr == "EXEC_INT_CALC":
                # Simple interest calculation
                interest = amount * (rate / 100) * time
                total_amount = amount + interest  # Calculate total amount after interest
                print(f"Total amount after interest: {total_amount}")
                print(f"Total interest amount: {interest}")
            elif instr.startswith("PUSH_PAY"):
                _, payment = instr.split()
                payment = float(payment)
            elif instr == "CALC_BAL":
                # Calculate balance after payment
                balance = total_amount - payment  # Subtract payment from the total amount after interest
                print(f"Balance after payment: {balance}")
            elif instr.startswith("SET_DATE"):
                _, date_value = instr.split()
                maturity_date = datetime.datetime.strptime(date_value, "%d/%m/%Y")
            elif instr.startswith("SET_PERIOD"):
                _, period_days = instr.split()
                period_days = int(period_days)
            elif instr == "CALCULATE_MATURITY":
                # Calculate the maturity date
                if maturity_date is not None:
                    if period_days == 365:
                        # If the period is exactly 365 days, add 1 year to the maturity date
                        # Check if the current year is a leap year and if the date is February 29
                        if maturity_date.month == 2 and maturity_date.day == 29 and not is_leap_year(maturity_date.year + 1):
                            # If the next year is not a leap year, adjust the date to February 28
                            end_date = maturity_date.replace(year=maturity_date.year + 1, day=28)
                        else:
                            # Otherwise, add 1 year to the maturity date
                            end_date = maturity_date.replace(year=maturity_date.year + 1)
                    else:
                        # Otherwise, use timedelta to add the period in days
                        end_date = maturity_date + datetime.timedelta(days=period_days)
                    print(f"Maturity date after period: {end_date.strftime('%d/%m/%Y')}")
                else:
                    print("Error: Maturity date not set before calculation")