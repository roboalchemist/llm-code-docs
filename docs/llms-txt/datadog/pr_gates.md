# Source: https://docs.datadoghq.com/pr_gates.md

---
title: PR Gates
description: >-
  Learn how to use PR Gates to enable your team to control what code makes it to
  production.
breadcrumbs: Docs > PR Gates
---

# PR Gates

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

PR Gates allow you to control software security and quality by configuring rules to block pull requests with substandard code from being merged. Preventing pull requests with substandard code from being merged can ensure that the code that is eventually deployed to production adheres to high organizational standards, reducing incidents and minimizing unwanted behaviors.

{% image
   source="https://datadog-docs.imgix.net/images/pr_gates/setup/sca_3.7c476f7435ac182dff3825a0d1b10a46.png?auto=format"
   alt="An SCA rule that triggers a failure if any library vulnerabilities with critical or high severity are detected in the repository." /%}

PR Gates, similar to [Datadog Monitors](https://docs.datadoghq.com/monitors/), consume data and findings output by compatible Datadog products and apply conditions to these findings to determine if a PR meets your organizational standards. To prevent unnecessary impact on your developers' velocity, PR Gates only block on violations introduced by the code changes of the PR in question, not on findings that already existed in your repository before the PR and its branch were created. For example, if you configure PR Gates to block on Critical-severity code vulnerabilities, PR Gates fails and blocks the PR only if a developer introduces a new Critical code vulnerability as part of that PR.

You can configure PR Gates rules for the following categories. Please note that the compatible product must be running on your desired repositories before PR Gates can begin taking action on the relevant PRs:

| Source type                                                                                                          | Condition types                                       |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [**Static Code Analysis (SAST)**](https://docs.datadoghq.com/security/code_security/static_analysis)                 | - Code vulnerabilities- Code quality violations       |
| [**Software Composition Analysis**](https://docs.datadoghq.com/security/code_security/software_composition_analysis) | - Library vulnerabilities- Library license violations |
| [**Code Coverage**](https://docs.datadoghq.com/code_coverage/)                                                       | - Total code coverage- Patch code coverage            |
| [**Infrastructure as Code Scanning**](https://docs.datadoghq.com/security/code_security/iac_security/)               | - IaC vulnerabilities                                 |

After creating PR Gates rules, Datadog will automatically create checks on your pull requests using the [GitHub integration](https://docs.datadoghq.com/integrations/github/) or [Azure DevOps Source Code integration](https://docs.datadoghq.com/integrations/azure_devops_source_code/). Set those checks as required in GitHub or Azure DevOps when you are ready to enforce them.

{% alert level="warning" %}
PR Gates are not supported in pull requests in public repositories, or on pull requests targeting a destination branch in a different repository from the source branch (that is, forked repositories trying to merge into the main repository).
{% /alert %}

## Rule types{% #rule-types %}

PR Gates offers the following rule types:

{% tab title="Static Code Analysis (SAST)" %}
You can create rules to block code changes from being merged when a pull request's modified lines introduce at least one new code vulnerability or code quality violation of a certain severity.

{% image
   source="https://datadog-docs.imgix.net/images/pr_gates/setup/static_analysis_3.6a7b5af7f86566da8dd47ed5300b27c9.png?auto=format"
   alt="A PR Gate rule that fails when one or more new code quality violations of error-level severity are contained in the repository" /%}

{% /tab %}

{% tab title="Software Composition Analysis (SCA)" %}
You can create rules to block code changes from being merged when a pull request's modified lines introduce at least one new library vulnerability of a certain severity or at least one new library with a forbidden license.

{% image
   source="https://datadog-docs.imgix.net/images/pr_gates/setup/sca_3.7c476f7435ac182dff3825a0d1b10a46.png?auto=format"
   alt="A PR Gate rule that fails when one or more critical or high severity library vulnerabilities are contained in the repository" /%}

{% /tab %}

{% tab title="Code Coverage" %}
You can create rules to block code changes from being merged when a pull request's modified lines cause the repository's overall code coverage to fall below a certain percentage or if the patch coverage of those lines is below a certain threshold.

{% image
   source="https://datadog-docs.imgix.net/images/pr_gates/setup/code_coverage.154f6421916b97984dec101d57b31507.png?auto=format"
   alt="A PR Gate rule that fails when one or more critical or high severity library vulnerabilities are contained in the repository" /%}

{% /tab %}

{% tab title="Infrastructure as Code Scanning" %}
You can create rules to block code changes from being merged when a pull request's modified lines introduce at least one new infrastructure as code (IaC) vulnerability of a certain severity.

{% image
   source="https://datadog-docs.imgix.net/images/pr_gates/setup/iac.91796c41b5c8078bf12f234d175abbb4.png?auto=format"
   alt="A PR Gate rule that fails when one or more critical or high severity library vulnerabilities are contained in the repository" /%}

{% /tab %}

To create a PR Gate rule, see the [Setup documentation](https://docs.datadoghq.com/pr_gates/setup/).

## Manage rules{% #manage-rules %}

You can manage and update PR Gates rules on the [**PR Gates Rules**](https://app.datadoghq.com/ci/pr-gates) page. Improve your security and quality practices based on your project requirements and risk tolerances.

You can see all of the rules defined by the organization.

{% image
   source="https://datadog-docs.imgix.net/images/pr_gates/rules_list_3.10a15e16873614aedaa0bdc45b1ba2af.png?auto=format"
   alt="List of PR Gate rules in Datadog" /%}

## Further Reading{% #further-reading %}

- [Check out the latest Software Delivery releases! (App login required)](https://app.datadoghq.com/release-notes?category=Software%20Delivery)
- [Enhance code reliability with Datadog Quality Gates](https://www.datadoghq.com/blog/datadog-quality-gates/)
- [Use Datadog monitors as quality gates for GitHub Actions deployments](https://www.datadoghq.com/blog/datadog-github-deployment-protection-rules/)
- [Flaky tests: their hidden costs and how to address flaky behavior](https://www.datadoghq.com/blog/datadog-flaky-tests/)
- [Prevent cloud misconfigurations from reaching production with Datadog IaC Security](https://www.datadoghq.com/blog/datadog-iac-security/)
