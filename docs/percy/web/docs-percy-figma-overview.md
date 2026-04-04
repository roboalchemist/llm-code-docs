# Source: https://www.browserstack.com/docs/percy/figma/overview

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Figma designs comparison
Use Percy with Figma designs for visual comparison.

Percy’s support to configure Figma designs enables you to validate designs and detect visual discrepancies. It streamlines your design-to-development process by providing:

- Real-time screenshot comparisons for pixel-perfect accuracy.
- One-click setup to link Figma to Percy.
- Preview and interactive modes for design comparison.
- Collaborate with stakeholders and request changes and approvals.
New to Percy? Get started by creating a Percy project. For more information, seeCreate a Project. Once your project is created & build is triggered you are ready to perform visual testing with Percy.

[Create a Project](https://www.browserstack.com/docs/percy/get-started/create-project)
## High-level steps
- Upload Figma design file link.
- Map the snapshots with the required build snapshots.
- Compare designs and validate visual differences.
- For Percy on Automate projects, you must create at least one successful build before creating a Figma build.
- For Percy on Automate projects, resizing uses the baseline snapshot’s width from your Automate session. The height is taken from the Figma design to support full-page screenshots.
- The allowed width for the snapshots is between 120px and 2000px (inclusive).
- For Percy Web projects, ensure the snapshot width matches the design. For more information, seeset the snapshot width using the CLI.
[set the snapshot width using the CLI](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview#configuration-file)- Designs of the following node types are excluded:
[CANVAS, SECTION, COMPONENT_SET, RECTANGLE, VECTOR, GROUP, DOCUMENT, TEXT, LINE].
- If excluded nodes have nested designs, Percy attempts to retrieve relevant children, tracing up to 3 levels deep.

## Explore further
- Configure Figma designs
[Configure Figma designs](https://www.browserstack.com/docs/percy/figma/configuration)- Baseline management for Figma comparison
[Baseline management for Figma comparison](https://www.browserstack.com/docs/percy/figma/baseline-management)
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