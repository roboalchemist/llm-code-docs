# Source: https://www.browserstack.com/docs/percy/build-results/build-lifecycle

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Build lifecycle
Explore the actions you can perform on builds and snapshots.

This page explains the actions you can perform on builds and snapshots, including creating, reviewing, approving, or discarding changes, enabling you to effectively manage builds and streamline your visual testing workflow.

## Build actions
You can perform the following actions on an approved build if the build is approved and at least one snapshot is marked as approved.

- Unapprove build– Revert the approval status of the build. This option is available when at least one snapshot is approved.
- Reject build– Mark the build as rejected to prevent it from becoming the base build for future builds.
- Delete build– Permanently remove the build and its associated snapshots.

## Snapshot actions
You can approve and unapprove snapshots:

- Approve snapshot– Confirm the changes in the snapshot.
- Unapprove snapshot– Revert the approval, marking the snapshot as unreviewed.
Unapproving the build automatically unapproves all the snapshots within that build.

For detailed information about the approval process, including how to review, approve, and manage snapshots, visit thePercy Approval workflow page.

[Percy Approval workflow page](https://www.browserstack.com/docs/percy/build-results/approval)
### Additional actions for Visual Git
For Visual Git, you have the following additional options:

- Merge: Merge the changes from the current build into the baseline.
- Unmerge– Undo the merge action, setting the previous merged build as the baseline.
- Unmerge and unapprove build– Unmerge the build and change its status to unapproved.
- Unmerge snapshot– Undo the merge action, setting the previous merged snapshot as the baseline.
- Unmerging sets the previously merged snapshot as the baseline.
- If you approve the build and want to unapprove a snapshot, a confirmation modal appears.
For detailed information on managing baselines and performing actions with Git and Visual Git, refer to the following pages:

- Git baseline management
[Git baseline management](https://www.browserstack.com/docs/percy/baseline-management/git)- Visual Git Baseline Management
[Visual Git Baseline Management](https://www.browserstack.com/docs/percy/baseline-management/visual-git)
## Build receiving State
You can perform the following actions when receiving a build:

- Finalize to review– Mark the build as ready for review, making snapshots available for approval.
- Fail build– Mark the build as failed, indicating that it did not pass the required checks.

## History panel
Click the history icon to view the snapshot history. You can filter snapshots by date and the following states:

- All– Display all snapshots within the build.
- Approved– Show snapshots that you approved.
- Merged– Display snapshots that you merged into the baseline.
- Unreviewed– List snapshots awaiting approval.
- Changes requested– Show snapshots with requested changes.
- Failed– Display snapshots that failed checks.
- Auto-approved– Show snapshots automatically approved based on predefined rules.
- Rejected– Display snapshots you marked as rejected.
In summary, managing your builds and snapshots helps you maintain accurate visual test baselines. Use the available actions and explore Git and Visual Git features to streamline your workflow.

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