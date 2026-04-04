# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/setting-long-lived-branch-pattern.md

# Setting long-lived branch pattern

This feature is only available in the [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

As an organization admin, you can set the long-lived branch name pattern at the organization level provided you have an Enterprise plan organization. The organization-level patter applies by default to all projects. If the project admin sets a custom pattern for their project, this pattern overrides the organization’s pattern. See [long-lived-branch-pattern](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/long-lived-branch-pattern "mention") for more information.

### Introduction to the long-lived branches name pattern <a href="#introduction" id="introduction"></a>

SonarQube Cloud considers a branch to be long-lived if:

* It is the main branch, or
* Its name matches the long-lived branch name pattern.

All other branches are considered short-lived.

{% hint style="info" %}
The type of a branch (long-lived or short-lived) is set during its first analysis and cannot be changed afterward.
{% endhint %}

The name pattern is based on a regular expression. For example, the regular expression *`(branch|release)-.*`* matches any branch name that begins with the string `branch-` or `release-`.

If you don’t set any pattern at the organization level, the default pattern *`(branch|release)-.*`* applies.\* \*You can reset the organization pattern to this value.

### Setting a long-lived branches pattern for your organization <a href="#setting" id="setting"></a>

To set the long-lived branches pattern of your organization:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Organization settings.**
3. In **Branch** > **Long-lived branches detection**, enter your regular expression.
4. Select **Save**.

### Resetting the organization-level pattern to its default <a href="#reset-to-default" id="reset-to-default"></a>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Organization settings.**
3. In **Branch > Long-lived branches detection**, select reset. The pattern is reset to `(branch|release)-.*`.
