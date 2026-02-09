# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/dotnet-environments/specify-test-project-analysis.md

# Specifying test projects

This page refers to the SonarScanner for .NET, also known as SonarScanner for MSBuild. For more information about how to install and use it, read the [installing](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/installing "mention") documentation page.

### Analyzer references <a href="#analyzer-references" id="analyzer-references"></a>

* The SonarScanner for .NET adds the SonarAnalyzer.CSharp and SonarAnalyzer.VB analyzers on the fly during the build, even if they are not specifically referenced in the .NET project. The set of rules to execute is determined by the project type and quality profile defined in your instance of SonarQube Server.
* All third-party analyzers referenced by the .NET project (for example, via NuGet package references) will be executed as part of the build. Issues from those analyzers will be uploaded to SonarQube Server as [external analyzer reports](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/importing-external-issues). You can configure the third-party rules as you normally would using a [rule set](https://learn.microsoft.com/en-us/visualstudio/code-quality/using-rule-sets-to-group-code-analysis-rules?view=vs-2019) or [EditorConfig file](https://learn.microsoft.com/en-us/visualstudio/ide/create-portable-custom-editor-options?view=vs-2022).

  During the build, SonarScanner for .NET will merge your custom rule set with a rule set generated from the quality profile. In the event of a conflict, the settings in the generated rule set take precedence.

#### Differences between analysis of main projects and test projects <a href="#differences-between-analysis-of-main-projects-and-test-projects" id="differences-between-analysis-of-main-projects-and-test-projects"></a>

The SonarScanner for .NET analyzes main projects differently from test projects.

* Main projects implement new functionalities; an example would be a project for production or tooling.
* Test projects test functionalities implemented by main projects and are typically using a test framework.

**Analysis of main projects**

* Analysis rules will be run against main projects unless the rule or project is explicitly excluded. Raised issues will be uploaded to SonarQube Server.
* Only rules related to the main project code will be executed.
* The [metrics](https://docs.sonarsource.com/sonarqube-server/instance-administration/analysis-functions/metrics-parameters) for commercial versions of SonarQube Server are calculated.
* [Lines of code](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/monitoring/lines-of-code) (LOC) limits for projects in commercial versions of SonarQube Server are calculated.
* Syntax colorization and symbol highlighting are supported for both main projects and test projects.

**Analysis of test projects**

* Analysis rules will be run against test projects unless the rule or project is explicitly excluded. Raised issues will be uploaded to SonarQube Server.
* Only the rules related to test code will be executed on test projects. Likewise, rules that are explicitly excluded will not be executed.
* Test projects do not count towards the Lines of Code (LOC) limits for projects in commercial versions of SonarQube Server.
* Metrics and copy/paste detection data are not calculated for test projects.
* Syntax colorization and symbol highlighting are supported for both main projects and test projects.

**Analysis of excluded test projects**

* Analysis rules are not run against excluded test projects, no issues will be reported to SonarQube Server or SonarQube Cloud. This is the case even if the test project references third-party NuGet analyzer packages; those analyzers will not be executed.
* In SonarQube 9.9+, all test projects can be excluded from analysis by adding the `/d:sonar.dotnet.excludeTestProjects=true` SonarScanner for .NET parameter in the command line.
* In SonarQube versions 8.8 and older, all test projects are excluded from analysis on SonarQube.

**Analysis of projects excluded with \<SonarQubeExclude>true\</SonarQubeExclude>**

* Any project can be excluded from analysis using `<SonarQubeExclude>true</SonarQubeExclude>` in a project file.
* No rule diagnostics, metrics, syntax colorization, or symbol highlighting will be calculated during the analysis. Excluding these can help to reduce the time it takes to run an analysis.

### Explicit project categorization <a href="#explicit-project-categorization" id="explicit-project-categorization"></a>

It is possible to explicitly mark a project as being a test project by setting the MSBuild property `SonarQubeTestProject` to `true` or `false`.

```xml
<PropertyGroup>
  <SonarQubeTestProject>false</SonarQubeTestProject>
</PropertyGroup>
```

{% hint style="info" %}
Setting `SonarQubeTestProject` explicitly takes precedence over the default project categorization behavior.
{% endhint %}

### Implicit project categorization <a href="#implicit-project-categorization" id="implicit-project-categorization"></a>

SonarScanner for .NET decides whether a project contains main code or test code by looking at data in the project file. Categorization is assigned at the project level. In other words, all the code within a project is considered *as either main code or test code*; it is not possible to treat some of the code within the same project *as main code and other code as test code*.

The SonarScanner for .NET will treat the project as containing test code if any of the following are true:

* The project file contains the `MSTest ProjectTypeGuid`: `3AC096D0-A1C2-E12C-1390-A8335801FDAB`
* The project file contains the MSTest GUID (`{3AC096D0-A1C2-E12C-1390-A8335801FDAB}`) in the `ProjectTypeGuid` property.
* The project file contains the legacy Service GUID (`{82A7F48D-3B50-4B1E-B82E-3ADA8210C358}`) which is added by the Test Explorer to mark a project as containing tests.
* The project file contains the `ProjectCapability TestContainer` for [SDK-style .NET projects](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/overview#project-files). Note: this property can be set indirectly as a result of importing a NuGet package. See below for more information.
* The project file name matches the RegEx set in the deprecated property `sonar.msbuild.testProjectPattern`.
* The project references a known unit test-related assembly. The list of recognized assemblies is [here](https://github.com/SonarSource/sonar-scanner-msbuild/blob/master/src/SonarScanner.MSBuild.Tasks/IsTestByReference.cs#L35).

There are a few special project types for which MSBuild will create and build a temporary project (e.g., Microsoft Fakes, WPF) as part of the "main" build. The SonarScanner for .NET ignores such temporary projects. The "main" project will be categorized and treated as normal.

**Importing third-party unit test NuGet packages**

A project can be classified as a test project because it references a third-party unit test NuGet package. Packages can add MSBuild targets to the build.

For example, if your project references e.g. XUnit as follows:

```xml
<PackageReference Include="xunit" Version="2.4.1" />
```

Then the XUnit package will add a target to the build containing the following property assignment:

```xml
  <ItemGroup>
    <ProjectCapability Include="TestContainer" />
  </ItemGroup>
```

This will cause your project to be classified as a test project, and the MSBuild output will contain a message like the following:

```css-79elbk
Sonar: (MyProject.csproj) project has the ProjectCapability 'TestContainer' -> test project
```

### Project categorization <a href="#project-categorization" id="project-categorization"></a>

SonarScanner for .NET writes information about the project categorization to the MSBuild output log. The information will appear in logs at `normal` verbosity or greater.

When building with `MSBuild.exe`, the default logging verbosity is `normal`. Therefore, the categorization messages will be logged automatically by default.

When building with `dotnet build`, the default logging verbosity is `minimal`. Therefore, you must increase the logging verbosity to see categorization messages; this is achieved, for example, by passing a `-v:n` argument to `dotnet build`; for reference, here is the Microsoft documentation on [.NET build options](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-build#options).

Please note that this log output was added in SonarScanner for .NET [v4.7](https://github.com/SonarSource/sonar-scanner-msbuild/releases/tag/4.7.0.2295).

**Analysis setup examples**

The following examples are taken from an analysis setup used in the [SonarQube for Visual Studio](https://github.com/sonarsource/sonarlint-visualstudio) repository:

```css-79elbk
...
SonarQubeCategoriseProject:
  Sonar: (Progress.csproj) Categorizing project as test or product code...
  Sonar: (Progress.csproj) Project categorized. SonarQubeTestProject=False
...
```

```css-79elbk
...
SonarQubeCategoriseProject:
  Sonar: (Progress.TestFramework.csproj) Categorizing project as test or product code...
  Sonar: (Progress.TestFramework.csproj) SonarQubeTestProject has been set explicitly to true
  Sonar: (Progress.TestFramework.csproj) Project categorized. SonarQubeTestProject=true
...
```

```css-79elbk
...
SonarQubeCategoriseProject:
  Sonar: (SonarQube.Client.Tests.csproj) Categorizing project as test or product code...
  Sonar: (SonarQube.Client.Tests.csproj) project is evaluated as a test project based on the project name
  Sonar: (SonarQube.Client.Tests.csproj) Project categorized. SonarQubeTestProject=True
...
```

Please note that when a file is categorized as a test, verbose mode will show similar logs in the END step. For more details, please check `sonar.verbose` in the list of [#begin](https://docs.sonarsource.com/sonarqube-server/scanners/dotnet/using#begin "mention") step command line parameters.

```css-79elbk
DEBUG: 'foo/bar/baz/SomeClass.cs' generated metadata as test  with charset 'UTF-8'
DEBUG: 'foo\bar\baz\SomeClass.cs' indexed as test with language 'cs'
```
