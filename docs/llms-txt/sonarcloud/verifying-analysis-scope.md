# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/verifying-analysis-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/verifying-analysis-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/verifying-analysis-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/verifying-analysis-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/verifying-analysis-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/verifying-analysis-scope.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/verifying-analysis-scope.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/verifying-analysis-scope.md

# Verifying analysis scope

This section explains how to verify the configured properties and the properties read by the scanner to compute the project's analysis scope. See [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/introduction "mention") to Setting analysis scope for more information.

### Verifying the analysis scope properties configured for the project <a href="#configured-project-properties" id="configured-project-properties"></a>

This procedure lets you view the properties configured in the different possible locations on the CI/CD host and in SonarQube Cloud UI for a given analysis run.

To verify the configured analysis properties for a project:

1. Run the project analysis.
2. The analysis debug logs show which source and test files are indexed for the analysis (the scanner logs out to the place it was invoked from).\
   If the analysis fails with the error `File <fileName> can't be indexed twice. Please check that inclusion/exclusion patterns produce disjoint sets for main and test files` then it means that the indicated file is defined in your analysis scope as both source (main) and test file. In this case, you must correct your analysis scope.
3. You can also verify all the project’s exclusion parameters. To do so, proceed as follows:
   1. Retrieve the project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for details.
   2. Go to *Your Project* > **Administration** > **Background Tasks**.
   3. In the list, locate the project run you want to verify and click the three-dot menu in the far right column.
   4. In the contextual menu, select **Show SonarScanner Context**. The scanner context is shown:
      * The **Organization server settings** section (supported only with the Enterprise plan) shows the analysis parameters set in the UI for the organization.
      * The **Project server settings** section shows the analysis parameters set in the UI for the project.
      * The **Project scanner properties** section shows the analysis parameters set on the CI/CD host for the project.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-65d3947cde3a09d0db840b6f87cef3ba243d55ff%2F312c95fc65d87c8fff49fdad539aac9edae914d6.png?alt=media" alt="You can access the SonarScanner Context report from the Background tasks page. Here, you can find all of the properties you&#x27;ve defined for that SonarQube Cloud project." width="563"><figcaption></figcaption></figure></div>

{% hint style="warning" %}
Any property set on the CI/CD host and identified by the scanner as a sonar property (that means, with a key starting with `sonar.`) will be listed as a scanner property even if the scanner does not know about it (in that case, the scanner will just ignore the property, and no error will be raised).
{% endhint %}

### Verifying the analysis scope properties read by the scanner <a href="#properties-read-by-scanner" id="properties-read-by-scanner"></a>

To know which properties the scanner processes during the analysis run:

* In analysis debug logs, search for the `Project configuration` section as illustrated below (The scanner logs out to the place it was invoked from). The section may show:
  * `Excluded sources`: exclusion patterns processed by the scanner to compute the source files to be analyzed.
  * `Included sources`**:** inclusion patterns processed by the scanner to compute the source files to be analyzed.
  * `Excluded tests`: exclusion patterns processed by the scanner to compute the test files to be analyzed.
  * `Included tests`**:** inclusion patterns processed by the scanner to compute the test files to be analyzed.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-3b377659ded835d706aa874174298cb5d6aed1ec%2F0b547257f0e221cb0d1e3a150eb89d6e92ea5914.png?alt=media" alt="Your SonarQube Cloud project&#x27;s source and test files can be examined in the INFO logs produced by the SonarScanner." width="513"><figcaption></figcaption></figure></div>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-initial-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope "mention")
* [exclude-from-coverage-duplication](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/exclude-from-coverage-duplication "mention")
* [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention")
* [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention")
* [advanced-exclusions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/advanced-exclusions "mention")
* [other-adjustments](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/other-adjustments "mention")
