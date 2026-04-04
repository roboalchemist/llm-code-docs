# Source: https://docs.sonarsource.com/sonarqube-cloud/improving/main-branch-analysis.md

# Main branch analysis

SonarQube Cloud analyzes the **Main Branch** every time a change is made to it. Select **My Projects** in the global navigation and choose your project from the list to see the results. By default, the **Project Overview** is displayed. This view includes three sections:

1. **Latest Activity**: A summary of recent analyses performed on your project.
2. **Main Branch Status**: The quality gate status of your main branch, **Passed**, **Failed**, or **Not Computed**.
3. **Main Branch Evolution**: A summary of the code quality results for the main branch of your project.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-2842bf2d399bb8db495ab341947105ad07b3faa5%2F0990580234f9925176b53952bb2ef3ecc234b5d2.png?alt=media" alt="Your Project&#x27;s Overview page will show you the Latest Activity, Main Branch Status, and the Main Branch Evolution over time."><figcaption></figcaption></figure></div>

On the left side of the page, go to **Main Branch** to see a detailed breakdown of the results for the main branch of your project.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-51a8426237178d3b63c1cc51d805b848679721e8%2Fe79f23744132db4cd4a9e88966620696f11f7431.png?alt=media" alt="To see the analysis details of your Main Branch, select it from the left side bar."><figcaption></figcaption></figure></div>

### Quality gate <a href="#quality-gate" id="quality-gate"></a>

The quality gate status for your main branch is displayed under the **Summary** tab of the **Main Branch** view. It shows the releasability status of the main branch of your project, answering the question, "Can I release my project today?"

A quality gate consists of a set of conditions like "Reliability is rated at least A", "Maintainability is rated at least B", and "Test coverage is at least 80%". These conditions are applied to analysis results to determine whether the code meets the level of quality required.

If the main branch meets or exceeds the quality gate conditions, it displays a **Passed** status:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e19033f4e6467524df27c596a6645d8c72d72848%2Fb30d4ecef2b5a2536eb73de0e2ab793309768f0f.png?alt=media" alt="You will see this banner when the quality gate has failed." width="563"><figcaption></figcaption></figure></div>

If the main branch does not meet the quality gate conditions, it displays a **Failed** status:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-eda84495f351cd72fd35fcce01beb31dd07694c2%2F93c32f86776753bc35103990710bd20553af26e7.png?alt=media" alt="You will see this banner when the quality gate has passed." width="563"><figcaption></figcaption></figure></div>

### Setting a new code definition <a href="#setting-a-new-code-definition" id="setting-a-new-code-definition"></a>

Initially, when you start a new project, you may end up performing an analysis without first setting a new code definition. Selecting a new code definition for your project is an essential part of setting up SonarQube Cloud. Without one, the default quality gate won’t work. In this case, the system directs you to set up your new code definition, like this:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e6278f5731d367bcc10206df16751b6251a5163c%2F700624709bc9524ba843caa9797629feabc37b3c.png?alt=media" alt="You will see this banner when the SonarQube Cloud quality gate has not been computed." width="563"><figcaption></figcaption></figure></div>

What counts as new code can differ from project to project, so SonarQube Cloud provides a few options. We strongly encourage all users to choose a new code definition suitable for their project.

