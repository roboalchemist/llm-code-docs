# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/overview-of-integrated-cis.md

# Overview of integrated CIs

### CI integrations <a href="#ci-integrations" id="ci-integrations"></a>

SonarQube Cloud supports integration with the following continuous integration (CI) systems:

* [github-actions-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/github-actions-for-sonarcloud "mention")
* [bitbucket-pipelines-for-sonarcloud](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/bitbucket-pipelines-for-sonarcloud "mention")
* [azure-pipelines](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/azure-pipelines "mention")
* [gitlab-ci](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/gitlab-ci "mention")
* [circleci](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/circleci "mention")
* [other-cis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/other-cis "mention")

### Scanners <a href="#integrated-cis-scanners" id="integrated-cis-scanners"></a>

In SonarQube Cloud terminology, a *scanner* is the piece of software that performs the actual analysis on your code.

Typically, a scanner is configured to work as part of your build pipeline. Sonar provides different versions of the *SonarScanner* tool for different set-ups.

If your build process takes place on an on-premises machine (your own or some central build machine in your organization), you will need to download the appropriate scanner from Sonar, install it, and configure it.

If your build process is cloud-based (using CircleCI or similar), Sonar provides SonarScanner plugins that can be installed in those services.

SonarQube Cloud supports the following scanners and extensions, adapted to different setups:

* [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention"): Generic command-line tool for setups where no specialized scanner is available.
* [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention"): For use with Azure Pipelines.
* [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention"): For use with Java Gradle projects.
* [sonarcloud-extension-for-jenkins](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-jenkins "mention"): For use with Jenkins jobs.
* [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention"): For use with Java Maven projects.
* [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet "mention"): For use with .NET projects.
* [sonarscanner-for-npm](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-npm "mention"): For use with analysis on JS/TS and CSS code bases.

### Prerequisites for scanners <a href="#prerequisites-for-scanners" id="prerequisites-for-scanners"></a>

See [general-requirements](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/scanner-environment/general-requirements "mention").

### How the scanners work <a href="#how-the-scanners-work" id="how-the-scanners-work"></a>

All the scanner variants just wrap SonarQube Cloud’s powerful set of language analyzers. Since the scanner is installed as part of your build process, we don’t want you to have to re-install it every time a SonarQube Cloud language analyzer is added or improved. To ensure this, SonarScanner always checks for updates to its analyzer set from SonarQube Cloud and downloads any recent additions or changes, thus always staying up-to-date.

When the scanner is invoked it executes the analysis on the code and sends the results back up to SonarQube Cloud, where they are processed, stored, and displayed in the SonarQube Cloud interface.

### Comparison with automatic analysis <a href="#comparison-with-automatic-analysis" id="comparison-with-automatic-analysis"></a>

SonarQube Cloud’s *automatic analysis* can be thought of as a scanner that is integrated into the cloud service. It can be used without installing any additional software or integrating anything into your build pipeline.

For more details on automatic analysis, see [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention").

### Conflict between CI-based and automatic analysis <a href="#conflict-between-ci-based-and-automatic-analysis" id="conflict-between-ci-based-and-automatic-analysis"></a>

CI-based analysis (i.e., using SonarScanner as part of your build process) is not meant to run concurrently with automatic analysis. If automatic analysis is enabled on a project, any attempt to run a SonarScanner on the same project will fail, failing the build pipeline as it does so. Either use automatic analysis or use a CI-based analysis with SonarScanner, but not both!

For details on [#deactivating-automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/automatic-analysis#deactivating-automatic-analysis "mention") or reactivating automatic analysis, see the[automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") page.
