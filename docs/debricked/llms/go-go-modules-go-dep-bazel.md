# Source: https://docs.debricked.com/overview/language-support/go-go-modules-go-dep-bazel.md

# Go - Go Modules, Go Dep, Bazel

OpenText Core SCA supports tracking Go dependencies through:

* Go Modules, using *go.mod* files
* Go Dep, using *gopkg.lok* files
* Bazel, using *WORKSPACE* files

### **Go Modules**

OpenText Core SCA supports tracking Go dependencies using the Go Modules dependency management system and its associated go.mod file. To achieve the fastest and most accurate results, it is necessary to create a file containing the resolved dependency tree, *.gomod.debricked.lock*, before scanning.

This can be done using the [High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) technology in [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli). If you execute the *resolve* command, the CLI automatically identifies all manifest files that lack the recommended *go.lock* files and generates them as needed.

You can manually generate the recommended file(s) by running *go mod graph* followed by *go list -m all*, and storing the outputs separated by two new lines between the sections in the *gomod.debricked.lock* file.

```bash
printf "$(go mod graph)\n\n$(go list -mod=readonly -e -m all)" > gomod.debricked.lock
```

Every *gomod.debricked.lock* must be put in the same directory as the corresponding *go.mod.*&#x20;

OpenText Core SCA recommends running *go mod tidy* to clean up unused modules before pushing the *go.mod* files, ensuring more accurate service results.

### **Bazel**

OpenText Core SCA supports Go projects that utilize Bazel, scanning the *WORKSPACE* file format alongside any *Go* file formats in use. Although Bazel does not have native support for Go, support can be added using [Gazelle](https://github.com/bazelbuild/bazel-gazelle).

### **Go Dep**

Go Dep and its associated file *Gopkg.lock* is deprecated and will not get any improvements present in other formats, such as Go Modules.

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th>High Performance Scan</th></tr></thead><tbody><tr><td>Bazel</td><td><em>WORKSPACE</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>-</td></tr><tr><td>Bazel</td><td><em>install.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>Yes*</td></tr><tr><td>Go Modules</td><td><em>go.mod</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>Yes</td></tr><tr><td>Go Dep</td><td><em>gopkg.lock</em></td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes*</td></tr></tbody></table>

**\***&#x54;his is a native lock file format. Native lock file formats are the fastest formats to scan.
