# Source: https://www.browserstack.com/docs/percy/common-issue/proxy-requests

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Configuring Proxy Requests
The role and benefits of proxying requests during the visual testing process.

#### To Percy’s API
Percy’s SDKs implement the industry convention for proxying requests viaHTTP_PROXY,HTTPS_PROXY, andNO_PROXYenvironment variables.

`HTTP_PROXY``HTTPS_PROXY``NO_PROXY`
```
# unix example, set the env variable the way your OS/System expects
$ export HTTP_PROXY=http://a-proxy.example.com:1234
$ export HTTPS_PROXY=https://another-proxy.example.com:1234
# general syntax for setting proxy
$ export HTTPS_PROXY=https://username:password@proxyurl:proxyport
$ export NO_PROXY=http://example.com:1234

```

```
# windows example, set the env variable the way your OS/System expects
> $Env::HTTP_PROXY = 'http://a-proxy.example.com:1234'
> $Env::HTTPS_PROXY = 'https://another-proxy.example.com:1234'
# general syntax for setting proxy
> $Env::HTTPS_PROXY = 'https://username:password@proxyurl:proxyport'
> $Env::NO_PROXY = 'http://example.com:1234'

```

```
# windows example, set the env variable the way your OS/System expects
$ set HTTP_PROXY=http://a-proxy.example.com:1234
$ set HTTPS_PROXY=https://another-proxy.example.com:1234
# general syntax for setting proxy
$ set HTTPS_PROXY=https://username:password@proxyurl:proxyport
$ set NO_PROXY=http://example.com:1234

```

By default, the values are set to empty.

#### Asset discovery
If you need to proxy requests that occur in asset discovery, you may need to pass a--proxy-serverCLI flag as a browser launch argument in the Percydiscoveryconfiguration.

`--proxy-server``discovery`Need more support?Contact BrowserStack.

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