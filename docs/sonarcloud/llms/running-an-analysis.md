# Source: https://docs.sonarsource.com/sonarqube-for-eclipse/getting-started/running-an-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-for-visual-studio/getting-started/running-an-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-for-intellij/getting-started/running-an-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-for-vs-code/getting-started/running-an-analysis.md

# Running an analysis

Now that you’ve installed the SonarQube for IDE extension in your IDE, running an analysis is straight-forward. For the most part, new analyses are automatically triggered when you open a file, as you type, or with each file save following a change in the code. Below we’ve outlined other ways to trigger a SonarQube for IDE analysis.

### Triggering an analysis <a href="#triggering-an-analysis" id="triggering-an-analysis"></a>

First, open a project using one of the [rules](https://docs.sonarsource.com/sonarqube-for-vs-code/using/rules "mention"). Some languages can only be unlocked when running in [connected-mode](https://docs.sonarsource.com/sonarqube-for-vs-code/connect-your-ide/connected-mode "mention"). For C and C++, check the **Analyze C and C++ code** section below.

New analyses are automatically triggered in VS Code when you open or save a file; with Autosave configured, new issues will be reported as you type.

Check the [investigating-issues](https://docs.sonarsource.com/sonarqube-for-vs-code/using/investigating-issues "mention") page for details about how to recognize issues in your IDE.

### Enable or disable automatic analysis <a href="#enable-disable-automatic-analysis" id="enable-disable-automatic-analysis"></a>

It is possible to manually enable or disable automatic analysis. In the VS Code Status Bar, select **SonarQube** to toggle the setting. Alternatively, from the **SONARQUBE** panel, select the dual-arrow refresh icon to toggle automatic analysis.

### How it works <a href="#how-it-works" id="how-it-works"></a>

With Auto Save enabled in VS Code, SonarQube for IDE continuously analyzes the code while you type. Simply open any source file, start coding, and you will start seeing issues reported by SonarQube for IDE. Issues are highlighted in your code and also listed in the **PROBLEMS** panel.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-2940d6f2fe36f8359d3e5eac0373067fe295e6de%2Fsq-vscode-run-analysis.gif?alt=media" alt="To analyze a your code with SonarQube for VS Code, simply type. Any issues will be highlighted in the code editor and you will see a full list of issues in the PROBLEMS panel." width="375"><figcaption></figcaption></figure></div>

You can access the detailed rule description directly from your editor, using the provided contextual menu.

<div align="left"><figure><img src="https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2Fgit-blob-35330cef72d980e08d42a71e83282d89f203ef50%2F28bf231cb7e5e5daa5237bdcb57ccaf5159763d3.gif?alt=media" alt="Open a rule description in SonarQube for VS Code so that you can learn why this is an issue in your project." width="375"><figcaption></figcaption></figure></div>

### Analyze changed files

{% hint style="success" %}
This is a SonarQube for IDE Labs feature. Update your SonarQube for VS Code installation to version 4.37 or newer, then sign up for IDE Labs to get early access to our newest features and help shape the future of SonarQube for IDE!

Open the **SONARQUBE FOR IDE LABS** panel from the right side of your **SONARQUBE** panel.
{% endhint %}

Navigate to the **SOURCE CONTROL** > **Changes** view container and select the **Analyze Changed Files with SonarQube** (![](https://3457378997-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6LPRABg3ubAJhpfR5K0Y%2Fuploads%2FrIs3kGgS0QCI65aoPiJL%2Fsq-ide-black-play-icon.svg?alt=media\&token=4e9f810b-3419-4e1c-869b-f19332c6d10f)) icon to trigger an analysis on all files changed since the last commit to ensure fewer issues reach your remote repository. This is especially useful if automatic analysis is disabled for your development project. It can be your last check on changes you made before creating a pull request.

### Analyze C and C++ code <a href="#analyze-c-and-cpp-code" id="analyze-c-and-cpp-code"></a>

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

To analyze C and C++ code, you need to satisfy both of these conditions:

1. **Generate a compilation database** and
2. be on one of the **Supported environments**

See below for details.

#### Generate a compilation database <a href="#generate-a-compilation-database" id="generate-a-compilation-database"></a>

[Compilation database](https://clang.llvm.org/docs/JSONCompilationDatabase.html) is a JSON file format introduced by the LLVM project. It contains the compile commands used to build a project. For instructions on how to generate a compilation database, choose the appropriate collapsible below. The preferred option is to use the build system.

{% hint style="info" %}
The C and C++ ecosystem is diverse. This documentation provides a general overview of how to set up your environment under common circumstances. If you need more assistance than we can provide here, please check if the compilation database is a feature in your extension, search the [SonarQube for VS Code Community forum](https://community.sonarsource.com/c/sl/vs-code/36) for details about your build system, and reach out with questions if you have any troubles.
{% endhint %}

<details>

<summary>Using the build system</summary>

**Generate a compilation database using the build system**

Many build systems support the automatic generation of compilation databases. For example:

* CMake by simply setting this option `CMAKE_EXPORT_COMPILE_COMMANDS`
* VS Code [Makefile Tools](https://devblogs.microsoft.com/cppblog/makefile-tools-december-2021-update-problem-matchers-and-compilation-database-generation/) extension
* Ninja by setting the `compdb` flag
* Xcode through Clang’s `-gen-cdb-fragment-path` feature:

```css-79elbk
# Add the following "OTHER_CFLAGS" option to the xcodebuild command
xcodebuild clean build <additional args> OTHER_CFLAGS="\$(inherited) -gen-cdb-fragment-path \$(PROJECT_DIR)/CompilationDatabase"
# After the build, aggregate the fragments into "compile_commands.json"
cd CompilationDatabase && sed -e '1s/^/[\'$'\n''/' -e '$s/,$/\'$'\n'']/' *.json > ../compile_commands.json && cd ..
```

* Clang using the -MJ option. Note that this will generate a compilation database entry by input. The merge of all entries can be done through something like `sed -e '1s/^/[\'$'\n''/' -e '$s/,$/\'$'\n'']/' *.o.json > compile_commands.json`

When different choices are available, generating a compilation database through the build system should be preferred.

</details>

<details>

<summary>Using Sonar’s Build Wrapper</summary>

Build Wrapper is a tool developed by Sonar that generates a compilation database, capturing your build configuration at build time. To run Build Wrapper, you should prepend your clean build command with the Build Wrapper executable.

When you wrap your build command with the build wrapper, it will run the given command and gather all the configuration required for a correct analysis of C/C++/Objective-C projects such as macro definitions and include directories. The Build Wrapper does not impact your build; it merely monitors it and writes what it learns into files in a directory you specify. There is no need to build a second time without Build Wrapper.

You should download the build wrapper directly from SonarQube Cloud:

* [Download Build Wrapper for Linux](https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip)
* [Download Build Wrapper for macOS](https://sonarcloud.io/static/cpp/build-wrapper-macosx-x86.zip)
* [Download Build Wrapper for Windows](https://sonarcloud.io/static/cpp/build-wrapper-win-x86.zip)

Unzip the downloaded build wrapper and configure it in your PATH because doing so is just more convenient.

Execute build wrapper as a prefix to your usual clean build command. A clean build command should always build the project from scratch.

The examples below use `make`, `xcodebuild` and `MSBuild`, but any build tool that performs a full build can be used:

**Linux**

```bash
build-wrapper-linux-x86-64 --out-dir build_wrapper_output_directory make clean all
```

**macOS**

```bash
build-wrapper-macosx-x86 --out-dir build_wrapper_output_directory xcodebuild clean build
```

**Windows**

```bash
build-wrapper-win-x86-64.exe --out-dir  build_wrapper_output_directory MSBuild.exe /t:Rebuild /nodeReuse:False
```

At the end of your build, a `compile_commands.json` file should be generated in the specified output directory.

{% hint style="warning" %}
All the files generated by Build Wrapper in the output directory contain a dump of the environment. Sharing these files, in some contexts, can be a security concern.
{% endhint %}

</details>

<details>

<summary>Using open-source wrappers</summary>

**Generate a compilation database using open-source wrappers**

In case the above options are not successful in generating a compilation database, some open-source wrappers can help. For example:

* [Bear](https://github.com/rizsotto/Bear)
* [Bazel compile commands extractor](https://github.com/hedronvision/bazel-compile-commands-extractor)

</details>

<details>

<summary>Using a custom script</summary>

**Generate a compilation database using a custom script**

A compilation database is simply a JSON file that describes how to compile a project. If none of the previous approaches are feasible, for example, in the case of an *internal build system*, writing a script that generates a compilation database to describe how source files are supposed to be compiled might be the best solution.

**Best practices**

* Make sure that the compilation database contains the actual compile commands. This can be checked by running the compilation commands inside the `compile_commands.json` and verifying that they succeed.
* The compilation database should not contain header files entries. We use internal heuristics to analyze header files
* Make sure that the compilation database is up to date. It should be refreshed as part of the development cycle.

If you don’t use the Build Wrapper to generate a compilation database and the build relies on environment variables, make sure that they are set in the VS Code environment.

</details>

<details>

<summary>General recommendations</summary>

**Best practices**

* Make sure that the compilation database contains the actual compile commands. This can be checked by running the compilation commands inside the `compile_commands.json` and verifying that they succeed
* Make sure that the compilation database is up to date. It should be refreshed as part of the development cycle
* If the build system uses environment variables, make sure that they are set in the VS Code environment
* The compilation database should not contain header files entries. We use internal heuristics to analyze header files

</details>

#### Supported environments <a href="#supported-environments" id="supported-environments"></a>

<details>

<summary>Compilers</summary>

**Supported compilers**

* Any version of Clang, GCC, and Microsoft C/C++ compilers
* Any version of Intel compiler for Linux and macOS
* ARM5 and ARM6 compilers
* IAR compilers for ARM, Atmel AVR32, Atmel AVR, Renesas H8, Renesas RL78, Renesas RX, Renesas V850, Texas Instruments MSP430, and 8051
* QNX compilers
* Texas Instruments compilers on Windows and macOS for ARM, C2000, C6000, C7000, MSP430, and PRU
* Wind River Diab and GCC compilers
* Compilers based wholly on GCC, including, for instance, Linaro GCC, are also supported

</details>

<details>

<summary>Language standards</summary>

**Supported language standards**

C standards: C89, C99, C11, C17

C++ standards: C++03, C++11, C++14, C++17, C++20 and C++23.

GNU extensions

</details>

<details>

<summary>Runtime environments</summary>

**Supported runtime environments**

* Microsoft Windows on x86-64
* Linux on x86-64
* macOS with version 10.14.3 and later on x86-64

</details>

### Activating C and C++ Analysis <a href="#activating-c-and-cpp-analysis" id="activating-c-and-cpp-analysis"></a>

The analysis can be activated by simply pointing to a compilation database that describes the project to be analyzed. This can be done through a notification that pops up when a folder that contains a file named `compile_commands.json` is opened, or through the SonarQube for VS Code embedded action that lists all compilation database files in the folder, or by manually assigning the `sonarlint.pathToCompileCommands` option in the settings to the full path of the compilation database.

Note that the SonarQube for IDE embedded action can be used to switch the active compilation database.

### Troubleshooting C and C++ Analysis <a href="#troubleshooting-c-and-cpp-analysis" id="troubleshooting-c-and-cpp-analysis"></a>

In case the analysis is not working or obvious false positives are raised, here are the recommended actions in order:

1\. **Investigate the logs**:

* First, enable the `Verbose Logs` and look if there is any error or failures that indicate what went wrong.
* Check the [troubleshooting](https://docs.sonarsource.com/sonarqube-for-vs-code/resources/troubleshooting "mention") page for instructions to enable these logs.

2\. **Make sure that the compilation database is credible**:

* Check that the compilation database is up to date. It shouldn’t contain outdated commands or point to files that no longer exist.
* Make sure that the compilation database contains the actual compilation commands. This can be done by running the `commands` inside the `compile_commands.json` and verifying that they succeed.
* Make sure that the VS Code environment has the environment variables required to build the project.

3\. **Enable Rule \`S2260\`**:

* In case of obvious false positives in the raised issues, enable the [`cpp:S2260`](https://rules.sonarsource.com/cpp/RSPEC-2260/) or [`c:S2260`](https://rules.sonarsource.com/c/RSPEC-2260/) rule and check if it raises issues in the culprit file. This rule indicates that the analyzer failed to parse part of the code and might give hints or indicate a configuration problem.
* If it raises issues, follow the rule description to fix your code; if not, move to the step in troubleshooting.

4\. **Generate the CFamily reproducer File and Report the Issue**:

* When none of the previous suggestions work, please report the problem you encountered in the [Sonar community](https://community.sonarsource.com/).
* In case of a false positive or an analysis failure, we need the CFamily reproducer file to investigate the issue. To generate the reproducer file, add the following analyzer option to the `settings.json`:
  * `"sonarlint.analyzerProperties": {"sonar.cfamily.reproducer" : "C:\\replace\\by\\path\\to\\file.cpp"}`
* The `sonar.cfamily.reproducer` should point to the source or header file on which you face the issue. After setting that option, trigger the analysis on the culprit file. You should see in the logs that a file name `sonar-cfamily.reproducer` is generated in a temporary directory. Upload that file in your community report or ask us to share it privately if it contains sensitive information.
