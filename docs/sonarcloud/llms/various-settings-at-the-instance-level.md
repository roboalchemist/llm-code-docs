# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/various-settings-at-the-instance-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/various-settings-at-the-instance-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/various-settings-at-the-instance-level.md

# Various settings at the instance level

### Changing the default issue assignee at the instance level <a href="#changing-default-issue-assignee" id="changing-default-issue-assignee"></a>

When new issues are created during analysis, they are assigned to the last committer where the issue was raised. When it is not possible to identify the last committer, issues can be assigned to a default assignee if set at the global or project level. To set the default assigned for your instance (the project-level setting has precedence over the instance-level setting):

1. Go to **Administration > Configuration > General Setting > General > Issues.**
2. In **Default Assignee**, enter the user account.
3. Select **Save**.

### Related pages

* [#changing-default-issue-assignee](https://docs.sonarsource.com/sonarqube-server/project-administration/setting-up-features/project-settings#changing-default-issue-assignee "mention")
