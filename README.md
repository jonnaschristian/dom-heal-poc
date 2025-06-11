
# POC — DOM-Heal

**Prova de Conceito: Self-Healing de Seletores Automatizados**

Este repositório apresenta uma POC (Prova de Conceito) para validar a biblioteca `dom-heal`, demonstrando como ela pode ser integrada e utilizada em diferentes frameworks de testes automatizados (Cypress, Robot Framework e Selenium) a partir de cenários reais e controlados.

---

## 🎯 Objetivo da POC

- Demonstrar a capacidade da biblioteca DOM-Heal em identificar e corrigir automaticamente seletores quebrados após mudanças no front-end.
- Validar que a abordagem é agnóstica ao framework: funciona com qualquer suíte de testes web que consome arquivos de seletores.
- Mostrar o ciclo completo: extração do DOM, execução dos testes automatizados, alteração dos seletores e verificação dos resultados.

---

## 🗂️ Estrutura do Repositório

```
POC/
├── Cypress/
│   ├── e2e/         # Testes automatizados Cypress
│   └── fixtures/      # Arquivos JSON de seletores usados nos testes
│
├── Robot/
│   ├── tests/
│   └── resources/     # Arquivos JSON de seletores para Robot
│
├── Selenium/
│   ├── tests/
│   └── elements/      # Arquivos JSON de seletores para Selenium
│
├── Sites
│   ├── A/         # Site de referência original (HTML, CSS, JS)
│   ├── B/         # Site alterado propositalmente (quebra seletores)
│
└── README.md
```

---

## 🕸️ Sites A e B

- **Site A:** É a versão base/original. Os arquivos HTML/CSS/JS aqui representam o funcionamento esperado do sistema — é a referência dos testes.
- **Site B:** É uma versão com pequenas mudanças nos atributos dos elementos (id, class, name, etc), simulando mudanças típicas de manutenção/evolução de front-end e **quebrando** intencionalmente alguns seletores.

> **O objetivo é simular um cenário real: ao migrar os testes para o site B, alguns testes falham pois os seletores antigos não existem mais.**

---

## 🧪 Frameworks de Teste

A POC inclui o mesmo cenário de teste implementado nos três principais frameworks de automação web:

- **Cypress:** Testes escritos em JavaScript, usando os seletores armazenados nos fixtures JSON.
- **Robot Framework:** Testes em linguagem tabular, também utilizando arquivos JSON de seletores.
- **Selenium (Python):** Testes Python, lendo os seletores de arquivos JSON.

> Todos os frameworks consomem os mesmos arquivos de seletores, reforçando a abordagem universal do DOM-Heal.

---

## ⚙️ Fluxo de Uso/Revalidação

1. **Execute os testes automatizados no Site A**  
   (devem passar, já que os seletores batem com o DOM atual)

2. **Altere o alvo dos testes para o Site B**  
   (alguns testes vão falhar, pois os seletores estão desatualizados)

3. **Rode o DOM-Heal passando o JSON e a URL do Site B**  
   ```bash
   dom-heal rodar --json ./Cypress/fixtures/home.json --url http://localhost:8000/siteB/home.html
   ```

4. **Valide que o JSON foi atualizado**  
   O arquivo agora contém os seletores ajustados para o Site B.  
   O log de alterações detalha o que mudou.

5. **Rode novamente os testes com o JSON atualizado**  
   (Os testes devem passar mesmo com as alterações do front-end, sem necessidade de intervenção manual)

---

## 📝 Observações Importantes

- **Cada framework tem sua própria pasta de elementos/fixtures, mas o formato é sempre JSON**.
- É fundamental usar um arquivo de seletores por página para facilitar o controle das alterações.
- A biblioteca DOM-Heal é externa ao projeto de testes: pode ser chamada como CLI ou integrada via adaptação.

---

## 👨‍💻 Requisitos

- Node.js (para Cypress)
- Python 3.7+ (para Robot e Selenium)
- Google Chrome instalado localmente

---

## 🧑‍🏫 Autor

Prova de Conceito por **Jonnas Christian Sousa de Paiva**  
Contato: [jonnaschristian@gmail.com](mailto:jonnaschristian@gmail.com)

---
