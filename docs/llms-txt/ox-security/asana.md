# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/asana.md

# Asana Ticketing

Asana is a powerful work management platform that helps teams organize, track, and manage their projects and tasks efficiently.

With features like task assignments, project timelines, collaboration tools, and automation, Asana enables teams to stay aligned and productive, ensuring smooth project execution from start to finish.

Integrating OX Security with Asana brings security into the heart of your project management workflow, ensuring that security issues are tracked and resolved alongside other development tasks, as follows:

* **Automated Security Task Creation**: Security vulnerabilities detected by OX Security can be automatically logged as tasks in Asana, ensuring they are addressed without delay.
* **Improved Collaboration**: Developers, security teams, and project managers can work together seamlessly by managing security-related tasks within their existing Asana workflows.
* **Enhanced Visibility and Tracking**: Security issues are prioritized alongside other work, giving teams clear visibility into security risks and their resolution status.
* **Better Compliance and Risk Management**: By tracking security-related tasks within Asana, organizations can maintain compliance and reduce security risks proactively.

## Prerequisites

* Asana account

## Getting Asana Token

1. Log in to your Asana account.
2. Click your profile picture in the top-right corner and select **Settings**, then select **Apps**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1672d9e5476fca59c58ec3ece4b51a041f4a743e%2FAsana_settings_Apps.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Click **View developer console**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-933b78724931d70acc7b03645de124c9b531116c%2FAsana_settings_my_Apps%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Select + **Create new token**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-867598bcc7393d87c25bbf6bc5fd09ca0935d3f8%2FAsana_Create_new_token.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Add token details:

| **Token name**                     | A significant name that makes it easy to identify the purpose of the token. |
| ---------------------------------- | --------------------------------------------------------------------------- |
| **I agree to the Asana API Terms** | To read the terms, click **Asana API Terms** and then select the option.    |

1. Select **Create token**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-db8782f217d470e8bcce00eb7a5e5eccfdb18e5d%2FAsana_token_details.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Copy the token and store it in a different location. After closing this dialog you cannot see it again.

## Connecting to Asana

1. In the **OX app**, go to **Connectors** and search for Asana.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fdc9f33df9d64a56bf799de3e420ae75f776c8a1%2FAsana_icon_correct.png?alt=media" alt="" width="210"><figcaption></figcaption></figure>

1. Select **Asana**. The **Configure your Asana credentials** dialog appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-734df47de8a81dda835c7016f80cdc328faf6937%2FAsana_connect.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Select **CONNECT**. The Asana connector is configured.

## Adding Asana Tickets

After establishing the connection with Asana, you can add Asana tickets to tasks and issues in OX using one of the following methods:

* Adding a new ticket to an issue, or bulk of issues.
* Adding a new ticket as a scheduled task using workflows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ab281971d3df05fae41bef6c04de6b271a469106%2FAsana_WF.png?alt=media" alt="" width="135"><figcaption></figcaption></figure>

**To add a new Asana ticket in OX:**

1. In the **Issues** page, identify and select the issue for which you want to add a new ticket in Asana.
2. Select the Asana icon.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8ef49a85f73230de2ac74bcd6108813c929be1a3%2FAsana_issues_icon.png?alt=media" alt="" width="30"><figcaption></figcaption></figure>

1. Set the ticket details in the **Create Asana Ticket** dialog and select CREATE TICKET.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07d2f1396e216adfbe436ee5f3cbdbf277fabddc%2FAsana_create_ticket.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter        | Description                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------- |
| **Title**        | The title of the ticket that describes the problem/issue.                                                     |
| **Project**      | The name of the project, as it's defined in Asana.                                                            |
| **Priority**     | Set the priority that you think should be assigned to this ticket.                                            |
| **Assignee**     | Set the team member who will work on the ticket.                                                              |
| **Tags**         | Add tags for ticket classification. You can add only default Asana tags or tags that you have added in Asana. |
| **Dependencies** | Here you can add other Asana tickets that are related to/dependent on this ticket.                            |

The new ticket appears in Asana.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-408e3c07372f205f39b41d295e3752f81f6b6db9%2FAsana_new_ticket_in_app3.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
