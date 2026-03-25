# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/clickup.md

# ClickUp

*📋 Setting up automated task creation in ClickUp*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in ClickUp.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified ClickUp projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to ClickUp, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to ClickUp <a href="#connecting-the-aikido-app-to-clickup" id="connecting-the-aikido-app-to-clickup"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'ClickUp'
3. A prompt will request authorization for ClickUp.\
   ​

   ![ClickUp authorization prompt for issue-tracking; user currently unauthorized.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f596a8b23097cb626a88b2928dcbd43d3bec46f9%2Fclickup_795b1392-e60d-4492-8853-d2b4251f9fef.png?alt=media)
4. Login into your ClickUp account
5. Grant Aikido permission to access your ClickUp workspace

   ![ClickUp workspace selection screen for connecting with Aikido Security integration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c26585189847f4d665ab63ed941f0b89d184da59%2Fclickup_72bc2856-bacd-4204-a446-7984aa1e9f38.png?alt=media)
6. Once authorized, Aikido is successfully connected to ClickUp, enhancing your task management capabilities 🚀

![Map repositories to ClickUp projects and enable automatic task creation with Aikido.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8090b05b2126ec3028cb19cab5078db1f6c66c3c%2Fclickup_e419f1df-e108-4d00-ba4d-3057129c8133.png?alt=media)

## ​Options for Task Creation in ClickUp via Aikido <a href="#options-for-task-creation-in-clickup-via-aikido" id="options-for-task-creation-in-clickup-via-aikido"></a>

There are two different options to create new tasks from Aikido into ClickUp.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Assignee section with options to add or manage task assignments.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fclickup_63fe9e3c-4d1a-4724-b36c-e206e5043543.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options: create task, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-021540fd57c14956dfe908955e17785a65e98352%2Fclickup_b05ddc73-2393-4d76-97b5-29f663068d65.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![ClickUp task creation form for reporting high-severity XSS vulnerability findings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e816c82b292bf2f77092029f21e6a0591efc3d2f%2Fclickup_368fbd17-a295-490a-b7c2-a3adecaff6df.png?alt=media)
3. The newly created task in ClickUp will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Task warning about high-risk XSS attacks from unescaped input, labeled as open.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f93a1dd3b7fcb002297069e96fbaa9278ac6cc8d%2Fclickup_7292e563-fdc4-46d8-b2d7-48bbd8567288.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [ClickUp Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings for task severity and daily task limit are enabled.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fclickup_68aa1690-fb9a-4eb9-a9ad-72c970001cc4.png?alt=media)

   ​
4. Aikido will then autonomously generate ClickUp tickets based on these settings 🚀

***
