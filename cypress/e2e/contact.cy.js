import { faker } from '@faker-js/faker';

describe('Menu Contato', () => {
  let contact;

  before(() => {
    cy.fixture('contact.json').then((dados) => {
      contact = dados;
    });
  });

  it('Enviar mensagem com todos os campos válidos com sucesso', () => {
    const nome = faker.person.fullName();
    const email = 'teste@gmail.com';
    const telefone = faker.phone.number('(##) #####-####');
    const mensagem = faker.lorem.sentence();

    cy.get(contact.menu).click();
    cy.get(contact.tituloContato).should('contain', 'Contact Me');

    cy.get(contact.inputNome).type(nome);
    cy.get(contact.inputEmail).type(email);
    cy.get(contact.inputTelefone).type(telefone);
    cy.get(contact.inputMensagem).type(mensagem);
    cy.get(contact.btnEnviar).click();

    cy.get(contact.mensagemSucesso).should('be.visible').and('contain', 'Form submission successful!');
  });

  it('Enviar mensagem sem os campos preenchidos deve dar erro', () => {
    cy.get(contact.menu).click();
    cy.get(contact.tituloContato).should('contain', 'Contact Me');

    cy.get(contact.btnEnviar).should('have.class', 'disabled');
  });

  it('Não deve permitir enviar mensagem se o e-mail for inválido', () => {
    const nome = faker.person.fullName();
    const telefone = faker.phone.number('(##) #####-####');
    const mensagem = faker.lorem.sentence();

    cy.get(contact.menu).click();
    cy.get(contact.tituloContato).should('contain', 'Contact Me');

    cy.get(contact.inputNome).type(nome);
    cy.get(contact.inputEmail).type('emailinvalido');
    cy.get(contact.inputTelefone).type(telefone);
    cy.get(contact.inputMensagem).type(mensagem);

    cy.get(contact.mensagemErro).should('be.visible').and('contain', 'Email is not valid.');
  });
});