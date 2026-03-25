# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/jira/page-1.md

# Adding comments to Jira tickets

You can configure OX platform to automatically add comments to a variety of ticketing systems when specific actions are taken on OX issues. This ensures that developers working in this system are informed of changes made by security teams without needing direct communication.

When enabled, OX adds the comment directly to the linked ticket automatically, no manual entry is required.

You can choose which actions should trigger comments and enable them individually. This allows teams to control the level of detail shown in the ticketing system and avoid unnecessary noise.

The following ticketing systems are supported:

* Jira
* Azure Boards
* Asana
* Monday
* ServiceNow

**To add comments automatically:**

1. Go to **Settings > TICKETING AND MESSAGING**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d88738e022959cd80dc7619cf71278b3dd7dccb5%2FComments.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

2\. Enable the options that you want, as follows:

* **The issue is resolved:** The issue was resolved or reopened in the OX platform.
* **The issue's severity changes:** The severity definition of this issue was changed.
* **The issue is excluded:** The issue was excluded from the security scan, and from now on this issue will not be reported.
* **The issue is no longer available:** The issue was not identified in a specific scan.
* **The issue is reported as false positive:** The issue was manually defined in the OX platform as false positive, and a comment about it is automatically generated in the ticket linked to this issue.
* **A comment was added to the OX issue:** A new comment is manually added to an issue in the OX platform, and the same comment is automatically added to the ticket.
