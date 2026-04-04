# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/running-the-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/running-the-analysis.md

# Running the analysis

For Automatic Analysis mode, the analysis will run automatically after your project is activated (see the [#activating-automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/automatic-analysis#activating-automatic-analysis "mention") article on the [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") page). For Compilation Database mode, continue reading this page to learn how to execute the analysis on your CI.

Refer to the CFamily [prerequisites](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/prerequisites "mention") to pick the suitable scanner variant, and refer to the picked scanner documentation to learn how to execute it. In addition, you need to set the `sonar.cfamily.compile-commands` scanner property to analyze in Compilation Database mode.

### SonarScanner CLI <a href="#sonarscanner-cli" id="sonarscanner-cli"></a>

If you decide to use the Compilation Database mode, please ensure you have generated the `compile_commands.json` file before proceeding.

**Step 1:** Add the `sonar-project.properties` file at the root of your project. Sample `sonar-project.properties`:

```properties
sonar.projectKey=myFirstProject
sonar.projectName=My First C++ Project
sonar.projectVersion=1.0
sonar.sources=src
sonar.sourceEncoding=UTF-8
sonar.host.url=SonarCloudURL
```

Gathering all your code trees in a subdirectory of your project is recommended to avoid analyzing irrelevant source files like third-party dependencies. You can specify this subdirectory by setting the property `sonar.sources` accordingly. In this example, we named it `src`.

**Step 2:** Add the property `sonar.cfamily.compile-commands` in the `sonar-project.properties` file. You should set it to the path of the *Compilation Database* file relative to the project directory (`compile_commands.json` in these examples):\
`sonar.cfamily.compile-commands=compile_commands.json`

**Step 3:** Execute the SonarScanner CLI (`sonar-scanner`) from the root directory of your project: `sonar-scanner`\
For more SonarScanner CLI-related options, see the [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention") page.

**Step 4:** Follow the link provided at the end of the analysis to browse your project’s quality metrics in the UI.

### SonarScanner for .NET <a href="#sonarscanner-for-dotnet" id="sonarscanner-for-dotnet"></a>

This is an example of analyzing a Solution using a C++ and C# mix in Compilation Database mode with a build wrapper\*.\*

The SonarScanner for .NET does not handle `sonar-project.properties` files, so the compilation database must be set during the .NET `begin` step.

Note that in this scenario, source code stored in shared folders, which are not considered a "Project" by Visual Studio, won’t be scanned.

1. Download and install the SonarScanner for .NET (see [installing](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet/installing "mention")) and the build wrapper (see the CFamily [prerequisites](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/prerequisites "mention") page).
2. Execute the SonarScanner for .NET `begin` step with the build wrapper output parameter:\
   `/d:sonar.cfamily.compile-commands=<build_wrapper_output_directory>/compile_commands.json`
3. Add execution of the build wrapper to your normal .NET build command
4. Execute the SonarScanner for .NET `end` step to complete the analysis

```bash
SonarScanner.MSBuild.exe begin /k:"cs-and-cpp-project-key" /n:"My C# and C++ project" /v:"1.0" /d:sonar.cfamily.compile-commands="build_wrapper_output_directory/compile_commands.json"
build-wrapper-win-x86-64.exe --out-dir build_wrapper_output_directory MSBuild.exe /t:Rebuild /nodeReuse:False
SonarScanner.MSBuild.exe end
```

An analysis configuration example project with a mix of C# and C++ is available on [GitHub](https://github.com/sonarsource-cfamily-examples/windows-msbuild-dotnet-cpp-azure-sc).
