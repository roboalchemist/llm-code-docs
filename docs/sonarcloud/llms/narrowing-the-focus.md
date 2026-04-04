# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/narrowing-the-focus.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/narrowing-the-focus.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/narrowing-the-focus.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/narrowing-the-focus.md

# Narrowing the focus

There are many cases where you do not want to analyze every aspect of every source file in your project. For example, your project may contain generated code, source code from libraries, or intentionally duplicated code.

In such cases, it makes sense to skip some or all aspects of analysis for these files, thus removing noise and allowing you to focus on the issues that really matter.

To help narrow the focus, SonarQube gives you several options to precisely configure what will be analyzed and how. Most of the properties that define your analysis scope can be defined in the SonarQube UI. Other parameters must be set explicitly in the scanner invocation or in the appropriate configuration file as we describe in more detail below; see the [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/analysis-parameters "mention") page for more detail.

### Setting the initial scope <a href="#setting-the-initial-scope" id="setting-the-initial-scope"></a>

The initial scope of analysis is controlled by the following parameters:

* `sonar.sources` define the initial scope of analysis for non-test code in your project.
* `sonar.tests` define the initial scope of analysis for test code in your project.

These parameters define the starting point for analysis scope adjustment:

* Files outside the scope defined by these parameters *will not* be analyzed at all.
* Files within the scope defined by these parameters *will* be analyzed *unless excluded by further adjustments* (exclusions, inclusions, etc. See below.)

Additionally, these parameters are:

* only set at the project level. There are no global, server-level equivalents for these parameters.
* either set automatically by your SonarScanner, set explicitly in the `sonar-project.properties` configuration file, or set on the command line that invokes the scanner. There are no UI settings for these parameters.
* set explicitly and both accept a comma-delimited list of paths. Pattern matching with wildcards is not supported.

#### Why is test code scoped separately? <a href="#why-is-test-code-scoped-separately" id="why-is-test-code-scoped-separately"></a>

Test and non-test code are distinguished because

* Different analysis rules are applied to the two categories.
* The two categories have different metrics
* Test code does not count toward lines-of-code limits defined by your license.
* Test code does not count towards coverage (you don’t have to test your test code)

#### Automatic setting for Maven, Gradle, and .NET <a href="#automatic-setting-for-maven-gradle-and-net" id="automatic-setting-for-maven-gradle-and-net"></a>

If you are analyzing code using SonarScanner for Maven, SonarScanner for Gradle, or SonarScanner for .NET, the `sonar.sources` and `sonar.tests` parameters are automatically determined based on information in your project configuration. You do not have to explicitly set the parameters. If you do explicitly set the parameters (for example in your `pom.xml`, in the case of Maven), this will override the automatically determined values.

#### Defaults settings for other scenarios <a href="#defaults-settings-for-other-scenarios" id="defaults-settings-for-other-scenarios"></a>

If you are not using Maven, Gradle or .NET then

* By default, `sonar.sources` is set to the current working directory (the path `.`).
* By default, `sonar.tests` is not set.

#### Explicit settings <a href="#explicit-settings" id="explicit-settings"></a>

If the defaults are not suitable (for example, if you *do* have test code) you must set the parameters explicitly in the scanner invocation or in the appropriate configuration file (see [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/analysis-parameters "mention")).

When explicitly set, both `sonar.sources` and `sonar.tests` take a comma-delimited list of directories or files.

* The entries in the list are simple paths. Wildcards (`*`, `**`, and `?`) are not allowed.
* A directory in the list means that all analyzable files and directories recursively below it are included. An individual file in the list means that the file is included.
* The paths are interpreted relative to the project base directory. The base directory is defined by the scanner you are using. In most cases, this is the root directory of the project. If you are using the SonarScanner CLI, your base directory will be the current directory from which you invoke the tool (though this can be overridden using the parameter `sonar.projectBaseDir`).

#### Example <a href="#example" id="example"></a>

Let’s say your repository looks something like this, with your source and test code clearly separated at the top level:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-e82962af679b05ee902d9b60e4230d6a0cbc27ed%2F6517a878b94b98394f4a6cf4e656c52a6b92f675.png?alt=media)

