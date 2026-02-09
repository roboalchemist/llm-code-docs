# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/issues/retrieving.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/retrieving.md

# Retrieving issues

You can retrieve and view the issues detected during a project’s analysis. Ensure you have proper [#issues-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/introduction#issues-permissions "mention") on a project to view and administer the issues.

{% hint style="info" %}
Issues can also be reported in your DevOps platform. For more information, see [in-devops-platform](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/in-devops-platform "mention").
{% endhint %}

### Different ways of retrieving issues <a href="#retrieving" id="retrieving"></a>

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-8ab6ea0c87070f28cea075a4fb6d7a0c7b79c70e%2F43f8398345983d1aea4134ab5ce4d889976cf302.png?alt=media" alt="Issues are retrieved in from your branch&#x27;s Issues page or my navigating to My Issues, found in the top most menu bar."><figcaption></figcaption></figure>

1. From **My issues,** located at the top navigation bar. **My issues** lists all issues assigned to you.
2. From the **Issues** tab at a project level.
3. From the analysis report cards on branches and pull requests of your projects.
4. From the **Issues** tab at the organization level, if your organization belongs to an enterprise.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-6f07c22499b6069fc99ebaeb826194323ae8dff1%2Fdcfff6b20e687f702ca3eb74642a20b8123a32c7.png?alt=media" alt="Retrieve the issues for organization by navigating to Your Organization, and select its Issues page."><figcaption></figcaption></figure></div>

### Filtering issues <a href="#filtering-issues" id="filtering-issues"></a>

The Issues page is divided into two sections:

1. Filters are located in the left sidebar. This is where you enter your search criteria.
2. A list of issues is in the right section of the page, where your search results are displayed.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e898668d18c4c73e38f6277110aedc60d3da5159%2Fd76e984080ef3748e0fee0abc561a2f195b53792.png?alt=media" alt="The Issues page offers a set of filters on the left side of window to help you focus your retrieval efforts. The filtered list of issues will appear on the right side of the window."><figcaption></figcaption></figure></div>

#### Issue card

Each issue card contains information that helps you identify the following:

1. Project name and the path to the code file.
2. The name of the rule that triggered the issue.
3. Impacted software quality and severity level.
4. Status of the issue.
5. Assignee
6. Coding attribute
7. Tags
8. Additional information: line number, estimated time effort to fix the issue, the amount of time that has passed since the introduction of the code, and type.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-63d5e8d8bd2532125a35d6d0d77cf1f937fc6269%2F0154dc41830308ace669341ac222adbc9c5cf562.png?alt=media" alt="This image shows eight items: 1) Project name and the path to the code file. 2) The name of the rule that triggered the issue. 3) Impacted software quality and severity level. 4) Status of the issue. 5) Assignee. 6) Coding attribute. 7) Tags 8) Additional information: line number, estimated time effort to fix the issue, the amount of time that has passed since the introduction of the code, and type."><figcaption></figcaption></figure>

### Navigating issues <a href="#issues-navigating" id="issues-navigating"></a>

To navigate to an issue, select the issue card in the search results and press the Right arrow key or click on its name. A detail view of the issue opens in the right section, and the left sidebar shows the search results. To start a new search, press the Left arrow key or navigate one step back in your browser.

### Copying the URL of an issue <a href="#copying-url" id="copying-url"></a>

1. Retrieve an issue and navigate to the issue’s detail page.
2. Click on the link icon next to the name of the issue to copy the issue’s URL.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d500dddbfdd28da2dc5e7c44184195ee3fcde0a4%2F290fb350da4b4c1ddd62da987d535941f2afa6b4.png?alt=media" alt="Copying the URL of an issue is easy in SonarQube Cloud; With the issue open in your user interface, select the Copy to clipboard link symbol on the right side of the issue&#x27;s title."><figcaption></figcaption></figure></div>
