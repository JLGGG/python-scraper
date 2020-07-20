import os
import csv
import requests
import math
from bs4 import BeautifulSoup

def save_to_file(name, jobs):
  file = open(f'{name}.csv', mode="a")
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for job in jobs:
    writer.writerow(job)
  return

def create_job_csv(name, url):
  pay = []
  company = []
  if get_last_page_number(name, url) != 0:
    count = get_last_page_number(name, url)

    for n in range(count):
      if name == "ELAND FASHION":
        search_url = f"http://www.alba.co.kr/job/brand/elandfashion/?page={n+1}"
      else:
        search_url = f"{url}job/brand/?page={n+1}"
      result = requests.get(search_url)
      soup = BeautifulSoup(result.text, "html.parser")
      page_info = soup.find("div", {"class":"goodsList"})

      place = page_info.find_all("span", {"class":"company"})
      title = page_info.find_all("span", {"class":"title"})
      time = page_info.find_all("td", {"class":"data"})
      pay_method = page_info.find_all("span", {"class":"payIcon"})
      pay_amount = page_info.find_all("span", {"class":"number"})
      date = page_info.find_all("td", {"class":"regDate"})
      for x in range(len(place)):
        place[x] = place[x].get_text()
        title[x] = title[x].get_text()
        time[x] = time[x].get_text()
        pay.append(pay_method[x].get_text() + pay_amount[x].get_text())
        date[x] = date[x].get_text()
      company = list(zip(place, title, time, pay, date))
      save_to_file(name, company)
  else:
    save_to_file(name, company)

def get_last_page_number(name, sub_url):
  none_info = "해당 조건/분류에 일치하는 채용정보가 없습니다."
  result = requests.get(sub_url)
  soup = BeautifulSoup(result.text, "html.parser")
  page = soup.find("div", {"class":"goodsList"})
  td = page.find_all("td")
  for x in td:
    td[td.index(x)] = x.get_text()

  if none_info in td:
    return 0
  else:
    if name == "ELAND FASHION":
      page_number = page.find("p", {"class":"listCount"}).get_text()
      page_number = page_number.replace("\n 총", "")
      page_number = page_number.replace("\r\n\t\t", "")
      page_number = page_number.replace("건", "")
    else:
      page_number = page.find("p", {"class":"jobCount"}).get_text()
      page_number = page_number.replace("건", "")
      page_number = page_number.replace(",", "")
    page_count = math.ceil(int(page_number)/50)
    return page_count

os.system("clear")
alba_url = "http://www.alba.co.kr"

result = requests.get(alba_url)
soup = BeautifulSoup(result.text, "html.parser")

company = []
company_name = []
company_href = []
company_list = soup.find("div", id="MainSuperBrand")
company_info = company_list.find_all("li", {"class": "impact"})

for info in company_info:
  company_href.append(info.find("a", {"class":"goodsBox-info"})["href"])
  company_name.append(info.find("span", {"class": "company"}).get_text())
  
company = list(zip(company_name, company_href))

for x in range(len(company)):
  name = company[x][0]
  url = company[x][1]
  print(f'{name} scraping company contents.')
  create_job_csv(name, url)

#create_job_csv("호텔신라", "http://shilla.alba.co.kr/")

print("--------------------End-----------------------")


