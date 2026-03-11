# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/jira-data-center.md

# Jira Data Center

**Table of contents:**

* [Introduction](#introduction-)
* [Prerequisites](#prerequisites)
* [Connecting the Aikido App to Jira](#connecting-the-aikido-app-to-jira)
* [Options for Task Creation in Jira via Aikido](#options-for-task-creation-in-jira-via-aikido)
* [1. Manual Task Creation](#1-manual-task-creation)
* [2. Automated Task Creation](#2-automated-task-creation)
  * [Setup Jira Integration Now→](#setup-jira-integration-now-)
  * [Discover Integration Details →](#discover-integration-details--)

## Jira Data Center

***📋 Setting up automated task creation in Jira Data Center***

### Introduction <a href="#introduction" id="introduction"></a>

This article focuses on those companies that have Jira Data Center running (i.e., Jira on premise, different from [Jira Cloud](https://help.aikido.dev/en/articles/8680218-setting-up-automated-task-creation-in-jira-cloud)). The following one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Jira On Prem.

Following use cases are supported :

* Automated Ticket Creation: Automatically create and push tickets to specified Jira projects for seamless tracking of security issues.
* Manual Ticket Addition: Manually add security issue tickets to Jira, ensuring targeted attention for critical vulnerabilities.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

In order to make the connection to JIRA Data Center, you'll need to create a personal access token. This token will then be used to carry out all requests to your instance.\
​\
Please note that the level of access the integration has will be equal to the person who created the personal access token (PAT). It's therefore advised to let a person with sufficient access rights in the environment to create the PAT.

To create a PAT, you can follow the steps below:

1. Navigate to your JIRA Data Center environment
2. Click on your avatar in the navigation bar on top and navigate to "Profile"
3. Click on "Personal Access Tokens", you should end up on a screen similar to the one below**​**

   ![Jira Software personal access tokens page prompting user to create their first token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-792134445b90e7c6d1bf8e568dcbbc3840ea981c%2Fjira-data-center_bd8df7ef-3798-4bdb-acac-65a30ef15823.png?alt=media)
4. Click on "Create token" and give it an appropriate name
5. We advise to not set an expiry date, but if you do, you'll have to remind yourself to update the token in Aikido periodically
6. Once the token is created, you'll get to copy it momentarily, copy the token and keep it for the next step

### Connecting the Aikido App to Jira <a href="#connecting-the-aikido-app-to-jira" id="connecting-the-aikido-app-to-jira"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Jira Data Center'
3. Enter the url of your environment
4. Enter the PAT from the previous step and hit "Save"**​**

   ![Jira Data Center integration setup: enter server URL and personal access token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ea7bcbd99334f1ec8279aea3d333f6fd0bdf2e58%2Fjira-data-center_f6f0b160-29a8-4940-8cd2-0a53e76f1741.png?alt=media)
5. Once authorized, Aikido is successfully connected to Jira, enhancing your task management capabilities 🚀

   ![Jira Data Center integration settings for repo mapping, task autocreation, and default labels.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2ee2f66f0404ba302a1b0a237ddf9da89ebc570f%2Fjira-data-center_3d9b5e8e-600d-467a-9683-1c80aa0e556f.png?alt=media)

### Options for Task Creation in Jira via Aikido <a href="#options-for-task-creation-in-jira-via-aikido" id="options-for-task-creation-in-jira-via-aikido"></a>

There are two different options to create new tasks from Aikido into Jira.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the *+* in the assign column.**​**

   ![Task assignment table with add and options buttons under "Assignee" column.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fjira-data-center_41b48dfa-4002-4038-85ac-35e0f21a5378.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options to manage, share, or adjust task settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d48713cff103c764405a9fcbcfccdbde6e7c7ee3%2Fjira-data-center_8e0eca2d-bd15-4a1a-917e-c22a19b36547.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Jira task creation form with project, assignee, scope, summary, and description fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8e0c4229e5124fa8d1d8f8e4cd261a3e56169e01%2Fjira-data-center_2601869d-3437-4823-b410-264c9eb9f8fb.png?alt=media)
3. The newly created task in Jira will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical task: var\_dump() exposes sensitive info, needs attention and assignment.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5c8af49ae0f80e42d1ed19999fe754dacbd5f5cf%2Fjira-data-center_6fd5b53d-a667-4294-b410-5caecbb3552d.png?alt=media)

### 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Jira Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable 'Autocreation' by clicking the toggle to On.
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings: Automatically create one task daily for critical issues or higher.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fjira-data-center_003436a4-f840-40c3-a362-f9f37b377cc1.png?alt=media)

   **​**
4. Aikido will then autonomously generate Jira tickets based on these settings 🚀

***