In this case, you would set your `sonar.sources` like this:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-0f2b826c22a61ee695904e6582ab76436c63edfd%2Fcc420c3931080129ba552963fa150c141c975f81.png?alt=media)

and your `sonar.tests` like this:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-48a9b9d4de84a56714760ff68c425410a0b5476e%2F9569648e1e2db7957c7bc064dada12972b0ee7db.png?alt=media)

If you configure your scope in the `sonar-project.properties` file, it would look like this:

```css-79elbk
# Define separate root directories for sources and tests
sonar.sources = src/
sonar.tests = test/
```

There is no need for any further fine-tuning.

### Wildcard patterns <a href="#wildcard-patterns" id="wildcard-patterns"></a>

While the `sonar.sources` and `sonar.tests` parameters take simple paths, most of the parameters discussed below use path-matching patterns.

The patterns are defined using the following wildcards:

* `*` Match zero or more characters (not including the directory delimiter, `/`).
* `**` Match zero or more directory segments within the path.
* `?` Match a single character (not including the directory delimiter, `/`).

#### Examples <a href="#examples" id="examples"></a>

* The pattern `**/*.css`
  * matches `anyDirectory/anyFile.css`
  * doesn’t match `org/sonar.api/MyBean.java`
* The pattern `**/*Bean.java`
  * matches `org/sonar.api/MyBean.java`
  * doesn’t match `org/sonar/util/MyDTO.java`
* The pattern `**/*Bean?.java`
  * matches `org/sonar/util/MyOtherBean1.java`
  * doesn’t match `org/sonar/util/MyOtherBean.java`
* The pattern `org/sonar/*`
  * matches `org/sonar/MyClass.java`
  * doesn’t match `org/sonar/util/MyClassUtil.java`
* The pattern `org/sonar/**/*`
  * matches `org/sonar/MyClass.java`
  * doesn’t match `org/radar/MyClass.java`

### Location of UI settings <a href="#location-of-ui-settings" id="location-of-ui-settings"></a>

Unless otherwise noted, all the parameters below are settable at both the global and project level. The UI locations for the settings are found under:

* **Administration** > **Configuration** > **General Settings** (for global settings)
* **Project Settings** > **General Settings** (for project-level settings)

Any setting made at the global level will apply to all projects unless overridden at the project level (the only exceptions are the global exclusion parameters discussed above).

### File exclusion and inclusion <a href="#file-exclusion-and-inclusion" id="file-exclusion-and-inclusion"></a>

If the directory structure of your project does not cleanly separate source code from test code at the top level, you may have to adjust the scope using exclusions and inclusions.

{% hint style="warning" %}
Inclusions and exclusions should not be part of the initial analysis configuration. We recommend setting them only to solve issues. For example, when you notice that an analysis picked up files that you did not want analyzed.
{% endhint %}

These are set in the UI for both global and project levels, as follows:

#### Global level <a href="#global-level" id="global-level"></a>

**Administration** > **Configuration** > **General Settings** > **Analysis Scope** > **A. File Exclusions**

* **Global Source File Exclusions**: One or more wildcard patterns defining which files are filtered out from those defined by `sonar.sources`. This setting will apply to all projects on your SonarQube server. It cannot be overridden by any project-level source file exclusion. It also cannot be set as a key in a configuration file. If it is set, it must be set in the UI.
* **Source File Exclusions**: The same as the global version above except that it *can* be overridden by a project-level source file exclusion. It cannot be set as a key in a configuration file. If it is set, it must be set in the UI.
* **Global Test File Exclusions**: Same as the Global Source File Exclusions, above, except that it applies to test files.
* **Source File Inclusions**: One or more wildcard patterns defining which files to retain, while filtering out all others, from those defined by `sonar.sources`. This applies to all projects on your SonarQube server, though it can be overridden at the project level. It cannot be set as a key in a configuration file. If it is set, it must be set in the UI.
* **Test File Exclusions**: Same as the Source File Exclusions, above, except that it applies to test files.
* **Test File Inclusions**: Same as the Source File Inclusions, above, except that it applies to test files.

#### Project level <a href="#project-level" id="project-level"></a>

**Project Settings** > **General Settings** > **Analysis Scope** > **A. File Exclusions**

