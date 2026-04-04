# Source: https://www.activepieces.com/docs/admin-guide/guides/project-releases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Project Releases

> Learn how to manage and deploy releases across projects

Project Releases allow you to sync flows, connections, and tables between different projects—essential for teams that want to develop in one environment and deploy to another with confidence.

<Tip>
  **Example:** Build and test your automations in a **Staging** project, then seamlessly promote them to **Production** when ready. Simply navigate to your Production project → **Releases** → create a release from Staging, and all your changes will be applied instantly.
</Tip>

## Overview

There are three ways to create a release:

| Source       | Description                                      |
| ------------ | ------------------------------------------------ |
| **Git**      | Pull changes from a connected Git repository     |
| **Project**  | Copy flows from another project in your instance |
| **Rollback** | Restore a previous release state                 |

## Prerequisites

### Enabling Environments

In your project dashboard, go to settings then to Environments and hit the enable button.

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-1.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=1cd45275fae502e5ec17d9c70481d04b" alt="Enable Environments" data-og-width="1410" width="1410" data-og-height="897" height="897" data-path="resources/screenshots/enable-environments-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-1.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=f339facbfec2897b3ef857f3908c8635 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-1.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=ab450d9b5deb93816c16d173a48484ba 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-1.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=d19cfa8a3ff90eb97eb42323ddc1b05c 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-1.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=2ac4c095684ace3178b7b3badaa50a22 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-1.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=15c38c9c6920dc8d508db976ae5ec565 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-1.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=c2a759e07462c9e7ea01af1176987b96 2500w" />

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-2.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=cab8a5f97a6193444d15336844262b18" alt="Enable Environments" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/enable-environments-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-2.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=adab4d0374f5cc4a58f332e51c0f2de5 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-2.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=66040b659c011da7324b80cd8e894efb 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-2.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=855b000db55a471acf45e6dc8228c1cf 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-2.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=2eacb5efe32c49fdbf06ac027cf07077 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-2.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=dcb6b7116bbdba72069ac0c26a07900e 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/enable-environments-2.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=11806d38af71f64d29c9f27ad3f12837 2500w" />

## Getting Started

Navigate to the **Releases** page from your project sidebar to view all releases and create new ones.

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/project-releases-page.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=8d4f1f4b54fff8af85717ffde2b5a912" alt="Project Releases Page" data-og-width="1063" width="1063" data-og-height="672" height="672" data-path="resources/screenshots/project-releases-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/project-releases-page.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=37e1c80e0ce79a87ec5d535c960641b7 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/project-releases-page.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=f47ed59367a14175b20801ea2de6e3f0 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/project-releases-page.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=dd84fe31a506245530e2f35eae9af0d5 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/project-releases-page.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=0d32fb6e4c9c0c73d80939abe6eb20a2 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/project-releases-page.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=36447fc55b6cab15c46613028ca89736 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/project-releases-page.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=97f1f19656a9a1f3923c60d28c062568 2500w" />

## Connecting Git (Optional)

If you want to use Git to track your changes, you'll need to connect a Git repository first. This requires the Environments feature to be enabled.

## Creating a Release

### From Project

Apply changes from flows, connections and tables in one project to another.

<Steps>
  <Step title="Open Create Release Menu">
    Click the **Create Release** dropdown button.
  </Step>

  <Step title="Select From Project">
    Choose **From Project** from the dropdown menu.
  </Step>

  <Step title="Select Source Project">
    Choose the project you want to copy flows, connections and tables from.
  </Step>

  <Step title="Review and Apply">
    Review the changes, and click **Apply Changes**.
  </Step>
</Steps>

<img src="https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-1.png?fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=52cf75eef7ea0e510f0c8a0ead7da023" alt="Create Release from Project" data-og-width="1061" width="1061" data-og-height="675" height="675" data-path="resources/screenshots/create-release-from-project-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-1.png?w=280&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=910be928ea0661b82460a98b55d164ee 280w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-1.png?w=560&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=433c46359d3ccc5dc6a09c231685b4d1 560w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-1.png?w=840&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=06eebabb7d5f1586341365c519538bad 840w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-1.png?w=1100&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=c1202a0d1a297d0c5f6d373adfa2cf51 1100w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-1.png?w=1650&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=703e9597fd424d7d158a02b683f14d9a 1650w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-1.png?w=2500&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=de30f0867b1a202127ae6925f90c99c2 2500w" />

<img src="https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-2.png?fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=4dde7a456b064892dc74ab04c2272992" alt="Create Release from Project" data-og-width="1057" width="1057" data-og-height="667" height="667" data-path="resources/screenshots/create-release-from-project-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-2.png?w=280&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=346f7a5fa5ec99f0839f3e900ef75e9a 280w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-2.png?w=560&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=4b7d95659df0b09a5efc89796f90639c 560w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-2.png?w=840&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=c5381ebf779b1c73d0761ba157170304 840w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-2.png?w=1100&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=0ae5e649192b8b77d790b5415e81f884 1100w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-2.png?w=1650&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=2fcc20ff31b8ec0754e166c882affe77 1650w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-release-from-project-2.png?w=2500&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=9e6444bda5b19835f2b4608531e3be13 2500w" />

