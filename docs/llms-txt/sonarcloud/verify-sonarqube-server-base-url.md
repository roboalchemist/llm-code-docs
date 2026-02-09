# Source: https://docs.sonarsource.com/sonarqube-server/10.6/devops-platform-integration/github-integration/setting-up-at-global-level/verify-sonarqube-server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/devops-platform-integration/github-integration/setting-up-at-global-level/verify-sonarqube-server-base-url.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/devops-platform-integration/github-integration/setting-up-at-global-level/verify-sonarqube-server-base-url.md

# Verifying the server base URL

If you want to delegate the SonarQube Server user authentication to GitHub: you must use HTTPS. This means that the SonarQube Server instance must be [#securing-the-server-behind-a-proxy](https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/operating-the-server#securing-the-server-behind-a-proxy "mention").

You must configure your SonarQube Server base URL in SonarQube Server, otherwise, integration features will not work correctly.

To verify the server base URL configuration in SonarQube Server:

* Go to **Administration** > **Configuration** > **General Settings** > **General** > **General** and check the instance’s **Server base URL**.
