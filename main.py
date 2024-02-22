def main():
    # workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
def main():
    hours_worked = int(input('Enter your work hours: '))
    regular_hours_worked = 40
    reg_rate = 18.25
    ov_rate = 27.78


    overtime = hours_worked - regular_hours_worked
    overtime_wage = overtime * ov_rate
    regular_wage = regular_hours_worked * reg_rate
    total_wage = regular_wage + overtime_wage

    # print(f"Regular hours: {regular_hours_worked} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")
    print (f"Regular hours worked: {regular_hours_worked} Regular Pay: {regular_wage}")
   ##################################################
     # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage

    print(f"Regular hours: {regular_hours_worked} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
