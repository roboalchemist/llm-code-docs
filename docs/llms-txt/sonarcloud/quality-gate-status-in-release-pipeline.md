# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/adding-analysis-to-pipeline/quality-gate-status-in-release-pipeline.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/quality-gate-status-in-release-pipeline.md

# Checking quality gate in release pipeline

If the Publish Quality Gate Result task in your build pipeline is enabled, you can check the SonarQube Cloud quality gate status in your release pipeline. It takes place as a [pre-deployment gate](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/approvals/gates?view=azure-devops).

Note that this feature is in preview and:

* Only the quality gate related to the primary build artifact of the release will be checked.
* During a build, if multiple analyses are performed, all of the related quality gates are checked. If one of them has the status WARN, ERROR, or NONE, then the quality gate status on the release pipeline will be failed.
* If the quality gate is in the failed state, it will not be possible to get the pre-deployment gate passing as this status will remain in its initial state. You will have to execute another build with either the current issues corrected in SonarQube Cloud or with another commit for fixing them.
* The pre-deployment gates in the release pipeline check the status every five minutes for one day, by default. If you know that the SonarQube quality gate has failed and will remain in the failed state on Azure DevOps, you can increase this duration to a maximum of 6 minutes (so the gate will be evaluated only twice), or just cancel the release itself.

To check the SonarQube Cloud quality gate status in your Azure release pipeline:

1. In the Azure **release pipeline**, add a stage, then select **pre-deployment conditions**.
2. Enable the **gates**, then select **add**. Choose **SonarQube Cloud Quality Gate status check**.
3. Save your pipeline.

### Related pages <a href="#related-pages" id="related-pages"></a>

Adding the analysis to your build pipeline:

* [gradle-or-maven-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/gradle-or-maven-project "mention")
* [dotnet-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/dotnet-project "mention")
* [c-family-project](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/c-family-project "mention")
* [js-ts-go-python-php](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/js-ts-go-python-php "mention")
* [monorepo-projects](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/adding-analysis-to-build-pipeline/monorepo-projects "mention")
* [sonarqube-tasks](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines/sonarqube-tasks "mention")