* **Source File Exclusions**: One or more wildcard patterns defining which files are filtered out from those defined by `sonar.sources`. This can also be set in a configuration file using the key `sonar.exclusions`.
* **Source File Inclusions**: One or more wildcard patterns defining which files to retain, while filtering out all others, from those defined by `sonar.sources`. This can also be set in a configuration file using the key `sonar.inclusions`.
* **Test File Exclusions**: One or more wildcard patterns defining which files are filtered out from those defined by `sonar.tests`. This can also be set in a configuration file with the key `sonar.test.exclusions`.
* **Test File Inclusions**: One or more wildcard patterns defining which files to retain, while filtering out all others, from those defined by `sonar.tests`. This can also be set in a configuration file using the key `sonar.test.inclusions`.

To set these parameters by key you can:

* Set them in the configuration file `<YOUR_PROJECT>/sonar-project.properties`
* Set them on the command line when invoking the scanner.
* In the case of Maven, Gradle, or .NET projects, set them in the appropriate framework-specific configuration file.

#### How the parameter values are interpreted <a href="#how-the-parameter-values-are-interpreted" id="how-the-parameter-values-are-interpreted"></a>

The wildcard patterns are interpreted relative to the project base directory.

Exclusions and inclusions apply *on top of* the `sonar.sources` and `sonar.tests` settings. Both the exclusion and inclusion parameters act as filters. They only ever reduce the number of files in the analyzable set, they never add to the set.

#### Example <a href="#example" id="example"></a>

Let’s say your repository looks something like this, with your test code intermingled with your source code:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-0abe094b3351ef4b44056da5ce5dc5d912efc9b8%2F589e3819728f835faeab8fbe8f3606dd4d2cf5aa.png?alt=media)

You would define your `sonar.sources` like this, taking in the whole `src` directory:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-c44655d38892df303caaec88f6197fdddf22a981%2F57638cf618e8fbabea648b9a87c125657f030588.png?alt=media)

and then set **Source File Exclusions** (key `sonar.exclusions`) to

```css-79elbk
src/**/test/**/*
```

The result is that the set of source files to be scanned is everything under `src` minus every `test` subdirectory:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-097f6a28203f028e32eebe096b598e0373e89e91%2F54bcce3fe8d4221f21a6874c14b2af3aab22a470.png?alt=media)

To define the test files, first set `sonar.tests` to the whole `src` directory:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-564b38e5011d4a7118b5c842ad28de0df388e268%2Fa8fbb6d339b883d9d2885dbee28dc3c57638c20e.png?alt=media)

and then set **Test File Inclusions** (key `sonar.test.inclusions`) to

```css-79elbk
src/**/test/**/*
```

The result is that the set of source files to be scanned is everything under `src` *minus everything that is not* a `test` subdirectory:

