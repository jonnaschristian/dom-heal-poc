import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = r"C:\Users\Jonnas\Documents\dom-heal-poc\chromedriver-win64\chromedriver.exe"
URL = "http://localhost:8000/home.html"

with open("../elements/post.json", encoding="utf-8") as f:
    POST_SELECTORS = json.load(f)

def aguarda_elemento(driver, by, selector, timeout=10):
    for _ in range(timeout * 2):
        try:
            el = driver.find_element(by, selector)
            if el.is_displayed():
                return el
        except Exception:
            pass
        time.sleep(0.5)
    raise Exception(f"Elemento {selector} não ficou visível em {timeout}s.")

service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # Teste 1: Deve exibir corretamente o título, autor e data do post individual
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(By.XPATH, POST_SELECTORS["menu"]).click()

    titulo = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["titulo"])
    assert titulo.text == "Man must explore, and this is exploration at its greatest", f"Título errado: {titulo.text}"

    autor = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["autor"])
    assert "Start Bootstrap" in autor.text, f"Autor errado: {autor.text}"

    meta = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["meta"])
    assert "August 24, 2023" in meta.text, f"Data errada: {meta.text}"

    print("Teste 1 PASSOU")

    # Teste 2: Deve exibir o conteúdo principal do post
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(By.XPATH, POST_SELECTORS["menu"]).click()

    conteudo = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["conteudo"])
    assert conteudo.is_displayed() and conteudo.text.strip() != "", "Conteúdo principal não visível ou vazio"

    print("Teste 2 PASSOU")

finally:
    driver.quit()
