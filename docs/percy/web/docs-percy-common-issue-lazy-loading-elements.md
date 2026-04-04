# Source: https://www.browserstack.com/docs/percy/common-issue/lazy-loading-elements

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Capturing lazy-loaded elements in Percy snapshots
Learn how to use beforeSnapshot option to scroll and capture lazy-loaded elements.

Lazy-loaded elements (for example: a footer logo) are not captured in Percy snapshots when using thesnapshotcommand without a test browser. This happens because the asset-discovery browser doesn’t scroll, so elements outside the initial viewport are not requested or loaded. WhilewaitForSelectorandwindow.scrollTowork in test or renderer browsers, they don’t affect the asset-discovery browser.

`snapshot``waitForSelector``window.scrollTo`To address this, use thebeforeSnapshotoption in yoursnapshots.ymlfile to scroll the page in the asset-discovery browser before the snapshot is taken. This ensures that lazy-loaded elements enter the viewport and get captured correctly.

`beforeSnapshot``snapshots.yml`This scrolls to the bottom of the page before Percy captures the snapshot, allowing lazy-loaded elements like footer logos to load and appear correctly.

Need more support?Contact BrowserStack.

[Contact BrowserStack](https://www.browserstack.com/contact?ref=docs)
## Reference Topic
- Percy Common - FAQs
[Percy Common - FAQs](https://www.browserstack.com/docs/percy/troubleshoot/percy-common-faqs)
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