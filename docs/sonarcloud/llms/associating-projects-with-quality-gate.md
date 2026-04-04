# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/associating-projects-with-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate.md

# Associating a quality gate with projects

The default quality gate is associated with all projects in the organization that are not explicitly associated with a quality gate. You can explicitly associate a project with a quality gate:

* At the quality gate level with the Administer Quality Gates permission. The procedure is explained below.
* At the project level with the Administer Quality Gates permission or the Administer Project permission. See the [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention") page.

### Last setting overrides principle without a hierarchy <a href="#last-setting-overrides-without-hierarchy" id="last-setting-overrides-without-hierarchy"></a>

The "last setting overrides" principle applies without a hierarchy: the most recently configured setting will take precedence over all previous settings. For example:

1. From the **Quality Gates** page, you first associate quality gate 1 with project 1.
2. Still from the **Quality Gates** page, you associate quality gate 2 with project 1. Project 1 is now associated with quality gate 2.
3. From project 1’s settings, you associate project 1 with quality gate 3. Project 1 is now associated with quality gate 3 (the setting is updated in the **Quality Gates** page).
4. From the **Quality Gates** page, you associate quality gate 1 with project 1. Project 1 is now associated with quality gate 1 (the setting is updated in project 1’s settings).

{% hint style="warning" %}
To avoid misconfigurations, we recommend that in your instance, you perform explicit associations either from the **Quality Gates** page or from the project settings, but not from both.
{% endhint %}

### Associating (or disassociating) a quality gate with (from) projects <a href="#associating-quality-gate-with-projects" id="associating-quality-gate-with-projects"></a>

1. In the top navigation bar, select **Quality Gates**.
2. In the left panel, select the quality gate you want to manage.
3. In the right panel’s **Projects** section, select the **With** (to view only the associated projects), **Without** (to view only the not associated projects) or **All** tab.
4. Select or unselect the projects you want to associate or disassociate with / from the quality gate.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-3dd262e466884b534960b94e109a4ff73a414eed%2F47afad3dfa83da75a13eb3bf762189bd27b98c5e.png?alt=media" alt="Navigate to your quality gate in SonarQube Cloud to see (and manage) a list of projects that use that quality gate."><figcaption></figcaption></figure></div>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention")
* [viewing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/viewing-quality-gate "mention")
* [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates "mention")
* [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/changing-default-quality-gate "mention")
* [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention")
* [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention")
* [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention")
