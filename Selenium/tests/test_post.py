import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = r"../../chromedriver-win64/chromedriver.exe"
URL = "http://localhost:8000/home.html"

def load_post_selectors():
    with open("../elements/post.json", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def driver():
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

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

def test_post_titulo_autor_data(driver):
    POST_SELECTORS = load_post_selectors()
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(By.XPATH, POST_SELECTORS["menu"]).click()

    titulo = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["titulo"])
    assert titulo.text == "Man must explore, and this is exploration at its greatest", f"Título errado: {titulo.text}"

    autor = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["autor"])
    assert "Start Bootstrap" in autor.text, f"Autor errado: {autor.text}"

    meta = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["meta"])
    assert "August 24, 2023" in meta.text, f"Data errada: {meta.text}"

def test_conteudo_principal_post(driver):
    POST_SELECTORS = load_post_selectors()
    driver.get(URL)
    driver.maximize_window()
    driver.find_element(By.XPATH, POST_SELECTORS["menu"]).click()

    conteudo = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["conteudo"])
    assert conteudo.is_displayed() and conteudo.text.strip() != "", "Conteúdo principal não visível ou vazio"
