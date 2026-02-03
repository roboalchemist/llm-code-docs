# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/incremental-analysis/disabling-or-changing.md

# Disabling or changing the mechanisms

In very particular cases, you may need to disable or change the incremental analysis mechanisms.

### Disabling the Skip unchanged files mechanism <a href="#disable-skip-unchanged" id="disable-skip-unchanged"></a>

You can disable the Skip unchanged files mechanisms used by the Kotlin and Java analyzers by setting the `sonar.kotlin.skipUnchanged` or the `sonar.java.skipUnchanged` to `false`.

### Disabling the analysis cache mechanism <a href="#disable-analysis-cache" id="disable-analysis-cache"></a>

In particular cases, you may need to disable the analysis cache mechanism.

The analysis cache mechanism is enabled by default. If you disable it, the analyzer will analyze all files from scratch.

To disable the analysis cache mechanism, add the following parameter to your analysis (See [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/analysis-parameters "mention") for information about the setup of analysis parameters for the scanner.):

`sonar.analysisCache.enabled=false`

{% hint style="info" %}
The parameter `sonar.analysisCache.enabled` is not compatible with SonarScanner for .NET.
{% endhint %}

### Using the local filesystem for analysis caching <a href="#configure-filesystem-cache" id="configure-filesystem-cache"></a>

With the C/C++/Objective-C analyzer, you can configure the filesystem cache instead of using the analysis cache on the server. See also [customizing-the-analysis](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/customizing-the-analysis "mention") and [Analysis cache mechanism](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/introduction#analysis-cache).

### Related pages

* [introduction](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/incremental-analysis/introduction "mention")
