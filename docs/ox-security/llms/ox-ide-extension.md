# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/ox-ide-extension.md

# OX IDE Extension

The OX IDE extension provides scanning code changes locally within Visual Studio Code (VS Code) and similar environments, such as Cursor, Windsurf, VSCodium. It integrates with the OX Security platform and is intended for developers.

This option is not a replacement for full repository scans, but a complementary tool for early-stage, local validation.

The repository you scan must exist in your organization and be known to OX.

Currently the following issue categories are supported: Open Source Security, Code Security, SBOM, IaC, Secret/PII.

The main goal is to let you scan code locally before pushing changes to a remote repository, as follows:

* Detect vulnerabilities and secrets before they are exposed.
* Prevent pushing malicious code to shared environments.
* Fixing security issues early in the development process.

## How it works

After you install the IDE Extension, it appears in the side toolbar with the OX icon, and starts monitoring changes to files in your workspace.

You can initiate a scan directly from the IDE, which compresses your local changes and sends them to the OX backend for analysis. Scan results, such as vulnerable dependencies and hard-coded secrets are displayed in a dedicated sidebar, with each issue linked to the exact line of code and accompanied by a recommended fix.

You can group these findings by severity or category, filtering the view to focus on critical issues or to see all results at once. Throughout the process, the UI keeps you informed of scan status and messages (for example, **Scan is cancelled**).

After a scan completes, the IDE extension displays the detected issues in the left sidebar of your development environment. To help you review and prioritize results more efficiently, the extension supports grouping and filtering options.

## Requirements

* Visual Studio Code ^1.96.0
* Git extension for VS Code
* An OX.security account with API access

## Generating IDE/CLI Integration key

Before you install the extension, you need to generate an API key.

> **Note:** A user with Admin and Developer roles can create an API Key for the IDE extension. The API Key will be created according to the user's scope.

**To generate an API key:**

1. From the left pane of OX Security platform, select **Settings > API Key Settings**.
2. In the **API Key Settings** window, select **CREATE API KEY**.
3. In the **Create API Key** dialog, set the following:

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-715971677663314d6016a66115617dda5594379c%2FIDE_integration_key.png?alt=media" alt="" width="450"><figcaption></figcaption></figure>

|                     |                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **API Key Name**    | Add a meaningful name that is easy to identify. It is good practice to include the key's intended purpose in the name. |
| **API Key Type**    | Select IDE Integration.                                                                                                |
| **Expiration Date** | Until when you can use this key.                                                                                       |

1. Select **CREATE**. The key appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-701429fb3914c329ab688cbfe2438d0fce18e108%2FIDE_integration_key1.png?alt=media" alt="" width="452"><figcaption></figcaption></figure>

1. Copy and save the API Key Secret to be used when connecting to APIs. This is the only time when you can see and copy the key.
2. Select **CLOSE**. The new key appears in the **API Key Settings** page.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c9069799d044e63cca21e890f8fc21d15ebfc672%2FIDE_integration_key2.png?alt=media" alt=""><figcaption></figcaption></figure>

## Installing the OX IDE Extension

You can install the OX IDE Extension from your IDE marketplace, as follows:

* **VS Code Marketplace:** <https://marketplace.visualstudio.com/items?itemName=oxsecurity.ox-ide>
* **Open VSX Marketplace:** <https://open-vsx.org/extension/oxsecurity/ox-ide>

> **Note:** If your environment blocks marketplace access, for example, offline or restricted networks, contact OX technical support.

**To install the IDE extension and run a security scan:**

1. In **Marketplace**, search for **OX Security**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4570c88a54569d53916d757ff40ff48535582f19%2FIDE_extension_install_marketplace.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Select **Install**. The OX icon appears in the left bar, and a welcome page appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-eb192ad88bd6f9d2179e72f8119d303118c7947d%2FIDE_extension_install2%20(1).png?alt=media" alt="" width="428"><figcaption></figcaption></figure>

