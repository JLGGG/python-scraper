from extract import extract_information

result = extract_information()

print("Hello! Please choose select a country by number: ")
for x in result:
  print(f'# {result.index(x)} {x[0]}')

while(True):
  try:
    answer = int(input('#: '))
    if answer > len(result):
      print("Choose a number from the list.")
      continue
    print(f'The currecy code is {result[answer][1]}')
    break
  except Exception as ex:
    print("That wasn't a number")
    continue


