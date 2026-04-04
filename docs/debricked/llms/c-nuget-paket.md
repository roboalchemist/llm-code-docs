# Source: https://docs.debricked.com/overview/language-support/c-nuget-paket.md

# C# - Nuget, Paket

OpenText Core SCA currently supports the tracking of C# dependencies through:

* [NuGet](https://www.nuget.org/), using *.csproj*, *packages.lock.json* and *packages.config* files
* [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting), to find dependencies not defined in manifest-files
* Paket, using *paket.lock* file

If there is a modern NuGet project where dependencies are defined in *.csproj* files, OpenText Core SCA recommends using the *packages.lock.json* file. This file allows OpenText Core SCA to analyze the dependency tree and suggest root fixes. By default, NuGet does not generate this file, but you can create it using the [High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) technology with the OpenText Core SCA CLI or by enabling [repeatable package restores](https://devblogs.microsoft.com/nuget/enable-repeatable-package-restores-using-a-lock-file/) and then committing the generated file. When you run the resolve command, the OpenText Core SCA CLI automatically detects all manifest files that lack the recommended lock files and generates them as needed.

In older NuGet projects, dependencies are typically stored in a *packages.config* ile. OpenText Core SCA recommends that users generate the necessary lock file for dependency management and root fixes using High Performance Scans with the Debricked CLI. The command *debricked resolve* will create a *packages.lock.json* style file by first translating the *packages.config* into a `.csproj` file using NuGet. From there, the lock file is generated. Once the process is complete, the *.csproj* file is deleted, leaving only the newly created lock file. To avoid potential conflicts with NuGet, the specially created NuGet lock file is named as *packages.config.nuget.debricked.lock.*

By default, in all integrations except the GitHub app, the *Debricked* scan command will automatically try to generate the necessary lock files before sending your dependency files for scanning.

OpenText Core SCA also supports sending only *.csproj* or *packages.config* files for scanning, but the *packages.lock.json* or *packages.config.nuget.debricked.lock* file is preferred, as it provides the most accurate tracking of dependency versions and trees, enabling root fixes.

[High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) for NuGet utilize native commands when resolving and include all dependencies defined with NuGet, including those managed through [Central Package Management (CPM)](https://learn.microsoft.com/en-us/nuget/consume-packages/central-package-management).

If at least one of the supported files is committed to your repository, it will be automatically scanned for dependencies when you have done any of our integrations to your CI/CD pipeline.

### File fingerprinting

OpenText Core SCA supports scanning for C# dependencies not defined in manifest files through **file fingerprinting.** OpenText Core SCA database contains the hashes of *.nupkg* files as well as their unpacked contents (including .dll files) for all packages in the NuGet gallery. This is used when comparing with the contents of your application, to ensure as accurate matches as possible. For more information on file fingerprinting and how to set it up, see [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting).

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th>High Performance Scan</th></tr></thead><tbody><tr><td>Nuget</td><td><em>.csproj</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>Yes</td></tr><tr><td>Nuget</td><td><em>package.lock.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>Yes*</td></tr><tr><td>Nuget</td><td><em>packages.config</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes</td></tr><tr><td>Paket</td><td><em>paket.lock</em></td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes*</td></tr><tr><td>-</td><td>fingerprinted files<br>(.dll, .nupkg and more**)</td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>-</td></tr></tbody></table>

\*This is a native lock file format. Native lock file formats are the fastest formats to scan.

\*\*When building the knowledge base, the files are downloaded, unpacked and fingerprints are created for all file contents, except for certain excluded patterns. The fingerprints are created for the contents of each file. For example, Debricked matches *.dll* files for C# and *.class* files within *.jar* files for Java, along with similar files from other programming languages.&#x20;
