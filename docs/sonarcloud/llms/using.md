# Source: https://docs.sonarsource.com/sonarqube-mcp-server/using.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/using.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/using.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/using.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/using.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-npm/using.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/using.md

# Using the scanner

{% hint style="warning" %}
The SonarScanner for .NET version 9.2 [has been deprecated](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/9.2.0.110275) and should not be used.
{% endhint %}

### Use <a href="#use" id="use"></a>

{% hint style="info" %}
You can invoke the Scanner using arguments with both dash (-) or forward-slash (/) separators. For example:

`SonarScanner.MSBuild.exe begin /k:"project-key"` or

`SonarScanner.MSBuild.exe begin -k:"project-key"`
{% endhint %}

There are two versions of the SonarScanner for .NET. In the following commands, you need to pass an authentication token using the `sonar.token` property. To manage your tokens, see:

* From the Team plan: [scoped-organization-tokens](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/scoped-organization-tokens "mention").
* With the Free plan: [managing-tokens](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/managing-tokens "mention").

Any project file accepted by MSBuild.exe or dotnet can be used, for example *.sln*, *.proj*, *.csproj*, or *.vbproj*.

#### "Classic" .NET Framework invocation <a href="#classic-net-framework-invocation" id="classic-net-framework-invocation"></a>

The first version is based on the "classic" .NET Framework. To use it, execute the following commands from the root folder of your project:

```bash
SonarScanner.MSBuild.exe begin /k:"project-key" /o:"<organization>" /d:sonar.token="<token>"
MSBuild.exe <path to solution.sln> /t:Rebuild
SonarScanner.MSBuild.exe end /d:sonar.token="<token>"
```

#### .NET Core and .NET Core Global Tool invocation <a href="#net-core-and-net-core-global-tool-invocation" id="net-core-and-net-core-global-tool-invocation"></a>

The second version is based on .NET Core which has a very similar usage:

```bash
dotnet <path to SonarScanner.MSBuild.dll> begin /k:"project-key" /o:"<organization>" /d:sonar.token="<token>"
dotnet build <path to solution.sln> --no-incremental
dotnet <path to SonarScanner.MSBuild.dll> end /d:sonar.token="<token>" 
```

The .NET Core version can also be used as a .NET Core Global Tool. After installing the Scanner as a global tool as described above, it can be invoked as follows:

```bash
dotnet tool install --global dotnet-sonarscanner
dotnet sonarscanner begin /k:"project-key" /o:"<organization>" /d:sonar.token="<token>"
dotnet build <path to solution.sln> --no-incremental
dotnet sonarscanner end /d:sonar.token="<token>"
```

In summary, the invocation of the SonarScanner for .NET will depend on the scanner flavor you want to use:

| **Scanner Flavor**    | **Invocation**                                   |
| --------------------- | ------------------------------------------------ |
| .NET Core Global Tool | `dotnet sonarscanner begin` etc.                 |
| .NET Core 3.1+        | `dotnet <path to SonarScanner.MSBuild.dll>` etc. |
| .NET Framework 4.6.2+ | `SonarScanner.MSBuild.exe begin` etc.            |

**Notes:**

* The .NET Core version of the scanner does not support TFS XAML builds and automatic finding/conversion of Code Coverage files. Apart from that, all versions of the Scanner have the same capabilities and command-line arguments.

### Analysis steps <a href="#analysis-steps" id="analysis-steps"></a>

The construction of your pipeline will be slightly different according to your DevOps platform integration. Please see the appropriate pages for your platform:

