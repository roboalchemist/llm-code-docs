# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/sonarlint-connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/sonarlint-connected-mode.md

# Connected mode

SonarQube for IDE is your first line of defense in keeping your code clean. Connected mode binds your SonarQube (Server, Cloud) project to a project open in SonarQube for IDE so that you can catch issues immediately, even before you commit them.

SonarQube for IDE is a free IDE extension that integrates with SonarQube (Server, Cloud) using connected mode. Like a spell checker, SonarQube for IDE highlights issues as you type. When an issue is identified, SonarQube for IDE provides you with clear remediation guidance so you can fix it before the code is even committed. In many cases, it also provides a *quick fix* that can automatically fix the issue for you.

{% tabs %}
{% tab title="INTELLIJ" %}
SonarQube for IDE integrates with most JetBrains IDEs including IntelliJ IDEA, CLion, GoLand, WebStorm, PHPStorm, PyCharm, Rider, Android Studio & RubyMine.

* [Feature overview](https://www.sonarsource.com/products/sonarlint/features/jetbrains/)
* [Installation](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/getting-started/installation "mention") instructions
* Supported [Rules and languages](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/using/rules "mention")
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/setup) and list of [Connected mode](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/connected-mode) benefits.
* [Download](https://plugins.jetbrains.com/plugin/7973-sonarlint)
  {% endtab %}

{% tab title="VISUAL STUDIO" %}
SonarQube for IDE provides Visual Studio developers with a comprehensive in-IDE solution for improving the quality and security of the code they deliver.

* [Feature overview](https://www.sonarsource.com/products/sonarlint/features/visual-studio/)
* [Installation](https://app.gitbook.com/s/5CSDwdOaYoOAGYNiRqgl/getting-started/installation "mention") instructions
* Supported [Rules and languages](https://app.gitbook.com/s/5CSDwdOaYoOAGYNiRqgl/using/rules "mention")
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/setup) and list of [Connected mode](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/connected-mode) benefits.
* Downloads for:
  * [VS-2022](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2022)
  * [VS-2019](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2019)
  * [VS-2017](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2017)
    {% endtab %}

{% tab title="VS CODE" %}
SonarQube for VS Code will automatically identify and fix quality and security issues as you code with enhanced linting capabilities directly in your VS Code IDE.

* [Feature overview](https://www.sonarsource.com/products/sonarlint/features/vs-code/)
* [Installation](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/getting-started/installation "mention") instructions
* Supported [Rules and languages](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/rules "mention")
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup) and list of [Connected mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode) benefits.
* [Download](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode)
  {% endtab %}

{% tab title="ECLIPSE" %}
SonarQube for Eclipse will automatically identify and fix quality and security issues as you code with enhanced linting capabilities right in your Eclipse IDE.

* [Feature overview](https://www.sonarsource.com/products/sonarlint/features/eclipse/)
* [Installation](https://app.gitbook.com/s/kadXEH8HkykK7lKaDvVq/getting-started/installation "mention") instructions
* Supported [Rules and languages](https://app.gitbook.com/s/kadXEH8HkykK7lKaDvVq/using/rules "mention")
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/setup) and list of [Connected mode](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connected-mode) benefits.
* [Download](https://marketplace.eclipse.org/content/sonarlint)
  {% endtab %}
  {% endtabs %}

**Shared code quality and security expectations**

When using SonarQube for IDE without connected mode, a default quality profile is applied and users can customize their own ruleset. If you’re using a different [quality-profiles](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-profiles "mention") in SonarQube (Server, Cloud), you may see new issues in SonarQube (Server, Cloud) even though your commit looked clean in SonarQube for IDE. With connected mode, the quality profile defined in SonarQube (Server, Cloud) is also applied to your IDE, and you’re notified in your IDE when your local instance isn’t meeting the project’s [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-gates "mention") standards.

Additional code quality and security benefits include sharing the SonarQube (Server, Cloud) settings with all team members, guaranteeing that every developer is connected to the same profile.

**More security**

When using SonarQube for IDE alone, taint analysis issues found by commercial editions of SonarQube Server aren’t raised in SonarQube for IDE for performance reasons (we don’t want to slow down your editing). In connected mode, you’ll see the taint analysis issues SonarQube (Server, Cloud) raised in your project. You’ll get all of the context in your IDE that you need to triage and fix security problems thereby making sure the code you commit is safe.

**Using the Open in IDE feature**

When using Connected Mode with SonarLint for IntelliJ, Visual Studio, VS Code, or Eclipse, it’s possible to use the **Open in IDE** button to open most all issues in the code editor, speeding up the time it takes to find and fix the issue. Simply click the **Open in IDE** button from SonarQube to view it in your IDE; you’ll be prompted to set up Connected Mode if the project is not already bound.

Opening Security hotspots using the **Open in IDE** feature is available for all of the supported IDEs. See [#opening-in-ide](https://docs.sonarsource.com/sonarqube-server/10.8/issues/fixing#opening-in-ide "mention") for more details.

### SonarQube for IDE - SonarQube Server version support policy <a href="#version-support-policy" id="version-support-policy"></a>

SonarQube for IDE enables users to establish a connection to the latest SonarQube Server version and to the latest LTA (Long-Term Active) version. When a new LTA version is released, we still enable connecting SonarQube for IDE to the previous LTA version for a certain period of time (currently 9 months after the latest LTA release) to allow enough time for organizations to update their SonarQube Server version.

For more information about long-term support of SonarQube Server, check out our page describing the [active-versions](https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/upgrade-the-server/active-versions "mention"). Review your SonarQube for IDE-specific requirements for version-to-version differences.

{% hint style="warning" %}
*The 8.9LTA reached its support expiration date (in November ’23)*.
{% endhint %}

### Setting up connected mode <a href="#setting-up-connected-mode" id="setting-up-connected-mode"></a>

See the following links for instructions on setting up connected mode for each supported IDE:

* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/setup) in SonarQube for IntelliJ
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/setup) in SonarQube for Visual Studio
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup) in SonarQube for VS Code
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/setup) in SonarQube for Eclipse

### Understanding SonarQube for IDE usage <a href="#understanding-sonarlint-usage" id="understanding-sonarlint-usage"></a>

SonarQube Server Instance Admins can get an overview of users’ usage of SonarQube for IDE by going to **Administration** > **Security** > **Users.**

The **Last SonarQube for IDE connection** column indicates the last time the user used SonarQube for IDE in connected mode.

You can filter users based on their activity. The available options are:

* **All users**
* **Active users with SonarQube for IDE**: users of SonarQube for IDE in connected mode who were active at least once in the past 30 days.
* **Active users without SonarQube for IDE**: users who have connected to SonarQube Server at least once in the past 30 days.
* **Inactive users**: users who have not connected to SonarQube Server or used SonarQube for IDE in connected mode in the past 30 days.

### Smart notifications <a href="#smart-notifications" id="smart-notifications"></a>

Connected mode allows SonarQube (Server, Cloud) to send smart alerts to individuals or teams when new issues are discovered. With everyone in the loop, issues can be addressed promptly, improving the overall software quality and delivery. You’ll receive smart notifications in your IDE when:

* the [quality-gates](https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-gates "mention") status of a project *open in your IDE* changes
* a SonarQube Server analysis raises new issues *that you’ve introduced in a project open in your IDE*

You can activate or deactivate smart notifications in SonarQube for IDE on the IDE side on a server-by-server basis.

### Reviewing issues in your IDE <a href="#open-in-ide" id="open-in-ide"></a>

Seeing an issue directly in the IDE can help you better understand its context. This is the purpose of the **Open in IDE** button that you’ll see as an authenticated user.

This feature is available if you’re using a compatible version and flavor of SonarQube for IDE. The project must be open in the appropriate IDE and bound to the server using connected mode. To learn more about managing issues locally, please check the SonarQube for IDE documentation for your IDE

* [Investigating issues](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/using/investigating-issues "mention")
* [Investigating issues](https://app.gitbook.com/s/5CSDwdOaYoOAGYNiRqgl/using/investigating-issues "mention")
* [Investigating issues](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/investigating-issues "mention")
* [Investigating issues](https://app.gitbook.com/s/kadXEH8HkykK7lKaDvVq/using/investigating-issues "mention")

Keep in mind that the revision or branch analyzed by SonarQube (Server, Cloud) may not be the same as what you have opened in the IDE. In this case, SonarQube for IDE will do its best to locate the issue in your local code.

### Troubleshooting unexpected analysis results <a href="#troubleshooting-unexpected-analysis-results" id="troubleshooting-unexpected-analysis-results"></a>

<details>

<summary>Unexpected analysis results</summary>

Observing different analysis results between SonarQube (Server, Cloud) and SonarQube for IDE can have different causes.

**Some issues might be detected by a third-party**

Due to extensive resource requirements, injection vulnerability and some advanced bug detection rules are ignored by SonarQube for IDE. Please check the analyzer (PMD, Checkstyle, ESLint, PyLint, …). SonarQube for IDE will only run [rules from Sonar analyzers](https://rules.sonarsource.com/) including [custom rules extending Sonar analyzers](https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/adding-coding-rules). Third-party analyzers usually have their own IDE integration, so we have no plan to run them in SonarQube for IDE.

**Your test files might be mistaken as source files**

Test files can be defined on the server or in the IDE and when running in connected mode, these test sources will be used by SonarQube for IDE. Each SonarQube for IDE flavor has its own way of detecting which file is considered a test file; in SonarQube for IntelliJ, you must define your test files as a [Test Sources Root](https://www.jetbrains.com/help/idea/testing.html#add-test-root). To define test files on the server, please see the [analysis-scope](https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/analysis-scope "mention") page to set the scope of your analysis.

**Some complex rules are not run in SonarQube for IDE**

Due to extensive resource requirements, injection vulnerabilities and some advanced bug detection rules are ignored by SonarQube for IDE. Please check the [SonarQube for IDE roadmap](https://www.sonarsource.com/products/sonarlint/roadmap/) for a list of features and enhancements on the horizon.

**Only line-level issues are reported**

Some rules are able to report issues at the project level. Such issues are not displayed in SonarQube Server for IDE, only in [security-related-rules](https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/rules/security-related-rules "mention").

**When analyzing Java files, the analyzer might need some context for some issues to be found**

In IntelliJ, there is no incremental compilation of the .class files found in the compiler output folder; these are only produced or refreshed when the project is built. The workaround is to simply build your project with the green hammer (when using SonarQube for IntelliJ) in the top-right toolbar. The project should be built on a regular basis to keep the compiled files up-to-date and overcome this [known limitation](https://sonarsource.atlassian.net/browse/SLI-488).

</details>
