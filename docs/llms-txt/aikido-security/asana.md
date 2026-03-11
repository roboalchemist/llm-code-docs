# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/asana.md

# Asana

*📋 Setting up automated task creation in Asana*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Asana.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Asana projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Asana, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Asana <a href="#connecting-the-aikido-app-to-asana" id="connecting-the-aikido-app-to-asana"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Asana'
3. A prompt will request authorization for Asana.

   ![Asana integration unauthorized; prompt to authorize access for issue-tracking.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e2dc5abffa04d6945840f96e6c202c1b8f271982%2Fasana_98d9b2b9-76e9-4a91-8726-6468e0239bf0.png?alt=media)

   ​
4. Login into your Asana account
5. Grant Aikido permission to access your Asana workspace

   ![Asana permission request for Aikido Security to access and modify your account data.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-26c32d4ac81fdb742c4ea13cbbac95667f097bf6%2Fasana_c08d4b3c-4754-43f3-b511-a0cb2dc3865d.png?alt=media)
6. Once authorized, Aikido is successfully connected to Asana, enhancing your task management capabilities 🚀

![Configure Asana integration to map repositories and enable automatic task creation.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-58c449bb7f87877e4ce10cd8c2301b97eea432fb%2Fasana_bbbaa91c-c6ce-4001-9052-308b490bc384.png?alt=media)

## ​Options for Task Creation in Asana via Aikido <a href="#options-for-task-creation-in-asana-via-aikido" id="options-for-task-creation-in-asana-via-aikido"></a>

There are two different options to create new tasks from Aikido into Asana.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignee section with add and options buttons visible.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fasana_a6b1ac3d-ef37-454a-a531-b366d190f292.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.

   ![Action menu with options to manage, snooze, ignore, share, or adjust task severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-de6fef3756564ef12a31b460350c1d0b23228a8f%2Fasana_487046b9-543c-4f1f-bcfc-f00f9b9edf71.png?alt=media)

   ​
2. Fill in the required details in the popup modal.\
   ​

   ![Create a ClickUp task reporting a high-severity XSS vulnerability with details and link.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e816c82b292bf2f77092029f21e6a0591efc3d2f%2Fasana_22b79ff6-7c72-4889-9897-766cbe39516b.png?alt=media)
3. The newly created task in Asana will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![High-priority task warning: Unescaped input may cause XSS attacks.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f93a1dd3b7fcb002297069e96fbaa9278ac6cc8d%2Fasana_eca9cd6d-11f2-495c-88c4-db292078ec4c.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Asana Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Task autocreation settings for critical issues, limited to one task per day.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fasana_91aebcb9-d648-4193-ac60-f44d9aa5f37a.png?alt=media)

   ​
4. Aikido will then autonomously generate Asana tickets based on these settings 🚀
