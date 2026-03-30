# Source: https://docs.debricked.com/tools-and-integrations/cli/debricked-cli/file-fingerprinting.md

# File fingerprinting

{% hint style="info" %}
*This feature is only available for* [*SCA Enterprise*](https://debricked.com/pricing/) *users. Already have an account?* [*Click here to upgrade.*](https://debricked.com/app/en/repositories?billingModal=enterprise,free)

*Currently supported languages: C#, JavaScript, Java and Python.*
{% endhint %}

OpenText Core SCA supports scanning for unmanaged dependencies not defined in manifest-files by examining fingerprints of the contents (including binary files) of your application (with some exclusions for non-relevant files).

### Enabling file fingerprinting

To enable file fingerprint analysis, first you need to generate a debricked.fingerprints.txt file. This can be done using the [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli) `fingerprint` command, which can be added to your integration, so that it is generated appropriately before making a OpenText Core SCA scan. Ensure that your application has been built prior to running the `fingerprint` command, to ensure that the relevant dependencies are included in the scan. By default, OpenText Core SCA does not unpack archive files such as .jar, .nupkg, and .war, but it can be activated through the `—fingerprint-compressed-content` flag. To find out more about which files are unpacked with this file and more information on the command and the various available flags, run:

```
debricked fingerprint -h
```

File fingerprinting is run by default as part of the `scan` command (since CLI v2.0.10), but this can be disabled by running `debricked scan --no-fingerprint=true`.

#### Example Configuration

Here is an example of how to run the `fingerprint` command directly prior to the scan. The command can be run in any stage of your pipeline, as long as the debricked.fingerprints.txt file is available to be picked up when running `debricked scan`.

```bash
# GitLab CI/CD template

image: debricked/cli:2-resolution-debian

stages:
  - scan
debricked:
  stage: scan
  script:
    - debricked fingerprint
    - debricked scan --no-fingerprint=true
```

### Algorithm

The algorithm is built to make the match for each file in two stages:

* Package matching
* Version resolution

In the initial stage, OpenText Core SCA considers both the first occurrence of all packages which matches the given file hash and the path used. Based of those two parameters, a package is assigned to each file included in your fingerprints. The exact version is to be decided in the next part of the algorithm, as this particular file may exist in multiple versions of this package.

To decide the version or versions for a set of matches that are assigned to a specific package, OpenText Core SCA optimizes to find the version with the most matches. This is an iterative algorithm, so this part of the algorithm is run until all files have resolved a specific version. The stable versions are prioritized with higher release dates first if they have the same number of matches.

### Manage or override results

If you believe OpenText Core SCA has found a wrong dependency and you'd like to change matches, it is possible to manage and override the results.

In some instances, the package and/or version resulting from file fingerprinting may differ from the dependency used in your application. One way of ensuring the results is correct is excluding fingerprinting of a certain file or path. This can be achieved through the `scan` command by using the `--exclusion` flag and adding the correct dependency to a manifest file or a CycloneDX SBOM included in your scan.

If you instead wish to override these results without adding them to a dependency file, this can be done natively through the debricked-config.yaml file, with the CLI.

The overriding can be performed per file hash, set of file hashes, folders, and more. This is determined by an array called *fileRegexes*. If a file path matches a given Rust-flavoured regex, you can determine the pURL and version (if specified) that will be set to the matches made. Entries higher in the list have higher priority, so the first matching fileRegex for a given file path will always be taken.

It is also possible to exclude or ignore findings through configuration. For file fingerprinting, this can be done by specifying an empty pURL for a given set of  `fileRegex` patterns. Additionally, both file fingerprint and manifest analysis results can be ignored using the **ignore** section by specifying a package pURL and, optionally, a specific version to exclude.

Here is an example of the debricked-config.yaml format:

```yaml
overrides:
  - pURL: "pkg:npm/lodash"
    version: "1.0.0" # (optional: if left out, we will determine the version)
    fileRegexes: # (Rust regex)
      - "@types/lodash/.*"
  - pURL: "pkg:maven/org.openjfx/javafx-base"
    version: false # false means that we will determine the version
    fileRegexes:
      - "subpath/org.openjfx/.*"
  - pURL: "pkg:maven/junit/junit"
    fileRegexes:
      - "junit-3.8.1/junit-3.8.1.jar"
      - "junit-4.1/junit-4.1.jar"
  - pURL: "" # empty pURL ignores matching fileRegexes during fingerprint analysis
    fileRegexes:
      - "test/.*"
ignore:
    packages:
    - pURL: "pkg:npm/verdaccio"
      version: "3.7.0" # optional: if omitted, ignores all versions
    - pURL: "pkg:npm/chart.js"
    - pURL: "pkg:nuget/simpleinjector"
      version: "4.7.1"

```

If you want to try your regex, you could visit <https://regex101.com> and choose Rust as the flavour.

Packages match using the pURL of the package that you have imported. Use the common pURL format as per the pURL spec:

```
pkg:type/namespace/name
```

* The *scheme* section is the URL scheme with the constant value of *pkg.*
* The *type* section of the pURL corresponds to the package manager used by the dependency or the version control system used (in case of repository-only dependencies).
* The *namespace* is used mainly for repository dependencies corresponding to the repository owner or dependencies with vendor.
* The *name* section corresponds to the package or repository’s name.

Here are some examples of pURL searches and their corresponding results:

* *pkg:pypi/tensorflow* → Tensorflow
* *pkg:npm/react* → React
* pkg:maven/org.springframework.boot/spring-boot-starter-web

Have a look at the [pURL spec page](https://github.com/package-url/purl-spec) to learn more.
