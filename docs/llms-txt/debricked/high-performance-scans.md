# Source: https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans.md

# High performance scans

{% hint style="info" %}
High Performance Scans are currently available for **Maven** (pom.xml), **Gradle** (build.gradle), **Go modules** (go.mod), **Pip** (requirements.txt), **NuGet** (.csproj and packages.config), **yarn** (package.json), and **composer** (composer.json).&#x20;
{% endhint %}

Some package managers do not have native support for maintaining lock files with complete information on dependency versions and relations. In order to guarantee fast and accurate scans for these package managers, it is necessary to first generate this information into a file before sending it to OpenText Core SCA for scanning. Doing this also ensures that private dependencies are included in the scans and eliminates the need to send source code for a complete scan, since all information will be included in the generated file.

At **OpenText Core SCA**, the **High Performance Scans** solution makes this process as simple as possible. This technology enables you to accurately and quickly resolve full dependency trees for repositories that don't have a lock file present. By using the lock file resolution technology to generate the needed files before sending them to the **OpenText Core SCA** tool, all the drawbacks that come with trying to generate the files on our end are removed.

With High Performance Scans, you can generate **OpenText Core SCA** lock files on your end, without us having to handle any of your source code. This approach improves the performance of the scans, especially when built into an existing pipeline that already builds the project. It also enables us to parse more accurate dependency results and obtain the relations of private dependencies without accessing anything other than the dependency files to scan your repository. Furthermore, it allows us to handle files of much bigger size.

The High Performance Scanning is highly customizable, allowing you to set it up to run in conjunction with a scan or in any other part of your pipeline.

### Generate OpenText Core SCA lock(tree) files using high performance scans

The **High Performance Scans** technology is available through the [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli) by using the `resolve` command. This command analyses your project to find eligible manifest files, that do not have related lock files and uses them to generate the appropriate OpenText Core SCA lock files. When conducting a scan using the scan command, the feature is enabled by default. It can be disabled by using the `--no-resolve` flag. Additionally, this technology is available through [CI templates](https://github.com/debricked/cli/tree/main/examples/templates), which have been reworked using the new command to be as simple as possible. This is built with customizability in mind, to suit many different use-cases. You might, for example, want to generate the lock files using the *resolve* command in a build step in your pipeline, separate from the scan step, since it will save time not having to build the project twice. When doing this, it is important to ensure that the files resulting from the resolve command are included in the stage where the scan is run.

### Speed up OpenText Core SCA lock file resolution <a href="#howtospeedupthedebrickedlockfileresolution" id="howtospeedupthedebrickedlockfileresolution"></a>

The best approach for speeding up the generation of **OpenText Core SCA** lock files is to make sure that the dependencies that are used for building the project are cached on the system that OpenText Core SCA CLI operates on. By doing so, OpenText Core SCA CLI can utilize these locally installed dependencies instead of having to download them from the registries, which is a time-consuming task. Package managers cache their dependencies differently, so if you set up dependency caching for your package manager, OpenText Core SCA CLI will be able to utilize that out of the box and in the process make the OpenText Core SCA lock file resolution snappier.

#### **Example:**

Maven is a commonly used build automation tool (and package manager) in the Java world. When Maven downloads dependencies for a project the dependencies are by default cached in the directory `~/.m2/repository`. If OpenText Core SCA CLI is used to resolve a Maven project on this system, instead of downloading dependencies, the `~/.m2/repository` directory is first checked and if the currently processed dependency is already downloaded it will be reused.

### Error handling <a href="#errorhandling" id="errorhandling"></a>

The resolution feature utilizes package managers to create OpenText Core SCA lock files, which works smoothly for simpler projects. For more complex projects, there might be certain project requirements that the OpenText Core SCA CLI cannot interpret.

To account for that, the resolution feature is built to be as transparent as possible, showing you what went wrong, in order to assist in solving the issue. An example of such an error is when privately hosted dependencies are built into the project - if OpenText Core SCA CLI cannot resolve these private dependencies the error given by the package manager will be displayed for you.