![](https://1407932334-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5RUfx2eNg633cL6XgYzZ%2Fuploads%2Fgit-blob-965b36638a14169453cfca4b6997fb263f883a21%2Fa71717b342826487fc437f3bf19b198daa9c2a09.png?alt=media)

If you configure your scope in the `sonar-project.properties` file, it would look like this:

```css-79elbk
# Define the same root directory for sources and tests
sonar.sources = src/
sonar.tests = src/

# Include test subdirectories in test scope
sonar.test.inclusions = src/**/test/**/*

# Exclude test subdirectories from source scope
sonar.exclusions = src/**/test/**/*
```

#### Naming of parameters <a href="#naming-of-parameters" id="naming-of-parameters"></a>

Note that the initial scoping parameter for test code is `sonar.tests` (that’s `tests` with an `s`!) while the exclusion and inclusion parameters for test code are `sonar.test.exclusions` and `sonar.test.inclusions` (that’s `test`, without an `s`!).

#### Relationship with test coverage reporting <a href="#relationship-with-test-coverage-reporting" id="relationship-with-test-coverage-reporting"></a>

The test scoping parameters ( `sonar.tests`, `sonar.test.exclusion`, and `sonar.test.inclusion`) do not have anything to do with setting up test coverage reporting (see [overview](https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/test-coverage/overview "mention")). However, SonarQube will report an error if an imported coverage report lists a test file not encountered in the directories specified by the scoping parameters.

The parameter `sonar.coverage.exclusions`, on the other hand, is directly related to test coverage reporting (see below).

### Code coverage exclusion <a href="#code-coverage-exclusion" id="code-coverage-exclusion"></a>

**Analysis Scope** > **B. Code Coverage Exclusions**

This setting lets you exclude specific files or directories from code coverage reporting. The value of the parameter is a comma-delimited list of path-matching patterns relative to the current working directory.

When setting by key, use `sonar.coverage.exclusions`

### Duplication exclusions <a href="#duplication-exclusions" id="duplication-exclusions"></a>

**Analysis Scope** > **C. Duplication Exclusions**

This setting lets you exclude specific files or directories from duplication checking. The value is a comma-delimited list of path-matching patterns relative to the current working directory.

When setting by key, use `sonar.cpd.exclusions`

### Setting the scope by file type <a href="#scope-by-file-type" id="scope-by-file-type"></a>

**Languages** > *Your Language*

Most languages offer a way to restrict the scope of analysis to files matching a set of extensions. You can specify one or more suffixes (file extensions) for each language. For example, for the C language, `.c` and `.h` are set by default.

When setting by key, use the appropriate parameter of the form `sonar.<LANGUAGE>.file.suffixes`.

### Ignoring issues in files based on content <a href="#ignoring-files-based-on-content" id="ignoring-files-based-on-content"></a>

**Analysis Scope** > **D. Issue Exclusions** > **Ignore Issues on Files**

You can ignore files that contain a block of code matching a given regular expression. All issues (bugs, code smells, and vulnerabilities), as well as security hotspots, will be ignored within those files. In this setting, you can enter one or more regular expression patterns. Any file containing at least one of the specified patterns will be ignored.

For example, let’s say you have generated class files in your Java project that you wish to exclude. The files look something like this:

```css-79elbk
@Generated("com.example.generated")
public class GeneratedClass extends AnotherClass {
    // Some generated code
}
```

To exclude all such files, you might set this parameter to:

```css-79elbk
@Generated\(".*"\)
```

Note that since this value is a regular expression, you need to escape the `(` and `)` parentheses characters and use the expression `.*` match the string in between those parentheses.

The key for this parameter is `sonar.issue.ignore.allfile`, however, because it is a multi-value property, we recommend that it only be set through the UI.

### Ignoring blocks within files <a href="#ignoring-blocks-within-files" id="ignoring-blocks-within-files"></a>

**Analysis Scope** > **D. Issue Exclusions** > **Ignore Issues on Blocks**

You can ignore specific blocks of code within a file while continuing to scan the remainder of the file. Blocks to be ignored are delimited within the file by start and end strings. You specify these start and end strings by regular expressions. All issues (bugs, code smells, and vulnerabilities), as well as security hotspots within those blocks, will be ignored. You can enter one or more pairs of regular expression patterns. Any code in any file that lies between the start pattern and its corresponding end pattern will be ignored. Note that:

* If the first regular expression is found but not the second one, the end of the file is considered to be the end of the block.
* Regular expressions are not matched across multiple lines.

For example, let’s say you want to ignore the code in the method `doSomethingElse` using block delimiters, like this:

```css-79elbk
public class MyClass {
    public MyClass() {
        ...
    }

    public void doSomething() {
        ...
    }

    // BEGIN-NOSCAN
    public void doSomethingElse()
    {
        ...
    }
    // END-NOSCAN
}
```

You could specify the following regular expressions:

**Start of block**: `\s*//\s*START-NOSCAN`

**End of block:** `\s*//\s*END-NOSCAN`

These regular expressions ensure that the start and end block delimiters will be recognized regardless of the number of spaces around the line comment characters (`//`).

The key for this parameter is `sonar.issue.ignore.block`. However, because it is a multi-value property, we recommend that it only be set through the UI.

### Excluding specific rules from specific files <a href="#excluding-specific-rules-from-specific-files" id="excluding-specific-rules-from-specific-files"></a>

**Analysis Scope** > **D. Issue Exclusions** > **Ignore Issues on Multiple Criteria**

You can prevent specific rules from being applied to specific files by combining one or more pairs of strings consisting of a *rule key pattern* and a *file path pattern*.

The key for this parameter is `sonar.issue.ignore.multicriteria,` however, because it is a multi-value property, we recommend that only be set through the UI.

#### Rule key pattern <a href="#rule-key-pattern" id="rule-key-pattern"></a>

A rule key pattern consists of a rule repository name, followed by a colon, followed by a rule key, or a rule name globbing pattern.

For example:

* `java:S1195` matches exactly the [rule S1195 ](https://sonarcloud.io/organizations/sonarsource/rules?q=s1195\&open=java%3AS1195)in the Java rule repository.
* `java:*Naming*` matches all rules in the Java repository that include the string `Naming` in their rule name.

You can find the fully qualified rule ID of the rule definition and the rule name in the rule definition.

For example, for [this rule](https://sonarcloud.io/organizations/sonarsource/rules?open=css%3AS4655\&rule_key=css%3AS4655):

* Rule ID: `css:S4655`
* Rule name: *"!important" should not be used on "keyframes"*

#### File path pattern <a href="#file-path-pattern" id="file-path-pattern"></a>

A file path pattern uses the path-matching format described above to specify a set of directories or files.

#### Examples <a href="#examples" id="examples"></a>

* Ignore all issues in all files:
  * Rule key pattern: `*`
  * File path pattern: `**/*`
* Ignore all issues in the file `bank/ZTR00021.cbl`:
  * Rule key pattern: `*`
  * File path pattern: `bank/ZTR00021.cbl`
* Ignore all issues in files located directly in the Java package `com.foo`, but not in its sub-packages:
  * Rule key pattern: `*`
  * File path pattern: `com/foo/*`
* Ignore all issues against the coding rule `cpp:Union` in files in the directory `object` and its sub-directories:
  * Rule key pattern: `cpp:Union`
  * File path pattern: `object/**/*`

### Applying specific rules to specific files <a href="#applying-specific-rules-to-specific-files" id="applying-specific-rules-to-specific-files"></a>

You can only apply specific rules to specific files.

* Global level: **Administration** > **Configuration** > **General Settings** > **Analysis Scope** > **D. Issue Exclusions** > **Restrict Scope of Coding Rules**
* Project level: **Project Settings** > **General Settings** > **Analysis Scope** > **D. Issue Exclusions** > **Restrict Scope of Coding Rules**

The mechanics of setting these parameters are the same as for `sonar.issue.ignore.multicriteria`, above: Each entry consists of a rule key pattern and a file path pattern. The difference is that in this case, it means that the specified rule will only be applied to the specified set of files.

The key for this parameter is `sonar.issue.enforce.multicriteria`. However, because it is a multi-value property, we recommend that it should only be set through the UI.

#### Examples <a href="#examples" id="examples"></a>

* Only check the rule "Magic Number" on "Bean" objects and not on anything else:
  * Rule key pattern: `checkstyle:com.puppycrawl.tools.checkstyle.checks.coding.MagicNumberCheck`
  * File path pattern: `**/*Bean.java`
* Only check against the rule *Prevent GO TO statement from transferring control outside current module on COBOL programs* in the directories `bank/creditcard` and `bank/bankcard` (this restriction requires two criteria):
  * Rule key pattern 1: `cobol:COBOL.GotoTransferControlOutsideCurrentModuleCheck`
  * File path pattern 1: `bank/creditcard/**/*`
  * Rule key pattern 2: `cobol:COBOL.GotoTransferControlOutsideCurrentModuleCheck`
  * File path pattern 2: `bank/bankcard/**/*`

### SonarQube respects ignored files <a href="#sonarqube-respects-ignored-files" id="sonarqube-respects-ignored-files"></a>

Your SonarQube analysis will automatically exclude files that are ignored by your source code control system. For example, in git repositories, it respects the `.gitignore` file. SonarQube also respects the ignore directives used in SVN repositories.

This behavior can be disabled by setting

```css-79elbk
sonar.scm.exclusions.disabled = true
```

in the configuration file or command line.

Note that while SonarQube understands standard `.gitignore` directives, it does not understand `.gitignore` *negation patterns*. These are the patterns preceded by an exclamation mark(`!`). We recommend not using them in SonarQube projects.
