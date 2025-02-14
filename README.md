# Financial and Simple Interest Calculations, Compiler Workshop

Welcome to the **Financial Interest Compiler Workshop**! This workshop is designed to help you understand and utilize the Financial Interest Compiler for your financial calculations and data processing needs.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The **Financial Interest Compiler** is a specialized tool for compiling and analyzing financial data, particularly focusing on simple interest calculations, balance updates, and maturity date computations. This workshop will guide you through the process of setting up, using, and contributing to the Financial Interest Compiler project.

## Prerequisites
Before you begin, ensure you have the following:
- Basic knowledge of financial calculations and simple interest formulas
- Python installed on your machine (version 3.6 or higher)
- Git installed on your machine

## Installation
To install the Financial Interest Compiler, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/jason-ptm/stadistic-compiler.git
    ```
2. Navigate to the project directory:
    ```sh
    cd financial-interest-compiler
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To use the Financial Interest Compiler, follow these steps:

1. Run the compiler with a command file containing financial calculations:
    ```sh
    python run_compiler.py examples/example_3.txt
    ```
2. The output will display computed interest amounts, balance adjustments, and maturity date calculations.

### Example Commands
- **Simple Interest Calculation:**
    ```sh
    CALCULATE INTEREST AMOUNT 1000 RATE 5 TIME 2 YEARS
    ```
    **Output:**
    ```sh
    Total amount after interest: 1100.0
    ```

- **Defining an Interest Rate:**
    ```sh
    DEFINE RATE 3
    ```

- **Handling Payments and Balance Adjustments:**
    ```sh
    DEFINE RATE 4
    CALCULATE INTEREST AMOUNT 1500 RATE 4 TIME 1 YEARS
    PAYMENT 200
    BALANCE
    ```
    **Output:**
    ```sh
    Total amount after interest: 1560.0
    Balance after payment: 1360.0
    ```

## Contributing
We welcome contributions to the Financial Interest Compiler project! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Create a pull request.

