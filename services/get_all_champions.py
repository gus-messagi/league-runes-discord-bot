import requests
import re

from requests.exceptions import HTTPError

try:
  response = requests.get('https://lolstatic-a.akamaihd.net/frontpage/apps/prod/harbinger-l10-website/pt-br/production/pt-br/page-data/champions/page-data.json')

  response.raise_for_status()

except HTTPError as http_error:
  print(f'HTTP error occurred: {http_error}')
except Exception as err:
  print(f'Other error occurred: {err}')
else:
  response.encoding = "utf-8"
  all_champions = re.findall("(?<=/champions/)\w+", response.text)

  file = open("champions_list.txt", "w")

  for index in range(0, len(all_champions)):
    if (index == len(all_champions) - 1):
      file.write(all_champions[index])
    else:
      file.write(f"{all_champions[index]},")

  file.close()