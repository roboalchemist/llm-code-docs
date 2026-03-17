# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workflows/manage-workflow-versions.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workflows/manage-workflow-versions.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workflows/manage-workflow-versions.md

# Source: https://docs.roboflow.com/workflows/manage-workflow-versions.md

# Manage Workflow Versions

{% hint style="info" %}
Workflow Versions is a **premium** feature. Without it, previous versions cannot be restored.

For up-to-date information on our plans and their associated features, see our [pricing page](https://roboflow.com/pricing).
{% endhint %}

Every time you save a Workflow, a new version is saved in your Workflow Version History.

The Version History for a Workflow stores every saved change to the Workflow.

### See Versions

To see Versions of your Workflow, click the clock icon in the right sidebar of the Workflow editor. A panel will open up that shows all saved changes.

The most recent saved version will be marked as Live. This is the Workflow that will run in production when you run the Workflow.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c89d865c759d08525d6b3bf219174e01d205d62d%2FScreenshot%202025-06-27%20at%2009.17.15.png?alt=media" alt=""><figcaption></figcaption></figure>

### Set a Version Name

You can set names for versions in your Workflow Version History. To name a version, click the three dots next to a version name then click "Rename":

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ccc92da0b7638b522302fdf428fe85dc3e16318b%2FScreenshot%202025-06-27%20at%2009.22.39.png?alt=media" alt=""><figcaption></figcaption></figure>

You can then specify a name for your Workflow version:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-542a2631dd0be4f53f62356c748852bfa0b3ada3%2FScreenshot%202025-06-27%20at%2009.23.04.png?alt=media" alt=""><figcaption></figcaption></figure>

The version name will then be updated:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-08eca189cd90b37c5151b8f05447d8be2239f7af%2FScreenshot%202025-06-27%20at%2009.23.36.png?alt=media" alt=""><figcaption></figcaption></figure>

### Roll Back to a Previous Version

You can roll back to a previous version of a Workflow at any time.

To roll back to a previous version, click the three dots next to the name of a Workflow then click "Restore":

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-8a30af522badf5ee61919e1e280c9e9338b37bb3%2FScreenshot%202025-06-27%20at%2009.24.56.png?alt=media" alt=""><figcaption></figcaption></figure>

The Workflow Version will then appear in your editor. You will need to click the "Save" button to save your changes:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-7a4b10181d8363c42340008ea8ff3e4b082a6f2d%2FScreenshot%202025-06-27%20at%2009.26.08.png?alt=media" alt=""><figcaption></figcaption></figure>

When you press Save, a new version of your Workflow will be created with the changes you rolled back to. This will then be made the Live version of your Workflow.