<Warning>
  New connections created during a release are placeholders and need to be reconnected with valid credentials after the release is applied.
</Warning>

### From Git

<Steps>
  <Step title="Open Create Release Menu">
    Click the **Create Release** dropdown button.
  </Step>

  <Step title="Select From Git">
    Choose **From Git** from the dropdown menu.
  </Step>

  <Step title="Review Changes">
    A dialog will appear showing all the changes that will be applied:

    * **Flows Changes**: New, updated, or deleted flows
    * **Connections Changes**: New or renamed connections
    * **Tables Changes**: New, updated, or deleted tables
  </Step>

  <Step title="Select Changes">
    Check or uncheck the flows you want to include in this release.
  </Step>

  <Step title="Add Release Details">
    Enter a **Name** and optional **Description** for your release.
  </Step>

  <Step title="Apply Changes">
    Click **Apply Changes** to create the release.
  </Step>
</Steps>

<img src="https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-git-release.png?fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=a4582d90ec24e472da9137f2ab3becab" alt="Create Release from Git" data-og-width="1409" width="1409" data-og-height="889" height="889" data-path="resources/screenshots/create-git-release.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-git-release.png?w=280&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=59125298dc68faf0d76b2fe40cf4c6f8 280w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-git-release.png?w=560&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=ebf8e8c13026db75be65154e53dd47a5 560w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-git-release.png?w=840&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=e3bce617116a0b338fb3805e84f426de 840w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-git-release.png?w=1100&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=e08999c1671d356581f7e3ce6fe5c6b9 1100w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-git-release.png?w=1650&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=67274cde30a22df8f66189339c8be940 1650w, https://mintcdn.com/activepieces/43FONS7ax8WC7q2h/resources/screenshots/create-git-release.png?w=2500&fit=max&auto=format&n=43FONS7ax8WC7q2h&q=85&s=94ae5aecdf6f380294af77f1f2eab362 2500w" />

## Push Everything to Git

If your project is connected to a Git repository, you can push all your flows, connections, and tables to Git.

<Steps>
  <Step title="Click Push Everything">
    Click the **Push Everything** button on the releases page.
  </Step>

  <Step title="Enter Commit Message">
    Write a descriptive commit message explaining your changes.
  </Step>

  <Step title="Push">
    Click **Push** to send all published flows to the Git repository.
  </Step>
</Steps>

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-everything-to-git.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=e19de434abef093657c78b2044e66488" alt="Push Everything to Git Dialog" data-og-width="1403" width="1403" data-og-height="894" height="894" data-path="resources/screenshots/push-everything-to-git.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-everything-to-git.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=f741387c53a62ebf42204590669e0558 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-everything-to-git.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=dd85d9a225cbbf0793873d6d9aed08c7 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-everything-to-git.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=3040725f4baa5ad7cd1876d3f713de2a 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-everything-to-git.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=fd001082e2ab2849a4c7f1021f162ddb 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-everything-to-git.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=0373e4b7a53522ad55e346a14e2ed26c 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-everything-to-git.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=6968bf1e81d51b3b77ab74e0593d8642 2500w" />

## Pushing Individual Flows or Tables

You can also push specific flows or tables to Git without pushing everything.

<Warning>
  You can only push published flows to git
</Warning>

<Steps>
  <Step title="Select Items">
    Navigate to your flows or tables and select the items you want to push.
  </Step>

  <Step title="Open Push Dialog">
    Click the **Push to Git** option.
  </Step>

  <Step title="Enter Commit Message">
    Provide a commit message describing what you're pushing.
  </Step>

  <Step title="Push">
    Click **Push** to send the selected items to Git.
  </Step>
</Steps>

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-1.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=98b774cdafada21fef0603bc45d27869" alt="Push to Git Dialog" data-og-width="1412" width="1412" data-og-height="892" height="892" data-path="resources/screenshots/push-flows-to-git-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-1.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=bdefe2412f15b292a89eeaceabedb108 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-1.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=a9d5895e0b77ee6eee6a14d9ef0f2856 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-1.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=769116097ab4437e61e65c6a32c99029 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-1.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=b1a95fe4f5efdb5482f4d4ddf0062881 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-1.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=6202afea8e31a6a185f3baa3efa9f6d5 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-1.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=4a8d86ac88f19fd22950fca77304226b 2500w" />

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-2.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=87945284e4ecea4a7c14b2389cb8ae7b" alt="Push to Git Dialog" data-og-width="1059" width="1059" data-og-height="670" height="670" data-path="resources/screenshots/push-flows-to-git-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-2.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=154646cb8bbe5f76c47a99864bacfe16 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-2.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=e02658ffec765ef1c92f226015cafff3 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-2.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=62aa4313c4a1ef3dfe8e42f1d0590093 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-2.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=70d81a22699f808c2f0b653f3b51d7ba 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-2.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=8d29a3c6399ed87bb5501728b7a887a1 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/push-flows-to-git-2.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=91eddf7b759457b51720a3123dbb0dec 2500w" />

