# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/setting-new-code-definition-at-global-level.md

# New code definition

The global-level new code definition is called *baseline for new code*:

* It applies by default to all projects. A specific new code definition can be applied to the project instead.
* If it applies to a project, the project consistently uses the baseline for new code. Consequently, any modifications to the baseline will automatically be applied to the project.

The default baseline for new code is the Previous version option. With the Administer System permission, you can change it to the Number of days option, either in the UI or via the Web API.

For more information about the new code options, see [about-new-code](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code "mention").

### In the UI <a href="#in-the-ui" id="in-the-ui"></a>

1. In the top navigation bar, select **Administration** > **Configuration** > **General Settings** > **New Code**.
2. Select the new code option.
3. Select **Save**.

<figure><img src="broken-reference" alt="Set the new code definition by selecting a radio button corresponding to the new code option of your choice"><figcaption></figcaption></figure>

### Via the Web API <a href="#via-the-web-api" id="via-the-web-api"></a>

Use the [api/new\_code\_periods/set](https://next.sonarqube.com/sonarqube/web_api/api/new_code_periods/set) endpoint without specifying a branch or a project.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [about-new-code](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code "mention")
* [configuring-new-code-calculation](https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/configuring-new-code-calculation "mention")
