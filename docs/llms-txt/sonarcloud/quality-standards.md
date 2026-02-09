# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/analysis-functions/quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/analysis-functions/quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/analysis-functions/quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/analysis-functions/quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/analysis-functions/quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/analysis-functions/quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/quality-standards.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/quality-standards.md

# Managing quality standards

This page explains how to configure organization settings related to quality gates or quality profiles and requiring the Administer organization permission.

To manage the quality gates in your organization, see [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention").

To manage the quality profiles in your organization, see [introduction](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/introduction "mention").

### Configuring the quality gate fudge factor of your organization <a href="#quality-gate-fudge-factor" id="quality-gate-fudge-factor"></a>

The quality gate fudge factor refers to a mechanism where conditions on duplication and coverage are ignored until the number of new lines is at least 20. This is used to avoid overly strict enforcement when dealing with small changes, as minor issues might disproportionately impact the overall quality gate status.

The fudge factor is enabled by default in your organization. This organization’s setting is applied to all new projects. Project administrators can override it for their project.

To enable or disable the quality gate fudge factor of your organization:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Administration** > **Quality gate settings**.
3. Select or unselect **Ignore duplication and coverage on small changes**.
4. Select **Save**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention")
* [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention")
* [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention")
