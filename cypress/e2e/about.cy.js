describe('Menu About', () => {
  let about;

  before(() => {
    cy.fixture('elements/about.json').then((dados) => {
      about = dados;
    });
  });
  
  it('Deve exibir corretamente o título e texto principal da página About', () => {
    cy.get(about.menu).click();

    cy.get(about.titulo).should('be.visible').and('contain', 'About Me');
    cy.get(about.subtitulo).should('be.visible').and('contain', 'This is what I do.');
    cy.get(about.texto).should('be.visible').and('not.be.empty');
  });
});