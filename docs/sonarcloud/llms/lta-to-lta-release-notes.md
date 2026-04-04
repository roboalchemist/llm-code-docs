# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/lta-to-lta-release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/lta-to-lta-release-notes.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/lta-to-lta-release-notes.md

# LTA to LTA release notes

### Updating from SonarQube Server 9.9 LTA and 2025.1 LTA

You can update your SonarQube Server from 2025.1 LTA to 2026.1 LTA directly. However, if you are updating from 9.9 LTA you will need to do an intermediate version update to 2025.1 LTA. Refer to the following documentation for more information:

* 9.9 [LTA to 2025.1 LTA update notes](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/release-notes-and-notices/lta-to-lta-release-notes)&#x20;
* 2025.1 [LTA to 2025.4 LTA update notes](https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/lta-to-lta-release-notes)&#x20;
* The Update [roadmap](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/roadmap "mention") page for detailed procedures.

### 2025.1 LTA to 2026.1 LTA dependencies

<table><thead><tr><th width="166.1484375">Dependency</th><th width="124.109375">2025.1 LTA</th><th width="121.86328125">2025.4 LTA</th><th width="139.609375">2026.1 LTA</th><th>Notes</th></tr></thead><tbody><tr><td>SonarQube Server JRE support</td><td>Java 17 or Java 21</td><td>Java 17 or Java 21</td><td>Java 21 or Java 25 with JDK replacing JRE. </td><td>Support for Java 17 has been removed in 2026.1 LTA. See <a data-mention href="../../server-installation/server-host-requirements#software-requirements">#software-requirements</a></td></tr><tr><td>Microsoft SQL Server</td><td>13.0 - 16.0</td><td>13.0 - 16.0</td><td>14.0 - 16.0</td><td>2016 MSSQL Server 13.0 support has been removed in 2026.1. See <a data-mention href="../../server-installation/installing-the-database#ms-sql-server">#ms-sql-server</a></td></tr><tr><td>Microsoft SQL JDBC Auth package</td><td>12.8.1</td><td>12.10.2</td><td>12.10.2</td><td>See <a data-mention href="../../server-installation/installing-the-database#using-integrated-security">#using-integrated-security</a></td></tr><tr><td>PostgreSQL</td><td>13-17</td><td>13-17</td><td>14-18</td><td>Support for PostgreSQL version 13 has been removed in 2026.1 LTA. See <a data-mention href="../../server-installation/installing-the-database#database-requirements">#database-requirements</a></td></tr><tr><td>Oracle</td><td>21ai, 21C, 19C, XE Editions</td><td>21ai, 21C, 19C, XE Editions</td><td>21ai, 21C, 19C, XE Editions</td><td>See <a data-mention href="../../server-installation/installing-the-database#oracle">#oracle</a></td></tr><tr><td>SonarScanner JRE support (without JRE auto-provisioning)</td><td>Java 17</td><td>Java 17</td><td>Java 21</td><td>Java 17 has been deprecated in 2025.6 and is planned to be removed in 2026.3. See <a data-mention href="../analyzing-source-code/scanners/scanner-environment/general-requirements">general-requirements</a></td></tr><tr><td>PostgreSQL in Helm chart</td><td>deprecated</td><td>deprecated</td><td>removed</td><td>PostgreSQL dependency in Heml chart has been removed in 2026.1</td></tr><tr><td>Ingress Nginx</td><td></td><td></td><td>deprecated</td><td>Will be replaced with an alternative in 2026.2. See <a data-mention href="#deprecations-and-removals">#deprecations-and-removals</a></td></tr><tr><td>Kubernetes support</td><td>1.29 - 1.32</td><td>1.3 - 1.33</td><td>1.32 - 1.35</td><td>See the <a href="https://artifacthub.io/packages/helm/sonarqube/sonarqube">Helm chart</a> documentation.</td></tr><tr><td>Openshift support</td><td>4.11 - 4.17</td><td>4.11 - 4.17</td><td>4.17-4.20</td><td>See the <a href="https://artifacthub.io/packages/helm/sonarqube/sonarqube">Helm chart</a> documentation.</td></tr><tr><td><strong>SonarScanners</strong></td><td></td><td></td><td></td><td>Minimum required SonarScanner version at the time of the SonarQube Server release.</td></tr><tr><td>SonnarScanner CLI</td><td>7.0.1</td><td>7.2</td><td>8.01</td><td>See <a data-mention href="../analyzing-source-code/scanners/sonarscanner">sonarscanner</a></td></tr><tr><td>Azure DevOps extension</td><td>7.1.1</td><td>7.3</td><td>8.0.1</td><td>Compatible with: Azure DevOps Services, Azure DevOps Server (2022.2, 2020.1.2, 2019.1.2.) See <a data-mention href="../analyzing-source-code/scanners/sonarqube-extension-for-azure-devops">sonarqube-extension-for-azure-devops</a></td></tr><tr><td>Jenkins extension</td><td>2.17.3</td><td>2.18</td><td>2.18</td><td>See <a data-mention href="../analyzing-source-code/scanners/jenkins-extension-sonarqube">jenkins-extension-sonarqube</a></td></tr><tr><td>SonarScanner for Maven</td><td>5.0.0.4389</td><td>5.1.0.4751</td><td>5.5.0.6356</td><td>Prerequisite: Maven 3.2.5 or later. See <a data-mention href="../analyzing-source-code/scanners/sonarscanner-for-maven">sonarscanner-for-maven</a></td></tr><tr><td>SonnarScanner for Gradle</td><td>6.0.1.5171</td><td>6.2.0.5505</td><td>7.2.2.6593</td><td>Prerequisite: Gradle 7.6.4 or 8.4, or later. See <a data-mention href="../analyzing-source-code/scanners/sonarscanner-for-gradle">sonarscanner-for-gradle</a></td></tr><tr><td>SonarScanner for .NET</td><td>9.0.2</td><td>10.3.0.120579</td><td>11.0.0.126294</td><td>Prerequisite: NET Framework v4.7.2 or later, if using the .NET Framework. See <a data-mention href="../analyzing-source-code/scanners/dotnet/installing">installing</a> for .NET</td></tr><tr><td>SonarScanner for NPM</td><td>4.2.6</td><td>4.3.0</td><td>4.3.0</td><td>Prerequisite: Node.js 18.20.0 or later. See <a data-mention href="../analyzing-source-code/scanners/npm/installing">installing</a>for NPM</td></tr><tr><td>SonarScanner for Python</td><td>0.2.0.520</td><td>1.1.0.2035</td><td>1.3.0.4086</td><td>Prerequisite: Python 3.9 or later. See <a data-mention href="../analyzing-source-code/scanners/sonarscanner-for-python">sonarscanner-for-python</a></td></tr><tr><td>SonarScanner for Ant</td><td>Deprecated, use SonarScanner CLI</td><td>N/A</td><td>N/A</td><td></td></tr></tbody></table>

