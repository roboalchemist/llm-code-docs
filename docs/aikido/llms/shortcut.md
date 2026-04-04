# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/shortcut.md

# Shortcut

*📋 Setting up automated task creation in Shortcut*

### Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Shortcut.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Shortcut projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Shortcut, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Shortcut <a href="#connecting-the-aikido-app-to-shortcut" id="connecting-the-aikido-app-to-shortcut"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Shortcut'
3. A prompt will request authorization for Shortcut.\
   ​

   ![Shortcut issue-tracking setup screen prompting for API key configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0d2f97cdcd985979c860e6836a652bca58bdf510%2Fshortcut_47c4c8f3-3a8c-4029-ade4-7aae235f0cf1.png?alt=media)

   ​
4. Login into your Shortcut account
5. Grant Aikido permission to access your Shortcut workspace
6. Once authorized, Aikido is successfully connected to Shortcut, enhancing your task management capabilities 🚀

![Map repositories to Shortcut teams and enable or disable task autocreation.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8d9393c5053c40cded6d209149c751ed03fc75b9%2Fshortcut_509f1035-d5ae-49e2-9213-912ca5ffda52.png?alt=media)

## Options for Task Creation in Shortcut via Aikido <a href="#options-for-task-creation-in-shortcut-via-aikido" id="options-for-task-creation-in-shortcut-via-aikido"></a>

There are two different options to create new tasks from Aikido into Shortcut.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task table section showing "Assignee" field with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fshortcut_35248b32-c81f-4581-b101-909ea251588e.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Dropdown menu with task management actions: create, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4067fb2cc4f1003160a84d70590cd024877befb2%2Fshortcut_357ca834-144e-425d-80c3-e125c3b7ccd7.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​
3. The newly created task in ClickUp will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![High-priority tzinfo upgrade task, currently unassigned and open for action.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6fe8c245bf5c7526bd1514118b5f0cde09441e11%2Fshortcut_ad2fc758-eca3-4e95-94e4-7fb186aca52b.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Shortcut Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Task autocreation settings interface for handling critical issues, with daily task limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fshortcut_0db998f8-a063-4a93-a616-c08d38411906.png?alt=media)

   ​
4. Aikido will then autonomously generate Shortcut tickets based on these settings 🚀

***
