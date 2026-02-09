# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/gitlab/setting-up.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/setting-up.md

# Setting up authentication

You can delegate in SonarQube Server the authentication to GitLab by using one of the following provisioning modes:

* Just-in-Time
* Automatic

You need the global Administer System permission in SonarQube Server to set up the authentication delegation.

{% hint style="info" %}
When you set up GitLab authentication and provisioning, existing manual users are not removed and you cannot edit their group membership or permissions anymore. For security reasons, we recommend that you deactivate them: see [deactivating-users](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/deactivating-users "mention").
{% endhint %}

### Setup overview <a href="#overview" id="overview"></a>

SonarQube Server uses a GitLab OAuth 2 application to manage the authentication delegation to GitLab and the user or group synchronization. SonarQube Server uses a "GitLab Configuration" record to access the GitLab application.

<figure><img src="broken-reference" alt="SonarQube Server uses a GitLab OAuth 2 application to manage the authentication delegation to GitLab and the user or group synchronization. SonarQube Server uses a “GitLab Configuration” record to access the GitLab application."><figcaption></figcaption></figure>

### Step 1: Create a GitLab application for authentication and provisioning <a href="#create-gitlab-app" id="create-gitlab-app"></a>

1. Create a GitLab OAuth 2 application: see the [GitLab documentation](https://docs.gitlab.com/ee/integration/oauth_provider.html).
2. Specify the following settings in your GitLab application:
   * **Name**: Your app’s name, such as SonarQube Server.
   * **Redirect URI**: `<Your SonarQube Server URL>/oauth2/callback/gitlab`. For example, <https://sonarqube.mycompany.com/oauth2/callback/gitlab>.
   * **Scopes**: Select `api`if you plan to enable group synchronization with Just-in-Time or enable automatic provisioning. Select `read_user` otherwise.
3. Save your application. GitLab takes you to the application’s page, where you can find your Application ID and Secret you’ll need in Step 2 below.

### Step 2: Configure GitLab authentication and provisioning in SonarQube Server <a href="#configure-in-sq" id="configure-in-sq"></a>

1. In in SonarQube Server, go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. In **GitLab configuration**, select **Create configuration**. The New **GitLab Configuration** dialog opens.

<figure><img src="broken-reference" alt="Create a new GitLab configuration record in SonarQube"><figcaption></figcaption></figure>

3. Fill the fields of **GitLab configuration** with information from the GitLab application created in Step 1:
   * **Application ID**
   * **GitLab URL**: Enter `https://gitlab.com` or your own GitLab server URL where applicable.
   * **Secret**
4. Select the **Synchronize user groups** option if you want to enable group synchronization at user login:
   * In Just-in-Time provisioning mode, this means that group synchronization is enabled.
   * In automatic provisioning mode, this means that users’ group memberships are also synchronized at user authentication time (and not only on an hourly basis).
5. Select **Save configuration**. The configuration is created.

<figure><img src="broken-reference" alt="Create a new GitLab configuration record in SonarQube"><figcaption></figcaption></figure>

6. Select **Test configuration** to check the configuration. Correct it if necessary.
7. You can now enable the automatic provisioning option by selecting **Automatic user, group, and permission provisioning**. See [managing-automatic-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/managing-automatic-provisioning "mention") for more information.\
   If you don’t want to use the automatic provisioning option, you can configure JIT provisioning options in the **Provisioning** > **Just-in-Time provisioning** section, see [managing-jit-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/managing-jit-mode "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [just-in-time](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/just-in-time "mention")
* [automatic](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic "mention")
* [disabling](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/disabling "mention")
