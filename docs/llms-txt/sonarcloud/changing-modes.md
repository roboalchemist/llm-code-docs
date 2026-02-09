# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/code-metrics/changing-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/changing-modes.md

# Changing instance modes

### The concept of two modes <a href="#two-modes-concept" id="two-modes-concept"></a>

Starting with SonarQube Server 10.8 we are introducing the concept of two modes: [standard-experience](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/standard-experience "mention") and [mqr-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/instance-mode/mqr-mode "mention").

In Standard Experience, you can use familiar workflows and categorization for issues such as bugs, vulnerabilities, and code smells without impacting your way of working.

### Standard Experience metrics <a href="#standard-experience-metrics" id="standard-experience-metrics"></a>

The Standard Experience encompasses the use of rule types such as bugs, code smells, and vulnerabilities, with a single type and severity level for each rule. This approach focuses on assigning severity to a rule based on the single software quality (security, reliability, or maintainability) it has the largest impact on.

Severities in Standard Experience (Blocker, Critical, Major, Minor, and Info) are applied at the overall rule level.

### Multi-Quality Rule Mode metrics <a href="#mqr-mode-metrics" id="mqr-mode-metrics"></a>

The new MQR Mode aims to more accurately represent the impact an issue has on all [software-qualities](https://docs.sonarsource.com/sonarqube-server/user-guide/rules/software-qualities "mention"). It does this by assigning a separate severity to a rule for each software quality it might impact. This approach focuses on ensuring the impact on all affected software qualities is clear, not just the one most severely impacted.

Severities in MQR Mode (Blocker, High, Medium, Low, and Info) are applied at the software quality level.

### Example and comparison <a href="#example-comparison" id="example-comparison"></a>

To illustrate the difference between Standard Experience and MQR Mode, let’s examine the [Arguments in long RUN instructions should be sorted](https://rules.sonarsource.com/docker/RSPEC-7018/) rule in Docker:

* When your code breaks this rule in Standard Experience an issue is raised with a Code Smell type and Minor severity level.
* In MQR Mode, however, an issue is raised that impacts all three software qualities at different severity levels: Maintainability (Medium), Reliability (Low), and Security (Low). This provides you with a more comprehensive picture of the issue’s impact on your project.

### Switching modes <a href="#switching-modes" id="switching-modes"></a>

#### Permissions <a href="#permissions" id="permissions"></a>

To change from Standard Experience to MQR Mode and vice versa, you need instance admin permissions.

To switch the mode in your SonarQube Server instance go to **Administration** > **Configuration** > **General Settings** > **Mode** and select either **Standard Experience** or **Multi-Quality Rule Mode**.

#### From Standard Experience to MQR Mode <a href="#standard-experience-to-mqr" id="standard-experience-to-mqr"></a>

After switching to MQR Mode you will notice some changes in your SonarQube Server instance:

* The severities levels for rules, issues and ratings are now Blocker, High, Medium, Low, and Info.
* Bugs, Vulnerabilities, and Code Smells are replaced with software qualities: Reliability, Security, and Maintainability. Security vulnerabilities are replaced with Security in Portfolios and Security Reports.
* Since issues might impact multiple software qualities, the number of issues may increase. This might also impact the outcome of your quality profiles and quality gates.
* You might have to update the conditions of custom Quality Gates to use them with the MQR metrics as some metrics might impact more than one software quality.
* Check if your API calls to the Sonar solution use the correct MQR Mode metrics. See the [metrics-definition](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition "mention") page for more details.
* If you are using the generic issue format for the analysis report, you must use the latest format version as outlined on the [generic-issue-import-format](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/generic-issue-import-format "mention") page. Otherwise, all issues will appear with Maintainability set to Medium when you switch to MQR Mode.

#### From MQR Mode to Standard Experience <a href="#mqr-to-standard-experience" id="mqr-to-standard-experience"></a>

After switching to Standard Experience you will notice some changes in your SonarQube Server instance:

* The severities levels for rules, issues and ratings are now Blocker, Critical, Major, Minor, and Info.
* Reliability, Security, and Maintainability are replaced with Bugs, Vulnerabilities, and Code Smells types. Security is replaced with Security Vulnerabilities in Portfolios and Security Reports.
* Since issues impact only one type you might see different outcomes in your quality profiles and quality gates.
* You might have to update the conditions of custom Quality Gates to use them with the Standard Experience metrics.
* Check if your API calls to the Sonar solution use the correct Standard Experience metrics. See the Metric definitions page for more details.
* If you are using the generic issue format for the analysis report, you must use the latest format version as outlined on the [generic-issue-import-format](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/generic-issue-import-format "mention") page.
