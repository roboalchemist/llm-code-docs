# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/release-notes-and-notices/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/release-notes-and-notices/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/release-notes.md

# Release notes

These release notes describe the relevant changes implemented for SonarQube Server 2026.1 LTA. If you’re upgrading from the previous LTA, see the [lta-to-lta-release-notes](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/lta-to-lta-release-notes "mention"). For a complete list of all changes, see the [#full-release-notes](#full-release-notes "mention").

### New and enhanced features <a href="#new-and-enhanced-features" id="new-and-enhanced-features"></a>

View the release notes for new and enhanced features for SonarQube Server.

<details>

<summary>2026.1</summary>

#### AI and mobile compliance reporting

Extends our regulatory coverage to include critical AI and Mobile security standards such as OWASP Top 10 for LLM and OWASP MASVS for project security reports. This feature is available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarqube/) edition and above. See [security-related-rules](https://docs.sonarsource.com/sonarqube-server/user-guide/rules/security-related-rules "mention") for more information.

#### Feedback mechanism for self-hosted LLMs

Improves the success rate of generating valid AI CodeFix suggestions from self‑hosted LLMs.

#### JFrog Evidence Collection with SonarQube Server

This integration provides a single, verifiable audit trail if you use both SonarQube and JFrog with strict audit trail and compliance requirements. SonarQube analysis results are automatically signed and directly attached to your JFrog packages to create a single, verifiable source of truth. You no longer have to jump between tools to prove your code meets security standards. Everything you need for a rigorous audit is now visible within the JFrog Evidence Collection interface. This feature is available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarqube/) edition and above. See [jfrog-evidence-collection-integration](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/jfrog-evidence-collection-integration "mention") for more information.

#### SonarQube Advanced Security&#x20;

This feature is available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarqube/) edition and above.

**Malicious package detection**

