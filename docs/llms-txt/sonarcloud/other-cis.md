# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/other-cis.md

# Other CIs

To run an analysis on a CI provider other than those with specific integrations:

1. Integrate the SonarScanner analysis into your build pipeline as explained in the corresponding scanner section:
   * [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet "mention")
   * [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention"),
   * [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention")
   * [sonarscanner-for-npm](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-npm "mention")
2. If necessary, adjust the [setting-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope "mention") or customize other default [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention").
3. Start and test the analysis.
4. Add the branch analysis or pull request analysis to your pipeline. See the [branch-analysis-setup](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis-setup "mention") and [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention") pages for more information.

Here is an example of a configuration for pull requests in a CI job:

```properties
sonar.pullrequest.base=main
sonar.pullrequest.branch=feature/my-new-feature
sonar.pullrequest.key=5
```
