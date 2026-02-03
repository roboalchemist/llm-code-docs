# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners/scanner-environment/managing-jre-auto-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners/scanner-environment/managing-jre-auto-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners/scanner-environment/managing-jre-auto-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/managing-jre-auto-provisioning.md

# Managing JRE auto-provisioning

### About the JRE auto-provisioning feature

With JRE auto-provisioning, the Java Runtime Environment (JRE) version required for the scanner engine is automatically downloaded by the scanner from SonarQube. You may have to disable JRE auto-provisioning to manage your internally certified versions. In rare cases, you may have to adjust the default configuration.

If supported by your scanner, JRE auto-provisoning is enabled by default.

JRE auto-provisioning is currently supported by:

• SonarScanner CLI, from version 6.0.

• SonarScanner for .NET, from version 7.0.

• SonarScanner for NPM, from version 4.0.

• SonarScanner for Maven, from version 5.0.

• SonarScanner for Gradle, from version 6.0.

### Disabling JRE auto-provisioning

If you disable JRE auto-provisioning, make sure to provide a JRE that follows the necessary requirements. See [general-requirements](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/scanner-environment/general-requirements "mention").

To disable JRE auto-provisioning at the instance level (you need the Administer System permission):

1. Go to **Administration > Configuration > General Settings > General > General**.
2. Enable the **Disable Scanner JRE auto provisioning** option.

Alternatively, you can as well use the `sonar.scanner.skipJreProvisioning` analysis parameter and specify your own version of Java. For more details, see [#jre-autoprovisioning](https://docs.sonarsource.com/sonarqube-server/analysis-parameters#jre-autoprovisioning "mention").

### Adjusting JRE auto-provisioning

If the auto-detection doesn't work properly, you can set analysis parameters on your CI/CD host to:

* Define the operating system and / or CPU architecture type of your CI/CD host.
* Skip the JRE auto-provisioning and / or define the JRE version to be used by the scanner.

For more details, see [#jre-autoprovisioning](https://docs.sonarsource.com/sonarqube-server/analysis-parameters#jre-autoprovisioning "mention").

### Related pages

[#scanner-engine-and-analyzers-download](https://docs.sonarsource.com/sonarqube-server/analysis-overview#scanner-engine-and-analyzers-download "mention")
