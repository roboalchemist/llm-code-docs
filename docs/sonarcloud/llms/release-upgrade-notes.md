# Source: https://docs.sonarsource.com/sonarqube-server/8.9/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/release-notes-and-notices/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/release-notes-and-notices/release-upgrade-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/release-upgrade-notes.md

# Release update notes

This page contains notes about breaking changes and important updates to be aware of before upgrading. We recommend reading the notes for all the versions between your current version and the version you’re upgrading to.

If you’re upgrading from the previous LTA, see [lta-to-lta-release-upgrade-notes](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/lta-to-lta-release-upgrade-notes "mention").

For the list of new features in this version, see the [release-notes](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/release-notes "mention").

### Release 2025.1 upgrade notes <a href="#release-2025.1-upgrade-notes" id="release-2025.1-upgrade-notes"></a>

**Update in PostgreSQL support**

PostgreSQL versions 11 and 12 are no longer supported. Supported versions are now from 13 to 17.

**SAML configuration update required**

When configuring SAML on your SonarQube Server instance with assertion encryption, the response signature must be enforced. You might need to update your SAML configuration:

* If you use SAML with Microsoft Entra, make sure you sign the response by selecting **Sign SAML response** or **Sign SAML response and assertion** as the sign-in response. See **Step 2 > If you use encryption, enforce response signature** in [optional-security-features](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ms-entra-id/optional-security-features "mention").
* If you use SAML with PingID, make sure you sign the response by selecting **Sign Response** or **Sign Assertion & Response** as the sign-in response. See **Step 2 > To enable the encryption of SAML assertions** in [optional-security-features](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/ms-entra-id/optional-security-features "mention").

In addition, the assertion decryption now requires that you also store the public key certificate in SonarQube Server (not only the private key). Make sure the certificate is stored in SonarQube as follows:

1. In SonarQube Server, go to **Administration > Configuration > General Settings > Authentication > SAML**.
2. In **SAML Configuration > SAML**, select **Edit**. The **Edit SAML configuration** dialog opens.
3. In **Service provider certificate**, enter the certificate.

**Server base URL setup now mandatory for SAML authentication**

Your SAML authentication setup will not work if the SonarQube Server base URL is not set in SonarQube Server. See [server-base-url](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/server-base-url "mention").

**If migrating from 10.7: AI Code Assurance lost on projects**

