# Source: https://www.browserstack.com/docs/percy/figma/configuration

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Configure Figma designs
Learn how to compare Figma designs with Percy for design comparisons and visual testing.

To compare your Figma designs with your Percy build, follow these steps:

- Figma recently enforced stricterAPI rate limits, which reduces the number of designs Percy can fetch. These limits are especially restrictive for accounts with only View access and often cause errors or failed builds.
[API rate limits](https://developers.figma.com/docs/rest-api/rate-limits/)- For critical builds, grant Dev or Full access to our Figma service account (percy.figma@browserstack.com) to avoid rate limits and allow builds to complete.
Step 1: Go to your project build and click theCompare with designsicon.

- For Percy on Automate projects, you must create at least one successful build before creating a Figma build.
Step 2: Make your Figma project public to allow access via a shared link. If the project must remain restricted, grant “edit” access topercy.figma@browserstack.com.

`percy.figma@browserstack.com`If you experience errors due to Figma rate limits, grant “Dev” or “Full” access to our Figma service account.

Wait for Percy to accept the Figma invite. This may take a few minutes. After waiting, check the invite status in Figma. If the invite has not been accepted, it will appear grayed out. Once accepted, it will be displayed in regular text asPercy.

ClickContinue.

Step 3: Enter the Figma link to import your designs. Enter a Percy branch name. You can select an existing branch name from the drop-down or create a new one.

- The default base branch on Percy cannot be selected as the target branch for Figma builds.
- For Percy on Automate projects, Figma retrieves device, browser, and width details from the last successful build on the specified branch. If no baseline build exists, it falls back to the last successful build on the default base branch. If that also doesn’t exist, it uses the most recent successful build.
- You do not require a branch for your Figma designs inside the Figma tool.
- Share the Figma file directly; do not invite to the project.
Step 4: ClickImport designs. Your Figma designs load.

Step 5: Select the desired Figma designs. By default, the system pre-selects the first 50 imported designs.

You can import up to 50 designs per build.

ClickNextto continue.

Step 6: Rename or map your design to a snapshot name for comparison. You can either select an existing snapshot name from the list or provide a new one. Optionally, enable theUse design name as snapshot namecheckbox to automatically map snapshots. If no snapshot name is provided, Percy defaults to using the design name as the snapshot name.

- Percy does not allow multiple designs with the same dimensions to be mapped to the same snapshot.
- Unmapped designs will use the design name as the snapshot name.
Map the test case name to your design. For more information, seeMap test cases.

[Map test cases](https://www.browserstack.com/docs/percy/figma/testcase)Step 7: ClickSave and runto complete the process.

A new build is triggered for the imported Figma designs. By default, the first Figma build is auto-approved. The next time you trigger a build, the review page displays snapshots for comparison.

## Manage Figma design updates
When your Figma designs are updated, you can manually keep your Percy snapshots in sync using the Figma baseline update options when selecting a configured branch:

- Update baseline: Refresh existing imported designs.
- Import new + update baseline: Refresh existing designs and import new designs from your Figma file.

### Things to keep in mind
- The baseline update options are available only when selecting a branch that already has Figma designs configured.
- When frames are removed from your Figma file, Percy removes them from future builds during baseline updates.

## Related topic
- Baseline management for Figma comparison
[Baseline management for Figma comparison](https://www.browserstack.com/docs/percy/figma/baseline-management)- Upload Figma images to Percy via CLI
[Upload Figma images to Percy via CLI](https://www.browserstack.com/docs/percy/references/upload-figma-images)
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