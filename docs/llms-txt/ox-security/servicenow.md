# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/servicenow.md

# ServiceNow

ServiceNow is a leading digital workflow platform that helps organizations manage IT services, operations, and business processes with automation and efficiency. It’s widely used for incident management, change control, and service requests across enterprise environments.

Integrating OX Security with ServiceNow brings security insights directly into your IT operations workflows. Vulnerabilities and security issues detected by OX can be automatically converted into ServiceNow incidents or tasks, allowing IT and security teams to respond faster and more effectively.

**Benefits of the integration include:**

* **Centralized Incident Management:** Track and resolve security issues within the same platform used for IT operations.
* **Faster Response Times:** Automate ticket creation based on real-time vulnerability findings from OX.
* **Improved Collaboration:** Bridge the gap between security and IT teams with shared visibility and accountability.
* **Consistent Workflow:** Align security issue handling with your organization’s existing escalation and resolution processes.

## Prerequisites

* ServiceNow admin account.

## Creating a Dedicated ServiceNow API User

For ServiceNow-OX integrated incident management, you need to [define a new dedicated API user](#create-a-new-api-user) and then [assign this user the required roles and permissions](#assign-required-roles).

### Create a new API user

1. Go to <https://developer.servicenow.com/> and log in to your ServiceNow admin account.
2. Select **Start Building >** **Request Instance**. The process of instace creation takes 5-10 mins).
3. Select **Manage instance password**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e0bed55797af3fd4382ce24b3da55123ad85ce1c%2FSN_1.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Top start using services, click **Instance URL** and use the **Username** and the **Password**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3aed93b6523a22dc2b5c1f719b650f24bea848b5%2FSN_1_A.png?alt=media" alt="" width="282"><figcaption></figcaption></figure>

1. From the top menu, select **All > Users** and then in the right top corner, select **New**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f656b37e0dfb6753aaa8842b1dd1e9ba80e15ec0%2FSN_2.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Set the following parameters and select **Submit**.

| Parameter                | Description                                        |
| ------------------------ | -------------------------------------------------- |
| **User ID**              | api\_incident\_user                                |
| **First Name**           | Your first name.                                   |
| **Last Name**            | Your last name.                                    |
| **Password needs reset** | Select this checkbox.                              |
| **Active**               | Select this checkbox.                              |
| **Email**                | Type your email address for getting notifications. |
| **Time zone**            | Verify that the time zone is correct.              |

The new user appears in the list of users.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4698079e5692a987d9deefce65bbce58769b3ad8%2FSN_3.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select the desired User ID.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9972cd6d525095db3575f3435bf75a0d3945e6c6%2FSN_3_A.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Select **Set Password**, then select **Generate**, copy the new password and store it in a safe location.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0f91943e99261dd761d84216fb32ecec7e9a9478%2FSN_4.png?alt=media" alt=""><figcaption></figcaption></figure>

1. To link the new password to the user, select **Update**.

### Assign required roles

1. In the user definitions page, scroll down and select **Roles > Edit**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1374737c2b0ab36f39890012ff55a5edc9218ea8%2FSN_4_A.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Define the roles as follows and then select **Save**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-63959cb3ea22da903bc5f25a72a70e4d4d0f7d62%2FSN_5.png?alt=media" alt=""><figcaption></figcaption></figure>

| Role                | Description                          |
| ------------------- | ------------------------------------ |
| itil                | for incident creation and management |
| rest\_service       | essential for API access.            |
| rest\_api\_explorer | for testing API access               |
| catalog\_admin      | for category access                  |
| sn\_incident\_read  | for incident reading scope           |
| sn\_incident\_write | for incident writing scope           |

The new services appear in the user defidition page.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a6ee61988afbb1c1c6ccc57403b7e0794c3db9d4%2FSN_6.png?alt=media" alt=""><figcaption></figcaption></figure>

## Connecting to ServiceNow

1. In the **OX app**, go to **Connectors** and search for ServiceNow.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5d146182eac5340c49028e0e2db29c0a6660a8cf%2FSN_icon.png?alt=media" alt="" width="211"><figcaption></figcaption></figure>

1. Select **ServiceNow**. The **Configure your ServiceNow credentials** dialog appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-259eb86fb6e0089cbd6d986338d388e8529cfd44%2FSN_OX_connect.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

| Parameter               | Description                                                                      |
| ----------------------- | -------------------------------------------------------------------------------- |
| **ServiceNow Host URL** | The URL of the ServiceNow developer site.                                        |
| **User Name**           | The name of the user that was defined in ServiceNow for the integration with OX. |
| **Password**            | The password for the OX user in ServiceNow.                                      |
| **Token Name**          | The token name is automatically generated by OX.                                 |

1. Select **CONNECT**. The ServiceNow connector is configured.

## Adding ServiceNow Tickets

After establishing the connection with ServiceNow, you can add ServiceNow tickets to tasks and issues in OX using one of the following methods:

* Adding a new ticket to an issue, or bulk of issues.
* Adding a new ticket as a scheduled task using workflows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-352efad8621a3f7159ea1f541855744f688a0aa9%2FSN_WF.png?alt=media" alt="" width="209"><figcaption></figcaption></figure>

**To add a new ServiceNow ticket in OX:**

1. In the **Issues** page, identify and select the issue for which you want to add a new ticket in ServiceNow.
2. Select the ServiceNow icon.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-80e9f9d304cc2996df01ddb26f79f866bdcbd173%2FSN_issues_icon.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Set the ticket details in the **Create ServiceNow Ticket** dialog and select **CREATE TICKET**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bca83ba4fa3cf12ab77b18a060237de0b3d0d299%2FSN_issue_ticket.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter       | Description                                               |
| --------------- | --------------------------------------------------------- |
| **Title**       | The title of the ticket that describes the problem/issue. |
| **Category**    | The name of the workspace, as it's defined in Monday.     |
| **Assigned To** | Set the team member who will work on the ticket.          |
| **Priority**    | Set the priority for the ticket                           |

The new ticket appears in ServiceNow.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-425a51c83c60a9c7e68ac2023e01e6872f3fb0e1%2FSN_what%20you%20get%20in%20SN.png?alt=media" alt=""><figcaption></figcaption></figure>
