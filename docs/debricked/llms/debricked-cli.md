# Source: https://docs.debricked.com/tools-and-integrations/cli/debricked-cli.md

# OpenText Core SCA CLI

### Introduction

The OpenText Core SCA CLI is OpenText Core SCA's command line interface, bringing open-source security, and license compliance to your project via the command prompt.

**The OpenText Core SCA CLI is currently available for:** Windows, Linux, and macOS operating systems. It might work on other operating systems but has not been thoroughly tested yet.\
**Supported languages:** Javascript, Java, C#, Ruby, PHP, and [more](https://docs.debricked.com/overview/language-support).

**Supported package managers:** Yarn, Npm, Bowel, Bazel, Gradle, and [more](https://docs.debricked.com/overview/language-support).

### Mastering OpenText Core SCA's CLI and API - webinar recording

Check out our latest training webinar and learn the basics of working with OpenText Core SCA CLI and API:

{% embed url="<https://www.youtube.com/watch?v=3fEOTOwHGbM>" %}

### 1. Getting started <a href="#gettingstarted" id="gettingstarted"></a>

To use the OpenText Core SCA CLI, you must have a [OpenText Core SCA account](https://docs.debricked.com/overview/getting-started/create-a-debricked-account) and install the CLI.

The CLI can be run:

* locally in your terminal as an interactive shell
* in your CI/CD pipeline
* through docker

#### 1.1 Authentication <a href="#id-1.authentication" id="id-1.authentication"></a>

You can authenticate with OpenText Core SCA either through an access token (recommended for CI/CD integrations), or by using the `debricked auth` command to log into the UI (recommended for scanning local projects). To create an access token, log in to OpenText Core SCA and follow the steps to [generate an access token](https://docs.debricked.com/product/administration/generate-access-token). Make sure to keep the access token in a safe place for later use.&#x20;

### 2. Installation <a href="#id-2.installation" id="id-2.installation"></a>

The CLI can be installed and used through:

1. Local installations:\
   \- Standalone\
   \- Installation using Go
2. Adding the CLI into your CI/CD pipeline
3. Using a docker image

If you run into any issues during the installation process, feel free to [contact us](https://docs.debricked.com/overview/help).

#### 2.1 Local installation <a href="#id-2.1localinstallation" id="id-2.1localinstallation"></a>

**2.1.1 Standalone**

[Find the latest GitHub releases to download a standalone executable here](https://github.com/debricked/cli/releases).

**Command Example for Linux:**

```bash
curl -L https://github.com/debricked/cli/releases/latest/download/cli_linux_x86_64.tar.gz | tar -xz debricked
```

**Command Example for Windows:**

```bash
curl -L https://github.com/debricked/cli/releases/latest/download/cli_windows_x86_64.tar.gz | tar -xz debricked.exe
```

**Command Example for MacOS:**

```bash
curl -L https://github.com/debricked/cli/releases/latest/download/cli_macOS_arm64.tar.gz | tar -xz debricked
```

**2.1.2 Installation Using Go**

**Requirements:**

Local compilation of OpenText Core SCA CLI requires Go to be installed on your system. In order to check whether you already have the compiler installed on your device, run the command ‘*go version*’ on your terminal. If there is no command available, [install the Go compiler.](https://go.dev/doc/install)

**Installation**:

1. Install Go on your operating system following [the official documentation](https://go.dev/doc/install)
2. Clone the CLI repository to your local directory: <https://github.com/debricked/cli>

#### 2.2 Adding CLI to your CI or CD pipeline <a href="#id-2.2addingthecli-toyourci-cdpipeline" id="id-2.2addingthecli-toyourci-cdpipeline"></a>

The CLI can be integrated into your continuous integration (CI) to run scans on the pipeline. You can integrate using:

* Docker image
* Binary standalone

**2.2.1 Using docker OpenText Core SCA or CLI image**

1. Log in to debricked.com/app and follow the steps to [generate an access token.](https://docs.debricked.com/product/administration/generate-access-token)
2. Set your access token, named `DEBRICKED_TOKEN`, as an environment variable within your continuous integration (CI). If you don’t know how to configure your environment variable, check our documentation for the most common [CI integrations](https://docs.debricked.com/tools-and-integrations/integrations).
3. Configure a new job in your CI pipeline::

* `debricked/cli:2-resolution-debian` docker image
* Run `debricked scan`
* Add the `DEBRICKED_TOKEN` as a variable or (if possible) as a secret

See the example below for the GitHub actions integration (see the [debricked.yml](https://github.com/debricked/cli/blob/main/examples/templates/GitHub/debricked.yml) file):

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/examples/templates/GitHub/debricked.yml>" %}

For more details, please check our sample templates for the integration of your choice.

**2.2.2 Using standalone**

1. Log in to debricked.com/app and follow the steps to [generate an access token](https://docs.debricked.com/product/administration/generate-access-token).
2. Set your access token, named `DEBRICKED_TOKEN`, as an environment variable within your continuous integration (CI). If you don’t know how to configure your environment variable, visit our documentation for the most common [CI integrations](https://docs.debricked.com/tools-and-integrations/integrations).
3. Configure a new job in your CI pipeline::

* Run:

  ```bash
  curl -L https://github.com/debricked/cli/releases/latest/download/cli_linux_x86_64.tar.gz | tar -xz debricked
  ```

  to use the executable Debricked CLI.
* Run `debricked scan`.

Here’s an example of the Circle CI integration: [circleci](https://github.com/debricked/cli/blob/main/examples/templates/CircleCI/config.yml)[/config.yml file](https://github.com/debricked/cli/blob/main/examples/templates/CircleCI/config.yml). For more examples check out: <https://github.com/debricked/cli/tree/main/examples/templates>

```
jobs:
  build:
    docker:
      # specify the version here
      - image: cimg/go:1.17

    steps:
      - checkout
      - run: |
          printf "$(go mod graph)\n\n$(go list -mod=readonly -e -m all)" > .debricked-go-dependencies.txt
      # It is important that the generated dependency tree files are persisted and attached to the following scan step
      - persist_to_workspace:
          root: ~/repo
          paths:
            - '**.debricked-go-dependencies.txt'
            # Make sure to add all generated .debricked-go-dependencies.txt files

  scan:
    docker:
      - image: cimg/go:1.17
    working_directory: ~/repo
    steps:
      - checkout
      - run: curl -L https://github.com/debricked/cli/releases/latest/download/cli_linux_x86_64.tar.gz | tar -xz debricked
      - run: ./debricked scan

workflows:
  debricked-scan:
    jobs:
      - build
      - scan:
          requires:
            - build
```

### 3. Testing your installation <a href="#id-3.testyourinstallation" id="id-3.testyourinstallation"></a>

To confirm whether the installation was successful, run the command *‘./debricked --help’*. If you can see the menu as seen below, you are ready to scan your first project!

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FXJrCKL5UIV7hdfnXTpdi%2FCLI_Installation.png?alt=media&#x26;token=f427ac54-28b9-4a22-bdd5-a80659912029" alt=""><figcaption></figcaption></figure>

### 4. Scan your first project <a href="#id-4.scanyourfirstproject" id="id-4.scanyourfirstproject"></a>

Once you've installed the CLI, you're ready to scan your project. You can scan a local project allocated on your local machine or a project in a remote repository via a CI integration, follow the instructions below to perform your first scan:

1. Authenticate CLI with either access token or through the `debricked auth` command.
2. Run `debricked scan --help` to see the main menu and check if the CLI is running
3. Scan your project locally using the command: *`debricked scan [path] [options]`*

The *`path`* is the folder that contains your project's dependency file. See this practical example, scanning a local project:

```
debricked auth login
```

```
debricked scan ~/Desktop/myproject/EasyApp 
```

The `debricked auth login` command authenticates directly through the UI and is therefore suitable for scanning local projects.

The `path` is the *`~/Desktop/myproject/EasyApp`*. Since EasyApp is a git repository, no other flags are needed for the scan.

Include some \[option]s within your scan:

```
debricked scan ~/Desktop/myproject/EasyApp --commit "044bdc7c22e46be010969e9360dbe679830100f1" --branch "dev"  --exclusion "**/test/**"
```

The commit `--commit` specifies the hash commit, and the branch with the command `--branch`. Note that `--commit` and `--branch` are only required when the target path does not contain a git repository.

Another option is to change the directory to a folder that contains your project's dependency file. So, you can use "." For example:

```
debricked scan . --access-token <token>
```

As shown above, you can also use an access token while scanning, which is recommended for CI/CD integrations.

After the scan is complete, you will see the total number of vulnerabilities found and a list of automation rules that have been evaluated.&#x20;

You can [log in ](https://debricked.com/app/en/login)to the OpenText Core SCA web tool to see the scan results, by following the link with all the details.

### 5. List of commands <a href="#id-5.listofcommands" id="id-5.listofcommands"></a>

These are the main commands for the OpenText Core SCA CLI:

| Command                                                 | Description                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------- |
| help                                                    | Display options.                                            |
| scan \[path] \[access-token] \[flags]                   | Upload and check your dependency files for vulnerabilities. |
| resolve \[path] \[flags]                                | Resolve manifest files.                                     |
| files find \[path] \[access-token] \[flags]             | Search and print the dependency files.                      |
| <p>export \[command]</p><p>\[access-token] \[flags]</p> | Generate an export and send it by email.                    |
| callgraph \[path] \[flags]                              | Generate a static callgraph for a project.                  |
| fingerprint \[\[path] \[flags]]                         | Fingerprint files.                                          |
| auth \[command]                                         | Authenticate to OpenText Core SCA service.                  |

#### help <a href="#help" id="help"></a>

* `debricked [command] --help`

Type `debricked –-help` to display the main menu.

To display the options on any command just execute the \[command], followed by the `--help` option. For example, type `debricked scan -–help` to list the options for the scan command.

#### scan <a href="#scan" id="scan"></a>

* `debricked scan [path] [flags]`
* `debricked scan –-help` to see all the options.

The scan command uploads and check your dependency files for open-source vulnerabilities and license compliance.

Path:

* Use the path argument to specify which directory the dependency file is in, or to exclude it. For example: `debricked scan ~/Desktop/Coder-2022/Eccomerce2/ -t <token>`.
* Use the path to specify where the dependency file is allocated, you can use "." to search the current working directory. For instance: `debricked files find . -t <token>` or `debricked files find ~/Desktop/Coder-2022/Eccomerce2/ -t <token>`

Flags:

`-t --access-token` <mark style="background-color:red;">Required</mark>

Use this parameter to authenticate. Run `-t`, or `--access-token` and enter your access token created in the authentication. Example: `--access-token <token>`

`-e, --exclusions` <mark style="background-color:yellow;">Optional</mark>

Use this command to exclude files or folders you don't want to be scanned for some reason. The following terms are supported to exclude paths:

* "\*": matches any sequence of non-Separator characters.
* "/\*\*/": matches zero or multiple directories.
* "?": matches any single non-Separator character.
* "\[class]": matches any single non-Separator character against a class of characters
* "{alt1,...}": matches a sequence of characters if one of the comma-separated alternatives matches.

Examples: `-e "*/**.lock"`, `-e "**/node_modules/**"`, `-e "*/**.exe`, `-e "**/node_modules/**`\
You can use this command to ignore multiple terms. For example: `debricked files find . -e "**/node_modules/**" -e "**/package-lock.json"`

Default: in case you don’t provide this parameter will be set by default to ignore the “node\_modules”, "vendor", and “.git”

`-b, --branch` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to specify the branch to analyze in your project. For example: `-–branch main`

Default: if you don’t provide this parameter will be set by default to scan all the branches.

`-c, --commit` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to specify the commit to analyze in your project. Type `-–commit` followed by the hash commit. Example: `--commit 2609d8385125ddd2d7aa4cfb5be8fcd392e3280a`.

Default: if you don’t provide this parameter, OpenText Core SCA will scan the last commit.

`-i, --integration` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to specify the name of the integration used to trigger the scan. For example `--integration “GitHub Actions”`

Default: if you don’t provide this parameter, it will be set to “CLI” by default

`-p, --pass-on-timeout` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to pass scans if there is a service access timeout

`-r, --repository` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to specify the name of the repository to analyze. For example: `--repository EasyApp`

`-u, --repository-url` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to specify the URL address of the repository to analyze. For example:`--repository-url https://github.com/nordisk/myrepository`

`--no-resolve` <mark style="background-color:yellow;">Optional</mark>

When scanning, the High Performance resolution is enabled by default. Use this parameter to disabled it if needed. See [here](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) for more details about the High Performance Scan.

`--sbom string` <mark style="background-color:yellow;">Optional</mark>

Use this toggle parameter for generating and downloading SBOM report in the specified format after scan completion. Supported formats are 'CycloneDX' and 'SPDX-2.3'. Leaving the field empty results in no SBOM generation.

`--sbom-output string` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to specify the output path for downloaded SBOM report (if sbom is toggled).

More Example&#x73;**:**

In this example, we analyze all the dependencies files in our current directory. The “.” starts the scanning in the current working directory.

```
debricked scan . -t "<token>"
```

In this example, we are going to scan a project called “EasyApp” in the local directory “\~/Desktop/myproject/EasyApp”:

```
Debricked scan ~/Desktop/myproject/EasyApp --access-token "<token>" --commit "044bdc7c22e46be010969e9360dbe679830100f1" --branch "dev"  --exclusion "**/node_modules/**"
```

#### resolve <a href="#resolve" id="resolve"></a>

* `debricked resolve [path] [flags]`
* `debricked resolve –help` to see all the options.

The resolve command resolves manifest files to lock files. See [here](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/high-performance-scans) for more details about the High Performance Scan.

Path:

* Use the path argument to specify what manifest file to resolve or what directory to resolve manifest files in. For example: `debricked resolve ~/Desktop/Coder-2022/Eccomerce2/ -t <token>` or `debricked resolve ~/Desktop/Coder-2022/Eccomerce2/pom.xml -t <token>`.

Flags:

`-t --access-token` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to authenticate to enable a higher rate limit. Run `-t`, or `--access-token` and enter your access token created in the authentication. Example: --access-token \<token>

`-e, --exclusions` <mark style="background-color:yellow;">Optional</mark>

Use this command to exclude files or folders you don't want to be scanned for some reason. The following terms are supported to exclude paths:

* "\*": matches any sequence of non-Separator characters.
* "/\*\*/": matches zero or multiple directories.
* "?": matches any single non-Separator character.
* "\[class]": matches any single non-Separator character against a class of characters
* "{alt1,...}": matches a sequence of characters if one of the comma-separated alternatives matches.

Examples: `-e "*/**.lock"`, `-e "**/node_modules/**"`, `-e "*\**.exe`, `-e "**\node_modules\**`\
You can use this command to ignore multiple terms. For example: `debricked files find . -e "**/node_modules/**" -e "**/package-lock.json"`

Default: in case you don’t provide this parameter will be set by default to ignore the “node\_modules”, "vendor", and “.git”.

`--verbose` <mark style="background-color:yellow;">Optional</mark>\
Use the this flag to toggle verbosity in error output for resolution, this mainly applies to the error output provided from the package managers which the OpenText Core SCA CLI calls (i.e "external" errors) when resolving. For example `--verbose=false` to get less verbose error messaging.

Default: If you don’t provide this parameter, it will be set to “true” by default.

`--resolution-strictness int` <mark style="background-color:yellow;">Optional</mark>\
Use the this flag to configure exit codes for resolution, depending on the success of the command:\
\- 0 (default) - Always exit with code 0, even if any or all files failed to resolve\
\- 1 - Exit with code 1 if all files failed to resolve, otherwise exit with code 0\
\- 2 - Exit with code 1 if any file failed to resolve, otherwise exit with code 0\
\- 3 - Exit with code 1 if all files failed to resolve, if any but not all files failed to resolve exit with code 3, otherwise exit with code 0

`--regenerate int` <mark style="background-color:yellow;">Optional</mark>\
Use the this flag to toggle regeneration of already existing lock files between 3 modes. This is useful for when you use the resolve command to generate lock files permanently in your project and would like to ensure that they are kept up to date before every scan.\
\- 0 (default) - No regeneration\
\- 1 - Regenerates existing non package manager native OpenText Core SCA lock files\
\- 2 - Regenerates all existing lock files

`--prefer-npm` <mark style="background-color:yellow;">Optional</mark>\
This flag allows you to use **npm** instead of **yarn** (which is default) when resolving package.json files without lock files.

#### files find <a href="#filesfind" id="filesfind"></a>

* `debricked files find [path] [flags]`
* `debricked files find –-help` to see all the options.

Use this command to search all the dependencies files in your project.

Path:

* Use the path argument to specify which directory the dependency file is in, or to exclude it. For example: `debricked files find ~/Desktop/Coder-2022/Eccomerce2/ -t <token>`.
* Use the path to specify where the dependency file is allocated, you can use "." to search the current working directory. For instance: `debricked files find . -t <token>` or `debricked files find ~/Desktop/Coder-2022/Eccomerce2/ -t <token>`.

Note: If the path is inside a git repository, all the necessary flags branch, commit, etc) will be set for you automatically.

Flags:

`-l, --lockfile` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to find only the **lock files** in your project.

`-j, --json` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to print the file from the **path** in JSON format. Here’s an example, where we look for all the dependency files in the folder “project7” and print them in JSON format.

```
debricked files find  ~/Desktop/project7 -t <token> -e "**/node_modules/**" --json
```

Output:

```
[
  {
    "manifestFile": "go.mod",
    "lockFiles": [
      ".gomod.debricked.lock"
    ]
  }
]
```

`-s, --strict int`

Allows controlling which files are matched:

\- 0 (default) - returns all matched manifest and lock files regardless if they're paired or not

\- 1 - returns only lock files and pairs of manifest and lock-file

\- 2 - returns only pairs of manifest and lock-file\\

Workspaces:

Since release v2.0.7 `files find` support workspaces for npm and yarn. Nothing additional is needed to make workspaces work, but in addition to the official format we also support nesting the workspace patterns under a `packages` key. Examples:

```
{
  "workspaces": [
    "package/*"
  ]
}
```

```
{
  "workspaces": {
    "packages": [
      "package/*"
    ]
  }
}
```

For specific documentation on using workspaces with npm see the [npm workspace documentation](https://docs.npmjs.com/cli/v10/using-npm/workspaces), and for yarn see the [yarn workspace documentation](https://classic.yarnpkg.com/lang/en/docs/workspaces/).

#### export <a href="#report" id="report"></a>

{% hint style="info" %}
Prior to version 2.3.0, this command was referred to as 'report'.
{% endhint %}

**`export license`**

{% hint style="info" %}
*Note that this feature is only available for premium and enterprise users.* *Visit our* [*Pricing page*](https://debricked.com/pricing/) *for more info.*
{% endhint %}

Example for generating a license export:

```
debricked export license -t "<token>" --commit 044bdc7c22e46be010969e9360dbe679830100f1 --email user1@email.com
```

Flags:

`-t --access-token` <mark style="background-color:red;">Required</mark>

Use this parameter to authenticate. `-t`, or `--access-token` and enter your access token created in the authentication. For example: `--access-token <token>`

`-c, --commit` <mark style="background-color:red;">Required</mark>

Use this parameter to specify the hash commit of the repository to analyze. For example: `--commit 2609d8385125ddd2d7aa4cfb5be8fcd392e3280a`

`-e, --email` <mark style="background-color:red;">Required</mark>

Use this parameter to set the email address to which the export will be sent to. For example: `--email user1@email.com`

**`export vulnerability`**

{% hint style="info" %}
*Note that this feature is only available for premium and enterprise users.* *Visit our* [*Pricing page*](https://debricked.com/pricing/) *for more info.*
{% endhint %}

Example for generating a Vulnerability export:

```
debricked export vulnerability-t "<token>" --commit 044bdc7c22e46be010969e9360dbe679830100f1 --email user1@email.com
```

Flags:

`-e, --email` <mark style="background-color:red;">Required</mark>

Use this parameter to set the email address to which the export will be sent to. For example: `--email user1@email.com`

`export sbom`

{% hint style="info" %}
*Note that this feature is only available for enterprise users. Visit our* [*Pricing page*](https://debricked.com/pricing/) *for more info. If you wish to generate an SBOM directly following a scan, see the `--sbom` flag under* [*https://docs.debricked.com/tools-and-integrations/cli/debricked-cli#scan*](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli#scan)*.*
{% endhint %}

Example for generating sbom export:

```
debricked export sbom -t "<token>" --commit 1234 --repository 5678 --format SPDX-2.3
```

Flags:

`-t --access-token` <mark style="background-color:red;">Required</mark>

Use this parameter to authenticate. `-t`, or `--access-token` and enter your access token created in the authentication. For example: `--access-token <token>`

`-b, --branch` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to specify the name of the branch that you want to generate an SBOM export for.&#x20;

`-c, --commit` <mark style="background-color:red;">Required</mark>

Use this parameter to specify the ID of the commit that you want to generate an SBOM export for. Note that if this value is provided, the values for repository and branch will be ignored. For example: `--commit 1234`

`-f, --format` <mark style="background-color:red;">Required</mark>

Use this parameter to set the format that you want the SBOM export in. Supported options are 'CycloneDX' and 'SPDX-2.3'. For example: `--format SPDX-2.3`

`-o, --output string` <mark style="background-color:yellow;">Optional</mark>

Use this parameter to set the output path for downloaded SBOM json file. If no output path is set, the file is created in the format \<repository\_id>-\<commit\_id>.sbom.

`-r, --repository string` <mark style="background-color:red;">Required</mark>

Use this parameter to specify the ID of the repository that you want to generate an SBOM export for.

#### callgraph <a href="#callgraph" id="callgraph"></a>

* `debricked callgraph [[path] [flags]]`
* `debricked callgraph –help` to see all the options.

The callgraph command generates a static callgraph for a project. Execute command in project directory or specify project path.

Path:

* Use the path argument to specify the project path. If nothing is provided, the current working directory will be used.

Flags:

* `e, --exclusions` <mark style="color:yellow;">Optional</mark>

  * Specify which files or paths you don't want to include in the callgraph. The following terms are supported to exclude paths:

    | Term       | Meaning                                                                                               |
    | ---------- | ----------------------------------------------------------------------------------------------------- |
    | \*         | matches any sequence of non-Separator characters                                                      |
    | /\*\*/     | matches zero or multiple directories                                                                  |
    | ?          | matches any single non-Separator character                                                            |
    | \[class]   | matches any single non-Separator character against a class of characters (\[see "character classes"]) |
    | {alt1,...} | matches a sequence of characters if one of the comma-separated alternatives matches                   |

  Examples: `-e "**/target/test-classes/**"`, `-e "*\\test.class"`

  You can use this command to ignore multiple terms. For example: `debricked callgraph -e "**/target/test-classes/**" -e "*\\test.class"`
* \--no-build <mark style="background-color:yellow;">Optional</mark>
  * Do not automatically build all source code in the project. This option requires a pre-built project/available .class files.
* \--generate-timeout <mark style="background-color:yellow;">Optional</mark>
  * Sets a timeout (in seconds) on the call graph generation.
  * Default: If you don’t provide this parameter, it will be set by default to 3600 (1 hour).

Command Details:

The command can be divided into three main steps:

1. Build project

   * build project based on the root pom.xml. If no root pom.xml is found, all pom.xml files will be built individually.

   ```
   $ mvn package -q -DskipTests -e
   ```

   * a successful build will generate the necessary .class files
2. Copy external dependency files to `.debrickedTmpFolder` in the root pom.xml directory

   ```
   $ mvn q -B dependency:copy-dependencies -DoutputDirectory=/path/to/root/.debrickedTmpFolder -DskipTests -e
   ```
3. Generate call graph
   * Uses a built version of the [OpenText Core SCA vulnerable functionality](https://github.com/debricked/soot-wrapper) project to identify all .class files and map those to the root pom.xml, using the same path as `.debrickedTmpFolder`

     ```
     $ java -jar path/to/built/file/java/common/target/SootWrapper.jar -u path/to/root/target/classes/ -l /path/to/root/.debrickedTmpFolder  -f .debricked-call-graph
     ```
   * The generated call graph output is stored in the base64 encoded zip file `.debricked-call-graph`

The callgraph command requires at least java11. If your project cannot be built with java11, we would recommend you to build your project in your environment before running the command and use `--no-build` flag when generating the call graph.

Common Errors:

* Build failures
  * These are likely due to local configurations. If the build step fails, it is recommended to build your project as usual in your environment and skip step 1 above, i.e. just copy external dependencies to `.debrickedTmpFolder` and run `debricked callgraph --no-build` on your built project. Make sure all .class files are available.
* Callgraph failures
  * out of memory
  * cp dependencies

    ```
    * Critical:
    	|Command 'mvn -q -B dependency:copy-dependencies -DoutputDirectory=/path/to/root/.debrickedTmpFolder -DskipTests' executed in folder '/path/to/root/' gave the following error: 
    	|[ERROR] Failed to execute goal on project <project-name>: Could not resolve dependencies <deps>
    ```
  * mapping dependencies

    ```
    * Critical:
    	|Command 'java -jar path/to/built/file/java/common/target/SootWrapper.jar -u path/to/root/target/classes/ -l /path/to/root/.debrickedTmpFolder  -f .debricked-call-graph' executed in folder '/path/to/root' gave the following error: 
    	|
    	|Running SootWrapper version 5.0
    	|SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
    	|SLF4J: Defaulting to no-operation (NOP) logger implementation
    	|SLF4J: See <http://www.slf4j.org/codes.html#StaticLoggerBinder> for further details.
    	|Error: Found no entry points. Do path(s) to user code contain compiled user code?
    ```

    If you see the error above, make sure all .class files are available in the right path and that all external dependencies have been copied to .debrickedTmpFolder

#### fingerprint

* `debricked fingerprint [[path] [flags]]`
* `debricked fingerprint –help` to see all the options.

Fingerprint files for identification in a given path and write it to debricked.fingerprints.txt. This hashes all files to be used for matching against the OpenText Core SCA knowledge base.

Path:

* Use the path argument to specify the project path. If nothing is provided, the current working directory will be used.

Flags:

* `e, --exclusions` <mark style="background-color:yellow;">Optional</mark>

  Specify which files or paths you don't want to include when fingerprinting. The following terms are supported to exclude paths:

  | Term       | Meaning                                                                                               |
  | ---------- | ----------------------------------------------------------------------------------------------------- |
  | \*         | matches any sequence of non-Separator characters                                                      |
  | /\*\*/     | matches zero or multiple directories                                                                  |
  | ?          | matches any single non-Separator character                                                            |
  | \[class]   | matches any single non-Separator character against a class of characters (\[see "character classes"]) |
  | {alt1,...} | matches a sequence of characters if one of the comma-separated alternatives matches                   |

  Examples: `-e "/.pyc"`, `-e "*\\\\test.class"`, `-e "**/target/test-classes/**"`

  You can use this command to ignore multiple terms. For example: `debricked fingerprint -e "/node_modules/" -e "/.egg-info/" -e "/*venv/**"`

  By default, the following are ignored: /nbproject/,/nbbuild/,/nbdist/,/node\_modules/,/pycache/,/\_yardoc/,/eggs/,/wheels/,/htmlcov/,/pypackages/,/.egg-info/,/*venv/*\*
* -fingerprint-compressed-content <mark style="background-color:yellow;">Optional</mark>

  Fingerprint the contents of compressed files by unpacking them in memory, Supported files: \[.jar .nupkg .war]\
  default: false

**auth**

You can authenticate to the OpenText Core SCA service using this command. Following are the different commands:

* `debricked auth login` to authenticate with your OpenText Core SCA user.
* `debricked auth logout` to log out an authenticated OpenText Core SCA user.
* `debricked auth token` to retrieve access token for use in the OpenText Core SCA API.
* `debricked auth –help` to see all the options.

### 6. Troubleshooting and error messages <a href="#id-6.troubleshootinganderrormessage" id="id-6.troubleshootinganderrormessage"></a>

Below you can find the list of some of the most common error messages. If the problem persists and you can’t solve it for yourself or have additional questions feel free to reach contact our support team.

```
⨯ Unauthorized. Specify access-token. 
Read more at https://debricked.com/docs/administration/access-tokens.html
```

This error message appears when the access-token is missing or if you provide an invalid access token. For more information, see the \`-t -- access-token\` command.

```
Error: required flag(s) "email" not set
```

This error message appears when you run the \`debricked export vulnerability/license\` command without a valid email address. To resolve this, use the \`--email, -e\` \[options] to set an email the export should be sent to. For example: \`debricked export license -t “\<token>” –email ”<usuario1@gmail.com>”\`

```
Error: ⨯ No commit was found with the name
```

This error message appears when you run the \`debricked export vulnerability/license\` command but the CLI can’t find the commit. To resolve this, use the \`--commit, -c\` \[options] to provide a commit hash.

For example: \`debricked export license -t “\<token>” –email ”<usuario1@gmail.com>” –commit 044bdc7c22e46be010969e9360dbe679830100f1\`

```
Error: required flag(s) "commit" not set
```

This error message appears when you run the \`debricked export vulnerability/license\` command without any commits. To resolve this, use the \`--commit, -c\` \[options] to provide a commit hash.

For example: \`debricked export license -t “\<token>” –email ”<usuario1@gmail.com>” –commit 044bdc7c22e46be010969e9360dbe679830100f1\`

```
Error: invalid directory path specified: "~/Desktop/../../EasyApp"
```

This error message appears when the scan can't find any valid directory in the path. To resolve it, check if the path provided is correct.

```
Error: ⨯ failed to find repository name
```

This error message appears when we can't fetch the repository name. To fix this, set a name for the repository, using the `-r` flag.

#### **6.1 Getting support** <a href="#gettingsupport" id="gettingsupport"></a>

If you need help, contact us via our live chat, open Monday-Friday 9 am-5 pm CET, or email <support@debricked.com>.

**Uninstallation**

The only thing that is needed to uninstall is to remove the binary - the file called `debricked` or `debricked.exe` depending on your operating system.

#### **6.2 Create an issue or report a bug** <a href="#createanissueorreportabug" id="createanissueorreportabug"></a>

Before creating an issue or reporting a bug, make sure to contact support and discuss the issue or feedback with us first.

If you want to create an issue or report a bug you can do it directly by[ submitting an issue via GitHub](https://github.com/debricked/cli/blob/1a839d857dbd6ba8a8f9fcb51a8ec646e0bc2354/CONTRIBUTING.md#bug-reports).

#### 6.3 Upgrading from version 1.X.X to version 2.0.0

The 2.0.0 release contains some breaking changes, documented below:

{% @github-files/github-code-block url="<https://github.com/debricked/cli/blob/main/UPGRADE-2.0.md>" %}

#### **6.4 Contributors** <a href="#contributors" id="contributors"></a>

If you'd like to contribute directly to the project, check out [our guide](https://github.com/debricked/cli/blob/1a839d857dbd6ba8a8f9fcb51a8ec646e0bc2354/CONTRIBUTING.md). Feel free to reach out to any of the maintainers or other community members if you have any questions.
