# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration.md

# Project administration

- [Creating your project](/sonarqube-server/project-administration/creating-your-project.md): How to create your project in SonarQube Server.
- [Importing your DevOps platform repository](/sonarqube-server/project-administration/creating-your-project/importing-repo.md): Creating and importing projects from a DevOps platform repository.
- [Automating project creation and import](/sonarqube-server/project-administration/creating-your-project/automating-project-creation-and-import.md): When you have a large project base, it can be beneficial to automate project creation and import using the Web API.
- [Creating your project manually](/sonarqube-server/project-administration/creating-your-project/creating-project-manually.md): For a project not linked to a DevOps platform, you can create your SonarQube project manually.
- [Setting project permissions](/sonarqube-server/project-administration/setting-project-permissions.md): Setting up your permissions and creating permission templates.
- [Setting up project features](/sonarqube-server/project-administration/setting-up-features.md): How to set up various features for your project.
- [DevOps platform integration features](/sonarqube-server/project-administration/setting-up-features/devops-platform-integration.md): Setting up DevOps integration features for your project.
- [Managing project tags](/sonarqube-server/project-administration/setting-up-features/managing-project-tags.md): SonarQube Server's Project Tags allow you to categorize and group projects for easier selection on the Projects page.
- [Customizing Project Information page](/sonarqube-server/project-administration/setting-up-features/customizing-project-information-page.md): Managing project links on the project information page.
- [Setting various features at project level](/sonarqube-server/project-administration/setting-up-features/project-settings.md): Changing and customizing your project’s settings.
- [Adjusting project analysis](/sonarqube-server/project-administration/adjusting-analysis.md): How to adjust the analysis parameters and quality standards of your SonarQube Server project.
- [Setting analysis scope](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope.md): Setting and managing your analysis scope.
- [Introduction](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/introduction.md): Main steps for setting the project's analysis scope.
- [Setting initial scope](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/setting-initial-scope.md): Setting the initial scope of analysis for your project's source and test files.
- [Excluding based on path-matching patterns](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/excluding-files-based-on-patterns.md): Adjust your project’s initial analysis scope by excluding files based on path-matching patterns.
- [Excluding based on file extension](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/excluding-based-on-file-extension.md): For each programming language, define the file extensions to be analyzed.
- [Excluding from coverage or duplication](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/exclude-from-coverage-duplication.md): Exclude specific files from your project's code coverage analysis or duplication checks.
- [Applying advanced exclusions](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/advanced-exclusions.md): Tailor your project's analysis by applying advanced exclusions based on file content, specific code blocks, and defined coding rules.
- [Other adjustments](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/other-adjustments.md): Adjust your project's analysis based on secret detection scope, file size, and SCM file ignore patterns.
- [Verifying analysis scope](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/verifying-analysis-scope.md): Review configured properties and properties identified by the SonarScanner to determine your SonarQube project's analysis scope.
- [Defining matching patterns](/sonarqube-server/project-administration/adjusting-analysis/setting-analysis-scope/defining-matching-patterns.md): Define matching patterns for files and coding rules.
- [Managing your project's quality gate](/sonarqube-server/project-administration/adjusting-analysis/changing-quality-gate-and-fudge-factor.md): Changing your project's default quality gate and other parameters or features impacting your quality gate.
- [Changing your project's quality profiles](/sonarqube-server/project-administration/adjusting-analysis/changing-quality-gate.md): Changing the project's default quality profile.
- [Configuring new code calculation](/sonarqube-server/project-administration/adjusting-analysis/configuring-new-code-calculation.md): Configuring your project’s new code definition.
- [Maintaining your project](/sonarqube-server/project-administration/maintaining-project.md): How to perform various maintenance tasks on your SonarQube Server project.
- [Maintaining project branches](/sonarqube-server/project-administration/maintaining-project/maintaining-the-branches-of-your-project.md): Manage your project’s branches to fit the needs of your organization and workflow.
- [Managing project history](/sonarqube-server/project-administration/maintaining-project/managing-project-history.md): Manage your project’s history by editing and deleting snapshots of your project.
- [Changing the project key](/sonarqube-server/project-administration/maintaining-project/changing-project-key.md): You can update the project key without losing the history of the project.
- [Project move](/sonarqube-server/project-administration/maintaining-project/project-move.md): Project Move allows you to export a project from one SonarQube Server instance and import it into another SonarQube Server instance.
- [Deleting your project](/sonarqube-server/project-administration/maintaining-project/deleting-project.md): You can delete one or multiple projects, provided you have the necessary permissions to do so.
- [Changing your project binding](/sonarqube-server/project-administration/maintaining-project/changing-project-binding.md): You can bind an unbound project and you can change the binding of a bound project.
- [Managing monorepo projects](/sonarqube-server/project-administration/monorepos.md): Managing monorepo projects, a feature supported by SonarQube for GitHub and GitLab repositories.
- [Jira Cloud integration](/sonarqube-server/project-administration/jira-integration.md): Binding a SonarQube project with a Jira Cloud project.
- [AI features](/sonarqube-server/project-administration/ai-features.md): These pages contain information about administering SonarQube Server's AI features at the project level.
- [Overview](/sonarqube-server/project-administration/ai-features/overview.md): SonarQube Server provides a series of tools to help you identify, manage, and use AI-generated code in your projects.
- [Set up AI Code Assurance](/sonarqube-server/project-administration/ai-features/set-up-ai-code-assurance.md): Manage your AI Code Assurance standards using the SonarQube API.
- [AI CodeFix](/sonarqube-server/project-administration/ai-features/enable-ai-codefix.md): SonarQube's AI CodeFix service can suggest fixes for a select set of rules in Java, JavaScript, TypeScript, Python, C#, and C++ and can be enabled at the project level.
- [Configuring webhooks](/sonarqube-server/project-administration/webhooks.md): SonarQube webhooks notify external services when a project analysis is complete.
- [Managing portfolios](/sonarqube-server/project-administration/managing-portfolios.md): Setting up and managing portfolios in SonarQube Server.
- [Managing applications](/sonarqube-server/project-administration/managing-applications.md): Setting up and managing applications in SonarQube Server.
