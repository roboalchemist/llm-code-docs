# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/key-features.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/key-features.md

# Key features

The Jenkins extension for SonarQube lets you centralize the configuration of your SonarQube connection details in Jenkins global configuration.

* You can install the SonarScanner CLI, for Maven, for Gradle, or for .NET from Jenkins and centralize the configuration of SonarQube Cloud connection details in Jenkins global configuration.
* You can trigger the SonarQube Cloud analysis from your Jenkins Freestyle or Pipeline jobs using standard Jenkins build steps or [Jenkins Pipeline DSL](https://jenkins.io/solutions/pipeline/). Once the Jenkins job is complete, the extension will detect that a SonarQube Cloud analysis was made during the build and display a badge and a widget on the job page with a link to the SonarQube Cloud dashboard as well as quality gate status.
* Starting in the SonarQube Cloud Team plan, you can configure an automatic failing of your pipeline in case your code fails the quality gate you defined in SonarQube Cloud: see below.

### Automatic interruption of your pipeline in case the quality gate fails <a href="#pipeline-interruption" id="pipeline-interruption"></a>

This feature is available starting in the SonarQUbe Cloud Team plan. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") page for more details.

With the Jenkins extension, you can configure that your pipeline job fails in case the quality gate computed by SonarQube Cloud for your project fails. To do so, the extension makes webhook available: a webhook call must be configured in SonarQube Cloud to call back into Jenkins to allow the pipeline to continue or fail.

The figure below illustrates the process:

1. A Jenkins Pipeline job is started.
2. The job triggers the analysis by the SonarScanner.
3. The SonarScanner sends the results to SonarQube Cloud.
4. SonarQube Cloud completes the analysis, computes the quality gate configured for the project, and checks if the project fails or passes the quality gate.
5. SonarQube Cloud sends the pass or failure result back to the Jenkins webhook exposed by the extension.
6. The pipeline job continues (in case of a pass) or fails (otherwise).

<figure><img src="broken-reference" alt="How Jenkins integrates with the Sonar products."><figcaption></figcaption></figure>

### Related links <a href="#related-links" id="related-links"></a>

* [global-setup](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/global-setup "mention")
* [add-analysis-to-job](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/add-analysis-to-job "mention")
* [pipeline-pause](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/jenkins/pipeline-pause "mention")
