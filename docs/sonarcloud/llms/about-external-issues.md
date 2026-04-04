# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/importing-external-issues/about-external-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/importing-external-issues/about-external-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/importing-external-issues/about-external-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/about-external-issues.md

# About external issues

Many languages have dedicated analyzers (also known as linters) that are commonly used to spot problems in code. SonarQube can integrate the results from many of these external analyzers. This lets you see this information alongside the other SonarQube metrics and allows the external results to be taken into account when calculating quality gate status.

If your analyzer doesn't integrate with SonarQube Server, you can import the external issues either in the generic SonarQube format or in the SARIF format.

### List of supported analyzers

The table below lists the third-party analyzers that integrate with SonarQube Server.

<table><thead><tr><th width="197">Language</th><th>External analyzers</th></tr></thead><tbody><tr><td>Ansible</td><td>ansible-lint</td></tr><tr><td>Apex</td><td>PMD</td></tr><tr><td>Cloudformation</td><td>AWS CloudFormation Linter</td></tr><tr><td>C/C++/Objective-C</td><td>Valgrind Memcheck, Valgrind Helgrind</td></tr><tr><td>C#/VB.NET</td><td>Roslyn (inc. Roslyn analyzers provided by Microsoft)</td></tr><tr><td>CSS</td><td>StyleLint.io</td></tr><tr><td>Docker</td><td>Hadolint</td></tr><tr><td>Go</td><td>GoVet, GoLint, GoMetaLinter, golanci-lint, gosec</td></tr><tr><td>Java</td><td>SpotBugs, FindSecBugs, FindBugs, PMD, Checkstyle</td></tr><tr><td>JavaScript/TypeScript</td><td>ESLint</td></tr><tr><td>Kotlin</td><td>AndroidLint, Detekt, Ktlint</td></tr><tr><td>PHP</td><td>Psalm, PHPStan</td></tr><tr><td>Python</td><td>Pylint, Bandit, Flake8, Mypy, Ruff</td></tr><tr><td>Ruby</td><td>Rubocop</td></tr><tr><td>Scala</td><td>Scalastyle, Scapegoat</td></tr><tr><td>Swift</td><td>SwiftLint</td></tr><tr><td>Terraform</td><td>TFLint</td></tr></tbody></table>

### Limitations

The external issues will be taken into account by SonarQube in the analysis report and users will be able to resolve an external issue the same way as an internal issue.

But external issues have an important limitation. The activation of the rules that raise these issues cannot be managed within SonarQube. External rules are not visible on the Rules page or reflected in any quality profile.

{% hint style="info" %}
Managing an external issue within SonarQube has no impact on its state in the external tool. For example, when you mark an issue as false positive in SonarQube, it is not reflected in the external tool.
{% endhint %}

### Related pages

[external-analyzer-reports](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/external-analyzer-reports "mention")\
[generic-issue-import-format](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/generic-issue-import-format "mention")\
[importing-issues-from-sarif-reports](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports "mention")\
[integration-with-external-analyzers](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/integration-with-external-analyzers "mention")
