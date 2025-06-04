*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           JSONLibrary

Suite Setup       Carregar Seletores

*** Variables ***
${URL}            http://localhost:8000
${CHROMEDRIVER}   ../../chromedriver-win64/chromedriver.exe
${SELECTORS}      ${EMPTY}

*** Keywords ***
Carregar Seletores
    [Documentation]    Carrega o arquivo JSON com os seletores da página.
    ${json}    Load JSON From File    ../elements/about.json
    Set Suite Variable    ${SELECTORS}    ${json}

Abrir Navegador e Acessar Menu
    [Documentation]    Abre o navegador e clica no menu About.
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service(executable_path="${CHROMEDRIVER}")    sys
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    ${driver}=     Create WebDriver    Chrome    options=${options}    service=${service}
    Go To    ${URL}
    Maximize Browser Window
    Click Element   css=${SELECTORS['menu']}

Fechar Navegador
    [Documentation]    Fecha o navegador.
    Close Browser

Validar Conteúdo da Página About
    [Documentation]    Valida título, subtítulo e se o texto está visível na About.
    Wait Until Element Is Visible    css=${SELECTORS['titulo']}       10s
    Element Text Should Be           css=${SELECTORS['titulo']}       About Me
    Element Text Should Be           css=${SELECTORS['subtitulo']}    This is what I do.
    Element Should Be Visible        css=${SELECTORS['texto']}
    # Capture Page Screenshot        # Descomente para tirar print em cada validação

*** Test Cases ***
Validar Título e Textos da Página About
    [Documentation]    Testa se o About mostra o título, subtítulo e texto esperados.
    [Setup]        Abrir Navegador e Acessar Menu
    Validar Conteúdo da Página About
    [Teardown]     Fechar Navegador
