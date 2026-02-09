# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-gates/viewing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/quality-standards-administration/managing-quality-gates/viewing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-gates/viewing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-gates/viewing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-gates/viewing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-gates/viewing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/viewing-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/viewing-quality-gate.md

# Viewing a quality gate

Any user, even an ananymous user, can view the quality gates defined in a SonarQube Cloud instance. For information about quality gates, see [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention").

To view the definition of a quality gate:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. In the organization’s navigation bar, select **Quality Gates**.
3. In the left panel, select the quality gate you want to view. Its definition is displayed in the right panel. For information about the metrics used in the conditions, see the [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention") page.
4. To view the projects explicitly associated with this quality gate, navigate down to **Projects** in the right panel (Note that projects cannot be explicitly associated with the default quality gate). The **With** tab lists the associated projects. The **Without** tab lists the projects not associated with this quality gate. The **All** tab shows all projects.

The figure below shows the **Quality Gates** page:

1. The list of quality gates in your organization. Icons are used to indicate if a quality gate is qualified for Clean as You Code and/or AI Code Assurance.
2. The definition of the selected quality gate.
3. The projects associated with the selected project.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-099a828a8bf98911fc359182bf3cbb3c3c0bffc9%2Fc75eb5ccb74b7f427c9094f33a0379c7e9166e9f.png?alt=media" alt="Your SonarQube Cloud Quality Gates page shows you the conditions you&#x27;ve applied and the projects which use this particular quality gate when running analyses."><figcaption></figcaption></figure></div>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention")
* [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates "mention")
* [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/changing-default-quality-gate "mention")
* [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate "mention")
* [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention")
* [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention")
* [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention")
