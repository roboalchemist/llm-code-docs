# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-gitlab-account-to-aikido.md

# Connect GitLab Account

**Table of contents:**

* [Step 1. Logging in using GitLab](#step-1-logging-in-using-gitlab)
* [Step 2. Creating a workspace, join an existing workspace or create a demo](#step-2-creating-a-workspace-join-an-existing-workspace-or-create-a-demo)
* [Step 3. Connect a GitLab group to Aikido](#step-3-connect-a-gitlab-group-to-aikido)
* [Step 4. Selecting groups & selecting repos](#step-4-selecting-groups--selecting-repos)
* [5. Checking results](#5-checking-results)

## Connect GitLab account to Aikido

Aikido requests read-only access to your GitLab group to analyze your projects. After analysis, your code is always wiped from the system.

***Important before you start***

* If your GitLab is behind a firewall, we have a [list of Static IPs](https://help.aikido.dev/en/articles/8731261-allowing-ip-addresses-for-code-scanning) you can allowlist.
* The person who sets up the account needs to have access rights both to the GitLab instance **and** GitLab group\*.

{% hint style="warning" %}
\*An Aikido workspace always maps to a single GitLab group. We recommend to connect Aikido to a top-level GitLab group (i.e. root group) that contains all subgroups. If no top-level group exists, you can create a separate workspace for each GitLab group. This option is available after creating the first workspace via the top-left dropdown “Add another workspace”.
{% endhint %}

{% hint style="success" %}
**Repositories not linked to a group**, but linked to just your user can currently not be scanned. If you do have personal repositories which you'd like to have scanned, we recommend to create a personal group, or transfer them to a group you own.
{% endhint %}

#### Step 1. Logging in using GitLab <a href="#step-1-logging-in-using-gitlab" id="step-1-logging-in-using-gitlab"></a>

To get started, navigate to <https://app.aikido.dev> and log in with GitLab. This will look like the screenshot below. Here, Aikido only requests access to your identity on GitLab and the associated email address.

![Aikido Security requests access to read personal information from a GitLab account.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-55ac731f87c11d27462aee1d900212bfddef8b65%2Fconnect-gitlab-account-to-aikido_dd58925f-aa33-4b89-9e02-bd75cc1009ad.png?alt=media)

#### Step 2. Creating a workspace, join an existing workspace or create a demo <a href="#step-2-creating-a-workspace-join-an-existing-workspace-or-create-a-demo" id="step-2-creating-a-workspace-join-an-existing-workspace-or-create-a-demo"></a>

After authorizing Aikido to read your personal GitLab information you get the following screen.

![gitlab\_signup](https://ucarecdn.com/143adfc1-c0c6-4c71-8a3d-1bed03e7ca6a/)

On this page you can do one of 3 things:

* **Create a new workspace:** select this option if you want to connect a GitLab group to Aikido and start scanning your code repositories and clouds.
* **Join your team:** select this option if someone in your organization already connected a GitLab group to Aikido, and you'd like to get access to it
* **Use sample repo:** want to have a sneak peak of what Aikido looks like and what it can do? Create a demo account to get a taste of Aikido. You can always connect your GitLab group at a later moment

#### Step 3. Connect a GitLab group to Aikido <a href="#step-3-connect-a-gitlab-group-to-aikido" id="step-3-connect-a-gitlab-group-to-aikido"></a>

If you would like to create a new workspace, Aikido will need **read-only access** to your projects and groups. We will therefore redirect you back to GitLab so you can authorize Aikido.

**Note.** This does *not* give access to the actual repos yet. Selecting which ones you want to have scanned is in the step after this one.

![Aikido Security requests GitLab read access and user information authorization.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-99cd8b807b1832f7b8eff5bf78e3e751cd24869b%2Fconnect-gitlab-account-to-aikido_b461947a-bf2e-4a4e-936a-84efb59a1f48.png?alt=media)

#### Step 4. Selecting groups & selecting repos <a href="#step-4-selecting-groups--selecting-repos" id="step-4-selecting-groups--selecting-repos"></a>

After authorizing Aikido to read your groups and projects, you can select which group you'd like to connect to Aikido.

**Note:** Aikido will include any subgroups of the GitLab group you selected in the workspace

![Select a group to connect to Aikido as a workspace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f10225612eaf70ef96669b6069de25acf121f121%2Fconnect-gitlab-account-to-aikido_f0dad506-48d9-4216-a102-80051d6019b3.png?alt=media)

​After selecting the groups of choice, you can choose which repositories you want to give access to.

![Select repositories for monitoring security with Aikido's cloud and repo management tool.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6caceaad1872fc4aac3d6652b2d7c61245144bf5%2Fconnect-gitlab-account-to-aikido_b7b4ee31-ffac-48a6-8c1e-282fe833ca81.png?alt=media)

#### 5. Checking results <a href="#id-5-checking-results" id="id-5-checking-results"></a>

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in!
