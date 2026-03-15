# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/jira-cloud.md

# Jira Cloud

*📋 Setting up automated task creation in Jira Cloud*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Jira Cloud.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Jira projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Jira, ensuring targeted attention for critical vulnerabilities.

{% hint style="warning" %}
Note: the ticket creation is linked to the user who has set up the integration. We recommend creating an extra 'Aikido' user inside Jira with write access to all projects.
{% endhint %}

## Connecting the Aikido App to Jira <a href="#connecting-the-aikido-app-to-jira" id="connecting-the-aikido-app-to-jira"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Jira Issues'
3. A prompt will request authorization for Jira.\
   ​

   ![Jira access unauthorized; prompt to authorize account for issue-tracking integration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-556af441921a4c0ed9e37f27386a63fca7b3e117%2Fjira-cloud_7f02a7ff-2d6a-4fd2-859a-690ec2503847.png?alt=media)
4. Login into your Jira account
5. Grant Aikido permission to access your Jira workspace

   ![Aikido Security requests permission to access and manage your Atlassian Jira account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7d2ac9ab0fe4929ed1615e3358c1956f680100f4%2Fjira-cloud_a052e293-4386-42ea-a4ae-4fa3661b2fad.png?alt=media)
6. Once authorized, Aikido is successfully connected to Jira, enhancing your task management capabilities 🚀<br>

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FIIJTv7IwxLagom4d9B03%2Fimage.png?alt=media&#x26;token=7e64c1e3-bbc4-47a2-b543-6a6100e8a96b" alt="" width="563"><figcaption></figcaption></figure>

## ​Options for Task Creation in Jira via Aikido <a href="#options-for-task-creation-in-jira-via-aikido" id="options-for-task-creation-in-jira-via-aikido"></a>

There are two different options to create new tasks from Aikido into Jira.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assign column.**

   ![Task management table with “Assignee” column and options to add or edit entries.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fjira-cloud_0001b592-6b4b-4bbf-b3a8-ff8ddff44c51.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.

   ![Menu of task management actions: create, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d48713cff103c764405a9fcbcfccdbde6e7c7ee3%2Fjira-cloud_38576e60-ea82-4442-88d3-db09a3bbd539.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Jira task creation form detailing a critical security vulnerability.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8e0c4229e5124fa8d1d8f8e4cd261a3e56169e01%2Fjira-cloud_61e7326b-5183-4741-aaac-891ec98663fc.png?alt=media)
3. The newly created task in Jira will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Critical security task: var\_dump() may expose sensitive user information; action required.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5c8af49ae0f80e42d1ed19999fe754dacbd5f5cf%2Fjira-cloud_294591ba-6d3d-4cfc-9cee-0fc1b6c880cd.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Jira Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.

   ![Autocreation settings for automatic task generation based on issue severity and daily limit.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fjira-cloud_a2cf62ba-d5ce-4053-a032-2f6f5f0b43ad.png?alt=media)

   ​
4. Aikido will then autonomously generate Jira tickets based on these settings 🚀

### Jira Sync Information <a href="#jira-sync-information" id="jira-sync-information"></a>

Aikido automatically syncs a couple of fields to Jira

* Severity is mapped to the 'Priority field' in Jira (one way)
* Assignees are synced both ways (so updates in Jira will be reflected in Aikido too

***
