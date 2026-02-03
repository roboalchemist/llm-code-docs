# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/investigating-issues.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/investigating-issues.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/investigating-issues.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/investigating-issues.md

# Investigating issues

SonarQube for IDE can help developers by letting them perform local analyses to check their code before pushing it back to the SCM. While running an analysis, SonarQube for IDE raises an issue every time a piece of code breaks a coding rule.

Usually, a first analysis is performed as soon as one of the supported files is opened. Then, regular analyses are triggered when the editor content changes and/or when the file is saved.

This page describes how to find and investigate issues in your IDE.

### Defining issues <a href="#defining-issues" id="defining-issues"></a>

An *issue* is a problem in your code that violates one of the [Sonar rules](https://rules.sonarsource.com/). Issues found in code are linked to coding attributes and software qualities that determine the overall severity of an issue. Software qualities determine the overall severity of an issue that feeds back into the overall status of your code; please see pages on quality standards in the SonarQube Server and SonarQube Cloud documentation for more information:

* [Quality standards and new code](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/user-guide/about-new-code "mention") in SonarQube Server
* [Quality standards and new code](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/standards/about-new-code "mention") in SonarQube Cloud

Each issue is linked to one coding attribute which is associated with one or more software qualities; each software quality has a level of severity. See [software-qualities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/software-qualities "mention") for more information.

To communicate the code attributes, software qualities, and severity of issues found in your code, SonarQube for VS Code displays them in the **SonarQube Rule Description** webview as described below.

### Finding issues <a href="#finding-issues" id="finding-issues"></a>

For most issues, SonarQube for VS Code provides information about *why* there is an issue and offers one or more actions to fix your issue. Information for [fixing-issues](https://docs.sonarsource.com/sonarqube-for-vs-code/using/fixing-issues "mention") can be found in four places:

1. In the **VS Code Text Editor**, identifiable by the classic squiggles underlining issues in the code.
2. In the **Tooltip**, recommended action(s) can be found by clicking on the light bulb in the left margin of the code explorer view.
3. In the **PROBLEMS** panel, select your issue to highlight the issue-causing code in the Editor. Right-clicking on the issue opens the same tooltip action as described above.
4. In the **SONARQUBE** panel, working with issues is similar to the **PROBLEMS** panel except that all issues are shown, including [security-hotspots](https://docs.sonarsource.com/sonarqube-for-vs-code/using/security-hotspots "mention"), [taint-vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/taint-vulnerabilities "mention"), and [dependency-risks](https://docs.sonarsource.com/sonarqube-for-vs-code/using/dependency-risks "mention").

Injection vulnerabilities work a bit differently. At the **Tooltip**, select **Show all locations** to view the execution flow in the **SONARQUBE ISSUE LOCATIONS** view. See the [taint-vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/taint-vulnerabilities "mention") page for more details about working with these items.

#### Opening issues in the IDE <a href="#opening-issues-in-the-ide" id="opening-issues-in-the-ide"></a>

Understanding issues in context is a helpful way to address problems more effectively. Beginning in SonarQube Server 10.3, on SonarQube Cloud, and in SonarQube Community Build, it is possible to open all issues in your IDE, including taint vulnerabilities. Using the **Open in IDE** feature includes an automated connected mode setup to help with the process.

In your instance of SonarQube Server or SonarQube Community Build, or on SonarQube Cloud:

1. Navigate to your **Project** > **Issues** page,
2. select an issue’s detail view,
3. and select the **Open in IDE** button as an authenticated user to edit the issue in your IDE.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-64c5436227998d4058dcd71c0989dd7ad6a80697%2F56db0507ea87504bd25b126a516df20e9b45a629.png?alt=media" alt="After selecting the Open in IDE button from SonarQube Server or Cloud, a window will pop up to review the issue in your open IDE."><figcaption></figcaption></figure></div>

{% hint style="warning" %}
**Open in IDE** is not supported in Safari. Safari has strict security policies regarding custom protocol links which are required to open files directly in your IDE. When using SonraQube (Server, Cloud) or SonarQube Community Build, please use Chrome or Firefox for this functionality.
{% endhint %}

It’s best if your project is already open in the appropriate IDE and bound to the server using connected mode; if not, you will be prompted to set up a new connection and/or bind your project using the automatic connected mode setup feature. If you use **Open in IDE** and Windows Subsystem for Linux (WSL), check the [#open-in-ide](https://docs.sonarsource.com/sonarqube-for-vs-code/resources/troubleshooting#open-in-ide "mention") troubleshooting article if you’re having problems.

If you’ve already fixed the issue in your code, SonarQube for IDE will not be able to find it; only the matching code will be highlighted. In this case, check that recent changes have been analyzed by SonarQube (Server, Cloud) or SonarQube Community Build, then check the documentation on the relevant Issues pages for details about managing your issues on the server:

* [Managing issues](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/user-guide/issues "mention") in SonarQube Server.
* [Managing code issues](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/managing-your-projects/issues "mention") in SonarQube Cloud.
* [Managing issues](https://app.gitbook.com/s/bqrfLGeD0Y9vE5l9Le42/user-guide/issues "mention") in SonarQube Community Build.

Please see the [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") documentation to [#connection-setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup#connection-setup "mention") to an instance of SonarQube (Server, Cloud) or SonarQube Community Build. And if you have troubles with the automatic connected mode setup, we identified the most common errors for [#troubleshooting-connected-mode-setup](https://docs.sonarsource.com/sonarqube-for-vs-code/resources/troubleshooting#troubleshooting-connected-mode-setup "mention").

**AI CodeFix and Open in IDE**

SonarQube (Server, Cloud) will offer AI-generated fix suggestions for issues detected in your code when AI CodeFix is enabled on your project. You can view the suggestions as a diff view directly in your IDE by selecting **View Fix in IDE** from the **Issues** page in SonarQube (Server, Cloud).

The process is similar to selecting the **Open in IDE** button: it’s best to set up connected mode beforehand. Otherwise, you’ll be prompted to set up a new connection and/or bind your project using the automatic connected mode setup feature.

SonarQube (Server, Cloud) will offer AI-generated fix suggestions for issues detected in your code when AI CodeFix is enabled on your project. You can view the suggestions as a diff view directly in your IDE by selecting **View Fix in IDE** from the **Issues** page in SonarQube (Server, Cloud).

The process is similar to selecting the **Open in IDE** button: it’s best to set up connected mode beforehand. Otherwise, you’ll be prompted to set up a new connection and/or bind your project using the automatic connected mode setup feature.

### Focusing on new code <a href="#focusing-on-new-code" id="focusing-on-new-code"></a>

The **Focus on New Code** feature works when SonarQube for VS Code is running in either connected mode or standalone mode. As mentioned above, new code is defined differently in each mode. Please see the [new-code](https://docs.sonarsource.com/sonarqube-for-vs-code/using/new-code "mention") page to understand your options when using a New Code Definition.

**Focus on new code in connected mode**

Setting your focus on new code has these prerequisites running in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"):

* Your local project must be bound to a SonarQube (Server, Cloud) or SonarQube Community Build project.
* The new code definition must be defined in SonarQube (Server, Cloud) or SonarQube Community Build using a **Previous version**, **Number of days**, or **Specific analysis**.
* The **Reference branch** new code definition is not supported. Please check the server documentation for more details about setting your new code definition:
  * [Quality standards and new code](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/user-guide/about-new-code "mention") in SonarQube Server
  * [Quality standards and new code](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/standards/about-new-code "mention") in SonarQube Cloud
  * [Quality standards and new code](https://app.gitbook.com/s/bqrfLGeD0Y9vE5l9Le42/user-guide/about-new-code "mention") in SonarQube Community Build

By default, the **Focus on New Code** feature is set to **overall code** when you set up a new connection and establish the project binding; the last saved setting persists through restarts.

**Focus on new code in standalone mode**

When not running in connected mode, the **SonarQube focus** can still be used to highlight only issues found in new code. By default, the **SonarQube focus** feature is set to **overall code** when you open SonarQube for VS Code for the first time; the last saved setting persists through restarts.

#### Change your SonarQube focus <a href="#change-your-sonarqube-focus" id="change-your-sonarqube-focus"></a>

Setting your **SonarQube focus** is easy. To activate or deactivate this mode, select either the ![eye](https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-a33a9969921afcdc5b771eae2ebe5e71feb7f636%2Fc8721f2f80f537d1fd88ffbf3df6833ca2c93187.svg?alt=media) **eye icon** from the **SONARQUBE** panel or, when you select **SonarQube focus**: in the VS Code Status Bar, a quick pick window will pop up allowing you to switch focus.

Additionally, you can select or deselect the **Focus on New Code** mode from the VS Code > **Settings…** > **Settings** > **Extensions** > **SonarLint** > **User** settings menu.

{% hint style="info" %}
When deciding to override a globally defined new code definition at the project level in SonarQube (Server, Cloud) or SonarQube for Community Build, note that it is not possible to specify a unique new code definition at the branch level and still activate the **Focus on New Code** option.
{% endhint %}

### The SonarQube views <a href="#the-sonarqube-views" id="the-sonarqube-views"></a>

#### The SONARQUBE SETUP view container in VS Code <a href="#the-sonarqube-setup-view-container-in-vs-code" id="the-sonarqube-setup-view-container-in-vs-code"></a>

**CONNECTED MODE**

Here you can find your active connections and set up new connections if needed. Please see the [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") page to learn about the Sonar solution. If you’re running an AI-enabled IDE and want to install the SonarQube MCP Server, see the [#setup-the-sonarqube-mcp-server](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ides/cursor#setup-the-sonarqube-mcp-server "mention") article for instructions.

When you're using an AI-enabled IDE such as Cursor, Windsurf, or VS Code with Copilot enabled, and have already completed your [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") in SonarQube for IDE with SonarQube Server or SonarQube Cloud, a quick select button is available.

* Select the <picture><source srcset="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fr6Pesg2GVz7SeQGNl4hz%2Fmcp-dark-mode.png?alt=media&#x26;token=7ded2e19-d4ad-4017-a03d-42eee4abe3f4" media="(prefers-color-scheme: dark)"><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-0401b61efd30b446650d936aeba51a5fd7e33b62%2Fmcp-optimized.svg?alt=media" alt="" data-size="line"></picture> icon, **Configure MCP Server** from the **CONNECTED MODE** view window to use your connected mode credentials to start using the SonarQube MCP Server. The same workflow is available in the **AI AGENTS CONFIGURATION** view.

**RULES**

Sonar Rules can individually be turned on or off while running SonarQube for VS Code in standalone mode. Simply go to **SONARQUBE SETUP** > **RULES** view in the VS Code Activity Bar and deactivate or activate rules at will. Each rule is clearly marked as *on* or *off*, and it’s possible to filter the visible list by an **Active**, **All**, and **Inactive** status.

The **RULES** view is only visible while running SonarQube for VS Code in standalone mode because, when your project is bound to SonarQube (Server, Cloud) or SonarQube Community Build using [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"), the rule set is managed on the server side as defined by the quality profile.

**SONARQUBE ISSUE LOCATIONS**

If your issue is an injection vulnerability or a security hotspot with multiple locations, the security issue’s Flow will be shown here. The view will only appear when you select an injection vulnerability or security hotspot in the **SONARQUBE** panel. If there are no issues with secondary locations to report, the view is hidden.

Please see the documentation on [taint-vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/taint-vulnerabilities "mention") and [security-hotspots](https://docs.sonarsource.com/sonarqube-for-vs-code/using/security-hotspots "mention") for more information.

**AI AGENTS CONFIGURATION**

The **AI AGENTS CONFIGURATION** view is only available when running an AI-enabled agent and offers two tools to help your AI agent engage with SonarQube (Server, Cloud).

* Select **Configure SonarQube MCP Server** to use your connected mode credentials to install the SonarQube MCP Server. You will be prompted to complete your [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") if none exists.
* Available in Cursor, Kiro, and Windsurf: Select **Introduce SonarQube Rules File** to create explicit instructions for your AI-powered IDE to produce secure, reliable, and maintainable code.
  * The file provides SonarQube MCP Server instructions to your AI agent. As an example, it instructs the agent to disable SonarQube automatic analysis before starting code generation, and to enable it after the generation is complete. It also asks the agent to analyze changed files in batches, once the changes are done.

#### Editor Groups <a href="#editor-groups" id="editor-groups"></a>

**Code Editor**

In the VS Code code editor, colored waves (squiggles) underline *Warning* and *Information* issues. By default, *Hint* issues are marked by an ellipsis at the beginning of the line. Hovering over the squiggles will reveal code actions and more information about the issue.

**SonarQube Rule Description**

The **SonarQube Rule Description** Editor Group will display a brief explanation of the rule, along with a noncompliant and compliant code example.

Simply select any issue in the **PROBLEMS** or **SONARQUBE** panels and the **SonarQube Rule Description** webview will open automatically. Here you will find a brief explanation of the rule, along with a noncompliant and compliant code example (where available).

For some **SonarQube Rule Descriptions**, you can visualize a diff view for the noncompliant and compliant code sample, which should help you fix your issue.

If an [ai-codefix](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ai-codefix "mention") is available, you'll see the option in the actions menu (when right-clicking on an issue).

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-7b8db85eae04acb872e7629e6223f9f28154235a%2Fsq-vscode-open-rule-description-ai-codefix.png?alt=media" alt="The SonarQube Rule Description tab will give you lots of information to help you fix your issue."><figcaption></figcaption></figure></div>

An issue’s coding attribute, software qualities, and severity are found when opening the SonarQube Rule tab. Below the rule title, you will find the coding attributes that highlight an issue’s classification. Check the [glossary](https://docs.sonarsource.com/sonarqube-for-vs-code/resources/glossary "mention") for details about coding attributes, and the [software-qualities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/software-qualities "mention") page to better understand how they help classify your issue.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-ca9a4b669937a2320e3455022d1c3b7941ca8d1f%2F42237e013ce89749beb19dcdee42cf66ada8a984.png?alt=media" alt="Coding attributes and software qualities appear in the SonarQube Rule Description view. Your actual view may be different because when running in connected mode with SonarQube Server, the server&#x27;s mode is respected." width="563"><figcaption></figcaption></figure></div>

**When in Connected Mode**

If you’re running SonarQube for VS Code while in connected mode *with SonarQube Server or SonarQube Community Build*, your view will change according to the server settings. Standard Experience mode encompasses the use of rule types such as bugs, code smells, and vulnerabilities. Alternatively, if SonarQube Server is set to Multi-Quality Rule mode, you will more accurately represent the impact an issue has on all software qualities.

Please see the pages about the MQR mode and Standard Experience for detailed information about the available rule modes for your instance:

* [Choosing a mode for your instance](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/instance-administration/analysis-functions/instance-mode "mention") in SonarQube Server
* [Choosing a mode for your instance](https://app.gitbook.com/s/bqrfLGeD0Y9vE5l9Le42/instance-administration/analysis-functions/instance-mode "mention") in SonarQube Community Build

#### Panels <a href="#panels" id="panels"></a>

If you don't immediately see the Panels described below, either select the **Toggle Panels** icon in the upper right corner of VS Code, or toggle the **Warnings** display switch in the **Status Bar**.

**PROBLEMS**

Ideally, the team wouldn’t introduce any new issues (any new technical debt) when writing code. But in real life, it’s not always possible to code without creating new technical debt, and sometimes it’s just not worth it.

Selecting issues from the **PROBLEMS** panel will jump you to the line of code in your file where the code is highlighted. Right-clicking on an issue will reveal fixes that are available for that issue.

Each issue’s severity is indicated by the icon to the left of the description. Selecting an issue or hovering over the severity icon is another way to reveal the **Show fixes** lightbulb. In addition, issues from open files are shown in the SONARQUBE panel where they can be filtered and accessed alongside your security hotspots and injection vulnerabilities; a complete list of available filters is [#sonarqube](#sonarqube "mention").

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-f54a6d115dd56ec2a00a02e24d3960a85adb0ba5%2F061f906bf6cf6f6b4b057e3184ee8c3d2435fa17.png?alt=media" alt="SonarQube for VS Code uses a lightbulb icon as a tooltip to reveal access to actions you can take on issues in your code."><figcaption></figcaption></figure></div>

**OUTPUT**

This panel contains the SonarQube for VS Code logs. To view them in more detail and improve troubleshooting, you must enable the **Show Verbose Logs** option in the **Extensions** settings.

Please see the [troubleshooting](https://docs.sonarsource.com/sonarqube-for-vs-code/resources/troubleshooting "mention") page for complete details.

To better control the way you see and manage issues, check out the VS Code documentation on [fixing-issues](https://docs.sonarsource.com/sonarqube-for-vs-code/using/fixing-issues "mention") for quick ways to fix problems. Also, look at the article about running SonarQube for VS Code in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") for details about integrating your local analysis with your SonarQube (Server, Cloud) or SonarQube Community Build analysis.

**SONARQUBE**

All issues are available in the **SONARQUBE** panel. Select an issue to open its details and jump to the issue in the code editor. If multiple locations are impacted by the issue, the **Explorer** > **SONARQUBE ISSUE LOCATIONS** view will open to reveal the injection flow.

Right-click on any issue in the **SONARQUBE** panel to reveal more actions. The option to generate an AI CodeFix suggestion will be present if available. Selecting **More Actions…** will reveal Quick Fixes, the ability to **Accept** and issue, or open the SonarQube Rule description tab.

For a full list of Security Hotspots, run `SonarQube: Scan for Hotspots in Folder` from the command palette (**Ctrl** + **Shift** + **P** on Windows/Linux or **Command** + **Shift** + **P** on MacOS).

There are two filter mechanisms available in the SONARQUBE panel: **Focus on New Code** and **Filter Findings**:

1. **Focus on New Code**: switches the issues shown according to the new code definition used for your project. Changing the **SonarQube focus** is easily done from the SONARQUBE panel. Simply select the ![EYE](https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-a33a9969921afcdc5b771eae2ebe5e71feb7f636%2Fc8721f2f80f537d1fd88ffbf3df6833ca2c93187.svg?alt=media) eye icon to change your focus. More information about new code and quality standards is available on the [new-code](https://docs.sonarsource.com/sonarqube-for-vs-code/using/new-code "mention") page.
2. **Filter Findings**: sorts issues by which file state (All, Current, or Open), fix availability, or severity. Fix availability includes Quick Fix or AI CodeFix-eligible issues. When selecting **Severity**, only issues from open files will be shown. Injection vulnerabilities are also shown for open files (see point 5 below).
3. Enable or disable automatic analysis. The white circle in the status bar means that automatic analysis is enabled.
4. Filtering for **All** displays all issues in your open files.
5. In addition, when selecting **All** while in connected mode with SonarQube Server or SonarQube Cloud, you will see:
   * [taint-vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/taint-vulnerabilities "mention") in all files even if the file is not open.
   * all [security-hotspots](https://docs.sonarsource.com/sonarqube-for-vs-code/using/security-hotspots "mention") in all files (even unopened files) when you run the **Scan for Hotspots in Folder** command.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-791feae6341938fa4cc3ce0acfd99b33f156fa72%2Fsq-vscode-sonarqube-panel-descriptions.png?alt=media" alt="Depending on the filter you apply, what you see in the VS Code UI will be sorted accordingly."><figcaption></figcaption></figure></div>

### SonarQube for IDE Labs

**SONARQUBE FOR IDE LABS**

The **SONARQUBE FOR IDE LABS** panel highlights early access features; you'll need to join SonarQube for IDE Labs to have access to *Experimental* features. If closed, the panel will expand when selecting the **>** arrow on the right side of your **SONARQUBE** panel.&#x20;

After signing up, a series of active features are available, ready with descriptions and links to open Feedback forms where you can share your thoughts!&#x20;

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2FaGmAXvuK8BaXsOu6G1zc%2Fsq-vscode-ide-labs-sign-up.png?alt=media&#x26;token=90051e6e-734a-4b61-8476-ecc2008f79dd" alt="Sign up for access to the SonarQube IDE Labs to get early access to new features and for an opportunity to give direct feedback on what you think." width="373"><figcaption></figcaption></figure></div>

It's possible to **Enable** or **Disable** *Experimental* features at anytime by selecting the gear icon; features marked as *Stable* and *New* will always remain active.
