# Source: https://www.browserstack.com/docs/percy/build-results/root-cause-analysis

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Root cause analysis
Use the Root cause analysis feature to identify the cause of visual differences in your tests quickly.

The Root cause analysis feature in Percy helps you investigate visual differences effectively. If there are differences associated with a particular snapshot, root cause analysis mode displays only those differences where DOM changes are identified. If you do not see any differences, you can assume that there are no DOM differences associated with the build.

## Explore Root cause analysis
Activate Root cause analysis mode to interactively explore differences within snapshots and click on specific regions to identify their root causes. Normal differences are highlighted in red color, and when this feature is turned on, a purple color bounding box appears around them. Use this feature to streamline your debugging process.

To activate Root cause analysis for a snapshot, follow these steps:

Step 1: Go to your project build review screen and click the Root cause analysis</>icon. The head image (current snapshot) transforms to display the differences interactively, with each difference region becoming clickable for detailed inspection.

Step 2: Click on a specific difference within the snapshot. This information will be displayed on the same review screen underRoot cause analysissection. You can use the Diff navigator (<,>) to navigate through previous and next differences.

The review screen displays different types of differences, see the following section.

## Types of differences
With Root cause analysis, you can view different types of differences, as follows:

- DOM elements
- CSS attributes
- Position related differences
DOM element differences occur when there are changes to the structure or attributes of elements in the DOM. This can include the addition, removal, or modification of tags or attributes.

CSS attribute differences include changes in style properties, such as color, font, padding, margin, border, box shadow, opacity, background, and hover/active states.

Currently, only commonly used CSS attributes are supported.

Position-related differences include changes in an element’s position, size, or alignment, such as variations in width, height, aspect ratio, or spacing between elements. Misalignments within containers can also cause visual discrepancies.

These differences can significantly impact the layout and overall appearance of a page.

## Focus mode
Focusmode helps you concentrate on one visual difference at a time. It highlights a single diff using a purple bounding box along with the red pixels, making it easier to review changes in detail. 
While in focus mode, hover states remain active so you can still navigate between diffs without turning the mode off.

## Visualizing changes between snapshots
- The text color or background indicates the differences between the current and baseline snapshots. Green highlights values added in the current DOM, while red shows values that were removed. Identical values, such as element paths, box dimensions, or CSS rules, are not colored, emphasizing only the changes between the two snapshots.
- When you hover over RCA regions, a tooltip appears showing the class of the end element that has changed or been added. If the element does not have a class, the tooltip displays the tag name.

## Things to keep in mind
- This feature does not capture differences when the DOM structure does not change, even if visual differences exist. This applies to elements like:Carousels: The DOM stays the same while images rotate.iFrames: The outer DOM remains static, even when the content inside an iFrame updates.
- Carousels: The DOM stays the same while images rotate.
- iFrames: The outer DOM remains static, even when the content inside an iFrame updates.
- If there are two types of differences in the head image, general differences and intelli-ignore, these differences appear in different colors in Root cause analysis mode.When intelli-ignore is enabled, ignored differences appear in amber color. Root cause analysis mode shows these differences only if they have an associated DOM and intelli ignore is on.If the same component or element has both a normal and an intelli-ignore difference, everything is shown in red color without differentiation.
- When intelli-ignore is enabled, ignored differences appear in amber color. Root cause analysis mode shows these differences only if they have an associated DOM and intelli ignore is on.
- If the same component or element has both a normal and an intelli-ignore difference, everything is shown in red color without differentiation.
- Currently, if an ignore region is added and there is an actual DOM difference in that area, the difference appears in root cause analysis mode.
- This feature does not work when images are uploaded via Percy Upload, on Figma builds, or on snapshots.

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