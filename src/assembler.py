import datetime

class Assembler:
    def __init__(self, intermediate_representation):
        self.intermediate_rep = intermediate_representation
        self.assembly_code = []

    def get_assembly_code(self):
        return self.assembly_code

    def assemble(self):
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
        amount = 0
        rate = 0
        time = 0
        payment = 0
        balance = 0
        maturity_date = None
        period_days = 0

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
            elif instr.startswith("EXEC_INT_CALC"):
                interest = amount * (rate / 100) * time
                total_amount = amount + interest
                print(f"Total amount after interest: {total_amount}")
                print(f"Total interest amount: {interest}")
            elif instr.startswith("PUSH_PAY"):
                _, payment = instr.split()
                payment = float(payment)
            elif instr == "CALC_BAL":
                balance = amount - payment
                print(f"Balance after payment: {balance}")
            elif instr.startswith("SET_DATE"):
                _, date_value = instr.split()
                maturity_date = datetime.datetime.strptime(date_value, "%d/%m/%Y")
            elif instr.startswith("SET_PERIOD"):
                _, period_days = instr.split()
                period_days = int(period_days)
            elif instr == "CALCULATE_MATURITY":
                if maturity_date is not None:
                    end_date = maturity_date + datetime.timedelta(days=period_days)
                    print(f"Maturity date after period: {end_date.strftime('%d/%m/%Y')}")
                else:
                    print("Error: Maturity date not set before calculation")