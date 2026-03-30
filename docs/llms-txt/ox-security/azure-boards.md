# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/azure-boards.md

# Azure Boards

Azure Boards is a work tracking tool within Azure DevOps that helps software development teams plan, track, and discuss work items efficiently.

It provides customizable Kanban boards, backlogs, dashboards, and reporting tools to streamline project management, ensuring teams can collaborate effectively on software development and delivery.

Integrating OX Security with Azure Boards enhances your software development lifecycle by embedding security insights directly into your workflow, as follows:

* **Automated Issue Tracking:** Security findings detected by OX Security can be logged as work items in Azure Boards, ensuring that vulnerabilities are addressed promptly.
* **Seamless Collaboration:** Developers, security teams, and project managers can manage security-related tasks within their existing work tracking system, reducing friction in the remediation process.
* **Improved Security Visibility:** The integration provides clear visibility into security risks within the development pipeline, helping teams prioritize and resolve issues efficiently.
* **Enhanced Compliance Management:** Organizations can ensure compliance by tracking security-related tasks alongside other development activities, making audits and reporting more manageable.

## Prerequisites

* Microsoft Azure account

## Getting Azure Boards Token

1. Log in to your Azure DevOps account:\
   [https://${hosturl}/${OrgName}](https://${hosturl}/$%7BOrgName%7D)
2. From your profile picture in the top-right corner select **User settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7d7e3fa85c85b2d86daf70904640fcb8dd216c9e%2FAzureBoards2.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **Personal Access Tokens** and then click **+ New Token**.
2. In the **Create a new personal access token dialog box**, set the following:

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-01581e4cbeb701eb3dcff9974baaa3e458d7b294%2FAzureBoards4%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter            | Description                                                                                                                                                                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | A significant name that makes it easy to identify the purpose of the token.                                                                                                                                                                                                                       |
| **Organization**     | <p>Your organization name.<br>In case your azure account is used for several organizations, you need to choose from a list.</p>                                                                                                                                                                   |
| **Expiration (UTC)** | <p>Set the expiration date as far as possible.<br>Set a specific number of days for the token's validity.<br>Define a number of days based on your organization needs.<br><strong>Note:</strong> For security reasons, it is not recommended to use the option <strong>Never expire</strong>.</p> |
| **Scopes**           | <p>The scope of access associated with this token. Set the following:<br>- <strong>Work items</strong>: <strong>Read & write</strong>.<br>- <strong>Member Entitlement Management</strong>: <strong>Read</strong><br>- <strong>Project and Team</strong>: <strong>Read</strong></p>               |

1. Select **Create**. The dialog with the token appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1b3eb3a8fe4236be10b877482722854e669bdb5c%2FAzureBoards7.png?alt=media" alt="" width="363"><figcaption></figcaption></figure>

1. Copy the token and store it in a different location.\
   After closing this dialog you cannot see it again.

## Connecting to Microsoft Azure

1. In the **OX app**, go to **Connectors** and search for Azure Boards.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2944f1e601c47c91aeba3a8ff7add36624c2e9f8%2FAzureBoards_icon.png?alt=media" alt="" width="232"><figcaption></figcaption></figure>

1. Select **Azure Boards** and set the following parameters in the **Configure your Azure Boards credentials** dialog.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6ace8bacd7e4bf8b63d9be76022b8b89461b0cad%2FAzureBoards8.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter                 | Description                                |
| ------------------------- | ------------------------------------------ |
| **Azure Boards Host URL** | Add your Azure DevOps account URL.         |
| **Token**                 | Paste the token you have created.          |
| **Token Name**            | The name is generated automatically by OX. |

1. Select **CONNECT**. The success message appears.

## Adding Azure Boards Tickets

After establishing the connection with Azure Boards, you can add Azure tickets for DevOps tasks and issues in OX using one of the following methods:

* Adding a new ticket to an issue, or bulk of issues.
* Adding a new ticket as a scheduled task using workflows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b8eb1045380211a8f569626c07018fab11538d11%2FAzureBoards13.png?alt=media" alt="" width="158"><figcaption></figcaption></figure>

**To add a new Azure ticket in OX:**

1. In the Issues page, identify and select the issue for which you want to add a devops related ticket in Azure Boards.
2. Select the Azure Boards icon.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c85b4657c97b4d5bc9804c1742e7bc1fe0c68c92%2FAzureBoards_OXicon.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Set the ticket details in the **Create Azure Boards Ticket** dialog and select CREATE TICKET.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6c88f06fed7144fd17ad88f0ec2fc4983b506ae6%2FAzureBoards10.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter        | Description                                                       |
| ---------------- | ----------------------------------------------------------------- |
| **Title**        | The title of the ticket that describes the problem/issue.         |
| **Project**      | The name of the project, as it's defined in Azure Boards.         |
| **Priority**     | Set the priority that you think should be assigned to this issue. |
| **Assign To**    | Set the team member who will work on the ticket.                  |
| **Tags**         | Add tags for ticket classification.                               |
| **Story Points** | Define how long it should take to resolve this ticket.            |
| **Type**         | Specify the type of the Azure ticket (**Epic, Issue, Task**).     |
| **Teams**        | The team that should resolve the ticket.                          |
| **Area**         | The area, as defined in the Azure Boards ticket.                  |
| **Iteration**    | The sprint in which this ticket must be resolved.                 |

The new ticket appears in Azure Boards.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-87a7d930ce9ed57d5971d68942a51b4d93426bf7%2FAzureBoards12.png?alt=media" alt=""><figcaption></figcaption></figure>
