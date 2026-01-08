# Semgrep Community Edition in CI

Source: https://semgrep.dev/docs/deployment/oss-deployment

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Semgrep Community Edition- Semgrep CE in CI**On this page- [Deployment](/docs/tags/deployment)- [Semgrep Community Edition](/docs/tags/semgrep-community-edition)Semgrep Community Edition in CI
Semgrep Community Edition (CE) can be set up run static application security testing (SAST) scans on repositories of any size.

This guide explains how to set up Semgrep CE in your CI pipeline using entirely open source components, also known as a **stand-alone** CI setup. The preferred Semgrep CE command is `semgrep scan`.

## Prerequisites[​](#prerequisites)

- Sufficient permissions in your repository to:

Commit a CI configuration file.
- Start or stop a CI job.

- Optional: Create environment variables.

## Ensure your scans use open source components[​](#ensure-your-scans-use-open-source-components)
This setup uses only the **LGPL 2.1** Semgrep CLI tool. It is not subject to the usage limits of Semgrep AppSec Platform. In order to remain strictly open source, you must ensure that the rules you run use open source licenses or are your own custom Semgrep rules.

To verify a rule&#x27;s license, read the `license` key under the `metadata` of a Semgrep rule.

Click to expand for an example of a rule with a `license` key.This rule&#x27;s last line displays a `license: MIT` key-value pair.

`rules:  - id: eslint.detect-object-injection    patterns:      - pattern: $O[$ARG]      - pattern-not: $O[&quot;...&quot;]      - pattern-not: &quot;$O[($ARG : float)]&quot;      - pattern-not-inside: |          $ARG = [$V];          ...          &lt;... $O[$ARG] ...&gt;;      - pattern-not-inside: |          $ARG = $V;          ...          &lt;... $O[$ARG] ...&gt;;      - metavariable-regex:          metavariable: $ARG          regex: (?![0-9]+)    message: Bracket object notation with user input is present, this might allow an      attacker to access all properties of the object and even it&#x27;s prototype,      leading to possible code execution.    languages:      - javascript      - typescript    severity: MEDIUM    metadata:      cwe: &quot;CWE-94: Improper Control of Generation of Code (&#x27;Code Injection&#x27;)&quot;      primary_identifier: eslint.detect-object-injection      secondary_identifiers:        - name: ESLint rule ID security/detect-object-injection          type: eslint_rule_id          value: security/detect-object-injection      license: MIT`
For a comparison of the behavior between Semgrep CE CI scans and Semgrep AppSec Platform scans, see [** Semgrep AppSec Platform versus Semgrep Community Edition](/docs/semgrep-pro-vs-oss).

## Set up the CI job[​](#set-up-the-ci-job)
### Use template configuration files[​](#use-template-configuration-files)
Click the link of your CI provider to view a configuration file you can commit to your repository to create a Semgrep job:

