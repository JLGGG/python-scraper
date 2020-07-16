import os
import requests
from requests.exceptions import HTTPError

def check_validation_url(str):
  search = [".com", ".co", ".it", ".net"]
  for x in search:
    if str.find(x) != -1:
      return 1
  return -1
    
def check_url():
  str_http = "http://"
  str_https = "https://"

  input_list = list(map(str, input("Please write a URL or URLs you want to check. (separated by comma)\n").split(',')))

  for x in input_list:
    input_list[input_list.index(x)] = x.strip()

  for x in input_list:
    if not str_http in x and not str_https in x:
      input_list[input_list.index(x)] = str_http + x
    else: pass

  for url in input_list:
    if check_validation_url(url) == -1:
      print(f"{url} is not a valid URL")
      continue
    try:
      response = requests.get(url)
      response.raise_for_status()  
    except HTTPError as http_err:
      print(f'HTTP error occurred: {http_err}')
    except Exception:
      print(f'{url} is down')
    else:
      print(f'{url} is up')