# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/rust.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/rust.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/rust.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/rust.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/rust.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/rust.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/rust.md

# Rust

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

All versions are fully supported through the Clippy linter.

The Rust analyzer supports:

* Code Coverage import (LCOV and Cobertura formats)
* Cognitive Complexity metric
* Cyclomatic Complexity metric
* Import of Clippy output as external rules (JSON format)

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before using the Sonar Rust analyzer, ensure the following tools are installed and available in your system’s PATH:

* **Cargo**: The Rust package manager. You can install it from [rustup.rs](https://rustup.rs/).
* **Clippy (cargo clippy)**: A Rust linter to catch common mistakes and improve your code. Install it using `rustup component add clippy`.

### Running the analysis <a href="#running-the-analysis" id="running-the-analysis"></a>

You can analyze Rust projects using the [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention"). Make sure it is available on the machine running the analysis.

### Clippy integration <a href="#clippy-integration" id="clippy-integration"></a>

The Sonar Rust analyzer integrates with Clippy to provide code analysis. You can configure the Clippy integration in two ways:

* Run Clippy Analysis: The analyzer runs Clippy automatically (default).
* Import External Reports: Load pre-generated Clippy JSON reports.

These two methods are not mutually exclusive and can be used simultaneously. However, be aware that using both methods might lead to undesirable effects, such as duplicated Clippy issues.

#### Running the Clippy analysis <a href="#executing-the-clippy-analysis" id="executing-the-clippy-analysis"></a>

By default, the Sonar Rust analyzer automatically triggers a Clippy analysis. The analyzer will look for a *Cargo.toml* manifest in the project’s root directory and run Clippy.

* You can specify custom paths to `Cargo.toml` manifest files using `sonar.rust.cargo.manifestPaths`, which accepts a comma-separated list of file paths.
* You can disable the automatic Clippy analysis by setting the `sonar.rust.clippy.enable` property to `false`.

Even when Clippy analysis is disabled, all other Sonar Rust analysis features, such as code metrics calculation, code complexity, and code duplication, will remain active.

#### Importing external Clippy reports <a href="#importing-external-clippy-reports" id="importing-external-clippy-reports"></a>

You can import Clippy issues from external JSON reports using the `sonar.rust.clippy.reportPaths` property. This property accepts a comma-separated list of file paths to your Clippy JSON reports.

You can generate Clippy JSON reports with the command `cargo clippy --message-format=json`.

### Code coverage <a href="#code-coverage" id="code-coverage"></a>

See the [test-coverage-parameters](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/test-coverage-parameters "mention") page for information on importing coverage reports for Rust.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

For a complete list of available properties and their descriptions, please refer to the Rust-specific properties in the project **Administration** > **Configuration** > **General Settings** > **Languages** > **Rust**.

To discover and update the Rust-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **Rust**. See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties.

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

If the automatically triggered analysis fails, a warning will be displayed in the logs and on the SonarQube project page. To troubleshoot the issue, try manually running `cargo clippy` in the project directory to examine the error details.
