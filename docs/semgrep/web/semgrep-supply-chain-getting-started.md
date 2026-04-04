# Scan third-party dependencies

Source: https://semgrep.dev/docs/semgrep-supply-chain/getting-started#scan-a-project-without-lockfiles-beta

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Scan and triage- SCA (Supply Chain)- Open source security vulnerabilities**On this page- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)Scan third-party dependencies
This article walks you through the setup needed to scan your project with Semgrep Supply Chain and its configuration and customization options. Once you enable Semgrep Supply Chain, it automatically scans repositories that you have added to Semgrep AppSec Platform, but your repository must first meet the requirements for a successful scan.

## Project directory structure[​](#project-directory-structure)
To scan your project with Semgrep Supply Chain, it must have a manifest file or lockfile and use [supported package managers and filenames](/docs/supported-languages#semgrep-supply-chain).

Semgrep Supply Chain can correctly parse code files, manifest files, and lockfiles in subfolders as well. Code files that use the dependencies in the manifest file or lockfile must be nested in the same directory as the manifest file or lockfile. Manifest files and lockfiles must all use supported file names.

In the following example, Semgrep Supply Chain assumes that all code files using the dependencies in `my-project/running/lockfile.json` are nested in `my-project/running/` or deeper directories.

`/my-project├───/running│   ├───lockfile.json│   ├───bar.js│   └───/uphill│       ├───lockfile.json│       └────foo.js├───/biking`
If you have code files in `my-project/biking,` Semgrep Supply Chain does not associate them with the dependencies in `my-project/running/lockfile.json.` If there is another manifest file or lockfile in `my-project/running`, such as `my-project/running/uphill/lockfile.json`, then this overrides the original `my-project/running/lockfile.json` for all code files in `my-project/running/uphill/` or deeper directories.

Apache MavenTo run a Semgrep Supply Chain scan, generate a [dependency tree for Apache Maven](/docs/semgrep-supply-chain/setup-maven).

## Enable Semgrep Supply Chain[​](#enable-semgrep-supply-chain)

- Sign in to [** Semgrep AppSec Platform](https://semgrep.dev/login).
- Go to **[Settings &gt; General &gt; Supply Chain](https://semgrep.dev/orgs/-/settings/general/supplyChain)**.
- Click the **** Supply Chain scans** toggle if it is not already enabled.

## Scan frequency[​](#scan-frequency)
You can modify your CI configuration so that Semgrep Supply Chain scans your code at a specified frequency or whenever a specific event occurs, such as opening a pull request or merge request.

### Rule updates[​](#rule-updates)
Semgrep Supply Chain frequently receives rule updates. To take advantage of these updates, adjust the frequency with which Semgrep Supply Chain scans your codebase.

If a rule is updated, findings generated against the revised rule are considered **new findings**, even if the previous version generated a finding. The new finding is not affected by any triage actions on findings related to the prior version of the rule. Because the finding is new, you&#x27;ll also receive notifications through the channels you&#x27;ve set up, such as Slack.

### Schedule scans[​](#schedule-scans)
The following table is a summary of methods and resources to set up schedules for different CI providers.

CI providerWhere to set scheduleGitHub ActionsSee [Sample CI configs](/docs/semgrep-ci/sample-ci-configs#sample-github-actions-configuration-file) for information on how to modify your `semgrep.yml` fileGitLab CI/CDRefer to [GitLab documentation](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)JenkinsRefer to [Jenkins documentation](https://www.jenkins.io/doc/book/pipeline/running-pipelines/#scheduling-jobs-in-jenkins)Bitbucket PipelinesRefer to [Bitbucket documentation](https://support.atlassian.com/bitbucket-cloud/docs/pipeline-triggers/)CircleCIRefer to [CircleCI documentation](https://circleci.com/docs/scheduled-pipelines#get-started-with-scheduled-pipelines-in-circleci)BuildkiteRefer to [Buildkite documentation](https://buildkite.com/docs/pipelines/scheduled-builds)Azure PipelinesRefer to [Azure documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/scheduled-triggers?view=azure-devops&amp;tabs=yaml)SemaphoreRefer to [Semaphore documentation](https://docs.semaphore.io/using-semaphore/tasks)
### Event-triggered scans[​](#event-triggered-scans)
You can configure your CI/CD system to trigger a Semgrep Supply Chain scan whenever one of the following events occurs:

**Event****Scope of scan****Dependency rule set**Pull request or merge request[Diff-aware scan](/docs/deployment/customize-ci-jobs#set-up-diff-aware-scans)All dependency rulesPush or scheduled event, such as a cron jobFull scanAll dependency rules
## Scan a project without lockfiles (beta)[​](#scan-a-project-without-lockfiles-beta)
infoThis feature is currently in invite-only beta. Please contact [Semgrep Support](/docs/support) for more information.

Semgrep Supply Chain can scan projects without the need for lockfiles. This simplifies the configuration of Supply Chain scans. This feature is available for the following languages:

- C#
- Java projects built using Maven or Gradle Wrapper
- Kotlin
- Python

- Ensure that the environment where you run Semgrep scans has installed all of the dependencies required to build your project, such as Java and Maven or Python and pip.
- Initiate a Semgrep scan, ensuring that you include the `--allow-local-builds` flag:
`semgrep ci --allow-local-builds`
For existing CI jobs, you may have to edit your configuration file to include this flag.
Semgrep builds the project, using the build information included in the `pom.xml` or `build.gradle` file to determine the set of dependencies used by the project.

info
- Semgrep Managed Scans can&#x27;t determine the dependencies in a project when there is no manifest file or lockfile, so Supply Chain scans don&#x27;t return any findings.
- By default, Semgrep doesn&#x27;t surface errors generated during a scan. To view errors in the CLI output, include the `--verbose` when initiating your scan:
```
semgrep ci --allow-local-builds --verbose
```

## Run a scan using the CLI[​](#run-a-scan-using-the-cli)
You can start a stand-alone Semgrep Supply Chain scan by running the following command in the CLI:

`semgrep ci --supply-chain`
Semgrep prints a list of findings directly to the CLI, including the finding&#x27;s reachability determination, severity level, a brief description, and suggested remediation.

You can also view your results in Semgrep AppSec Platform. It displays all of the information displayed in the CLI, but it also offers you the ability to:

- [See additional finding details](/docs/semgrep-supply-chain/findings), such as whether the finding is always reachable or if it&#x27;s reachable if certain conditions are met, and its transitivity status
- Use the [dependency search](/docs/semgrep-supply-chain/dependency-search) feature
- Use the [license compliance](/docs/semgrep-supply-chain/license-compliance) feature

## Scan a monorepo&#x27;s dependencies[​](#scan-a-monorepos-dependencies)
Semgrep Supply Chain supports the scanning of monorepos. As outlined in [Project directory structure](#project-directory-structure), findings are grouped by directory based on the [manifest file or lockfile](/docs/semgrep-supply-chain/glossary#manifest-file) present in the monorepo.

## Block pull requests or merge requests[​](#block-pull-requests-or-merge-requests)
You can comment on or potentially block pull requests or merge requests by defining a [Supply Chain Policy](/docs/semgrep-supply-chain/policies).

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep Supply Chain](/docs/tags/semgrep-supply-chain)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/semgrep-supply-chain/getting-started.md)Last updated on **Dec 10, 2025**