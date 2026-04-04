# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/setting-up-features/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/setting-up-features/project-settings.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/setting-up-features/project-settings.md

# Setting various features at project level

Project administration is accessible through the **Project Settings** menu of each project. Only project administrators can access project’s settings.

### PDF reports <a href="#project-pdf-reports" id="project-pdf-reports"></a>

As a project administrator, you can change the PDF report subscription frequency of the project or application:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more details.
2. In the top right corner, select **Project Settings** > **General Settings** > **Governance**.
3. Under **Project and Application PDF Reports**, select an option from the **PDF Reports Frequency** drop-down menu.

You have the following options for subscription frequency:

* **Daily**
* **Weekly**
* **Monthly (default)**

{% hint style="info" %}
Users can only download or subscribe to a PDF report for a permanent branch. To set a branch as permanent, go to **Project Settings** > **Branches and Pull Requests** and make sure that the **Keep when inactive** toggle is on for that branch.
{% endhint %}

### Changing your project's default issue assignee <a href="#changing-default-issue-assignee" id="changing-default-issue-assignee"></a>

When new issues are created during analysis, they are assigned to the last committer where the issue was raised. When it is not possible to identify the last committer, issues can be assigned to a default assignee if set at the global or project level. To set the default assigned for your project (this setting has precedence over the global-level setting):

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more details.
2. In the top right corner, select **Project Settings** > **General Settings > General**.
3. In **Issues > Default Assignee**, enter the user account.

### Related pages

* [pdf-reports](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/pdf-reports "mention") (setup at the instance level)
* [#changing-default-issue-assignee](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/various-settings-at-the-instance-level#changing-default-issue-assignee "mention")
