# Source: https://help.aikido.dev/getting-started/task-management-systems/all-supported-task-trackers/gitlab-issues-self-managed.md

# GitLab Issues Self-Managed

*📋 Setting up automated task creation in GitLab Issues*

Aikido can connect to GitLab Self-Managed (On-prem) so that you can create issues for security findings found through Aikido. For each of the findings in the 'Feed' of Aikido, a GitLab issue can be created, and linked.

You will be able to follow along in the Feed, to whom the ticket is assigned.

### 1. Set up integration <a href="#id-1-set-up-integration" id="id-1-set-up-integration"></a>

**Step 1.** Go to <https://app.aikido.dev/settings/integrations> and scroll down to the 'Task trackers' section.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnuPGgMepHUcoOrR89krm%2Fimage.png?alt=media&#x26;token=8fcfb609-c48d-40ba-9755-fdefa96993d7" alt="" width="375"><figcaption></figcaption></figure>

**Step 2.** Click on 'Connect' and fill in the serve base URL, the PAT and Group ID

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fw3ii38ZrQSJ5McEb2QrC%2Fimage.png?alt=media&#x26;token=f1aa66e5-d118-4b60-9fe0-bcc995fa3ff7" alt="" width="373"><figcaption></figcaption></figure>

**Step 3.** Click 'Save' and you're connected. Close the modal and you will redirected to the settings page.

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
