grade = int(input("Please enter the grade you got on the last test: "))

if grade >= 90:
    print("Awesome! That's an A!")
elif grade >= 80 and grade < 90:
    print("Hey, a B isn't so bad.")
elif grade >= 70 and grade < 80:
    print("Could do better, keep improving.")
elif grade >= 65 and grade < 70:
    print("D is for dude.. seriously?")
elif grade >= 0 and grade < 65:
    print("Yeah, you failed")