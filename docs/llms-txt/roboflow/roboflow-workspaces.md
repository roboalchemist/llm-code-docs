# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workspaces/roboflow-workspaces.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workspaces/roboflow-workspaces.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workspaces/roboflow-workspaces.md

# Source: https://docs.roboflow.com/workspaces/roboflow-workspaces.md

# Create a Workspace

All computer vision projects in Roboflow belong to a workspace. Creating a new workspace allows you to invite a separate group of teammates to collaborate on projects, and every workspace is billed separately with its own resources and API keys.

### Create a New Workspace

After log in, to create a new Workspace, click on the name of your workspace in the left side panel. Then, click the "+" icon:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-da3bd2244ab7632930075b719caadb4663b4c1d8%2FScreenshot%202024-07-10%20at%2009.56.17.png?alt=media" alt=""><figcaption></figcaption></figure>

### Workspace Setup

When you create a new Workspace, you need to choose a plan for the Workspace. To learn more about the available plans you can check out our [Pricing](https://roboflow.com/pricing) page.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-48e871fadba4922f3449e325f8b7da0884677bdf%2FScreenshot%202025-02-17%20at%2015.43.08.png?alt=media" alt="Workspace Creation Menu: Workspace Usage Type Selection"><figcaption><p>Create a workspace and select a plan to get started with Roboflow.</p></figcaption></figure>

The selected Workspace Name will also become part of the `workspace ID`

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-1c8dbfc03413269031b54b5dd5936c22f4347851%2FScreenshot%202025-02-17%20at%2015.44.53.png?alt=media" alt="Workspace Creation Menu: Selecting a Workspace Name"><figcaption><p>If your organization has workspaces available to join, you will see them listed.</p></figcaption></figure>

Enter emails, comma-separated, for individuals to receive workspace invitations with specified roles (`Admin` or `Labeler` roles)

* Select `Back` to change the Workspace Name or Usage Type
* Select `Skip` to skip team invitations.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-eb8c8e6cb232ea62f6f7d4768e4daf7a1c9e56cd%2FScreenshot%202025-02-17%20at%2015.47.21.png?alt=media" alt="Workspace Invitations: Workspace Creation Menu"><figcaption><p>Invite teammates to collaborate on projects in your workspace.</p></figcaption></figure>

### **Renaming Workspaces**

Click the pencil-shaped icon next to the workspace name on the main landing page for the workspace.

Enter the new workspace name and click "Save"

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2ba39395c368863b916245b16474690c700404f1%2Fimage.png?alt=media" alt="Renaming a workspace"><figcaption><p>Renaming a workspace</p></figcaption></figure>

***Note:*****&#x20;Renaming a workspace will update the workspace ID.**

### **Workspace Settings**

Select `Settings` in the left sidebar to open the Workspace Settings menu.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5649d2323354ec0d1ee5a5fa5a22c690aeb47928%2FScreenshot%202025-04-09%20at%2010.07.09.png?alt=media" alt=""><figcaption><p>Workspace Settings Menu</p></figcaption></figure>

* **Plan and Billing** - View your current workspace plan, how to add Billing Info, and more workspace upgrade options
* **Usage** - Workspace Features and Usage (all-time and by month)
  * Team Members, Projects, Source Images, Generated Images, Inference Usage (view and download charts)
* **Members** - View workspace members, member roles, status of workspace invitations
* **Roboflow API** - View, copy and revoke Public and Private API Keys
* **Third Party Keys** - Integrations with Microsoft Azure, Amazon Web Services (AWS), Google Cloud Platforms (GCP) and OpenAI
* **Rename Workspace** - Give the workspace a new name. This will update the `workspace ID`
* **Delete Workspace** - This action is irreversible after confirming deletion. Proceed with caution.
* **Transfer of Ownership** - It is not possible to transfer the creator role. The creator role is a signatory role that is equivalent to an admin but cannot be removed. To have a new designated admin, have the creator of the workspace promote a user to admin or keep the creator email active.

### Deleting a Workspace

Once you are finished with your projects in Roboflow, you may delete your workspace. Deleting a workspace is a permanent action. To delete your workspace, click on the workspace settings menu and click **Delete Workspace**. As shown below, you will be required to confirm this action - deletion **cannot be reversed**.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-94437f35c3eabbb1d84a09eac36edc8ccc0a1b17%2FScreenshot%202025-04-09%20at%2010.07.25.png?alt=media" alt=""><figcaption><p>Type in the name of the workspace to confirm deletion.</p></figcaption></figure>
