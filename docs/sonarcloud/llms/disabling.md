# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/gitlab/disabling.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/disabling.md

# Disabling authentication

### Disabling the GitLab configuration <a href="#disabling-config" id="disabling-config"></a>

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. If the automatic provisioning mode is enabled, disable it as follows:
3. In the **Provisioning** section, select the **Just-in-time user provisioning** option.
4. Select the **Save** button.
5. Select **Disable configuration**.
6. You can delete the configuration by selecting the **Delete** button. In that case, you won’t be able to re-enable this configuration.

### Re-enabling the GitLab configuration <a href="#reenable-config" id="reenable-config"></a>

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. Select **Enable configuration**.
3. If you had configured the automatic provisioning mode, select the **Automatic user, group, and permission provisioning** option. Your previous settings are kept.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [just-in-time](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/just-in-time "mention")
* [automatic](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic "mention")
* [setting-up](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/setting-up "mention")
