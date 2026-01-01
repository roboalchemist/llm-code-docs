# Source: https://www.browserstack.com/docs/percy/ember/getting-started

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Run a sample Percy build with Ember
Get hands-on experience on running Percy with Ember using our sample repository

## Prerequisites
Before you start, ensure that you have the following installed:

- Node 18 or later
[Node 18 or later](https://nodejs.dev/en/download/)- Git
[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)Follow these steps to clone the sample web application, run a build, and view the results of the visual comparison:

Clone the sample applicationClone theexample-percy-emberapplication, change the directory, and compile the sample application by running these commands:

`example-percy-ember`You can explore the sample application by opening thesrc/main/resources/index.htmlfile.

`src/main/resources/index.html`Create a Percy projectTo create a project, follow these steps:

- Sign into Percy.
[Sign in](https://percy.io/signup)- In Percy, create a project of the type, Web.
- Name the project.
 After the project is created, Percy generates a token.
- Note down the token.
 You have to use it to set your environment variable in the next step.
For details on creating a project, seeCreate a Percy project.

[Create a Percy project](https://www.browserstack.com/docs/percy/get-started/create-project)Set the project token as an environment variableRun the given command to setPERCY_TOKENas an environment variable:

`PERCY_TOKEN`To learn about environment variables in Percy, seePercy environment variables.

[Percy environment variables](https://www.browserstack.com/docs/percy/get-started/set-env-var)Generate the first buildIn this step, we run the sample test script to take a few snapshots using thepercy.snapshotmethod. The sample application contains an  file in which the method is called. The goal is to have a visual build with which to compare a later build.

[percy.snapshot](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview)`percy.snapshot`On completion, you see logs from Percy confirming that the snapshots were successfully uploaded and a direct URL to the dashboard. There are no visual comparisons yet.

Modify the sample application

Edit theapp/templates/application.hbsfile to introduce some visual changes. In our example, we are adding inline CSS to bold theClear Completedbutton on line 18-20 of the file.

`app/templates/application.hbs`Commit your changes

Commit the changes you made to the sample application by running the following command:

Generate the second buildRun the test script again.

This takes new screenshots of our modified application, uploads them to Percy, and compares them with the previous screenshots to show visual differences.

View results

- Open your project dashboard to view your builds.
- Open the second build to view the visual differences in comparison to the first build.
On the third pane, you see the screenshots from the first build on the left, and from the second, on the right.

Percy highlights what’s changed visually in the application. Use the options on the screen toreview the changes on different browsers and widths.

[review the changes on different browsers and widths.](https://www.browserstack.com/docs/percy/project-settings/cross-browser)
## Congratulations!
You’ve successfully run the sample Percy build.
As you’ve seen, Percy helps you capture visual differences in your application that go undetected with functional testing alone.

This was just a sneak peek. Percy can do a lot more. To make the best out of it, integrate Percy with your test suite. To know more check out the related topics.

## Related topics
- Integrate your test suite with Percy
[Integrate your test suite with Percy](https://www.browserstack.com/docs/percy/integrate/overview)- Choose your base build selection strategy
[Choose your base build selection strategy](https://www.browserstack.com/docs/percy/base-selection/base-build)- View Percy build results
[View Percy build results](https://www.browserstack.com/docs/percy/build-results/approval)
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