{% tabs %}
{% tab title="GITHUB" %}
See the [github](https://docs.sonarsource.com/sonarqube-cloud/getting-started/github "mention") page.
{% endtab %}

{% tab title="BITBUCKET CLOUD" %}
See the [bitbucket-cloud](https://docs.sonarsource.com/sonarqube-cloud/getting-started/bitbucket-cloud "mention") page.
{% endtab %}

{% tab title="GITLAB" %}
See the [gitlab](https://docs.sonarsource.com/sonarqube-cloud/getting-started/gitlab "mention") page.
{% endtab %}

{% tab title="AZURE DEVOPS" %}
See the [azure-devops](https://docs.sonarsource.com/sonarqube-cloud/getting-started/azure-devops "mention") page.
{% endtab %}
{% endtabs %}

#### Begin <a href="#begin" id="begin"></a>

The `begin` step is executed when you add the `begin` command-line argument. It hooks into the build pipeline, downloads SonarQube Cloud quality profiles and settings, and prepares your project for analysis.

**Begin step command line parameters**

* `/k:<project-key>`
  * **\[required]** Specifies the key of the analyzed project in SonarQube Cloud.
* `/n:<project name>`
  * **\[optional]** Specifies the name of the analyzed project in SonarQube Cloud.
  * Adding this argument will overwrite the project name in SonarQube Cloud if it already exists.
* `/v:<version>`
  * **\[recommended]** Specifies the version of your project.
* `/o:<organization>`
  * **\[required]** Specifies the name of the target organization in SonarQube Cloud.
* `/d:sonar.token=<token> or <username>`
  * **\[recommended]** Specifies the authentication token or username used to authenticate with to SonarQube Cloud.
  * If this argument is added to the begin step, it must also be added to the end step.
* `/d:sonar.verbose=true`
  * **\[optional]** Sets the logging verbosity to detailed.
  * Add this argument before sending logs for troubleshooting.
* `/d:sonar.dotnet.excludeTestProjects=true`
  * **\[optional]** Excludes Test Projects from analysis.
  * Add this argument to improve build performance when issues should not be detected in Test Projects.
* `/d:sonar.http.timeout=60`
  * **\[optional]** Specifies the time in seconds to wait before the HTTP requests time out.
* `/d:<analysis-parameter>=<value>`
  * **\[optional]** Specifies an additional SonarQube Cloud analysis parameter, you can add this argument multiple times. Please note that the `sonar.sources` and `sonar.tests` parameters are not supported.
* `/s:<custom.analysis.xml>`
  * **\[optional]** Overrides the `$install_directory/SonarQube.Analysis.xml`. You need to give the absolute path to the file.
* `/d:sonar.plugin.cache.directory=<path_to_directory>`
  * **\[optional]** Requires version 5.15+. Overrides the path where the scanner downloads its plugins. Plugins that are already present will not be downloaded again, unless newer versions are available.
  * You can provide a relative or an absolute path.
  * Defaults to the machine’s temporary files directory.
* `/d:sonar.scanner.scanAll=true`
  * **\[optional]** Enables and Disables the analysis of multiple file types. See the [#multi-language-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/configuring#multi-language-analysis "mention") article for the full details. Unless manually excluded, the files linked by the *.csproj* project file will be analyzed even if the value is false.
  * **Default**: true
* `/d:sonar.cs.analyzeRazorCode=<value>`
  * **\[optional]** If set to "true", .razor and .cshtml files will be fully analyzed, this may increase the analysis time. If set to "false", .cshtml files will be analyzed for taint vulnerabilities only.
  * **Caution**: Defining this in your begin step overrides the value set in SonarQube (Server, Cloud).
* `/d:sonar.scanner.useSonarScannerCLI=true`
  * **\[optional]** If set to `true`, the [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention") will be used in the end step. Without this parameter, the end step will use the scanner engine downloaded from SonarQube Cloud. Use this setting if you encounter failures in the end step or incomplete analysis results with the SonarScanner for .NET version 10.4 or higher.

**Default**: true

For detailed information about all available parameters, see the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page.

{% hint style="warning" %}
The "begin" step will modify your build like this:

* the active `CodeAnalysisRuleSet` will be updated to match the SonarQube Cloud quality profile
* `WarningsAsErrors` will be turned off

If your build process cannot tolerate these changes we recommend creating a second build job for SonarQube Cloud analysis.
{% endhint %}

#### Build <a href="#build" id="build"></a>

Between the `begin` and `end` steps, you need to build your project, execute tests and generate code coverage data. This part is specific to your needs, and it is not detailed here. See the [dotnet-test-coverage](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/dotnet-test-coverage "mention") page for more information.

The rules configured in your quality profile are run during the build, and it is expected that analyzing with SonarQube Cloud can increase build duration from 4 to 8 times. The impact on duration will vary by project and by what rules are enabled; some rules are simple to execute and others take additional time to have the expected impact and precision. See the [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention") page for information about managing those rules.

#### End <a href="#end" id="end"></a>

The end step is executed when you add the "end" command-line argument. It cleans the `MSBuild/dotnet` build hooks, collects the analysis data generated by the build, the test results, and the code coverage, and then uploads everything to SonarQube Cloud. There are only two additional arguments that are allowed for the end step.

**End step command line parameters:**

* `/d:sonar.token=<token>` or `/d:sonar.token=<username>`
  * If this argument is added to the Begin step, it must also be added to the End step.

#### Known limitations <a href="#known-limitations" id="known-limitations"></a>

* MSBuild versions 14 and older are not supported. MSBuild 15 is deprecated and support will be removed in a future version. We recommend using MSBuild 16 as a minimal version.
* Web Application projects are supported. Legacy Web Site projects are not.
* Projects targeting multiple frameworks and using preprocessor directives could have slightly inaccurate metrics (lines of code, complexity, etc.) because the metrics are calculated only from the first of the built targets.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/introduction "mention")
* [installing](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/installing "mention")
* [configuring](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/configuring "mention")
