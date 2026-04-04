# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/docker.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/docker.md

# Docker

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

Dockerfile versions 1.0 to 1.6 are supported.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the Docker-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Docker**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Dockerfiles <a href="#dockerfiles" id="dockerfiles"></a>

**No NoSonar Support:**

Trailing comments are not permitted in Dockerfiles. For this reason, our Dockerfile parser does not support NOSONAR comments to suppress issues. Issues and hotspots must be reviewed in the UI.

**Missing Uniform Filename Convention:**

Dockerfiles can have all kinds of names and do not need a file extension. For this reason, it is difficult for the scanner and the analyzer to recognize all Dockerfiles. By default, all files named Dockerfile, Dockerfile.\*, or \*.dockerfile are considered Dockerfiles. If other conventions apply, these can be specified via the scanner property sonar.lang.patterns.docker.
