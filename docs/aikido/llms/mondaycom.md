# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/mondaycom.md

# Monday.com

*📋 Setting up automated task creation in Monday.com*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in the Monday app.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Monday.com projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Monday.com, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Monday.com <a href="#connecting-the-aikido-app-to-mondaycom" id="connecting-the-aikido-app-to-mondaycom"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Monday.com'\
   A modal will request an **API Key** (of your Monday workspace). This API key can be found in Administration -> Connections -> API.\
   ​

   ![Monday.com integration setup screen requesting API key for issue tracking configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-875f3c3e098d4dee0aa02aa1181e59d898c84d69%2Fmondaycom_4398b70e-28ca-4e9b-9b40-bf3788b6b1d9.png?alt=media)
3. When you have filled in the credentials correctly, the 'Connected' status will appear.\
   ​

   ![Monday.com issue-tracking integration successfully connected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9a78c058627a830a2264f88b08fbec57b21ccd34%2Fmondaycom_4661f824-7819-4aff-b74b-b7dd04a0c42c.png?alt=media)

Close the modal & open the Monday.com Integration page.

![Map repositories to monday.com projects and enable automated task creation with Aikido.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5e7e807248251fc05aca0994ba37aefb1dcd1fd2%2Fmondaycom_dc426a4a-3d15-46dc-aad4-998e028ffa9f.png?alt=media)

## Options for Task Creation in Monday.com via Aikido <a href="#options-for-task-creation-in-mondaycom-via-aikido" id="options-for-task-creation-in-mondaycom-via-aikido"></a>

There are two different options to create new tasks from Aikido into Monday.com.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignment interface with options to add or manage an assignee.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fmondaycom_504a5b08-ce92-4bd3-b464-fa7388ff2b18.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options to create task, snooze, ignore, copy link, or adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f5536a3335e1cc523ce45b3d7377bb96634f0dfc%2Fmondaycom_466636e8-15d6-4a23-abb5-27f748884ebe.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Task creation form for project management in monday.com, detailing a critical upgrade issue.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2520f14235e8aae5d2c2bb86930fa33f6fc02a3b%2Fmondaycom_7ed10212-15ca-4d68-afd4-6510ac747e14.png?alt=media)

   ​
3. The newly created task in Monday.com will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical Log4j upgrade task assigned to Maarten De Schuymer.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-45f83feaef6ed9d301bd489d96d791b93d6f4a51%2Fmondaycom_e8b64e9e-3feb-471c-9ac9-a1c89c5fba00.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Monday.com Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Task tracker settings for automatic task creation based on issue severity and daily limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-99fc126ce92c0f7fb334ea553c56470c86832fbd%2Fmondaycom_843bd00e-b2b0-4106-be92-cc720f2f6419.png?alt=media)
4. Aikido will then autonomously generate Monday.com tickets based on these settings 🚀

***

***
