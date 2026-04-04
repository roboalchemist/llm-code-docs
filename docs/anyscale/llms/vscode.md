# Source: https://docs.anyscale.com/platform/workspaces/vscode.md

# Develop with local VS Code or Cursor on an Anyscale workspace

[View Markdown](/platform/workspaces/vscode.md)

# Develop with local VS Code or Cursor on an Anyscale workspace

This page describes using your local installation of VS Code or Cursor for interactive development on an Anyscale workspace.

When you use a local IDE connected to an Anyscale workspace, you're developing inside of the containerized environment deployed to your workspace Ray cluster. See [Launch jobs and services from an Anyscale workspace](/development/workspace-defaults.md) and [Container-driven development on Anyscale](/development/containers.md).

## Launch a local IDE from the Anyscale console[​](#launch-a-local-ide-from-the-anyscale-console "Direct link to Launch a local IDE from the Anyscale console")

You use the Anyscale console to automatically configure a connection between your preferred IDE and an Anyscale workspace.

note

When you use this pattern, Anyscale installs a VS Code extension and adds it to your `remote.SSH.defaultExtensions` setting. For details, see [Anyscale workspaces extension on Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=anyscalecompute.anyscale-workspaces\&ssr=false#overview).

Complete the following steps to connect a local IDE to your Anyscale workspace:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Workspaces**.
3. Click the name of the workspace.
4. If the workspace isn't running, click **Start**.
5. Click the chevron next to your current editor, such as ![VS Code editor chevron](data:image/png;base64,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).
6. Click **Open in VS Code desktop** or **Open in Cursor**. A new page loads asking you to confirm you want to open the application.
7. Click **Open Visual Studio Code** or **Open Cursor**. Your IDE of choice opens.
8. A dialog appears with the text **Allow 'Workspaces' extension to open this URI?**. Click **Open**.
9. A new window for your browser appears that's connected to your Anyscale workspace cluster.

## Configure the Anyscale workspaces VS Code extension to use SSH over HTTPS[​](#https "Direct link to Configure the Anyscale workspaces VS Code extension to use SSH over HTTPS")

note

This feature is available as a beta release.

If you launch local VS Code or Cursor from an Anyscale cloud deployed on Kubernetes, such as AKS, EKS, or GKE, you connect over HTTPS by default.

If your Anyscale cloud uses AWS or Google Cloud virtual machines, you can configure the Anyscale workspaces VS Code extension to use SSH over HTTPS.

Complete the following steps to enable SSH over HTTPS:

1. Open VS Code or Cursor on your machine.
2. Click **Code > Settings > Settings** to open the settings.
3. Search for `anyscale`.
4. Under **Anyscalecompute › Anyscale-workspaces: Connection Method**, select **https**.

## Remove Anyscale workspaces VS Code extension[​](#remove-anyscale-workspaces-vs-code-extension "Direct link to Remove Anyscale workspaces VS Code extension")

To remove the Anyscale workspaces VS Code extension, complete the following steps:

1. Open VS Code on your machine.
2. Click **Code > Settings > Settings** to open the settings.
3. Search for `remote.SSH.defaultExtensions`.
4. Next to `anyscale.anyscale-workspace`, click the **X**.
5. Click **View > Extension** to open the **Extensions** tab.
6. Search for `Anyscale`. Find the extension named **Workspaces** published by **anyscalecompute**.
7. Click the gear icon and select **Uninstall**.
