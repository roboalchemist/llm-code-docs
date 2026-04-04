# Source: https://docs.datadoghq.com/security/code_security/static_analysis.md

---
title: Static Code Analysis (SAST)
description: >-
  Learn about Datadog Static Code Analysis to scan code for quality issues and
  security vulnerabilities before your code reaches production.
breadcrumbs: Docs > Datadog Security > Code Security > Static Code Analysis (SAST)
---

# Static Code Analysis (SAST)

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="warning" %}
Code Security is not available for the  site.
{% /alert %}


{% /callout %}

## Overview{% #overview %}

Static Code Analysis is Datadog's Static Application Security Testing (SAST) capability. SAST is a clear-box software testing technique that analyzes a program's pre-production code without the need to execute the program.

Static Code Analysis helps you identify security vulnerabilities and maintainability issues early in the software development life cycle (SDLC) to ensure only the highest quality, most secure code makes it to production. It provides organizations with the following benefits:

- Applications are less vulnerable to security breaches over time, due to new vulnerabilities being caught through SAST scans before code reaches production.
- Takes the guesswork out of adhering to an organization's code standards, enabling your development team to ship compliant code without significant impacts to developer velocity.
- Onboard developers faster because Static Code Analysis enables an organization to maintain a more readable codebase over time.

## Set up Static Code Analysis{% #set-up-static-code-analysis %}

Static Code Analysis supports scanning for security vulnerabilities and poor coding practices in the following languages and technologies:

- [python](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Python)
- [javascript](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=JavaScript)
- [typescript](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=TypeScript)
- [java](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Java)
- [c sharp](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=CSharp)
- [go](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Go)
- [ruby](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Ruby)
- [php](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=PHP)
- [docker](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Docker)
- [yaml](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=YAML)
- [kotlin](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Kotlin)
- [elixir](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Elixir)
- [apex](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Apex)
- [swift](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules?languages=Swift)
- [other](https://docs.datadoghq.com/security/code_security/static_analysis/setup/?tab=circleciorbs#upload-third-party-static-analysis-results-to-datadog)

Scans can run via your CI/CD pipelines or directly in Datadog with hosted scanning.To get started, go to the [**Code Security** setup page](https://app.datadoghq.com/security/configuration/code-security/setup) or see the [Setup documentation](https://docs.datadoghq.com/security/code_security/static_analysis/setup).

## Integrate into the development lifecycle{% #integrate-into-the-development-lifecycle %}

### Source code management{% #source-code-management %}

- [Pull Requests](https://docs.datadoghq.com/static_analysis/github_pull_requests)

### IDEs{% #ides %}

- [Datadog Plugin for JetBrains IDEs](https://docs.datadoghq.com/developers/ide_plugins/idea/)
- [Datadog Extension for Visual Studio Code](https://docs.datadoghq.com/developers/ide_plugins/vscode/#static-analysis)

## Search and filter results{% #search-and-filter-results %}

After setting up Static Code Analysis, a scan is run on each commit to a scanned repository. Violations are summarized per repository on the [**Code Security Repositories** page](https://app.datadoghq.com/ci/code-analysis). Click on a repository to analyze **Code Vulnerabilities** and **Code Quality** results from Static Code Analysis.

- The **Code Vulnerabilities** tab contains the violations found by Datadog's rules in the [Security category](https://docs.datadoghq.com/security/code_security/static_analysis_rules?categories=Security).
- The **Code Quality** tab contains the violations found by Datadog's rules in the [Best Practices, Code Style, Error Prone, or Performance categories](https://docs.datadoghq.com/security/code_security/static_analysis_rules?categories=Best+Practices&categories=Code+Style&categories=Error+Prone&categories=Performance).

To filter your results, use the facets to the left of the list, or search. Results can be [filtered by service or team facets](https://docs.datadoghq.com/security/code_security/static_analysis/#link-results-to-datadog-services-and-teams).

Every row represents a violation. Each violation is associated with the specific commit and branch that is selected in the filters at the top of the page (by default, results are shown for the latest commit on the default branch of the repository you are viewing).

Click on a violation to open a side panel that contains information about the scope of the violation and where it originated.

The content of the violation is shown in tabs:

- **Details**: A description of the violation and the lines of code that caused it. To see the offending code snippet, configure the relevant source code integration for your provider ([GitHub](https://docs.datadoghq.com/integrations/github/), [GitLab](https://docs.datadoghq.com/integrations/gitlab-source-code/), Azure[6](https://en.wikipedia.org/wiki/Camel_case)).
- **Remediation**: One or more code fixes that can resolve the violation, with options for remediation.
- **Event**: JSON metadata regarding the violation.

### Filter out false positives{% #filter-out-false-positives %}

For a subset of SAST vulnerabilities, Bits AI can review the context of the finding and assess whether it is more likely to be a true or false positive, along with a short explanation of the reasoning.

For more information, see [AI-Enhanced Static Code Analysis](https://docs.datadoghq.com/security/code_security/static_analysis/ai_enhanced_sast/).

## Customize your configuration{% #customize-your-configuration %}

To customize which Static Code Analysis rules are configured in your repositories or across your organization, see the [Setup documentation](https://docs.datadoghq.com/security/code_security/static_analysis/setup/#customize-your-configuration).

## Link findings to Datadog services and teams{% #link-findings-to-datadog-services-and-teams %}

To link findings to Datadog services and teams, see the [Setup documentation](https://docs.datadoghq.com/security/code_security/static_analysis/#link-results-to-datadog-services-and-teams).

## Apply suggested fixes{% #apply-suggested-fixes %}

In Datadog Static Code Analysis, there are two types of suggested fixes:

1. **Deterministic Suggested Fix:** For simple violations like linting issues, the rule analyzer automatically provides templated fixes.
1. **AI-suggested Fix:** For complex violations, fixes are typically not available beforehand. Instead, you can use AI-suggested fixes, which use OpenAI's GPT-4 to generate a suggested fix. You can choose between "Text" and "Unified Diff" fixes, which outputs plain text instructions or a code change for resolving the violation, respectively.

### Fix a vulnerability or quality issue directly from Datadog{% #fix-a-vulnerability-or-quality-issue-directly-from-datadog %}

If GitHub is your source code manager, you can push a code change to fix a SAST issue directly from Datadog in two ways.

#### Open a pull request{% #open-a-pull-request %}

If your GitHub app's **Pull Requests** permission is set to **Read & Write**, one-click remediation is enabled for all Static Code Analysis findings with an available suggested fix.

Follow these steps to fix a vulnerability and open a pull request:

1. View a specific SAST result in Code Security.
1. Click **Fix Violation** in the side panel of the result.
1. Select **Open a Pull Request**.
1. Enter a pull request title and commit message.
1. Click **Create PR**.

#### Commit directly to the current branch{% #commit-directly-to-the-current-branch %}

You can also fix a vulnerability by committing directly to the branch the result was found on.

To commit a suggested fix:

1. View a specific SAST result in Code Security.
1. Click **Fix Violation** in the side panel of the result.
1. Click **Commit to current branch**.

## Report false positives{% #report-false-positives %}

If you believe a specific violation is a false positive, you can flag it as a false positive with a reason for flagging, which sends a report directly to Datadog. Submissions are reviewed on a regular basis to improve ruleset quality over time.
