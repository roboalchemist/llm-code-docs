# Source: https://docs.airbyte.com/platform/2.0/contributing-to-airbyte.md

# Source: https://docs.airbyte.com/platform/1.8/contributing-to-airbyte.md

# Source: https://docs.airbyte.com/platform/1.7/contributing-to-airbyte.md

# Source: https://docs.airbyte.com/platform/1.6/contributing-to-airbyte.md

# Source: https://docs.airbyte.com/community/contributing-to-airbyte.md

# Contributing to Airbyte

Copy Page

Thank you for your interest in contributing! Contributions are very welcome. We appreciate first time contributors and we are happy help you get started. Join our [community Slack](https://slack.airbyte.io) and feel free to reach out with questions in [`#dev-and-contribuions` channel](https://airbytehq.slack.com/archives/C054V9JFTC6).

If you're interacting in Slack, codebases, mailing lists, events, or any other Airbyte activity, you must follow the [Code of Conduct](/community/code-of-conduct.md). Please review it before getting started.

## Code Contributions[​](#code-contributions "Direct link to Code Contributions")

Most of the issues that are open for contributions are tagged with [`good first issue`](https://github.com/airbytehq/airbyte/issues?q=is%3Aopen+is%3Aissue+label%3A%22good%20first%20issue%22) or [`help-welcome`](https://github.com/airbytehq/airbyte/issues?q=is%3Aopen+is%3Aissue+label%3Ahelp-welcome). If you are interested in an issue that isn't tagged, post a comment with your approach, and we'd be happy to assign it to you. If you submit a fix isn't linked to an issue you're assigned, there is chance Airbyte won't accept it.

### Contributions we accept[​](#contributions-we-accept "Direct link to Contributions we accept")

* Fixes and enhancements to existing API source connectors
* New streams and features for existing connectors using the Connector Builder/YAML
* New API source connectors built with the Connector Builder
* Migrations of an existing connector from Python to the Connector Builder/YAML

Airbyte evaluates contributions outside this scope on a case-by-case basis. Reach out to the Airbyte team before starting to ensure the team can accept your idea.

Contributions to Airbyte connectors may take some time to review, as they can affect many users. To assist us during code review, include as much information as possible in your pull request, including examples, use cases, documentation links, and more.

warning

Airbyte is revamping its core Java destinations codebase. We're not reviewing/accepting new Java connectors at this time.

### Contributions we don't accept[​](#contributions-we-dont-accept "Direct link to Contributions we don't accept")

* Platform contributions. In mid-2025, Airbyte stopping accepting community contributions to the Airbyte platform. Continue reporting issues through GitHub so we can investigate and prioritize fixes and improvements.

### Standard contribution workflow[​](#standard-contribution-workflow "Direct link to Standard contribution workflow")

1. Fork the `airbyte` repository.
2. Clone the repository locally.
3. Create a branch for your feature/bug fix with the format `{YOUR_USERNAME}/{FEATURE/BUG}` (e.g. `jdoe/source-stock-api-stream-fix`)
4. Make and commit changes.
5. Push your local branch to your fork.
6. Submit a Pull Request so that we can review your changes.
7. [Link an existing Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) that doesn't include the `needs triage` label to your Pull Request. Pull requests without an issue attached take longer to review.
8. Write a PR title and description that follows the [Pull Request Handbook](/community/contributing-to-airbyte/resources/pull-requests-handbook.md).
9. An Airbyte maintainer will trigger the CI tests for you and review the code.
10. Review and respond to feedback and questions by Airbyte maintainers.
11. Merge the contribution.

You can check the status of your contribution in this [Github Project](https://github.com/orgs/airbytehq/projects/108/views/4). It will provide you what Sprint your contribution was assigned and when you can expect a review.

### Pull Request permission requirements[​](#pull-request-permission-requirements "Direct link to Pull Request permission requirements")

When submitting a pull request, please ensure that Airbyte maintainers have write access to your branch. This allows us to apply formatting fixes, security-related patches, and dependency updates directly, which significantly speeds up the review and approval process.

To enable write access on your PR from Airbyte maintainers, please check the "Allow edits from maintainers" box when submitting from your PR. You must also create your PR from a fork in your **personal GitHub account** rather than an organization account, or else you will not see this option. The requirement to create from your personal fork is based on GitHub's additional security restrictions for PRs created from organization forks. For more information about the GitHub security model, please see the [GitHub documentation page regarding PRs from forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/allowing-changes-to-a-pull-request-branch-created-from-a-fork).

For more details on contribution requirements, please see our [contribution workflow documentation](https://docs.airbyte.com/community/contributing-to-airbyte#standard-contribution-workflow).

warning

Do not submit a pull request using the default branch of your forked repository. This will block Airbyte maintainers from pushing changes to your branch.

## Connector contributions[​](#connector-contributions "Direct link to Connector contributions")

Guidelines for connector contributions included in the [Connector Development Guide](/platform/connector-development/.md):

* [Contribute a New Connector](/platform/connector-development/submit-new-connector.md) - Guide to submitting a new connector to Airbyte.
* [Developing Connectors Locally](/platform/connector-development/local-connector-development.md) - Guide to setting up your local environment for connector development.
* [Breaking Changes in Connectors](/platform/connector-development/connector-breaking-changes.md) - Guide to breaking changes and version updates.

## Documentation contributions[​](#documentation-contributions "Direct link to Documentation contributions")

We welcome all pull requests that clarify concepts, fix typos and grammar, and improve the structure of Airbyte's documentation. Check the [Updating Documentation](/community/contributing-to-airbyte/writing-docs.md) guide for details on submitting documentation changes.

For examples of good connector docs, see the [Salesforce source connector](/integrations/sources/salesforce.md) and [Snowflake destination connector](/integrations/destinations/snowflake.md) docs.

## Community Content[​](#community-content "Direct link to Community Content")

We welcome contributions as new tutorials / showcases / articles, or as enhancements to any of the existing guides on our tutorials page. Head to this repo dedicated to community content: [Write for the Community](https://github.com/airbytehq/write-for-the-community).

Feel free to submit a pull request in this repo, if you have something to add even if it's not related to anything mentioned above.

## Engage with the Community[​](#engage-with-the-community "Direct link to Engage with the Community")

Another crucial way to contribute is by reporting bugs and helping other users in the community. You're welcome to join the [Community Slack](https://slack.airbyte.io). Refer to our [Issues and Feature Requests](/community/contributing-to-airbyte/issues-and-requests.md) guide to learn about the best ways to report bugs.
