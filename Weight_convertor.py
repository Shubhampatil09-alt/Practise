# # Python weight convertor.
# wt = float(input("Enter your Weight: "))
# unit = input("Kilogram or pound ? ( K Or L): ").upper()

# if unit == "K":
#     wt = wt*2.205
#     unit = "Lbs."
# elif unit =="L":
#     wt = wt / 2.205
#     unit = "Kgs"
# else:
#     print(f" {unit} was not valid..... ")
    
# print(f" Your weight is {wt} {unit}")    
#==========================================================================
# Temperatur conversion program.

unit =  input("Enter Unit (C/F): ").upper()
temp = float(input("Enter the Temp: "))
if unit == "C":
    temp = round((9*temp)/ 5+32,1)
    print(f"Temperature in Farhenit:  {temp} C")
elif unit == "F":
    temp = round((temp - 32) *5/9,1)
    print(f"Temperature in Celsius:  {temp} F")
else:
    print(f"{unit} is invalid of measure")
print("")

#---------------------------------------------------------------