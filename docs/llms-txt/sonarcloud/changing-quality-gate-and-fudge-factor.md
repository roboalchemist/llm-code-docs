# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/changing-quality-gate-and-fudge-factor.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/changing-quality-gate-and-fudge-factor.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/changing-quality-gate-and-fudge-factor.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/changing-quality-gate-and-fudge-factor.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/changing-quality-gate-and-fudge-factor.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/changing-quality-gate-and-fudge-factor.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/changing-quality-gate-and-fudge-factor.md

# Managing your project's quality gate

### Changing the quality gate applied to your project <a href="#quality-gate" id="quality-gate"></a>

The instance’s default quality gate is applied by default to your project. As a project administrator, you can apply other standards to your project. To do so:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more details.
2. Select **Project Settings > Quality Gate**.
3. Select **Always use a specific Quality Gate**, and select the quality gate in the list.
4. Select **Save**.

### Setting up the Sandbox feature for your project

If your instance admin has enabled the Sandbox feature in your instance, you can switch it on or off for your project, and, if allowed by the instance admin, you can change the sandbox conditions. For more information about this feature, see [#sandboxing-of-issues-coming-from-sonarqube-update](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview#sandboxing-of-issues-coming-from-sonarqube-update "mention").

{% hint style="info" %}
If you switch off the Sandbox feature for your project, any existing sandboxed issues will remain in the Sandbox and can still be triaged by users.
{% endhint %}

#### Switching Sandbox on or off

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more details.
2. In the top right corner, select **Project Settings > General Settings > General**.
3. In **Sandbox specific issue categories after SonarQube update**, enable the Sandbox feature.
4. Select Save.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/GlC2W5NUy0k1sutIMDHk/sonarqube-server-switch-off-on-sandbox-for-your-project_Qs0142.png" alt="In the project Settings, switch on or off the sandbox feature for your project"><figcaption></figcaption></figure>

#### Changing the Sandbox conditions

If allowed by your instance admin, you can change the software quality and/or severity of issues moved to the Sandbox.

Proceed as follows:

1. Retrieve your project.
2. In the top right corner, select **Project Settings > General Settings > General**.
3. In **Sandbox specific issue categories after SonarQube update**, make sure the sandbox feature is enabled.
4. In **Choose software quality and severity of issues automatically moved to sandbox after SonarQube update**, change the software quality(ies) and/or severity(ies).
5. Select **Save**.
6. To reset the sandbox conditions to their default values, select **Reset To Default**.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/SzNTIRxikcDRYMOcwN1X/sonarqube-server-change-sandbox-conditions-for-your-project_Qs0141.png" alt=""><figcaption></figcaption></figure>

### Configuring the quality gate fudge factor <a href="#configuring-fudge-factor" id="configuring-fudge-factor"></a>

The quality gate fudge factor refers to a mechanism where conditions on duplication and coverage are ignored until the number of new lines is at least 20. This is used to avoid overly strict enforcement when dealing with small changes, as minor issues might disproportionately impact the overall quality gate status.

The fudge factor is enabled by default in your instance. This global setting is applied to all new projects. Project administrators can override it for their project.

You can enable the fudge factor in the UI as explained below, or by setting the `sonar.qualitygate.ignoreSmallChanges` property to `false` or `true` on the CI/CD host (see [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention")).

To enable or disable the quality gate fudge factor in the UI for your project:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more details.
2. Select **Project Settings > General Settings > General**.
3. In the **Quality gate** section, unselect or select **Ignore duplication and coverage on small changes**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates "mention")
* [viewing-quality-gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/viewing-quality-gate "mention")
* [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/managing-custom-quality-gates "mention")
* [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/changing-default-quality-gate "mention")
* [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate "mention")
* [subscribing-to-notifications](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-your-account/subscribing-to-notifications "mention")
* [#sandboxing-of-issues-coming-from-sonarqube-update](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/solution-overview#sandboxing-of-issues-coming-from-sonarqube-update "mention")
