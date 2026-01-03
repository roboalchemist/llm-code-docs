# Source: https://www.browserstack.com/docs/percy/common-issue/common-errors/browser-spawn-failure

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Error - Browser spawn failure
Learn how to fix errors related to browser spawn failures in Percy

Spawn failures usually occur on node when it is unable to spawn a child process. This can be due to permissions or environment issues in which the node process is running.

Try these solutions to resolve this error:

Solution 1:

Spawn failures can occur if you run multiple CLI instances on the same machine simultaneously. We recommend using a single Percy CLI on a machine. For more information, seeParallel tests on same machine.

[Parallel tests on same machine](https://www.browserstack.com/docs/percy/integrate/parallel-test-suites#parallel-tests-on-the-same-machine)To fix errors related to the port being in use already by killing the process, seekill the Percy process.

[kill the Percy process](https://www.browserstack.com/docs/percy/common-issue/common-errors/percy-port-in-use)Solution 2:

- For Mac, try installing Rosetta using the following command:

```
softwareupdate --install-rosetta

```

`softwareupdate --install-rosetta`- For WindowsDisable any antivirus software you have installed and check if the error persists. If the error is resolved, it indicates that your antivirus is blocking Percy from spawning a new browser instance. In this case, modify your antivirus settings to allow Percy to spawn a browser.
- Disable any antivirus software you have installed and check if the error persists. If the error is resolved, it indicates that your antivirus is blocking Percy from spawning a new browser instance. In this case, modify your antivirus settings to allow Percy to spawn a browser.
Need more support?Contact BrowserStack.

[Contact BrowserStack](https://www.browserstack.com/contact?ref=docs)
## Reference Topic
- Percy Common error messages
[Percy Common error messages](https://www.browserstack.com/docs/percy/troubleshoot/percy-common-faqs#common-error-messages)
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