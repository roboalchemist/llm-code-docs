# Source: https://www.browserstack.com/docs/percy/figma/baseline-management

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Baseline management for Figma comparison
Learn how the baseline management works for Figma design comparisons and visual testing.

Baseline management for Figma ensures consistent visual testing across different builds. By defining a stable baseline, you can track changes in your Figma designs and their impact on the visual quality. The baseline is typically established from a previous snapshot and serves as the reference for future comparisons.

This page explains how baseline management works for Figma builds in the context of Git and Visual Git workflows.

## Git workflow
- Builds B1 and B2 are created from the Master Build.
- Build B3 consists of four snapshots, a, b, c, and d.
- Build B4 builds upon B3 and includes six snapshots, a, b, c, d, e, and f.
- Build B5 is a feature build from B3 and has three snapshots, a, b, and c.
- Build B6 is a Figma build that has five snapshots, a, d, x, y, and z.
- For Build B7, snapshots include a, b, c, and d. Snapshot ‘a’ and ‘d’ use B6 (the Figma build) as their baseline, while snapshots ‘b’ and ‘c’ use the last approved build as their baseline.

## Visual Git workflow
- Buildes B1 and B2 are created from the Master Build.
- Build B7 has four snapshots, a, b, c, and d. Snapshots ‘a’ and ‘d’ use Build B6, the Figma build, as their baseline, while snapshots ‘b’ and ‘c’ use the last approved build as their baseline.
- Build B8 continues from Build B7 and inherits its baseline. Build B8 contains one snapshot, ‘a’.
- Build B9 has three snapshots, a, c, and d. Snapshot ‘a’ uses Build B8 as the baseline, while snapshots ‘c’ and ‘d’ use the last approved snapshots for ‘c’ and ‘d’ as their baseline.

## Related topic
- Git
[Git](https://www.browserstack.com/docs/percy/baseline-management/git)- Visual Git
[Visual Git](https://www.browserstack.com/docs/percy/baseline-management/visual-git)
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