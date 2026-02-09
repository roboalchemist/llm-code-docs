# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/analysis-modes.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/analysis-modes.md

# Analysis modes

The analysis can operate in *Automatic Analysis* or *Manual configuration* (Compilation Database) modes.

* [automatic-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/automatic-analysis "mention") automatically analyzes your code simply by reading it from your GitHub repository, without the need to configure a CI-based analysis.
* Compilation Database mode gives you more control over the configuration and requires a CI-based analysis configuration. You can activate this mode by deactivating Automatic Analysis and supplying a `compile_commands.json` to the SonarScanner.

The analyzer must understand the code’s intended compilation options to ensure an accurate static analysis of the CFamily code.

* In Compilation Database mode, these options are provided to the analyzer through [Compilation Database](https://clang.llvm.org/docs/JSONCompilationDatabase.html): a JSON file introduced by the LLVM project.
* In Automatic Analysis mode, the analyzer attempts to deduce these options automatically. A set of high-level Automatic Analysis properties can tune the automatic deduction process. For details, see the [#automatic-analysis-specific-properties](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/customizing-the-analysis#automatic-analysis-specific-properties "mention") article on the [customizing-the-analysis](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/customizing-the-analysis "mention") page.

### Choosing the right analysis mode <a href="#choosing-the-right-analysis-mode" id="choosing-the-right-analysis-mode"></a>

Compilation Database mode is recommended if:

* Your projects aren’t hosted on GitHub. Automatic Analysis is only available for GitHub repositories.
* You’re seeking the highest CFamily analysis quality SonarQube Cloud can provide. Please note that in rare instances, Automatic Analysis may result in some issues being overlooked.
* You want to have finer control over the analysis configuration, such as analyzing a specific build variant.
* You require faster analysis. In Compilation Database mode, you can control the hardware capacity on the CI where the analysis runs.
* Your projects have Objective-C code: Objective-C analysis is not supported in Automatic Analysis mode.

Automatic Analysis mode is recommended if:

* Your projects use compilers that don’t meet the supported compiler prerequisite of Compilation Database mode (see the [prerequisites](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/prerequisites "mention") page).
* Your projects use compilation environments where generating a compilation database is not feasible (see the [prerequisites](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/prerequisites "mention") page).
* You desire a swift analysis setup without the need to allocate human resources for the maintenance of a CI pipeline and the generation of a Compilation Database.
* Your projects have a low CFamily code percentage.
