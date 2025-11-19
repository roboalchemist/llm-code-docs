# Source: https://docs.augmentcode.com/codereview/overview.md

# Source: https://docs.augmentcode.com/cli/overview.md

# Source: https://docs.augmentcode.com/cli/automation/overview.md

# Source: https://docs.augmentcode.com/codereview/overview.md

# Using Augment Code Review

> Use Augment Code Review to catch critical issues, comment on PRs, and collaborate on fixes.

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

## Introduction

Augment Code Review provides a native GitHub experience for reviewing pull requests. With [Augment Code's extension](https://docs.augmentcode.com/quickstart#1-install-the-augment-extension) and [Auggie CLI](https://docs.augmentcode.com/cli/overview),
writing code is no longer the bottleneck—reviewing is. Code Review helps developers complete reviews faster while reducing bugs that reach production.

<CardGroup cols={1}>
  <Card title="Code Review Admin Guide" href="/codereview/admin-guide" icon="gear">
    Ask your plan Administrator to configure Augment Code Review and grant repository access on GitHub.
  </Card>
</CardGroup>

## Getting Started

Your plan Enterprise Administrator can [configure](https://app.augmentcode.com/settings/code-review) Augment Code Review to review automatically, or you can request a review by commenting on your PR.

* **Automatic Review on PR Opened:** Augment Code Review will automatically review and post a comment as soon as the PR is opened in GitHub. Use it when your teams want immediate feedback on all pull requests.
* **Request Review by Manual command:** Trigger a review by commenting on the PR with any of the following: `auggie review`, `augment review`, or `augmentcode review`. Augment Code Review will add 👀 to the comment so you know it is reviewing the PR. If Code Review finds an issue, it will leave a comment. If no issues are found, you'll see a comment saying "Review completed. No suggestions at this time."
* **Disabled:** Turn off Augment Code Review for a specific repository.

***

## How Augment Code Review Gathers Context

Code Review provides high-quality reviews by gathering context from multiple sources:

**PR Contents**: The agent analyzes the complete code diff to understand what changed and why.

**Entire Repository**: Through Augment's Context Engine, the agent has access to your full codebase, enabling it to identify cross-system impacts and maintain consistency with existing patterns.

**PR Title and Description**: More detailed PR descriptions help the agent provide better, more targeted reviews. Include information about:

* What the PR accomplishes
* Why the changes were made
* Any special considerations or context

**Custom Guidelines**: Repository-specific review guidelines defined in `.augment/code_review_guidelines.yaml` help the agent focus on what matters most to your team. See the [Admin Guide](/codereview/admin-guide#tell-augment-code-review-to-check-specific-areas-with-guidelines) for details on configuring guidelines.

**MCP Tools**: Integration with Model Context Protocol tools will provide additional context sources and capabilities.

***

## Review Quality and Focus

Augment Code Review prioritizes high signal-to-noise ratio by focusing on high-impact issues:

* **Bugs**: Logic errors, edge cases, and potential runtime issues
* **Security concerns**: Vulnerabilities, unsafe operations, and data exposure risks
* **Correctness**: Null handling and error management
* **Cross-system problems**: Breaking changes, API compatibility, and integration issues

The agent avoids low-value style nags and focuses on objective issues that can cause real problems in production.

***

## Best Practices

**Write detailed PR descriptions**: The more context you provide in your PR title and description, the better the agent can understand your intent and provide relevant feedback.

**Use custom guidelines**: Define repository-specific review guidelines to help the agent focus on your team's priorities and domain-specific concerns.

**Provide feedback**: Give feedback on comments using the thumbs up emoji to indicate whether the comment is useful or thumbs down if the comment was not helpful.

**Ask for a follow-up review**: If you make significant changes to the PR and want another review, then ask for a follow-up review by commenting on your PR with the same comments as a manual request: `auggie review`, `augment review`, or `augmentcode review`. The agent will add 👀 to the comment so you know it is reviewing the PR.
