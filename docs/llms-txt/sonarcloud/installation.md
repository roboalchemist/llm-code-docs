# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/getting-started/installation.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/getting-started/installation.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/getting-started/installation.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/installation.md

# Installation

For the most part, SonarQube for IDE can be installed directly from your IDE’s Marketplace. Offline installations are also possible and previous versions are available if needed.

### Instructions <a href="#instructions" id="instructions"></a>

SonarQube for VS Code can be installed like any other VS Code extension as explained in the [VS Code documentation](https://code.visualstudio.com/docs/editor/extension-marketplace). The standard installation workflow described below works for VS Code, including the Cursor and Trae editors, as well as VSCodium, GitHub Codespaces, and GitPod, among others:

1. Select **Extensions** in the left sidebar of your VS Code app.
2. Enter `SonarQube for IDE` in the search bar.
3. Select **Install**.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-f8523c4fc016918b33b52d98202e99e86e3f4a9e%2Fcf7c85916358e5b25041b376d8e00f8765586a37.png?alt=media" alt="How to find SonarQube in the VS Code Extension Marketplace."><figcaption></figcaption></figure></div>

Once the installation is complete, select the **Reload Required** button to finish the process.

Using the standard method, SonarQube for VS Code will be downloaded from:

* the [Microsoft Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode) for VSCode and GitHub Codespaces.
* the [OpenVSX community marketplace](https://open-vsx.org/extension/SonarSource/sonarlint-vscode), for Cursor, [Trae](https://docs.trae.ai/ide/manage-extensions), and Windsurf editors, as well as VSCodium and GitPod.
  * Both [Cursor](https://docs.cursor.com/guides/migration/vscode) and [Windsurf](https://docs.windsurf.com/windsurf/getting-started#forgot-to-import-vs-code-configurations%3F) offer profile migration tools, which should include your VS Code extensions.
  * In Cursor, you can simply drag and drop the .vsix file into the extensions tab.

As an alternative, the VSIX package for any given version can be downloaded from the [/sonarlint-vscode Release page on GitHub](https://github.com/SonarSource/sonarlint-vscode/releases) and installed using the `Install from VSIX` command in accordance with Microsoft’s [Install from a VSIX instructions](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix).

### First taste of SonarQube for IDE <a href="#first-taste-of-sonarlint" id="first-taste-of-sonarlint"></a>

Now that you have SonarQube for VS Code installed, open or create a new project containing source files in a programming language SonarQube for VS Code can analyze out of the box. See the [rules](https://docs.sonarsource.com/sonarqube-for-vs-code/using/rules "mention") for languages that work with your IDE.

SonarQube for VS Code offers a **walkthrough** to help you make the best out of it SonarQube for IDE; it covers the basic features to help you:

* see issues in your code.
* learn more about those issues and fix them.
* synchronize the analysis configuration with other contributors.
* diagnose problems and share feedback with the SonarQube for IDE team.

The walkthrough will be automatically displayed when you install SonarQube for IDE for the first time, and you can manually open it anytime from the command palette: search **Welcome Open Walkthrough…**, then select **Welcome to SonarQube for IDE!** to have a look!

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-8783347409a329e969df02796f119c9b404d1396%2F6042387c433f013a6c14558483ba3911d68ba4b0.png?alt=media" alt="The Welcome to SonarSonarQube for VS Code introduction walkthrough screen." width="563"><figcaption></figcaption></figure></div>

### Connect to your server <a href="#updating-sonarlint-in-vs-code" id="updating-sonarlint-in-vs-code"></a>

Connect SonarQube for VS Code to your instance of [SonarQube Server](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/user-guide/connected-mode), [SonarQube Cloud](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/improving/connected-mode), or [SonarQube Community Build](https://app.gitbook.com/s/bqrfLGeD0Y9vE5l9Le42/user-guide/connected-mode) to expand your analysis capabilities and share quality profiles with your team. See the article about connected mode [#benefits](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode#benefits "mention"), and the [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") page for full instructions to get going.

### Updating SonarQube for IDE in VS Code <a href="#updating-sonarlint-in-vs-code" id="updating-sonarlint-in-vs-code"></a>

By default, SonarQube for VS Code will update automatically as soon as a new release is published. However, SonarQube for VS Code will *not update automatically* for users who intentionally pin a previous version of the extension.

### Limitations

SonarQube for VS Code is not supported in [Visual Studio Code Virtual Workspaces](https://code.visualstudio.com/api/extension-guides/virtual-workspaces). When installing SonarQube for VS Code you may receive the following error: `This extension has been disabled because it does not support virtual workspaces`&#x20;

Support for virtual workspaces is on the Sonar roadmap; please check out the [feature description](https://portal.productboard.com/sonarsource/4-sonarqube-for-ide/c/499-support-remote-github-repositories-in-vs-code) and tell us how important the feature is to you.
