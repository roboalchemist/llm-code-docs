# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/server-base-url.md

# Server base URL

You must configure your base URL in the SonarQube Server. Otherwise, integration and authentication features will not work correctly, the URLs generated in reports and emails will be wrong, etc.

{% hint style="warning" %}
If you want to delegate the SonarQube Server user authentication to an OAUTH provider (GitHub, Bitbucket, GitLab, SAML), you should use HTTPS for security reasons. This means that the SonarQube Server instance should be secured behind a proxy (see [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")).
{% endhint %}

{% hint style="info" %}
The SonarQube base URL needs to be a public URL if SonarQube expects to receive information from an external system. This is basically only relevant if you use SCIM (since it requires SonarQube to be reachable by the Identity Provider).
{% endhint %}

To configure the server base URL in SonarQube Server:

1. Go to **Administration** > **Configuration** > **General Settings** > **General** > **General.**
2. In **Server base URL**, set your SonarQube Server instance’s URL.
