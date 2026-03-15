# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/how-to-scan-a-personal-gitlab-project.md

# How to Scan a Personal GitLab Project

**Table of contents:**

* [Step 1. Create a new group in GitLab](#step-1-create-a-new-group-in-gitlab)
* [Step 2. Transfer your personal projects to the newly created group](#step-2-transfer-your-personal-projects-to-the-newly-created-group)
* [Step 3. Connect the group to Aikido](#step-3-connect-the-group-to-aikido)

## How to scan a personal GitLab project

At this moment, Aikido only allows to scan projects which are linked to a group. Projects linked to your GitLab user are currently not supported.\
​\
If you'd like to enable code scanning on your personal GitLab projects, we recommend you create a personal group and transfer the projects there. To accomplish this, we recommend you follow the steps below.

#### Step 1. Create a new group in GitLab <a href="#step-1-create-a-new-group-in-gitlab" id="step-1-create-a-new-group-in-gitlab"></a>

Login to your GitLab account, navigate to "Groups" in the left-hand side navigation and click on "New group". Follow the steps to create a group.

![GitLab Groups dashboard with options to explore, create, and search for groups.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f4c4a2bdcdce6e2d188891de29bc58e0934b91ca%2Fhow-to-scan-a-personal-gitlab-project_6f7e4107-4a83-44b6-ae5c-f858a3b4ac78.png?alt=media)

#### Step 2. Transfer your personal projects to the newly created group <a href="#step-2-transfer-your-personal-projects-to-the-newly-created-group" id="step-2-transfer-your-personal-projects-to-the-newly-created-group"></a>

Now, you can transfer your personal projects to the newly created group. To do this, navigate to the project's detail page and go to it's "General settings", which you can see in the left-hand side navigation. At the bottom you can expand the "Advanced" settings section.

![GitLab project general settings page showing configuration options for visibility, badges, and advanced features.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-14b6a6ad756dfffbc60ca773e3ab093ab9ca330a%2Fhow-to-scan-a-personal-gitlab-project_12819150-cf77-456d-95fc-21fcad9de857.png?alt=media)

At the bottom of this section, you can transfer this project to a different namespace.\
​

![GitLab project settings for changing repository path and transferring project namespace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-bef13254ff0392a1d9039e4ccd975bbcef6d2927%2Fhow-to-scan-a-personal-gitlab-project_968e99ba-c1be-4ccd-ac56-e243c658c35f.png?alt=media)

#### Step 3. Connect the group to Aikido <a href="#step-3-connect-the-group-to-aikido" id="step-3-connect-the-group-to-aikido"></a>

Now that you transferred your new project to the new namespace aka "group", you can connect Aikido to that group and allow read-only acces to start scanning for vulnerabilities.\
​\
In Aikido, select the Group dropdown picker in the left-hand side navigation, and click on "Add another workspace".

![Workspace menu showing "aikido-dev" on Pro plan with team and settings options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-36973a8dc3ab1cda5a314aebebf1c8f7b68a7a83%2Fhow-to-scan-a-personal-gitlab-project_75339182-b6b1-4078-a9d1-e7d549c7bdc2.png?alt=media)

You will now go through the flow of connecting your newly created GitLab group to Aikido to grant read-only access to your personal projects.
