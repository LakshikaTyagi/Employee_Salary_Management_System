class Employee:
    def __init__(self, emp_id, name, basic_salary):
        # Encapsulation (private variables)
        self.__emp_id = emp_id
        self.__name = name
        self.__basic_salary = basic_salary

        # Salary components
        self.__hra = 0
        self.__da = 0
        self.__tax = 0
        self.__gross = 0
        self.__net = 0

    # Method to calculate salary components
    def calculate_salary(self):
        self.__hra = 0.20 * self.__basic_salary   # 20% HRA
        self.__da = 0.10 * self.__basic_salary    # 10% DA
        self.__tax = 0.05 * self.__basic_salary   # 5% Tax

        self.__gross = self.__basic_salary + self.__hra + self.__da
        self.__net = self.__gross - self.__tax

    # Method to display salary details
    def display_salary(self):
        print("\n===== EMPLOYEE SALARY SLIP =====")
        print(f"Employee ID   : {self.__emp_id}")
        print(f"Name          : {self.__name}")
        print(f"Basic Salary  : {self.__basic_salary:.2f}")
        print(f"HRA (20%)     : {self.__hra:.2f}")
        print(f"DA (10%)      : {self.__da:.2f}")
        print(f"Tax (5%)      : {self.__tax:.2f}")
        print(f"Gross Salary  : {self.__gross:.2f}")
        print(f"Net Salary    : {self.__net:.2f}")
        print("================================\n")


# Main Program
def main():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    emp = Employee(emp_id, name, basic_salary)
    emp.calculate_salary()
    emp.display_salary()


# Run
main()