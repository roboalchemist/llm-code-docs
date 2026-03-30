# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/github-issues.md

# GitHub Issues

**Table of contents:**

* [Introduction](#introduction-)
* [Prerequisites](#prerequisites)
* [Connecting the Aikido App to GitHub Issues](#connecting-the-aikido-app-to-github-issues)
  * [Options for Task Creation in GitHub Issues via Aikido](#options-for-task-creation-in-github-issues-via-aikido)
* [Manual Task Creation](#manual-task-creation)
* [Automated Task Creation](#automated-task-creation)
  * [Setup GitHub Issues Integration Now →](#setup-github-issues-integration-now-)
  * [Discover Integration Details →](#discover-integration-details-)

## GitHub Issues

*📋 Setting up automated task creation in GitHub Issues*

### Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in GitHub Issues

Following use cases are supported :

* **Manual Ticket Addition**: Manually sync security issue tickets to GitHub Issues.
* **Automated Ticket Creation**: Automatically create and push tickets to specified GitHub Issue projects/repos.&#x20;

{% hint style="warning" %}
All issues will be automatically created in the respective repo. If you wish to disable this functionality, contact us.
{% endhint %}

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* GitHub account needs to be an organisation account
* Issues need to be enabled inside GitHub

### Connecting the Aikido App to GitHub Issues <a href="#connecting-the-aikido-app-to-github-issues" id="connecting-the-aikido-app-to-github-issues"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'GitHub Issues'
3. **Install the Issues App inside your organisation** ([Install Link](https://github.com/apps/aikido-issues/installations/new)). This is needed in order to select your organisation.\
   ​

   ![GitHub issue-tracking integration setup requires authorization and organization configuration.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-892b2ffe71a1d5666c1a7af5d4fe637aff06ee14%2Fgithub-issues_bb36cac9-b2e2-49f3-9efc-eccad640cb18.png?alt=media)
4. Select your organisation and repos\
   ​

   ![Aikido Issues installation prompt with user selection interface.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6fa85fd0bd5abbe8ba03e1997cd54e19087bf827%2Fgithub-issues_4563a93d-56a5-4793-9297-dd32eadc05b5.png?alt=media)
5. When installed succesfully, you will get a notification on top of the page in GitHub. **Return to Aikido.**\
   ​

   ![Notification confirming "Aikido Issues" was updated for the specified user account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e4f484c8a536b4452eb9cf1659d72b0a27fead19%2Fgithub-issues_6f174321-dada-40f3-938e-635ce3e1a691.png?alt=media)
6. **Select your organisation** in the modal.\
   ​

   ![Dropdown menu for selecting an organization in settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-de468ded024a4bdb9355a8c7eb5ab4802c72489f%2Fgithub-issues_869211a2-7d05-499d-95b1-76188d6f4518.png?alt=media)
7. **Click Save.** The status will now change to **Connected.**

   ![GitHub issue-tracking integration successfully connected and ready for use.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-233f10dbcea1796acd0cfe9c4bd41a502cd4fecd%2Fgithub-issues_1816d0df-29de-4d8e-9d64-da3851964f10.png?alt=media)
8. Close the modal & open the GitHub Issues Integration page. By default all issues will be synced to the 'Default Repo'. **Contact us** if you'd like to have autosyncing issues to the respective repo.

![
](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ac22813bab7365f8b245c5a497a2fe5311a226bd%2Fgithub-issues_62e79607-05a8-4f84-b7f3-77a7009eeb62.png?alt=media)

1. You can set a Default Label that will be send for all Aikido Issues. These will be synced and appear in GitHub.​\
   ​

   ![Open GitHub issue for minor aws/aws-sdk-php upgrade, labeled low priority security fix.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-51369fd5fe250500b37224369a3b95646410b073%2Fgithub-issues_39e93b13-3513-4384-b079-1b9cba20563e.png?alt=media)

#### Options for Task Creation in GitHub Issues via Aikido <a href="#options-for-task-creation-in-github-issues-via-aikido" id="options-for-task-creation-in-github-issues-via-aikido"></a>

There are two different options to create new tasks from Aikido into GitHub Issues

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### Manual Task Creation <a href="#manual-task-creation" id="manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task management interface showing "Assignee" column with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fgithub-issues_a7a0ade6-e58d-4930-8b44-564db5251eed.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Dropdown menu with task management actions: create, snooze, ignore, copy link, adjust severity.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1b55c4f9f3975d4d09d36f4c8ff9b1aa21818e3b%2Fgithub-issues_7e71f2c8-d4a3-4214-9fc0-26341486d030.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Form for creating a new GitHub issue task with project, assignee, and description fields.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-d4780357247803a6f09ddeb87b3883a3205c34b3%2Fgithub-issues_c876d6f9-e42b-4d14-9e16-6d8f0474d73d.png?alt=media)

   ​
3. The newly created task in GitHub Issues will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Task management dashboard showing a low-priority AWS SDK PHP upgrade task.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-bf4076136ced939ad1e21d5e45582d6280156952%2Fgithub-issues_8160a9aa-cc40-4bab-9d96-e0f9f7b3f4c6.png?alt=media)

### Automated Task Creation <a href="#automated-task-creation" id="automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [GitHub Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Task autocreation settings: enable automatic creation for critical issues, limited to one task per day.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fgithub-issues_9ec09e96-b743-4daf-8fcc-f333d2bcaba2.png?alt=media)

   ​
4. Aikido will then autonomously generate GitHub Issues based on these settings 🚀

***
