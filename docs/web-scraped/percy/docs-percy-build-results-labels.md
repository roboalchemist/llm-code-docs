# Source: https://www.browserstack.com/docs/percy/build-results/labels

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Create labels/tags
Learn how to use labels/tags to organize projects, builds, and snapshots.

Labels/Tags are essential for categorizing and organizing projects, builds and snapshots. They improve the ability to filter and search for specific builds and snapshots, enhancing overall project management. By using labels/tags, teams streamline workflows, facilitate better tracking and management, and enhance collaboration, ensuring everyone stays on the same page.

Minimum required @percy/cli version is 1.28.8.

## Create project labels/tags
You can create project labels/tags while setting up a Percy project. Navigate toCreate Project, select the type of project, enter the name and add your own label/tags or choose from the available options.

Once the build is generated, you will see the added labels/tags in your build on theProjectspage.

## Create builds with labels/tags
You can create new builds with labels/tags using the--labelsoption in Percy CLI commands. Add multiple labels/tags by separating them with commas. To include spaces in labels/tags, use double quotes.

`--labels`
### Example CLI command:

### Example with multi-word labels/tags:

### Defining labels/tags in Percy configuration file
Labels/Tags can also be defined in the Percy configuration file (percy.yml) under the percy key using thelabelskey.

`labels`Example percy.yml file:

## Associating snapshots with labels/tags
You can associate snapshots with labels/tags by utilizing thepercySnapshotorpercyScreenshotfunctions and including the labels/tags as a key in the options parameter.

`percySnapshot``percyScreenshot`Use thepercySnapshotmethod for Percy Web projects and thepercyScreenshotmethod for Percy on Automate projects.

`percySnapshot``percyScreenshot`Example:

This enables you to effectively manage and filter your snapshots and builds using labels/tags, improving organization and workflow efficiency.

## Search using labels/tags
TheProjectsandBuildspages now include a newly introduced search text box that enables you to search using labels/tags. Additionally, you can search snapshots using labels and names for individual snapshots on the review page by clicking thesearchicon.

- Clicking the search text box will automatically populate a dropdown menu with all valid labels/tags used across the organization, including those in projects, builds, and snapshots.
- You can select one or more labels/tags and optionally add a search term to search within the project, build or snapshot name on those pages.

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