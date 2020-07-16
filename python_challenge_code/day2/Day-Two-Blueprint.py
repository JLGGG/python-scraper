"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

def is_on_list(days, selected_day):
    if selected_day in days:
      return True
    else:
      return False

def get_x(days, selected_number):
  return days[selected_number]

def add_x(days, want_to_add_day):
  days.append(want_to_add_day)

def remove_x(days, want_to_delete_day):
  days.remove(want_to_delete_day)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #




