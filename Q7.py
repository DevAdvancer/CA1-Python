# Write a program in Python to convert a given number of days into days, month, year and week.
class DateConverter:
    def __init__(self, days):
        self.days = days

    def convert_to_weeks(self):
        return self.days // 7, self.days % 7

    def convert_to_months(self):
        months = self.days // 30
        remaining_days = self.days % 30
        return months, remaining_days

    def convert_to_years(self):
        years = self.days // 365
        remaining_days = self.days % 365
        return years, remaining_days


def main():
    days = int(input("Enter the number of days: "))
    converter = DateConverter(days)

    weeks, remaining_days = converter.convert_to_weeks()
    months, remaining_days_in_month = converter.convert_to_months()
    years, remaining_days_in_year = converter.convert_to_years()

    print(f"{days} days is equivalent to:")
    print(f"Weeks: {weeks} weeks and {remaining_days} days")
    print(f"Months: {months} months and {remaining_days_in_month} days")
    print(f"Years: {years} years and {remaining_days_in_year} days")


if __name__ == "__main__":
    main()