1. In the **Welcome to OX Security** page, select **Open settings**. The **Settings** tab opens on the right.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-376bbfd8a3e1e35975091d105c61c43fb2cebcf8%2FIDE_extension_install3%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

1. Add the API key that you generated in the OX Security platform. The message **No issues detected yet** appears on the left and the OX icon appears on the side bar.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b69a6507af79a092d5eb151f7d8997d7c2210ce6%2FIDE_extension_install4.png?alt=media" alt=""><figcaption></figcaption></figure>

The following commands are now available from the side bar:

|                         |                                                              |
| ----------------------- | ------------------------------------------------------------ |
| `Open Settings`         | Opens the OX extension settings panel.                       |
| `Report an Issue`       | Opens a template to report bugs to the OX GitHub repository. |
| `Upload Logs`           | Sends logs to telemetry.                                     |
| `Focus on Found Issues` | Highlights issues in the sidebar.                            |

## Setting API endpoints for OX cloud services

By default OX IDE extension operates on cloud using settings predefined by OX Security. In addition, you can manually switch to the custom API endpoint.

**To define API endpoints:**

1. In the top part of the OX IDE extension, click the gear icon next to the scan button and select **Settings**.
2. To work on-prem or other scenarios, clear **Use predefined API endpoints for OX cloud**, and then in the **Custom API Endpoints** text box, type your local deployment URL.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-feafc52c59b83fab1bcbce814881d3191bf9cadf%2FSettings_Table_API_Endpoints.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

## Sending logs/events to the telemetry service

To support compliance and regulatory opt-out requirements, OX IDE extension can send logs/events to the telemetry service. This option is enabled by default, and you can disable it.

**To disable sending logs/events to telemetry service:**

1. In the top part of the OX IDE extension, click the gear icon next to the scan button and select **Settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5b0d2f462094df427b93f52d56e41fef4c454b10%2FSettings_Table_Telemetry%20(1).png?alt=media" alt="" width="359"><figcaption></figcaption></figure>

1. Clear the **Enable telemetry for your VS Code extension** checkbox.

## Running a scan and analyzing the results

After installing the OX IDE extension and setting it up, you can start running security scans.

When viewing scan results, you can select an issue to navigate directly to the relevant line in the code. This allows you to understand and resolve issues without leaving the OX IDE extension.

**To run a scan:**

* Click the triangle button on the top. The scan runs and then the results appear with the direct link to the specific location in the code that contains a security risk and remediation recommendations.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07a6ea4197995b24085a476fc94f885d29b34cfe%2FIDE_extension_install5.png?alt=media" alt=""><figcaption></figcaption></figure>

Each issue in the list includes the following:

* Severity label
* Short description
* Category
* Status
* Reference to the affected code line
* Suggested fix

### Grouping issues

You can organize issues into logical sets for better navigation, as follows:

* **By severity:** Displays issues in the following order: Critical, High, Medium, and Low. Use this option to focus on the most urgent issues first.\
  OR,
* **By category:** Displays issues based on their type: Open Source Security, Code Security, SBOM, IaC, Secret/PII. Use this option to address similar types of issues across your codebase.

Each group is collapsible and expandable.

**To group security issues:**

* In the top part of the OX IDE extension, click the gear icon next to the scan button and select **Settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-13ed244efea297e2032e3c09a9802c664ee9fba7%2FSettings_Table_Grouping.png?alt=media" alt="" width="368"><figcaption></figcaption></figure>

### Filtering issues

You can use filtering to reduce visual noise and concentrate on the issues that matter most.

You can filter which issues to display, based on the severity levels. The Appoxalypse severity level issues are always presented by default and you cannot set the extension not to display them.

**To filter security issues:**

* In the top part of the OX IDE extension, click the gear icon next to the scan button and select **Settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6c159d8a4f99073d4da9abf7e823a9fb6f3e3077%2FSettings_Table_Filtering.png?alt=media" alt="" width="404"><figcaption></figcaption></figure>

You’re now ready to start using the OX IDE VS Code extension.
