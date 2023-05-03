import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


url_amazon = 'https://www.amazon.com'

# Configurando Selenium
options = Options()
options.add_argument('window-size=2000,2000')
service = Service(ChromeDriverManager().install())

# Ativação do Selenium
navegador = webdriver.Chrome(service=service, options=options)


navegador.get(url=url_amazon)
time.sleep(2)

# Clica no Botão 'Delivery to'
navegador.find_element(By.ID, 'nav-global-location-popover-link').click()
time.sleep(2)

# Insere o ZIP CODE - Chicago
navegador.find_element(By.ID, 'GLUXZipUpdateInput').send_keys('60601')
navegador.find_element(By.ID, 'GLUXZipUpdate').click()
time.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="a-popover-1"]/div/div[2]/span').click()
time.sleep(2)

# Clica no menu 'ALL'
navegador.find_element(By.ID, 'nav-hamburger-menu').click()
time.sleep(2)

# Clica em 'See ALL'
navegador.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/ul[1]/li[22]/a[1]').click()
time.sleep(2)

# Coleta as informações da página
page_content = navegador.page_source
site_bs = BeautifulSoup(page_content, 'html.parser')


def category_name(site):
    return site.find('a', {'data-menu-id': i}).get_text(strip=True)

# def category_url(site):
#     return site.find('a', {'data-menu-id': i}).get('href')

