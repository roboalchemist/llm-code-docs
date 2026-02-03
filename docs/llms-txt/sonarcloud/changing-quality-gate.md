# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/changing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/changing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/changing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/changing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/changing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/changing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate.md

# Quality gate

The organization’s default quality gate is applied by default to your project. As a project administrator, you can apply other standards to your project. In addition, you can change the fudge factor used for quality gate computation for your project.

### Changing the quality gate applied to your project <a href="#quality-gate" id="quality-gate"></a>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left navigation bar, select **Administration** > **Quality Gate**.
3. Select **Use a specific quality gate**, and select the quality gate in the list.
4. Select **Save**.

### Changing the quality gate fudge factor of your project <a href="#quality-gate-fudge-factor" id="quality-gate-fudge-factor"></a>

The quality gate fudge factor refers to a mechanism where conditions on duplication and coverage are ignored until the number of new lines is at least 20. This is used to avoid overly strict enforcement when dealing with small changes, as minor issues might disproportionately impact the overall quality gate status.

The fudge factor is enabled by default in your organization. This organization’s setting is applied to all new projects. Project administrators can override it for their project.

To enable or disable the fudge factor for your project:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left navigation bar, select **Administration** > **Quality Gate**.
3. Unselect or select **Ignore duplication and coverage on small changes**.
4. Select **Save**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention")
* [viewing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/viewing-quality-gate "mention")
* [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates "mention")
* [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/changing-default-quality-gate "mention")
* [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate "mention")
* [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention")
* [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention")
* [quality-standards](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/quality-standards "mention")
