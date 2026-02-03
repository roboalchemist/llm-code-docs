# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/dotnet-environments/dotnet-test-coverage.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/dotnet-test-coverage.md

# .NET test coverage

SonarQube Cloud supports the reporting of test coverage information as part of the analysis of your .NET project.

However, SonarQube Cloud does not produce the coverage report itself. Instead, you must set up a third-party tool to produce the report as part of your build process. You then need to configure your analysis to tell the SonarScanner where the report is located so that it can pick it up and send it to SonarQube Cloud, where it will be displayed on your project dashboard along with the other analysis metrics.

SonarQube Cloud supports the following .NET test coverage tools:

* [#visual-studio-code-coverage](#visual-studio-code-coverage "mention")
* [#dotnetcoverage](#dotnetcoverage "mention") Code Coverage
* [#dotcover](#dotcover "mention")
* [#opencover](#opencover "mention")
* [#coverlet](#coverlet "mention")

{% hint style="info" %}
If you wish to use an unsupported tool, SonarQube Server supports generic format coverage for test coverage and test execution imports. However, note that it you are responsible for converting its output to the generic format. For information on the generic format including examples, see the [generic-test-data](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/generic-test-data "mention") page.

This page, *.NET test coverage*, focuses on the directly supported coverage tools.
{% endhint %}

### Follow the tutorial <a href="#follow-the-tutorial" id="follow-the-tutorial"></a>

When you import your .NET project into SonarQube Cloud, you will be guided through the setup process by an in-product tutorial. Once you have completed the tutorial, you should have a working analysis setup. The next step is to adjust that setup to enable coverage reporting.

The .NET scanner comes in four variants depending on which version of .NET and which CI you are using (*.NET Framework*, *.NET Core*, *.NET Global Tool*, and the *Azure DevOps Extension*). The setup is slightly different for each variant (see the [introduction](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/introduction "mention") to SonarScanner for .NET and [sonarcloud-extension-for-azure-devops](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarcloud-extension-for-azure-devops "mention") sections for more details), but the essential steps are the same.

The analysis is always split into two parts in your build process; the `begin` step and the `end` step. In between, you perform the actual build and your tests. To enable coverage reporting, you need to make the following changes:

* In the scanner `begin` step, add the appropriate parameter to specify the location of the coverage report file that will be produced.
* Just after the `build` step but before the scanner `end` step, ensure that your `test` step produces the coverage report file.

### Examples using the .NET tool scanner variant <a href="#examples-using-the-net-tool-scanner-variant" id="examples-using-the-net-tool-scanner-variant"></a>

The SonarScanner for .NET comes in four major variants: *.NET Framework*, *.NET Core*, *.NET Global Tool*, and the *Azure Pipelines extension*.

#### dotnet-coverage <a href="#dotnetcoverage" id="dotnetcoverage"></a>

This is a modern alternative to the Visual Studio Code Coverage provided by Microsoft (see above) that outputs results in the same format, is cross-platform and not dependent on having Visual Studio installed. It requires .NET Core 3.1 or later.

To use [dotnet-coverage](https://docs.microsoft.com/en-us/dotnet/core/additional-tools/dotnet-coverage), you can install it as a local or global dotnet tool:

```bash
dotnet tool install --global dotnet-coverage
```

Using this tool, your build script would look like something like this:

```bash
dotnet sonarscanner begin /k:"<sonar-project-key>"
    /d:sonar.token="<sonar-token>"
    /d:sonar.cs.vscoveragexml.reportsPaths=coverage.xml
dotnet build --no-incremental
dotnet-coverage collect "dotnet test" -f xml -o "coverage.xml"
dotnet sonarscanner end /d:sonar.token="<sonar-token>"
```

Note that we specify the path to the reports using `sonar.cs.vscoveragexml.reportsPaths` because this tool’s output format is the same as the Visual Studio Code Coverage tool. See the [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") page for information about this parameter. The code sample above uses the `-f xml` parameter to specify that the output format is in XML.

#### Visual Studio Code Coverage <a href="#visual-studio-code-coverage" id="visual-studio-code-coverage"></a>

We only recommend the use of this tool when the build agent has Visual Studio Enterprise installed or when you are using an Azure DevOps Windows image for your build. In these cases, the *.NET Framework* scanner will automatically find the coverage output generated by the `--collect "Code Coverage"` parameter without requiring an explicit report path setting. It will also automatically convert the generated report to XML. No further configuration is required. Here is an example:

```bash
SonarScanner.MSBuild.exe begin /k:"<sonar-project-key>" /d:sonar.token="<sonar-token>" 
dotnet build --no-incremental
dotnet test --collect "Code Coverage"
SonarScanner.MSBuild.exe end /d:sonar.token="<sonar-token>"
```

#### dotCover <a href="#dotcover" id="dotcover"></a>

To use [dotCover](https://www.jetbrains.com/help/dotcover/dotCover__Coverage_Analysis_on_Third-Party_Server.html) you must install it as a global dotnet tool:

```bash
dotnet tool install --global JetBrains.dotCover.CommandLineTools
```

Using this tool, your build script would look like something like this:

```bash
dotnet sonarscanner begin /k:"<sonar-project-key>"
    /d:sonar.token="<sonar-token>"
    /d:sonar.cs.dotcover.reportsPaths=dotCover.Output.html
dotnet build --no-incremental
dotnet dotcover test --dcReportType=HTML
dotnet sonarscanner end /d:sonar.token="<sonar-token>"
```

Note that the code sample above specifies the path to the reports using **`sonar.cs.dotcover.reportsPaths`** because it is using dotCover; see the [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") page for information about this parameter.

#### OpenCover <a href="#opencover" id="opencover"></a>

To use [OpenCover](https://github.com/OpenCover/opencover/wiki/Usage) you must download it from [OpenCover releases page](https://github.com/OpenCover/opencover/releases) and unzip it in an appropriate directory, for example: `C:\tools\opencover`

When using OpenCover, your build script would look like something like this:

```bash
dotnet sonarscanner begin /k:"<sonar-project-key>"
    /d:sonar.token="<sonar-token>"
    /d:sonar.cs.opencover.reportsPaths=coverage.xml
dotnet build --no-incremental
& C:\tools\opencover\OpenCover.Console.exe -target:"dotnet.exe" 
    -targetargs:"test --no-build"
    -returntargetcode
    -output:coverage.xml
    -register:user
dotnet sonarscanner end /d:sonar.token="<sonar-token>"
```

Note that the code sample specifies the path to the reports using `sonar.cs.opencover.reportsPaths` because it is using OpenCover. See the [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") page for information about this parameter.

#### Coverlet <a href="#coverlet" id="coverlet"></a>

To use [Coverlet](https://github.com/coverlet-coverage/coverlet), you must install it as a global dotnet tool:

```bash
dotnet tool install --global coverlet.console
```

You also have to install [the coverlet collector NuGet package](https://www.nuget.org/packages/coverlet.collector/) on your test project.

When using Coverlet, your build script would look like something like this:

```bash
dotnet sonarscanner begin /k:"<sonar-project-key>"
    /d:sonar.token="<sonar-token>"
    /d:sonar.cs.opencover.reportsPaths=coverage.xml
dotnet build --no-incremental
coverlet .\CovExample.Tests\bin\Debug\net6.0\CovExample.Tests.dll
    --target "dotnet" 
    --targetargs "test --no-build"
    -f=opencover 
    -o="coverage.xml"
dotnet sonarscanner end /d:sonar.token="<sonar-token>"
```

Note that the code sample specifies the path to the reports in `sonar.cs.opencover.reportsPaths` because Coverlet produces output in the same format as OpenCover. See the [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") page for information about this parameter.

### .NET Framework and .NET Core scanners <a href="#net-framework-and-net-core-scanners" id="net-framework-and-net-core-scanners"></a>

In most of the examples above, we use the .NET tool scanner variant. If you use the *.NET Framework* or *.NET Core* scanner, the commands will be a bit different but the pattern will be the same. See the [installing](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/installing "mention") page for details.

### Azure DevOps extension for SonarQube <a href="#sonarscanner-for-azure-devops" id="sonarscanner-for-azure-devops"></a>

Using the Azure DevOps extension for SonarQube and Visual Studio Code Coverage with a C# project, your azure-pipelines.yml would look something like the example below.

Note that with the Azure DevOps extension for SonarQube, the scanner `begin` step is handled by the `SonarCloudPrepare` task and the scanner `end` step is handled by the `SonarCloudAnalyze` task. Details about these properties are found on the [Azure DevOps Extension for SonarQube Cloud](https://marketplace.visualstudio.com/items?itemName=SonarSource.sonarcloud) page.

Also note in the code sample below, that because the build is running on Windows (`vmImage: windows-latest`), the pipeline does not need to explicitly define the path to the coverage report; this is evident because `sonar.cs.vscoveragexml.reportsPaths` is not included.

Additionally, you need to run `codecoverage.exe` to convert the report to XML. Here is a code sample, to be named azure-pipelines.yml in your files:

```yaml
trigger:
- main # or another name representing your main branch

variables:
- name: system.debug
  value: true 

pool:
  vmImage: windows-latest

steps:
- task: DotNetCoreCLI@2
  inputs:
    command: 'restore'
    projects: '<YourProject.sln>'
    feedsToUse: 'select'

- task: SonarCloudPrepare@4
  inputs:
    SonarCloud: '<YourSonarQubeServiceEndpoint>'
    organization: '<YourOrganizationName>'
    scannerMode: 'dotnet'
    projectKey: '<YourProjectKey>'
    projectName: '<YourProjectName>'

- task: DotNetCoreCLI@2
  inputs:
    command: 'build'
    projects: '<YourProject.sln>'

- task: DotNetCoreCLI@2
  inputs:
    command: 'test'
    projects: 'tests/**/*.csproj'
    arguments: '--collect "Code Coverage"'

- task: SonarCloudAnalyze@4
```

{% hint style="info" %}
The parameter `sonar.cs.ncover3.reportsPaths` was formerly used for or NCover3 . This parameter has been deprecated.
{% endhint %}

### VB.NET <a href="#vbnet" id="vbnet"></a>

The examples above are all for C# projects. The setup is identical for VB.NET projects except that you would use these parameters:

* `sonar.vbnet.vscoveragexml.reportsPaths` for Visual Studio Code Coverage
* `sonar.vbnet.dotcover.reportsPaths` for dotCover
* `sonar.vbnet.opencover.reportsPaths` for OpenCover or Coverlet

See the [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") section for information about these parameters.

{% hint style="warning" %}
The parameter `sonar.vbnet.ncover3.reportsPaths` was formerly used for or NCover3 . This parameter has been deprecated.
{% endhint %}

### Troubleshooting the import of the coverage report <a href="#troubleshooting" id="troubleshooting"></a>

#### Troubleshooting guide <a href="#troubleshooting-guide" id="troubleshooting-guide"></a>

See the [Troubleshooting guide for .NET code coverage import](https://community.sonarsource.com/t/coverage-troubleshooting-guide-for-net-code-coverage-import/37151).

#### Additional notes <a href="#additional-notes" id="additional-notes"></a>

**Invalid file path**

When using the `UserSourceLink` option of your tool, the coverage report is generates with source link URIs instead of system paths. You may need to turn off this option to use system paths as the source input for file coverage.
