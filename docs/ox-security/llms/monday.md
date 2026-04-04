# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/monday.md

# Monday

Monday is a versatile work management platform that helps teams streamline workflows, track projects, and collaborate efficiently.

It offers customizable dashboards, automation, and integrations to enhance productivity across various industries.

By integrating OX Security with Monday.com, teams can seamlessly incorporate security insights into their existing workflows.

This integration enables the following:

* automatic tracking of security issues
* real-time updates on vulnerabilities
* visibility into security risks

With OX Security’s capabilities, development and security teams can prioritize and address threats directly from their Monday.com workspace, ensuring a more secure and efficient software development process.

{% hint style="info" %}
OX Security supports only working with Monday boards.
{% endhint %}

## Prerequisites

* Monday account.

## Getting Monday Token

1. Log in to your Monday.com account.
2. Click your profile picture in the top-right corner and select **Administration**.
3. In the left pane, select **Connections** and then in the right pane select the **API** tab.
4. In the **API Token** section, click **Generate** and then **Copy**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ce1caf7b49a4cc8ed67bb3b36cee3c546c1a994e%2FMonday_token2.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Copy the token and store it in a different location. After closing this dialog you cannot see it again.

## Connecting to Monday

1. In the **OX app**, go to **Connectors** and search for Monday.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9bab919c6598b5f91f9f7206484bd63d3475f0d9%2FMonday_icon.png?alt=media" alt="" width="200"><figcaption></figcaption></figure>

1. Select **Monday**. The **Configure your Monday credentials** dialog appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dda6fe8629e71dd0523f2447fc463cabb7060f22%2FMonday_connecting.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Select **CONNECT**. The Monday connector is configured.

## Adding Monday Tickets

After establishing the connection with Monday, you can add Monday tickets to tasks and issues in OX using one of the following methods:

* Adding a new ticket to an issue, or bulk of issues.
* Adding a new ticket as a scheduled task using workflows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3d658a09e9057500ad4c0b219daeec4d76d30bec%2FMonday_WF.png?alt=media" alt="" width="203"><figcaption></figcaption></figure>

**To add a new Monday ticket in OX:**

1. In the **Issues** page, identify and select the issue for which you want to add a new ticket in Monday.
2. Select the Monday icon.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f6efe34061f6ab5c3bf48bb25df4412c73415390%2FMonday_icon_issues.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Set the ticket details in the **Create Monday Ticket** dialog and select **CREATE TICKET**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8a765feae87213089018ae0021b5b617df318b3e%2FMonday_Ticket_issue.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter       | Description                                               |
| --------------- | --------------------------------------------------------- |
| **Title**       | The title of the ticket that describes the problem/issue. |
| **Workspace**   | The name of the workspace, as it's defined in Monday.     |
| **Board**       | The Monday board associated with this ticket.             |
| **Status**      | The status of the ticket.                                 |
| **Assigned To** | Set the team member who will work on the ticket.          |

The new ticket appears in Monday.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8dac8492b700cda46fe0fc1822545f66e698dc07%2FMonday_tickets_in_Monday.png?alt=media" alt=""><figcaption></figcaption></figure>
