# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-gates/changing-default-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/quality-standards-administration/managing-quality-gates/changing-default-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-gates/changing-default-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-gates/changing-default-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-gates/changing-default-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-gates/changing-default-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/changing-default-quality-gate.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/changing-default-quality-gate.md

# Changing default quality gate

A default quality gate is defined in your organization: any project that is not explicitly associated with a quality gate, is associated with its organization’s default quality gate. The default quality gate is indicated in the UI with the `DEFAULT` tag.

By default, the default quality gate is the built-in quality gate **Sonar way**. You can set any built-in or custom quality gate as the default quality gate. Check the [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention") page for instructions.

{% hint style="info" %}
If you set as default a quality gate that is explicitly associated with projects, the explicit association is not shown anymore in the UI but is not removed: if you change again the default quality gate, the explicit association will show up again.
{% endhint %}

To change the default quality gate:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. In the organization’s navigation bar, select **Quality Gates**.
3. In the left panel, select the quality gate you want to set as default.
4. In the top right corner of the quality gate, select the Actions button, then select **Set as default**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-518db43697f37d76ce18b452a5954a1ce3052d90%2Ffbd16b3c4401213b3c552d1d352e8074b6f21215.png?alt=media" alt="Any quality gate can be selected as your DEFAULT quality gate in SonarQube Cloud. Simply navigate to the three-dot menu of your quality gate and select Set as Default."><figcaption></figcaption></figure></div>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention")
* [viewing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/viewing-quality-gate "mention")
* [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates "mention")
* [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate "mention")
* [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention")
* [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention")
* [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention")
