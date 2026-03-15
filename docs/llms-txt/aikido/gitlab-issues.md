# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/gitlab-issues.md

# GitLab Issues

*📋 Setting up automated task creation in GitLab Issues*

Aikido can connect to GitLab so that you can create issues for security findings found through Aikido. For each of the findings in the 'Feed' of Aikido, a GitLab issue can be created, and linked.

You will be able to follow along in the Feed, to whom the ticket is assigned.

### 1. Set up integration <a href="#id-1-set-up-integration" id="id-1-set-up-integration"></a>

Go to <https://app.aikido.dev/settings/integrations> and scroll down to the 'Task trackers' section.

![GitLab integration for tracking and managing security issues; connect to create GitLab issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-54d911143299bee5c0b06583d2ee2b2b74fe8b81%2Fgitlab-issues_315ed60c-bb33-46de-8437-b67458cb6851.png?alt=media)

Click on 'Connect'

![GitLab authorization prompt for issue-tracking, awaiting user permission to proceed.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-418cc61c9ab0094dbbe886cbb7f229bb39fa69b7%2Fgitlab-issues_bd90ccd9-fdd9-46b8-b552-d28145c3f0d7.png?alt=media)

Click on 'Authorize GitLab'

![Authorization prompt for Aikido Issues to access GitLab user's API and account data.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ff8dfbbb15b3bae70630a8967baed6cc944511ab%2Fgitlab-issues_febb5b75-7e73-4a47-8d71-e576826a89d8.png?alt=media)

And select a 'Group' for which you want to activate the integration.

Click 'Save' and you're connected.

![GitLab issue-tracking integration status: Connected.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1c60ea2ab03a0fa5921b27c964033ea10d136dcc%2Fgitlab-issues_902c3217-4139-4079-9490-3f2059fbbdab.png?alt=media)

### 2. Create a GitLab issue for a finding, inside Aikido <a href="#id-2-create-a-gitlab-issue-for-a-finding-inside-aikido" id="id-2-create-a-gitlab-issue-for-a-finding-inside-aikido"></a>

Go to the [Feed](https://app.aikido.dev/queue), and go to the security finding of choice. In the column 'Assignee', you will find the ability to assign a GitLab Issue to someone.

![Assign a new task owner by clicking the plus icon.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1c4a80c473662a23eb9f82a9c9f060066c532a94%2Fgitlab-issues_cd3756a0-ebf2-4903-9d80-6f172e7d880d.png?alt=media)

When you click on it, a popup will open.

![Task creation form for assigning and summarizing a security fix in GitLab.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c7540129cf2ae91a67956a6ec43d8047bcac2d9f%2Fgitlab-issues_2d25f8b3-11d3-4b4a-b25f-100095e4966a.png?alt=media)

When creating the Issue Task, this will be made clear in the UI of Aikido

![Open task assigned to user "roelanddel" displayed in a project management dashboard.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-1ac15a6f39e427c476b18d446bdf0d794c4fe96e%2Fgitlab-issues_a34498f0-206a-444d-ae0b-2a8992cb8ab7.png?alt=media)

You're done!

### &#x20;<a href="#set-up-gitlab-issues-integration" id="set-up-gitlab-issues-integration"></a>

***
