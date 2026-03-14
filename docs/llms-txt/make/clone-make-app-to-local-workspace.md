# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/clone-make-app-to-local-workspace.md

# Clone Make app to local workspace

{% hint style="warning" %}
Please be advised that this feature is in beta so it may encounter occasional bugs or inconsistencies.
{% endhint %}

To start the development of an app in a local directory or git repository, or start tracking changes in your app, you need to clone the Make app to the local workspace.

## Step 1: Open the local folder

Open the folder where you intend to store the app in Visual Studio Code.

Select the section that corresponds to your development setup:

* 'Local Directory' if you are working directly on your computer's file system
* 'Git Repository' if you are using version control with Git

The 'Git Repository' section describes the development in the Git repository using the [GitHub Desktop](https://desktop.github.com/) app. However, any preferred [GUI tool](https://git-scm.com/downloads/guis) or CLI can be used.

<details>

<summary>Local directory</summary>

1. Open Visual Studio Code and navigate to **File > Open Folder.**

<img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-860dbd4bdd2c9dd2e279da021f058980b33f7592%2FScreenshot%202024-07-15%20at%2015.23.42.png?alt=media" alt="" data-size="original">

2. In the file manager, select the folder where the app should be cloned.
3. In the pop-up window, click "Yes, I trust the authors" option.

<img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7fbe65184a1169b927d56ffa2b9f4f362d22f0ba%2FScreenshot%202024-07-15%20at%2015.28.06.png?alt=media" alt="" data-size="original">

The current local directory in Visual Studio is set.

</details>

<details>

<summary>Git repository using the GitHub Desktop app</summary>

1. Navigate to the GitHub Desktop app and open the repository where you intend to store the app.
2. Click **Open in Visual Studio Code**.

<img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-83315327d1596d463f20c7132a1484f1e0f5bb48%2FScreenshot%202024-07-16%20at%2010.05.59%20(1).png?alt=media" alt="" data-size="original">

3. In the pop-up window, click "Yes, I trust the authors" option.

<img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-a92fda5129e455400340509b86c2111cdf050ab0%2FScreenshot%202024-05-09%20at%2021.25.32.png?alt=media" alt="Dialog window requesting the confirmation of trusting the authors of the code" data-size="original">

The current repository in Visual Studio is set.

</details>

## Step 2: Clone the app to the local folder

Once the repository in Visual Studio is set, you can proceed to cloning the app to the local folder.

{% stepper %}
{% step %}
In the opened window of Visual Studio Code, go to the Make Apps Editor and right-click the app you wish to save to your repository. Select **Clone to Local Folder (beta)**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-13f8e0b8055e02ed7954c2a8b03e6fb47898a26a%2FScreenshot%202024-05-09%20at%207.20.45.png?alt=media" alt="" width="260"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Read the text in the dialog window and confirm reading by clicking **Continue**.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-575dc061e5d6cb46b61d5b9ef3af9a84630f248b%2FScreenshot%202024-05-09%20at%207.22.01.png?alt=media" alt="" width="404"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Enter the workspace subdirectory name where the app should be cloned to. \
\
If the subdirectory doesn't exist yet, it will be created. The default subdirectory is set to `src`. Click **Enter**.

If you are going to store more than one app in the repository, you can create a subfolder by using the `src/app-name` path, where the `app-name` is the name of the app folder.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-8e686f536027c1448df6e0b867c73e05fe92d470%2FScreenshot%202024-07-16%20at%2010.10.10.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% endstep %}

{% step %}
A dialog window asking whether[ common data](https://docs.make.com/apps/app-structure/connections#common-data) should be included or not will pop up.

* **Exclude (more secure)** - Select, if your app contains sensitive data, such as Client ID and Secret. Common data will not be stored in your local workspace or a repository.
* **Include (for advanced users only) -** Select, if you want to store the common data in your local workspace or a repository. Be aware that storing common data outside of Make could potentially expose the app to vulnerabilities.
  {% endstep %}
  {% endstepper %}

The app is now cloned to the local folder.

## Step 3: Versioning the local app

Versioning is only available if you are using version control with Git.

The following steps describe the development in the Git repository using the [GitHub Desktop](https://desktop.github.com/) app as an example.

{% hint style="info" %}
The `.secrets` file with your Make API keys is only stored in the local folder. By default, the file is excluded from the git versioning.
{% endhint %}

To properly start the versioning of your app in the Git repository:

{% stepper %}
{% step %}
Go to the GitHub Desktop app and open the repository where you deployed the current version of your app. You will see a list of new files.
{% endstep %}

{% step %}
Enter the Summary of the commit and click **Commit to main**. Or optionally, click **Publish branch**.
{% endstep %}

{% step %}
Optionally, click **Publish branch**.
{% endstep %}
{% endstepper %}

The first version of your app is logged. Every new change or a new component in the app will be considered a new change.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c0848c523a986a6ea4955488d862246b2ddf6763%2FScreenshot%202024-07-16%20at%2010.18.34.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