### Update notes

#### Java requirements for SonarQube Server runtime (2026.1)

* The SonarQube Server runtime now requires Java Development Kit (JDK). The previous requirement of a Java Runtime Environment (JRE) is no longer sufficient, and a full JDK is required.
* Added Support for Java 25 in addition to Java 21.&#x20;
* Removed support for Java 17.

See [server-host-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements "mention") and [#deprecations-and-removals](#deprecations-and-removals "mention") sections for additional information.

#### PostgreSQL support (2026.1)

Support for PostgreSQL versions 14 through 18 is now available, enabling deployments using the most recent PostgreSQL release. PostgreSQL version 13 is not supported anymore. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention") for more information.

#### Kubernetes and Openshift support (2026.1)

* Supported Kubernetes Versions: From 1.32 to 1.35. Support for versions 1.30 and 1.31 has been removed.
* Supported Openshift Versions: From 4.17 to 4.20. Support for versions 4.11 to 4.16 has been removed.

#### Upgrade to Microsoft SQL JDBC Auth 12.10.2 package (2025.6.1)

To use integrated security in Microsoft SQL database, upgrade to Microsoft SQL JDBC Auth 12.10.2 package. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention") for more information.

#### Support for MSSQL server (2026.1)

Supported MSSQL server is now 2022 (MSSQL Server 16.0); 2019 (MSSQL Server 15.0); 2017 (MSSQL Server 14.0). Support for 2016 MSSQL Server 13.0 support has been removed. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention") for more information.

#### SonarQube Server includes Elasticsearch 8.x (2026.1)

SonarQube Server 2026.1 LTA and later includes Elasticsearch 8.x, which requires read and write access to the `/tmp` directory. This is a requirement from Elasticsearch itself and cannot be disabled. For more information and a solution, see [#fonts](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux#fonts "mention").

#### Setting up the Sandbox feature (2025.5)

To ensure the Sandbox feature is active before project analysis, you need to set system properties before restarting your SonarQube Server following the update. The specific configuration varies based on your installation type. See the [#sandbox](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties#sandbox "mention") documentation and [#setting-up-the-sandbox-feature-at-the-instance-level](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/quality-standards#setting-up-the-sandbox-feature-at-the-instance-level "mention") for more information.

See [#removals-and-deprecations](#removals-and-deprecations "mention") for additional information.

### New and enhanced features

#### Languages

<details>

<summary>Apex</summary>

**New rules for Apex (2025.6)**

Expansion of code quality and security rules for [apex](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/apex "mention"), 42 new rules (98 total rules), to address enterprise coverage gaps, for example:

SOQL

* [S7960](https://rules.sonarsource.com/apex/tag/soql/RSPEC-7960/) - SOQL queries should be assigned to Lists to avoid QueryException
* [S8011](https://rules.sonarsource.com/apex/tag/soql/RSPEC-8011/) - SOQL queries should use SystemModStamp instead of LastModifiedDate for better performance
* [S8129](https://rules.sonarsource.com/apex/tag/soql/RSPEC-8129/) - SOQL queries should not contain hardcoded literals

SOSL

* [S8048](https://rules.sonarsource.com/apex/tag/sosl/RSPEC-8048/) - SOSL queries in test methods should use "Test.setFixedSearchResults"

Governor limits

* [S7992](https://rules.sonarsource.com/apex/tag/governor-limits/RSPEC-7992/) - SOQL queries should include LIMIT clauses to prevent hitting governor limits
* [S8033](https://rules.sonarsource.com/apex/tag/governor-limits/RSPEC-8033/) - HTTP requests should have explicit timeout configuration
* [S8127](https://rules.sonarsource.com/apex/tag/governor-limits/RSPEC-8127/) - SOQL queries should not be executed inside loops

</details>

<details>

<summary>Cobol</summary>

**Cobol improvements (2026.1)**

Adds support for parsing additional language constructs and includes fixes for crashes and false positives for [cobol](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/cobol "mention"). Related rules include:

* [S3938](https://rules.sonarsource.com/cobol/RSPEC-3938/): Track uses of forbidden statements
* [S1725](https://rules.sonarsource.com/cobol/RSPEC-1725/): Open files should be closed explicitly
* [S1574](https://rules.sonarsource.com/cobol/RSPEC-1574/): Data items should be initialized with data of the correct type
* [S1289](https://rules.sonarsource.com/cobol/RSPEC-1289/): Unused data item blocks should be removed

</details>

<details>

<summary>CFamily</summary>

**MISRA C++:2023 rules released (2025.6)**

The[ MISRA C++ 2023 rules](https://rules.sonarsource.com/cpp/tag/misra-c++2023) have been released and are no longer in Early Access. This expands coverage to all 179 MISRA C++2023 guidelines in Enterprise and Data Center editions plus SonarQube for IDE when in connected mode. See [#quality-profiles](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/customizing-the-analysis#quality-profiles "mention") for more information.

**New Sonar Misra C++ 2023 quality profile available (2025.6)**

A new Sonar MISRA C++ 2023 Compliance quality profile is available starting in Enterprise edition. It combines Sonar way rules with[ MISRA C++ 2023 rules](https://rules.sonarsource.com/cpp/tag/misra-c++2023) and is designed for projects seeking MISRA compliance.

</details>

<details>

<summary>GitHub Actions</summary>

**GitHub Actions support (2025.5)**

SonarQube Server now supports analysis of YAML files detected as [github-actions](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/github-actions "mention").

**IaC analysis improved for GitHub Actions (2025.5)**

The analysis of Infrastructure as Code (Ansible, Azure Resource Manager, CloudFormation, Docker, Kubernetes, Terraform) has been improved to detect security misconfigurations and vulnerabilities in GitHub Actions. To do so, the following rules have been added:

* [S7630](https://rules.sonarsource.com/githubactions/RSPEC-7630/): GitHub Actions should not be vulnerable to script injections
* [S7631](https://rules.sonarsource.com/githubactions/RSPEC-7631/): Checking out code from a fork in a privileged workflow context is security-sensitive
* [S7633](https://rules.sonarsource.com/githubactions/RSPEC-7633/): Parsing structured data as a secret is security-sensitive
* [S7634](https://rules.sonarsource.com/githubactions/RSPEC-7634/): Passing the full secrets context to a workflow step is security-sensitive
* [S7635](https://rules.sonarsource.com/githubactions/RSPEC-7635/): Passing the full secrets context to reusable workflows is security-sensitive
* [S7636](https://rules.sonarsource.com/githubactions/RSPEC-7636/): Expanding secrets in run blocks is security-sensitive
* [S7637](https://rules.sonarsource.com/githubactions/RSPEC-7637/): Using external GitHub actions and workflows without a full length commit hash is security-sensitive
* [S6596](https://rules.sonarsource.com/githubactions/RSPEC-6596/): Specific version tag for image should be used

</details>

<details>

<summary>Go</summary>

**Expansion of code quality rules for Go (2025.6)**

Added 24 new rules targeting the base [go](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/go "mention") language, for example:

* [S8188](https://rules.sonarsource.com/go/tag/performance/RSPEC-8188/) - Context cancellation functions should be deferred
* [S8193](https://rules.sonarsource.com/go/type/Code%20Smell/RSPEC-8193/) - Variables in if short statements should be used beyond just the condition
* [S8197](https://rules.sonarsource.com/go/tag/performance/RSPEC-8197/) - Use "bytes.Equal" instead of "bytes.Compare" for equality checks
* [S8206](https://rules.sonarsource.com/go/type/Bug/RSPEC-8206/) - Deprecated "InterfaceData" method should not be used
* [S8208](https://rules.sonarsource.com/go/tag/http/RSPEC-8208/) - HTTP response bodies should be closed to prevent resource leaks
* [S8210](https://rules.sonarsource.com/go/type/Code%20Smell/RSPEC-8210/) - Variables should be used
* [S8239](https://rules.sonarsource.com/go/tag/performance/RSPEC-8239/) - Context parameters should be reused instead of creating new background contexts
* [S8242](https://rules.sonarsource.com/go/type/Code%20Smell/RSPEC-8242/) - Context should not be stored in struct fields
* [S8259](https://rules.sonarsource.com/go/type/Bug/RSPEC-8259/) - Busy waiting loops should use proper synchronization

**Go 1.25 support (2025.5)**

Go version 1.25 is now supported.

</details>

<details>

<summary>IaC</summary>

**IaC improvements (2026.1)**

The analysis of Infrastructure as Code (Ansible, Azure Resource Manager, CloudFormation, Docker, Kubernetes, Terraform, GitHub Actions) has been improved.

Helm templates are now evaluated even if `values.yaml` is missing.

The following rules have been added:

* [S6437](https://rules.sonarsource.com/azureresourcemanager/RSPEC-6437/): Credentials should not be hard-coded
* [S7638](https://rules.sonarsource.com/githubactions/RSPEC-7638/): ACTIONS\_ALLOW\_UNSECURE\_COMMANDS should not be used
* [S8232](https://rules.sonarsource.com/githubactions/RSPEC-8232/): Workflows should not rely on unverified GitHub context values to trust events
* [S8233](https://rules.sonarsource.com/githubactions/RSPEC-8233/): Write permissions should be defined at the job level
* [S8262](https://rules.sonarsource.com/githubactions/RSPEC-8262/): Artifacts should not contain secrets
* S8263: GitHub Action invocations should not be vulnerable to parameter injection attacks
* [S8264](https://rules.sonarsource.com/githubactions/RSPEC-8264/): Read permissions should be defined at the job level

</details>

<details>

<summary>Java</summary>

**Java improvements (2025.6)**

Improvements to [java](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/java "mention") rules:

* [S1068](https://rules.sonarsource.com/java/RSPEC-1068/): Unused "private" fields should be removed
* [S1144](https://rules.sonarsource.com/java/RSPEC-1144/): Unused "private" methods should be removed
* [S1479](https://rules.sonarsource.com/java/RSPEC-1479/): "switch" statements should not have too many "case" clauses
* [S1186](https://rules.sonarsource.com/java/RSPEC-1186/): Methods should not be empty
* [S1948](https://rules.sonarsource.com/java/RSPEC-1948/): Fields in a "Serializable" class should either be transient or serializable
* [S1989](https://rules.sonarsource.com/java/RSPEC-1989/): Exceptions should not be thrown from servlet methods
* [S2097](https://rules.sonarsource.com/java/RSPEC-2097/): "equals(Object obj)" should test the argument's type
* [S2187](https://rules.sonarsource.com/java/RSPEC-2187/): TestCases should contain tests
* [S2698](https://rules.sonarsource.com/java/RSPEC-2698/): Test assertions should include messages
* [S3306](https://rules.sonarsource.com/java/RSPEC-3306/): Constructor injection should be used instead of field injection
* [S3329](https://rules.sonarsource.com/java/RSPEC-3329/): Cipher Block Chaining IVs should be unpredictable
* [S4605](https://rules.sonarsource.com/java/RSPEC-4605/): Spring beans should be considered by "@ComponentScan"
* [S5738](https://rules.sonarsource.com/java/RSPEC-5738/): "@Deprecated" code marked for removal should never be used
* [S6813](https://rules.sonarsource.com/java/RSPEC-6813/): Field dependency injection should be avoided

**Java security (2025.6)**

Related rules:

* [S2076](https://rules.sonarsource.com/java/RSPEC-2076/): OS commands should not be vulnerable to command injection attacks
* [S2083](https://rules.sonarsource.com/java/RSPEC-2083/): I/O function calls should not be vulnerable to path injection attacks
* [S5146](https://rules.sonarsource.com/java/RSPEC-5146/): HTTP request redirections should not be open to forging attacks
* [S6547](https://rules.sonarsource.com/java/RSPEC-6547/): Environment variables should not be defined from untrusted input
* [S7518](https://rules.sonarsource.com/java/RSPEC-7518/): Privileged prompts should not be vulnerable to injection attacks

</details>

<details>

<summary>JavaScript / TypeScript / CSS</summary>

**New CSS rules (2025.6)**

The following CSS accessibility rules have been added:

* S7923: Orientation of the page is not restricted using CSS transform property
* S7924: Text has minimum contrast
* S7925: Spacing and height in style attributes is not \`!important\`

**TypeScript support (2025.6)**

All versions of through 5.9.3 are supported. See [javascript-typescript-css](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/javascript-typescript-css "mention") for more information.

**JavaScript / TypeScript analyzer speed improvements (2025.6)**

Optimization of the analysis engine, moving logic to Node.js and using WebSockets, resulting in up to 40% faster analysis for large projects.

**58 Quick Fixes for JavaScript / TypeScript (2025.6)**

Automatically enables Quick Fixes in SonarQube IDE for 58 existing JavaScript and TypeScript rules.

**AngularJS rules for TypeScript (2025.5)**

The following rules related to AngularJS have been added to the TypeScript analysis:

* [S7655](https://rules.sonarsource.com/typescript/RSPEC-7655/): Angular classes should implement lifecycle interfaces for their lifecycle methods
* [S7641](https://rules.sonarsource.com/typescript/RSPEC-7641/): Angular lifecycle methods should be used in the correct context
* [S7656](https://rules.sonarsource.com/typescript/RSPEC-7656/): Angular Pipes should implement PipeTransform interface
* [S7650](https://rules.sonarsource.com/typescript/RSPEC-7650/): Components and directives should not use the "inputs" metadata property
* [S7648](https://rules.sonarsource.com/typescript/RSPEC-7648/): Components, Directives, and Pipes should use standalone architecture
* [S7647](https://rules.sonarsource.com/typescript/RSPEC-7647/): Empty Angular lifecycle methods should be removed
* [S7649](https://rules.sonarsource.com/typescript/RSPEC-7649/): Input bindings should not be aliased
* [S7653](https://rules.sonarsource.com/typescript/RSPEC-7653/): Output bindings should not be aliased
* [S7652](https://rules.sonarsource.com/typescript/RSPEC-7652/): Output bindings should not be named "on" or prefixed with "on"
* [S7651](https://rules.sonarsource.com/typescript/RSPEC-7651/): Output bindings should not be named as standard DOM events
* [S7654](https://rules.sonarsource.com/typescript/RSPEC-7654/): The "outputs" metadata property should not be used in Angular components and directives

**JavaScript analysis improved (2025.5)**

68 rules from the eslint-plugin-unicorn have been added to the JavaScript analysis.

</details>

<details>

<summary>JCL</summary>

**New leaveFile API for JCL (2026.1)**

A new leaveFile API is available for custom rules for [jcl](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/jcl "mention") language, giving rule authors more control over how files are processed and reported.

</details>

<details>

<summary>.NET and C#</summary>

**.NET 10 and C# 14 support (2026.1)**

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

**Injection vulnerabilities supported for .NET WPF framework (2025.5)**

Taint analysis is now supported for Windows Presentation Foundation (WPF) entry points, such as UI controls, data bindings or command parameters.

</details>

<details>

<summary>PHP</summary>

**Reduction in false positives (2026.1)**

Reduces false positives on several rules and cleans up build and dependency infrastructure. Related rules:<br>

* [S1155](https://rules.sonarsource.com/php/RSPEC-1155/): "empty()" should be used to test for emptiness
* [S1172](https://rules.sonarsource.com/php/RSPEC-1172/): Unused function parameters should be removed
* [S2699](https://rules.sonarsource.com/php/RSPEC-2699/): Tests should include assertions
* [S1068](https://rules.sonarsource.com/php/RSPEC-1068/): Unused "private" fields should be removed

**PHP analysis improved (2025.5)**

[php](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/php "mention") keyword parsing has been optimized by replacing the regex-based logic.

</details>

<details>

<summary>PL/SQL</summary>

**Support for PL/SQL 3.18.0.216 (2025.6)**

The following [pl-sql](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/pl-sql "mention") rules have been updated:

* [S1135](https://rules.sonarsource.com/plsql/RSPEC-1135/): Track uses of "TODO" tags
* [S1192](https://rules.sonarsource.com/plsql/RSPEC-1192/): String literals should not be duplicated
* [S1854](https://rules.sonarsource.com/plsql/RSPEC-1854/): Unused assignments should be removed
* [S2340](https://rules.sonarsource.com/plsql/RSPEC-2340/): "LOOP ... END LOOP;" constructs should be avoided
* [S2454](https://rules.sonarsource.com/plsql/RSPEC-2454/): Columns should be aliased
* [S2534](https://rules.sonarsource.com/plsql/RSPEC-2534/): Positional and named arguments should not be mixed in invocations
* [S3651](https://rules.sonarsource.com/plsql/RSPEC-3651/): Individual "WHERE" clause conditions should not be unconditionally true or false
* [S4081](https://rules.sonarsource.com/plsql/RSPEC-4081/): "PLS\_INTEGER" types should be used
* [S4196](https://rules.sonarsource.com/plsql/RSPEC-4196/): Output parameters should be assigned
* [S4421](https://rules.sonarsource.com/plsql/RSPEC-4421/): Features deprecated in Oracle 12 should not be used
* [S5245](https://rules.sonarsource.com/plsql/RSPEC-5245/): Identifiers should be written in lower case

</details>

<details>

<summary>Python</summary>

**Support for Python 3.14 (2025.6)**

Includes the new JIT compiler and defer statement features. See [python](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/python "mention") for more information. Related rules:

* [S7931](https://rules.sonarsource.com/python/RSPEC-7931/): "NotImplemented" should not be used in boolean contexts
* [S7941](https://rules.sonarsource.com/python/RSPEC-7941/): Compression modules should be imported from the compression namespace
* [S7942](https://rules.sonarsource.com/python/RSPEC-7941/): Template strings should be processed before use
* [S7943](https://rules.sonarsource.com/python/RSPEC-7943/): Template and str should not be concatenated directly
* [S7945](https://rules.sonarsource.com/python/RSPEC-7945/): Template string processing should use structural pattern matching

**Rules for Python Pytorch library (2025.6)**

Specialized rules for PyTorch to help write efficient, error-free Machine Learning code. The new rules include:

* S7697: PyTorch tensor operations should assign results or use in-place variants
* S7699: Dropout layers should be defined as model attributes in "\_\_init\_\_" method
* [S7702](https://rules.sonarsource.com/python/RSPEC-7702/): Specify "start\_dim" when using "torch.flatten" to preserve batch dimension
* [S7703](https://rules.sonarsource.com/python/RSPEC-7703/): Method calls should use parentheses when saving PyTorch model state
* [S7704](https://rules.sonarsource.com/python/RSPEC-7704/): PyTorch module classes should not be instantiated inline in forward methods
* [S7706](https://rules.sonarsource.com/python/RSPEC-7706/): Use PyTorch Lightning's built-in checkpointing instead of manual checkpoint saving
* S7709: Tensor lists should be concatenated with "torch.cat()" instead of "torch.tensor()"
* [S7708](https://rules.sonarsource.com/python/RSPEC-7708/): Tensors should not be concatenated incrementally in loops
* [S7710](https://rules.sonarsource.com/python/RSPEC-7710/): Use "torch.empty()" instead of list comprehensions for empty tensor initialization
* S7711: Dataset "\_\_len\_\_" methods should return an integer, not "torch.Size"
* [S7713](https://rules.sonarsource.com/python/RSPEC-7713/): Tensor operations should rely on automatic broadcasting instead of manual expansion

**Python security (2025.6)**

Related rules:

* [S2076](https://rules.sonarsource.com/python/RSPEC-2076/): OS commands should not be vulnerable to command injection attacks
* [S2083](https://rules.sonarsource.com/python/RSPEC-2083/): I/O function calls should not be vulnerable to path injection attacks
* [S3649](https://rules.sonarsource.com/python/RSPEC-3649/): Database queries should not be vulnerable to injection attacks
* [S5131](https://rules.sonarsource.com/python/RSPEC-5131/): Endpoints should not be vulnerable to reflected cross-site scripting (XSS) attacks
* [S5144](https://rules.sonarsource.com/python/RSPEC-5144/): Server-side requests should not be vulnerable to forging attacks
* [S5334](https://rules.sonarsource.com/python/RSPEC-5334/): Dynamic code execution should not be vulnerable to injection attacks
* [S7518](https://rules.sonarsource.com/python/RSPEC-7518/): Privileged prompts should not be vulnerable to injection attacks
* [S7693](https://rules.sonarsource.com/python/RSPEC-7693/): Operating AI agents without predefined boundaries is security-sensitive
* [S7698](https://rules.sonarsource.com/python/RSPEC-7698/): AI agent code execution without sandboxing is security-sensitive

**Python analysis: new rules for PyTorch library (2025.5)**

The following rules have been added:

* [S7508](https://rules.sonarsource.com/python/RSPEC-7508/): Redundant collection functions should be avoided
* [S7675](https://rules.sonarsource.com/python/RSPEC-7675/): Tensor copying should use recommended methods
* [S7695](https://rules.sonarsource.com/python/RSPEC-7695/): "super()" calls should not be used in TorchScript methods

**Python analysis: AWS Lambda rules (2025.5)**

The following rules related to AWS lambdas and common practices have been added to the [python](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/python "mention") analysis:

* [S6249](https://rules.sonarsource.com/python/RSPEC-6249/): Authorizing HTTP communications with S3 buckets is security-sensitive
* [S7613](https://rules.sonarsource.com/python/RSPEC-7613/): AWS Lambda handlers should return only JSON serializable values
* [S7609](https://rules.sonarsource.com/python/RSPEC-7609/): AWS CloudWatch metrics namespace should not begin with \`AWS/\`
* [S6246](https://rules.sonarsource.com/python/RSPEC-6246/): Lambdas should not invoke other lambdas synchronously
* [S7608](https://rules.sonarsource.com/python/RSPEC-7608/): S3 operations should verify bucket ownership using ExpectedBucketOwner parameter
* [S7618](https://rules.sonarsource.com/python/RSPEC-7618/): Network calls in AWS Lambda functions shouldn't be made without explicit timeout parameters
* [S7617](https://rules.sonarsource.com/python/RSPEC-7617/): Reserved environment variable names should not be overridden in Lambda functions
* [S6243](https://rules.sonarsource.com/python/RSPEC-6243/): Reusable resources should be initialized at construction time of Lambda functions
* [S6262](https://rules.sonarsource.com/python/RSPEC-6262/): AWS region should not be set with a hardcoded String
* [S7622](https://rules.sonarsource.com/python/RSPEC-7622/): boto3 operations that support pagination should be performed using paginators or manual pagination handling
* [S7621](https://rules.sonarsource.com/python/RSPEC-7621/): AWS waiters should be used instead of custom polling loops
* [S7620](https://rules.sonarsource.com/python/RSPEC-7620/): AWS Lambda handlers should clean up temporary files in /tmp directory
* [S7625](https://rules.sonarsource.com/python/RSPEC-7625/): Long-term AWS access keys should not be used directly in code
* [S7614](https://rules.sonarsource.com/python/RSPEC-7614/): AWS Lambda handlers must not be an async function
* [S7619](https://rules.sonarsource.com/python/RSPEC-7619/): "botocore.exceptions.ClientError" must be explicitly catch and handled

**Parallel execution of Python rules (2025.5)**

Parallel execution of [python](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/python "mention") rules is now supported.<br>

</details>

<details>

<summary>Ruby</summary>

**New rules for Ruby (2025.6)**

33 new language-specific and framework-specific rules for [ruby](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/ruby "mention"), including 12[ targeting Ruby-on-rails](https://rules.sonarsource.com/ruby/tag/rails/), for example:

* [S7839](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7839/): Global variables should not be used in Rails applications
* [S7844](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7844/): Asset compilation should be disabled in production environments
* [S7867](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7867/): Rails API controllers using "respond\_to" should include "ActionController::MimeResponds"
* [S7875](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7875/): Rails applications should define a root route with proper controller#action syntax
* [S7887](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7887/): Before destroy callbacks should use proper halt mechanism
* [S7895](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7895/): HTTP status codes should use symbols instead of numeric values
* [S7897](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7897/): Rails queries should use "find\_by" instead of "where.take" for single record retrieval
* [S7899](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7899/): Rails collections should use "ids" instead of "pluck(:id)" for primary keys
* [S7904](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7904/): Rails model callback methods should be private
* [S7905](https://rules.sonarsource.com/ruby/tag/rails/RSPEC-7905/): Controllers should inherit from appropriate base classes

</details>

<details>

<summary>Rust</summary>

Rust analysis improvements (2025.5)

The Clippy analysis can now be run offline by setting `sonar.rust.clippy.offline` to `true`. This prevents Clippy from trying to fetch dependencies. Dependencies must still be available locally for the analysis to work correctly. This setting is intended for air-gapped environments. See [rust](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/rust "mention") for more information.

</details>

<details>

<summary>Scala</summary>

**Reduced false positives and negatives (2026.1)**

Include fixes to false positives and negatives for [scala](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/scala "mention") in the following rules:

* [S1192](https://rules.sonarsource.com/scala/RSPEC-1192/): String literals should not be duplicated
* [S126](https://rules.sonarsource.com/scala/RSPEC-126/): "if ... else if" constructs should end with "else" clauses

</details>

<details>

<summary>Secrets</summary>

**Reduced false positives (2026.1)**

[secrets](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/secrets "mention") rules have been improved to reduce the detection of false positives and the following rule have been added:

* [S6418](https://rules.sonarsource.com/yaml/RSPEC-6418/): Hard-coded secrets are security-sensitive
* [S2068](https://rules.sonarsource.com/yaml/RSPEC-2068/): Hard-coded passwords are security-sensitive
* [S7552](https://rules.sonarsource.com/secrets/RSPEC-7552/): SMTP credentials should not be disclosed
* [S8350](https://rules.sonarsource.com/secrets/RSPEC-8350/): xAI API keys should not be disclosed

**New rules have been added for Secrets detection (2025.6):**

* [S8135](https://rules.sonarsource.com/secrets/RSPEC-8135/): JSON Web Tokens should not be disclosed
* [S8136](https://rules.sonarsource.com/secrets/RSPEC-8136/): HTTP authentication credentials should not be disclosed
* [S8214](https://rules.sonarsource.com/secrets/RSPEC-8214/): Handsontable License Keys should not be disclosed
* [S8215](https://rules.sonarsource.com/secrets/RSPEC-8215/): Password hashes should not be disclosed
* [S8217](https://rules.sonarsource.com/secrets/RSPEC-8217/): HTTP Authentication Bearer tokens should not be disclosed
* [S8219](https://rules.sonarsource.com/secrets/RSPEC-8219/): Azure DevOps App secrets should not be disclosed

</details>

<details>

<summary>Shell / bash</summary>

**Shell/bash analysis (2025.6)**

Introduction of 31 code quality and security rules specifically for shell/bash scripts. For example:

* [S1481](https://rules.sonarsource.com/shell/RSPEC-1481/): Unused local variables should be removed
* [S4830](https://rules.sonarsource.com/shell/RSPEC-4830/): Server certificates should be verified during SSL/TLS connections
* [S6506](https://rules.sonarsource.com/shell/RSPEC-6506/): Allowing downgrades to a clear-text protocol is security-sensitive
* [S7684](https://rules.sonarsource.com/shell/RSPEC-7684/): Variable names should follow shell naming conventions
* [S7674](http://rules.sonarsource.com/shell/RSPEC-7674/): Variables should be quoted during expansion
* [S7677](https://rules.sonarsource.com/shell/RSPEC-7677/): Error messages should be sent to stderr
* [S7689](https://rules.sonarsource.com/shell/RSPEC-7689/): Command substitution should use modern "$()" syntax instead of backticks

</details>

<details>

<summary>Swift</summary>

**Support for Swift 5.9 through 6.1 (2025.6)**

Comprehensive support for [swift](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/swift "mention") versions 5.9 through 6.1, including macros, variadic generics, and new syntax features.

**Support SwiftUI (2025.6)**

Targeted support for SwiftUI that silences irrelevant rules and disables rules in preview sections, for example:

* [S107](https://rules.sonarsource.com/swift/RSPEC-107/): ​​Functions should not have too many parameters
* [S3087](https://rules.sonarsource.com/swift/RSPEC-3087/): Closure expressions should not be nested too deeply

**SAST for Swift (2025.6)**

Introduces Static Application Security Testing (SAST) for Swift, targeting cryptography and communication issues.

**Detect passwords and secrets in Swift (2025.6)**

Enhanced secret detection for Swift using entropy checks and post-processing to reduce noise.

</details>

<details>

<summary>T-SQL</summary>

**T-SQL analyzer update (2025.6)**

Updates to ensure [t-sql](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/t-sql "mention") analysis are ready for the upcoming Long Term Active (LTA) release. Related fixes and improvements to:

* [S1116](https://rules.sonarsource.com/tsql/RSPEC-1116/): ​​Empty statements should be removed
* [S1523](https://rules.sonarsource.com/tsql/RSPEC-1523/): Dynamically executing code is security-sensitive
* Parsing of `CREATE STATISTICS` statement
* Parsing of `CREATE/DROP ASYMMETRIC KEY`
* Parsing of `CREATE MESSAGE TYPE`

</details>

<details>

<summary>VB6</summary>

**VB6 improvements (2026.1)**

Fixes parse errors and line count for [vb6](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/vb6 "mention"). Related rules:

* [S138](https://rules.sonarsource.com/vb6/RSPEC-138/): Subs and functions should not have too many lines
* [S1151](https://rules.sonarsource.com/vb6/RSPEC-1151/): "Case" clauses should not have too many lines

</details>

<details>

<summary>XML</summary>

**Improvements to the XML rules (2025.6)**

Various improvements to [xml](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/xml "mention") rules and analyzer. Related rules:

* [S2068](https://rules.sonarsource.com/xml/RSPEC-2068/): Hard-coded credentials are security-sensitive
* [S3330](https://rules.sonarsource.com/xml/RSPEC-3330/): Creating cookies without the "HttpOnly" flag is security-sensitive
* [S5344](https://rules.sonarsource.com/java/RSPEC-5344/): Passwords should not be stored in plaintext or with a fast hashing algorithm
* [S5734](https://rules.sonarsource.com/javascript/RSPEC-5734/): Allowing browsers to sniff MIME types is security-sensitive
* [S7630](https://rules.sonarsource.com/githubactions/RSPEC-7630/): GitHub Actions should not be vulnerable to script injections

</details>

#### Analysis

**JFrog Evidence Collection with SonarQube Server (2026.1)**

This integration provides a single, verifiable audit trail if you use both SonarQube and JFrog with strict audit trail and compliance requirements. SonarQube analysis results are automatically signed and directly attached to your JFrog packages to create a single, verifiable source of truth. You no longer have to jump between tools to prove your code meets security standards. Everything you need for a rigorous audit is now visible within the JFrog Evidence Collection interface. This feature is available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarqube/) edition and above. See [jfrog-evidence-collection-integration](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/jfrog-evidence-collection-integration "mention") for more information.

**High-volume file move detection (2025.6)**

SonarQube now stops the analysis when a high-volume file move is detected and raises a warning to let users revert to their initial project configuration in case of an unintended file move.

**Sandboxing of issues coming from SonarQube update (2025.5)**

Some SonarQube updates may introduce new issues in your code on sections that have not been changed since the previous analysis. These new issues may lead to abrupt and unexplained quality gate and pipeline failures, causing frustration and delays in releases.

To eliminate these pain points, you can enable sandboxing. This way:

* The sandboxed issues won’t impact your quality gate.
* Users will be able to triage the sandboxed issues at their own pace.

See [#from-sonarqube-update](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview#from-sonarqube-update "mention") and [#update-notes](#update-notes "mention") for more information.

#### Feedback mechanism for self-hosted LLMs (2026.1)

Improves the success rate of generating valid AI CodeFix suggestions from self‑hosted LLMs.

#### Quality gate fudge factor improved (2026.1)

To avoid overly strict enforcement of small changes, the quality gate ignores coverage and duplication conditions for very small sets of new code. See [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/changing-default-quality-gate "mention") for more information.

#### Integrations

**Jira (2025.6)**

This feature introduces a secure, app-based connection for integrating SonarQube Server with Jira Cloud. This lays the groundwork for powerful future workflows, such as issue tracking,  release readiness assessment and creating Jira work items from SonarQube issues. For more information see the following documentation:

* [jira-integration](https://docs.sonarsource.com/sonarqube-server/instance-administration/jira-integration "mention") on an instance level
* [jira-integration](https://docs.sonarsource.com/sonarqube-server/project-administration/jira-integration "mention") on a project level
* [managing-jira-work-items](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/managing-jira-work-items "mention")

**Slack (2025.6)**

Delivers real-time notifications for quality gate status changes (failed or failed-to-passed) directly into Slack channels. See [slack](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/slack "mention") or more information.

**GitHub Enterprise Cloud with Data Residency now supported (2025.6)**

SonarQube’s integration with GitHub Enterprise Cloud with Data Residency is now supported.

**Navigation from SonarQube to GitHub (2025.6)**

You can now navigate from your SonarQube project to the bound GitHub repository by selecting the project bound icon.

#### Reporting

**AI and mobile compliance reporting (2026.1)**

Extends our regulatory coverage to include critical AI and Mobile security standards such as OWASP Top 10 for LLM and OWASP MASVS for project security reports. This feature is available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarqube/) edition and above. See [security-related-rules](https://docs.sonarsource.com/sonarqube-server/user-guide/rules/security-related-rules "mention") for more information.\
\
**Security standards (2025.6)**

SonarQube Server rules and security reports have been updated to comply with the most recent security standards. The new and updated security standards are:

* OWASP Top 10 2025: Updating security rule mappings, documentation, and reporting to align with the newly released OWASP Top 10 2025
* STIG ASD version 6: Integration and mapping of our security rules to the latest security technical implementation guide (STIG) for application security and development, version 6.

Security reports are available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarqube/) edition and higher. See [security-reports](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-reports/security-reports "mention") for the full list of security standards and language coverage.

**WCAG Accessibility compliance (2025.6)**

Introduces Accessibility reports via API to monitor compliance with[ WCAG 2.1 AA](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-21/) and[ 2.2 AA](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) standards.

#### Security

**New rules for detecting LLM issues (2025.6)**

The new version of security analyzer contains new and improved rules for detecting LLM related security issues.

**Detect security misconfigurations in bash shell files (2025.6)**

Detects unsafe file permissions, insecure commands (`curl` / `wget`), and hardcoded secrets in `.sh` files.

#### SonarQube Advanced Security

Available as part of SonarQube Advanced Security license for [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarqube/) edition and higher. See [advanced-security](https://docs.sonarsource.com/sonarqube-server/advanced-security "mention") for more information.

**Malicious package detection (2026.1)**

Receive blocker-level alerts if a dependency matches publicly known datasets of known malicious packages.

**ASAST configs refreshed for C# and Java top 1k libraries, and Python top 100 (2025.6)**

Automatically delivers optimized Advanced SAST configurations for the Top 1,000 most used libraries in C# and Java, and top 100 Python libraries.

**C/C++ support for Conan and vcpkg projects - beta (2025.6)**

Allows customers to analyze C and C++ projects that utilize the Conan or vcpkg package managers to return vulnerability and license information.

**Software bill of materials (SBOM) import (CycloneDX, SPDX) - beta (2025.6)**

Allows customers to import software bill of materials (SBOM) in CycloneDX or SPDX format to retrieve vulnerability information. This supports the scanning of arbitrary applications and dependencies, including container images and complex C++ applications.

**SPDX 3.0 support (2025.6)**

Ensures support for the latest SPDX 3.0 standard.

**SCA service activation at the project level (2025.5)**

In the previous version, Software Composition Analysis (SCA) was enabled in the UI at the instance level for all projects. With this new version, when you enable the service as an instance admin, you can additionally define the default activation status (on or off) for all projects in your instance.

#### Server operation

**In-product communication of product news (2025.6)**

Sonar will now provide in-product notifications to users regarding important product updates. These messages will be tailored to specific audiences. Users will receive alerts for new messages and will have access to a complete message history.

**Announcement messages improved (2025.5)**

It’s now possible to add links to your custom announcement messages in the UI. For more information, see [#announcements](https://docs.sonarsource.com/sonarqube-server/instance-administration/ui-customization/custom-messages#announcements "mention").

**JRE auto-provisioning can be disabled at instance level (2025.5)**

JRE auto-provisioning for the scanners on CI/CD host is enabled by default. It was possible to disable it through an analysis parameter. You can now disable it at the SonarQube Server instance level.&#x20;

**Improved memory consumption of Sonar scanners (2025.5)**

In order to reduce memory consumption for the scanner-engine, visibility information is now discarded for excluded files.

#### UI and UX

**Rules statuses visible on the Issues page (2025.6)**

Surfacing the rule status, specifically beta, directly on the Issues and Issues detail pages. This clarifies the maturity of the rule that generated the issue.

**Update to the login page (2025.6)**

Updated accessibility, layout, and error messages resulting in an improved overall login experience.

### Removals and deprecations

#### Java 17 not supported any more (2026.1)

Java version 21 is the minimum version required to run SonarQube Server. See [#software-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements#software-requirements "mention") for more information.

#### PostgreSQL in Helm charts removed (2026.1)

The deprecated PostgreSQL dependency in the Helm chart has been removed. If you were relying on this dependency for production, you must take the following steps to upgrade to the new chart: back up their existing database, import the data into a new database, and then update the JDBC URL within the SonarQube chart configuration. See [installing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installing-helm-chart "mention") for more information.

#### Kubernetes and Openshift versions removed (2026.1)

* Support for versions 1.30 and 1.31 has been removed.
* Support for versions 4.11 to 4.16 has been removed.

#### 2016 MSSQL Server 13.0 support removed (2026.1)

Support for 2016 MSSQL Server 13.0 support has been removed. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention")  for more information.

#### Deprecation of Ingress NGINX (2026.1)

Due to the retirement of the ingress-nginx controller in November 2025 (with best-effort support ceasing in March 2026), the dependency on this chart is now deprecated.

We advise migrating to the [Gateway API](https://gateway-api.sigs.k8s.io/guides/), which is the modern successor to Ingress. Should you need to continue using Ingress, please consult the [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) for a list of suitable alternative controllers. A replacement dependency will be provided in a future release.

#### Deprecation of Automatic AI Code Detection (2026.1)

Autodetect AI-Generated Code has been deprecated. Sonar will adjust the AI Code Assurance offering to adapt to the industry changes with high AI adoption. A warning callout has been added to the SonarQube UI in global and project settings. See [ai-code-assurance](https://docs.sonarsource.com/sonarqube-server/ai-capabilities/ai-code-assurance "mention") for more information.

#### Deprecation of Design and Architecture features (2025.6)

The cycle detection and architecture as code for Java and JS/TS are deprecated (S7027, S7091, S7134, S7197), pending removal in January 2026. They will be replaced by improved architecture capabilities.&#x20;

#### Deprecation of Java 17 as a scanner runtime (2025.6)

Java 17 is deprecated as a supported scanner runtime environment and its support ends with SonarQube 2026.3 (July 2026). There is no impact for this change if you use JRE auto-provisioning, enabled by default on scanners that support it, because it keeps Java version requirements always up to date. If you disabled JRE auto-provisioning or your scanner doesn’t support it, you need to update to Java 21 or newer. See:

* [#java-runtime-environment-jre](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/general-requirements#java-runtime-environment-jre "mention") requirements for all SonarScanners.
* [Community post](https://community.sonarsource.com/t/phasing-out-java-17-as-a-scanner-runtime/153678) for more information about the deprecation.
* [managing-jre-auto-provisioning](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/managing-jre-auto-provisioning "mention") for additional information.
