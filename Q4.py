# Write a program in Python to compute simple Interest.
class SimpleInterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_simple_interest(self):
        simple_interest = (self.principal * self.rate * self.time) / 100
        return simple_interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))

    calculator = SimpleInterestCalculator(principal, rate, time)
    simple_interest = calculator.calculate_simple_interest()

    print(f"The simple interest is: {simple_interest}")
    print(f"The total amount after {time} years is: {principal + simple_interest}")

if __name__ == "__main__":
    main()
