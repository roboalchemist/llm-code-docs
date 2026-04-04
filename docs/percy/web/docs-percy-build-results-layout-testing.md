# Source: https://www.browserstack.com/docs/percy/build-results/layout-testing

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Layout testing
Learn how layout testing works in Percy

Layout testing is a process to check the arrangement and positioning of UI elements to confirm they match the expected design or layout guidelines. It helps identify issues such as misaligned elements, incorrect spacing, or any discrepancies in the visual presentation. This is particularly effective for cross-environment testing providing a reliable validation of page structure.

Percy’s layout testing focuses on validating the structure of page layout. It identifies page elements from baseline such as text, images, buttons, divs and columns, ensuring their relative positions remain consistent. The visual comparison is executed by providing a meticulous examination of layout changes without verifying content alterations.

It’s a powerful tool for cross-environment testing, providing reassurance that the page structure remains intact across different operating systems, browsers, and devices.

- Currently, the Layout testing feature currently works only with Percy SDK and@percy/cliversion 1.27.4 and higher.
`@percy/cli`- Use thepercySnapshotmethod for Percy Web projects and thepercyScreenshotmethod for Percy on Automate projects.
`percySnapshot``percyScreenshot`
### To enable layout testing in Percy, follow these steps:
Set up Percy and have builds running actively using thepercySnapshotcommand.

[percySnapshot](https://www.browserstack.com/docs/percy/take-percy-snapshots/snapshots-via-scripts)Enable layout testing while capturing the screenshots.

Run and review buildsOnce the build is completed, go to the Percy dashboard and locate the layout icon on snapshot thumbnails to recognize the snapshots that underwent layout diffing process.

## Things to keep in mind
- Base snapshots must exist, and any base snapshots dated before November 1, 2023, will not be considered. In such scenarios, we will have standard Percy behaviour.
- Layout testing will not function with commands such asnpx percy snapshotor if utilized within a configuration file (e.g. ‘xyz.yml’ file).
`npx percy snapshot`- iframes with the same domain or subdomain which is accessible JavaScript will be considered along with its content.
- iframes from different domains are verified for their existence, not their content.
- The difference in text layout wouldn’t be emphasized if the text is present but remains unseen due to its color blending into the background.
- Only differences are highlighted within the head image (or the image currently compared to the base/image on the right side of the review screen). For example, if a specific region is removed from the base image, the difference will only be highlighted within the head image.

## Limitations
- Only works forpercySnapshotcommand.
`percySnapshot`- If you have set “enableJS” to true while testing dynamic websites to capture dynamic animations, images, etc., it may cause inconsistent layout testing in such scenarios.
- Snapshots throughpercy uploadwill not work for layout testing.
`percy upload`- Pop-ups differences may not be accurate.
- Shadow DOM elements are not supported.

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