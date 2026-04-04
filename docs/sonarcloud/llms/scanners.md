# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners.md

# Scanners

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