- [GitHub Actions](/docs/semgrep-ci/sample-ci-configs#github-actions)
- [GitLab CI/CD](/docs/semgrep-ci/sample-ci-configs#gitlab-cicd)
- [Jenkins](/docs/semgrep-ci/sample-ci-configs#jenkins)
- [Bitbucket Pipelines](/docs/semgrep-ci/sample-ci-configs#bitbucket-pipelines)
- [Buildkite](/docs/semgrep-ci/sample-ci-configs#buildkite)
- [CircleCI](/docs/semgrep-ci/sample-ci-configs#circleci)
- [Azure Pipelines](/docs/semgrep-ci/sample-ci-configs#azure-pipelines)

### Use other methods[​](#use-other-methods)
Use either of the following methods to run Semgrep on other CI providers.

#### Direct docker usage[​](#direct-docker-usage)
Reference or add the [semgrep/semgrep](https://hub.docker.com/r/semgrep/semgrep) Docker image directly. The method to add the Docker image varies based on the CI provider. This method is used in the [Bitbucket Pipelines code snippet](/docs/semgrep-ci/sample-ci-configs#sample-bitbucket-pipelines-configuration-snippet).

#### Install `semgrep` within your CI job[​](#install-semgrep-within-your-ci-job)
If you cannot use the Semgrep Docker image, install Semgrep as a step or command within your CI job:

- Add `pip3 install semgrep` into the configuration file as a step or command, depending on your CI provider&#x27;s syntax.
- Run any valid `semgrep scan` command, such as `semgrep scan --config auto`.

For an example, see the [Azure Pipelines code snippet](/docs/semgrep-ci/sample-ci-configs#sample-azure-pipelines-configuration-snippet).

## Configure your CI job[​](#configure-your-ci-job)
The following sections describe methods to customize your CI job.

### Schedule your scans[​](#schedule-your-scans)
The following table is a summary of methods and resources to set up schedules for different CI providers.

CI providerWhere to set scheduleGitHub ActionsSee [Sample CI configs](/docs/semgrep-ci/sample-ci-configs#sample-github-actions-configuration-file) for information on how to modify your `semgrep.yml` fileGitLab CI/CDRefer to [GitLab documentation](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)JenkinsRefer to [Jenkins documentation](https://www.jenkins.io/doc/book/pipeline/running-pipelines/#scheduling-jobs-in-jenkins)Bitbucket PipelinesRefer to [Bitbucket documentation](https://support.atlassian.com/bitbucket-cloud/docs/pipeline-triggers/)CircleCIRefer to [CircleCI documentation](https://circleci.com/docs/scheduled-pipelines#get-started-with-scheduled-pipelines-in-circleci)BuildkiteRefer to [Buildkite documentation](https://buildkite.com/docs/pipelines/scheduled-builds)Azure PipelinesRefer to [Azure documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/scheduled-triggers?view=azure-devops&amp;tabs=yaml)SemaphoreRefer to [Semaphore documentation](https://docs.semaphore.io/using-semaphore/tasks)
### Customize rules and rulesets[​](#customize-rules-and-rulesets)
#### Add rules to scan with `semgrep scan`[​](#add-rules-to-scan-with-semgrep-scan)
You can customize what rules to run in your CI job. The rules and rulesets can come from the [Semgrep Registry](https://semgrep.dev/explore/), or your own rules. The sources for rules to scan with are:

- The value of the `SEMGREP_RULES` environment variable.
- The value passed after `--config`. You can use multiple `--config` arguments, one per value. For example: `semgrep scan --config p/default --config p/comment`.

The `SEMGREP_RULES` environment variable accepts a list of local and remote rules and rulesets to run. The `SEMGREP_RULES` list is delimited by a space (` `) if the variable is exported from a shell command or script block. For example, see the following BitBucket Pipeline snippet:

`# ...  script:    - export SEMGREP_RULES=&quot;p/nginx p/ci no-exec.yml&quot;    - semgrep ci# ...`
The line defining `SEMGREP_RULES` defines three different sources, delimited by a space:

`- export SEMGREP_RULES=&quot;p/nginx p/ci no-exec.yml&quot;`
The example references two rulesets from Semgrep Registry (`p/nginx` and `p/ci`) and a rule available in the repository (`no-exec.yml`).

If the `SEMGREP_RULES` environment variable is defined from a YAML block, the list of rules and rulesets to run is delimited by a newline. See the following example of a GitLab CI/CD snippet:

`# ...variables:  SEMGREP_RULES: &gt;-    p/nginx    p/ci    no-exec.yml# ...`
#### Write your own rules[​](#write-your-own-rules)
Write custom rules to enforce your team&#x27;s coding standards and security practices. Rules can be forked from existing community-written rules.

See [Writing rules](/docs/writing-rules/overview) to learn how to write custom rules.

### Ignore files[​](#ignore-files)
See [** Ignore files, folders, and code](/docs/ignoring-files-folders-code).

By default `semgrep ci` skips files and directories such as `tests/`, `node_modules/`, and `vendor/`. It uses the default `.semgrepignore` file which you can find in the [Semgrep GitHub repository](https://github.com/semgrep/semgrep/blob/develop/cli/src/semgrep/templates/.semgrepignore). This default is used when no explicit `.semgrepignore` file is found in the root of your repository.

Optional: Copy and commit the default `.semgrepignore` file to the **root of your repository** and extend it with your own entries or write your `.semgrepignore` file from scratch. If Semgrep detects a `.semgrepignore` file within your repository, it does not append entries from the default `.semgrepignore` file.

For a complete example, see the [.semgrepignore file in Semgrep’s source code](https://github.com/semgrep/semgrep/blob/develop/.semgrepignore).

caution`.semgrepignore` is only used by Semgrep. Integrations such as [GitLab&#x27;s Semgrep SAST Analyzer](https://gitlab.com/gitlab-org/security-products/analyzers/semgrep) do not use it.

### Save or export findings to a file[​](#save-or-export-findings-to-a-file)
To save or export findings, pass file format options and send the formatted findings to a file.

For example, to save to a JSON file:

`semgrep scan --json &gt; findings.json`

The JSON schema for Semgrep&#x27;s CLI output can be found in [semgrep/semgrep-interfaces](https://github.com/semgrep/semgrep-interfaces/blob/main/semgrep_output_v1.jsonschema).

You can also use the SARIF format:

`semgrep scan --sarif &gt; findings.sarif`

Refer to the [CLI reference](/docs/cli-reference) for output formats.

## Migrate to Semgrep AppSec Platform from a stand-alone CI setup[​](#migrate-to-semgrep-appsec-platform-from-a-stand-alone-ci-setup)
Migrate to Semgrep AppSec Platform to:

- **View and manage findings in a centralized location**. False positives can be ignored through triage actions. These actions can be undertaken in bulk.
- **Configure rules and actions to undertake when a finding is generated by the rule**. You can undertake the following actions:

Audit the rule. This means that findings are kept within Semgrep&#x27;s **Findings** page and are not surfaced to your team&#x27;s SCM.
- Show the finding to your team through the use of PR and MR comments.
- Block the pull request or merge request.

To migrate to Semgrep AppSec Platform:

- Create an account in [Semgrep AppSec Platform](https://semgrep.dev/login).
- Click **[Projects](https://semgrep.dev/orgs/-/projects)** &gt; **Scan New Project** &gt; Run scan in CI.
- Follow the steps in the setup page to complete your migration.
- Optional: Remove the old CI job that does not use Semgrep AppSec Platform.

## Semgrep CE jobs versus Semgrep jobs[​](#semgrep-ce-jobs-versus-semgrep-jobs)
FeatureSemgrep CI (`semgrep ci`)Semgrep CE CI (`semgrep scan`)Customized SAST scans✔️✔️[SCA (software composition analysis) scans](/docs/semgrep-supply-chain/overview)✔️--[Secrets  scans](/docs/semgrep-secrets/conceptual-overview)✔️--[PR (pull request) or MR (merge request) comments](/docs/category/pr-or-mr-comments)✔️--[Finding status tracked over lifetime](/docs/semgrep-code/findings)✔️--Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Deployment](/docs/tags/deployment)- [Semgrep Community Edition](/docs/tags/semgrep-community-edition)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/deployment/oss-deployment.md)Last updated on **Oct 21, 2025**