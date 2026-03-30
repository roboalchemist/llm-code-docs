# Source: https://docs.socket.dev/docs/socket-package.md

# socket package

Get score and other details on software packages

These set of commands are your gateway to get Socket.dev scoring on packages from ecosystems like npm, rubygems, and pypi.

## socket package --help

```
$ socket package --help

  Commands relating to looking up published packages

  Usage
    $ socket package <command>

  Commands
    score             Look up score for one package which reflects all of its transitive dependencies as well
    shallow           Look up info regarding one or more packages but not their transitives

  Options
    (none)

  Examples
    $ socket package --help
```

# Score

There are basically two kinds of package scores: shallow and deep scores. Before we cover that we should mention what a "purl" is.

## PURL

A PURL is a string that conforms to a [specification for a "package URL"](https://github.com/package-url/purl-spec/tree/main) which is a general way to name a package in such a way that it can be recognized and that there can be no ambiguity about the ecosystem, package name, or version. An example would be `pkg:npm/socket` or `pkg:pypi/pip`.

In docs we may casually refer to a "purl" just like you would when you say "url" for any website.

## Shallow score

When the score only applies to the package itself and not its direct or transitive dependencies then it's a shallow score. It simply applies to the software that was written by that dev or vendor, not the other packages it may also depend on.

To get shallow package scores for multiple packages you can use the `socket package shallow` command. It supports two ways;

* you start by specifying an ecosystem and then any number of packages

```
$ socket package shallow npm babel eslint@1.0.0

ℹ Requesting shallow score data for 2 package urls (purl): pkg:npm/babel, pkg:npm/eslint@1.0.0
✔ Received API response (after requesting looking up package).

Shallow Package Score

Please note: The listed scores are ONLY for the package itself. It does NOT
             reflect the scores of any dependencies, transitive or otherwise.


Package: pkg:npm/babel@6.23.0

- Supply Chain Risk:   99
- Maintenance:         80
- Quality:             50
- Vulnerabilities:    100
- License:            100
- Alerts (0/2/2):     [middle] deprecated, [middle] trivialPackage, [low] newAuthor, [low] unmaintained


Package: pkg:npm/eslint@1.0.0

- Supply Chain Risk:   97
- Maintenance:         95
- Quality:            100
- Vulnerabilities:    100
- License:            100
- Alerts (0/1/2):     [middle] deprecated, [low] dynamicRequire, [low] filesystemAccess

```

<br />

* you can specify any number of "PURL" names, even mix ecosystems

```
$ socket package shallow pkg:maven/log4j/log4j@1.2.17 pkg:pypi/charset-normalizer@3.4.0 pkg:npm/eslint@1.0.0

ℹ Requesting shallow score data for 3 package urls (purl): pkg:maven/log4j/log4j@1.2.17, pkg:pypi/charset-normalizer@3.4.0, pkg:npm/eslint@1.0.0
✔ Received API response (after requesting looking up package).

Shallow Package Score

Please note: The listed scores are ONLY for the package itself. It does NOT
             reflect the scores of any dependencies, transitive or otherwise.


Package: pkg:npm/eslint@1.0.0

- Supply Chain Risk:   97
- Maintenance:         95
- Quality:            100
- Vulnerabilities:    100
- License:            100
- Alerts (0/1/2):     [middle] deprecated, [low] dynamicRequire, [low] filesystemAccess


Package: pkg:maven/log4j@1.2.17

- Supply Chain Risk:   36
- Maintenance:        100
- Quality:             89
- Vulnerabilities:     25
- License:             80
- Alerts (5/3/3):     [critical] criticalCVE, [critical] criticalCVE, [critical] criticalCVE, [high] cve, [high] cve, [middle] networkAccess, [middle] potentialVulnerability, [middle] usesEval, [low] filesystemAccess, [low] unidentifiedLicense, [low] unmaintained


Package: pkg:pypi/charset-normalizer@3.4.0

- Supply Chain Risk:   99
- Maintenance:        100
- Quality:            100
- Vulnerabilities:    100
- License:            100
- Alerts (0/2/1):     [middle] hasNativeCode, [middle] usesEval, [low] filesystemAccess
```

The shallow scores give a good indication of what might be wrong with the package itself but it does not tell anything about how safe a package is, unless of course it has zero dependencies.

## Deep score

In general when people want to know the score of a package they are talking about the package as a whole, so including any software that shipped with it. This leads us to a "deep" score, or a "transitive" score. This kind of score reflects the whole package as it gets shipped, including its direct dependencies, the dependencies that those depend on, and so forth. That's also called "transitive dependencies".

To get the transitive dependency score for a package you can use two ways, similar as for the shallow score above:

* you start with the ecosystem followed by the package your want to inspect

```
$ socket package deep npm eslint --markdown

ℹ Requesting deep score data for this purl: pkg:npm/eslint
✔ Received API response (after requesting the deep package scores).
✔ Score report for "pkg:npm/eslint" ("npm/eslint@9.28.0"):

# Complete Package Score

This is a Socket report for the package *"npm/eslint@9.28.0"* and its *86* direct/transitive dependencies.

It will show you the shallow score for just the package itself and a deep score for all the transitives combined. Additionally you can see which capabilities were found and the top alerts as well as a package that was responsible for it.

The report should give you a good insight into the status of this package.

## Package itself

Here are results for the package itself (excluding data from dependencies).

### Shallow Score

This score is just for the package itself:

- Overall: 95
- Maintenance: 95
- Quality: 100
- Supply Chain: 96
- Vulnerability: 100
- License: 100

### Capabilities

These are the capabilities detected in the package itself:

- env
- url

### Alerts for this package

These are the alerts found for the package itself:

| -------- | -------------- |
| Severity | Alert Name     |
| -------- | -------------- |
| low      | dynamicRequire |
| low      | envVars        |
| -------- | -------------- |

## Transitive Package Results

Here are results for the package and its direct/transitive dependencies.

### Deep Score

This score represents the package and and its direct/transitive dependencies:
The function used to calculate the values in aggregate is: *"min"*

- Overall: 65
- Maintenance: 74
- Quality: 65
- Supply Chain: 96
- Vulnerability: 100
- License: 100

### Capabilities

These are the packages with the lowest recorded score. If there is more than one with the lowest score, just one is shown here. This may help you figure out the source of low scores.

- Overall: npm/shebang-command@2.0.0
- Maintenance: npm/json-stable-stringify-without-jsonify@1.0.1
- Quality: npm/shebang-command@2.0.0
- Supply Chain: npm/eslint@9.28.0
- Vulnerability: npm/estraverse@5.3.0
- License: npm/estraverse@5.3.0

### Capabilities

These are the capabilities detected in at least one package:

- env
- eval
- fs
- shell
- unsafe
- url

### Alerts

These are the alerts found:

| -------- | ------------------ | ---------------------------- |
| Severity | Alert Name         | Example package reporting it |
| -------- | ------------------ | ---------------------------- |
| middle   | shellAccess        | npm/cross-spawn@7.0.6        |
| middle   | usesEval           | npm/ajv@6.12.6               |
| low      | debugAccess        | npm/resolve-from@4.0.0       |
| low      | dynamicRequire     | npm/keyv@4.5.4               |
| low      | envVars            | npm/eslint@9.28.0            |
| low      | filesystemAccess   | npm/argparse@2.0.1           |
| low      | highEntropyStrings | npm/jiti@2.4.2               |
| low      | minifiedFile       | npm/jiti@2.4.2               |
| low      | unmaintained       | npm/esutils@2.0.3            |
| -------- | ------------------ | ---------------------------- |

```

<br />

* or by specifying the whole purl

```
$ socket package deep 'pkg:maven/org.apache.beam/beam-runners-flink-1.15-job-server@2.58.0?classifier=tests&ext=jar' --markdown

ℹ Requesting deep score data for this purl: pkg:maven/org.apache.beam/beam-runners-flink-1.15-job-server@2.58.0?classifier=tests&ext=jar
✔ Received API response (after requesting the deep package scores).
✔ Score report for "pkg:maven/org.apache.beam/beam-runners-flink-1.15-job-server@2.58.0?classifier=tests&ext=jar" ("pkg:maven/org.apache.beam/beam-runners-flink-1.15-job-server@2.58.0?classifier=tests&ext=jar"):

# Complete Package Score

This is a Socket report for the package *"pkg:maven/org.apache.beam/beam-runners-flink-1.15-job-server@2.58.0?classifier=tests&ext=jar"* and its *404* direct/transitive dependencies.

It will show you the shallow score for just the package itself and a deep score for all the transitives combined. Additionally you can see which capabilities were found and the top alerts as well as a package that was responsible for it.

The report should give you a good insight into the status of this package.

## Package itself

Here are results for the package itself (excluding data from dependencies).

### Shallow Score

This score is just for the package itself:

- Overall: 100
- Maintenance: 100
- Quality: 100
- Supply Chain: 100
- Vulnerability: 100
- License: 100

### Capabilities

No capabilities were found in the package.

### Alerts for this package

There are currently no alerts for this package.

## Transitive Package Results

Here are results for the package and its direct/transitive dependencies.

### Deep Score

This score represents the package and and its direct/transitive dependencies:
The function used to calculate the values in aggregate is: *"min"*

- Overall: 6
- Maintenance: 71
- Quality: 88
- Supply Chain: 6
- Vulnerability: 25
- License: 50

### Capabilities

These are the packages with the lowest recorded score. If there is more than one with the lowest score, just one is shown here. This may help you figure out the source of low scores.

- Overall: maven/io.trino.hadoop/hadoop-apache@3.2.0-12
- Maintenance: maven/org.apache.beam/beam-sdks-java-extensions-arrow@2.58.0
- Quality: maven/log4j/log4j@1.2.17
- Supply Chain: maven/io.trino.hadoop/hadoop-apache@3.2.0-12
- Vulnerability: maven/log4j/log4j@1.2.17
- License: maven/com.fasterxml.jackson.datatype/jackson-datatype-joda@2.15.4

### Capabilities

These are the capabilities detected in at least one package:

- env
- eval
- fs
- net
- shell
- unsafe

### Alerts

These are the alerts found:

| -------- | ---------------------- | ---------------------------------------------------- |
| Severity | Alert Name             | Example package reporting it                         |
| -------- | ---------------------- | ---------------------------------------------------- |
| critical | criticalCVE            | maven/log4j/log4j@1.2.17                             |
| critical | didYouMean             | maven/io.trino.hadoop/hadoop-apache@3.2.0-12         |
| high     | cve                    | maven/log4j/log4j@1.2.17                             |
| middle   | hasNativeCode          | maven/org.apache.beam/beam-vendor-grpc-1_60_1@0.2    |
| middle   | mediumCVE              | maven/org.apache.ant/ant@1.10.9                      |
| middle   | networkAccess          | maven/log4j/log4j@1.2.17                             |
| middle   | potentialVulnerability | maven/log4j/log4j@1.2.17                             |
| middle   | shellAccess            | maven/org.apache.beam/beam-vendor-calcite-1_28_0@0.2 |
| middle   | usesEval               | maven/log4j/log4j@1.2.17                             |
| low      | copyleftLicense        | maven/javax.annotation/javax.annotation-api@1.3.2    |
| low      | envVars                | maven/org.apache.beam/beam-vendor-calcite-1_28_0@0.2 |
| low      | filesystemAccess       | maven/log4j/log4j@1.2.17                             |
| low      | gptAnomaly             | maven/io.netty/netty-transport@4.1.100.Final         |
| low      | licenseException       | maven/javax.annotation/javax.annotation-api@1.3.2    |
| low      | mildCVE                | maven/org.apache.hadoop/hadoop-common@2.10.2         |
| low      | noLicenseFound         | maven/com.google.guava/failureaccess@1.0.2           |
| low      | nonpermissiveLicense   | maven/org.apache.commons/commons-math3@3.6.1         |
| low      | unidentifiedLicense    | maven/log4j/log4j@1.2.17                             |
| low      | unmaintained           | maven/log4j/log4j@1.2.17                             |
| -------- | ---------------------- | ---------------------------------------------------- |

```

<br />

The deep score for a package should give you a good indication of whether it's safe to run a package. But mind you, we can only report the things that we actually know out about!

## Output flags

The commands support `--json` for a raw dump, `--markdown` for a nice legible and shareable report, and otherwise default to doing a colorized `console.log` dump in NodeJS that trims objects after a certain depth.