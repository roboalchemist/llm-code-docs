# Source: https://www.browserstack.com/docs/percy/integrate/percy-sdk-workflow

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Percy SDK and screenshot capture workflow
This guide explains how the Percy infrastructure works with SDKs

To debug Percy builds, a comprehensive understanding of Percy’s workflow, spanning from SDKs to screenshot capture, is essential. This document explains the operations of both the SDKs and the Percy infrastructure.

At a high level, Percy works by capturing a snapshot of the DOM within the test browser. Subsequently, the DOM is transmitted to Percy’s API to be concurrently rendered across various browsers and widths for screenshots. The SDKs are responsible for capturing the DOM and assets, while the APIs handle the proxying and rendering of these snapshots in browsers for screenshots. It is important to note that screenshots are not captured within your test suite but within Percy’s infrastructure.

## How SDKs work
There are two major steps in the Percy SDK to know about:

- Capturing the DOM state
- Asset discovery
WhenpercySnapshotis called, Percy’s SDKs capture the exact state of the DOM. The SDK serializes the current page state into the DOM by applying form element values, capturing CSSOM, including accessible iframes, and converting canvas elements into images. This process is handled by the@percy/dompackage. We serialize these elements because their state is stored in the page’s memory and is not encoded into the DOM. Without this serialization, that content would be missing from the snapshot.

`percySnapshot`[@percy/dom](https://github.com/percy/cli/tree/master/packages/dom)- Firefox/Chromiumare the supported test browsers for capturing the DOM state.
`Firefox/Chromium`- Shadow DOM capturing is currently supported only in the Chrome browser. This feature is unavailable on Firefox due to a lack of serialization support.

### Input elements
Input elements (input, textarea, select) are serialized by setting respective DOM attributes to their matching JavaScript property counterparts. For example, checked, selected, and value.

### Frame elements
Frame elements are serialized when they are CORS accessible and if they haven’t been built by JavaScript when JavaScript is enabled. They are serialized by recursively serializing the iframe’s document element with the@percy/domlibrary.

`@percy/dom`
### CSSOM rules
When JavaScript is not enabled, CSSOM rules are serialized by iterating over and appending each rule to a new stylesheet inserted into the document’s head.

### Canvas elements
Canvas elements drawing buffers are serialized as data URIs and the canvas elements are replaced with image elements. The image elements reference the serialized data URI and have the same HTML attributes as their respective canvas elements. The image elements also have a max-width of 100% to accommodate responsive layouts in situations where canvases may be expected to resize with JS.

### Video elements
Videos without a poster attribute undergo automatic serialization of the current frame, and the resulting image is set as theposterattribute. This ensures that videos consistently display a stable image when screenshots are captured.

`poster`Once the DOM is captured & serialized, it gets sent to@percy/corefor asset discovery. Asset discovery renders the captured DOM in a Chromium browser, where the SDK intercepts all network requests the DOM makes. This captures assets needed to render the page in Percy’s infrastructure for a screenshot. By default, all assets served on the same hostname as the tests are captured. You can capture more hostnames with theallowed-hostnamesconfig key. Asset discovery also resizes the viewport to the passed widths to ensure assets are captured for the right screen sizes.

`@percy/core`[allowed-hostnames](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview#all-configuration-options)`allowed-hostnames`Asset discovery by default will wait100msfor no new network requests to be made by the captured DOM. Once that timeout has been reached asset discovery will close for the given snapshot. It’s not uncommon to have to increase thenetwork-idle-timeoutto allow for more network requests to be made.

`100ms`[network-idle-timeout](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview#all-configuration-options)`network-idle-timeout`Since Percy re-renders the DOM in a browser outside of your test suite, you may need to provide authentication to the requests this browser is making. Thediscoveryconfiguration key in Percy’s SDKs  provides a few ways to authenticate requests like request-headers, authorization, and cookies.

[discovery](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview#all-configuration-options)`discovery`NOTEChromiumis supported browser for Asset discovery, we manage its ourselves in@percy/corepackage, you couldskip the asset discovery browser downloadby providing your own.

`Chromium``@percy/core`[skip the asset discovery browser download](https://docs.percy.io/docs/skipping-asset-discovery-browser-download)
## How the infrastructure works
With the DOM captured and the right assets gathered to render the page, it’s time to capture the screenshot. Percy re-renders the page concurrently across browsers/widths for screenshots.

By default, Percy renders all snapshots with JavaScript disabled. This choice stems from the fact that JavaScript has already executed and modified the page before the DOM is captured. Although enabling JavaScript in Percy’s infrastructure is possible, it often leads to unexpected issues. Most web pages are not designed to handle rendering with an already fully formed DOM, potentially resulting in issues such as redirects or the loss of serialized states (clearing inputs, etc.).

When the page is re-rendered, Percy modifies the captured DOM slightly to do things like remove<noscript>tags and freeze CSS animations.

`<noscript>`NOTEFor a list of Browsers we support in Infrastructure, seeCross-browser visual testing.

[Cross-browser visual testing](https://www.browserstack.com/docs/percy/project-settings/cross-browser)If you suspect an infrastructure issue, checkPercy Common - FAQspage. Otherwise,feel free to contact our support team.

[Percy Common - FAQs](https://www.browserstack.com/docs/percy/troubleshoot/percy-common-faqs)[feel free to contact our support team](https://www.browserstack.com/contact#technical-support)
## Debugging SDK’s
All Percy SDKs use@percy/cli, ensuring a consistent approach to debugging snapshot issues across all SDKs.

`@percy/cli`
### Debug vs verbose logging
If you are certain you are debugging an asset issue, avoid consuming Percy screenshots during the troubleshooting process. Utilize the--debugCLI flag, which performs all SDK functionsexceptcreating build and uploading snapshots. This includes capturing the DOM, running asset discovery over the captured DOM, and enabling verbose logs.

`--debug`If you still like to create a Percy build, utilize the--verboseCLI flag. This enables verbose logs and simultaneously uploads the captured snapshots to Percy’s API.

`--verbose`Understanding SDK debugging often requires reading the detailed verbose logs provided by the SDKs. Percy’s logs are labeled to specify the originating package for clarity.

For example[percy:core]means the log is coming from the@percy/corepackage. This helps figure out if the log is from the client SDK or one of the packages that constitute@percy/cli.

`[percy:core]``@percy/core``@percy/cli`
### Display the asset discovery browser
At times, it’s more straightforward to understand the process by observing the asset discovery browser rendered on your captured page. Achieve this by configuringheadless: falsein thediscovery.launch-options.

`headless: false``discovery.launch-options`
## Related topics
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