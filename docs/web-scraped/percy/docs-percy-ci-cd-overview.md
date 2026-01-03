# Source: https://www.browserstack.com/docs/percy/ci-cd/overview

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Trigger visual tests from CI/CD
Learn how to integrate Percy with a variety of available CI/CD tools

Percy works best when integrated into your CI workflow, running continuously alongside your test suite. Percy integrates with all common CI providers and can be configured for custom environments.

## Supported CI integrations
You can integrate Percy with the following CI services:

[JenkinsIntegrate Percy with Jenkins.](https://www.browserstack.com/docs/percy/ci-cd/jenkins)Integrate Percy with Jenkins.

[Azure PipelinesIntegrate Percy with Azure Pipelines.](https://www.browserstack.com/docs/percy/ci-cd/azure-pipelines)Integrate Percy with Azure Pipelines.

[Circle CIIntegrate Percy with Circle CI.](https://www.browserstack.com/docs/percy/ci-cd/circleci)Integrate Percy with Circle CI.

[Bitbucket PipelineIntegrate Percy with Bitbucket Pipeline.](https://www.browserstack.com/docs/percy/ci-cd/bitbucket-pipeline)Integrate Percy with Bitbucket Pipeline.

[Travis CIIntegrate Percy with Travis CI.](https://www.browserstack.com/docs/percy/ci-cd/travis-ci)Integrate Percy with Travis CI.

[GitHub ActionsIntegrate Percy with GitHub Actions.](https://www.browserstack.com/docs/percy/ci-cd/github-actions)Integrate Percy with GitHub Actions.

[GitLab CIIntegrate Percy with GitLab CI.](https://www.browserstack.com/docs/percy/ci-cd/gitlab)Integrate Percy with GitLab CI.

[AppVeyorIntegrate Percy with AppVeyor.](https://www.browserstack.com/docs/percy/ci-cd/appveyor)Integrate Percy with AppVeyor.

[Harness CIIntegrate Percy with Harness CI.](https://www.browserstack.com/docs/percy/ci-cd/harness)Integrate Percy with Harness CI.

[SemaphoreIntegrate Percy with Semaphore.](https://www.browserstack.com/docs/percy/ci-cd/semaphore)Integrate Percy with Semaphore.

[BuildkiteIntegrate Percy with Buildkite.](https://www.browserstack.com/docs/percy/ci-cd/buildkite)Integrate Percy with Buildkite.

[CodeShipIntegrate Percy with CodeShip.](https://www.browserstack.com/docs/percy/ci-cd/codeship)Integrate Percy with CodeShip.

[NetlifyIntegrate Percy with Netlify.](https://www.browserstack.com/docs/percy/ci-cd/netlify)Integrate Percy with Netlify.

[OthersIntegrate Percy with Other CI-CD tool.](https://www.browserstack.com/docs/percy/ci-cd/others)Integrate Percy with Other CI-CD tool.

Click each CI service to see step-by-step integration instructions.

ProtipDon’t see your CI service? We’re constantly adding support for CI services. Reach out tosupportto see if yours is on the way.

[support](mailto:support@percy.io)
## How it works
Percy is designed to integrate with your tests and CI environment to run continuous visual reviews. After you add Percy to your tests and your CI environment, Percy starts receiving and rendering screenshots every time a CI build runs.

## Configure CI environment variables
To enable Percy, configure the environment variable, ‘PERCY_TOKEN’, in your CI service. This is our write-only API token unique for each Percy project and should be kept secret.

You can findPERCY_TOKENin your project settings.

`PERCY_TOKEN`
## Start and stop Percy CLI
There are two ways to start and stop Percy CLI from your CI setup:

### Percy execution command
Add thepercy execcommand in your configuration file (for example, make file, package.json, or req.txt) to start Percy, as shown below:

[percy exec](https://www.browserstack.com/docs/percy/take-percy-snapshots/snapshots-via-scripts)In your pipeline script, make changes similar to the following:

### Percy start and stop commands
If you cannot use thepercy execcommandin your configuration file, use thepercy exec:startandpercy exec:stopcommands.

[command](https://www.browserstack.com/docs/percy/take-percy-snapshots/snapshots-via-scripts)In this case, your configuration file looks as follows:

And your pipeline script should be similar to the following:

The above script performs the following actions:

- Install Percy CLI.
- Start Percy CLI with PERCY_TOKEN.
- Run your tests.
- Stop Percy CLI.

## Parallel test suites
Percy automatically supports most parallelized test environments. Snapshots are pushed from your tests to Percy and rendered for you to review in the same Percy build, no matter if your tests are run in different processes or even on different machines. You can also simply configure Percy to support complex parallelization setups.

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