In SonarQube Server 10.7, the **Sonar way** quality gate was enforced on projects marked as containing AI Code. If you’re migrating from this version, these projects will loose AI Code Assurance. To resolve this, you must apply a quality gate qualified for AI Code Assurance to these projects. To do so, you can use the **Sonar way for AI Code** quality gate or a custom quality gate you have qualified for AI Code Assurance. See [ai-standards](https://docs.sonarsource.com/sonarqube-server/2025.1/ai-capabilities/ai-standards "mention").

### Release 10.8 upgrade notes <a href="#release-10.8-upgrade-notes" id="release-10.8-upgrade-notes"></a>

**Instance mode feature**

Your SonarQube Server instance has two modes to choose from: [standard-experience](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/instance-mode/standard-experience "mention") and [mqr-mode](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/instance-mode/mqr-mode "mention"). Upon upgrading, existing SonarQube Server 10.1 and earlier are configured with the Standard Experience by default whereas SonarQube Server 10.2 and later are configured with MQR mode.

For details on switching modes, see the [changing-modes](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/code-metrics/changing-modes "mention") page.

### Release 10.7 upgrade notes <a href="#release-10.7-upgrade-notes" id="release-10.7-upgrade-notes"></a>

**Updated GitLab automatic provisioning feature**

Automatic user and group provisioning with GitLab now includes permission synchronization, which automatically synchronizes project visibility:

* To prevent unwanted updates to project permissions and project visibility, upgrading SonarQube will suspend automatic provisioning until you confirm the choice of provisioning method in the authentication settings.

For details, see the [setting-up](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/setting-up "mention") page.

**Disable the confidential header in portfolio PDF reports**

Admin users have a new toggle in the **Administration -> Governance -> Portfolio PDF Reports** section, allowing them to dynamically enable or disable the "Confidential" header.

For details, see the [managing-portfolios](https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/managing-portfolios "mention") page.

**API updates**

When querying rules or issues, INFO and BLOCKER may appear as statuses at the quality level (i.e. a rule might have a reliability severity of BLOCKER). You can also create rules and issues with these additional severities. See [Web API](https://next.sonarqube.com/sonarqube/web_api) in the help menu of SonarQube Server.

The affected APIs are:

* api/issues/\*
* api/rules/\*
* api/projects/export\_findings
* api/qualityprofiles/compare
* api/qualityprofiles/changelog

### Release 10.6 upgrade notes <a href="#release-10.6-upgrade-notes" id="release-10.6-upgrade-notes"></a>

There are no upgrade notes for SonarQube 10.6. For the release notes, see [Release notes](https://app.gitbook.com/s/VhGCsZJo9Ao0Jjyhvpxl/setup-and-upgrade/release-notes "mention").

### Release 10.5 upgrade notes <a href="#release-10.5-upgrade-notes" id="release-10.5-upgrade-notes"></a>

**Cognitive complexity calculation updated for Javascript and Typescript**

If you analyze Javascript and Typescript projects, note that we’ve updated how cognitive complexity is calculated. Notably, nested function complexity is no longer added to the parent. This will translate as a drop in the metric for some users.

**End of support of Node.js 16 in the scanner environment**

Node.js 16 is no longer supported as a scanner runtime environment. If you’re using a custom Node.js installation, we recommend the latest [LTS version](https://nodejs.org/en/about/previous-releases), currently v20.

**Updates to custom plugins required**

For a faster analysis, SonarQube now [improving-performance](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/maintenance/improving-performance "mention") by default. To avoid dependency errors, you’ll need to update the configuration of your custom plugins. See [plugin-basics](https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/plugin-basics "mention") for more information. Also, if you use third-party plugins, make sure to use the latest ones compatible with this feature.

[Full release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2015441%20AND%20issuetype%20%21%3D%20Task)

### Release 10.4 upgrade notes <a href="#release-10.4-upgrade-notes" id="release-10.4-upgrade-notes"></a>

**Project overview update**

Issue counts on the overall code of projects now reflect the Clean Code software qualities.

Make sure you re-analyze your projects after upgrading to compute and display these counts.

**JavaScript/TypeScript/CSS configuration**

A minimum of 4GB memory is now [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/javascript-typescript-css "mention"), use `sonar.javascript.node.maxspace` configuration if you encounter memory issues. Also, file encoding errors will now cause an analysis failure, use `sonar.sourceEncoding=UTF-8` if you encounter problems.

**Node.js is no longer a requirement for analysis**

In most cases, installing Node.js in the environment where you’re running analysis is [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/javascript-typescript-css "mention").

**End of support of Node.js 14 in the scanner environment**

Node.js 14 is [no longer supported](https://community.sonarsource.com/t/node-js-v14-no-longer-supported-v16-stops-early-next-year/105428) as a scanner runtime environment. Also, Node.js v16 will soon be unsupported. If you are using a custom Node.js installation, we recommend the [latest LTS version](https://nodejs.org/en/about/previous-releases), currently v20.

**End of support of Java 11 as scanner environment**

Java 11 is no longer supported as a scanner runtime environment. The minimum required version is Java 17. See the [general-requirements](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/scanner-environment/general-requirements "mention") for more information. ([SONAR-21157](https://sonarsource.atlassian.net/browse/SONAR-21157))

**SonarScanner for .NET compatibility**

Starting SonarQube 10.4, analysis of .NET projects requires [SonarScanner for .NET 5.14+](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/5.14.0.78575).

**End of support of MSBuild 14**

MSBuild 14 is no longer supported for scanning .NET code. ​​MSBuild 15 is deprecated and support will be removed in a future version. We recommend using MSBuild 16 as a minimal version. ([SONAR-21554](https://sonarsource.atlassian.net/browse/SONAR-21554))

{% hint style="info" %}
To know which Web API endpoints and parameters are deprecated after an upgrade, see [api-deprecation](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/monitoring/api-deprecation "mention").
{% endhint %}

<details>

<summary>Full release notes</summary>

[Version 10.4.1 release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2015509%20AND%20issuetype%20!%3D%20Task)\
[Version 10.4 release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2014265%20AND%20issuetype%20!%3D%20Task)

</details>

### Release 10.3 upgrade notes <a href="#release-10.3-upgrade-notes" id="release-10.3-upgrade-notes"></a>

**Updated quality gate conditions for Clean as You Code**

Clean as You Code conditions have evolved: The Sonar way quality gate now uses a 0 issues condition on new code. We recommend updating your custom quality gates after the upgrade. The ratings on the project overview page will stay unchanged while your quality gate may now fail. For details, see [quality-gates](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/quality-gates "mention").

The previous Sonar way quality gate is preserved as "Sonar way (legacy)" upon upgrading. You can keep using it if you’re not ready for the change. ([SONAR-20604](https://sonarsource.atlassian.net/browse/SONAR-20604) & [SONAR-20607](https://sonarsource.atlassian.net/browse/SONAR-20607))

[Full release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2014267%20AND%20issuetype%20!%3D%20Task)

### Release 10.2 upgrade notes <a href="#release-10.2-upgrade-notes" id="release-10.2-upgrade-notes"></a>

**Maximum new code definition value automatically adjusted in existing projects**

For existing projects, if the value of the **Number of days** option is set to a higher value than 90 before the upgrade, SonarQube automatically changes it to 90. As a consequence, some issues might move out of the new code. See the [about-new-code](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/about-new-code "mention") page for more information. ([SONAR-20155](https://sonarsource.atlassian.net/browse/SONAR-20155))

**Updated GitHub automatic provisioning feature**

Automatic user and group provisioning with GitHub now includes permission synchronization, which automatically synchronizes project visibility:

* To prevent unwanted updates to project permissions and project visibility, upgrading SonarQube will suspend automatic provisioning until you confirm the choice of provisioning method in the authentication settings.
* The GitHub app requires new permissions to be added and approved.

For details, see the [github](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/github "mention") page. ([SONAR-20309](https://sonarsource.atlassian.net/browse/SONAR-20309))

**Clean Code updates**

The classification of issues and rules has evolved:

* Issue types are deprecated. Issues are now classified based on Clean Code attributes and software qualities.
* The severity of an issue is now tied to the issue’s impact on the software qualities.

Existing types and severities are preserved and are still used to evaluate the Quality Gate conditions. Type and severity can no longer be edited on issues and rules via the UI.

For details, see [introduction](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/introduction "mention") to Managing issues. ([SONAR-20023](https://sonarsource.atlassian.net/browse/SONAR-20023))

<details>

<summary>Full release notes</summary>

* [Version 10.2.1 release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2014296)
* [Version 10.2 release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2014093)

</details>

### Release 10.1 upgrade notes <a href="#release-10.1-upgrade-notes" id="release-10.1-upgrade-notes"></a>

**Dropping support for NET Framework < 4.6.2**\
The minimum supported .NET Framework version is 4.6.2. Support for earlier versions has been dropped. If you’re running an earlier version, you’ll need to upgrade your build environment wherever your analysis is run. See [this release note](https://github.com/SonarSource/sonar-dotnet/releases/tag/9.0.0.68202) for more information.

**Updated options for new code definition**\
To make them more in line with the Clean as You Code methodology, the following options have been updated for projects:

* Specific analysis: This setup is now available only via the Web API. Automation is required to ensure the value is kept up to date.
* Number of days: The maximum value allowed when setting it up is now 90. It’s recommended to update your existing projects accordingly.

  See the [about-new-code](https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/about-new-code "mention") page for more information. ([SONAR-19294](https://sonarsource.atlassian.net/browse/SONAR-19294))

[Full release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2014087)

### Release 10.0 upgrade notes <a href="#release-10.0-upgrade-notes" id="release-10.0-upgrade-notes"></a>

**SCIM provisioning requires configuration**\
SCIM provisioning for SAML authentication evolves for a tightened synchronization of users and groups. To use the updated set of user and group SCIM provisioning features, see [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/overview "mention").

Without action on your part, upon upgrading, already assigned users are not deleted from SonarQube, but they are no longer bound to your IdP. You’ll need to [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/saml/scim/overview "mention") in SonarQube and adjust your IdP settings. ([SONAR-18797](https://sonarsource.atlassian.net/browse/SONAR-18797)).

**Updated security policy for page extensions**\
To improve security, pages added to the UI by plugins can no longer include inline scripts. If you use this feature, you might need to update your plugins. See [adding-pages-to-the-webapp](https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/adding-pages-to-the-webapp "mention") for more information. ([SONAR-18809](https://sonarsource.atlassian.net/browse/SONAR-18809)).

**Projects displaying modules are no longer supported**\
The concept of modules was removed in v7.6. SonarQube no longer migrates the structure of projects still displaying modules. Make sure you re-analyze these projects before upgrading to SonarQube 10.0. ([SONAR-17706](https://sonarsource.atlassian.net/browse/SONAR-17706)).\
**Deprecated pull request configuration properties removed**\
DevOps Platform Integration settings are no longer inferred from scanner-level analysis parameters, which were deprecated in SonarQube 8.1. To prevent pull request decoration from failing, make sure you have configured each project with the settings found under the project-level **Project Settings > DevOps Platform Integration**.

This particularly affects users integrating with Azure DevOps who formerly relied on the [sonarqube-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/sonarqube-extension-for-azure-devops "mention") to pass these properties. ([SONAR-17711](https://sonarsource.atlassian.net/browse/SONAR-17711)).

**Deprecated web services and parameters removed**\
The web services and parameters that were deprecated in versions 8.x and 9.x have been removed. For more information, see [the corresponding list](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%20SONAR%20AND%20labels%20%3D%2010.0-removed-webapi) and read the [API deprecation policy](https://community.sonarsource.com/t/api-deprecation-policy-change/57998).

**Microsoft SQL Server and Integrated Authentication**\
If you use Microsoft SQL Server with Integrated Authentication, note that the minimum supported version of the [Microsoft SQL JDBC Driver package](https://learn.microsoft.com/en-us/sql/connect/jdbc/release-notes-for-the-jdbc-driver) has been updated to 11.2.3. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/installing-the-database "mention") for more information.

**seccomp filter required on kernel**

The version of Elasticsearch has been updated and now requires a kernel with seccomp enabled. Make sure that seccomp is available on your kernel. See [linux](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation/linux "mention") for more information. ([SONAR-17714](https://sonarsource.atlassian.net/browse/SONAR-17714))

[Full release notes](https://sonarsource.atlassian.net/issues/?jql=project%20%3D%2010139%20AND%20fixVersion%20%3D%2012624)

### Release 9.9 and earlier upgrade notes <a href="#release-9.9-and-earlier-upgrade-notes" id="release-9.9-and-earlier-upgrade-notes"></a>

See the SonarQube Server 9.9 LTA [Release upgrade notes](https://app.gitbook.com/s/Bmptmznn7RpPe5u7vdup/setup-and-upgrade/release-upgrade-notes "mention").
