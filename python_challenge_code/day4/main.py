from url import check_url
import os

def not_valid_answer_recheck():
  print("Do you want to start over? y/n")
  answer = input()
  if answer == 'y':
    return 1
  elif answer == 'n':
    return 0
  else:
    return -1

while True:
  print("Welcome to IsItDown.py!")
  check_url()

  print("Do you want to start over? y/n")
  answer = input()
  if answer == 'y':
    os.system('clear')
    continue
  elif answer == 'n':
    print("bye")
    break
  else:
    while True:
      print("That's not a valid answer")
      result = not_valid_answer_recheck()
      if result == -1:
        continue
      else:
        break
    if result == 1:
      os.system('clear')
      continue
    elif result == 0:
      print("bye")
      break


