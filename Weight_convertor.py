# Python weight convertor.
wt = float(input("Enter your Weight: "))
unit = input("Kilogram or pound ? ( K Or L): ").upper()

if unit == "K":
    wt = wt*2.205
    unit = "Lbs."
elif unit =="L":
    wt = wt / 2.205
    unit = "Kgs"
else:
    print(f" {unit} was not valid..... ")
    
print(f" Your weight is {wt} {unit}")    