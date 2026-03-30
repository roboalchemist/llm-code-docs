# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/workspace-settings/connecting-to-remote-repositories.md

# Context Enhancement

### What is Connection?

Connection is a feature within **Tabnine Personalization**, created to improve the relevance and precision of AI-powered code suggestions. By making Tabnine aware of remote/external code repositories within the organization – beyond just the developer’s local environment – Connection provides a broader scope of contextual code examples.

Utilizing a Global RAG index, Connection retrieves relevant code snippets from these remote sources.

## Enabling Remote Codebase Awareness in Tabnine Enterprise

***(connection to software repository for global code awareness)***

{% hint style="warning" %}
Codebase awareness is available only for Tabnine Chat, and not for Code Completions.
{% endhint %}

{% hint style="info" %}
Note:

1. Connection to the remote codebase is ***only*** available if Tabnine Context is enabled.
2. If this feature is disabled, contact your account manager at Tabnine to enable it.
   {% endhint %}

### Setting Remote Git Providers

To start, an admin should go to the **Admin Console.** From there enter **⚙ Settings**, then select **Personalization** (in older versions, from Settings go to Workspace).

If this feature is disabled, contact your Tabnine account manager to enable it.

Once enabled, the admin can link Connection to external remote repositories.

Next, the admin should define Connection to their git providers (using SSH Key or HTTPS credentials). Finally, the admin can add repositories using these connection methods.

Start with an empty state. Enable the Connection feature in order to connect to a provider.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-458e50e60588559d99ddee6bb641f6cc40c45b4b%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Connection with an SSH Key

Next, set Connection to a git provider with an SSH key, which you can generate in the window:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-51668abd3449643f66303e1488ea5150823c79cd%2Fimage.png?alt=media" alt=""><figcaption><p>Generating an SSH key in Tabnine's Admin Console</p></figcaption></figure>

The admin then copies the SSH key and adds it to their git provider. For example: [GitHub](https://github.com/settings/keys), [GitLab](https://gitlab.com/-/user_settings/ssh_keys), and [Bitbucket](https://bitbucket.org/account/settings/ssh-keys/).

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-1c44bbd5405fcb922402738b2354a64d46cae9e1%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Connection with HTTPS

Alternatively, you can set Connection to a git provider via HTTPS using PTA (personal access tokens) from the git providers:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a27a74403fb4a13bde9bcbb2fb2c3ebb866edc28%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Managing Connected Repositories

#### Adding Repositories

Before you add your first git repo, you will see a gray window. There, click the blue button reading <mark style="background-color:blue;">**Connect to a git repository**</mark>.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-cedea06785f036e4c055c24d06e94fe828fb3d93%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Again, you can either use an SSH Key or HTTPS.

Either way, paste the link to the repo.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ed3e67e183eab69c038f011f9d531e391245afb1%2Fimage.png?alt=media" alt=""><figcaption><p>Connection with SSH</p></figcaption></figure>

With HTTPS, also add the connection name under **Select HTTPS Credentials**.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-684a8312b80f3622b4f048c66c4e5c4d66f61896%2Fimage.png?alt=media" alt=""><figcaption><p>Connection with HTTPS</p></figcaption></figure>

For both SSH and HTTPS, next hit <mark style="background-color:blue;">**Connect**</mark>.

You will see the following message in the lower righthand corner of the screen when a repo is successfully added:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-319f08406213ac67401fa2430c857030d842c464%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Once you already have one git connected, the window will show the list of all available gits as well as a blue <mark style="background-color:blue;">**+ Connect repository**</mark> button.

Press that button, then follow the same process as above.

Optionally, you can add a link pattern for source code navigation.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-44dbbfba3ff5b7b57bbffc57e5184c34537097d4%2Fimage%20(71).png?alt=media" alt=""><figcaption></figcaption></figure>

#### Removing & Editing

To edit providers, select the blue <mark style="color:blue;">Edit git providers</mark> text to the right above the <mark style="background-color:blue;">**Connect to a git repository**</mark> windo&#x77;**.**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9ee73b66c0be4022ac9c1d1cce236b5aed758246%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Alternatively, you can also delete current repositories. Once done, the following message will display in the lower righthand corner of the screen:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e237741a88fa15451fb83a351e03d38675ff9a7e%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### View Status

There might be a delay beforehand, where a status message will read <mark style="color:blue;">Queued for indexing</mark>. Indexing might take a while, possibly up to an hour.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-4ffac2c989f05f38089ee76a73ae98e5458c1cc3%2FPixelated%20queued.png?alt=media" alt=""><figcaption></figcaption></figure>

There will be one of four statuses: "<mark style="color:blue;">Pending</mark>," "In process," "Successful," or "Failed."

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c70cf41d23a708ddfbc9d7aa3e1a5e38f7469c11%2Fimage.png?alt=media" alt=""><figcaption><p>Indexing might take a few minutes</p></figcaption></figure>
