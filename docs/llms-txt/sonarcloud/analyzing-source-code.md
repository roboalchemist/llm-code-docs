# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code.md

# Analyzing source code

- [SonarQube Server analysis overview](/sonarqube-server/analyzing-source-code/analysis-overview.md): This page explains SonarQube Server’s main analysis steps and how SonarQube Server integrates with your CI pipeline.
- [Project analysis setup](/sonarqube-server/analyzing-source-code/overview.md): This page introduces briefly the prerequisites and the setup steps necessary for a project analysis with SonarQube Server.
- [Scanners](/sonarqube-server/analyzing-source-code/scanners.md): Information about various SonarScanners.
- [Scanner environment](/sonarqube-server/analyzing-source-code/scanners/scanner-environment.md): Information on scanner environment requirements, TLS certificates, and checked out code.
- [General requirements](/sonarqube-server/analyzing-source-code/scanners/scanner-environment/general-requirements.md): General requirements for setting up your SonarScanner for SonarQube Server.
- [TLS certificates on client side](/sonarqube-server/analyzing-source-code/scanners/scanner-environment/manage-tls-certificates.md): If your SonarQube Server instance is secured, add the self-signed certificate to the CI/CD host. If mutual TLS is used, an additional setup is required.
- [Checked-out code](/sonarqube-server/analyzing-source-code/scanners/scanner-environment/verifying-code-checkout-step.md): During the checkout of a working copy (clone) of the code from the project repository, we recommend using the full depth.
- [Managing JRE auto-provisioning](/sonarqube-server/analyzing-source-code/scanners/scanner-environment/managing-jre-auto-provisioning.md): How to disable or adjust JRE auto-provisioning for scanners.
- [SonarScanner CLI](/sonarqube-server/analyzing-source-code/scanners/sonarscanner.md): The SonarScanner CLI is the scanner to use when there is no specific scanner for your build system.
- [Azure DevOps Extension](/sonarqube-server/analyzing-source-code/scanners/sonarqube-extension-for-azure-devops.md): The Azure DevOps Extension for SonarQube Server makes it easy to integrate analysis into your build pipeline, allowing you to analyze all supported languages.
- [Jenkins extension](/sonarqube-server/analyzing-source-code/scanners/jenkins-extension-sonarqube.md): This extension lets you centralize the configuration of your SonarQube Server connection details in your Jenkins global configuration.
- [SonarScanner for Maven](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-maven.md): The SonarScanner for Maven is recommended as the default scanner for Maven projects.
- [SonarScanner for Gradle](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-gradle.md): The SonarScanner for Gradle provides an easy way to start the analysis of a Gradle project with SonarQube Server.
- [SonarScanner for .NET](/sonarqube-server/analyzing-source-code/scanners/dotnet.md): Information on installing, using, and configuring the SonarScanner for .NET.
- [Introduction](/sonarqube-server/analyzing-source-code/scanners/dotnet/introduction.md): Your entry point to understanding how the SonarScanner for .NET works with SonarQube Server.
- [Installing the scanner](/sonarqube-server/analyzing-source-code/scanners/dotnet/installing.md): Installing the SonarScanner for .NET to run with SonarQube Server is easy. Everything you need to know is on this page.
- [Using the scanner](/sonarqube-server/analyzing-source-code/scanners/dotnet/using.md): Check this page to learn how to invoke the SonarScanner for .NET and understand which parameters to use in your SonarQube Server analysis.
- [Configuring the scanner](/sonarqube-server/analyzing-source-code/scanners/dotnet/configuring.md): Configuring the SonarScanner for .NET in SonarQube Server can be tricky. Here is everything you need to know.
- [SonarScanner for NPM](/sonarqube-server/analyzing-source-code/scanners/npm.md): This section describes how to install, use, and configure the sonarScanner for NPM.
- [Introduction](/sonarqube-server/analyzing-source-code/scanners/npm/introduction.md): The SonarScanner for NPM makes it very easy to trigger a SonarQube Server analysis on your JavaScript code base, without needing additional tools or resources.
- [Installing the scanner](/sonarqube-server/analyzing-source-code/scanners/npm/installing.md): Depending on how you want to start the SonarScanner for NPM, you will use a different method to install the scanner.
- [Using the scanner](/sonarqube-server/analyzing-source-code/scanners/npm/using.md): To start the SonarScanner for NPM, you can either add the analysis to your build files or use the scanner start command line (with or without npx).
- [Configuring the scanner](/sonarqube-server/analyzing-source-code/scanners/npm/configuring.md): This section explains how to configure the parameters used for an analysis with the SonarScanner for NPM when running it with SonarQube Server.
- [SonarScanner for Python](/sonarqube-server/analyzing-source-code/scanners/sonarscanner-for-python.md): The SonarScanner for Python provides an easy way to start the analysis of a Python project with SonarQube Server.
- [Analysis parameters](/sonarqube-server/analyzing-source-code/analysis-parameters.md): Analysis parameters are used to set up your analysis.
- [Configuration overview](/sonarqube-server/analyzing-source-code/analysis-parameters/configuration-overview.md): This page explains the hierarchy and provides general configuration guidelines regarding the analysis parameters.
- [Parameters not settable in the UI](/sonarqube-server/analyzing-source-code/analysis-parameters/parameters-not-settable-in-ui.md): This section lists the analysis parameters (sonar properties) that must be configured on the CI/CD host, as they cannot be set within the user interface.
- [Languages](/sonarqube-server/analyzing-source-code/languages.md)
- [Supported languages](/sonarqube-server/analyzing-source-code/languages/overview.md): SonarQube Server provides analysis of different languages depending on the edition you’re running.
- [ABAP](/sonarqube-server/analyzing-source-code/languages/abap.md): ABAP analysis is available starting in commercial editions of SonarQube Server.
- [Ansible](/sonarqube-server/analyzing-source-code/languages/ansible.md): Language-specific information about the way SonarQube Server supports the analysis of Ansible.
- [Apex](/sonarqube-server/analyzing-source-code/languages/apex.md): Apex analysis is available starting in SonarQube Server Enterprise Edition.
- [Azure Resource Manager](/sonarqube-server/analyzing-source-code/languages/azure-resource-manager.md): SonarQube analysis supports Azure Resource Manager templates in the JSON & Bicep formats, and is available starting in Community Edition.
- [C/C++/Objective-C](/sonarqube-server/analyzing-source-code/languages/c-family.md): Information on how to set up, run, and customize analysis for C, C++ and Objective-C.
- [C/C++/Objective-C analysis overview](/sonarqube-server/analyzing-source-code/languages/c-family/overview.md): An overview of the configuration required to analyze CFamily code in SonarQube Server.
- [Analysis modes](/sonarqube-server/analyzing-source-code/languages/c-family/analysis-modes.md): Presentation of the several analysis modes.
- [Prerequisites](/sonarqube-server/analyzing-source-code/languages/c-family/prerequisites.md): Prerequisites for CFamily analysis in SonarQube Server.
- [Running the analysis](/sonarqube-server/analyzing-source-code/languages/c-family/running-the-analysis.md): How to run a CFamily code analysis in SonarQube Server.
- [Customizing the analysis](/sonarqube-server/analyzing-source-code/languages/c-family/customizing-the-analysis.md): How to customize your CFamily code analysis.
- [Understanding the analysis](/sonarqube-server/analyzing-source-code/languages/c-family/understanding-the-analysis.md): Details on the CFamily analysis and the way it works with SonarQube Server.
- [Related pages](/sonarqube-server/analyzing-source-code/languages/c-family/related-pages.md): Pages related to CFamily analysis in SonarQube Server
- [CloudFormation](/sonarqube-server/analyzing-source-code/languages/cloudformation.md): SonarQube Server can analyze Infrastructure-as-Code (IaC) languages such as CloudFormation, Kubernetes, and Terraform.
- [COBOL](/sonarqube-server/analyzing-source-code/languages/cobol.md): Cobol analysis is available starting in Enterprise Edition.
- [C#](/sonarqube-server/analyzing-source-code/languages/csharp.md): C# analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [Dart](/sonarqube-server/analyzing-source-code/languages/dart.md): SonarQube Server can analyze the Dart language.
- [Docker](/sonarqube-server/analyzing-source-code/languages/docker.md): SonarQube Server can analyze Infrastructure-as-Code (IaC) languages such as CloudFormation, Kubernetes, and Terraform.
- [Flex](/sonarqube-server/analyzing-source-code/languages/flex.md): Flex analysis is available starting in all editions of SonarQube Server and SonarQube Community Build.
- [GitHub Actions](/sonarqube-server/analyzing-source-code/languages/github-actions.md): SonarQube supports analysis of YAML files detected as GitHub Actions.
- [Go](/sonarqube-server/analyzing-source-code/languages/go.md): Go analysis is available in all editions of SonarQube.
- [HTML](/sonarqube-server/analyzing-source-code/languages/html.md): HTML analysis is available in all editions of SonarQube and SonarQube Community Build.
- [Java](/sonarqube-server/analyzing-source-code/languages/java.md): Java analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [JavaScript/TypeScript/CSS](/sonarqube-server/analyzing-source-code/languages/javascript-typescript-css.md): JavaScript, TypeScript, and CSS analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [JCL](/sonarqube-server/analyzing-source-code/languages/jcl.md): JCL analysis is available starting in SonarQube Server Enterprise Edition and supported by SonarQube for Eclipse when running in Connected Mode.
- [JSON](/sonarqube-server/analyzing-source-code/languages/json.md)
- [Kotlin](/sonarqube-server/analyzing-source-code/languages/kotlin.md): Kotlin analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [Kubernetes/Helm](/sonarqube-server/analyzing-source-code/languages/kubernetes.md): SonarQube Server can analyze Infrastructure-as-Code (IaC) languages such as CloudFormation, Kubernetes, and Terraform.
- [PHP](/sonarqube-server/analyzing-source-code/languages/php.md): PHP analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [PLI](/sonarqube-server/analyzing-source-code/languages/pli.md): PLI analysis is available starting in SonarQube Server Enterprise Edition.
- [PL/SQL](/sonarqube-server/analyzing-source-code/languages/pl-sql.md): PL/SQL analysis is available starting in SonarQube Server Developer Edition.
- [Python](/sonarqube-server/analyzing-source-code/languages/python.md): Python analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [RPG](/sonarqube-server/analyzing-source-code/languages/rpg.md): RPG is available starting in SonarQube Server Enterprise Edition.
- [Ruby](/sonarqube-server/analyzing-source-code/languages/ruby.md): Ruby analysis is available in all editions of SonarQube Server and Community Build.
- [Rust](/sonarqube-server/analyzing-source-code/languages/rust.md)
- [Scala](/sonarqube-server/analyzing-source-code/languages/scala.md): Scala analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [Shell](/sonarqube-server/analyzing-source-code/languages/shell.md): The Shell analyzer for SonarQube Server is designed to perform static code analysis on Bash and POSIX Shell scripts.
- [Swift](/sonarqube-server/analyzing-source-code/languages/swift.md): Swift analysis is available starting in SonarQube Server Developer Edition.
- [Secrets](/sonarqube-server/analyzing-source-code/languages/secrets.md): SonarQube Server detects exposed Secrets in your source code and language-agnostic config files, starting in the SonarQube Community Build.
- [Terraform](/sonarqube-server/analyzing-source-code/languages/terraform.md): SonarQube Server can analyze Infrastructure-as-Code (IaC) languages such as CloudFormation, Kubernetes, and Terraform.
- [T-SQL](/sonarqube-server/analyzing-source-code/languages/t-sql.md): T-SQL analysis is available starting in SonarQube Server Developer Edition.
- [VB.NET](/sonarqube-server/analyzing-source-code/languages/vb-dotnet.md): VB.NET analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [VB6](/sonarqube-server/analyzing-source-code/languages/vb6.md): VB6 analysis is available starting in the SonarQube Server Enterprise Edition.
- [XML](/sonarqube-server/analyzing-source-code/languages/xml.md): XML analysis is available in all editions of SonarQube Server and SonarQube Community Build.
- [YAML](/sonarqube-server/analyzing-source-code/languages/yaml.md)
- [.NET environments](/sonarqube-server/analyzing-source-code/dotnet-environments.md): This section contains information on how to work with .NET environments when using SonarQube Server.
- [Overview](/sonarqube-server/analyzing-source-code/dotnet-environments/overview.md): Running .NET analysis on SonarQube Server can be tricky to set up. This page gives you an overview of what’s required depending on your .NET framework.
- [Getting started with .NET](/sonarqube-server/analyzing-source-code/dotnet-environments/getting-started-with-net.md): Your page to get started setting up a .NET analysis in any edition of SonarQube Server.
- [SonarScanner for .NET](/sonarqube-server/analyzing-source-code/dotnet-environments/sonarscanner-for-dotnet.md): Understanding how to analyze .NET projects in SonarQube Server can be difficult. This user guide helps make the setup process easy.
- [.NET test coverage](/sonarqube-server/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md): SonarQube Server supports the reporting of test coverage information as part of the analysis of your .NET project.
- [Specifying test projects](/sonarqube-server/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md): The SonarScanner for .NET analyzes test projects in a different way than main projects. Metrics sent to SonarQube Server provide more insight into your project.
- [VB.NET](/sonarqube-server/analyzing-source-code/dotnet-environments/vb-dotnet.md): VB.NET analysis is available in all editions of SonarQube Server.
- [Troubleshooting](/sonarqube-server/analyzing-source-code/dotnet-environments/troubleshooting.md): Sometimes problems occur when dialing in your .NET analysis in SonarQube Server. Here are some guides created to explain use cases and potential problems.
- [Test coverage](/sonarqube-server/analyzing-source-code/test-coverage.md): Information on the reporting of test coverage information as part of your project analysis.
- [Overview](/sonarqube-server/analyzing-source-code/test-coverage/overview.md): SonarQube's test coverage reports and test execution reports are important metrics in assessing the quality of your code.
- [C / C++ / Objective-C test coverage](/sonarqube-server/analyzing-source-code/test-coverage/c-family-test-coverage.md): Information on reporting test coverage information in SonarQube Server for the CFamily languages.
- [Dart test coverage](/sonarqube-server/analyzing-source-code/test-coverage/dart-test-coverage.md): Information on reporting test coverage information in SonarQube Server for Dart.
- [Go test coverage](/sonarqube-server/analyzing-source-code/test-coverage/go-test-coverage.md): SonarQube Server supports the reporting of test coverage information as part of the analysis of your Go project.
- [Java test coverage](/sonarqube-server/analyzing-source-code/test-coverage/java-test-coverage.md): Information on reporting test coverage information in SonarQube Server for Java.
- [JavaScript / TypeScript test coverage](/sonarqube-server/analyzing-source-code/test-coverage/javascript-typescript-test-coverage.md): Information on reporting test coverage information in SonarQube Server for Javascript and Typescript.
- [.NET test coverage](/sonarqube-server/analyzing-source-code/test-coverage/dotnet-test-coverage.md): Information on reporting test coverage information in SonarQube Server for .NET projects.
- [PHP test coverage](/sonarqube-server/analyzing-source-code/test-coverage/php-test-coverage.md): Information on reporting test coverage information in SonarQube Server for PHP projects.
- [Python test coverage](/sonarqube-server/analyzing-source-code/test-coverage/python-test-coverage.md): Information on reporting test coverage information in SonarQube Server for Python projects.
- [Generic test data](/sonarqube-server/analyzing-source-code/test-coverage/generic-test-data.md): SonarQube supports generic formats for test coverage and test execution import.
- [Test coverage parameters](/sonarqube-server/analyzing-source-code/test-coverage/test-coverage-parameters.md): SonarQube's test coverage reports describe the percentage of your code that has been tested by your test suite during a build.
- [Test execution parameters](/sonarqube-server/analyzing-source-code/test-coverage/test-execution-parameters.md): This page describes what analysis parameters are needed to import test execution reports into SonarQube.
- [Importing external issues](/sonarqube-server/analyzing-source-code/importing-external-issues.md): How to import issues generated by third-party analyzers into your project analysis.
- [About external issues](/sonarqube-server/analyzing-source-code/importing-external-issues/about-external-issues.md): Issues generated by third-party analyzers can be imported into SonarQube Server.
- [External analyzer reports](/sonarqube-server/analyzing-source-code/importing-external-issues/external-analyzer-reports.md): How to set up the import for your project of issues generated by third-party analyzers that integrate with SonarQube.
- [Generic formatted reports](/sonarqube-server/analyzing-source-code/importing-external-issues/generic-issue-import-format.md): SonarQube Server supports a generic import format for raising external issues in code.
- [SARIF reports](/sonarqube-server/analyzing-source-code/importing-external-issues/importing-issues-from-sarif-reports.md): SonarQube Server supports the standard Static Analysis Results Interchange Format (SARIF) for raising external issues in code.
- [Background tasks](/sonarqube-server/analyzing-source-code/background-tasks.md): Information on background tasks in SonarQube Server.
- [Pull request analysis](/sonarqube-server/analyzing-source-code/pull-request-analysis.md): Information on setting up pull request analysis for your projects.
- [Introduction](/sonarqube-server/analyzing-source-code/pull-request-analysis/introduction.md): SonarQube Server supports pull request analysis: analysis results only include issues that have been introduced by the pull request itself.
- [Setting up the pull request analysis](/sonarqube-server/analyzing-source-code/pull-request-analysis/setting-up-the-pull-request-analysis.md): With SonarQube Server, a pull request analysis occurs when a pull request is opened and every time a change is pushed to the pull request branch.
- [Branch analysis](/sonarqube-server/analyzing-source-code/branch-analysis.md): Information on setting up Branch analysis for your projects.
- [Introduction](/sonarqube-server/analyzing-source-code/branch-analysis/introduction.md): Branch analysis allows you to trigger an analysis on a push to any long-living branch or to short-lived branches without involving pull requests.
- [Setting up the branch analysis](/sonarqube-server/analyzing-source-code/branch-analysis/setting-up-the-branch-analysis.md): In SonarQube Server, branch analysis allows you to trigger an analysis on a push to any specified branch without involving pull requests.
- [CI integration](/sonarqube-server/analyzing-source-code/ci-integration.md): Information on integrating SonarQube Server with your CI pipelines.
- [Overview](/sonarqube-server/analyzing-source-code/ci-integration/overview.md): SonarQube Server supports integration on multiple platforms allowing you to maintain code quality and security in your projects.
- [Jenkins integration](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration.md): Information on integrating SonarQube Server with Jenkins.
- [Key features](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/key-features.md): Sonar provides an extension for Jenkins to enable smooth integration with Jenkins. This section explains the key features of this integration.
- [Setting up Jenkins](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/global-setup.md): This page explains how to set up Jenkins globally for the integration with SonarQube Server by using SonarQube extension for Jenkins.
- [Adding analysis to a Jenkins job](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/add-analysis-to-job.md): This section explains how to add the SonarQube Server analysis to your Jenkins Freestyle or Pipeline jobs.
- [Setting up a pipeline pause](/sonarqube-server/analyzing-source-code/ci-integration/jenkins-integration/pipeline-pause.md): To configure an automatic failing of your Jenkins pipeline in case the quality gate computed by SonarQube Server fails, you must set up a pipeline pause.
- [Codemagic integration](/sonarqube-server/analyzing-source-code/ci-integration/codemagic-integration.md): Information on setting up Codemagic with SonarQube Server.
- [SCM integration](/sonarqube-server/analyzing-source-code/scm-integration.md): Collecting SCM data during code analysis can unlock a number of SonarQube Server features.
- [Security engine custom configuration](/sonarqube-server/analyzing-source-code/security-engine-custom-configuration.md): Security Engine Custom Configuration is available as part of the Enterprise Edition. The security engine tracks the path that data follows through your code.
- [Troubleshooting the analysis](/sonarqube-server/analyzing-source-code/troubleshooting-the-analysis.md): If your SonarQube Server analysis errors out.
- [Incremental analysis](/sonarqube-server/analyzing-source-code/incremental-analysis.md): Information on SonarQube incremental analysis and how to disable or change the mechanisms.
- [About the incremental analysis](/sonarqube-server/analyzing-source-code/incremental-analysis/introduction.md): This page explains the mechanisms used to perform incremental branch and pull request analysis in SonarQube Server.
- [Disabling or changing the mechanisms](/sonarqube-server/analyzing-source-code/incremental-analysis/disabling-or-changing.md): In very specific cases, you may have to disable or change the incremental analysis mechanism.
- [JFrog Evidence Collection integration](/sonarqube-server/analyzing-source-code/jfrog-evidence-collection-integration.md): SonarQube Server integrates with JFrog Evidence Collection to provide trusted auditing for software packages.
