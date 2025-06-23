import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER_PATH = r"../../chromedriver-win64/chromedriver.exe"
URL = "http://localhost:8000/home.html"

def load_home_selectors():
    with open("../elements/home.json", encoding="utf-8") as f:
        return json.load(f)

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

def test_titulo_e_subtitulo_blog(driver):
    HOME_SELECTORS = load_home_selectors()
    driver.get(URL)
    driver.maximize_window()
    titulo = aguarda_elemento(driver, By.CSS_SELECTOR, HOME_SELECTORS["tituloCabecalho"])
    subtitulo = aguarda_elemento(driver, By.CSS_SELECTOR, HOME_SELECTORS["subtituloCabecalho"])
    assert titulo.text == "Clean Blog", f"Título errado: {titulo.text}"
    assert subtitulo.text == "A Blog Theme by Start Bootstrap", f"Subtítulo errado: {subtitulo.text}"

def test_acesso_post_individual_pela_home(driver):
    HOME_SELECTORS = load_home_selectors()
    POST_SELECTORS = load_post_selectors()
    driver.get(URL)
    driver.maximize_window()
    cards = driver.find_elements(By.CSS_SELECTOR, HOME_SELECTORS["cardsPost"])
    assert len(cards) > 0, "Nenhum card de post encontrado na Home"

    primeiro_card = cards[0]
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", primeiro_card)
    primeiro_link = primeiro_card.find_element(By.TAG_NAME, "a")

    # Espera o link ser clicável
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "a")))

    # Tenta clicar normalmente, se não conseguir faz via JS (bypass)
    try:
        primeiro_link.click()
    except Exception:
        driver.execute_script("arguments[0].click();", primeiro_link)

    titulo_post = aguarda_elemento(driver, By.XPATH, POST_SELECTORS["titulo"])
    assert titulo_post.is_displayed() and titulo_post.text.strip() != "", "Título do post não visível ou vazio"
