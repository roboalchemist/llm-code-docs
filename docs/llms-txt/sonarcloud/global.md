# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/global.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/global.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/global.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/devops-platform-integration/bitbucket-integration/data-center/global.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/global.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/global.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-cloud-integration/global.md

# Source: https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/global.md

# Setting up Bitbucket Data Center integration at global level

This section explains how to set up Bitbucket Data Center and SonarQube to allow users to import Bitbucket Data Center repositories. To perform this setup, you need the global Administer System permission in SonarQube.

### Prerequisites

You’ve set a SonarQube Server base URL in SonarQube Server: see [server-base-url](https://docs.sonarsource.com/sonarqube-server/instance-administration/server-base-url "mention").

### Step 1: Create a Personal Access Token

You must provide a Bitbucket Data Center [Personal Access Token](https://confluence.atlassian.com/bitbucketserver0515/personal-access-tokens-961275199.html) that will be used by SonarQube to report the quality gate to the pull requests. This token will be stored in SonarQube and can be revoked at any time in Bitbucket Data Center.

To generate the token, we recommend using a dedicated Bitbucket Data Center account with Administrator permissions. In any case, the account must have the `Read` permission for the repositories that will be analyzed.

If you want to enter the token in SonarQube in encrypted format, you can encrypt this token.

See [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/encrypting-settings "mention") for more information about settings encryption.

### Step 2: Create a Bitbucket configuration record

This integration is performed through a "Bitbucker Configuration" record, which is used in SonarQube to access the Bitbucket Data Center instance.

{% hint style="info" %}
Starting in SonarQube Server's [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/), you can integrate SonarQube with multiple Bitbucket Data Center instances, each instance being accessed with a different Bitbucket Configuration.
{% endhint %}

To set up a Bitbucket Configuration in SonarQube:

1. In the SonarQube UI, go to **Administration > Configuration > General Settings > DevOps Platform Integrations**.
2. Select the **Bitbucket** tab and click **Create configuration**. The **Create a configuration** dialog opens.
3. Select **Bitbucket Server**.

<figure><img src="broken-reference" alt="Select Bitbucket Server in the Create a configuration dialog."><figcaption></figcaption></figure>

4. Specify the following settings:
   * **Configuration Name** (Enterprise and Data Center edition only): The name used to identify your Bitbucket configuration at the project level. Use something succinct and easily recognizable.
   * **Bitbucket Server URL**: Your Server or Data Center instance URL. For example, `https://bitbucket-server.your-company.com`.
   * **Personal Access Token**: The token you generated in Step 1.
5. Select **Save configuration**.

### Related pages

[import-repos](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/import-repos "mention")\
[project](https://docs.sonarsource.com/sonarqube-server/devops-platform-integration/bitbucket-integration/bitbucket-server-integration/project "mention")
