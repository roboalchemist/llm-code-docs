# Source: https://docs.debricked.com/overview/language-support/java-and-kotlin-gradle-maven-bazel.md

# Java & Kotlin - Gradle, Maven, Bazel

OpenText Core SCA currently supports tracking Java or Kotlin dependencies using:

* Gradle (using *build.gradle* and *build.gradle.kts* files)
* Maven (using *pom.xml* files)
* Bazel (using *WORKSPACE* and *install.json* files)
* [File fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting) to detect dependencies not specified in manifest files

### **Gradle**

To achieve the fastest and most accurate results, create a file containing the resolved dependency tree named *.gradle.debricked.lock* before scanning.

This can be accomplished using the [High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) technology in [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli). If you execute the *resolve* command, the CLI automatically identifies all manifest files that lack the recommended Gradle lock files and generates them as needed.

You can create the recommended file(s) manually by running the *Gradle dependencies* command and saving the output in a *gradle.debricked.lock* file.

```bash
gradle dependencies > gradle.debricked.lock
```

Every *gradle.debricked.lock* file should be placed in the same directory as its corresponding *build.gradle* or *build.gradle.kts* file.

### **Maven**

To achieve the fastest and most accurate results, create a file containing the resolved dependency tree named *.maven.debricked.lock* before scanning.

This can be accomplished using the [High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) technology in our [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli). If you execute the *resolve* command, the CLI automatically identifies all manifest files that lack the recommended maven lock files and generates them as needed.

You can manually generate the recommended file(s) by running the **Maven dependency:tree** plugin and saving the output to a *maven.debricked.lock* file.

```bash
mvn dependency:tree -DoutputFile=maven.debricked.lock -DoutputType=tgf
```

Every *maven.debricked.lock* file should be placed in the same directory as the corresponding *pom.xml* file.

### **Bazel**

OpenText Core SCA supports Java projects that utilize Bazel by scanning the *WORKSPACE* file format along with any Java file formats in use. To ensure fast and accurate scans, OpenText Core SCA recommends utilizing *rules\_jvm\_external* to generate an *install.json* file, which resolves and pins all indirect dependencies in a lock file.&#x20;

For more information on setting this up in your project, see [Bazel blog](https://blog.bazel.build/2019/03/31/rules-jvm-external-maven.html).

### File fingerprinting

OpenText Core SCA supports scanning for Java dependencies not defined in manifest-files through **file fingerprinting.** Our database contains the hashes of *.jar* and *.war* files as well as their unpacked contents for all packages in the largest maven repository. This is used when comparing with the contents of your application, to ensure as accurate matches as possible.&#x20;

For more information on file fingerprinting and how to set it up, see [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting).

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th data-type="checkbox">High Performance Scan</th></tr></thead><tbody><tr><td>Gradle</td><td><em>build.gradle</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td></tr><tr><td>Gradle</td><td><em>build.gradle.kts</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td></tr><tr><td>Maven</td><td><em>pom.xml</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td></tr><tr><td>Bazel</td><td><em>WORKSPACE</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>true</td><td>false</td></tr><tr><td>Bazel</td><td><em>install.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>true</td><td>false</td></tr><tr><td>-</td><td>fingerprinted files (.jar, .war, pom.xml and more*)</td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>false</td></tr></tbody></table>

\*When building the knowledge base, the files are downloaded, unpacked and fingerprints are created for all file contents, except for certain excluded patterns. The fingerprints are created for the contents of each file. For example, OpenText Core SCA matches *.dll* files used in C# and *.class* files found within *.jar* files from Java, among others.
