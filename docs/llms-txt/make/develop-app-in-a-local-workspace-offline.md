# Source: https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/develop-app-in-a-local-workspace-offline.md

# Develop app in a local workspace (offline)

Unlike online development within the Make web interface, local development doesn't provide access to advanced features such as prefilled code templates, IML object suggestions, and seamless integration with the Scenario Builder for continuous testing.

Instead, it offers a self-contained environment for app creation and modification, ideal for situations where internet connectivity is unreliable or where comprehensive testing within the Scenario Builder isn't required.&#x20;

Additionally, local development allows synchronization with Git repositories and provides full search capabilities across the entire codebase.

## Create or edit a current component in a local app

Each group of components, such as RPCs, modules, or custom IML functions, contains the component directories with corresponding code files.

If you need to edit the current code, click the file you want to edit and develop your changes in the opened tab. Save the changes.

If you need to create a new component:

{% stepper %}
{% step %}
Right-click the corresponding components' folder and select **New Local Component: \<component's name> (beta).** For example, New Local Component: Module (beta).

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-b049d8099dcd2e547c19c651566faa964413c1f9%2FScreenshot%202024-05-10%20at%2013.12.48.png?alt=media" alt="" width="332"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Enter the component's name, label, and other corresponding parameters.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-c4ed28b12a8d32216f50f4df6614ecb80698c85c%2FScreenshot%202024-05-10%20at%2013.15.54.png?alt=media" alt="" width="469"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
A new component with the corresponding files is created.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-4f1f9c59bc36500e10a4b007a86063dac4f07069%2FScreenshot%202024-05-10%20at%2013.25.30.png?alt=media" alt="" width="431"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Write the code in the corresponding files and save the changes.
{% endstep %}
{% endstepper %}

Next, you will commit the changes in the [Git repository.](https://developers.make.com/custom-apps-documentation/get-started/make-apps-editor/apps-sdk/local-development-for-apps/commit-the-changes-in-git-repository)
