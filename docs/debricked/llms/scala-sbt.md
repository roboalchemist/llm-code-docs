# Source: https://docs.debricked.com/overview/language-support/scala-sbt.md

# Scala - SBT

OpenText Core SCA now supports tracking Scala dependencies through the following methods:

* SBT, by utilizing *pom.xml* files
* [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting), to find dependencies not specified in manifest files

### SBT

OpenText Core SCA does not directly support scanning *build.sbt* files. However, SBT provides commands to generate a corresponding pom.xml file. This *pom.xml* file can be used to create a lock file, which allows OpenText Core SCA to analyze the complete list of direct and indirect dependencies along with their relationships.

You can do this using the High-Performance Scans technology available in [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli). By running the *resolve* command, the CLI will automatically detect any *build.sbt* files and use them to generate the needed maven dependency files. This is also run by default within the *scan* command.

You can manually create the recommended file(s) by running the following commands and saving the output into a *maven.debricked.lock* file.

```
// sbt makePomSome code
mv target/scala-*/*.pom pom.xml
mvn dependency:tree -DoutputFile=maven.debricked.lock -DoutputType=tgf
```

{% hint style="info" %}
Every *maven.debricked.lock* file should be placed in the same directory as the corresponding *pom.xml* file.
{% endhint %}

### File fingerprinting

OpenText Core SCA offers the capability to scan for Scala dependencies that are not specified in manifest files through file fingerprinting. The OpenText Core SCA database includes the hashes of .jar and .war files, along with their unpacked contents, for all packages in the largest Maven repository. This information is used to compare with the contents of your application, ensuring the most accurate matches possible.

*For more information on file fingerprinting and how to set it up, see* [*file fingerprinting*](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting)*.*

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th>Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th>High Performance Scan</th></tr></thead><tbody><tr><td>SBT</td><td><em>build.sbt</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>No</td><td>false</td><td>Yes</td></tr></tbody></table>
