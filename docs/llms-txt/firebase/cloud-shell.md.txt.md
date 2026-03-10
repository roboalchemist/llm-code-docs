# Source: https://firebase.google.com/docs/cloud-shell.md.txt

# Cloud Shell in the Firebase console

<br />

Cloud Shell is an interactive shell environment that lets
you manage your projects and resources from your web browser. You can access
Cloud Shell directly from the [Firebase console](https://console.firebase.google.com/),
giving you access to the Firebase CLI and other command-line tools without
needing to install them on your local machine.

## Access Cloud Shell in the Firebase console

To access Cloud Shell from the Firebase console, click
**Cloud Shell** in the right menu.

The terminal opens in a pane at the bottom of the screen. To adjust your
workspace, you can maximize the terminal window or open it in a new window.

## Use pre-installed tools in Cloud Shell

Command-line tools, like the
[Firebase CLI](https://firebase.google.com/docs/cli),
[Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli),
and
[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud),
come pre-installed in Cloud Shell. Plus, they're already authenticated with
the Google Account you used to log into the Firebase console.
Cloud Shell also includes Node.js, Python, and other industry-standard
tools (view a
[list of all pre-installed tools](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works#tools)).

These pre-installed tools can be helpful when you don't want to install or
authenticate tools on your local machine.

After [providing Cloud Shell with access to your files](https://firebase.google.com/docs/cloud-shell#manage-files), you
can run commands to interact with those files directly from the Cloud Shell
terminal.

### Use the Firebase CLI

Manage your Firebase and Google Cloud resources using standard terminal
commands. For example, you can deploy Firebase Hosting sites or manage
Firebase App Hosting backends, and more.

The following are some common Firebase CLI commands:

| Command | Description |
|---|---|
| `firebase login` | Cloud Shell automatically authenticates you when you open it in the Firebase console, but you can use this command to switch accounts. |
| `firebase init` | Establish the current directory as a Firebase project directory, linking it to a specific Firebase project. |
| `firebase deploy` | Deploy code and assets to your Firebase project. |
| `firebase --help` | View a list of all available Firebase commands. |

## Install the Firebase extension for Gemini CLI

You can extend the capabilities of Gemini CLI in
Cloud Shell by installing extensions. For example, you can install the
Firebase extension to help you manage
your Firebase projects and get insights into your resources:

    gemini extensions install https://github.com/gemini-cli-extensions/firebase

With the Firebase extension, you can use Gemini to understand
and manage your deployments, monitor project health, and more. For more
information about specific commands, view the
[extension documentation](https://github.com/gemini-cli-extensions/firebase).

## Use the Cloud Shell Editor

Cloud Shell comes with a built-in code editor based on Code OSS. With
the Cloud Shell Editor, you can browse file directories and view and edit
files in your Cloud Shell environment with an in-browser editor. For example,
if you ran `firebase init`, you could switch to the Cloud Shell Editor
to view and modify your `firebase.json` configuration file.

To open the Cloud Shell Editor, click **Open Editor** on the toolbar
of the Cloud Shell window.

[Learn more about the Cloud Shell Editor](https://docs.cloud.google.com/shell/docs/editor-overview).

> [!NOTE]
> **Note:** Gemini Code Assist in the Cloud Shell Editor is subject to its own free tier limits and does not use your prompts or its responses as data to train its models.

## Customize your Cloud Shell environment

You can customize your Cloud Shell environment to your preferences. To adjust
terminal settings, click
**Settings**. In this
menu, you can set your preferences for theme, font type and size, and copy,
keyboard, and scrollbar defaults.

[Learn more about how to configure terminal settings.](https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal)

## Manage files in Cloud Shell

Cloud Shell doesn't have direct access to your local machine's file system,
but you can move files between your local machine and your Cloud Shell
environment.

### Upload and download files

You can upload files to your Cloud Shell environment to work with them there,
or download files from Cloud Shell to your local machine.

You can upload and download files and folders using any of these options:

- Select **More** , then select either **Upload** or **Download**.
- Run the `gcloud cloud-shell scp` command in your local terminal.
- Use the Cloud Shell Editor.

[Learn more about uploading and downloading files](https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files).

### Use Git commands

If you have code or configuration files stored in a Git repository, you can
access them from Cloud Shell using `git` commands in the Cloud Shell
terminal.

## Select a Firebase project

Cloud Shell defaults to the project that's open in the Firebase console
when Cloud Shell is launched. The selected project in Cloud Shell isn't
updated if the project opened in the Firebase console changes. You can check
and switch projects in Cloud Shell using gcloud CLI commands.

To view the selected project in Cloud Shell, run the following command:

    gcloud config get-value project

To switch projects, run the following command:

    gcloud config set project PROJECT_ID

## Use Cloud Shell with Firebase services

You can use Cloud Shell to interact with various Firebase products and
features, including:

- **[Firebase Hosting](https://firebase.google.com/docs/hosting/quickstart)**: Deploy web apps and more.
- **[Firebase App Hosting](https://firebase.google.com/docs/app-hosting/alt-deploy#deploy-source)**: Build and deploy full-stack web apps and dynamic backends.
- **[Cloud Functions for Firebase](https://firebase.google.com/docs/functions/get-started)**: Deploy serverless functions triggered by backend events or HTTP requests.
- **[Firebase Security Rules](https://firebase.google.com/docs/rules)**: Define access controls and data validation for various Firebase products.
- **[Firebase AI Logic](https://firebase.google.com/docs/ai-assistance/prompt-catalog/add-ai-features)**: Build AI-powered features into your apps using Firebase and Google's models.

You can also preview web applications running in your Cloud Shell environment
by [using Web Preview](https://docs.cloud.google.com/shell/docs/using-web-preview).