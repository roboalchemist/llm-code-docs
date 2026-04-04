# Source: https://learn.microsoft.com/en-us/azure/devops/release-notes

Title: Azure DevOps Roadmap

URL Source: https://learn.microsoft.com/en-us/azure/devops/release-notes

Markdown Content:
* * *

| [What's New](https://aka.ms/azuredevops/releasenotes) | [Developer Community](https://developercommunity.visualstudio.com/spaces/21/index.html) | [DevOps Blog](https://devblogs.microsoft.com/devops/) | [Documentation](https://learn.microsoft.com/en-us/azure/devops/?view=azure-devops&preserve-view=true) |

* * *

This feature list is a peek into our roadmap. It identifies some of the significant features we are currently working on and a rough timeframe for when you can expect to see them. It is not comprehensive but is intended to provide some visibility into key investments. At the top you will find a list of our large multi-quarter initiatives and the features that they break down into. Further down you will find the full list of significant features we have planned.

Each feature is linked to an article where you can learn more about a particular item. These features and dates are the current plans and are subject to change. The Timeframe columns reflect when we expect the feature to be available.

GitHub Advanced Security for Azure DevOps (GHAzDO) brings additional security features to Azure DevOps under an additional license. Any project collection administrator can now enable Advanced Security for their organization, projects and repos from the Project Settings or Organization Settings.

The main capabilities of GitHub Advanced Security for Azure DevOps are:

*   _Secret Scanning:_ Detect and remediate plaintext secrets in your git repositories. If push protection is enabled, it also detects and blocks secrets before they are pushed to your repositories.
*   _Code Scanning:_ Search for potential security vulnerabilities and coding errors in your code using CodeQL or a third-party tool.
*   _Dependency Scanning:_ Detect and alert when your code depends on a package that is insecure and receive straightforward remediation guidance.

You can learn more about how to configure GitHub Advanced Security for Azure DevOps in our [documentation](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features).

Upcoming capabilities we expect to deliver include:

| Feature | Area | Quarter |
| --- | --- | --- |
| [Determine detected partner secrets validity](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/ghazdo/secret-validity) | GitHub Advanced Security for Azure DevOps | ![Image 1: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q3 |
| [Link Boards items to Advanced Security Alerts](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/ghazdo/boards-linking) | GitHub Advanced Security for Azure DevOps | ![Image 2: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q4 |
| [Status check policies for Advanced Security alerts](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/ghazdo/status-check) | GitHub Advanced Security for Azure DevOps | 2026 Q1 |
| [CodeQL default setup (one-click enablement)](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/ghazdo/default-setup) | GitHub Advanced Security for Azure DevOps | 2026 Q2 |
| [Automatically fix detected dependency scanning vulnerabilities with Dependabot security updates](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/ghazdo/dependabot) | GitHub Advanced Security for Azure DevOps | Future |

Azure DevOps supports many different authentication mechanisms, including basic authentication, personal access tokens (PATs), SSH, and Microsoft Entra ID (formerly Azure Active Directory) access tokens. These mechanisms are not created equally from a security perspective, especially when it comes to the potential for credential theft. For example, unintended leakage of credentials like PATs can let malicious actors into Azure DevOps organizations where they can gain access to critical assets like source code, pivot toward supply chain attacks, or even pivot toward compromising production infrastructure. To minimize the risks of credential theft, we will focus our efforts in the upcoming quarters in the following areas:

*   Enable administrators to improve authentication security through control plane policies.

*   Reducing the need for PATs and other stealable secrets by adding support for more secure alternatives.

*   Deepening Azure DevOps' integration with Microsoft Entra ID to better support its various security features.

*   Avoiding the need to store production secrets in Azure Pipelines service connections.

| Feature | Area | Quarter |
| --- | --- | --- |
| [Workload identity federation for Docker service connection](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/secret-free-acr-deployments) | Pipelines | ![Image 3: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2024 H2 |
| [Full web support for Conditional Access Policies](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/conditional-access-policy) | General | ![Image 4: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2024 Q4 |
| [Policies to disable the use of personal access tokens (PAT)](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/disable-alternate-auth-policy) | General | ![Image 5: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q2 |
| [PAT-less authentication from pipeline tasks to Azure DevOps APIs](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/new-service-connection) | Pipelines | 2026 Q1 |
| [Continuous access evaluation](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/continuous-access-evaluation) | General | Future |
| [Using device bound Entra tokens in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/proof-of-possession) | General | Future |
| [Workload identity federation Azure DevOps issuer retirement](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/wif-azdo-issuer-retirement) | Pipelines | Future |

The Azure DevOps and GitHub integration continues to be of major strategic importance. Our goal is to keep improving this integration to make it easier for customers to move their repositories to GitHub while continuing to use Azure Boards, Pipelines, and Test Plans. All of this is done while maintaining a high level of traceability between work and code.

Below is a list of investments currently on our roadmap.

| Feature | Area | Quarter |
| --- | --- | --- |
| [Support for GitHub Enterprise Cloud with data residency](https://learn.microsoft.com/en-us/azure/devops/release-notes/2025/sprint-260-update#azure-boards-and-pipelines-integration-for-github-enterprise-cloud-with-data-residency) | Boards | ![Image 6: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q3 |
| [MCP Server for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/release-notes/2025/sprint-264-update#azure-devops-local-mcp-server-generally-available) | General | ![Image 7: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q4 |
| [GitHub Coding Agent for Azure Boards](https://learn.microsoft.com/en-us/azure/devops/release-notes/2026/sprint-268-update#general-availability-of-github-copilot-integration-for-azure-boards) | Boards | ![Image 8: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q4 |
| [Increase limit of connected GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/boards-increase-repo-limit) | Boards | 2026 Q1 |
| [Remote Azure DevOps MCP Server](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/general-remote-ado-mcp-server) | Boards | 2026 Q1 |

You can also view a detailed list of planned and recent investments on our [features timeline](https://learn.microsoft.com/en-us/azure/devops/boards/github/features-timeline).

Managed DevOps Pools is an evolution of Azure DevOps Virtual Machine Scale Set agent pools. It provides better pool scalability and reliability, simplifies pool management, and allows you to use the VM images from Microsoft-hosted agents on custom Azure VMs. You can read more about Managed DevOps Pools [here](https://aka.ms/mdp-docs). Features to support new scenarios will be added to Managed DevOps Pools and not Virtual Machine Scale Set pools. Managed DevOps Pools is generally available, so you can migrate your Virtual Machine Scale Set pools to Managed DevOps Pools and use them for production workflows, wherever possible.

You will find the detailed roadmap [here](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/features-timeline?view=azure-devops&preserve-view=true).

For the past several years, all our pipelines investments have been in the area of YAML pipelines. Furthermore, all our security improvements have been for YAML pipelines. For example, with YAML pipelines, the control over [protected resources](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/resources) (e.g., repositories, service connections, etc.) is in the hands of the resource owners as opposed to pipeline authors. The [job access tokens](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/access-tokens#scoped-build-identities) that are used in YAML pipelines are scoped to specific repositories that are specified in the YAML file. These are just two examples of security features that are available for YAML pipelines. For these reasons, we recommend using YAML pipelines over classic. Adoption of YAML over classic has been significant for builds (CI). However, many customers have continued to use classic release management pipelines over YAML for releases (CD). The primary reason for this is the lack of parity in various CD features between the two solutions. Over the past year, we addressed several gaps in this area, notably in **Checks**. Checks are the primary mechanism in YAML pipelines to gate promotion of a build from one stage to another. We will continue to address gaps in other areas over the next year. Our focus will be on user experiences, traceability, and environments.

| Feature | Area | Quarter |
| --- | --- | --- |
| [Stage-level traceability](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/stage-traceability) | Pipelines | 2026 Q1 |
| [On-demand out of order execution of stages](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/on-demand-execution) | Pipelines | 2026 Q1 |
| [Service connections in checks](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/service-connections-in-checks) | Pipelines | Future |
| [Checks extensibility](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/checks-extensibility) | Pipelines | Future |

Azure DevOps provides a variety of testing tools and integrations to support different testing needs. These include manual testing, automated testing, and exploratory testing. The platform allows for the creation and management of test plans and test suites, which can be used to track manual testing for sprints or milestones. Additionally, Azure DevOps integrates with CI/CD pipelines, enabling automated test execution and reporting.

We are ramping up our investments in this area in response to feedback from our most active customer base. Our focus will be on the following aspects of test management: improving end-to-end test traceability; extending support for various programming languages and frameworks for automated testing in Test Plans; redesigning workflows and experiences for consuming test runs and test results.

Below, you will find several investments that we plan to deliver as part of this initiative:

| Feature | Area | Quarter |
| --- | --- | --- |
| [Quick access to Test Results in Test Case](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/quick-access-to-test-results) | Test Plans | ![Image 9: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q4 |
| [Latest Test Outcome in Requirements](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/recent-test-result) | Test Plans | ![Image 10: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q4 |
| [New Test Run experience - Public Preview](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/new-test-run-experience) | Test Plans | ![Image 11: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q4 |
| [Enhanced Test Point Result Panel](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/enhanced-test-point) | Test Plans | ![Image 12: Done](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/media/checkmark.png)2025 Q4 |
| [Support for JavaScript (Playwright) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-playwright) | Test Plans | 2026 Q1 |
| [Support YAML pipelines in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-yaml-pipelines) | Test Plans | 2026 Q1 |
| [Support for re-running of data driven tests](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/testplans/support-for-rerunning) | Test Plans | 2026 Q1 |
| [Improve Reliability of Test & Feedback Extension for Edge and Chrome](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/testplans/TFE-Improved-Reliability) | Test Plans | 2026 Q2 |
| [Support Capturing of Actual Test Result](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/testplans/Actual-Test-Result) | Test Plans | 2026 Q2 |

| Timeframe | Feature | Area |
| --- | --- | --- |
| **2026 Q1** | [Commits search](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/commits-search) | General |
| [Manage high privilege scopes, pipeline decorators, and unpublished extensions](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/manage-high-privilege-scopes) | General |
| [Remote Azure DevOps MCP Server](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/general-remote-ado-mcp-server) | General |
| [Organization-level alerts view in security overview](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/ghazdo/organization-level-alerts) | GitHub Advanced Security for Azure DevOps |
| [Support work item integration with the GitHub Copilot coding agent (GA)](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/boards/work-item-integration-with-github-coding-agent) | Boards |
| [Improved Filtering Experience in Boards and Backlogs](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/boards/improved-filter-experience-boards-backlogs) | Boards |
| [Increase limit of connected GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/boards-increase-repo-limit) | Boards |
| [Condensed views for kanban and sprint boards](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/boards-condensed-views) | Boards |
| [Stage-level traceability](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/stage-traceability) | Pipelines |
| [On-demand out of order execution of stages](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/on-demand-execution) | Pipelines |
| [Hosted macOS agents on Apple Silicon](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/macos-agents-apple-silicon) | Pipelines |
| [Large hosted agents](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/large-agents) | Pipelines |
| [Support YAML pipelines in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-yaml-pipelines) | Test Plans |
| [Latest Test Outcome in Requirements](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/recent-test-result) | Test Plans |
| [New Test Run experience - Public Preview](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/new-test-run-experience) | Test Plans |
| [Enhanced Test Point Result Panel](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/enhanced-test-point) | Test Plans |
| [Support for JavaScript (Playwright) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-playwright) | Test Plans |
| [Support for re-running of data driven tests](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/testplans/support-for-rerunning) | Test Plans |
| [Replace existing Wiki editor with Monaco Editor](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/wiki-monaco-editor) | Wiki |
| **2026 Q2** | [CodeQL default setup (one-click enablement)](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/ghazdo/default-setup) | GitHub Advanced Security for Azure DevOps |
| [Improve Reliability of Test & Feedback Extension for Edge and Chrome](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/testplans/TFE-Improved-Reliability) | Test Plans |
| [Support Capturing of Actual Test Result](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/testplans/Actual-Test-Result) | Test Plans |
| **Future** | [Auditing GA](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/auditing-ga) | General |
| [Policies to disable authentication methods](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/disable-alternate-auth-policy) | General |
| [PR search](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/pr-search) | General |
| [Dependabot Security Update Support](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/ghazdo/dependabot) | GitHub Advanced Security for Azure DevOps |
| [Report YAML stage status in deployment control on work items](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/boards-yaml-stage-status-on-work-item) | Boards |
| [Track repo cloning](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/track-repo-cloning) | Repos |
| [Ability to run tasks on next available Node version, if targeted version is not available](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/pick-next-runner) | Pipelines |
| [In the Box tasks support Node.js 24](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/in-the-box-tasks) | Pipelines |
| [Retire Node 6, 10 and 16 from the Agent](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2026/retire-node-6) | Pipelines |
| [Control access to GitHub repositories](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/control-access-to-github-repos) | Pipelines |
| [Support Pipelines App with GitHub Enterprise Server](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/support-pipelines-app) | Pipelines |
| [Service connections in checks](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/service-connections-in-checks) | Pipelines |
| [Checks extensibility](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/checks-extensibility) | Pipelines |
| [Seamless build pipeline integration for Test Case Run](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/seamless-build-pipelines) | Test Plans |
| [Support for Java (Playwright) in Azure Test Plan](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-java-playwright) | Test Plans |
| [Support for Python (UnitTest & Robot) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-unittest-robot) | Test Plans |
| [Support for PHP (PHPUnit & Pest) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-phpunit-pest) | Test Plans |
| [Customizable flaky test detection logic](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/customizable-flaky-test) | Test Plans |
| [Package promote task in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/package-promote-task) | Artifacts |
| [Deprecate old Azure Artifacts tasks in Azure Pipelines and default to new, auth-only tasks](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/deprecate-old-azure-artifacts) | Artifacts |

| Timeframe | Feature | Area |
| --- | --- | --- |
| **Future** | [Policies to disable authentication methods](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/disable-alternate-auth-policy) | General |
| [Substring search](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/substring-search) | General |
| [Commits search](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/commits-search) | General |
| [PR search](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/pr-search) | General |
| [New Boards Hub](https://learn.microsoft.com/en-us/azure/devops/release-notes/2024/sprint-237-update#new-boards-hub-on-by-default) | Boards |
| [Markdown editor for work item multi-line fields](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2023/work-item-support-for-markdown) | Boards |
| [Track repo cloning](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/track-repo-cloning) | Repos |
| [Stop shipping Node 6 and Node 10 runners with the agent](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/remove-node-6) | Pipelines |
| [Support Pipelines App with GitHub Enterprise](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/support-pipelines-app) | Pipelines |
| [Service connections in checks](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/service-connections-in-checks) | Pipelines |
| [Checks extensibility](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2022/checks-extensibility) | Pipelines |
| [Package promote task in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/package-promote-task) | Artifacts |
| [Deprecate old Azure Artifacts tasks in Azure Pipelines and default to new, auth-only tasks](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/deprecate-old-azure-artifacts) | Artifacts |
| [Dashboard Global Parameter](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/dashboard-global-parameter) | Reporting |
| [Dashboard Template](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2024/dashboard-template) | Reporting |
| [Seamless build pipeline integration for Test Case Run](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/seamless-build-pipelines) | Test Plans |
| [Advanced Test Case result history](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/advanced-test-result) | Test Plans |
| [Latest Test Outcome in Requirements](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/recent-test-result) | Test Plans |
| [Direct link from Test Plan work item to Test Plans page](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/direct-link-from-test-plan) | Test Plans |
| [Auto-pause manual test case run](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/auto-pause-manual-test) | Test Plans |
| [Resume paused test cases on by default](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/resume-paused-test-cases) | Test Plans |
| [Undo test step in web and desktop runner](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/undo-test-step) | Test Plans |
| [Export test cases with custom columns in XLSX](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/export-test-cases) | Test Plans |
| [Restore deleted test plans and test suites using REST API](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/restore-deleted-test-plans) | Test Plans |
| [View Test Case State in Execute Tab](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/view-state-execute-tab) | Test Plans |
| [New Test Plans directory](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/new-test-plans-directory) | Test Plans |
| [New Test Run experience](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/new-test-run-experience) | Test Plans |
| [Enhanced Test Point Result Panel](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/enhanced-test-point) | Test Plans |
| [Support for Java (JUnit) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-junit) | Test Plans |
| [Support for JavaScript (Jest) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-jest) | Test Plans |
| [Support for Python (UnitTest & Robot) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-unittest-robot) | Test Plans |
| [Support for JavaScript (Playwright) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-playwright) | Test Plans |
| [Support for PHP (PHPUnit & Pest) in Azure Test Plans](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-phpunit-pest) | Test Plans |
| [Support for Java (Playwright) in Azure Test Plan](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/support-for-java-playwright) | Test Plans |
| [Customizable flaky test detection logic](https://learn.microsoft.com/en-us/azure/devops/release-notes/roadmap/2025/testplans/customizable-flaky-test) | Test Plans |

---

We would love to hear what you think about these features. Report any problems or suggest a feature through [Developer Community](https://developercommunity.visualstudio.com/spaces/21/index.html).

![Image 13: Make a suggestion](https://learn.microsoft.com/en-us/azure/devops/release-notes/media/help-make-a-suggestion.png)

You can also get advice and your questions answered by the community on [Stack Overflow](https://stackoverflow.com/questions/tagged/azure-devops).
