# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/http-header.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/http-header.md

# HTTP header

You can delegate user authentication to third-party systems (proxies/servers) using HTTP header authentication.

When this feature is activated, SonarQube Server expects that the authentication is handled prior to any query reaching the server. The tool that handles the authentication should:

* Intercept calls to the SonarQube Server.
* Take care of the authentication.
* Update the HTTP request header with the relevant SonarQube Server user information.
* Re-route the request to SonarQube Server with the appropriate header information.

<figure><img src="broken-reference" alt="HTTP header authentication mechanism"><figcaption></figcaption></figure>

All the parameters required to activate and configure this feature are available in SonarQube Server configuration file. See the `SSO AUTHENTICATION` section in `<sonarqubeHome>/conf/sonar.properties`.

Using HTTP header authentication is an easy way to integrate your SonarQube Server deployment with an in-house SSO implementation.
