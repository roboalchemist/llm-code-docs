# Source: https://www.browserstack.com/docs/percy/cypress/getting-started/integrate-your-tests

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Integrate your Cypress tests with Percy
A guide to integrating your Cypress automated tests with BrowserStack Percy. Catch visual differences in your web application on time.

Percy integrates with your tests through both Percy and Automate TurboScale using BrowserStack Cypress CLI. To set up the integration, select the appropriate section and follow the instructions provided.

This documentation applies to Percy Cypress SDK version 3.0.0 and above.

Integrate Percy with your test suite to run visual tests. To do that, follow these steps:

Create a Percy projectSign in toPercy. In Percy, create a project of the type, Web, and then name the project. After the project is created, Percy generates a token. Make a note of it. You have to use it set your environment variable in the next step.

[Sign in to](https://percy.io/signup)For details on creating a project, seeCreate a Percy project.

[Create a Percy project](https://www.browserstack.com/docs/percy/get-started/create-project)Set the project token as an environment variableRun the given command to set PERCY_TOKEN as an environment variable:

To learn about environment variables in Percy, seePercy environment variables.

[Percy environment variables](https://www.browserstack.com/docs/percy/get-started/set-env-var)Install Percy dependenciesInstall the components required to establish the integration environment for your test suite.

To install the dependencies, run the following command:

Update your test script

Import the Percy library to use the method and attributes required to take screenshots.

In order to add Percy snapshots to your Cypress tests, you have to first import the@percy/cypresspackage into yourcypress/support/e2e.jsfile:

`@percy/cypress``cypress/support/e2e.js`If you’re usingTypeScript, include"types": ["cypress", "@percy/cypress"]in yourtsconfig.jsonfile.

`TypeScript``"types": ["cypress", "@percy/cypress"]``tsconfig.json`This gives you access to the Percy snapshot command in any of your Cypress tests, viacy.percySnapshot(). You can now incorporate visual tests in your existing suite:

`cy.percySnapshot()`The snapshot method arguments are:

- name- The snapshot name; must be unique to each snapshot; defaults to the test title
`name`- options-See per-snapshot configuration options
`options`[See per-snapshot configuration options](https://www.browserstack.com/docs/percy/take-percy-snapshots/snapshots-via-scripts#per-snapshot-configuration)For example:

To learn more, seePercy snapshot.

[Percy snapshot](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview)Run PercyRun your tests using thepercy execcommand as shown below:

[percy exec](https://github.com/percy/cli/tree/master/packages/cli-exec#percy-exec)`percy exec`If you are unable to use thepercy:execcommand or prefer to run your tests using IDE run options, you can use thepercy exec:startandpercy exec:stopcommands. To learn more, visitRun Percy.

`percy:exec``percy exec:start``percy exec:stop`[Run Percy](https://www.browserstack.com/docs/percy/take-percy-snapshots/snapshots-via-scripts#commands)–>

### Congratulations!
You have successfully created your first build on Percy. To see the build with snapshots of your application, visit your project in Percy.When you run another build with visual changes to your application, Percy takes new snapshots. You can then see the comparisons between the two runs on the new build.

## Advanced topics

### Percy Snapshot command
In the preceding steps, we used the Percy Snapshot command for capturing snapshots. Percy provides various  configurations to use with Percy snapshot command. To learn more visit,Percy snapshot command.

[Percy snapshot command](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview)
### Base build selection
By default, Percy uses the previous build for comparison however, you always have the option to configure the base build for comparison as needed. To learn more, visitbase build selection logic.

[base build selection logic](https://www.browserstack.com/docs/percy/base-selection/base-build)
## Related topics
- Simplify Percy CLI setup with executables
[Simplify Percy CLI setup with executables](https://www.browserstack.com/docs/percy/common-issue/percy-executable)- Migrate to Percy CLI
[Migrate to Percy CLI](https://www.browserstack.com/docs/percy/migration/migrate-to-cli)- Snapshot vs Screenshot
[Snapshot vs Screenshot](https://www.browserstack.com/docs/percy/overview/basics#screenshots-and-snapshots)- CI/CD
[CI/CD](https://www.browserstack.com/docs/percy/ci-cd/overview)In this tutorial, we will use Cypress’ Kitchen Sink sample app to run our tests. It is an example app provided by Cypress to learn how Cypress works.

This integration works exclusively with BrowserStack TurboScale when used with Percy. When running tests on standard BrowserStack Automate, Percy does not work with the BrowserStack Cypress CLI.

## Prerequisites
- Ensure that you understandCypress fundamentalsand how Cypress runs tests
[Cypress fundamentals](https://www.cypress.io/how-it-works)- Cypress version 13.10
- BrowserStack Username and Access key, which you can find in youraccount settings. If you have not created an account yet, you cansign up for a Free Trialorpurchase a plan
[account settings](https://www.browserstack.com/accounts/settings)[sign up for a Free Trial](https://www.browserstack.com/users/sign_up)[purchase a plan](https://www.browserstack.com/pricing)- NodeJSversion 20.9
[NodeJS](https://nodejs.org/en/download/)
## Run your first test
Perform the following steps to run Cypress tests with Automate Turboscale using the sample Kitchen Sink project.

### Create a Percy project
Sign in toPercy. In Percy, create a project of the type, Web, and then name the project. After the project is created, Percy generates a token. Make a note of it. You have to use it to set your environment variable in the next step.

[Sign in to](https://percy.io/signup)[Create a Percy project](https://www.browserstack.com/docs/percy/get-started/create-project)
### Set the project token as an environment variable
Run the given command to set PERCY_TOKEN as an environment variable:

[Percy environment variables](https://www.browserstack.com/docs/percy/get-started/set-env-var)
### Install Percy and BrowserStack Cypress CLI dependencies
Install the components required to establish the integration environment for your test suite.

```
# Install the BrowserStack Cypress CLI
npm install -g browserstack-cypress-cli
# Install the Percy and Cypress CLI
npm install --save-dev @percy/cypress

```

### Create the configuration file
Create and configure thebrowserstack.jsonfile which contains configurations, such as BrowserStack credentials, capabilities, etc., that are required for running the tests. Use the followinginitcommand to initialize the app project folder and create a boilerplatebrowserstack.jsonfile:

`browserstack.json``init``browserstack.json`
```
browserstack-cypress init

```

`browserstack-cypress init`After thebrowserstack.jsonfile is created, modify or add the mandatory configurations that are required to run the Cypress test as shown in the following sample code. The mandatory configurations are BrowserStack credentials, Turboscale parameters, Cypress configuration file, browser-device combinations, and the number of parallels:

`browserstack.json`
```
// browserstack.json

{
  "auth": {
    "username": "YOUR_USERNAME",
    "access_key": "YOUR_ACCESS_KEY"
  },
  "browsers": [{
      "browser": "chrome",
            "os": "linux",
            "versions": "latest"
    } 
  ],
  "run_settings": {
        "cypress_config_file": "./cypress.config.js",
        "project_name": "new-project",
        "build_name": "new-build",
        "exclude": [],
        "parallels": "2",
        "system_env_vars": ["PERCY_TOKEN"]
        "npm_dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "react-modal": "^3.16.1",
            "react-router-dom": "^6.15.0",
            "@percy/cypress": "^3.1.6"
        },
        "record": true,
        "record-key": "87b774c4-a373-43fa-986e-0833a55dc6d7",
        "projectId": "2m6i88",
        "package_config_options": {},
        "headless": true,
        "turboScale": true,
        "turboScaleOptions": {
            "gridName": "turboscale-trial-grid"
        }
    },
    "disable_usage_reporting": true
}

```

In the above sample code snippet, the following parameters are mandatory to run the test:

- username,access_key
`username``access_key`- browser,os
`browser`- projectId,turboScale
`projectId``turboScale`- PERCY_TOKEN
`PERCY_TOKEN`For more information, seeRun your first Cypress test with Automate Turboscale.

[Run your first Cypress test with Automate Turboscale](https://www.browserstack.com/docs/automate-turboscale/integrate-with-self-hosted-solution/cypress)`@percy/cypress``cypress/support/e2e.js``TypeScript``"types": ["cypress", "@percy/cypress"]``tsconfig.json``cy.percySnapshot()``name``options`[See per-snapshot configuration options](https://www.browserstack.com/docs/percy/take-percy-snapshots/snapshots-via-scripts#per-snapshot-configuration)
### Run tests
Run the test using the following command:

```
npx browserstack-cypress run

```

`npx browserstack-cypress run`
## View your test results
After you run your test, review visual changes in yourPercy project builds.

## Advanced scenario
If you run tests across multiple browsers or use parallels, set thePERCY_PARALLEL_TOTALandPERCY_PARALLEL_NONCEenvironment variableso Percy knows how many parallel workers to expect, and which parallels to combine into a single build. For more information, see theParallel test suites.

`PERCY_PARALLEL_TOTAL``PERCY_PARALLEL_NONCE`[environment variable](https://www.browserstack.com/docs/percy/get-started/set-env-var)[Parallel test suites](https://www.browserstack.com/docs/percy/integrate/parallel-test-suites)You must both export and setPERCY_PARALLEL_NONCEandPERCY_TOKENin the config file.

`PERCY_PARALLEL_NONCE``PERCY_TOKEN`
### Example
If you run tests with2 parallelsacross3 browsers, set:PERCY_PARALLEL_TOTAL=6andPERCY_PARALLEL_NONCE=12345.

`PERCY_PARALLEL_TOTAL=6``PERCY_PARALLEL_NONCE=12345`
#### We're sorry to hear that. Please share your feedback so we can do better
Contact ourSupport teamfor immediate help while we work on improving our docs.

[Support team](https://www.browserstack.com/support)
#### We're continuously improving our docs. We'd love to know what you liked
- This page has exactly what I am looking for
- This content & code samples are accurate and up-to-date
- The content on this page is easy to understand
- Other (please tell us more below)
Thank you for your valuable feedback

- ON THIS PAGE
Is this page helping you?

[Support team](https://www.browserstack.com/support)Thank you for your valuable feedback!

[Talk to an Expert](https://www.browserstack.com/contact?ref=docs-page-floating-contact)Welcome to Percy

New to Percy?

[View
          Documentation](https://www.browserstack.com/docs/percy/get-started-without-code-or-automation-script)Select your framework and language to proceed

- Selenium
- Playwright
- Cypress
[Cypress](https://www.browserstack.com/docs/percy/cypress/get-started)- Puppeteer
[Puppeteer](https://www.browserstack.com/docs/percy/puppeteer/get-started)- Ember
[Ember](https://www.browserstack.com/docs/percy/ember/get-started)- Storybook
[Storybook](https://www.browserstack.com/docs/percy/storybook/get-started)- Gatsby
[Gatsby](https://www.browserstack.com/docs/percy/gatsby/get-started)- Jekyll
[Jekyll](https://www.browserstack.com/docs/percy/jekyll/get-started)- Appium
[Appium](https://www.browserstack.com/docs/percy/appium/get-started)- Tricentis Tosca
[Tricentis Tosca](https://www.browserstack.com/docs/percy/tosca/get-started)- Build your own SDK
[Build your own SDK](https://www.browserstack.com/docs/percy/build-your-own-SDK/get-started)