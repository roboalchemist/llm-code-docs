# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using/dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using/dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using/dependency-risks.md

# Dependency risks

In connected mode, you can see the results from SonarQube (Server, Cloud) [Advanced Security ](https://app.gitbook.com/s/B4UT2GNiZKjtxFtcFAL7/advanced-security)tools for Software composition analysis (SCA), directly in the VS Code UI. This includes:

* vulnerabilities in your third-party open source dependencies.
* seeing where your open source dependencies may be in conflict with your organization’s license policies.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* Using SonarQube Server Enterprise edition version 2025.4 or later or SonarQube Cloud with the Enterprise Plan.
* Having the Advanced Security add-on with SCA enabled. SCA is enabled by default in SonarQube Cloud and must be manually activated in SonarQube Server.
* Running SonarQube for VS Code in connected mode with SonarQube (Server, Cloud). See the pages on [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention") and [setup](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/setup "mention") for more details.

### How to view your dependency risks <a href="#how-to-view-your-dependency-risks" id="how-to-view-your-dependency-risks"></a>

In SonarQube for VS Code, dependency risks are displayed in the **SONARQUBE** Panel.

<figure><img src="https://assets-eu-01.kc-usercontent.com/b1eeb429-d9e0-0100-be87-468f6802040a/2058fda7-08c2-406d-a0a6-c7e44ece2f82/dependency-risks-sq-for-vs-code.png?w=1401&#x26;h=955&#x26;auto=format&#x26;fit=crop" alt="List of dependency risks under the SONARQUBE panel in VS Code"><figcaption></figcaption></figure>

For each dependency risk, the following information is displayed:

* **Risk type**: Vulnerability and Prohibited license
* **Risk severity**: Blocker, High, Medium, Low, or Info
* **Package name**
* **Package version**

You can select a risk to open it in SonarQube Server to get more details.

### Fixing dependency risks <a href="#fixing-dependency-risks" id="fixing-dependency-risks"></a>

Because dependency risk analysis requires that you run in connected mode, any changes you make to the code must be analyzed by your instance of SonarQube (Server, Cloud). Here are two options to resolve dependency risks displayed by SonarQube for VS Code:

* After you fix the dependency risk in your IDE, commit your code and rerun the analysis on SonarQube Server or SonarQube Cloud. The new status of the risk will be reflected in your IDE.
* Mark the dependency risk as **Confirmed**, **Accepted**, or **Safe** directly from the VS Code UI or SonarQube (Server, Cloud). You can also add comments. The status update is then reflected in VS Code or SonarQube (Server, Cloud).
