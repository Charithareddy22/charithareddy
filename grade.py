sub1 = float(input("Enter marks for Sub1: "))
sub2 = float(input("Enter marks for Sub2: "))
sub3 = float(input("Enter marks for Sub3: "))

avg = (sub1 + sub2 + sub3) / 3

if avg >= 90:
    print("Grade: A")
elif 80 <= avg<90:
    print("Grade: B")
elif 70 <= avg<80:
    print("Grade: C")
else:
    print("Grade: Fail")