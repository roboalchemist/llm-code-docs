# Source: https://docs.gitguardian.com/public-monitoring/perimeter/github-organizations.md

# GitHub organizations

> Add and manage GitHub organizations in your Public Monitoring perimeter, including monitoring private members via a personal access token.

GitGuardian can monitor multiple GitHub organizations that belong to your company. Once configured, GitGuardian will:
- scan every commit on each repository of the GitHub organization,
- add the organizationâs *members* to the list of monitored developers, and scan any of their public activity.

## Adding organizations to your perimeter

To add GitHub organizations to your monitored list, GitGuardian needs the GitHub ID of each organization. Contact our **[support team](mailto:support@gitguardian.com)** if you are missing a company-owned organization in your perimeter.

## Monitoring private members

You can enrich the list of [monitored developers](./developers.md) with the private members of your GitHub organization by providing GitGuardian an access token with `read:org` scope.

:::info
Please note that we currently only accept classic tokens from GitHub. Fine-grained tokens are not supported at this time.
:::

### Step 1: Generate a personal access token

Generate a personal access token (classic) from a GitHub account with access to the organization. Select "No expiration" so that GitGuardian can continuously monitor the future addition/removal of members.

![Generate GitHub token](/img/public-monitoring/perimeter/generate-github-token.png)

### Step 2: Submit the token to GitGuardian

Go to your GitGuardian's settings in [Integration > Sources > GitHub Public](https://dashboard.gitguardian.com/workspace/settings/integrations/public_monitoring), click "Monitor private members" and submit the GitHub token generated in the previous step.

![Monitor private members](/img/public-monitoring/perimeter/monitor-private-members-button.png)
![Monitor private members - submit token](/img/public-monitoring/perimeter/monitor-private-members-token.png)

## Managing your organization perimeter

To view and manage GitHub organizations in your perimeter:

1. Navigate to [Perimeter > Public sources](https://dashboard.gitguardian.com/public-perimeter/sources)
2. Review the list of monitored organizations and repositories
3. Contact our **[support team](mailto:support@gitguardian.com)** to add missing company-owned organizations
