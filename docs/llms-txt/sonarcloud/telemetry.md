# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/telemetry.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/telemetry.md

# Telemetry

Your SonarQube Server installation sends telemetry data to Sonar daily. This data helps us understand how SonarQube Server is used, which in turn helps us improve our products.

### No personally identifiable information is sent. <a href="#no-personally-identifiable-information-is-sent" id="no-personally-identifiable-information-is-sent"></a>

The telemetry feature only sends anonymized, non-project-specific data related to which features of the product are being used.

Personal data, such as usernames or email addresses, is never sent. Neither is source code nor any project-specific data such as project name, repository, or author is ever sent. No IP addresses are ever sent.

The data is sent securely, held under restricted access, and not published outside of Sonar.

Protecting your privacy is important to us. If you have any concerns about telemetry data collection, please email us at `security@sonarsource.com`.

### What information is sent? <a href="#what-information-is-sent" id="what-information-is-sent"></a>

Every 24 hours, SonarQube Server sends a JSON payload and selected measure payloads to:

* `https://telemetry.sonarsource.com/sonarqube`
* `https://telemetry.sonarsource.com/sonarqube/metrics`

The data consists of anonymized information about:

* The SonarQube Server instance: version, license type, edition, database type, cloud usage and other information about the instance.
* Each project on the instance:
  * A technical identifier that does not reveal any project-specific details.
  * Project characteristics such as last analysis time, number of findings, and new code definition.
* Each user on the instance:
  * A technical identifier that does not reveal any personal information about the user.
  * Instance usage information, like last activity time and current status.
* Each quality gate on the instance:
  * A technical identifier that does not reveal any project-specific details.
  * A quality gate compliance status.
  * Quality gate conditions.
* Each quality profile of the instance:
  * A technical identifier that does not reveal any project-specific details.
  * Quality profile characteristics such as language, if the default Sonar way quality profile is used or if the parent of the quality profile is Sonar way.
  * Number of rules that are activated, deactivated, or overridden in the quality profile.
* Each branch on the instance:
  * A technical identifier that does not reveal any branch-specific details.
  * Branch characteristics, like its new code definition.

In addition to the payload, SonarQube Server also sends measures consisting of anonymized information about the usage of SonarQube Server for future product improvements. For example: the number of lines per language, AI code detection, installation data, user active status, and other anonymized data.

### Turning telemetry off <a href="#turning-it-off" id="turning-it-off"></a>

You can disable telemetry at any time by setting the `sonar.telemetry.enable = false` in `<sonarqubeHome>conf/sonar.properties`. By default, it is set to `true`.

#### Telemetry from SonarScanners

SonarScanners gather and transmit telemetry data to SonarQube Server. This data is then relayed to Sonar, but only if telemetry is enabled. SonarScanners do not send telemetry directly to Sonar, and there are no scanner-specific settings to enable or disable it.

\\
