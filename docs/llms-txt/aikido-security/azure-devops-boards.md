# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/azure-devops-boards.md

# Azure DevOps Boards

*📋 Setting up automated task creation in Azure DevOps Boards*

## Introduction <a href="#introduction" id="introduction"></a>

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Azure DevOps Boards.

Following use cases are supported :

* **Automated Ticket Creation**: Automatically create and push tickets to specified Boards projects for seamless tracking of security issues.
* **Manual Ticket Addition**: Manually add security issue tickets to Boards, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Boards <a href="#connecting-the-aikido-app-to-boards" id="connecting-the-aikido-app-to-boards"></a>

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Azure DevOps Boards'\
   A modal will request some more information to authenticate:

   * **UserID**​: this is your **email**
   * **Access Token**: Can be found inside Azure DevOps. As scope, under '**Work Items**', you can select '**Read & write**'.
   * **Organisation** ***Name*****:** name of the organisation, can be found in the URL <mark style="color:red;">Make sure to include the organisation name ONLY, without the prefix of the url https\://...</mark>\ <br>

   ![Azure DevOps integration setup screen prompting for user ID, token, and organization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-576a9243c01363aca2a13c3d8fa8ab27964c51cd%2Fazure-devops-boards_d8185da7-4270-4757-983c-2f49135d8433.png?alt=media)
3. After filling in the credentials correctly, press save and Close the modal.\
   ​
4. Open the Azure DevOps Boards Integration page to manage the auto creation settings.\
   ​

   ![Azure DevOps Boards integration setup: map repos, enable autocreation, set default task type.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c34d515eb718263b78f7eaacb54cb95452508680%2Fazure-devops-boards_6ca66041-0504-4364-9a0c-281eee90ffa3.png?alt=media)

## Options for Task Creation in Azure DevOps Boards via Aikido <a href="#options-for-task-creation-in-azure-devops-boards-via-aikido" id="options-for-task-creation-in-azure-devops-boards-via-aikido"></a>

There are two different options to create new tasks from Aikido into Boards

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation <a href="#id-1-manual-task-creation" id="id-1-manual-task-creation"></a>

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.**\
   ​

   ![Task assignment table section with add and options buttons.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2a44826adbd2b7e39af0611ffbee11bc3cce4a30%2Fazure-devops-boards_ae1f257e-0299-4349-b6df-4992273bef04.png?alt=media)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Actions dropdown menu with options for task management and severity adjustment.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a4e79410a509c6922b4448a3458827a1a1093e51%2Fazure-devops-boards_a9b48cf3-8614-447c-b1dd-252ae08967c8.png?alt=media)
2. Fill in the required details in the popup modal.\
   ​

   ![Azure DevOps Boards task creation form with fields for project, assignee, scope, summary, and description.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6f8e295ef602f38de07d5e15463bda8e487943ae%2Fazure-devops-boards_636e8271-d106-4556-9e2f-fb9c1cc51345.png?alt=media)

   ​
3. The newly created task in Boards will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![High-priority task: Minor upgrade for @babel/traverse, assigned to aaron aikidodev.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-41ed8008ed2475cc2914de266aa4b0757dfcf747%2Fazure-devops-boards_803ed3f1-1548-49b0-ba58-64e153b91f1a.png?alt=media)

## 2. Automated Task Creation <a href="#id-2-automated-task-creation" id="id-2-automated-task-creation"></a>

{% hint style="info" %}
Aikido will automatically create tasks **every hour in bulk.** There is at the moment no option to trigger this manually.
{% endhint %}

1. Go to the [Azure DevOps Boards Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Autocreation settings for generating daily tasks on critical issues or higher.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-da1a939037cd23b7d988757d5c66cc6b9a6ddc8b%2Fazure-devops-boards_b847c651-3f59-4660-8350-960a783810d7.png?alt=media)

   ​
4. Aikido will then autonomously generate Boards tickets based on these settings 🚀

***
