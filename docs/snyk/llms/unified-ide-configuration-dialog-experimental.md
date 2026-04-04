# Source: https://docs.snyk.io/developer-tools/snyk-ide-plugins-and-extensions/unified-ide-configuration-dialog-experimental.md

# Unified IDE Configuration Dialog (experimental)

You can use only one IDE configuration dialog to configure all your IDEs.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FfvJxTKBqL9aIJkmzaQGY%2Fimage.png?alt=media&#x26;token=b4a4464d-fe72-4609-9ce6-5b0c432d52e3" alt=""><figcaption></figcaption></figure>

## Enabling/Disabling

### Visual Studio Code

1. Add `"htmlSettings": true` to the `snyk.features.preview` object.
2. Click **Settings** in the Snyk extension panel to open the settings page.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2F5OJpIjIsJVyTMTTWEGRD%2FScreenshot%202026-01-14%20at%2011.45.20.png?alt=media&#x26;token=544f4bfe-d051-4681-a72f-1d236d37aa19" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2F5XsmTH5YbuyfmjolcYd6%2FScreenshot%202026-01-14%20at%2011.47.24.png?alt=media&#x26;token=fed345fe-144a-45e8-bdd0-e66d56f93084" alt=""><figcaption></figcaption></figure>

### JetBrains

The configuration dialog is disabled by default. To enable the dialog, set the `snyk.useNewConfigDialog` feature flag to `true` in the JetBrains IDE built-in registry.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FGadfhizNCRqdFrYkfSvy%2Fimage.png?alt=media&#x26;token=98a4a12e-f546-468c-831f-fc67a6a64569" alt=""><figcaption></figcaption></figure>

### Eclipse

Set the `SNYK_USE_NEW_CONFIG_DIALOG` environment variable globally, or launch the IDE from the terminal using a shell script to ensure the variable is enabled.

### Visual Studio

In the **Experimental** Snyk settings, click **Open settings v2 page**.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2FiNRj4EjjtSI6sTHloDok%2FScreenshot%202026-01-14%20at%2011.52.50.png?alt=media&#x26;token=e3072a9f-0829-4ae4-90ad-0c785374a44d" alt=""><figcaption></figcaption></figure>

### Disabling the new settings page

{% hint style="info" %}
If you disable the new settings page, your configurations remain active. These settings are not visible in the native IDE settings.
{% endhint %}

## Scan Configuration

| Setting          | Description                                                                             |
| ---------------- | --------------------------------------------------------------------------------------- |
| Snyk Open Source | Enable/Disable Snyk Open Source scanning                                                |
| Snyk Code        | Enable/Disable Snyk Code scanning                                                       |
| Snyk IaC         | Enable/Disable Snyk IaC scanning                                                        |
| Scanning Mode    | Trigger automatic scans with activated products at startup and when you save documents. |

## Filtering and Display

| Setting                                   | Description                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Filter by severity                        | Show selected severity levels                                                                                                                                                                                                                                                                                    |
| Issue View Options \| Show Open Issues    | Show issues that are not ignored                                                                                                                                                                                                                                                                                 |
| Issue View Options \| Show Ignored Issues | Show issues that are ignored                                                                                                                                                                                                                                                                                     |
| Filter by Risk Score                      | Only show issues with a risk score above or equal to the given numeric threshold                                                                                                                                                                                                                                 |
| Delta Findings                            | <p>The <a href="../visual-studio-code-extension/view-analysis-results-from-visual-studio-code-extension#net-new-issues-versus-all-issues">delta findings feature</a> allows to see only newly introduced issues.<br></p><p>All Issues: show all issues<br>Net-New Issues: show only newly introduced issues.</p> |

## Authentication

| Setting                          | Description                                                                                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication Method            | <ul><li>OAuth2: recommended authentication method</li><li>Token: use legacy Snyk API tokens</li><li>PAT: use personal access tokens experimental</li></ul> |
| Endpoint                         | The (custom) endpoint to communicate with the Snyk API. On multitenant, this is automatically set to the user configured API URL after login.              |
| Insecure (Skip SSL Verification) | Disable SSL certificate verification for HTTPS connections.                                                                                                |
| Token                            | Use this token to authenticate with the Snyk API.                                                                                                          |
| Authenticate                     | Trigger authentication to log in                                                                                                                           |
| Logout                           | Delete authentication credentials                                                                                                                          |

## CLI Configuration

| Setting                       | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CLI Path                      | <p>Enter the file path for the Snyk CLI binary. The plugin uses this path to start the Snyk CLI in the background and to store downloads, if enabled.</p><p>You must provide the correct Snyk CLI location, even if <code>Manage Binaries Automatically</code> is enabled. If the plugin cannot find the binary and <code>Manage Binaries Automatically</code> is disabled, the plugin does not work.</p> |
| Manage Binaries Automatically | Download the latest compatible CLI automatically to the location given in `CLI Path`                                                                                                                                                                                                                                                                                                                      |
| CLI Release Channel           | If `Manage Binaries Automatically` is enabled, the `CLI Release Channel` setting governs, from which release channel binaries are downloaded (stable, release candidate, preview).                                                                                                                                                                                                                        |
| Base URL                      | The base URL to use for CLI downloads.                                                                                                                                                                                                                                                                                                                                                                    |

## Permissions

| Setting        | Description                                                                       |
| -------------- | --------------------------------------------------------------------------------- |
| Trusted Folder | Filesystem path of a folder and all of its subfolders to be trusted for scanning. |
| Add Folder     | Add a new trusted folder                                                          |

## Folder Settings

| Setting                          | Description                                                                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auto Select Organization         | Snyk automatically selects the Organization for this folder based on the SCM integration and imported Projects. If Snyk cannot find a match, it uses your default Organization. |
| Organization                     | Enter the Organization ID or name for this folder. If auto-select is enabled, the field displays the Organization as read-only.                                                 |
| Additional CLI Parameters        | Enter space-separated Snyk CLI parameters to scan this folder. For example, `--severity-threshold=high --debug`.                                                                |
| Additional Environment Variables | Add environment variables to the Snyk CLI, for example, `JAVA_HOME`. This feature is supported only in Eclipse.                                                                 |
| Pre/Post Scan Commands           | Configure commands to run before or after a scan. For example, set up reference branches for delta scanning to ensure builds run before the scan.                               |
