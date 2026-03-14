# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/linear.md

# Linear

*📋 Setting up automated task creation in Linear*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Linear.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Linear projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Linear, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Linear <a href="#connecting-the-aikido-app-to-linear" id="connecting-the-aikido-app-to-linear"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Linear Issues'
3. A prompt will request authorization for Linear.\
   ​

   ![Authorization prompt for Linear issue-tracking; user currently unauthorized.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-850e27321b08e82d6e5f5ba1a65ae23ae4d9483f%2Flinear_3620920b-3f02-43c8-a768-08cd22401356.png?alt=media)
4. Login into your Linear account
5. Grant Aikido permission to access your Linear workspace

   ![Aikido Security requests access to manage and comment on issues in your Linear workspace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9adced6265021a0ff866af89265b71201fd349b9%2Flinear_5b96e403-1657-482b-b760-19f73d2bd463.png?alt=media)
6. Once authorized, Aikido is successfully connected to Linear, enhancing your task management capabilities 🚀

## ​Options for Task Creation in Linear via Aikido <a href="#options-for-task-creation-in-linear-via-aikido" id="options-for-task-creation-in-linear-via-aikido"></a>

There are two different options to create new tasks from Aikido into Linear.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assign column.**\
   ​

   ![Task management interface showing the "Assignee" column with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Flinear_68a7926c-ffdc-4813-b3e0-5e25252173f7.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Dropdown menu offering task creation and additional action options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-50c4fc60bc662b3821f743b2f5d7ee7d1a3a2ab8%2Flinear_cedd6e79-044b-42d9-a646-bd611ee50265.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Task creation form for reporting a critical Content Security Policy issue in Aikido.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5a5936aaded7a55d81b8ff689a708bc6d8f8e85f%2Flinear_10e057ec-646a-497c-bef2-24c7353c91ba.png?alt=media)
3. The newly created task in Linear will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical task: CSP header missing, issue unassigned and currently open for resolution.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f42269839d66ff6c54219e84ac5f559aa00b31dc%2Flinear_dae76f1e-7db0-4ff3-b011-52631c0175d5.png?alt=media)

### 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Linear Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings for automatic task creation based on severity and daily limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Flinear_2a504784-5a18-4dac-a575-fd4f2ea7bab2.png?alt=media)

   ​
4. Aikido will then autonomously generate Linear tickets based on these settings 🚀

***
