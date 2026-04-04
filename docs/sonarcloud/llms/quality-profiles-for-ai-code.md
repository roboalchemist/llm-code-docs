# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/ai-code-assurance/quality-profiles-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/ai-code-assurance/quality-profiles-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/ai-code-assurance/quality-profiles-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/ai-code-assurance/quality-profiles-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/ai-code-assurance/quality-profiles-for-ai-code.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/quality-profiles-for-ai-code.md

# Quality profiles for AI code

### Overview <a href="#overview" id="overview"></a>

SonarQube Cloud’s AI Code Assurance features help you set appropriate standards for projects containing AI-generated code. The process begins with [#label-projects-with-ai-code](https://docs.sonarsource.com/sonarqube-cloud/standards/overview#label-projects-with-ai-code "mention") and continues with [#apply-a-quality-gate-for-ai-code-assurance](https://docs.sonarsource.com/sonarqube-cloud/standards/overview#apply-a-quality-gate-for-ai-code-assurance "mention"). The final step involves assigning a quality profile recommended for AI Generated code to assign a collection of rules applied during an analysis.

If you need more information about what a quality profile does, please read [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention"). There, you’ll learn how quality profiles are assigned by language, what the inheritance tree looks like, and how to profiles are associated with projects.

### Quality profiles for AI code <a href="#quality-profiles-for-ai-code" id="quality-profiles-for-ai-code"></a>

The Sonar way quality profile and its derivatives are excellent choices for AI-generated code. Leveraging the Sonar way provides a solid foundation, and extending it allows for tailored rule sets to further enhance coverage. While the Sonar way profile currently features the recommended for AI-generated code badge ![$in-shield-on](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d7f52ebf82d639fd6bae4f80add21c21628c518e%2F185be81999243203ea71699933ca21b534b1d0c8.svg?alt=media), we are actively working to broaden this recognition to include customized profiles in upcoming releases. Using Sonar way is a great starting point for setting up robust analysis for projects with AI code and allows for the creation and assignment of custom profiles that meet specific needs.

#### Recommendations on custom quality profiles for AI code <a href="#recommendations-on-custom-quality-profiles-for-ai-code" id="recommendations-on-custom-quality-profiles-for-ai-code"></a>

The Sonar way quality profile is recommended for projects containing AI-generated code. It and any of its derivatives, which may apply more rules than the parent to an analysis, are recommended for AI code. The Sonar way is recommended because it contains the most optimum rules and thresholds for most projects, and helps detect issues at scale that might be introduced by the injection of AI-generated code.

If you want to add rules or avoid unexpected changes on the BUILT-IN profile, copy the Sonar way and modify it to fit your workflow. Choosing a different quality profile will not affect your AI Code Assurance status.

### Assigning a quality profile for AI code <a href="#assigning-a-quality-profile-for-ai-code" id="assigning-a-quality-profile-for-ai-code"></a>

The "Sonar way" profile comes BUILT-IN and ready to use for every programming language. If you haven’t changed your default settings, this profile will automatically be applied to all new projects you create.

You aren’t required to use a profile recommended for AI-generated code to get the benefits of AI Code Assurance. However, using one is highly encouraged as it helps keep all your projects consistent and organized.

#### Assign profiles by project <a href="#assign-profiles-by-project" id="assign-profiles-by-project"></a>

To assign a quality profile recommended for AI code to multiple languages by project, navigate to the *Your project* > **Administration / Quality profiles** page. Under each language you have in your project, select a profile that’s a derivative of the Sonar way.

#### Assign profiles by language <a href="#assign-profiles-by-language" id="assign-profiles-by-language"></a>

To set an AI Code Assured profile for multiple projects by language, go to the *Your organization* > **Quality profiles** page and pick the language you want to update. You’ll likely see the default *Sonar way* profile, or if it’s been copied or extended, you’ll also see those versions.

Next, with your desired profile chosen, select **Change Projects**. Adjust the filters to see a list of your projects. Then, just check or uncheck the boxes to select or deselect projects and select **Close**. If the changes don’t show up right away, refresh the page.

Remember, after assigning a new quality profile, you’ll need to run a new analysis to see the update on the project’s **Information** page.

For detailed instructions about assigning quality profiles, check out the [associating-a-quality-profile-with-projects](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/associating-a-quality-profile-with-projects "mention") page.

### Customizing a quality profile for AI code <a href="#customizing-a-quality-profile-for-ai-code" id="customizing-a-quality-profile-for-ai-code"></a>

Any derivative of the Sonar way can be extended to cover more rules and catch more issues. Please see the [creating-a-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/creating-a-quality-profile "mention") page for complete details.

Remember that at this time, only the Sonar way carries the recommended for AI-generated code badge ![$in-shield-on](https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-d7f52ebf82d639fd6bae4f80add21c21628c518e%2F185be81999243203ea71699933ca21b534b1d0c8.svg?alt=media); the ability to assign that badge to custom profiles is on our development roadmap.

### Related pages <a href="#related-pages" id="related-pages"></a>

* SonarQube Cloud's [ai-capabilities](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities "mention")
* [overview](https://docs.sonarsource.com/sonarqube-cloud/standards/ai-code-assurance/overview "mention")
* Administering your [ai-features](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features "mention") as an Organization Admin
  * Learn how to[autodetect-ai-code](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/autodetect-ai-code "mention") in projects using GitHub and GitHub Copilot
  * Quickly [enable-ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/ai-features/enable-ai-codefix "mention") to get AI-generated fix suggestions