## Rolling Back a Release

If something goes wrong after applying a release, you can easily rollback to a previous state.

<Steps>
  <Step title="Find the Release">
    Locate the release you want to rollback to in the releases list.
  </Step>

  <Step title="Click Rollback">
    Click the rollback icon (↩) next to the release.
  </Step>

  <Step title="Review Changes">
    Review the changes that will be applied to restore that release state.
  </Step>

  <Step title="Apply Rollback">
    Select the changes to include and click **Apply Changes**.
  </Step>
</Steps>

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/rollback-release.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=014b599b2164257c1cd267686edb57c7" alt="Rollback Release" data-og-width="1409" width="1409" data-og-height="891" height="891" data-path="resources/screenshots/rollback-release.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/rollback-release.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=62de6e2f4bb62c804e7859d8d0fa6fe7 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/rollback-release.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=b16faf6cca26d5b43f38c862ffbdeb79 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/rollback-release.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=bbeda9c954628b43541ba5f96f54cb55 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/rollback-release.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=cdfcdcacf3a3055a7ddc540f0fa7afa0 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/rollback-release.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=b588d75ef4bd106d6bb724a3bb2e8294 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/rollback-release.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=83adc856e4f067ddaf32733313001ccb 2500w" />

## Release Details

Each release in the list shows:

| Column          | Description                                             |
| --------------- | ------------------------------------------------------- |
| **Name**        | The name you gave the release                           |
| **Source**      | Where the release came from (Git, Project, or Rollback) |
| **Imported At** | When the release was created                            |
| **Imported By** | The user who created the release                        |

Click on any release to view its full details.

<img src="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/release-details.png?fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=91d8979fe0bf13121571a62be348ce01" alt="Release Details" data-og-width="1416" width="1416" data-og-height="895" height="895" data-path="resources/screenshots/release-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/release-details.png?w=280&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=eb51642dd753356a374ecf10b8dba47e 280w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/release-details.png?w=560&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=fa7d1b63e98c593b5200699b3d5d2dc2 560w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/release-details.png?w=840&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=0fb8a771b852d33ba302ab299cd92065 840w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/release-details.png?w=1100&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=01c3f579246d6c4949a5d6a9a9b312a5 1100w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/release-details.png?w=1650&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=00668e3b9ca28959f81ca7e91bc20d84 1650w, https://mintcdn.com/activepieces/HfEX6NmvKT3DcQHg/resources/screenshots/release-details.png?w=2500&fit=max&auto=format&n=HfEX6NmvKT3DcQHg&q=85&s=4ea39e90eac163d569b7d18623fc7213 2500w" />

## Understanding the Changes Preview

When creating a release, you'll see a preview of all changes:

### Flow Changes

* New flows that will be created
* Existing flows that will be updated
* Flows that will be deleted

### Connection Changes

* New connections are placeholders and must be reconnected after the release
* Renamed connections

### Table Changes

* New, updated, and deleted tables are shown with their respective indicators

## Best Practices

<CardGroup cols={2}>
  <Card title="Use Descriptive Names" icon="tag">
    Give your releases meaningful names like "v1.2.0 - Added email notifications" to easily identify them later.
  </Card>

  <Card title="Review Before Applying" icon="eye">
    Always review the changes preview carefully before applying a release to avoid unexpected modifications.
  </Card>

  <Card title="Test in Development" icon="flask">
    If using Git sync, test changes in a development project before deploying to production.
  </Card>

  <Card title="Document Changes" icon="file-lines">
    Use the description field to document what changed and why for future reference.
  </Card>
</CardGroup>

## Permissions

To create and manage releases, you need the **Write Project Release** permission. Contact your instance administrator if you don't have access to the releases feature.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Environment settings are locked">
    The Environments feature must be enabled on your instance plan to use Git sync. Contact your instance administrator to upgrade your plan or enable this feature.
  </Accordion>

  <Accordion title="Git connection fails">
    * Verify your SSH private key is correctly formatted (ends with an endline), and make sure it has an empty phrase.
    * Ensure the remote URL is in SSH format (not HTTPS)
    * Check that the branch exists in the repository
  </Accordion>

  <Accordion title="No changes detected">
    If no changes appear when creating a release, it means your current project is already in sync with the source.
  </Accordion>

  <Accordion title="Connection placeholders">
    After applying a release with new connections, navigate to the Connections page and reconnect them with valid credentials.
  </Accordion>

  <Accordion title="Push Everything button not visible">
    Make sure you configured your git settings and if you are selecting flows, make sure they are published.
  </Accordion>

  <Accordion title="Cannot find Environment settings">
    Navigate to **Project Settings** from the sidebar, then click on **Environment**. If you don't see this option, the Environments feature may not be enabled for your instance.
  </Accordion>
</AccordionGroup>
