# Source: https://www.browserstack.com/docs/percy/baseline-management/git

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Git
Git baseline management strategy for your visual test workflow.

The Git strategy works like Git-based branching comparisons when code changes in a branch are merged with the main or production branch. In this case, Percy relies on Git commit information to find the right base build.

The base build for a particular build in Git-based branching comparisons in Percy is the build forked from that branch.

The following diagram shows how the base build is selected with this strategy:

Git Strategy Example:

Developers handle releases using a full CI/CD setup.

Developer A works on a new feature in a dedicated branch. They create 10 builds during development and compare changes against the current production version using theGitstrategy. Once development is finished, they initiate a PR to merge into the main branch. CI/CD conducts functional and visual checks. If successful, changes deploy to production.

## How are the base builds selected with Git?
The following describes how your base builds are selected with the Git strategy:

When you push changes to your codebase and have Percy generate screenshots, Percy groups the screenshots in snapshots, and snapshots into a build. New screenshots are compared to baseline screenshots from a previous build. This previous build is also known as the base build.

Percy uses a variety of strategies to determine the optimal base build for comparison on every build you create. The particular strategy used depends on several factors, including any installedSCM integrations, the default branch of the project, and which commits have previously finished builds.

[SCM integrations](https://www.browserstack.com/docs/percy/ci-cd/overview)Percy takes a lot of care in automatically selecting the best base build to give you clean, accurate diffs. The chart below demonstrates a simplified view of Percy’s base build selection logic. Click the thumbnail below to view the full-size diagram.

(a) Is the build attached to a pull request?(c) Is there a merge base commit present, and a Percy build for the merge base commit?If your project has an active source control management integration, like GitHub or GitLab, then Percy will always try to compare builds created in conjunction with pull (or merge) requests to the base branch for the pull request. This ensures that only the changes relevant to the pull request are visible in the Percy diff. If there have been changes on the base branch (e.g.,master) since the pull request was opened, the visual diff will not reflect those changes.

`master`(b) Has Percy attempted to find a build on the “master” branch?(d) Is there any previous Percy build on this branch?Percy’s fallback behavior, when no merge base commit build is present, is to compare a build to the latest build on the default base branch. This is the “master” branch by default, but you can override it when creating new builds (see “Overriding the default base branch”). If there are no builds present on the default base branch, then Percy will fall back to using any previous build on the same branch as the build’s commit.

(e) Has Percy tried every branch strategy?If Percy has exhausted all the prior options and has not found a viable candidate for the base build, then no base build will be chosen, and all snapshots will be treated as new. This generally only happens on the first build for a new project, but can also occur when the default base branch is misconfigured (see “Overriding the default base branch” above).

### The common cases
In almost all cases, Percy’s defaults ‘just work,’ but if you are looking to select only the ‘latest approved build/snapshot’ as the base build for comparisons, then utilize theApproval Required Branchesfeature from project settings, which is designed to work for the use cases where builds are getting created from a single branch.

This section explains the three common types of Percy builds, and the common base build selection for them. The description below assumes you’re using Percy from a CI service we support and have our source code repository integration in place.

#### Pull request builds
The most common use case for Percy is visual reviews associated with pull requests. To select the base build, Percy will first determine the target branch of the pull request (often master). It will then determine the common ancestor commit (the merge base) between the source branch and target branch. Once it has that target branch and common ancestor commit, it will choose the Percy build associated with them as the base build.

This provides you with the best visual review, showing only the changes introduced by this pull request, avoiding any other changes that may have occurred on the target branch in the interim.

#### Feature branch builds
Feature branch builds are similar to pull request builds, with the exception that they don’t have a pull request specifying the target branch. In this case, the ‘master’ branch is picked as the target branch. The target commit and the base build are subsequently determined in the same way as the pull request builds described above.

If you typically merge into a ‘development’ branch rather than the ‘master’ branch, you may want to setPERCY_TARGET_BRANCHto ‘development’ in your environment variables, to specify development as the default base branch.

`PERCY_TARGET_BRANCH`
#### Master branch builds
Percy uses the most recent finished build on the master branch as the base build for new master branch builds.

We encourage you to run Percy builds for every commit on the master branch, as these provide the baseline builds for the pull request and feature builds described above.

## Approval workflow
During project creation, selecting the baseline management strategy is essential for identifying the appropriate base snapshot for comparison. After completing this step, it is necessary to familiarize yourself with Percy’s approval workflow options.

The Percy approval workflow is integral to the visual review process. Understand the different approval types and the complexities of how base build selection collaborates with various approval workflow options. A solid understanding of these interrelated processes is essential for effectively overseeing your projects and builds.

You cannot undo a snapshot approval. For more information, seeApproval workflow.

[Approval workflow](https://www.browserstack.com/docs/percy/build-results/approval)
### Default base branch
When Percy generates screenshots, it organizes the screenshots into snapshots, and the snapshots into a build. Subsequently, new screenshots undergo comparison with baseline screenshots from a prior build.

By default, Percy uses “master” as the default base branch. You can configure a branch to serve as the default base for comparisons. If your Git project’s main branch has a different name, it’s important to update your Percy settings to match. This ensures smooth integration and accurate visual reviews. Configuring the default base branch ensures that all subsequent branches derive their baseline for comparisons from the specified default base branch.

If the default branch is not set as ‘master’ and no branch is specified, Percy comparisons are not possible in that scenario.

### Setting the projects default base branch
If git projects default branch is different frommaster, you will want to update your  projects settings to mirror that. By default,  usesmasteras the default branch, but it’s not uncommon for teams to use a branch likedevelopas the main development branch.

`master``master``develop`To update this setting, you will need to go to your projects settings page. Once you’re on the settings page, look for a “Default base branch” heading under “Project Details”and update the “Default base branch” input.

### Overriding the default base branch
Sometimes you will want to override the default baseline for certain builds. To do this, you will need to set aPERCY_TARGET_BRANCHenvironment variable. The value ofPERCY_TARGET_BRANCHwill be the branch that has a  build which you want to use as a baseline.

`PERCY_TARGET_BRANCH``PERCY_TARGET_BRANCH`For example, if you want to compare your current checked out branch to thestagingbranch, you would set  toPERCY_TARGET_BRANCH=staging. That will use the last  build onstagingas the baseline to generate comparisons.

`staging``PERCY_TARGET_BRANCH=staging``staging`Note that if you have an SCM integration,PERCY_TARGET_BRANCHwill only be used for builds NOT associated with a pull request. A pull request’s target branch will take priority over the branch specified byPERCY_TARGET_BRANCH. To override a base build set with a PR, you will also need to setPERCY_TARGET_COMMITto a specific commit SHA.

`PERCY_TARGET_BRANCH``PERCY_TARGET_BRANCH``PERCY_TARGET_COMMIT`
### Overriding the default base commit
If you want to specify a specific commit to be used to selecting the base build, you can set thePERCY_TARGET_COMMITenvironment variable to the full commit SHA. This will only work if there is a finished  build for that commit.

`PERCY_TARGET_COMMIT`
### Auto-approve branches
Auto-approve branches in Percy refer to a feature that enables builds generated on specific branches in a version control system to skip manual approval and automatically pass visual reviews in Percy.

When you designate a branch for auto approval, builds on these branches automatically become “auto-approved” regardless of changes detected. This eliminates manual intervention, resulting in fewer false positives and saving time.

Note:

- By default commits on “master” branch are marked as auto-approve branch.
- This project setting enables teams to filter and auto-approve specific branches viaregex.
[regex](https://www.browserstack.com/docs/percy/base-selection/branch-selection)- If there are any missing snapshots in the build, we still auto-approve the build.
- If there are fewer than 10% failed snapshots in the build, it is auto-approved. If there are more than 10% failed snapshots, the build is marked as failed. If you prefer not to auto-approve,contact usto enable the validation flag for you.
[contact us](https://www.browserstack.com/contact?ref=docs)
### Approval required branches
Approval required branches typically refer to branches where changes must be approved before they can be merged into another branch. Configuring the “Approval required branches” option means that builds on these branches will exclusively use the most recently approved build within the specified branch as their baseline. Once this configuration is in place, Percy’s intelligent base build selection logic will be disabled on these branches.

This setting should only be used in special circumstances, such as for isolated branches used by a QA team who has a test suite in a disconnected repository.

You can set approved snapshots as the baseline by utilizing the “Approval required branches” setting

## Base snapshot selection
Percy’s snapshot-based approval feature enables you to review and make decisions on the visual changes detected in your application. By comparing the before and after snapshots in a build, you can validate and approve individual snapshots or the build as a whole. This means you can either approve or reject changes on a granular level, evaluating each snapshot separately, or choose to approve all the snapshots in the build collectively. This flexibility gives you control over the approval process, ensuring that only the desired and intentional visual changes are accepted.

This approach is particularly beneficial for branches that are dedicated to Quality Assurance (QA) activities. Such isolated branches provide a dedicated environment for QA teams to conduct their testing activities without interfering with ongoing development work. It enables them to perform thorough and comprehensive testing without the risk of impacting the main development branch.

By using the snapshot-based approval feature, QA teams can meticulously review and validate visual changes introduced in a specific branch or environment.

## Set approved snapshots as baseline
To set approved snapshots as the baseline for comparison:

- Login to Percy & navigate to your created Percy project.
- Go toProject Settings»Advanced Options»Approval required branches.
- In the Approval required branches field, specify the name of your testing branch. If you work with multiple branches, specify multiple branches with space and use a “*” as a wildcard match.
These branches are subject to a formal approval process before changes can become baseline for future builds.

Note:When you designate a branch (let’s sayqa-branch) as the approval required branch in your workflow, ensure not to set the same branch in the Auto Approval branch field.

### Check more details about how do build and snapshot approvals work
The following workflow outlines Percy’s systematic approach to reviewing and approving changes, encompassing both the evaluation of the entire set of snapshots at the overall build level, the individual approval of each snapshot, and the decision-making process for new and missing snapshots.

### Build approval workflow
Percy offers two approaches to capture and compare visual snapshots: Normal builds and partial builds.

A normal build involves rendering and capturing the entire application or page as a visual snapshot, encompassing all elements and components present in the interface, whereas a partial build focuses on rendering and capturing specific elements or components of the application’s interface as visual snapshots.

Based on the build type, Percy follows the below workflow:

- Normal Build: If a normal build is approved, it becomes the base build for subsequent builds. However, if it is not approved, it cannot serve as the base build but any approved snapshots within the build can still become the base snapshots for future builds.
- Partial Build: If a partial build is detected, it cannot be designated as the base build. However, approved snapshots from the partial build can still be considered as base snapshots. Note that in the case of partial builds, missing snapshots will not trigger notifications. For more information, seePartial builds.
[Partial builds](https://www.browserstack.com/docs/percy/baseline-management/partial-builds)
### Snapshot approval workflow
For Snapshot approval, Percy checks if the approved version of each snapshot is available on the same branch. If it is, Percy compares the snapshots to see if there are any differences. If yes, the user is asked to review the snapshot and decide whether to approve or request changes. If there are no differences, the snapshots are automatically approved.

On the other hand, if the approved version of a snapshot is not present on the branch, Percy treats the snapshot in the current build as a new snapshot and notifies the same.

### Snapshot is missing in the build
If a snapshot is not found in the current build, Percy verifies whether the snapshot exists in the base build. If it is present in the base build, Percy notifies the user that the snapshot is missing. However, if the snapshot is not found in the base build, the workflow comes to an end.

## Working with approval required branches - An example
- Let’s consider a scenario where a user has generated the first build, called Build 1, which has been approved.Build 1 consists of three snapshots, namely A, B, and C.Since the build is in an approved state, all the snapshots within this build are also considered approved.
- Build 1 consists of three snapshots, namely A, B, and C.
- Since the build is in an approved state, all the snapshots within this build are also considered approved.
- Now, the user proceeds to generate the second build, known as Build 2. Build 2 includes snapshots A, B, and D.At this point, Percy will perform a snapshot-level comparison between snapshots A and B from Build 1, as these snapshots were approved in the previous build.Also, during the comparison, Percy will notify that snapshot C is missing in Build 2, and it will recognize snapshot D as a new snapshot in this build.There are two possible outcomes of this comparison. First, if snapshot D is approved and there are no differences found between snapshots A and B, then Build 2 is considered approved. On the other hand, if snapshot D is either approved or unapproved and there are differences detected between snapshots A and B, then Build 2 is not approved and cannot serve as the baseline.
- At this point, Percy will perform a snapshot-level comparison between snapshots A and B from Build 1, as these snapshots were approved in the previous build.
- Also, during the comparison, Percy will notify that snapshot C is missing in Build 2, and it will recognize snapshot D as a new snapshot in this build.
- There are two possible outcomes of this comparison. First, if snapshot D is approved and there are no differences found between snapshots A and B, then Build 2 is considered approved. On the other hand, if snapshot D is either approved or unapproved and there are differences detected between snapshots A and B, then Build 2 is not approved and cannot serve as the baseline.
- Let’s break down the scenario where a user introduces a third build, Build 3, with snapshots A, C, and D. The next comparison depends on whether Build 2 is approved or not.If Build 2 is not approved, then snapshots A and C  are compared with the snapshots from Build 1.In this case, snapshot B from Build 1 will be notified as missing, and if snapshot D was approved in Build 2, it will be compared; otherwise, it will be notified as new snapshot.
- If Build 2 is not approved, then snapshots A and C  are compared with the snapshots from Build 1.
- In this case, snapshot B from Build 1 will be notified as missing, and if snapshot D was approved in Build 2, it will be compared; otherwise, it will be notified as new snapshot.
- Moving forward, the user introduces Build 4, which is marked as a partial build, containing only snapshot A.In this case, Build 4 won’t complain for missing snapshot, and if this build is approved than only that  snapshot A will be approved. However, now Build 4 cannot become a base build.
- In this case, Build 4 won’t complain for missing snapshot, and if this build is approved than only that  snapshot A will be approved. However, now Build 4 cannot become a base build.
- Next, the user generates Build 5, with snapshots A, B, C and D and all snapshots in this build are approved, hence Build 5 now becomes the base build.
The process of comparison continues in a similar manner for further builds.

### Identifying Whether a Snapshot is Not Derived from the Base Build
Check the below example of Percy’s build, where in the left panel, Build 22 is specified as the baseline build, but during the comparison, it takes the base snapshot from Build 28. This means that this particular snapshot present in Build 28 is being used as the baseline for comparison instead of the snapshot from base Build 22.

Note:This approved snapshot when considered from Build 28 indicates either it was approved in Build 28 or it has no changes since the last approved build until Build 28.

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
[Join 10k+ QA leaders & scale testing with 20+ AI agentsRegister now](https://www.browserstack.com/events/qa-leadership-summit-winter-2025?ref=guide-page&utm_source=docs&utm_medium=website&utm_platform=&utm_content=guide&utm_campaign=QALS-winter-november-2025&utm_campaigncode=701OW00000WdkF3YAJ&utm_term=docs-banner)Join 10k+ QA leaders & scale testing with 20+ AI agents

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