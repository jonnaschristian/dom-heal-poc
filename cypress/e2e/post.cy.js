describe('Menu Post', () => {
  let post;

  before(() => {
    cy.fixture('elements/post.json').then((dados) => {
      post = dados;
    });
  });

  it('Deve exibir corretamente o título, autor e data do post individual', () => {
    cy.xpath(post.menu).click();

    cy.xpath(post.titulo)
      .should('be.visible')
      .and('have.text', 'Man must explore, and this is exploration at its greatest');
    cy.xpath(post.autor)
      .should('be.visible')
      .and('contain', 'Start Bootstrap');
    cy.xpath(post.meta)
      .should('contain', 'August 24, 2023');
  });

  it('Deve exibir o conteúdo principal do post', () => {
    cy.xpath(post.menu).click();
    cy.xpath(post.conteudo).should('be.visible').and('not.be.empty');
  });
});