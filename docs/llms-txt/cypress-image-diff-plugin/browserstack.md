# Source: https://cypress.visual-image-diff.dev/getting-started/cypress-integration/browserstack.md

# Browserstack

## Setup

Install `browserstack-cypress-cli` package

* `yarn add browserstack-cypress-cli` OR `npm i browserstack-cypress-cli`

Run `browserstack-cypress-cli init`

* This will generate your browserstack.json file

Update the generated `browserstack.json` file with your Browserstack credentials and some configs

Required changes

* replace the `auth` credentials
* update `cypress_config_file` location, e.g. to `cypress.config.js`
* update `parallels` option, e.g. to `"1"`
* set `downloads` to your cypress-image-diff screenshot and report location:
  * it will be used later on when updating baseline images
  * for example:

    <pre class="language-json" data-full-width="true"><code class="lang-json">"downloads": ["./cypress-image-diff-screenshots", "./cypress-image-diff-html-report"]
    </code></pre>
* add all your test running dependencies to `npm_dependencies`

Recommended changes

* update the browsers section according to your preferences
  * *reference:* [*https://www.browserstack.com/docs/automate/cypress/browsers-and-os*](https://www.browserstack.com/docs/automate/cypress/browsers-and-os)

## Running the tests

You can now run the tests with the `browserstack-cypress run` command

*Reference:* [*https://www.browserstack.com/docs/automate/cypress#run-your-first-test*](https://www.browserstack.com/docs/automate/cypress#run-your-first-test)

## Artifacts

Upon running the `browserstack-cypress run` command with the `--sync` flag. It will sync the Browserstack build's artifacts to your local machine under `build_artifacts` folder.&#x20;

*Reference:* [*https://www.browserstack.com/docs/automate/cypress/custom-reports-build-artifacts*](https://www.browserstack.com/docs/automate/cypress/custom-reports-build-artifacts)

## Updating baseline images

After running the tests with the previously mentioned `browserstack-cypress run` command you can simply copy the given comparison image from your local `build_arfifacts/build_id/../../cypress-image-diff-screenshots/comparison` folder and move it to the `cypress-image-diff-screenshots/baseline` images folder. Which will serve as the new basline images for any futures test runs.

### Creating browser + OS specific baseline images

In order to create browser specific baseline image we can use Cypress environmental variables.

For example:

```typescript
describe('template spec', () => {
  it('passes', () => {
    cy.visit('../../report-example.html')
    cy.contains('Data Hub home page search bar - chrome').should('be.visible')
    cy.compareSnapshot(`${Cypress.env('BROWSER')}-example`)
  })
})
```

When running the&#x20;

`CYPRESS_BROWSER="chrome@latest:OS X Ventura" browserstack-cypress run --sync --browser "chrome@latest:OS X Ventura"`

* It will override the browser configs in `browserstack.json` file
* Tests will generate browser/OS specific baselines image like `browserstack.spec.cy.ts-chrome@latest:OS X Ventura-example.png`

Drawback: You have to trigger a new browserstack build for each browser and OS combinations

## Example project setups

#### Javascript

<https://github.com/tamasmagyar/cypress-image-diff-js-browserstack-integration>

#### Typescript

<https://github.com/tamasmagyar/cypress-image-diff-js-browserstack-integration-typescript>

## Example browserstack.json

```json
{
    "auth": {
        "username": "your_username",
        "access_key": "your_access_key"
    },
    "browsers": [
        {
            "browser": "chrome",
            "os": "Windows 10",
            "versions": [
                "latest",
                "latest-1"
            ]
        }
    ],
    "run_settings": {
        "cypress_config_file": "cypress.config.js",
        "project_name": "project-name",
        "build_name": "build-name",
        "exclude": [],
        "parallels": "1",
        "npm_dependencies": {
            "browserstack-cypress-cli": "^1.25.3",
            "cypress": "^13.2.0",
            "cypress-image-diff-js": "^1.30.1"
        },
        "package_config_options": {},
        "headless": true
    },
    "connection_settings": {
        "local": false,
        "local_identifier": null,
        "local_mode": null,
        "local_config_file": null
    },
    "disable_usage_reporting": false
}
```
