# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using/fixing-issues.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/fixing-issues.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/fixing-issues.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/fixing-issues.md

# Fixing issues

Whether your issue is about *a potential security problem*, considered to be *a bad coding practice*, or *a more serious logic error*, fixing issues usually involves changes to the code. SonarQube for IDE’s issue messages contain useful information about how to fix the potential problem and include a rule description so that you can learn more about why the issue is reported.

SonarQube for VS Code offers multiple ways to investigate and fix problems in your code. Issues are usually presented in multiple locations and you can typically hover and/or click or right-click over these markers to open a tooltip that reveals your options. See the [investigating-issues](https://docs.sonarsource.com/sonarqube-for-vs-code/using/investigating-issues "mention") page for more information about finding and identifying your issues.

Double-click an issue in the SonarQube for IDE view window to jump to and highlight the code in the explorer. Once the code is highlighted, you have more than one way to expose solutions and suggested quick fixes.

#### Rule selection <a href="#rule-selection" id="rule-selection"></a>

Issues are reported when your code violates one or more of Sonar's rules. When running SonarQube for VS Code in standalone mode (ie: when you're *not in connected mode*), it's possible to locally manage which rules are used to find issues in your code. See the [#using-sonar-rules](https://docs.sonarsource.com/sonarqube-for-vs-code/rules#using-sonar-rules "mention") articles to learn what's possible.&#x20;

