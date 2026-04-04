# Source: https://docs.debricked.com/overview/language-support/javascript-npm-yarn-bower.md

# JavaScript - NPM, Yarn, Bower, pnpm

OpenText Core SCA now tracks JavaScript and TypeScript dependencies through:

* NPM (using *package.json* and *package-lock.json* files)
* Yarn (using *package.json* and *yarn.lock* files)
* Bower (using *bower.json* files)
* pnpm ((using *package.json* and *pnpm-lock.yaml* files)
* [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting) to detect dependencies not specified in manifest files

OpenText Core SCA recommends committing the *lock* files to achieve the most accurate tracking, as these files include the specific resolved versions of both direct and indirect dependencies. If you only commit the *package.json* file, OpenText Core SCA will update all dependencies to the latest available versions based on the specified version constraints.

If at least one supported file is committed to the repository, it will automatically be scanned for dependencies when you integrate with the CI/CD pipeline.

### Bower

To achieve the fastest and most accurate results, create a file containing the resolved dependency tree before scanning. This can be accomplished using the [High Performance Scans](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) technology in [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli). By executing the *resolve* command, the CLI automatically identifies all manifest files that lack the recommended *bower.debricked.lock* files and generates them as needed.

### File fingerprinting

OpenText Core SCA supports scanning for JavaScript dependencies not defined in manifest-files through **file fingerprinting.** The database contains the hashes of relevant files (including .js and .ts files) for all packages in the npm registry. This is used when comparing with the contents of your application, to ensure as accurate matches as possible.&#x20;

For more information on file fingerprinting and how to set it up, see [file fingerprinting](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting).

### **Supported file formats and features**

<table data-full-width="true"><thead><tr><th>Package manager</th><th>Supported file formats</th><th data-type="checkbox">Root dependencies </th><th data-type="checkbox">Indirect dependencies</th><th data-type="checkbox">Dependency trees</th><th data-type="checkbox">Security scanning</th><th data-type="checkbox">License scanning</th><th data-type="checkbox">Root fix</th><th data-type="checkbox">Pull Request</th><th data-type="checkbox">Reachability Analysis</th><th>High Performance Scan</th></tr></thead><tbody><tr><td>NPM</td><td><em>package.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>Yes</td></tr><tr><td>NPM</td><td><em>package.lock.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>Yes*</td></tr><tr><td>Yarn</td><td><em>package.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>Yes</td></tr><tr><td>Yarn</td><td><em>yarn.lock</em> </td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>Yes*</td></tr><tr><td>Bower</td><td><em>bower.json</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>Yes</td></tr><tr><td>pnpm</td><td><em>package.json (using the attribute</em> <code>packageManager</code>)</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>Yes</td></tr><tr><td>pnpm</td><td><em>pnpm-lock.yaml</em></td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>true</td><td>false</td><td>Yes*</td></tr><tr><td>-</td><td>fingerprinted files (.js, .ts and more**)</td><td>true</td><td>true</td><td>false</td><td>true</td><td>true</td><td>false</td><td>false</td><td>false</td><td>-</td></tr></tbody></table>

**\***&#x54;his is a native lock file format. Native lock file formats are the fastest formats to scan.
