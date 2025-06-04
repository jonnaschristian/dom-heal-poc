import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Caminho para o chromedriver
CHROMEDRIVER_PATH = r"C:\Users\Jonnas\Documents\dom-heal-poc\chromedriver-win64\chromedriver.exe"
URL = "http://localhost:8000"

# Carrega os seletores do JSON (ajuste o caminho conforme sua estrutura!)
with open("../elements/about.json", encoding="utf-8") as f:
    SELECTORS = json.load(f)

service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(URL)
    driver.maximize_window()

    # Clica no menu About
    driver.find_element(By.CSS_SELECTOR, SELECTORS["menu"]).click()
    time.sleep(1)  # Ajuste para WebDriverWait se quiser mais robusto

    # Valida título
    titulo = driver.find_element(By.CSS_SELECTOR, SELECTORS["titulo"])
    assert "About Me" in titulo.text and titulo.is_displayed(), "Título incorreto ou não visível"

    # Valida subtítulo
    subtitulo = driver.find_element(By.CSS_SELECTOR, SELECTORS["subtitulo"])
    assert "This is what I do." in subtitulo.text and subtitulo.is_displayed(), "Subtítulo incorreto ou não visível"

    # Valida texto principal visível e não vazio
    texto = driver.find_element(By.CSS_SELECTOR, SELECTORS["texto"])
    assert texto.is_displayed() and texto.text.strip() != "", "Texto principal não visível ou vazio"

    print("Teste About PASSOU!")

finally:
    driver.quit()
