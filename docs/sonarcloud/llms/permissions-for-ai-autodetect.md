# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/ai-features/permissions-for-ai-autodetect.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/ai-features/permissions-for-ai-autodetect.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/ai-features/permissions-for-ai-autodetect.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/ai-features/permissions-for-ai-autodetect.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/ai-features/permissions-for-ai-autodetect.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/ai-features/permissions-for-ai-autodetect.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/permissions-for-ai-autodetect.md

# Permissions for AI Autodetect

To activate AI Code Autodetection, a SonarQube Cloud Organization Administrator must first check that the feature is enabled.

Then, a DevOps platform administrator must set the correct permission level in your AI-powered web service. For specific instructions in your DevOps platform, please refer to the applicable section below.

### GitHub Copilot Business <a href="#github-copilot-business" id="github-copilot-business"></a>

When a SonarCloud administrator activates AI Code Autodetection (see the [autodetect-ai-code](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/autodetect-ai-code "mention") page) for a SonarCloud organization, GitHub Copilot Business app administrators will receive an email notification to review the SonarCloud App’s permission request. The App administrator should review the request and accept the **Read-only** access to GitHub Copilot Business.

With access to your GitHub Copilot Business App, SonarQube Cloud can evaluate users’ GitHub Copilot usage and code contribution patterns to identify potential AI-generated code. If there is a match in user data, SonarQube Cloud will display the ![$ai-icon-sparkle](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-975a17de7ce8ae3b164dd9f9db9c791adb294bbb%2F4be9087a2b059c269f15df202838af7a74e71a96.svg?alt=media)**AI code detected** status on the project’s Overview and Project Information pages.

SonarQube Cloud does not retroactively check older code from previous commits. In addition, projects that have the ![$contains-ai-code](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ca3b9de37a93a3d09c496b45878e418adab02c9f%2Fc151514ef7beca0f865ee429bc9fe0e33b05ceb4.svg?alt=media) label applied by a quality standards administrator will be excluded from automatic AI code detection. See the [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview#label-projects-with-ai-code "mention") article to learn more.

{% hint style="warning" %}
If the GitHub Copilot Business and Enterprise account administrator chooses to ignore the request, Sonar’s AI Code Autodetection will be turned on, but not be activated.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* SonarQube Cloud's [ai-capabilities](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities "mention")
* Use [ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-codefix "mention") to get AI-generated fix suggestions
* To learn about AI Code Assurance:
  * [overview](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview "mention") for AI-generated code
  * [#marking-a-project-as-containing-ai-generated-code](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-code-assurance#marking-a-project-as-containing-ai-generated-code "mention")
  * and learn how to use [quality-gates-for-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-gates-for-ai-code "mention")
