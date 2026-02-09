# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/long-lived-branch-pattern.md

# Long-lived branch pattern

SonarQube Cloud considers a branch to be long-lived if:

* It is the main branch, or
* Its name matches the long-lived branch name pattern.

All other branches are considered short-lived.

{% hint style="warning" %}
The type of a branch (long-lived or short-lived) is set during its first analysis and cannot be changed afterward.
{% endhint %}

If your project belongs to an Enterprise plan organization, its long-lived branch name pattern is by default the pattern set at the organization level. You can change it.

The name pattern is based on a regular expression. For example, the regular expression: *`(branch|release)-.*`* matches any name that begins with the string `branch-` or `release-`.

<details>

<summary>Changing the long-lived branch pattern of your project</summary>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left navigation bar, select **Branches**.
3. In the top-right corner, select the edit icon on the right of **Long-lived branches pattern**. The **Detection of long-lived branches** dialog opens as illustrated below (in the case of an enterprise plan organization).
4. Enter your regular expression.
5. Select **Save**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-3b21f9e7eaeb2080ccf0e1a9a724c973531d8dea%2F7ef540717a76d8543fbb7aa0cf52500c9d896439.png?alt=media" alt="When selecting the Edit icon in the upper right corner of your SonarQube Cloud project&#x27;s Branches page, you will see if the saved detection pattern is your Organization&#x27;s default pattern." width="563"><figcaption></figcaption></figure></div>

</details>

<details>

<summary>Resetting the long-lived branch pattern to default</summary>

If your project belongs to an Enterprise plan organization, you may want to reset the long-lived branch to the default set at the organization level. To do so:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left navigation bar, select **Branches**.
3. In the top-right corner, select the edit icon on the right of **Long-lived branches pattern**. The **Detection of long-lived branches** dialog opens.
4. Select **Reset to default**.

</details>
