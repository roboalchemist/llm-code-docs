# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/prerequisites.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/c-family/prerequisites.md

# Prerequisites

### Supported language standards <a href="#supported-language-standards" id="supported-language-standards"></a>

Please check the C, C++, and Objective-C rows in the [overview](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/overview "mention") for an up-to-date list of supported versions.

### Additional prerequisites for Compilation Database mode <a href="#additional-prerequisites-for-compilation-database-mode" id="additional-prerequisites-for-compilation-database-mode"></a>

#### Supported runtime environments <a href="#supported-runtime-environments" id="supported-runtime-environments"></a>

For the SonarScanner to analyze CFamily code, it must run on one of the following environments:

* Microsoft Windows on x86-64
* Linux on x86-64 or ARM64
* macOS with version 10.14.3 and later on x86-64 or Apple Silicon

#### SonarScanner <a href="#sonarscanner" id="sonarscanner"></a>

SonarScanner executes the analysis of CFamily languages on the CI.

* Use [sonarscanner-for-dotnet](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-dotnet "mention") for projects with mixed CFamily and .Net code.
* Use [sonarscanner-for-maven](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-maven "mention") for Maven projects with mixed CFamily and Java code.
* Use [sonarscanner-for-gradle](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-for-gradle "mention") for Gradle projects with mixed CFamily and Java code.
* Otherwise, use the default [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention").

#### Supported compilers <a href="#supported-compilers" id="supported-compilers"></a>

To be analyzed in Compilation Database mode, a project must compiled by one of the following compilers:

* Any version of Clang, clang-cl, GCC, and Microsoft C/C++ compilers
* Any version of the Intel compiler for Linux and macOS
* ARM5 and ARM6 compilers
* IAR compilers for ARM, Atmel AVR32, Atmel AVR, Renesas H8, Renesas RL78, Renesas RX, Renesas V850, Texas Instruments MSP430, and for 8051
* QNX compilers
* Texas Instruments compilers for ARM (`armcl` and `tiarmclang`), C2000, C6000, C7000, MSP430, and PRU
* Wind River Diab and GCC compilers
* Microchip MPLAB XC8, XC16, and XC32 Compilers
* Compilers based wholly on GCC, including Linaro GCC

#### Generating a compilation database <a href="#generating-a-compilation-database" id="generating-a-compilation-database"></a>

To analyze in Compilation Database mode, you need to be able to use one of two alternative ways to generate the compilation database:

* Sonar *Build Wrapper*
* Third-Party tools

**Choosing the right tool**

The general recommendation is to use Build Wrapper unless there is a compelling reason not to.

**Reasons to use Build Wrapper**

* Build Wrapper enforces running the build before the analysis, which ensures that the code is in good shape for analysis: the code is compilable, the configuration file is not outdated, and the generated source files are available during the analysis.
* The project build relies on environment variables, which can only be captured using *Build Wrapper*.
* Recommended and supported by Sonar

**Reasons to use third-party tools**

* When build-wrapper doesn’t work as expected with your build-system or environment. For example, recent versions of XCode
* You want to use a third-party tool that, unlike build-wrapper, does not require a clean build to generate a compilation database
* You already generate and use a reliable Compilation Database in your CI pipeline

**Using Build Wrapper**

Analysis configuration example projects with Build Wrapper are available on [GitHub](https://github.com/orgs/sonarsource-cfamily-examples/repositories?q=topic%3Abuild-wrapper+topic%3Asonarqube) for various compilers, build systems, and operating systems.

*Build Wrapper* is a tool developed by SonarSource that generates a compilation database, capturing your build configuration at build time. To run Build Wrapper, prepend your clean build command with the *Build Wrapper* executable.

When you wrap your build command with Build Wrapper, it will run the given command and gather all the configuration required for a correct analysis of C/C++/Objective-C projects, such as macro definitions and include directories. Build Wrapper does not impact your build; it merely monitors and writes what it learns into files in your specified directory.

Build Wrapper must be downloaded each time from SonarQube Cloud before executing it to ensure that the latest version is used:

* [Download Build Wrapper for Linux x86-64](https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip)
* [Download Build Wrapper for Linux aarch64](https://sonarcloud.io/static/cpp/build-wrapper-linux-aarch64.zip)
* [Download Build Wrapper for macOS](https://sonarcloud.io/static/cpp/build-wrapper-macosx-x86.zip)
* [Download Build Wrapper for Windows](https://sonarcloud.io/static/cpp/build-wrapper-win-x86.zip)

{% hint style="info" %}
If you’re using the [GitHub Action for SonarQube](https://github.com/marketplace/actions/official-sonarqube-scan) to perform the scan, use the `sonarqube-scan-action/install-build-wrapper` sub-action to install the Build Wrapper.
{% endhint %}

Unzip the downloaded Build Wrapper and configure it in your `PATH` because doing so is just more convenient.

Execute Build Wrapper as a prefix to your usual clean build command. A clean build command should always build the project from scratch. At the end of your build, a `compile_commands.json` file should be generated in the specified output directory. This file contains information about the compilation units that were built by your build command.

Any file that doesn’t end up in a compiled compilation unit will not be analyzed. As a consequence, source files that are not compiled and header files that are not included in any compiled source file will not be analyzed.

Executing build-wrapper doesn’t interfere with your build command. There is no need to build a second time without a build-wrapper. Just make one build and wrap it up.

Notes:

* Build Wrapper supports [ccache](https://ccache.dev/). This can be used to speed up clean builds by caching previous compilations and detecting when the same compilation is being done again. It is commonly used to compensate for the need for a clean build when using the build-wrapper.
* Build Wrapper does not support statically linked compilers on Linux and macOS, such as some versions of Texas Instruments compilers on Linux.

The examples below use make, xcodebuild, and MSBuild, but any build tool that performs a full build can be used:

<details>

<summary>Linux</summary>

* For Linux x86-64:

```bash
build-wrapper-linux-x86-64 --out-dir build_wrapper_output_directory make clean all
```

* For Linux aarch64:

```bash
build-wrapper-linux-aarch64 --out-dir build_wrapper_output_directory make clean all
```

</details>

<details>

<summary>macOS</summary>

```bash
build-wrapper-macosx-x86 --out-dir build_wrapper_output_directory xcodebuild clean build
```

</details>

<details>

<summary>Windows</summary>

```bash
build-wrapper-win-x86-64.exe --out-dir  build_wrapper_output_directory MSBuild.exe /t:Rebuild /nodeReuse:False
```

</details>

**Important notes**

* Build Wrapper collects information about the build, including absolute file paths (source files, standard headers, libraries, etc.). Later, SonarScanner CLI uses this information and needs to access those paths. While this is straightforward when running these two steps on the same host, it is worth considering when using any containerization. A consequence of this is that Compilation-Database based C/C++/Objective-C analysis is NOT supported by the [SonarScanner CLI Docker image](https://hub.docker.com/r/sonarsource/sonar-scanner-cli).
* Build Wrapper generates three files in its output directory: build-wrapper-dump.json, compile\_commands.json, and build-wrapper.log. All these files contain a dump of the environment, which can be a security concern in some contexts.

**Specifics of using Build Wrapper with Bazel**

[Bazel](https://www.bazel.build/) recommends that you use the [`--batch`](https://docs.bazel.build/versions/master/user-manual.html#flag--batch) parameter when running in a Continuous Build context. When using Build Wrapper, you are in such a context. Also, you need to deactivate Bazel’s ["sandbox"](https://bazel.build/docs/sandboxing) mechanism so that the compiled file paths can be retrieved after the compilation phase.

Here is an example of the Build Wrapper command with Bazel parameters on macOS:

```bash
build-wrapper-macosx-x86 --out-dir bw bazel
  --batch
  build
  --spawn_strategy=local
  --strategy=Genrule=local
  --bazelrc=/dev/null
  //main:hello-world
```

**Specifics of using build-wrapper with MSBuild**

Instead of starting new nodes when building your code, MsBuild can reuse previously launched build nodes. In that case, Build Wrapper cannot monitor files compiled on these nodes. Therefore, we advise turning off this feature using the [`nodeReuse:False`](https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-command-line-reference?view=vs-2022) command-line option.

**Using third-party tools**

Depending on your build system, some third-party options can be used to generate a compilation database.

<details>

<summary>Some examples</summary>

Some examples:

* [CMake](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html) by setting the option `CMAKE_EXPORT_COMPILE_COMMANDS`
* [Ninja](https://ninja-build.org/manual.html) by setting the `compdb` flag
* XCode through Clang’s `-gen-cdb-fragment-path` feature:

```properties
# Add the following "OTHER_CFLAGS" option to the xcodebuild command
xcodebuild clean build <additional args> OTHER_CFLAGS="\$(inherited) -gen-cdb-fragment-path \$(PROJECT_DIR)/CompilationDatabase"
# After the build, aggregate the fragments into "compile_commands.json"
cd CompilationDatabase && sed -e '1s/^/[\'$'\n''/' -e '$s/,$/\'$'\n'']/' *.json > ../compile_commands.json && cd ..
```

* Clang using the -MJ option. Note that this will generate a compilation database entry by input. The merge of all entries can be done through something like `sed -e '1s/^/[\'$'\n''/' -e '$s/,$/\'$'\n'']/' *.o.json > compile_commands.json`
* Open source wrappers like [Bear](https://github.com/rizsotto/Bear) and [Bazel compile commands extractor](https://github.com/hedronvision/bazel-compile-commands-extractor)

</details>

Analysis configuration example projects that generate compilation databases using third-party tools are available on [GitHub](https://github.com/orgs/sonarsource-cfamily-examples/repositories?q=topic%3Abuild-wrapper+topic%3Asonarqube).

**Important notes**

* Make sure that the tool you are using generates the right up-to-date compile commands. To do so, generate a compilation database before every analysis. Also, verify that the Compilation Database contains your actual build commands by running one of the compilation commands and ensuring that it succeeds.
* The environment where you execute the analysis should be the same as the build environment; the analyzer may need to access the build-related environment variables. For example, when using the Microsoft Visual C++ compiler, execute the analysis from the same Visual Studio Developer Command Prompt you use to build your project. The command prompt sets some environment variables, like `INCLUDE`, that must be set during the analysis.
