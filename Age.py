name = input("Enter the student's name: ")
age = int(input("Enter your age: "))

if age < 10:
    print(name, ", to enroll, you must be at least 10 years old.")
else:
    if age > 20:
        print(name, ", enrollment is limited to individuals aged 20 and under.")
    else:
        print(name, ", you are eligible to enroll.")