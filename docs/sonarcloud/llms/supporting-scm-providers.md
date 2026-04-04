# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Source: https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/supporting-scm-providers.md

# Supporting SCM providers

The SonarScanners use information from the project’s SCM provider, if available, to:

* Assign a new issue to the person who introduced it. The last committer on the related line of code is considered to be the author of the issue.
* Estimate the coverage on new code, including added and changed code since in your new code.
* Display the most recent commit on each line in the code viewer.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/IcBvVyFBgnej1YvKo6TS/executable-lines-python-exception.png" alt="Exempt a block of Python code from coverage"><figcaption><p>Exempt a block of Python code from coverage</p></figcaption></figure>

The only required SCM command is "blame", which gets the last committer of each line for a given file. This command is executed by a SonarQube Server plugin through the extension point `org.sonar.api.batch.scm.ScmProvider`. See the embedded [scm-integration](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scm-integration "mention") documentation for more details.
