# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/maintaining-project/changing-project-binding.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/changing-project-binding.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/maintaining-project/changing-project-binding.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/changing-project-binding.md

# Changing your project binding

You must be an administrator of your project.

### Unbinding or changing the binding of a bound project

1. Retrieve your project. For more information, see [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention").
2. Go to **Project Settings** > **General Settings** > **DevOps Platform Integration**.
3. In the bottom of the page, select **Reset**. The project is unbound.
4. To bind the project to another repository, see [#binding-an-unbound-project](#binding-an-unbound-project "mention") below.

### **Binding an unbound project**&#x20;

If you created your project manually and want to bind it to its DevOps platform repository to benefit the features of a bound project, proceed as follows:

1. Retrieve your project in SonarQube Server. For more information, see [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention")..
2. In front of the project name, select **Bind project**. The DevOps Platform Integration page opens.

<figure><img src="broken-reference" alt="Select Bind project in front of the project name to bind your unbound project."><figcaption></figcaption></figure>

3. In **Configuration name**, enter the Configuration record used to manage your DevOps platform integration at the global level. Ask your system administrator.&#x20;
4. This step depends on your DevOps platform:
   * GitHub: In **Repository name**, enter the name of the GitHub repository you want to bind.\
     You can enable the [analysis summary under the GitHub Conversation tab](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/in-devops-platform/github#pull-request-decoration).
   * Bitbucket Cloud: In **Repository slug**, enter the URL of the Bitbucket Cloud repository you want to bind.
   * GitLab:  In **Project ID**, enter the unique identifier of your GitLab project you want to bind.
   * Azure DevOps:&#x20;
     * In **Project name**, enter the name of the Azure DevOps project containing your repository.
     * In **Repository name**, enter the name of the Azure DevOps repository you want to bind.
     * By default, [pull request annotations](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/in-devops-platform/azure-devops#pull-request-decoration) are enabled. You can disable them.
5. Select **Save**. The new binding is saved.

<figure><img src="broken-reference" alt="Once you have saved your project binding configuration, select the Check configuration button."><figcaption></figcaption></figure>

6. Select **Check configuration**. SonarQube Server checks if the entered DevOps platform repository exists and you have access to it.

{% hint style="info" %}
The project binding (incl. the configuration check) is logged in the [audit logs](https://docs.sonarsource.com/sonarqube-server/instance-administration/security/audit-logs).
{% endhint %}
