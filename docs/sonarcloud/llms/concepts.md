# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/concepts.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/concepts.md

# Concepts

### Architecture <a href="#architecture" id="architecture"></a>

| **Concept** | **Definition**                                                                         |
| ----------- | -------------------------------------------------------------------------------------- |
| Analyzer    | A client application that analyzes the source code to compute **snapshots**.           |
| Database    | Stores configuration and **snapshots.**                                                |
| Server      | Web interface that is used to browse **snapshot** data and make configuration changes. |

### Quality <a href="#quality" id="quality"></a>

| **Concept**         | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clean Code          | Code whose attributes make your software reliable, secure, and maintainable. See [introduction](https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-code/introduction "mention") for more details.                                                                                                                                                                                                                                                         |
| Bug                 | An issue that represents something wrong in the code. If this has not broken yet, it will, and will probably break at the worst possible moment. This needs to be fixed as soon as possible.                                                                                                                                                                                                                                                                                  |
| Code smell          | A maintainability-related issue in the code. Leaving it as-is means that at best, developers maintaining the code will have a harder time than they should when making changes. At worst, they’ll be so confused by the state of the code that they’ll introduce additional errors as they make changes.                                                                                                                                                                      |
| Cost                | See Remediation cost.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Debt                | See Technical debt.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Issue               | When a piece of code does not comply with a rule, an issue is logged on the snapshot. An issue can be logged on a source file or a unit test file.                                                                                                                                                                                                                                                                                                                            |
| Measure             | The value of a metric for a given file or project at a given time. For example, 125 lines of code on class MyClass or, the density of duplicated lines = 30.5% on project myProject, can be considered a measure.                                                                                                                                                                                                                                                             |
| Metric              | <p>A type of measurement. Metrics can have varying values, or measures, over time. Examples: number of lines of code, complexity, etc.</p><p>A metric may be either <em>qualitative</em> (for example, the density of duplicated lines, line coverage by tests, etc.) or <em>quantitative</em> (for example, the number of lines of code, the complexity, etc.)</p>                                                                                                           |
| New code definition | A changeset or period that you’re keeping a close watch on for the introduction of new problems in the code. Ideally, this is since the `previous_version`, but if you don’t use a Maven-like versioning scheme, you may need to set a time period such as *21 days since a specific analysis* or use a reference branch. See [about-new-code](https://docs.sonarsource.com/sonarqube-server/10.7/core-concepts/clean-as-you-code/about-new-code "mention") for more details. |
| Quality profile     | A set of rules. Each snapshot is based on a single quality profile. See also [quality-profiles](https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/analysis-functions/quality-profiles "mention").                                                                                                                                                                                                                                                    |
| Rule                | A coding standard or practice that should be followed. Not complying with coding rules can lead to issues and hotspots. Adherence to rules can be used to measure the quality of code files or unit tests.                                                                                                                                                                                                                                                                    |
| Remediation cost    | The estimated time required to fix vulnerability and reliability Issues.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Snapshot            | A set of **measures** and **issues** on a given project at a given time. A snapshot is generated for each analysis.                                                                                                                                                                                                                                                                                                                                                           |
| Security hotspot    | Security-sensitive pieces of code that need to be manually reviewed. Upon review, you’ll either find that there is no threat or that there is vulnerable code that needs to be fixed.                                                                                                                                                                                                                                                                                         |
| Technical debt      | The estimated time required to fix all maintainability issues and code smells.                                                                                                                                                                                                                                                                                                                                                                                                |
| Vulnerability       | A security-related issue that represents a backdoor for attackers. See also [security-related-rules](https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/rules/security-related-rules "mention")                                                                                                                                                                                                                                                                    |
