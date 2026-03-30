# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/jetbrains-youtrack.md

# JetBrains YouTrack

*📋 Setting up automated task creation in JetBrains YouTrack*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in YouTrack.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified YouTrack projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to YouTrack, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to YouTrack <a href="#connecting-the-aikido-app-to-youtrack" id="connecting-the-aikido-app-to-youtrack"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'YouTrack'\
   A modal will request the **Service URL** (of your YouTrack space) and the **Permanent Token**. The permanent token can be generated inside Profile -> Account Security in YouTrack.\
   ​

   ![JetBrains YouTrack integration setup screen requiring configuration for Service URL and token.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-324f79ae66f62e7764d3fd76916e71265a0c4746%2Fjetbrains-youtrack_4b2cd46d-fffe-4903-8c91-3b2f596a08d0.png?alt=media)
3. When you have filled in the credentials correctly, the 'Connected' status will appear.\
   ​

   ![JetBrains YouTrack issue-tracking integration is successfully connected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9cdf5b48fda4eed06398705329713d8807ac77de%2Fjetbrains-youtrack_6e0c61d5-f127-47e0-b0ba-79421e6a7dc6.png?alt=media)
4. Close the modal & open the YouTrack Integration page.\
   ​

![Map Git repositories to YouTrack projects and enable automatic task creation.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9041bf2c74162134ef849833df0df3384211ba6c%2Fjetbrains-youtrack_32e98656-e17b-4e42-9d5e-ad2611ed3541.png?alt=media)

## Options for Task Creation in YouTrack via Aikido <a href="#options-for-task-creation-in-youtrack-via-aikido" id="options-for-task-creation-in-youtrack-via-aikido"></a>

There are two different options to create new tasks from Aikido into YouTrack.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignment table section with options to add or manage assignees.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fjetbrains-youtrack_fd1bad1c-19b7-41d9-ba08-683817d37328.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Action menu with options: create task, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cd9fbadb30b244291b649bcf5dc8dd1b0d7978db%2Fjetbrains-youtrack_8642287d-0d10-46bf-9d0d-d25cf159d51d.png?alt=media)

   ​
2. Fill in the required details in the popup modal.\
   ​

   ![Form for creating a security task in JetBrains YouTrack with summary and details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b1da99a1c36e0b4fe0770088171be43c8b5b7eda%2Fjetbrains-youtrack_98ce3ad1-5aca-4912-b986-17f2e2dc385c.png?alt=media)
3. The newly created task in YouTrack will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).\
   ​

   ![Security alert: HSTS header missing, high severity, reported by admin.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1fb87a2e240a65757508c64913a3e68b48a86579%2Fjetbrains-youtrack_df00a756-237c-4b53-949c-a66b981c5a56.png?alt=media)

### 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [YouTrack Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Automatic task creation for critical issues, limited to one task per day.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fjetbrains-youtrack_664f2728-c619-4a8c-8cde-32b8a1abaf16.png?alt=media)

   ​
4. Aikido will then autonomously generate YouTrack tickets based on these settings 🚀\
   ​
