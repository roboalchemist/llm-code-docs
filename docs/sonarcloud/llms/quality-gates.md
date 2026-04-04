# Source: https://docs.sonarsource.com/sonarqube-server/8.9/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/user-guide/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/analysis-functions/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/analysis-functions/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/quality-gates.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/improving/quality-gates.md

# Quality gates

A quality gate is an indicator that tells you whether your code meets the minimum level of quality required for your project. It consists of a set of conditions that are applied to the results of each code analysis and review. If the analysis results meet or exceed the quality gate conditions then it shows a **Passed** status otherwise, it shows a **Failed** status. For more information, see [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention").

### Quality gates appear with analysis results <a href="#quality-gates-appear-with-analysis-results" id="quality-gates-appear-with-analysis-results"></a>

Quality gates are displayed in the SonarQube Cloud interface along with the code review and analysis results of the main branch of the project, other non-main branches, and pull requests.

For pull requests, the quality gate will also be displayed in the repository platform as a pull request decoration.

The quality gates will indicate a **Passed** or **Failed** status (or if not properly set up, a **Not Computed** status, see below)

For example, go to **Main Branch** > **Summary** > **Quality Gate**; here you can see the quality gate for the main branch of a project with a **Passed** status:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ef3bfbae8f1d679ac12bfe8a6af754ca610231ee%2Faf768ec73f0e62101745c719efe4f9c243d94143.png?alt=media" alt="The Main Branch Summary page gives you an overall status of the issues found in your project."><figcaption></figcaption></figure></div>

If you are using the [connected-mode](https://docs.sonarsource.com/sonarqube-cloud/improving/connected-mode "mention"), changes to your main branch quality gate will also appear as notifications in your IDE (this only works if you have configured SonarQube for IDE to connect to your SonarQube Cloud account).

### When is a quality gate not computed? <a href="#when-is-a-quality-gate-not-computed" id="when-is-a-quality-gate-not-computed"></a>

There are two main reasons why the quality gate may not be computed:

* You have performed only one analysis on your code (the quality gate is computed after the second analysis).
* No new code definition is set up for the project. This may only occur for projects created a long time ago since in the recent versions of SonarQube Server you cannot create a new project without setting up the new code definition.

If the quality gate has not been computed then the **Not computed** message is displayed in the place where the quality gate status usually appears as illustrated below.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e6278f5731d367bcc10206df16751b6251a5163c%2F700624709bc9524ba843caa9797629feabc37b3c.png?alt=media" alt="You will see this banner when the SonarQube Cloud quality gate has not been computed." width="563"><figcaption></figcaption></figure></div>

The **Set New Code Definition** button is displayed as well in case no new code definition is set up. To fix this, click the button. For more details on setting up the definition, see [about-new-code](https://docs.sonarsource.com/sonarqube-cloud/standards/about-new-code "mention") page.

### How quality gates are used <a href="#how-quality-gates-are-used" id="how-quality-gates-are-used"></a>

The purpose of the quality gate is to tell you whether your code is good enough to be pushed to the next step:

* For the main branch and other long-lived branches, the quality gate answers the question: "Can I release my code today?"
* For pull requests (and short-lived branches), the quality gate answers the question: "Can I merge this pull request?"

By keeping an eye on the quality gate you can quickly judge the status of your code and decide on what to do next.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/introduction-to-quality-gates "mention")
* [notifications](https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications "mention")
* [viewing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/viewing-quality-gate "mention")
* [managing-custom-quality-gates](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/managing-custom-quality-gates "mention")
* [changing-default-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/changing-default-quality-gate "mention")
* [associating-projects-with-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-gates/associating-projects-with-quality-gate "mention")
* [changing-quality-gate](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/changing-quality-gate "mention")
