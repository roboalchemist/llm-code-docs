# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/ci-integration/codemagic-integration.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/codemagic-integration.md

# Codemagic integration

SonarScanners running in Codemagic can automatically detect branches and merge or pull requests in certain jobs. You don’t need to explicitly pass the branch or pull request details.

### Adding SonarQube Server scripts to your Codemagic .yml file <a href="#codemagic" id="codemagic"></a>

To analyze your code when using Codemagic:

* Add the following scripts to your existing `codemagic.yaml` file:

```yaml
scripts:   
   - |
       # download and install the SonarScanner
       wget -O $FCI_BUILD_DIR/sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.4.0.2170-macosx.zip
       # If running in a Linux environment, download https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.4.0.2170-linux.zip 
       unzip $FCI_BUILD_DIR/sonar-scanner.zip
       mv sonar-scanner-* sonar-scanner
  - |
       # Generate and upload code analysis report
       export PATH=$PATH:$FCI_BUILD_DIR/sonar-scanner/bin
       sonar-scanner \
       -Dsonar.projectKey=YOUR_PROJECT_KEY \
       -Dsonar.host.url=SONARQUBE_URL \
```

* Define `SONAR_TOKEN` as a Codemagic environment variable.

### Automatically detecting pull requests <a href="#detecting-pull-requests" id="detecting-pull-requests"></a>

For SonarQube Server to automatically detect pull requests when using Codemagic, you need to add an event in the triggering section of your `codemagic.yaml` file as shown in the following snippet:

```yaml
    triggering:
      events:
        - pull_request
```

For triggering to work, you also need to set up a link between Codemagic and your DevOps platform (Bitbucket, Github, etc.). See the [Codemagic documentation](https://docs.codemagic.io/configuration/webhooks/) for more information.

### Caching the .sonar folder <a href="#sonar-folder" id="sonar-folder"></a>

Caching the `.sonar` folder saves time on subsequent analyses. To do this, add the following snippet to your `codemagic.yaml` file:

```yaml
    cache:
      cache_paths:
        - ~/.sonar
```
