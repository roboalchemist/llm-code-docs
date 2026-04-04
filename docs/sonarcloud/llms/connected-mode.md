# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/connected-mode.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode.md

# SonarQube for IDE

Connected mode binds your SonarQube Cloud project to a local project so that automated code review can catch issues immediately, right in the IDE, before you even commit them.

[SonarQube for IDE](https://www.sonarsource.com/products/sonarlint/) is a free IDE extension that integrates with SonarQube (Server, Cloud) using connected mode. Like a spell checker, automated code review highlights issues as you type. When an issue is identified, SonarQube for IDE provides you with clear remediation guidance so you can fix it before the code is even committed. In many cases, it also provides a *quick fix* that can automatically fix the issue for you.

### Supported IDEs <a href="#supported-ides" id="supported-ides"></a>

{% tabs %}
{% tab title="VS CODE" %}
SonarQube for VS Code will automatically identify and fix quality and security issues as you code with enhanced linting capabilities directly in your VS Code IDE. SonarQube for VS Code works with most VS Code forks including Cursor, Windsurf, Trae, and more.

* [Feature overview](https://www.sonarsource.com/products/sonarlint/features/vs-code/)
* [Installation](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/getting-started/installation "mention") instructions
* Supported [Rules and languages](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/rules "mention")
* [Connected mode setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup) and list of [Connected mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode) benefits.
* [Download](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarlint-vscode)
  {% endtab %}

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
  * [VS-2019](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2019) (no longer suppoerted)
  * [VS-2017](https://marketplace.visualstudio.com/items?itemName=SonarSource.SonarLintforVisualStudio2017) (no longer suppoerted)
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

The supported languages vary by IDE. Check the Rules page for your IDE to learn which languages are supported out-of-the-box and which require the use of connected mode.

Though SonarQube for IDE can run local analyses in standalone mode, we highly recommend that you set up connected mode with SonarQube (Server, Cloud) or SonarQube Community Build. Running SonarQube Cloud and SonarQube for IDE in connected mode provides additional [valuable features](https://www.sonarsource.com/products/sonarlint/features/connected-mode/).

### Connected mode benefits <a href="#connected-mode-benefits" id="connected-mode-benefits"></a>

* When combining SonarQube for IDE-supported rules with Sonar Cloud's [overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/overview "mention"), you can analyze more languages and detect more issues.
* Highlight advanced issues (in the IDE) like injection vulnerabilities, detected by SonarQube Cloud. See [security-related-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-related-rules "mention") for more information.
* Use the same quality profile locally as is defined on SonarQube Cloud. See the [managing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles "mention") pages for more details.
* Apply settings, such as [rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules "mention") and file exclusion defined on SonarQube Cloud, to your local analysis. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/introduction "mention") to analysis scope for more information.
* Define specific [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") on SonarQube Cloud, and have those parameters applied locally.
* Automatically suppress issues that are marked as Accepted or False Positive on SonarQube Cloud so that locally reported issues match those found on the server. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/introduction "mention") to managing code issues for more details.
* Use the SonarQube for IDE focus on new code features to concentrate detection of issues only in new code. See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for more information.
* Changes in your SonarQube Cloud [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention") will arrive in your IDE when you accept Smart notifications.

#### Using the Open in IDE feature

If you’re using SonarQube for IntelliJ, Visual Studio, VS Code, or Eclipse, the **Open in IDE** button can be used to open most all issues in the code editor, speeding up the time it takes to find and fix your issue. Simply click the **Open in IDE** button from SonarQube Cloud to view it in your IDE; you’ll be prompted to set up connected mode if the project is not already bound.

Opening Security hotspots using the **Open in IDE** feature is available for all of the SonarQube IDEs. See [fixing](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/fixing "mention") for more details.

### Reviewing issues in your IDE <a href="#open-in-ide" id="open-in-ide"></a>

Seeing an issue directly in the IDE can help you better understand its context. This is the purpose of the **Open in IDE** button that you’ll see as an authenticated user.

This feature is available if you’re using a compatible version and flavor of SonarQube for IDE. The project must be open in the appropriate IDE and bound to the server through connected mode. To learn more about managing issues locally, please check the SonarQube for IDE documentation for your IDE:

* [Investigating issues](https://app.gitbook.com/s/6LPRABg3ubAJhpfR5K0Y/using/investigating-issues "mention") in SonarQube for VS Code
* [Investigating issues](https://app.gitbook.com/s/NvI4wotPmITyM0mnsmtp/using/investigating-issues "mention") in SonarQube for IntelliJ
* [Investigating issues](https://app.gitbook.com/s/5CSDwdOaYoOAGYNiRqgl/using/investigating-issues "mention") in SonarQube for Visual Studio
* [Investigating issues](https://app.gitbook.com/s/kadXEH8HkykK7lKaDvVq/using/investigating-issues "mention") in SonarQube for Eclipse

Simply open a file of a supported language and start coding, and you will start seeing issues highlighted in your code. For example, here is SonarQube for VSCode:

![](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-754d8e8796159ead28cd5ae9ebb7ab5d5573fa6f%2Feb85cb7652471f2d8fe753af157333830a3d58ca.gif?alt=media)

Keep in mind that the revision or branch analyzed by SonarQube (Server, Cloud) may not be the same as what you have opened in the IDE. In this case, SonarQube for IDE will do its best to locate the issue in your local code.

### Commercial-level rules

There are commercial-level rules available in SonarQube Cloud for all plans. However, these rules will not appear in your IDE unless your SonarQube for IDE is in connected mode.

### Injection vulnerabilities <a href="#injection-vulnerabilities" id="injection-vulnerabilities"></a>

*Injection vulnerabilities* are also known as *injection flaws* or *taint vulnerabilities*; the names are often used interchangeably (ie: injection flaws, injection vulnerabilities, and taint vulnerabilities). They are issues raised by specific security-related rules in SonarQube Server and SonarQube Cloud and remain a top concern. Common types include [SQL Injection](https://rules.sonarsource.com/java/type/Vulnerability/RSPEC-3649/), [Deserialization](https://rules.sonarsource.com/java/type/Vulnerability/RSPEC-5135/), and [Command Injection](https://rules.sonarsource.com/java/type/Vulnerability/RSPEC-2076/) vulnerabilities.

Injection vulnerabilities are unique issues because of how data and information flow within your application. This flow becomes a problem when a user controls the data input into the application (source), and that data is not validated or sanitized before it is used by sensitive functions (sink). This lack of validation or sanitization is what allows a potential attacker to manipulate the data flow for malicious purposes.

Because injection vulnerabilities (i.e., taint vulnerabilities) often involve code in multiple files and functions, SonarQube for IDE can only raise them after a full project analysis. This is why taint vulnerabilities are pulled from SonarQube Server or SonarQube Cloud after a project analysis.

You can find the definition of injection vulnerabilities in the [glossary](https://docs.sonarsource.com/sonarqube-cloud/appendices/glossary "mention")

Currently, as analyzed by SonarQube Cloud, injection vulnerabilities are only pulled from the project’s main branch.

### Smart notifications <a href="#smart-notifications" id="smart-notifications"></a>

Connected mode allows SonarQube (Server, Cloud) to send smart alerts to individuals or teams when new issues are discovered. With everyone in the loop, issues can be addressed promptly, improving the overall software quality and delivery. You’ll receive smart notifications in your IDE when:

* the [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention") status of a project *open in your IDE* changes
* a SonarQube analysis raises new issues that you’ve introduced in a project open in your IDE

Each developer must individually activate or deactivate SonarQube for IDE smart notifications directly in SonarQube for IDE on the IDE side. When setting up connected mode for the first time, there’s a box to check to decide whether or not you want to receive Smart Notifications from SonarQube Cloud in your IDE.

For all the details about managing notifications, check the SonarQube for IDE documentation that matches your IDE:

* [Notifications](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode#notifications) in SonarQube for VS Code
* [Notifications](https://docs.sonarsource.com/sonarqube-for-intellij/connect-your-ide/connected-mode#notifications) in SonarQube for IntelliJ
* [Notifications](https://docs.sonarsource.com/sonarqube-for-visual-studio/connect-your-ide/connected-mode#notifications) in SonarQube for Visual Studio
* [Notifications](https://docs.sonarsource.com/sonarqube-for-eclipse/connect-your-ide/connect-your-ide/connected-mode#notifications) in SonarQube for Eclipse

### Troubleshooting unexpected analysis results <a href="#troubleshooting-unexpected-analysis-results" id="troubleshooting-unexpected-analysis-results"></a>

<details>

<summary>Unexpected analysis results</summary>

Observing different analysis results between SonarQube (Server, Cloud) and SonarQube for IDE can have different causes.

**Some issues might be detected by a third-party**

Due to extensive resource requirements, injection vulnerability and some advanced bug detection rules are ignored by SonarQube for IDE. Please check the analyzer (PMD, Checkstyle, ESLint, PyLint, …). SonarQube for IDE will only run [rules from Sonar analyzers](https://rules.sonarsource.com/) including custom rules extending Sonar analyzers. Third-party analyzers usually have their own IDE integration, so we have no plan to run them in SonarQube for IDE.

**Your test files might be mistaken as source files**

Test files can be defined on the server or in the IDE, and when running in connected mode, these test sources will be used by SonarQube for IDE. Each SonarQube for IDE flavor has its own way of detecting which file is considered a test file; in SonarQube for IntelliJ, you must define your test files as a [Test Sources Root](https://www.jetbrains.com/help/idea/testing.html#add-test-root). To define test files on the server, please see the [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/introduction "mention") page to set the scope of your analysis.

**Some complex rules are not run in SonarQube for IDE**

Due to extensive resource requirements, injection vulnerabilities and some advanced bug detection rules are ignored by SonarQube for IDE. Please check the [SonarQube for IDE roadmap](https://www.sonarsource.com/products/sonarlint/roadmap/) for a list of features and enhancements on the horizon.

**Only line-level issues are reported**

Some rules are able to report issues at the project level. Such issues are not displayed in SonarQube Server for IDE, only in SonarQube Server; see the [security-related-rules](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-related-rules "mention") page for more details.

**When analyzing Java files, the analyzer might need some context for some issues to be found**

In IntelliJ, there is no incremental compilation of the .class files found in the compiler output folder; these are only produced or refreshed when the project is built. The workaround is to simply build your project with the green hammer (when using SonarQube for IntelliJ) in the top-right toolbar. The project should be built on a regular basis to keep the compiled files up-to-date and overcome this [known limitation](https://sonarsource.atlassian.net/browse/SLI-488).

</details>
