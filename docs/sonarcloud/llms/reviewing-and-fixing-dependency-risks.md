# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/advanced-security/reviewing-and-fixing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/advanced-security/reviewing-and-fixing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/advanced-security/reviewing-and-fixing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/advanced-security/reviewing-and-fixing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-server/advanced-security/reviewing-and-fixing-dependency-risks.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-security/reviewing-and-fixing-dependency-risks.md

# Reviewing and fixing dependency risks

Advanced Security is an add-on that requires a separate subscription to your SonarQube Cloud's [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

SonarQube Cloud lets you manage dependency risks, mark them as safe, confirmed, or accepted, and assign them to other members of your team.

### Permissions <a href="#permissions" id="permissions"></a>

On private projects, and portfolios, the following permissions apply:

* **Browse**: access, browse, confirm dependency risks, change assignee.
* **Administer issues**: change risk severity, resolve risks as **Accepted** or **Safe**.

Anyone is allowed to browse dependency risks on public projects and portfolios.

Changing the status of a dependency risk requires the **Administer Issues** permission.

### Reviewing and fixing dependency risks <a href="#reviewing-and-fixing-dependency-risks" id="reviewing-and-fixing-dependency-risks"></a>

Navigate to the **Dependency Risks** tab of your project or portfolio.

Use **Filters** in the left side bar to narrow down the results. You can filter the results by:

* **Risk type**: Vulnerability, Malicious package, and Prohibited license
* **Risk severity**: Blocker, High, Medium, Low, or Info
* **Software quality**: Security, Maintainability
* **Dependency type**: Direct or Transitive
* **Dependency scope**: Production or Development
* **Package manager**: See [Analyzing project for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca) for a list of supported package managers and languages.
* **Status**: Accepted, Confirmed, Open, Fixed, Safe
* **Assignee**: Type in the name of the person assigned and select it from the list.

From there, you can sort the list of results:

* by choosing the sorting criteria from the **Sort by** dropdown menu
* by vulnerability name by entering a vulnerability ID (such as CVE-2022-38392) into the search box

The following information is displayed for each dependency risk in the list:

<figure><img src="data:image/svg+xml;charset=utf-8,%3Csvg%20height=&#x27;369&#x27;%20width=&#x27;1028&#x27;%20xmlns=&#x27;http://www.w3.org/2000/svg&#x27;%20version=&#x27;1.1&#x27;%3E%3C/svg%3E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://assets-eu-01.kc-usercontent.com/b1eeb429-d9e0-0100-be87-468f6802040a/128422bc-f650-4fce-aa68-92a22004b833/dependency-risk-card.png?w=1028&#x26;h=369&#x26;auto=format&#x26;fit=crop" alt="Information on each dependency risk card." height="369" width="1028"><figcaption></figcaption></figure>

1. Descriptive title of the dependency risk. Click on the title to open a detailed view.
2. Software quality, risk type, and severity
3. Status: Open, Confirmed, Accepted, Safe
4. Assignee of the risk
5. Amount of time that has passed since the risk was first detected
6. Affected dependency and version

### Understanding the risk types <a href="#understanding-the-risk-types" id="understanding-the-risk-types"></a>

Each dependency risk has an assigned risk type:

