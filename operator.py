"""
1. Logical Operator :
Or : We check multiple condition, at least one of those condition must be True.
AND: We check multiple condition, All conditions must be True.
NOT: It inverts the condition. (Not False, Not True.)
        
"""
#OR
temp = 45
is_rain = False
if temp > 25 or temp <0 or is_rain:
    print("Event cancel")
else:
    print("We will do event")