Receive blocker-level alerts if a dependency matches publicly known datasets of known malicious packages. See [advanced-security](https://docs.sonarsource.com/sonarqube-server/advanced-security "mention") for more information.

#### Quality gate fudge factor improved

To avoid overly strict enforcement of small changes, the quality gate ignores coverage and duplication conditions for very small sets of new code. See [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/changing-default-quality-gate "mention") for more information.

#### Languages

**Cobol**

Adds support for parsing additional language constructs and includes fixes for crashes and false positives for [cobol](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/cobol "mention"). Related rules include:

* [S3938](https://rules.sonarsource.com/cobol/RSPEC-3938/): Track uses of forbidden statements
* [S1725](https://rules.sonarsource.com/cobol/RSPEC-1725/): Open files should be closed explicitly
* [S1574](https://rules.sonarsource.com/cobol/RSPEC-1574/): Data items should be initialized with data of the correct type
* [S1289](https://rules.sonarsource.com/cobol/RSPEC-1289/): Unused data item blocks should be removed

**IaC**

The analysis of Infrastructure as Code (Ansible, Azure Resource Manager, CloudFormation, Docker, Kubernetes, Terraform, Shell, GitHub Actions) has been improved.

Helm templates are now evaluated even if values.yaml is missing.

The following rules have been added:

* [S6437](https://rules.sonarsource.com/azureresourcemanager/RSPEC-6437/): Credentials should not be hard-coded
* [S7638](https://rules.sonarsource.com/githubactions/RSPEC-7638/): ACTIONS\_ALLOW\_UNSECURE\_COMMANDS should not be used
* [S8232](https://rules.sonarsource.com/githubactions/RSPEC-8232/): Workflows should not rely on unverified GitHub context values to trust events
* [S8233](https://rules.sonarsource.com/githubactions/RSPEC-8233/): Write permissions should be defined at the job level
* [S8262](https://rules.sonarsource.com/githubactions/RSPEC-8262/): Artifacts should not contain secrets
* S8263: GitHub Action invocations should not be vulnerable to parameter injection attacks
* [S8264](https://rules.sonarsource.com/githubactions/RSPEC-8264/): Read permissions should be defined at the job level

**JCL**

A new `leaveFile` API is available for custom rules for [jcl](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/jcl "mention") language, giving rule authors more control over how files are processed and reported.

**.NET 10 and C# 14 support**

Empowers .NET teams to adopt the Long Term Support (LTS) release of .NET 10 and C# 14 immediately, ensuring their analysis remains accurate, performant, and free of false positives associated with new language constructs. See [vb-dotnet](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/vb-dotnet "mention") and [csharp](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/csharp "mention") for more information.

Related rules:

* [S1121](https://rules.sonarsource.com/csharp/RSPEC-1121/): Assignments should not be made from within sub-expressions
* [S1144](https://rules.sonarsource.com/csharp/RSPEC-1144/): Unused private types or members should be removed
* [S2225](https://rules.sonarsource.com/csharp/RSPEC-2225/): "ToString()" method should not return null
* [S2292](https://rules.sonarsource.com/csharp/RSPEC-2292/): Trivial properties should be auto-implemented
* [S2325](https://rules.sonarsource.com/csharp/RSPEC-2325/): Methods and properties that don't access instance data should be static
* [S2583](https://rules.sonarsource.com/csharp/RSPEC-2583/): Conditionally executed code should be reachable
* [S2589](https://rules.sonarsource.com/csharp/RSPEC-2589/): Boolean expressions should not be gratuitous
* [S2692](https://rules.sonarsource.com/csharp/RSPEC-2692/): "IndexOf" checks should not be for positive numbers
* [S2953](https://rules.sonarsource.com/csharp/RSPEC-2953/): Methods named "Dispose" should implement "IDisposable.Dispose"
* [S2970](https://rules.sonarsource.com/csharp/RSPEC-2970/): Assertions should be complete
* [S3063](https://rules.sonarsource.com/csharp/RSPEC-3063/): "StringBuilder" data should be used
* [S3264](https://rules.sonarsource.com/csharp/RSPEC-3264/): Events should be invoked
* [S3398](https://rules.sonarsource.com/csharp/RSPEC-3398/): "private" methods called only by inner classes should be moved to those classes
* [S3459](https://rules.sonarsource.com/csharp/RSPEC-3459/): Unassigned members should be removed
* [S3877](https://rules.sonarsource.com/csharp/RSPEC-3877/): Exceptions should not be thrown from unexpected methods
* [S3928](https://rules.sonarsource.com/csharp/RSPEC-3928/): Parameter names used into ArgumentException constructors should match an existing one
* [S4545](https://rules.sonarsource.com/csharp/RSPEC-4545/): "DebuggerDisplayAttribute" strings should reference existing members
* [S7039](https://rules.sonarsource.com/csharp/RSPEC-7039/): Content Security Policies should be restrictive

**PHP**

Reduces false positives on several rules and cleans up build and dependency infrastructure for [php](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/php "mention"). Related rules:

* [S1155](https://rules.sonarsource.com/php/RSPEC-1155/): "empty()" should be used to test for emptiness
* [S1172](https://rules.sonarsource.com/php/RSPEC-1172/): Unused function parameters should be removed
* [S2699](https://rules.sonarsource.com/php/RSPEC-2699/): Tests should include assertions
* [S1068](https://rules.sonarsource.com/php/RSPEC-1068/): Unused "private" fields should be removed

**Scala**

Include fixes to false positives and negatives for [scala](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/scala "mention") on the following rules:

* [S1192](https://rules.sonarsource.com/scala/RSPEC-1192/): String literals should not be duplicated
* [S126](https://rules.sonarsource.com/scala/RSPEC-126/): "if ... else if" constructs should end with "else" clauses

**Secrets**

[secrets](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/secrets "mention") rules have been improved to reduce the detection of false positives and the following rule have been added:

* [S6418](https://rules.sonarsource.com/yaml/RSPEC-6418/): Hard-coded secrets are security-sensitive
* [S2068](https://rules.sonarsource.com/yaml/RSPEC-2068/): Hard-coded passwords are security-sensitive
* [S7552](https://rules.sonarsource.com/secrets/RSPEC-7552/): SMTP credentials should not be disclosed
* [S8350](https://rules.sonarsource.com/secrets/RSPEC-8350/): xAI API keys should not be disclosed

**VB6**

Fixes parse errors and line count for [vb6](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/vb6 "mention"). Related rules:

* [S138](https://rules.sonarsource.com/vb6/RSPEC-138/): Subs and functions should not have too many lines
* [S1151](https://rules.sonarsource.com/vb6/RSPEC-1151/): "Case" clauses should not have too many lines

</details>

### Update notes <a href="#upgrade-notes" id="upgrade-notes"></a>

This section contains notes about breaking changes and important updates to be aware of before updating. If you’re updating from the previous LTA, see [LTA to LTA release notes](https://app.gitbook.com/s/4FzELVjsPO4ijRo3jtBV/server-update-and-maintenance/release-notes-and-notices/lta-to-lta-release-notes "mention").

<details>

<summary>2026.1</summary>

#### Java requirements for SonarQube Server runtime

* The SonarQube Server runtime now requires Java Development Kit (JDK). The previous requirement of a Java Runtime Environment (JRE) is no longer sufficient, and a full JDK is required.
* Added Support for Java 25 in addition to Java 21.&#x20;
* Removed support for Java 17.

See [#software-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements#software-requirements "mention") for more details.

#### PostgreSQL support

Support for PostgreSQL versions 14 through 18 is now available, enabling deployments using the most recent PostgreSQL release. PostgreSQL version 13 is not supported anymore. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention") for more information.

#### Kubernetes and Openshift support

* Supported Kubernetes Versions: From 1.32 to 1.35. Support for versions 1.30 and 1.31 has been removed.
* Supported Openshift Versions: From 4.17 to 4.20. Support for versions 4.11 to 4.16 has been removed.

#### Support for MSSQL server

Supported MSSQL server is now 2022 (MSSQL Server 16.0); 2019 (MSSQL Server 15.0); 2017 (MSSQL Server 14.0). Support for 2016 MSSQL Server 13.0 support has been removed. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention") for more information.

#### SonarQube Server includes Elasticsearch 8.x

SonarQube Server 2026.1 LTA and later includes Elasticsearch 8.x, which requires read and write access to the `/tmp` directory. This is a requirement from Elasticsearch itself and cannot be disabled. For more information and a solution, see [#fonts](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux#fonts "mention").

</details>

### Deprecations and removals <a href="#deprecations-and-removals" id="deprecations-and-removals"></a>

This section contains information on the deprecation and removal of SonarQube Server features and API endpoints. See the [deprecation-policy](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/deprecations/deprecation-policy "mention") for more information.

<details>

<summary>2026.1</summary>

#### Java 17 not supported any more

Java version 21 is the minimum version required to run SonarQube Server. See [#software-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements#software-requirements "mention") for more details.

#### PostgreSQL in Helm charts removed

The deprecated PostgreSQL dependency in the Helm chart has been removed. If you were relying on this dependency for production, you must take the following steps to upgrade to the new chart: back up their existing database, import the data into a new database, and then update the JDBC URL within the SonarQube chart configuration. See [installing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installing-helm-chart "mention") for more information.

#### Kubernetes and Openshift versions removed

* Support for versions 1.30 and 1.31 has been removed.
* Support for versions 4.11 to 4.16 has been removed.

#### 2016 MSSQL Server 13.0 support removed

Support for 2016 MSSQL Server 13.0 support has been removed. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention")  for more information.

#### Deprecation of Ingress NGINX

Due to the retirement of the ingress-nginx controller in November 2025 (with best-effort support ceasing in March 2026), the dependency on this chart is now deprecated.

We advise migrating to the [Gateway API](https://gateway-api.sigs.k8s.io/guides/), which is the modern successor to Ingress. Should you need to continue using Ingress, consult the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) for a list of suitable alternative controllers. A replacement dependency will be provided in a future release.

#### Deprecation of Automatic AI Code Detection

Autodetect AI-Generated Code has been deprecated. Sonar will adjust the AI Code Assurance offering to adapt to the industry changes with high AI adoption. A warning callout has been added to the SonarQube UI in global and project settings. See [ai-code-assurance](https://docs.sonarsource.com/sonarqube-server/ai-capabilities/ai-code-assurance "mention") for more information.

</details>

### Full release notes <a href="#full-release-notes" id="full-release-notes"></a>

Links to the full release notes in Jira:

* [2026.1](https://sonarsource.atlassian.net/issues?jql=project%20%3D%2010139%20AND%20issuetype%20!%3D%20Task%20AND%20fixversion%20%3D%2023523)

### Related page

* [lta-to-lta-release-notes](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/lta-to-lta-release-notes "mention")
