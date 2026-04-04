# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/advanced-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/advanced-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/advanced-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/advanced-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/advanced-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/advanced-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/advanced-exclusions.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/advanced-exclusions.md

# Advanced exclusions

In very specific situations, you may have to:

* Exclude files based on the file content.
* Exclude blocks within files.
* Exlude specific files from specific coding rules.

{% hint style="info" %}
It is strongly advised to configure these features in SonarQube UI. The configuration on the CI/CD host which is very tedious and implies using a set of properties is not documented in this guide.
{% endhint %}

{% hint style="info" %}
As the admin of an Enterprise plan organization, you can perform these settings as the default settings for all projects of your organization. See [advanced-exclusion-features](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/advanced-exclusion-features "mention").
{% endhint %}

### Excluding files based on file content <a href="#excluding-based-on-file-content" id="excluding-based-on-file-content"></a>

You can exclude from the analysis files that contain a block of code matching a given regular expression. You can enter one or more regular expression patterns. Any file containing at least one of the specified patterns will be ignored.

The parameter to be configured is **Ignore Issues on Files**. For a configuration example of this parameter, see below.

To define the **Ignore Issues on Files** parameter:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Analysis scope**.
3. In **Issues > Ignore Issues on Files**, enter and save a regular expression pattern.
4. You can enter a second regular expression pattern and so on.

<details>

<summary>Example of Ignore Issues on Files parameter configuration</summary>

Let’s say you have generated class files in your Java project that you wish to exclude. The files look something like this:

```java
@Generated("com.example.generated")

public class GeneratedClass extends AnotherClass {

    // Some generated code

}
```

To exclude all such files, you might set the **Ignore Issues on Files** parameter to the following regular expression: `@Generated\(".*"\)`

</details>

### Excluding blocks within files <a href="#excluding-blocks-within-files" id="excluding-blocks-within-files"></a>

You can exclude from the analysis specific blocks contained in any source file (The rest of the file will be analyzed.). The parameter to be configured is **Ignore Issues in Blocks**.

<details>

<summary>Principles governing the use of the Ignore Issues in Blocks parameter</summary>

Blocks to be ignored are delimited within the file by start and end strings specified by regular expression patterns:

* If the first regular expression is found but not the second one, the end of the file is considered to be the end of the block.
* Regular expressions are not matched across multiple lines.

Any block - within any file - containing at least one of the specified patterns will be ignored.

</details>

<details>

<summary>Defining the Ignore Issues in Blocks parameter</summary>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. Go to **Administration** > **General Settings** > **Analysis scope**.
3. In **Issues** > **Ignore Issues in Blocks**, enter and save a block definition.
4. You can enter a second block definition and so on.

</details>

<details>

<summary>Example of Ignore Issues in Blocks parameter configuration</summary>

You can use block delimiters to specify the block to be excluded as illustrated below. In this example, you want to ignore the code in the method `doSomethingElse` below delimited by `// BEGIN-NOSCAN` and `// END-NOSCAN`.

```c
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

You could define the block to be excluded with the following regular expressions:

* Start of block: `\s*//\s*START-NOSCAN`
* End of block: `\s*//\s*END-NOSCAN`

These regular expressions ensure that the start and end block delimiters will be recognized regardless of the number of spaces around the line comment characters (`//`).

</details>

### Excluding specific files from specific coding rules <a href="#excluding-from-specific-coding-rules" id="excluding-from-specific-coding-rules"></a>

This section explains how to exclude specific files from specific coding rules in your project analysis.

<details>

<summary>Introduction to coding rules exclusion</summary>

To exclude specific files from specific coding rules, you can:

* Exclude specific files from the check against specific coding rules.\
  To do so, you define exclusion criteria. An exclusion criterion is a combination of:
  * A coding rule key pattern: specifies the coding rules to be excluded.
  * A file path pattern: specifies the files to which the specified coding rules will not be applied.
* Apply the check against specific coding rules to specific files. It means that the other files are excluded from this check.\
  To do so, you define inclusion criteria. An inclusion criterion is a combination of:
  * A coding rule key pattern: specifies the coding rules to be applied.
  * A file path pattern: specifies the files to which the specified rules will be applied. The specified rules will not be applied to the other files.

</details>

<details>

<summary>Defining coding rule inclusion or exclusion criteria</summary>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for details.
2. Go to **Administration** > **General Settings** > **Analysis scope**.
3. In the **Issues** > **Ignore Issues on Multiple Criteria** parameter (to define an exclusion criterion), or in the **Issues** > **Restrict Scope of Coding Rules** (to define an inclusion criteria), enter and save a pair consisting of, see [defining-matching-patterns](https://docs.sonarsource.com/sonarqube-cloud/appendices/defining-matching-patterns "mention"):
   * A pattern for coding rule keys.
   * A pattern for file paths.
4. You can add a second criterion, and so on.

</details>

<details>

<summary>Examples of Ignore Issues on Multiple Criteria parameter configuration (inclusion criterion)</summary>

| **Example**                                                                                                                                                                             | **Inclusion criterion**                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>Check:</p><p>• The coding rule "compareTo" should not be overloaded"</p><p>• Only on "Bean" objects and on nothing else.</p>                                                         | <p>• Rule key pattern: java:s4351</p><p>• File path pattern: \*\*/\*Bean.java</p>                                                                                                                                                                                                                                                          |
| <p>Check:</p><p>• The coding rule "GO TO DEPENDING ON should not be used" in COBOL.</p><p>• Only on files in the directories bank/creditcard and bank/bankcard and on nothing else.</p> | <p>Two criteria must be used.</p><p>Criterion 1:</p><p>• Rule key pattern: cobol:S4883</p><p>• File path pattern: bank/creditcard/<strong>/</strong></p><p><em><strong>Criterion 2:</strong></em></p><p><em><strong>• Rule key pattern: cobol:S4883</strong></em></p><p><em><strong>• File path pattern: bank/bankcard/</strong>/</em></p> |

</details>

<details>

<summary>Examples of Restrict Scope of Coding Rules parameter configuration (exclusion criterion)</summary>

| Example                                                                                                                                                   | Exclusion criterion                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| <p>Ignore:</p><p>• All coding rules.</p><p>• In all files.</p>                                                                                            | <p>• Rule key pattern:</p><p><em>• File path pattern: \*\*/</em></p>           |
| <p>Ignore:</p><p>• All coding rules.</p><p>• In the file bank/ZTR00021.cbl.</p>                                                                           | <p>• Rule key pattern: \*</p><p>• File path pattern: bank/ZTR00021.cbl</p>     |
| <p>Ignore:</p><p>• All coding rules.</p><p>• In files located directly in the Java package com.foo, but not in its sub-packages.</p>                      | <p>• Rule key pattern:</p><p><em>• File path pattern: com/foo/</em></p>        |
| <p>Ignore:</p><p>• The C++ coding rules where the word "union" appears in the name.</p><p>• In files in the directory object and its sub-directories.</p> | <p>• Rule key pattern: cpp:Union</p><p>• File path pattern: object/\*\*/\*</p> |

</details>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [setting-initial-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/setting-initial-scope "mention")
* [exclude-from-coverage-duplication](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/exclude-from-coverage-duplication "mention")
* [excluding-files-based-on-patterns](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-files-based-on-patterns "mention")
* [excluding-based-on-file-extension](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/excluding-based-on-file-extension "mention")
* [other-adjustments](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/other-adjustments "mention")
* [verifying-analysis-scope](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/setting-analysis-scope/verifying-analysis-scope "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/setting-config-at-org-level/adjusting-analysis-scope/introduction "mention") to Adjusting analysis scope
