*** Settings ***
Library           SeleniumLibrary
Library           Collections
Library           JSONLibrary

Suite Setup       Carregar Seletores Home e Post

*** Variables ***
${URL}            http://localhost:8000/home.html
${CHROMEDRIVER}   ../../chromedriver-win64/chromedriver.exe
${HOME_SELECTORS}      ${EMPTY}
${POST_SELECTORS}      ${EMPTY}

*** Keywords ***
Carregar Seletores Home e Post
    ${json_home}=    Load JSON From File    ../elements/home.json
    Set Suite Variable    ${HOME_SELECTORS}    ${json_home}
    ${json_post}=    Load JSON From File    ../elements/post.json
    Set Suite Variable    ${POST_SELECTORS}    ${json_post}

Abrir Navegador e Acessar Home
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service(executable_path="${CHROMEDRIVER}")    sys
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    ${driver}=     Create WebDriver    Chrome    options=${options}    service=${service}
    Go To    ${URL}
    Maximize Browser Window

Fechar Navegador
    Close Browser


*** Test Cases ***
Deve exibir corretamente o título e subtítulo do blog
    [Setup]        Abrir Navegador e Acessar Home
    Wait Until Element Is Visible    css=${HOME_SELECTORS['tituloCabecalho']}       10s
    Element Should Be Visible        css=${HOME_SELECTORS['tituloCabecalho']}
    Element Text Should Be           css=${HOME_SELECTORS['tituloCabecalho']}       Clean Blog
    Element Should Be Visible        css=${HOME_SELECTORS['subtituloCabecalho']}
    Element Text Should Be           css=${HOME_SELECTORS['subtituloCabecalho']}    A Blog Theme by Start Bootstrap
    [Teardown]     Fechar Navegador

Deve permitir acessar um post individual a partir de um card na Home
    [Setup]        Abrir Navegador e Acessar Home
    Scroll Element Into View         css=${HOME_SELECTORS['cardsPost']}
    Wait Until Element Is Visible    css=${HOME_SELECTORS['cardsPost']}    10s
    Click Element                    css=${HOME_SELECTORS['cardsPost']} 
    Wait Until Element Is Visible    xpath=${POST_SELECTORS['titulo']}    10s
    Element Should Be Visible        xpath=${POST_SELECTORS['titulo']}
    ${titulo}=    Get Text           xpath=${POST_SELECTORS['titulo']}
    Should Not Be Empty              ${titulo}
    [Teardown]     Fechar Navegador
