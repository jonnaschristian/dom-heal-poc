describe('Menu Home', () => {
  let home, post;

  before(() => {
    cy.fixture('elements/home.json').then((dadosHome) => {
      home = dadosHome;
    });
    cy.fixture('elements/post.json').then((dadosPost) => {
      post = dadosPost;
    });
  });

  it('Deve exibir corretamente o título e subtítulo do blog', () => {
    cy.get(home.tituloCabecalho).should('be.visible').and('have.text', 'Clean Blog');
    cy.get(home.subtituloCabecalho).should('be.visible').and('have.text', 'A Blog Theme by Start Bootstrap');
  });

  it('Deve permitir acessar um post individual a partir de um card na Home', () => {
    cy.get(home.cardsPost).should('exist').and('have.length.greaterThan', 0);
    cy.get(home.cardsPost).first().find('a').first().click();
    cy.xpath(post.titulo).should('be.visible').and('not.be.empty');
  });
});