* **Vulnerability**: When a third-party dependency is affected by a publicly reported vulnerability, such as a record on [CVE.org](http://cve.org/)
* **Malicious package**: When a third-party dependency is known to be malicious
* **Prohibited license**: When a third-party dependency has a software license not allowed by the project's associated [license profile and policy](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies).

### Changing dependency status and assigning risks <a href="#changing-dependency-status-and-assigning-risks" id="changing-dependency-status-and-assigning-risks"></a>

#### Dependency risk lifecycle <a href="#dependency-risk-lifecycle" id="dependency-risk-lifecycle"></a>

A dependency risk can have the following statuses:

* **Open**: Initial state of a dependency risk after analysis. The risk has not been yet reviewed.
* **Confirmed**: Indicates that the dependency risk has been reviewed and the risk is valid.
* **Accepted**: The risk is valid but it may not be fixed for a while.
* **Safe**: Indicates that the dependency risk does not compromise the security of the software. A mandatory justification must be provided.

To change the status of the dependency risk, click the **Change Status** button to open a modal. From the **Status** dropdown list select a new status for the risk and enter a description for the change in the **Explain your decision** text box.

#### Assigning a dependency risk <a href="#assigning-a-dependency-risk" id="assigning-a-dependency-risk"></a>

You can delegate a review of dependency risks to other team members by clicking the **Unassigned** dropdown menu and entering a name. You can also assign the risk to yourself.

#### Email notifications <a href="#email-notifications" id="email-notifications"></a>

If you have subscribed to [email notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications) for a project, note that the notifications that apply to issues also apply to dependency risks.

### Detailed view <a href="#detailed-view" id="detailed-view"></a>

Clicking the title of the dependency risk in the list of results opens its detailed view page:

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-173521ea0ca2dc7d2a299e789557fc131e70b96c%2Fimage%20(6).png?alt=media" alt="The detailed view of a dependency risks in SonarQube Cloud"><figcaption></figcaption></figure>

<figure><img src="data:image/svg+xml;charset=utf-8,%3Csvg%20height=&#x27;1424&#x27;%20width=&#x27;3214&#x27;%20xmlns=&#x27;http://www.w3.org/2000/svg&#x27;%20version=&#x27;1.1&#x27;%3E%3C/svg%3E" alt=""><figcaption></figcaption></figure>

1. Details of the dependency risk, including **Risk type**, **Risk Severity**, **First detected**, **Assignee**, and **Status**.
2. **What’s the Risk?** and **How can I fix it?** allow you to review information about the dependency risk, the factors affecting the risk’s severity, and information about currently used dependency versions and fixes.
3. **Affected dependencies** shows the dependency version that raised the risk, dependency type, package manager and the associated risks. Click the **View all risks for this dependency** for a full list.

### What’s the risk? <a href="#whats-the-risk" id="whats-the-risk"></a>

Sonar uses a holistic approach to determine the severity of a dependency risk. The methods used depend on the associated risk type.

<figure><img src="data:image/svg+xml;charset=utf-8,%3Csvg%20height=&#x27;230&#x27;%20width=&#x27;512&#x27;%20xmlns=&#x27;http://www.w3.org/2000/svg&#x27;%20version=&#x27;1.1&#x27;%3E%3C/svg%3E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://assets-eu-01.kc-usercontent.com/b1eeb429-d9e0-0100-be87-468f6802040a/5789f5e3-7835-4203-99a2-5ce64a0eaf24/whats-the-risk-tab.png?w=512&#x26;h=230&#x26;auto=format&#x26;fit=crop" alt="The &#x22;What&#x27;s the risk&#x22; tab in the UI." height="230" width="512"><figcaption></figcaption></figure>

#### Vulnerability risk <a href="#vulnerability-risk" id="vulnerability-risk"></a>

Sonar partners with select open source maintainers to uphold their software to secure development practices. As part of this partnership, Sonar-partnered maintainers provide guidance on vulnerabilities. This guidance includes:

* Whether the vulnerability is real, or a false positive
* How likely it is that the vulnerability will affect typical usage
* Whether the vulnerability affects development or test usage, or only production usage
* What workarounds, if any, are available
* What specific functions or methods are affected

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a64ac4c5dba62b3e6856325798ee309f01b95b49%2Fimage%20(7).png?alt=media" alt="The Insights from the maintainer tab in the SonarQube UI."><figcaption></figcaption></figure>

This guidance ensures that developers have comprehensive information to speed up remediation times.

**Risk evaluation**

The risk evaluation is based on the following factors:

* **Severity**: Evaluates the technical severity of a vulnerability based on an assessment by [CVSS](https://www.first.org/cvss/).
* **Known exploited**: Shows if the risk has been actively exploited in the wild. It’s measured by [KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
* **Chance of future exploitation**: Estimates the likelihood (percentage) of a software vulnerability being exploited in the wild over the next 30 days. It’s measured by [EPSS](http://first.org/epss).

Sonar combines these factors to assign a severity to a discovered vulnerability to ensure that developers are prioritizing the most urgent risk in their applications.

#### Malicious package risk <a href="#malicious-package-risk" id="malicious-package-risk"></a>

Malicious package risks are always BLOCKER severity. They should be remediated immediately.

#### Prohibited license risk <a href="#prohibited-license-risk" id="prohibited-license-risk"></a>

The dependency risk for prohibited license risk type depends on the configuration of your instance’s license profile and policy. The **What’s the risk?** tab provides information about the risk associated with the license and links to relevant resources. For more information, see [Managing license profiles and policies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies).

### Dependency risk severities <a href="#risk-severities" id="risk-severities"></a>

The table below lists the dependency risk severities used for vulnerability risks and their definition.

| **Risk severity** | **Definition**                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blocker           | A vulnerability is on the CISA KEV list.                                                                                                                                                                                                                                                                                                                                               |
| High              | <p>Vulnerability has both:</p><ul><li>High exploitability (an EPSS probability greater than 5%)</li><li>High risk (a CVSS score over 7.0)</li></ul>                                                                                                                                                                                                                                    |
| Medium            | <p>Any other vulnerability that has both:</p><ul><li>Moderate or unknown exploitability (an EPSS probability greater than 0.5%, or no EPSS scoring)</li><li>Moderate risk (a CVSS score over 4.0)</li></ul>                                                                                                                                                                            |
| Low               | Any remaining vulnerability that does not fit into another category.                                                                                                                                                                                                                                                                                                                   |
| Info              | <p>Any of the following is true:</p><ul><li>A Tidelift or Sonar partnered maintainer has declared the vulnerability a false positive</li><li>The vulnerability has been declared as <em>withdrawn</em> by a vulnerability source (NIST, OSV)</li></ul><p>Note: this categorization for Info overrides any criteria that would place the risk into Critical, High, or Low severity.</p> |

**Editing risk severities**

If you decide that a different level is more appropriate for a given risk, you can manually set a new severity level. Keep in mind that doing so may impact your quality gates.

To customize the risk severity level for **Software qualities impacted**:

1. Select a risk from the search results list.
2. Click on the quality: **Security**, **Reliability**, or **Maintainability**.
3. Select the severity level you wish to apply from the dropdown list. You can also change the severity level from the risk's details page.

Note that if you manually update the severity level for a risk, it will no longer be updated automatically by Sonar, even if the data used in the severity calculation changes.

### How can I fix it? <a href="#how-can-i-fix-it" id="how-can-i-fix-it"></a>

#### Vulnerability <a href="#vulnerability" id="vulnerability"></a>

The **How can I fix it?** tab displays information about dependency versions, starting with the latest, and available fixes.

<figure><img src="data:image/svg+xml;charset=utf-8,%3Csvg%20height=&#x27;444.99999999999994&#x27;%20width=&#x27;512&#x27;%20xmlns=&#x27;http://www.w3.org/2000/svg&#x27;%20version=&#x27;1.1&#x27;%3E%3C/svg%3E" alt=""><figcaption></figcaption></figure>

<figure><img src="https://assets-eu-01.kc-usercontent.com/b1eeb429-d9e0-0100-be87-468f6802040a/9ae308e9-c13f-468b-b7a8-babb41abf82e/how-can-i-fix-it-tab.png?w=512&#x26;h=445&#x26;auto=format&#x26;fit=crop" alt="The &#x22;How can I fix it&#x22; tab for dependency risks in the SonarQube UI." height="444.99999999999994" width="512"><figcaption></figcaption></figure>

The following options are available:

* **Complete fix**: A dependency version that fixes all associated vulnerabilities.
* **Partial fix**: A dependency version that fixes the vulnerability but not all other vulnerabilities associated with the dependency.
* **Affected version**: A dependency version for which the vulnerability was detected.

#### Malicious package \<a href="malicious-package" id="malicious-package"

Any machine that has an installed a malicious piece of software should be considered compromised and remediated immediately. The How can I fix it? tab provides steps that should be followed when malware is detected, including informing your information security team.

#### Prohibited license <a href="#prohibited-license" id="prohibited-license"></a>

The dependency risk for prohibited license risk type depends on the configuration of your instance’s license profile and policy. The How can I fix it? tab provides information about different license categories and links to relevant resources. In general, resolving a license risk will require choosing a different software package to use instead. For more information, see [Managing license profiles and policies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies).

### Setting a license profile and policy <a href="#setting-a-license-profile-and-policy" id="setting-a-license-profile-and-policy"></a>

Instance admins can configure a license profile and policy to define which licenses are allowed or prohibited for the dependencies used in your projects or the whole instance. For more information, see Managing license profiles and policies.

### Dependency risks in quality gates <a href="#dependency-risks-in-quality-gates" id="dependency-risks-in-quality-gates"></a>

The **Project overview** page displays dependency risks and indicates whether they pass or fail the associated quality gate.

As a quality gate administrator, you can configure quality gate conditions for **Prohibited license**, **Malicious package**, and **Vulnerability** types for new and overall code, or set limits on the number or severity of dependency risks that will cause the quality gate to fail. See [Managing custom quality gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates) for more information.

If your organization has recently purchased the Advanced Security package, you will have to create a custom quality gate to make sure no new dependency risks are introduced in your projects.

See [Understanding measures and metrics](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions) for more information about Advanced Security metrics used in quality gates.

### Downloading a dependency risk report <a href="#downloading-a-dependency-risk-report" id="downloading-a-dependency-risk-report"></a>

You can download a report of the dependency risks for your project, applications, and portfolios from the project overview page, or by calling a [SonarQube Cloud API endpoint](https://api-docs.sonarsource.com/sonarqube-cloud/default/public-dependencyservice-v1-1).

The report lists dependency risks based on the latest scan for the default branch of your project, application or portfolio. It can help managers identify:

* What violations exist in their team’s projects
* What patterns of risk are associated with higher-level dependencies, and how to use the information to guide developers effectively
* What specific upgrades developers can perform to remove multiple violations.

The report is downloaded JSON and CSV format and contains information on:

* Project, Application, Portfolio
* Dependency chain(s)
* Risk title (a short description of the risk)
* Risk type
* Risk severity
* Risk status, including comments when status was changed
* CVSS score associated to the risk
* CVE and CWE ids, if relevant
* Date when Sonar assigned the Risk to the project

### Related pages <a href="#related-pages" id="related-pages"></a>

* [Viewing dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/viewing-dependencies)
* [Analyzing projects for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca)
* [Managing license profiles and policies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies)
* [Troubleshooting](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/troubleshooting-the-dependency-analysis)
* [Best practices for managing dependency risks](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/best-practices-for-managing-dependency-risks)
