# Source: https://docs.tabnine.com/main/welcome/readme/personalization/connection-global-codebase-awareness.md

# Connection: Global Codebase Awareness

What is Connection?

Connection (Global RAG) [personalizes](https://docs.tabnine.com/main/welcome/readme/personalization) Tabnine to your organization’s code by extending the available context for [Tabnine Chat ](https://docs.tabnine.com/main/getting-started/tabnine-chat)to include remote/external code repositories, even if they’re not part of the local IDE workspace.

This enhances AI code suggestions, making them more accurate and relevant to the organization.

## Why is this important?

In many cases, the relevant context for Tabnine is located in external repositories that are not included in the current project.

For example, users may need specific code that resides outside the IDE or suggestions that rely on patterns from the remote codebase.

## Who has access to the Connection feature?

The Connection feature is available to enterprise customers in all deployments.

To enable this feature for your team, please contact your account manager.

## How to enable this feature:

The Enterprise team admin manages the connected repositories.\
The admin can establish connections to Git providers using:

* SSH: By configuring Tabnine’s SSH key
* HTTPS: By using access tokens from the Git providers

[Learn more](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/workspace-settings/connecting-to-remote-repositories).

## How does the end user work with connected repositories?

### Context Scoping

Specify which repositories are relevant for Tabnine to use as context. Learn more about [Context Scoping](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping).

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-77d0708067af70d55c1abb77c463a8c1138b3c21%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Get Answers based on References from External Repositories

Tabnine Chat may generate answers using context from remote repositories. The exact references used will appear in the "References" section.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d35843f160d570e94dc4036847591caafc284eb0%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Navigate to Resource

Quickly access relevant remote code references by clicking the corresponding link. The browser will open the original source code directly within the connected Git provider.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-87b77a40d1f0c61261ac812ac078c40b2ce0ed53%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Which Git providers are supported?

#### Supported providers:

* GitHub
* GitLab
* Bitbucket

{% hint style="info" %}
**Note:**

Both cloud and self-hosted installations are supported, provided Tabnine servers can connect to the Git providers.
{% endhint %}

#### For other providers:

* Indexing and retrieving chat answers from external repositories generally works for most standard Git providers.
* Navigating to external repositories' references may not work consistently due to variations in URL patterns.

### Which users have access to context from the external repository?

Connections are managed at the team level.

Each user only has access to the repositories that are connected to their specific team.

### Which files are being indexed?

[Learn more](https://docs.tabnine.com/main/welcome/readme/tabnines-personalization-in-depth#what-files-are-being-indexed)

### Indexing Process and RAG Index

* Your connected repositories are cloned to Tabnine servers for indexing and are deleted immediately after indexing is complete.
* The **RAG index** is securely retained on Tabnine servers and remains private.
* A periodic background process checks for updates in the connected repositories and refreshes the corresponding index when needed.
* This update process can take up to **one hour**.

Read more on the [Index Lifecycle](https://docs.tabnine.com/main/welcome/readme/tabnines-personalization-in-depth#index-life-cycle).

#### Perforce

{% hint style="info" %}
This is currently in 'preview' mode. To get access, contact <support@tabnine.com>.
{% endhint %}

You can connect Perforce depots for global connection indexing.

On the **Context enhancement** page, scroll down to **Connect external Perforce depots**.

Press <mark style="background-color:blue;">**Add depot**</mark>.

Enter the depot path below and select an available Perforce server.

Then click <mark style="background-color:blue;">**Connect**</mark>.

Indexing might take a few minutes. When finished, the Perforce depot will be available in your context engine.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a3395e284d5e7ed3fcd701a60d071018e7388680%2FScreenshot%202025-04-10%20at%2010.49.46.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fd3c50ed077c8a82f4028d0ba41525831525b5dc%2FPerforce%20activate.gif?alt=media" alt=""><figcaption></figcaption></figure>

To remove the depot, press the X. You can also change the depot path by clicking the edit icon.
