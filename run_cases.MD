
# Financial and Simple Interest Calculations

## Run cases

### Basic Simple Interest Calculation

Input
```bash
CALCULATE INTEREST AMOUNT 1000 RATE 5 TIME 2 YEARS
```
Log
```bash
Total amount after interest: 1100.0
```
---

### Definition of Rate without Interest Calculation

Input
```bash
DEFINE RATE 3
```
Log

NOT expected output for the calculation. Check that no syntactic or semantic errors occur.

---

### Interest Calculation with Payment and Balance

Input
```bash
DEFINE RATE 4
CALCULATE INTEREST AMOUNT 1500 RATE 4 TIME 1 YEARS
PAYMENT 200
BALANCE
```
Log
```bash
Total amount after interest: 1560.0
Balance after payment: 1360.0
```

---

### Extensive Use of Features

Input
```bash
CALCULATE INTEREST AMOUNT 2000 RATE 3.5 TIME 3 YEARS
SAVINGS
INVESTMENT
ANNUITY
CALCULATE MATURITY DATE 01/01/2024 PERIOD 30 DAYS
```
Log
```bash
Total amount after interest: 2210.0
Maturity date after period: 31/01/2024
```

---

### Semantic errors

Input
```bash
CALCULATE INTEREST AMOUNT -100 RATE 5 TIME 2 YEARS
```
Log
```bash
Compilation error: Semantic error at token X: Amount must be a positive number
```

---
Input
```bash
CALCULATE INTEREST AMOUNT 1000 RATE 150 TIME 2 YEARS
```
Log
```bash
Compilation error: Semantic error at token X: Rate must be between 0 and 100
```

---

### Date Manipulation

Input
```bash
CALCULATE MATURITY DATE 12/31/2023 PERIOD 365 DAYS
```
Log
```bash
Maturity date after period: 31/12/2024
```

---