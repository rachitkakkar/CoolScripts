from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def search(query):
    open('geckodriver.log', 'w').close() #Clear Log File

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(f'https://duckduckgo.com/{query}')
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    results = []

    if soup.find_all(class_="no-results t-m") == []:
        for i in range(len(soup.find_all(class_="result results_links_deep highlight_d result--url-above-snippet"))):
            result = {}

            result["title"] = soup.find_all(class_="result__a")[i].get_text()
            result['domain'] = soup.find_all(class_="result__url js-result-extras-url")[i]['href']
            result['description'] = soup.find_all(class_="result__snippet js-result-snippet")[i].get_text()
            results.append(result)
 
        return results

    else:
        return None

print(search("hello"))
