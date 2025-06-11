*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           JSONLibrary

Suite Setup       Carregar Seletores Post

*** Variables ***
${URL}            http://localhost:8000/home.html
${CHROMEDRIVER}   ../../chromedriver-win64/chromedriver.exe
${POST_SELECTORS}      ${EMPTY}

*** Keywords ***
Carregar Seletores Post
    ${json_post}=    Load JSON From File    ../elements/post.json
    Set Suite Variable    ${POST_SELECTORS}    ${json_post}

Abrir Navegador e Acessar Menu Post
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service(executable_path="${CHROMEDRIVER}")    sys
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    ${driver}=     Create WebDriver    Chrome    options=${options}    service=${service}
    Go To    ${URL}
    Maximize Browser Window
    Click Element   xpath=${POST_SELECTORS['menu']}

Fechar Navegador
    Close Browser

*** Test Cases ***
Deve exibir corretamente o título, autor e data do post individual
    [Setup]        Abrir Navegador e Acessar Menu Post
    Wait Until Element Is Visible    xpath=${POST_SELECTORS['titulo']}    10s
    Element Should Be Visible        xpath=${POST_SELECTORS['titulo']}
    Element Text Should Be           xpath=${POST_SELECTORS['titulo']}    Man must explore, and this is exploration at its greatest
    Element Should Be Visible        xpath=${POST_SELECTORS['autor']}
    Element Should Contain           xpath=${POST_SELECTORS['autor']}    Start Bootstrap
    Element Should Contain           xpath=${POST_SELECTORS['meta']}     August 24, 2023
    [Teardown]     Fechar Navegador

Deve exibir o conteúdo principal do post
    [Setup]        Abrir Navegador e Acessar Menu Post
    Wait Until Element Is Visible    xpath=${POST_SELECTORS['conteudo']}    10s
    Element Should Be Visible        xpath=${POST_SELECTORS['conteudo']}
    ${conteudo}=    Get Text         xpath=${POST_SELECTORS['conteudo']}
    Should Not Be Empty              ${conteudo}
    [Teardown]     Fechar Navegador
