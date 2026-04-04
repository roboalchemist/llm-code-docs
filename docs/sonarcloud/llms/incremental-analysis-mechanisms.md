# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/incremental-analysis-mechanisms.md

# Incremental analysis mechanisms

Incremental analysis may be used to shorten the [main-branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/main-branch-analysis "mention"), the [branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis "mention"), and the [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention").

Different mechanisms may be used:

* Unchanged files are skipped from the analysis for files that can be processed independently by the analyzer.
* The analysis cache mechanism allows reusing previous analysis results.

This section explains both mechanisms.

### Skip unchanged files mechanism <a href="#skip-unchanged-files" id="skip-unchanged-files"></a>

This mechanism is used for pull request analyses. With this mechanism, the analysis of (particular) unchanged files (compared to the target branch) is either skipped or optimized:

* For languages like CSS, HTML, XML, Apex, Go, Ruby, and Scala, where all files can be analyzed independently, the scanner only supplies modified files to the analyzer. This means that only the changed files are analyzed.
* For languages like Kotlin, Java, JavaScript, C#, and VB.NET, the analyzer either skips particular unchanged files or optimizes the analysis of these files. For more information, see the respective language section in this documentation.

### Analysis cache mechanism <a href="#analysis-cache" id="analysis-cache"></a>

With the analysis cache mechanism, the metadata of a branch analysis is cached on the server side at the end of the analysis. This way, this data is available to the analyzers for future analysis.

The analysis cache mechanism is supported for the following languages:

* To shorten a branch analysis: C, C++, Objective-C, and COBOL. For the other languages, the branch cache is still downloaded to be updated with the newest state of the branch, and then re-uploaded to the server.
* To shorten a pull request analysis: C, C++, Objective-C, Java, JavaScript, C#, VB.NET, TypeScript, Kotlin, PHP, and Python.

#### Caching process <a href="#caching-process" id="caching-process"></a>

The server manages a single analysis cache for each branch, which corresponds to the latest analysis.

The caching process is as follows:

1. Before an analysis, the SonarScanner downloads from the server the corresponding cache:
   * For a long-lived branch analysis, the cache of the long-lived branch.
   * For a short-lived branch analysis:
     * If available, the cache of the short-lived branch.
     * Otherwise, the cache of the target branch.
   * For a pull request, the cache of the target branch.
   * Or, as a fallback, the cache of the main branch.
2. During the analysis, the analyzers can access the cache locally to read and/or write to the cache.
3. At the end of the analysis:
   * For a branch analysis: the SonarScanner uploads the new cache of the branch to the server (overwriting the existing one).
   * For a pull request analysis: the SonarScanner doesn’t upload the cache of the pull request branch (the cache is not persisted).

<figure><img src="broken-reference" alt="How incremental analysis works in SonarQube."><figcaption></figcaption></figure>

Note that:

* If the SonarScanner for .NET is used, the scanner version 5.12 or higher is required.
* With the C/C++/Objective-C analyzer you can also configure the change of the cache storage to the local filesystem. However, this configuration should be used only in very specific use cases.

#### Analysis optimization <a href="#analysis-optimization" id="analysis-optimization"></a>

The way the analyzer optimizes the analysis based on the cached data depends on the language. For most analyzers, the optimization will be similar to the optimization done by the C/C++/Objective-C analyzer described below. The optimization done by the Kotlin analyzer is different.

<details>

<summary>C/C++/Objective-C</summary>

During a branch analysis, the C/C++/Objective-C analyzer analyzes only the code sections that are affected by the changes in the branch compared to the previous branch analysis.

During a pull request analysis, the analyzer analyzes only the code sections that are affected by the changes compared to the target branch.

To decide whether a code section is affected by the changes, the analyzer queries the loaded cache for information. It checks if the cached analysis results can be reused (cache hit). To do so, it checks various conditions such as cross-file dependencies, quality profile setting changes, build setting changes, etc. :

* If there is a cache hit, the analyzer leverages the previously stored analysis results, and thus, saves time.
* Otherwise, the analyzer performs a new analysis of the concerned code.

</details>

<details>

<summary>Kotlin</summary>

During a branch analysis, the Kotlin analyzer stores the copy-paste duplication (CPD) tokens to provide accurate duplication information on pull requests.

During a pull request analysis, the analyzer re-uses the CPD tokens cached during the last target branch analysis for files that have not changed compared to the target branch.

</details>

### Disabling the Skip unchanged files mechanism <a href="#disable-skip-unchanged" id="disable-skip-unchanged"></a>

You can disable the Skip unchanged files mechanism used by the Kotlin and Java analyzers by setting the `sonar.kotlin.skipUnchanged` or the `sonar.java.skipUnchanged` to `false`.

### Disabling the analysis cache mechanism <a href="#disable-analysis-cache" id="disable-analysis-cache"></a>

In particular cases, you may need to disable the analysis cache mechanism.

The analysis cache mechanism is enabled by default. If you disable it, the analyzer will analyze all files from scratch.

To disable the analysis cache mechanism:

1. In the SonarQube Cloud UI, retrieve your project.
2. In the left navigation bar of your project, select **Administration > General Settings**.
3. In **Sensor cache**, disable the **Sensor cache for project** option (`sonar.sensor.cache.project.enable` property).

### Using the local filesystem for analysis caching <a href="#configure-filesystem-cache" id="configure-filesystem-cache"></a>

With the C/C++/Objective-C analyzer, you can configure the filesystem cache instead of using the analysis cache on the server. You should use this configuration only in very specific use cases. See the article on [#analysis-cache](https://docs.sonarsource.com/sonarqube-cloud/languages/c-family/customizing-the-analysis#analysis-cache "mention") article on the [customizing-the-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/customizing-the-analysis "mention") page for more details.
