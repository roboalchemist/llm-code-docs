# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/getting-started/offline-installation.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/getting-started/offline-installation.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/getting-started/offline-installation.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/offline-installation.md

# Offline installation

Typically, offline installations start with a download of SonarQube for IDE from your IDE’s Marketplace.

Please check the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode) > **Version History** page to download the most recent versions.

If you don’t have access to your IDE’s Marketplace, you can find the [SonarQube for VS Code VSIX release files here](https://github.com/SonarSource/sonarlint-vscode/releases).

### Instructions <a href="#instructions" id="instructions"></a>

To install SonarQube for IDE offline, you need to first get access to SonarQube for IDE’s VSIX file from either the Marketplace or the release files as described above.

You can download official versions on the Marketplace, or sometimes an ad-hoc version can be built mainly for debugging purposes when a user reports a bug on the Sonar Community forum.

To install the extension, use the dedicated command `>Extensions: Install from VSIX...` in the Visual Studio Code **Command Palette**. Select the VSIX file from the explorer and install it.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-cb05d13cf845c0910d406c4179cefc397e7366e5%2Fcfe8b581cb6137c226672deae20f35bada7566f1.png?alt=media" alt="Go to the VS Code Command Pallet to install SonarQube for VS Code from a VSIX." width="375"><figcaption></figcaption></figure></div>

### CFamily analyzer <a href="#cfamily-analyzer" id="cfamily-analyzer"></a>

To optimize download times, the CFamily analyzer is not included by default with the VSIX release files. You can perform an offline installation by getting the analyzer’s JAR file and deploying it in an installation folder.

#### Finding the installation path <a href="#finding-the-installation-path" id="finding-the-installation-path"></a>

By default, the CFamily analyzer is downloaded to a persistent folder next to the extension’s installation folder (see the [Visual Studio Code documentation](https://code.visualstudio.com/docs/editor/extension-marketplace#_where-are-extensions-installed)).

For example, if SonarQube for VS Code is installed at `/home/user/.vscode/extensions/SonarSource.sonarlint-vscode-{extensionVersion}`, a given analyzer will be downloaded to `/home/user/.vscode/extensions/sonarsource.sonarlint_ondemand-analyzers/sonar-cfamily-version/{analyzerVersion}/sonarcfamily.jar`

#### Performing the offline installation <a href="#performing-the-offline-installation" id="performing-the-offline-installation"></a>

1. Find the required version of the analyzer, declared in the extension’s `package.json` file.
2. With this version number, download the analyzer’s JAR file from <https://binaries.sonarsource.com/?prefix=CommercialDistribution/sonar-cfamily-plugin/>.
3. Deploy the downloaded JAR as `/home/user/.vscode/extensions/sonarsource.sonarlint_ondemand-analyzers/sonar-cfamily-plugin/{analyzerVersion}/sonarcfamily.jar`
