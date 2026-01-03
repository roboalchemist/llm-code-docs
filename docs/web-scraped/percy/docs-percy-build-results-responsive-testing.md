# Source: https://www.browserstack.com/docs/percy/build-results/responsive-testing

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Responsive Visual Testing
Learn how responsive visual testing works in Percy

A powerful feature of Percy is visual testing for responsive user interfaces, allowing you to automatically detect visual regressions on mobile, tablet, and desktop screens at once.

You provide a list of responsive breakpoint widths and we take care of the rest.

## How it works
Because Percy stores the original DOM snapshot and page assets, we simply render the same page at different widths by resizing the browser when generating page screenshots. This is handled entirely server-side and has no effect on the speed of your tests since all rendering and diffing takes place in Percy.

### Configuring responsive snapshots
Configuring Percy for responsive visual testing is as easy as specifying your desired responsive breakpoint widths when you call Percy snapshots.

NOTE:
Check the documentation forthe specific SDK you’re usingto learn how to add responsive widths to your snapshot calls.

[the specific SDK you’re using](https://www.browserstack.com/docs/percy/integrate/overview)
### Usage
Each responsive width counts as a separate screenshot that counts towards your monthly screenshot usage. For example, a snapshot of your homepage at 375px and 1280px will count as 2 screenshots.

## Reference topic
- Browser compatibility and maximum page dimensions with Percy
[Browser compatibility and maximum page dimensions with Percy](https://www.browserstack.com/docs/percy/common-issue/browser-compatibility)
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