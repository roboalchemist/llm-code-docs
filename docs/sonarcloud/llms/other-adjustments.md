# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/other-adjustments.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/other-adjustments.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/other-adjustments.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/other-adjustments.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/other-adjustments.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/other-adjustments.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/other-adjustments.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/other-adjustments.md

# Other analysis scope adjustments

See [overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/overview "mention") page for language-specific properties related to analysis scope adjustment.

### Adjusting the secret detection scope <a href="#secret-detection-scope" id="secret-detection-scope"></a>

By default, SonarQube Cloud detects exposed secrets in all files processed by the language analyzers. You can refine the scope of the secret detection, see [secrets](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/secrets "mention") for more details.

### Excluding files over a certain size <a href="#excluding-files-over-certain-size" id="excluding-files-over-certain-size"></a>

You can set the `sonar.filesize.limit` and `sonar.javascript.maxFileSize` properties on the CI/CD host to exclude files over a certain limit. For more information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").

### Disabling the SCM’s file ignore patterns <a href="#disabling-scm-file-ignore" id="disabling-scm-file-ignore"></a>

Your SonarQube analysis will automatically exclude files that are ignored by your source code control system. For example, in git repositories, it respects the `.gitignore` file. SonarQube also respects the ignore directives used in SVN repositories.

You can disable this behavior by setting the sonar property `sonar.scm.exclusions.disabled` to `true` on the CI/CD host. For more information, see [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-initial-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope "mention")
* [exclude-from-coverage-duplication](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/exclude-from-coverage-duplication "mention")
* [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention")
* [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention")
* [verifying-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/verifying-analysis-scope "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/introduction "mention") to Adjusting the analysis scope at the organization level
