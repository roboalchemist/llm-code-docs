# Source: https://www.browserstack.com/docs/percy/build-results/approval

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Approval workflow
Approve visual differences identified by Percy

Percy approval workflow is an important part of the visual review process. By following this guide, you can understand the different approval types and the request change feature provided by Percy, the concept of auto-approved branches, and how Percy effectively handles the approval workflow.

## Approval types
Percy provides you granular control over the approval process. You can manage approvals in different ways:

- Approve build
- Approve groups of matching visual changes
- Approve individual snapshots
- You can only approve snapshots, and not individual screenshots. This means that you can approve snapshots, which has screenshots captured across all browsers and width combination. However, it is not possible to approve individual screenshots taken on a specific browser for a specific width.
You canrequest changesif a snapshot is not yet ready for approval. By doing this, the build status will be changed to “Changes requested.”

[request changes](https://www.browserstack.com/docs/percy/build-results/change-request)Note:Once all snapshots in a build are approved, the whole build will be approved. If you have a source code integration installed, only marking a complete build as approved will mark your Percy check as “passed.”

## How approvals are carried forward
Approved snapshots that were previously accepted will retain their approval status across builds throughout the lifespan of the branch. Essentially, identical snapshots will only require approval once per branch, as they are “carried forward.” For further information, refer tobase build selectionlogic.

[base build selection](https://www.browserstack.com/docs/percy/base-selection/base-build)Note: This is only applicable for multi-branch or Git style workflow. If you are working on approval required branches workflow, you can refer to ourBase snapshots selection.

[Base snapshots selection](https://www.browserstack.com/docs/percy/base-selection/base-snapshot)
## An example

### Scenario 1: Snapshot exists in the main branch
Percy always compares first with the main branch, if there are differences, then it will check if the same differences were approved in the immediate previous build in same branch.

- Let’s consider a scenario in which you have a snapshot A in the main branch. The snapshot has a button which is blue in color.
- Create a feature branch (F1) from the main branch.
- Create Build 1 in F1. In this build, the color of button in snapshot A is changed from blue to green. In this case the build gets compared with the base build in the main branch and you approve the changes in Build.Pre state - 1 Changed, 1 Unreviewed, and 0: Approved.Post state - 1 Changed, 0 Unreviewed, and 1: Approved.
- Pre state - 1 Changed, 1 Unreviewed, and 0: Approved.
- Post state - 1 Changed, 0 Unreviewed, and 1: Approved.
- Next, create another build Build 2, in F1 . The snapshot in Build 2 remains exactly the same as the one in Build 1. In this case, the approval from Build 1 is carried forward to Build 2.Pre state - 1 Changed, 0 Unreviewed, and 1: Approved.Post state - 1 Changed, 0 Unreviewed, and 1: Approved.
- Pre state - 1 Changed, 0 Unreviewed, and 1: Approved.
- Now, let’s say you create another build, Build 3 in which the button color changes from green to red. This snapshot has a change that is not approved in Build 2 in F1 and in the base build in the main branch. In this case, the approval is not carried forward.
- Now, a user requests changes in Build 3 to change the color red.Pre state - 1 Changed, 1 Unreviewed, and 0: Approved.Post state - 1 Changed, 1 Changed Requested, and 1: Approved.
- Post state - 1 Changed, 1 Changed Requested, and 1: Approved.
- In the next build Build 4, the user changes the color from red to green, so the new Build 4 is submitted for review again. In this case also, the approval is not carried forward.Pre state - 1 Changed, 1 Unreviewed, and 0: Approved.Post state - 1 Changed, 0 Changed Requested, and 1: Approved.
- Post state - 1 Changed, 0 Changed Requested, and 1: Approved.

### Scenario 2: Snapshot does not exist in the main branch
- Let’s consider a snapshot B which is not present in the base build in the main branch, you create a new feature branch (F2) and add a new feature on this branch in Build 1.
- This snapshot will be identified as a new snapshot in Build 1 and it will never be compared with main branch as the snapshot does not exist in the main branch.
- This new snapshot has a green color button and you have approved this snapshot.Pre state - 1 Changed, 1 Unreviewed, and 0: Approved.Post state - 1 Changed, 0 Unreviewed, and 1: Approved.
- You create another build in the feature branch Build 2. The snapshot in Build 2 remains exactly the same as the one in Build 1. In this case, the approval from Build 1 is carried forward to Build 2.Pre state - 1 Changed, 0 Unreviewed, and 1: Approved.Post state - 1 Changed, 0 Unreviewed, and 1: Approved.
- Now, let’s say you create another build, Build 3 in which the button color changes from green to red. This snapshot has a change that is not approved in Build 2 in F2. In this case, the approval is not carried forward.
- Now, a user requests changes in Build 3 to change the color.Pre state - 1 Changed, 1 Unreviewed, and 0: Approved.Post state - 1 Changed, 1 Changed Requested, and 1: Approved.

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