If you simply want to toggle a rule, jump straight to the [#edit-rules](https://docs.sonarsource.com/sonarqube-for-vs-code/rules#edit-rules "mention") article to learn how to turn Sonar rules on or off in your IDE.

{% hint style="info" %}
When a project is bound to a SonarQube (Server, Cloud) or SonarQube Community Build, the **RULES** view  is not visible in the UI. In this case, the rules configuration from the server applies. For more information, see the server documentation about quality profiles to edit rules:

* [Managing quality profiles](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/standards/managing-quality-profiles "mention") in SonarQube Cloud
* [Managing quality profiles](https://app.gitbook.com/s/yDv2XwTC1xoOKBYeCK45/quality-standards-administration/managing-quality-profiles "mention") in SonarQube Server
  {% endhint %}

### Quick fixes <a href="#quick-fixes" id="quick-fixes"></a>

Some issues have Sonar Quick Fixes which means that with a single click, SonarQube for IDE will automatically edit your source code to comply with the rule description and fix the issue. Even when a Sonar Quick Fix is not available, SonarQube for IDE provides options in the tooltip to help you fix your code.

While in the explorer window, select the issue in the PROBLEMS view panel or click the lightbulb in the left margin of the VS Code editor to reveal the tooltip exposing one or more of these options:

* **✧˖° Fix with AI CodeFix**: AI CodeFix suggestions are available when running in connected mode with SonarQube (Server, Cloud). See the article about [#ai-codefix](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ai-codefix#ai-codefix "mention") for details.
* **Open description of rule**: opens a new view panel with the detailed rule description, which usually explains why the issue is raised and explains how to fix it.
* **Deactivate rule ‘yyy:XXX’**: This action disables the rule in the user’s VSCode settings and is only available when you are *not using Connected Mode*.
  * To reactivate a rule, go to the **SONARQUBE SETUP** > **RULES** view in VS Code and click the 3-dots to select **Find Rule By Key**.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-f54a6d115dd56ec2a00a02e24d3960a85adb0ba5%2F061f906bf6cf6f6b4b057e3184ee8c3d2435fa17.png?alt=media" alt="SonarQube for VS Code uses a lightbulb icon as a tooltip to reveal access to actions you can take on issues in your code."><figcaption></figcaption></figure></div>

{% hint style="info" %}
If your code violates more than one rule, a set of options will be presented for each instance. An example is shown in the image below.

* SonarQube for VS Code calls out that your container is missing both CPU *and* memory limits with rules [kubernetes:S6869](https://rules.sonarsource.com/kubernetes/RSPEC-6869/) and [kubernetes:S6864](https://rules.sonarsource.com/kubernetes/rspec-6864/); the Maintainability and Security of your code is potentially affected.
  {% endhint %}

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-94f957c8ed41e1658dfdb60c1559a76dce77b781%2Fba2099abcc405398186aebe973d7a65c740a999f.png?alt=media" alt="If your code violates multiple rules, multiple quick fixes will be shown." width="563"><figcaption></figcaption></figure></div>

### AI CodeFix in your IDE <a href="#ai-codefix" id="ai-codefix"></a>

If you’re running in connected mode with SonarQube Server or SonarQube Cloud, you might see the **✧˖°** icon which means that there is an AI-generated fix suggestion available. Please check the requirements for using [ai-codefix](https://docs.sonarsource.com/sonarqube-for-vs-code/ai-capabilities/ai-codefix "mention").

### Fixing injection vulnerabilities <a href="#fixing-taint-vulnerabilities" id="fixing-taint-vulnerabilities"></a>

**Injection vulnerabilities** (also called taint vulnerabilities) are [Security-related rules](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/digging-deeper/security-related-rules "mention") issues that are only raised by SonarQube Server and SonarQube Cloud. Due to technical limitations, SonarQube for VS Code can not raise such issues on local analysis and must be running in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") to sync injection vulnerabilities from the server.

Injection vulnerabilities are distinguished in the **SONARQUBE** panel as shown in the following image. Learn how to fix your injection vulnerability by using the tooltip options:

1. Note that your issue list might be collapsed depending on the new code period that is activated when selecting **Focus on New Code**. See the [#setting-your-focus-on-new-code](https://docs.sonarsource.com/sonarqube-for-vs-code/new-code#setting-your-focus-on-new-code "mention") article for more information.
2. In the **SONARQUBE** panel, your taint vulnerabilities are easily identifiable by looking at the ![sh](https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-93a7838da36c0063c10fde7d977e7d149f3f073f%2F2481ba9faf7c4ab9e521ac602a771be41b24cac1.svg?alt=media) identifying badge. You will also see how many locations this vulnerability occupies.
3. Select one of your taint vulnerabilities to focus the code editor and open the **SONARQUBE ISSUE LOCATIONS** view.
4. Selecting an issue will also open the **SonarQube Rule Description** view.
5. Find more information under the **How can I fix it?** tab.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-ebc0cf828f427ff93277205d935cc7b6ebb4b9b6%2F5a4b8d6866c8194e38fe4b0c8dd1a9a0711de3ed.png?alt=media" alt="Injection vulnerabilities (also known as taint vulnerabilities) are also shown in the SONARQUBE view."><figcaption></figcaption></figure></div>

Please see the documentation about [taint-vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/taint-vulnerabilities "mention") for more information about working with these particular security issues\*.\*

### Marking issues <a href="#marking-issues" id="marking-issues"></a>

When running SonarQube for VS Code in connected mode with SonarQube Server 10.2 and newer, it is possible to mark issues before submitting your code for PR analysis.

To mark an issue, go to your issue in the code editor or the **PROBLEMS** panel and select the lightbulb to find the **Quick Fix** menu. Then select **SonarQube: Resolve issue violating rule \`**<*your rule>***\` as…** and choose either **Accepted** or **False positive** to resolve the new issue. Note that the **Quick Fix** menu is only available in the lightbulb next to your issue in the code editor.

{% hint style="info" %}
When running in connected mode with SonarQube Server 10.4 or newer, **Won’t Fix** becomes **Accept**.
{% endhint %}

Marking an issue can be applied to both *new issues* and *known issues*. Marks made on known issues will be reflected on the SonarQube Server server within a few minutes; marks made on new issues will be reflected on the server when a new analysis is run. The option to mark an issue as resolved will not appear if you are connected to an unsupported version of SonarQube Server.

To unmark *all issues not yet known in SonarQube Server*, open the **VS Code Command Palette** and run the command `SonarQube: Reopen Local Issues for current file`. This command will only affect new issues that were marked before an analysis was run on the server.

#### Requirements for marking issues <a href="#requirements-for-marking-issues" id="requirements-for-marking-issues"></a>

* SonarQube for VS Code 3.21 or newer.
* Running in connected mode with SonarQube Server 10.2 or newer.
* In SonarQube Server, the **Administer Issues** permission must be granted to the user(s).

{% hint style="info" %}
[security-hotspots](https://docs.sonarsource.com/sonarqube-for-vs-code/using/security-hotspots "mention") and [taint-vulnerabilities](https://docs.sonarsource.com/sonarqube-for-vs-code/using/taint-vulnerabilities "mention") found also on SonarQube Server, Cloud, or on SonarQube Community Build can be marked using different terminology regarding the issue’s status. Please see the dedicated documentation for fixing each of those issue types.
{% endhint %}
