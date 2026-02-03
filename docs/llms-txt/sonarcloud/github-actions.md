# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/github-actions.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/github-actions.md

# GitHub Actions

The analysis is searches for workflows located in `**/.github/workflows/**` and composite actions in `**/actions.yml`.

### Language-specific properties <a href="#languagespecific-properties" id="languagespecific-properties"></a>

Discover and update the YAML properties in *Your Project* > **Administration** > **General Settings** > **Languages** > **GitHub Actions**.

### Deactivating GitHub Actions analysis <a href="#deactivating-github-actions-analysis" id="deactivating-github-actions-analysis"></a>

You can deactivate the analysis of GitHub Actions by setting the `sonar.githubactions.activate` property to `false`.
