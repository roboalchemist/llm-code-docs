# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/ai-code-assurance/monitor-projects-with-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/ai-code-assurance/monitor-projects-with-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/ai-code-assurance/monitor-projects-with-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/ai-code-assurance/monitor-projects-with-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/ai-code-assurance/monitor-projects-with-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/ai-code-assurance/monitor-projects-with-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/monitor-projects-with-ai-code.md

# Monitor projects with AI code

Monitoring projects containing AI code is the final step in ensuring that your projects in SonarQube Cloud meet your AI Code Assurance standards.

Sonar’s AI Code Assurance helps you ensure security and code quality within projects containing AI-generated code. By utilizing project labels, custom quality gate certification and marking, and dynamic project badge publishing, you can maintain high standards and confidently assure the quality of your AI projects.

By now, you’ve likely completed the first two steps to qualify your projects as AI Code Assured:

1. [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/overview#label-projects-with-ai-code "mention")
2. [#apply-a-quality-gate-for-ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/standards/overview#apply-a-quality-gate-for-ai-code-assurance "mention")

You should be able to see your projects’ AI Code Assurance status on the **Projects** page and on each of the branch overview pages (**Overview**, **Main Branch**, **Pull Requests**, and **Branches**).

With those objectives in place, you can publish dynamic AI Code Assurance badges to your external websites to monitor projects.

### Understanding your AI Code Assurance labels <a href="#ai-code-assurance-labels" id="ai-code-assurance-labels"></a>

Your project **Overview** and **Project Information** pages show labels highlighting the state of AI Code Assurance. These labels provide a quick visual reference of your project’s state of AI Code Assurance status, including the state of containing AI-generated code and the status of your project’s quality gate.

#### Internal AI Code Assurance status <a href="#internal-ai-code-assurance-status" id="internal-ai-code-assurance-status"></a>

Here’s what each AI Code Assurance label represents, and what you can do to update the status.

![$contains-ai-code](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ca3b9de37a93a3d09c496b45878e418adab02c9f%2Fc151514ef7beca0f865ee429bc9fe0e33b05ceb4.svg?alt=media): Defined by a Project Admin that the project contains AI-generated code.

* Go to **Project settings** > **AI-generated code** or use the API to activate and deactivate this label.

![$in-shield-success](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-1be77f79e3fc37e74593f103a10b637fa15d4104%2Fdc39952837c5fcfee0e10e48781c469f3a96d50f.svg?alt=media) **AI Code Assurance passed**: Your code *is passing the quality gate qualified for AI-generated code*.

* Run a new analysis to check your code against the quality gate.

![$in-shield-error](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-53ee1c9803dcb7afc14f6b3415bb2fb6693aee82%2F9040dcf9d62138bd33f0f61a706047eee2dd041e.svg?alt=media) **AI Code Assurance failed**: Your code *is not passing the quality gate qualified for AI-generated code*.

* Address the issues in your code to meet the standards defined by your quality gate.

![$in-shield-on](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d7f52ebf82d639fd6bae4f80add21c21628c518e%2F185be81999243203ea71699933ca21b534b1d0c8.svg?alt=media) **AI Code Assurance is on**: Your code *uses a quality gate qualified for AI-generated code* and the quality gate status has not been computed.

* Run a new analysis to update the status of your quality gate.

![$in-shield-off/disabled](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-b276430a5ca86328b5104e28cdb85e6ce0276e60%2F36db0d31c4bbcfae3106b7404405d1b73b89f897.svg?alt=media) **AI Code Assurance is off**: Your code is *not marked* as containing AI code or is *not using* a quality gate qualified for AI-generated code.

* Check that your project is marked as **Contains AI-Generated Code**,
* assign a quality gate qualified for AI-generated code,
* then run an analysis to update the quality gate status.

### Using the AI Code Assurance badge <a href="#using-the-ai-code-assurance-badge" id="using-the-ai-code-assurance-badge"></a>

To complete the final objective for AI Code Assurance, add a dynamic AI Code Assurance badge to monitor the current status of your AI Code Assured projects on your web pages. This badge works like other SonarQube external badges and can be used by any team member with project access.

See the documentation on [#using-project-badge](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/managing-your-project-as-developer#using-project-badge "mention") for instructions on how to publish SonarQube badges externally.

#### External AI Code Assurance badges <a href="#external-ai-code-assurance-badges" id="external-ai-code-assurance-badges"></a>

Here’s what each AI Code Assurance badge represents, and what you should do to update the status.

![$AI Code Assurance \[sonar\] | Pass](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-f6accdfe0649afcd7fdfbf228000611c57ed1bf4%2Feb510566bfd00a317fb0b12d22ba75312a947283.svg?alt=media): Your code *is passing the quality gate qualified for AI-generated code*.

* Run a new analysis to check your code against the quality gate.

![$AI Code Assurance \[sonar\] | Fail](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-0dd716479df5fd525e80b1b631bcf2900254a481%2F175eb12b2229f37861dfa00e772b2d4ed85f387e.svg?alt=media): Your code *is not passing the quality gate qualified for AI-generated code*.

* Address the issues in your code to meet the standards defined by your quality gate.

![$AI Code Assurance \[sonar\] | On](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-fa10dba8ca8559ee9640a0f256cd8be492317080%2Fa27578006c1ca9edf322166ebcf63d17a6699a8d.svg?alt=media): Your code *is using a quality gate qualified for AI-generated code* and the quality gate status has not been computed.

* Run a new analysis to update the status of your quality gate.

![$AI Code Assurance \[sonar\] | Off](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-86f586a1a1a3cf56890b5bfa2d319dcef66926db%2F750bf1cc94f61c39fc41f300a20cf68e08889434.svg?alt=media): Your code is *not using* a quality gate qualified for AI-generated code.

* Assign a quality gate qualified for AI-generated code and run an analysis to update the quality gate status.

### Related pages <a href="#related-pages" id="related-pages"></a>

* SonarQube Cloud's [ai-capabilities](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities "mention")
* [overview](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview "mention")
* Administering your [ai-features](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features "mention") as an Organization Admin
  * Learn how to[autodetect-ai-code](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/autodetect-ai-code "mention") in projects using GitHub and GitHub Copilot
  * Quickly [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix "mention") to get AI-generated fix suggestions
