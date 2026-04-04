# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/taint-vulnerabilities.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/taint-vulnerabilities.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/taint-vulnerabilities.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/taint-vulnerabilities.md

# Injection vulnerabilities

*Injection vulnerabilities* are also known as *injection flaws* or *taint vulnerabilities*; the names are often used interchangeably (ie: injection flaws, injection vulnerabilities, and taint vulnerabilities). They are issues raised by specific security-related rules in SonarQube (Server, Cloud) and remain a top concern. Common types include [SQL Injection](https://rules.sonarsource.com/java/type/Vulnerability/RSPEC-3649/), [Deserialization](https://rules.sonarsource.com/java/type/Vulnerability/RSPEC-5135/), and [Command Injection](https://rules.sonarsource.com/java/type/Vulnerability/RSPEC-2076/) vulnerabilities. See the server related documentation for more details about this type of rule:

* [Security-related rules](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/user-guide/rules/security-related-rules "mention") in SonarQube Cloud
* [Security-related rules](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/digging-deeper/security-related-rules "mention") in SonarQube Cloud

[Injection vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/resources/glossary#i) are unique issues because of how data and information flow within your application. This flow becomes a problem when a user controls the data input into the application (source), and that data is not validated or sanitized before it is used by sensitive functions (sink). This lack of validation or sanitization is what allows a potential attacker to manipulate the data flow for malicious purposes.

Because injection vulnerabilities (i.e., taint vulnerabilities) often involve code in multiple files and functions, SonarQube for IDE can only raise them after a full project analysis. This is why taint vulnerabilities are pulled from SonarQube Server or SonarQube Cloud after a project analysis.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* Running SonarQube for IDE in connected mode with SonarQube Cloud or a SonarQube Server commercial edition is required. See the pages on [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") and [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") for more details.
* Your project should be analyzed regularly, ideally by your CI server.

#### Limitations <a href="#limitations" id="limitations"></a>

* Only taint vulnerabilities in open files are shown in the IDE.
* SonarQube for IDE does not support short-lived branches therefore, when running in connected mode with SonarQube Cloud, you must work with [Branch analysis setup #Long-lived and short-lived branches](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/enriching/branch-analysis-setup#long-lived-and-short-lived-branches "mention"); SonarQube Server does not distinguish between long- and short-lived branches.
  * SonarQube for VS Code follows a logic pattern as defined in the [#branch-awareness](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode#branch-awareness "mention") article to sync the branch analysis on SonarQube (Server, Cloud) with the local analysis, including the synchronization of taint vulnerabilities, in your IDE.
* You’re limited by your SonarQube (Server, Cloud) plan restrictions regarding lines of code limits and branches you can analyze.

### How to display taint vulnerabilities <a href="#how-to-display-taint-vulnerabilities" id="how-to-display-taint-vulnerabilities"></a>

1. Complete your [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") and bind your project to SonarQube (Server, Cloud).
2. In the standard VS Code Panel below the editor region, open the **SONARQUBE** panel.
3. The **SONARQUBE** panel displays the list of injection vulnerabilities that are found in the bound folder. The injection vulnerabilities found in the entire project will be listed by file.

### How to fix your taint vulnerabilities <a href="#how-to-fix-your-taint-issues" id="how-to-fix-your-taint-issues"></a>

Injection vulnerabilities are distinguished in the **SONARQUBE** panel as shown in the following image. Learn how to fix your injection vulnerability by using the tooltip options:

1. Note that your issue list might be collapsed depending on the new code period that is activated when selecting **Focus on New Code** (see [#setting-your-focus-on-new-code](https://docs.sonarsource.com/sonarqube-for-vs-code/new-code#setting-your-focus-on-new-code "mention")).
2. In the **SONARQUBE** panel, your taint vulnerabilities are easily identifiable by looking at the ![sh](https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-93a7838da36c0063c10fde7d977e7d149f3f073f%2F2481ba9faf7c4ab9e521ac602a771be41b24cac1.svg?alt=media) identifying badge. You will also see how many locations this vulnerability occupies.
3. Select one of your taint vulnerabilities to focus the code editor and open the **SONARQUBE ISSUE LOCATIONS** view.
4. Selecting an issue will also open the **SonarQube Rule Description** view.
5. Find more information under the **How can I fix it?** tab.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-ebc0cf828f427ff93277205d935cc7b6ebb4b9b6%2F5a4b8d6866c8194e38fe4b0c8dd1a9a0711de3ed.png?alt=media" alt="Injection vulnerabilities (also known as taint vulnerabilities) are also shown in the SONARQUBE view."><figcaption></figcaption></figure></div>

Because the detection of taint vulnerabilities requires that you run in connected mode, any changes you make to the code must be analyzed by your instance of SonarQube (Server, Cloud). Here are two options to resolve taint vulnerabilities displayed by SonarQube for IDE:

* After you fix the taint vulnerability in your IDE, commit your code to the server and rerun the analysis on SonarQube (Server, Cloud). The new status (of the vulnerability) will be reflected in your IDE.
* Go to the issue in SonarQube (Server, Cloud) and mark it as **Accept** or **False positive**. The new status will be updated locally in less than one minute.

{% hint style="info" %}
When running in connected mode with SonarQube Server 10.4 or newer, **Won’t Fix** becomes **Accept**.
{% endhint %}

See the [fixing-issues](https://docs.sonarsource.com/sonarqube-for-vs-code/using/fixing-issues "mention") page for complete details about fixing issues, including [#fixing-taint-vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/fixing-issues#fixing-taint-vulnerabilities "mention"), in SonarQube for VS Code.
