import os
from babel.numbers import format_currency
from extract import extract_information, convert_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

def main():
  flag = False
  result = extract_information()
  temp = []

  print("Welcome to CurrencyConvert PRO 2000\n")
  for x in result:
    print(f'# {result.index(x)} {x[0]}')
  
  print("Where are you from? Choose a country by number.\n")

  while(True):
    try:
      answer = int(input('#: '))
      if answer >= len(result):
        print("Choose a number from the list.")
        continue
      print(result[answer][0])
      temp.append(result[answer])
      
      if flag == True:
        break
      else:
        flag = True
        print("\nNow choose another country.\n")
    except ValueError:
      print("That wasn't a number.")
      continue

  print(f'\nHow many {temp[0][1]} do you want to conver to {temp[1][1]}?')

  while(True):
    try:
      money = int(input())
      break
    except ValueError:
      print("That wasn't a number.")
  
  request_url = f'https://transferwise.com/gb/currency-converter/{temp[0][1]}-to-{temp[1][1]}-rate?amount={money}'
  
  unit = float(convert_currency(request_url))
  print(f"{format_currency(money, temp[0][1], locale='ko_KR')} is {format_currency(money*unit, temp[1][1], locale='ko_KR')}")

main()