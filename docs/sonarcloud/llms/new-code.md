# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/new-code.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/new-code.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/new-code.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/new-code.md

# New code

### New code and your quality standards <a href="#new-code-and-quality-standards" id="new-code-and-quality-standards"></a>

Focusing on new code is an important step in getting the most out of SonarQube for IDE. When you run an analysis on your main branch (or other long-lived branches) in SonarQube (Server, Cloud) and have set up [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"), SonarQube for IDE uses the server’s New Code Definition (NCD) to determine which issues you should focus on fixing, and calls out the issues found in new code. Focusing on *new code* is at the core of implementing the SonarQube strategy, knowing that the other code will be incrementally fixed over time.

To achieve this, SonarQube for IDE offers the [#focusing-on-new-code](https://docs.sonarsource.com/sonarqube-for-vs-code/investigating-issues#focusing-on-new-code "mention") feature to highlight new code in the IDE.

### Your new code definition <a href="#your-new-code-definition" id="your-new-code-definition"></a>

When SonarQube for IDE is running in connected mode, the SonarQube for IDE uses the NCD defined in SonarQube Server or on SonarQube Cloud. When SonarQube for IDE is running in standalone mode, a locally defined *new code period* highlights your new code.

Running SonarQube for IDE in connected mode with SonarQube (Server, Cloud) offers more opportunities to choose how you define new code.

#### New code definition options <a href="#new-code-definition-options" id="new-code-definition-options"></a>

When you use the NCD found in your SonarQube (Server, Cloud) quality profile, you have more opportunities to choose how to define new code. Check out their respective pages for details:

* [Quality standards and new code](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/user-guide/about-new-code "mention") in SonarQube Server
* [Quality standards and new code](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/standards/about-new-code "mention") in SonarQube Cloud

Without [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"), new code is defined by a *new code period*: any code added or changed in the last 30 days is considered new code. The 30-day timeframe is defined using Git.

*When not using Git*, the new code period begins with the first SonarQube for IDE analysis.

There is no option to manually define a new code period in SonarQube for IDE.

### Setting your focus on new code <a href="#setting-your-focus-on-new-code" id="setting-your-focus-on-new-code"></a>

The **Focus on new code** feature works when SonarQube for IDE is running in either connected mode or standalone mode. New code is defined differently in each mode as mentioned above.

**Focus on new code in connected mode**

Setting your focus on new code has these prerequisites running in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"):

* Your local project must be bound to a SonarQube (Server, Cloud) or SonarQube Community Build project.
* The new code definition must be defined in SonarQube (Server, Cloud) or SonarQube Community Build using a **Previous version**, **Number of days**, or **Specific analysis**.
* The **Reference branch** new code definition is not supported. Please see the [#new-code-definition-options](#new-code-definition-options "mention") article above for links to learn how to properly set your new code definition on the server.

By default, the **Focus on New Code** feature is set to **overall code** when you set up a new connection and establish the project binding; the last saved setting persists through restarts.

**Focus on new code in standalone mode**

When not running in connected mode, the **SonarQube focus** can still be used to highlight only issues found in new code. By default, the **SonarQube focus** feature is set to **overall code** when you open SonarQube for VS Code for the first time; the last saved setting persists through restarts.

#### Change your SonarQube focus <a href="#change-your-sonarqube-focus" id="change-your-sonarqube-focus"></a>

Setting your **SonarQube focus** is easy. To activate or deactivate this mode, select either the ![eye](https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-a33a9969921afcdc5b771eae2ebe5e71feb7f636%2Fc8721f2f80f537d1fd88ffbf3df6833ca2c93187.svg?alt=media) **eye icon** from the **SONARQUBE** panel or, when you select **SonarQube focus**: in the VS Code Status Bar, a quick pick window will pop up allowing you to switch focus.

Additionally, you can select or deselect the **Focus on New Code** mode from the VS Code > **Settings…** > **Settings** > **Extensions** > **SonarLint** > **User** settings menu.

{% hint style="info" %}
When deciding to override a globally defined new code definition at the project level in SonarQube (Server, Cloud) or SonarQube for Community Build, note that it is not possible to specify a unique new code definition at the branch level and still activate the **Focus on New Code** option.
{% endhint %}

Running SonarQube for Eclipse in connected mode with SonarQube (Server, Cloud) and SonarQube Community Build offers more opportunities to choose how you define new code.

### How the new code definition affects the analysis results <a href="#how-new-code-affects-the-analysis-results" id="how-new-code-affects-the-analysis-results"></a>

Focusing on new code and understanding how to work with new code to apply your quality standards are only applicable in SonarQube Server, SonarQube Cloud, and SonarQube Community Build. Learn more about setting quality standards in the server documentation:

* [Quality standards administration](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/quality-standards-administration "mention") in SonarQube Server
* [Setting your quality standards](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/standards "mention") in SonarQube Cloud
* [Quality standards administation](https://app.gitbook.com/s/bqrfLGeD0Y9vE5l9Le42/quality-standards-administration "mention") in SonarQube Community Build

Here are two important points to consider regarding your NCD and SonarQube for VS Code:

* When running SonarQube for IDE in connected mode and enabling the **Focus on New Code** feature, the NCD from SonarQube (Server, Cloud) is used to show you only issues found in *new code*.
* When running SonarQube for IDE while not in connected mode and enabling the **Focus on New Code** feature, [running-an-analysis](https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/running-an-analysis "mention") will show you only issues found in *new code*.

The **Focus on New Code** feature gives you immediate feedback in the IDE, before you submit new code with new issues. Read the [#focusing-on-new-code](https://docs.sonarsource.com/sonarqube-for-vs-code/investigating-issues#focusing-on-new-code "mention") article for more information.