Once you have set up a new code definition and performed another analysis, the quality gate status should appear. See [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") for more information.

### Built-in quality gate <a href="#built-in-quality-gate" id="built-in-quality-gate"></a>

SonarQube Cloud provides a built-in quality gate, called the *Sonar way* quality gate, enabled on the main branch by default. This quality gate reflects Sonar’s recommended settings. However, your requirements may differ, so you may wish to define a custom quality gate. For details see the [quality-gates](https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates "mention") page.

### New code quality measures <a href="#new-code-quality-measures" id="new-code-quality-measures"></a>

When you first look at a newly analyzed project, it can be challenging to decide where to start fixing issues. To help with this, SonarQube Cloud encourages you to focus your efforts on *new code*. This is why we encourage users to set a suitable new code definition for their project.

To help you focus on recently changed code, the main branch summary displays a specific tab for new code.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-07bea7876c5d18287624e8808ab894a78ab81416%2F8b005f70c68ba203c2100fdaf14bfb9725ffc035.png?alt=media" alt="The Main Branch Summary page will show you the status of your analysis against the quality gate."><figcaption></figcaption></figure></div>

Note that the new code quality measures (and any quality gate that relies on them, like the default quality gate) will only appear upon the *second* analysis performed *after* a new code definition has been set.

### Overall code quality measures <a href="#overall-code-quality-measures" id="overall-code-quality-measures"></a>

In addition to new code quality measures, the main branch summary also displays the **Overall Code** quality measures in another tab. This tab shows the issues found in *all code*, including new code.

### Measures categories <a href="#measures-categories" id="measures-categories"></a>

The measures themselves are displayed as tiles corresponding to the following categories:

* **Reliability**: Details of issues with an impact on the reliability of your software.
* **Maintainability**: Details of issues with an impact on the maintainability of your software.
* **Security**: Details of issues with an impact on the security of your software.
* **Accepted issues**: Accepted issues. See the [solution-overview](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/issues/solution-overview "mention") for more details.
* **Coverage**: Displays the percentage of potentially testable lines of code that are *actually* covered by test cases. The lines of code that *could* be covered are referred to as the **lines to cover**. Of those **lines to cover**, those that are currently *not covered* are referred to as the **uncovered lines**. The coverage percentage calculation is, therefore: `coverage = 100 - (100 * uncovered_lines / lines_to_cover)`. Note that **lines to cover** only counts lines that are included in the coverage report and testable (for example, lines that are only composed of `}` are not counted). This differs from how duplicated lines are counted. For more details see the [overview](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/overview "mention") of the test coverage page.
* **Duplications**: Identical lines of code detected. All lines of code into account (including non-testable lines). Since this differs from how coverage lines are counted, the final count for the two metrics may differ.
* **Security Hotspots**: Security-sensitive hotspots needing review.

Clicking on any figure takes you to a more detailed view, either in the **Measures** tab or the **Issues** tab.

### Other tabs <a href="#other-tabs" id="other-tabs"></a>

*Your Project* > **Main Branch** > **Issues**

* The **Issues** tab provides an overview of all the issues detected by the analysis and lets you filter the list by adjusting the facets on the left.

*Your Project* > **Main Branch** > **Security Hotspots**

* The **Security Hotspots** tab provides information on detected [security-hotspots](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/security-hotspots "mention").

*Your Project* > **Main Branch** > **Measures**

* The **Measures** tab shows all project metrics. Choose a measure for more details. Both list and tree views are available for each measure, and tree maps are available for percentages and ratings.

*Your Project* > **Main Branch** > **Code**

* The **Code** tab takes you to an outline of your project structure. Drill down to see files in a directory, and choose a file to see its code. If your project is too large for easy exploration via drilling down, the search feature on this page lets you search within the files and directories in the current project.

*Your Project* > **Main Branch** > **Activity**

* The **Activity** tab takes you to the full list of code scans performed on your project since it was created in SonarQube Cloud. Here you can follow the evolution of the quality gate, see the changes of quality profiles and find out when a given version of your code has been scanned.

**Visualizations** allow you to compare project components and quickly spot the ones that represent the most significant risks. Several predefined visualizations are available. You can also create custom ones with the metrics of your choice.

*Your Project* > **Administration**

* If you are a project administrator, the **Administration** menu gives you access to all project-level settings.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-dd797a8309d7a69fe188e4251f01c393b2abdbc2%2F9c7d6945d3ef519c70c90121b521fc4ced8bee40.png?alt=media" alt="Project administrators can access the project settings, found under Administration in the left sidebar."><figcaption></figcaption></figure></div>

*Your Project* > **Information**

* The **Information** page provides additional details on various aspects of your project including an option to download regulatory reports. See [viewing-project-regulatory-reports](https://docs.sonarsource.com/sonarqube-cloud/getting-started-with-enterprise/viewing-enterprise-reports/viewing-project-regulatory-reports "mention") for more details.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-f919829597e9a503ea257c7cb37e26c1e5585f9b%2Ff764a2b00b329f8130b42fec980a6b7bc7570563.png?alt=media" alt="The Information page is accessible from the left side bar and shows you key details about your project such as the Project and Organization Keys."><figcaption></figcaption></figure></div>

### Other analysis views <a href="#other-analysis-views" id="other-analysis-views"></a>

In this section, we looked at how the results of **Main Branch** analysis are displayed. In addition, you can also access the code review and analysis results of **Pull Requests** and other **Branches** through the project navigation on the left side of the screen.

For details on these topics see the [branch-analysis](https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis "mention") and [pull-request-analysis](https://docs.sonarsource.com/sonarqube-cloud/improving/pull-request-analysis "mention") sections.

### Incremental analysis <a href="#incremental-analysis" id="incremental-analysis"></a>

Some analyzers use the analysis cache mechanism to shorten the main branch analysis. See [incremental-analysis-mechanisms](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/incremental-analysis-mechanisms "mention") for more information.
