function registerUser(username, email) {
    cy
        .visit('/register')
        .get('input[name="username"]').type(username)
        .get('input[name="email"]').type(email)
        .get('input[name="password"]').type('test')
        .get('input[type="submit"]').click();
}

function logOutUser() {
    cy.get('.navbar-burger').click();
    cy.contains('Log Out').click();
}

function logInUser(email) {
    cy
        .get('a').contains('Log In').click()
        .get('input[name="email"]').type(email)
        .get('input[name="password"]').type('test')
        .get('input[type="submit"]').click()
        .wait(100)
}

export { registerUser, logOutUser, logInUser }