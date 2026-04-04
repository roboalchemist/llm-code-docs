# Source: https://cypress.visual-image-diff.dev/getting-started/cypress-integration.md

# Cypress integration

Follow the steps below to have access to the comparison command so you can build visual regression tests

### Setup

Install Cypress:

```sh
npm i -D cypress
```

Install the core package and the HTML report:

```sh
npm i -D cypress-image-diff-js cypress-image-diff-html-report
```

Then initialise Cypress if you don't have a project:

```sh
npx cypress open
```

Finally follow a suitable option for you below:

* [Typescript](https://cypress.visual-image-diff.dev/getting-started/cypress-integration/typescript)
* [Javascript](https://cypress.visual-image-diff.dev/getting-started/cypress-integration/javascript)
* [Cypress < v10](https://cypress.visual-image-diff.dev/getting-started/cypress-integration/cypress-less-than-v10)

Once the above is complete, you will be all set to [write a test](https://cypress.visual-image-diff.dev/getting-started/..#writing-a-test)!

If you have any struggles with integration, please refer to [these examples](https://github.com/kien-ht/cypress-image-diff-html-report/tree/1aad688d5f4806be82a85c8bce1461cb0dbe4d79/examples).
