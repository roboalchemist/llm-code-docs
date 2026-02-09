# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-npm/configuring.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/configuring.md

# Configuring the scanner

### Code Coverage <a href="#code-coverage" id="code-coverage"></a>

In an Azure DevOps / TFS environment, test files are automatically retrieved as follows:

* A search is done for *.trx* files in any `TestResults` folder located under `$Build.SourcesDirectory`.
* If no .trx files are found there, then a fallback search is performed under `$Agent.TempDirectory`.

Once the *.trx* files have been found, their *.coverage* counterparts are retrieved and converted to *.coveragexml* files for upload to SonarQube Cloud.

As stated above, this will work only with the .NET Framework version of the scanner.

See the[dotnet-test-coverage](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/dotnet-test-coverage "mention") page for more information.

### Excluding projects from analysis <a href="#excluding-projects-from-analysis" id="excluding-projects-from-analysis"></a>

Some project types, such as [Microsoft Fakes](https://msdn.microsoft.com/en-us/library/hh549175.aspx), are automatically excluded from the analysis. To manually exclude a different type of project from the analysis, place the following in its *.csproj* / *.vbproj* file.

```xml
<!-- in .csproj -->
<PropertyGroup>
  <!-- Exclude the project from analysis -->
  <SonarQubeExclude>true</SonarQubeExclude>
</PropertyGroup>
```

### Advanced topics <a href="#advanced-topics" id="advanced-topics"></a>

**Analyzing MSBuild 12, 14, and 15 projects with MSBuild 16**

The Sonar Scanner for .NET requires your project to be built with MSBuild 16. We recommend installing Visual Studio 2017 or later on the analysis machine in order to benefit from the integration and features provided with the Visual Studio ecosystem (VSTest, MSTest unit tests, etc.).

Projects targeting older versions of the .NET Framework can be built using MSBuild 16 by setting the "TargetFrameworkVersion" MSBuild property as documented by Microsoft:

* [How to: Target a Version of the .NET Framework](https://msdn.microsoft.com/en-us/library/bb398202.aspx)
* [MSBuild Target Framework and Target Platform](https://msdn.microsoft.com/en-us/library/hh264221.aspx)

For example, if you want to build a .NET 3.5 project, but you are using a newer MSBuild version:

```bash
MSBuild.exe /t:Rebuild /p:TargetFramework=net35
```

If you do not want to switch your production build to MSBuild 16, you can set up a separate build dedicated to the SonarQube Cloud analysis.

**Detection of test projects**

You can read a full description of that subject on our wiki [here](https://github.com/SonarSource/sonar-scanner-msbuild/wiki/Analysis-of-product-projects-vs.-test-projects).

**Per-project analysis parameters**

Some analysis parameters can be set for a single MSBuild project by adding them to its *.csproj* file.

```xml
<!-- in .csproj -->
<ItemGroup>
  <SonarQubeSetting Include="sonar.stylecop.projectFilePath">
    <Value>$(MSBuildProjectFullPath)</Value>
  </SonarQubeSetting>
</ItemGroup>
```

#### Analyzing languages other than C# and VB <a href="#analyzing-languages-other-than-c-and-vb" id="analyzing-languages-other-than-c-and-vb"></a>

For newer SDK-style projects (used by .NET Core, .NET 5, and later), the SonarScanner for .NET will analyze all file types supported by the available language plugins unless explicitly excluded.

If you have an `esproj` project type, make sure to use [Microsoft.VisualStudio.JavaScript.SDK](https://www.nuget.org/packages/Microsoft.VisualStudio.JavaScript.SDK) version 0.5.74-alpha or later to ensure the SonarScanner for .NET recognizes the esproj contents for scanning.

For older-style projects, the scanner will only analyze files listed in the *.csproj* or *.vbproj* project file. Usually, this means that only C# and VB files will be analyzed. To enable the analysis of other types of files, include them in the project file.

Even if you disable multi-file analysis (see below), any files included by an element of the `ItemTypes` in [this list](https://github.com/SonarSource/sonar-scanner-msbuild/blob/5.14.0.78575/src/SonarScanner.MSBuild.Tasks/Targets/SonarQube.Integration.targets#L109) will be analyzed automatically. For example, the following line in your *.csproj* or *.vbproj* file will enable the analysis of all JavaScript files in the directory foobecause the content is one of the `ItemTypes` that are automatically analyzed.

```xml
<Content Include="foo\bar\*.js" />
```

Additionally, `<Compilation Remove="FileName.ext"/>` and `<None Remove="FileName.ext"/>` attributes in .NET project files (either .csproj or .vbproj) work differently depending on the file type and if the `sonar.scanner.scanAll` property (the multi-language analysis feature) is enabled or not.

* C# and VB.NET files will not be analyzed since they are not part of the compilation, and therefore the Roslyn analyzers will not run on them.
* When the multi-language analysis feature is enabled, additional language file types (such as JavaScript, TypeScript, SQL, etc.) are added to the scope and will be analyzed. To ignore specific language file types, we recommend that you use the `sonar.exclusions` property. See the [#multi-language-analysis](#multi-language-analysis "mention") article (below) for a list of file types automatically picked up by the scanner.

You can also add `ItemTypes` to the default list by following [these directions](https://github.com/SonarSource/sonar-scanner-msbuild/blob/5.14.0.78575/src/SonarScanner.MSBuild.Tasks/Targets/SonarQube.Integration.targets#L70).

You can check which files the scanner will analyze by looking in the file *.sonarqube-project.properties* after MSBuild has finished.

File type extensions can be manually excluded from the analysis using `sonar.exclusions`. See the [introduction](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/introduction "mention") to setting the analysis scope of your project for guidance.

#### Using SonarScanner for .NET with a proxy <a href="#using-sonarscanner-for-net-with-a-proxy" id="using-sonarscanner-for-net-with-a-proxy"></a>

On build machines that connect to the Internet through a proxy server you might experience difficulties connecting to SonarQube Server. To instruct the Java VM to use specific proxy settings use the following value:

```bash
SONAR_SCANNER_OPTS = "-Dhttp.proxyHost=yourProxyHost -Dhttp.proxyPort=yourProxyPort"
```

Where *yourProxyHost* and *yourProxyPort* are the hostname and the port of your proxy server. There are additional proxy settings for HTTPS, authentication, and exclusions that could be passed to the Java VM. For more information, see the following article: <https://docs.oracle.com/javase/8/docs/technotes/guides/net/proxies.html>.

You also need to set the appropriate proxy environment variables used by .NET. `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, and `NO_PROXY` are all supported. You can find more details [here](https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpclient.defaultproxy?view=net-5.0).

{% hint style="info" %}
Proxy environment variables do not work with the .NET Framework variant of SonarScanner for .NET at this time.
{% endhint %}

#### **Multi-language analysis**

The SonarScanner for .NET (starting from v8.0) automatically analyzes file types for select languages when the `sonar.scanner.scanAll` parameter is enabled. These file types are automatically picked up by the scanner:

Introduced in the SonarScanner for .NET v8.0:

* Ansible (.yaml)
* CloudFormation (.yaml)
* CSS (.css, .less, .scss, .sass)
* Helm (.yaml)
* HTML (.html, .xhtml, .cshtml, .vbhtml, .aspx, .ascx, .rhtml, .erb,.shtm, .shtml,.cmp, .twig)
* Javascript (.js, .jsx, .cjs, .mjs, .vue). See the [javascript-typescript-test-coverage](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/javascript-typescript-test-coverage "mention") page for details to adjust your setup.
* JSON (.json)
* Kubernetes (.yaml)
* PLSQL (.sql, .pks, .pkb)
* SQL (.tsql)
* TypeScript (.ts, .tsx, .cts, .mts). See the [javascript-typescript-test-coverage](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/javascript-typescript-test-coverage "mention") page for details to adjust your setup.

Introduced in the SonarScanner for .NET v10.0:

* AzureResourceManager (.bicep)
* Docker (Dockerfile, \*.dockerfile, \*.Dockerfile, Dockerfile.\*)
* Go (.go)
* Java Config files (\*app\*.properties, \*app\*.yaml, \*app\*.yml)
* PHP (.php, .php3, .php4, .php5, .phtml, .inc)
* Python (.py, .ipynb), including Jupyter Notebooks
* Secrets (\*.sh, \*.bash, \*.zsh, \*.ksh, \*.ps1, \*.properties, \*.conf, \*.pem, \*.config, .env, config)
* Terraform (.tf)

File type extensions can be found and configured in the SonarQube Cloud UI; see the [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention") page for more details. Additionally, you can also use path-matching patterns; see the [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention") page for this information.

Unless manually excluded, the files linked by the *.csproj* project file will be analyzed even if the value is false.

{% hint style="info" %}
Multi-Language analysis is enabled by default. If this was not intended and you have issues such as hitting your LOC limit or analyzing unwanted files, you can set `/d:sonar.scanner.scanAll=false` in the Begin step to *turn off multi-language analysis*.

If you're using an Azure pipeline, you can add `sonar.scanner.scanAll=false` to the `extraProperties` in your [#prepare-analysis-configuration](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/azure-pipelines/sonarqube-tasks#prepare-analysis-configuration "mention").
{% endhint %}

### Known issues <a href="#known-issues" id="known-issues"></a>

**I have multiple builds in the same pipeline, each of them getting analyzed even if the Run Code Analysis has already been executed:**

The scanner doesn’t uninstall the global `ImportBefore` targets to support concurrent analyses on the same machine. The main effect is that if you build a solution where a .sonarqube folder is located nearby, then the `sonar-dotnet` analyzer will be executed along with your build task.

To avoid that, you can disable the targets file by adding a build parameter:

```bash
msbuild /p:SonarQubeTargetsImported=true
dotnet build -p:SonarQubeTargetsImported=true
```

**Excluding files in certain directories**

[It is known](https://github.com/SonarSource/sonar-dotnet/issues/6328) that the SonarScanner for .NET can’t filter the excluded files/folders from the analysis, which happens during the build. The `sonar.exclusions` property is only used to filter issues sent to SonarQube Cloud during the final step.

As a workaround, you can try to add an *.editorconfig* file in the folder to override the severity of the Sonar rules:

```ini
[*.cs]
dotnet_diagnostic.S1118.severity = none
```

Unfortunately, you may have to manually do this for every rule.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/introduction "mention")
* [installing](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/installing "mention")
* [using](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/using "mention")
