# Source: https://www.browserstack.com/docs/percy/build-results/visual-testing

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Visual Testing on mobile browsers
Learn all about visual testing on mobile Browsers

Percy is an all-in-one visual testing and review platform that allows you to run visual tests using either the BrowserStack SDK or the Percy SDK. Cross-browser visual testing is available for all Percy customers to effortlessly see visual changes across different mobile browsers. You can manage browsers through either Automate or Percy. For more information, seeCreate a project.

[Create a project](https://www.browserstack.com/docs/percy/get-started/create-project)Based on your browser selection management, refer to the appropriate section:

Percy runs visual tests for all major mobile browsers specified in your BrowserStack configuration file. Set the browser version by integrating your test with theBrowserStack SDK with Automate. Use theAutomate capability builderto configure various mobile browser names and versions.

[BrowserStack SDK with Automate](https://www.browserstack.com/docs/percy/integrate/percy-with-browserstack-sdk)[Automate capability builder](https://www.browserstack.com/docs/automate/capabilities)In your BrowserStack configuration file, include the following mobile browser details under theplatformattribute:

`platform`- os name
- osVersion
- browserName
- browserVersion
All specified browsers appear under theDevice & Browsersdrop-down. Select a device, and the build displays separate screenshots for that device and browser, highlighting the visual differences specific to each.

## Important changes for mobile browsers
Behavior differences to note when running Percy tests on mobile browsers.

### Screenshot width
The width parameter passed while running Percy tests will be ignored for mobile browsers as Percy uses real mobile devices and the screenshot width is fixed for these. Please note that the behavior on desktop browsers remains unchanged.

### Portrait mode
All screenshots on mobile browsers will be taken in portrait mode by default. Please refer to these pages to read more about changes in mobile browsers’ behavior:

- Text stability in iOS
[Text stability in iOS](https://www.browserstack.com/docs/percy/troubleshoot/text-stability)- Autoplay videos here
[Autoplay videos here](https://www.browserstack.com/docs/percy/stabilize-screenshots/videos#handling-videos-on-mobile-browsers)Currently, Percy supports the following combinations for mobile browsers:

- Safari with iOS
- Chrome with Android (Beta)
We’ll soon add more combinations to this list.Contact usif you’re looking for something specific.

[Contact us](https://www.browserstack.com/contact)
## How to access mobile browsers
To access mobile browsers, you will have to upgrade to thePercy Desktop & Mobileplan. If you do not have access to the mobile plan:

[Percy Desktop & Mobile](https://www.browserstack.com/pricing?product=percy)- Reach out to your Percy account owner and ask them to upgrade.
- If you don’t know the account owner, fill outthisform and we will reach out to your account owner.
[this](https://www.browserstack.com/contact?ref=footer#sales)- Alternatively, you can request a free trial of the mobile plan using thesame form.
[same form](https://www.browserstack.com/contact#sales)If you already have a Percy Desktop & Mobile plan, you can turn mobile browsers on or off using either of the following options:

- Browser Settings Page: Use this page to view and change the browser coverage for all your Percy projects.
[Browser Settings Page](https://percy.io/dashboard/browsers)- Project settings: You can also use the project settings page to toggle browsers on/off
While reviewing diffs, Percy will show separate screenshots for each browser, highlighting the visual diffs specific to each.

## Differences between desktop and mobile plans
All features in Desktop and Desktop & Mobile plans are same, except the support for mobile browsers. Please visit thepricingpage for a detailed comparison between the desktop and mobile plans.

[pricing](https://www.browserstack.com/pricing?product=percy)[Text stability in iOS](https://www.browserstack.com/docs/percy/troubleshoot/text-stability)[Autoplay videos here](https://www.browserstack.com/docs/percy/stabilize-screenshots/videos#handling-videos-on-mobile-browsers)
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