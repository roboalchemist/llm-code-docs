# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/analysis-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-overview.md

# SonarQube Server analysis overview

With SonarQube Server, you can perform automated code review and analysis of your project’s main branch, as well as multiple branches and pull requests.

### What is automated code review? <a href="#what-is-automated-code-review" id="what-is-automated-code-review"></a>

An automated code review is a software development process in which static code analysis tools are used to automatically review and analyze the source code for potential issues and coding standard violations. Automated code review accelerates the identification and resolution of code issues and improves code quality (reliability, security, maintainability).

### Code analysis with the SonarScanner <a href="#sonarscanner" id="sonarscanner"></a>

The SonarScanner performs the automated source code analysis as part of your code review process. This stand-alone program runs on the CI/CD host and sends the analysis results to SonarQube Server, which computes them, calculates the quality gate, and generates reports.

To perform the analysis, the SonarScanner uses the [supported languages](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/overview) that it downloads from SonarQube Server at installation.&#x20;

The Sonar Solution offers SonarScanners that integrate with the following build systems: Gradle, Maven, .NET, NPM, and Python. For other project types, the SonarScanner CLI which requires more manual configuration is used.

### Analysis process <a href="#analysis-process" id="analysis-process"></a>

Essentially, the main steps of the analysis process are:

1. Your build or CI pipeline starts the SonarScanner.
2. The SonarScanner scans the local repository and determines the files to be analyzed according to the configured analysis scope.
3. The scanner sends an analysis request to the respective language analyzer which retrieves the files to be analyzed from the file system and analyzes them according to the configured [quality profiles](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles).&#x20;
4. The analyzer sends the analysis results ([metrics](https://docs.sonarsource.com/sonarqube-server/user-guide/code-metrics/metrics-definition) and [issues](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview)) to the scanner which forwards them to SonarQube Server in the form of a report.
5. SonarQube Server computes the analysis results asynchronously to perform the following:
   * It identifies the new issues according to the configured [quality standards](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code) and raises them in both the new code and the overall code (It uploads the code as part of the analysis and shows users the code that it raised issues on. Unanalyzed changes in the code are not visible.).
   * It computes the [quality gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates).
   * It generates reports.

{% hint style="info" %}
By default, only files that are recognized by your edition of SonarQube Server are loaded into the project during analysis.
{% endhint %}

### Integration into your CI pipeline <a href="#ci-pipeline" id="ci-pipeline"></a>

Integrating SonarQube Server into your CI pipeline brings powerful code review capabilities to your projects. Key features include main branch analysis, pull request analysis, and multiple branch analysis, ensuring comprehensive code quality checks at every stage of development.

The relevant CI pipeline steps with SonarQube Server integration are:

1. A developer pushes changes on a branch to the remote repository.
2. A CI pipeline is triggered for the specific branch. For this purpose, webhooks may be used when events occur in the Source Control Management (SCM) system or the repository may be monitored by a CI/CD tool like Jenkins.
3. The pipeline clones the remote repository and checks out the relevant branch to the local repository on the CI/CD host (The code and SCM metadata are copied.).
4. In the case of a compiled programming language, the pipeline builds the code.
5. The pipeline executes the appropriate Sonar Scanner to analyze the code.
6. The scanner sends the analysis results to SonarQube Server, which computes them.
7. The Server sends the Quality Gate computation result to the CI pipeline (This step is optional.).
8. The pipeline continues (if the Quality Gate succeeds) or stops (otherwise).

<figure><img src="broken-reference" alt="An overview of the SonarQube Server analysis process."><figcaption></figcaption></figure>

### Scanner engine and analyzers download at analysis time <a href="#scanner-engine-and-analyzers-download" id="scanner-engine-and-analyzers-download"></a>

A SonarScanner is a scanner bootstrapper that downloads the scanner engine and language analyzers from SonarQube Server at analysis time. This way:

* It ensures that the scanner engine and analyzer versions are compatible with SonarQube Server.
* Only the analyzers necessary to analyze the detected languages are downloaded.

The figure below shows a simplified view of the download process of the scanner engine and language analyzers. For each analysis run:

1. The CI or build pipeline starts the SonarScanner.
2. The SonarScanner connects to SonarQube Server to retrieve the scanner engine version to be used. It checks the scanner cache for the scanner engine version. If it doesn’t find it, it downloads it from SonarQube Server and stores it in the cache.
3. The scanner engine scans the code to identify the different languages used in the project to be analyzed.
4. The scanner engine checks the scanner cache for the required language analyzers. If it doesn’t find them, it downloads them from SonarQube Server and stores them in the cache.

<figure><img src="broken-reference" alt="The SonarScanner downloads the Scanner engine which downloads the language analyzers"><figcaption></figcaption></figure>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [overview](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/overview "mention")
* [troubleshooting-the-analysis](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/troubleshooting-the-analysis "mention")
