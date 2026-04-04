# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/azure-devops-integration/troubleshooting-analysis.md

# Troubleshooting analysis

See also [troubleshooting-the-analysis](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/troubleshooting-the-analysis "mention").

### Azure build pipeline fails <a href="#azure-pipeline-fails" id="azure-pipeline-fails"></a>

If your Azure build pipeline fails on the analysis stage, check that you correctly set the integration at the global level. In particular, check the PAT failure points. See [#preparing](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/setting-up-integration-at-global-level#preparing "mention") for more information.

### Missing blame information or Could not find ref error <a href="#missing-blame-info-error" id="missing-blame-info-error"></a>

The errors "*Missing blame information…*" and "*Could not find ref…*" can be caused by checking out with a partial or shallow clone, or when using Git submodules. You should disable git shallow clone to make sure the scanner has access to all of your history when running analysis with Azure DevOps.

For more information, see the MS article on [Shallow fetch](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops\&tabs=yaml#shallow-fetch).

### Self-signed certificate error on Prepare Analysis Configuration task <a href="#self-signed-certificate-error" id="self-signed-certificate-error"></a>

Try to add the server self-signed certificate as described in [#azure-pipelines](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/manage-tls-certificates#azure-pipelines "mention").
