import pathlib
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.leagueofgraphs.com/champions/runes/kaisa'

dir_path = pathlib.Path(__file__).parent.absolute()

javascript_file = open(f"{dir_path}/js/html2canva.min.js", "r").read()

javascript_script = (
  'html2canvas(document.querySelector("#runesColumn")).then(canvas => {'
  'document.body.appendChild(canvas)'
  '});'
)

with webdriver.Chrome(f"{dir_path}/chromedriver") as browser:
  browser.get(url)

  browser.execute_async_script(javascript_file)
  browser.execute_async_script(javascript_script)

#   html = browser.page_source

# soup = BeautifulSoup(html, "html.parser")

# runes_div = soup.find("div", id="runesColumn")

# print(runes_div)

#runesColumn