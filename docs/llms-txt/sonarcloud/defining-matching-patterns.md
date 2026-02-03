# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/adjusting-analysis/setting-analysis-scope/defining-matching-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/setting-analysis-scope/defining-matching-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/setting-analysis-scope/defining-matching-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/setting-analysis-scope/defining-matching-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/setting-analysis-scope/defining-matching-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/adjusting-analysis/setting-analysis-scope/defining-matching-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/defining-matching-patterns.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/appendices/defining-matching-patterns.md

# Defining matching patterns

### Defining matching patterns for files <a href="#for-files" id="for-files"></a>

To define path-matching patterns, you can use the following wildcards:

* `*` matches zero or more characters (not including the directory delimiter, `/`).
* `**` matches zero or more directory segments within the path.
* `?` matches a single character (not including the directory delimiter, `/`).

A file path definition is either relative to the sonar.projectBaseDir property, which is by default the directory from which the analysis was started, or absolute. See [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") for more information.

The table below shows path-matching pattern examples.

| **Matching pattern**               | **Definition**                                                                                                                     |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `**/*.css`                         | `<anyDirectory>/<anyFileName>.css`                                                                                                 |
| `**/*Bean.java`                    | <p><code>\<anyDirectory>/\<anyString>Bean.java</code></p><p>Example: <code>org/sonar.api/MyBean.java</code></p>                    |
| `**/*Bean?.java`                   | <p><code>\<anyDirectory>/\<anyString>Bean\<singleCharacter>.java</code></p><p>Example: <code>org/sonar.api/MyBean1.java</code></p> |
| `org/sonar/*`                      | `org/sonar/<anyFile>`                                                                                                              |
| `org/sonar/**` or `org/sonar/**/*` | <p><code>org/sonar/\<anyDirectory>/\<anyFile></code></p><p>Example: <code>org/sonar/api/test/Bean.java</code></p>                  |

### Defining matching patterns for coding rules <a href="#for-coding-rules" id="for-coding-rules"></a>

To define matching patterns for coding rules, use the following syntax:

`<ruleRepository>:<searchString>`

Where:

* ruleRepository: is the identifier of the rule repository\
  Examples: SonarQube java (identifier: java) or Security SonarAnalyzer PHP (identifier: phpsecurity), etc.\
  You can use the wildcard pattern \* (any string) to define the rule repository.
* searchString: is any search string present in the rule key or in the rule name

The matching pattern means that any rule:

* of the specified repository
* whose name or key contains the specified search string

is a match.

<details>

<summary>Rule-matching pattern examples</summary>

| **Rule-matching pattern** | **Description**                      |
| ------------------------- | ------------------------------------ |
| `css:S4655`               | Rule ID s4655 in the repository css. |
| `*:S4655`                 | Rule ID s4655 in any repository.     |
| `*`                       | All rules.                           |

</details>

<details>

<summary>Identifying the repository, name, and key of a rule</summary>

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Go to **Rules**.
3. Use the filter on the left to search for a rule. The search results are displayed in the right panel.
4. In the search results, click the rule you want to view. The rule opens and you can see the rule parameters.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e5661d0fd3303fd7e47d3a14d5aae682cba8fdc2%2F564c9ad456df69d4d1596e964ecba5205eceb19d.png?alt=media" alt="The rule name, rule ID, and the repository to which the rule belongs are all available when selecting an issue in the SonarQube Cloud UI." width="563"><figcaption></figcaption></figure></div>

</details>
