import os
import requests
from bs4 import BeautifulSoup

def extract_information():
  os.system("clear")
  url = "https://www.iban.com/currency-codes"

  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")

  table = soup.find("table", {"class": "table"})

  informations = table.find_all('td')

  refined_countrys = []
  refined_currencies = []

  count = 0
  for x in informations:
    informations[informations.index(x)] = informations[informations.index(x)].get_text()
    count += 1

  for x in range(0, count, 4):
    if informations[x+2] == "":
      continue
    refined_countrys.append(informations[x])

  for x in range(2, count, 4):
    if informations[x] == "":
      continue
    refined_currencies.append(informations[x])

  res = list(zip(refined_countrys, refined_currencies))
  return res

def convert_currency(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  unit = soup.find("span", {"class": "text-success"}).get_text()
  return unit