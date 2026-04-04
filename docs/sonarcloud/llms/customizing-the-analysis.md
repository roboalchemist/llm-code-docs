# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/customizing-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/customizing-the-analysis.md

# Customizing the analysis

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

Discover and update the C/C++/Objective-C specific properties in the project settings. From the project homepage, go to **Administration** > **General Settings** > **Languages** > **C/C++/Objective-C** > **Automatic Analysis Settings**.

### Analyzing test files <a href="#analyzing-test-files" id="analyzing-test-files"></a>

The scanner property `sonar.tests` is used to pinpoint the directories that contain test source files. Recognizing these test files aids the analyzers in adjusting their rules accordingly. For instance, analyzers can activate rules specific to tests and deactivate those not applicable in a testing context.

Currently, the CFamily analyzer treats main and test source files identically. As a result, the `sonar.tests` scanner property is not supported at this time and is disregarded by the analyzer.

To analyze test source files, they should be incorporated into the `sonar.sources` scanner property. In that case, please note that the test code is considered part of the overall code and counts toward the license usage.​​

### Quality profiles <a href="#quality-profiles" id="quality-profiles"></a>

* Like all other languages supported by SonarQube Cloud, C, C++, and Objective-C come with the "Sonar way" profile. This is Sonar’s recommended quality profile, designed to fit most projects. To learn more, see the [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention") page.
* We also provide the "Mission critical" quality profile for C++. It is our recommendation for modern C++ development (C++17 and beyond) for mission-critical software. It is based on MISRA C++ 2023 and trades more constraints on your code for more code safety.

### Targeted C++ standard <a href="#targeted-cpp-standard" id="targeted-cpp-standard"></a>

The analyzer targets a specific version of the C++ language to tune the rules in the activated quality profile. This reporting standard is used to:

* Suppress rules that cannot be applied, such as rules that suggest using C++20 features while compiling the code with C++17.
* Adjust rules’ messages to suggest the proper fix according to the used standard. For example, a rule that suggests using `std::ranges::any_of` with C++20 will be tuned to suggest using `std::any_of` with an older standard.

In Compilation Database mode, the reporting standard defaults to the version used to compile the code. This is ideal for most projects. However, there are some edge cases where there is a need to use a reporting standard different from the compilation standard. For this reason, we provide the following scanner property to adjust the reporting standard:

```properties
sonar.cfamily.reportingCppStandardOverride=c++98|c++11|c++14|c++17|c++20|c++23
```

This property is only recommended for use in cases where a project has to comply with a standard older than the one it is compiled with. This can happen if:

* The compiler doesn’t allow setting a specific standard. For example, MSVC doesn’t allow specifying a standard older than C++14.
* The project wants to be compiled with the latest standard while still complying with an older one.

In Automatic Analysis mode, the reporting standard defaults to the latest version. In this case, we recommend setting the property if the project needs to comply with an older standard.

### C++20 Modules <a href="#cpp-20-modules" id="cpp-20-modules"></a>

Support for C++20 modules is currently experimental and not enabled by default.

* Since the analyzer is based on Clang 20, not all features of C++20 modules are supported. For more information, see the [official documentation for Clang](https://releases.llvm.org/20.1.0/tools/clang/docs/StandardCPlusPlusModules.html).
* Header units are not currently supported.
* The CFamily analyzer needs to know where to find the module units and how to build their corresponding Binary Module Interfaces (BMI). Hence, the Compilation Database must contain the necessary compiler calls for a complete clean build. This is also true for import std. Module units do not need to be indexed by Sonar unless you want them to be analyzed.
* Support for this feature is only available through the Sonar Community; commercial support is not currently available.
* When modules are involved, there may be some False Positives or Negatives. If you find any, [please report them via the Sonar Community](https://community.sonarsource.com/t/how-to-report-a-false-positive-false-negative/37022/1) or mark "*Share* *comment with Sonar to help improve our analyzers*" when flagging an issue as a False Positive in SonarQube Cloud.

Use the following scanner property to enable C++20 module support:

```properties
sonar.cfamily.enableModules=true
```

There are some aspects to keep in mind when analyzing code with C++20 modules:

* The property above will enable module support only for source files compiled with C++20 or later.
* Using modules requires building intermediate *BMIs*, which, by default, will be put under the directory configured by **`sonar.working.directory`** (usually, `.sonarscanner` under the project root directory). You must account for some extra space to store these files, which SonarScanner will remove at the end of the analysis.
* Analysis results and module dependencies are cached, but the intermediate BMIs are not. Hence, when re-analyzing a file, the analyzer will have to build its full tree of dependencies.

### Automatic Analysis specific properties <a href="#automatic-analysis-specific-properties" id="automatic-analysis-specific-properties"></a>

While Automatic Analysis mode automatically deduces the low-level configurations, optionally tuning some high-level configurations can be beneficial to force the analysis of specific project variants and improve its analysis quality. Those high-level configurations can be tuned through settings Automatic Analysis specific properties that fall into three categories: custom preprocessor, custom analysis target, and forcing a C++ language standard.

* Set a custom preprocessor to tune which parts of the code are analyzed and which features macros are enabled or disabled.
* Set custom targets to tune the size of types and inform the analyzer about the environment the project aims to run on. This can be especially useful for embedded projects with custom architecture.
* Override the default C++ language standard if the project needs to comply with a standard other than the latest.

You can find more on those settings and how to set them in the project administration settings. From the project homepage, go to **Project Settings** > **General Settings** > **Languages** > **C/C++/Objective-C** > **Automatic Analysis**.

While it is recommended and easier to set these properties from the UI, they can be set in `.sonarcloud.properties`, for example:

```properties
# Set a multiline custom preprocessor to disable C++ exceptions and define a `custom_macro` to 1
sonar.cfamily.customPreprocessor=#undef __cpp_exceptions\n#define custom_macro 1\n

# Set custom targets, possible values are listed in the UI
# This is equivalent to Clang command line argument: "-target aarch64-pc-linux-gnu"
sonar.cfamily.customTargetArch=aarch64
sonar.cfamily.customTargetVendor=pc
sonar.cfamily.customTargetSystem=linux
sonar.cfamily.customTargetEnv=gnu

# Override the default C++ language standard with c++14
sonar.cfamily.reportingCppStandardOverride=c++14
```

Note that you don’t need to worry about these properties by default. Different UI warnings are raised when the analysis quality is considered too low, suggesting providing the Automatic Analysis-specific properties or moving from Automatic Analysis to Compilation Database mode.

### Analysis cache <a href="#analysis-cache" id="analysis-cache"></a>

The C/C++/Objective-C analyzer uses the [#analysis-cache](https://docs.sonarsource.com/sonarqube-cloud/incremental-analysis-mechanisms#analysis-cache "mention") to perform incremental analysis.

Incremental analysis is activated by default and uses server cache storage. It’s possible to change the cache storage to the local file system.

You should consider changing the cache storage to the local filesystem when:

* The server cache size becomes a concern.
* You want to optimize the cache lifecycle based on your project workflow.\
  In particular, if you have long-living pull request branches, you may want to persist the cache for each pull request analysis.

With the filesystem cache, you define a path to the cache. The analyzer loads the cache provided in this directory at the beginning of the analysis and overwrites it at the end. Persisting this directory at the end of the analysis, and loading the cache of the most relevant analysis at the beginning becomes the responsibility of the CI configuration. For example, for the first analysis of a pull request branch, a good option is usually to load the target branch cache to the location of the pull request branch analysis cache.

{% hint style="warning" %}
Be aware that the setup of a filesystem cache is complicated since you must implement the cache lifecycle management logic in your CI configuration.
{% endhint %}

To configure the filesystem cache:

1. Set the `sonar.cfamily.analysisCache.mode` property to `fs` (filesystem) on your CI/CD host (the default value is `server` for server-side cache). See the corresponding SonarScanner section for more information about the setup methods.
2. To set the path to the cache, use the `sonar.cfamily.analysisCache.path` property in your CI process configuration.

### Incremental symbolic execution <a href="#incremental-symbolic-execution" id="incremental-symbolic-execution"></a>

The analyzer provides an incremental symbolic execution mode that incrementally updates the analysis results computed for the rules with a symbolic-execution tag (see the [#implementationrelated-rule-tags](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/understanding-the-analysis#implementationrelated-rule-tags "mention") articl&#x65;*)*. It may be used to shorten the analysis.

Incremental symbolic execution is enabled by default. It acts as an additional layer on top of the analysis cache and uses the same storage to maintain the required information as selected for the analysis cache (server cache or local file system). For more information on the analysis cache, see the corresponding section above.

In contrast to the analysis cache, incremental symbolic execution detects code changes on an intra-file level rather than treating a file and its dependencies as a whole. This allows it to skip parts of the analysis or to reuse parts of the previous analysis results that are still valid even in cases where a file or its dependencies did undergo edits.

To toggle the incremental symbolic execution mode, set the property `sonar.cfamily.symbolicExecution.useIncrementalMode` to `true` or `false` at the scanner level.

### Parallel code scan <a href="#parallel-code-scan" id="parallel-code-scan"></a>

By default, the analyzer tries to parallelize the analysis of compilation units; it spawns as many jobs as the machine’s logical CPUs allow.

If required, in **Compilation Database mode**, the number of scheduled parallel jobs can be customized by configuring the property `sonar.cfamily.threads=n` at the scanner level, where `n` is an integer indicating the maximum number of parallel jobs.

You should consider setting the `sonar.cfamily.threads` property only when the desired number of logical CPUs cannot be detected automatically. A typical example is when the analysis should not consume all the available computing resources to leave room for other tasks running in parallel on the same machine.

When setting the `sonar.cfamily.threads` property, you should set it to a value less or equal to the number of logical CPUs available. Over-committing doesn’t accelerate the analysis and can even slow it down.

### Automatic Shallow Mode for Advanced Bug Detection

For large files that take a long time to analyze, you can activate Automatic Shallow Mode, which trades a potentially lower bug detection rate for a faster analysis time.

To activate shallow mode on files with more than `N` entry points set the property `sonar.cfamily.symbolicExecution.automaticShallowModeThreshold=N`. An entry point is essentially a (member-) function declaration with a body. The analyzer begins its work at every function declared with a body, so a file containing many entry points will require a longer analysis time.

By default `sonar.cfamily.symbolicExecution.automaticShallowModeThreshold=0` which means this feature is disabled.

If you are willing to reduce the bug detection rate in order to reduce analysis time, we recommend setting it to 70 entry points. Choosing a lower, non-zero value for `N` will reduce analysis depth on more files and will make the analysis even faster. Choosing a higher value for `N` restricts shallow mode only to the largest files, minimizing the impact on small and medium files.
