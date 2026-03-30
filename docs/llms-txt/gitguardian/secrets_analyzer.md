# Source: https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/secrets_analyzer.md

# Secrets Analyzers

> Two Slack API keys may seem to offer the same accesses, but their associated
permissions can differ significantly. If a secret with the permission
`read:profile` is exposed, it will cause less harm than a secret with
`read:everything`. It's important to share this information with users so they
can prioritize their remediation efforts.

# Secrets Analyzers

Two Slack API keys may seem to offer the same accesses, but their associated
permissions can differ significantly. If a secret with the permission
`read:profile` is exposed, it will cause less harm than a secret with
`read:everything`. It's important to share this information with users so they
can prioritize their remediation efforts.

The Secrets Analyzer feature offers additional context on detected secrets,
including their roles and permissions, as well as relevant contextual
information such as ownership and perimeter when found. This helps security
teams evaluate the potential impact of a secret incident and effectively
prioritize their remediation efforts.

Understanding the context of a secret is a game changer for assessing the impact
of a secret incident, as it directly correlates to the possible damages in the
event of a breach.

## Activate the feature

The feature is activated by default. To disable it, navigate to `Settings > Secrets > General`.

Once activated, the analyzer will immediately work on upcoming incidents but
also existing incidents.

## Helping Prioritize with a Built-in Saved View: `Critical Scopes`

To help you quickly identify incidents involving secrets with permissions that
require your immediate attention, we provide the built-in saved view
`Critical Scopes`. This view filters for the most critical permissions
associated with the analyzers we currently implement.

In the future, we will update this saved view to include additional permissions
as we add more analyzers.

![Secrets Analyzer Saved View](/img/secrets-detection/secrets-analyzers/secrets_analyzer_saved_view.png)

#### What permissions does this saved view encompass ?

##### GitHub PAT Fine Grained

  ```
  # Repo permissions
  Administration:Read, ReadWrite
  Contents:Read, ReadWrite
  Environments:Read, ReadWrite
  Secret scanning alerts:Read,ReadWrite
  Secrets:Read, ReadWrite

  # Accounts permissions
  Codespaces user secrets:Read, ReadWrite
  GPG keys: Read, ReadWrite
  Git SSH keys: Read, ReadWrite
  ```

##### GitHub PAT Classic

  ```
  admin:org
  repo
  write:packages
  write:org
  delete:packages
  read:org
  admin:public_key
  admin:org_hook
  delete_repo
  admin:enterprise
  admin:gpg_key
  admin:ssh_signing_key
  ```

##### Gitlab PAT

  ```
  api
  read_repository
  read_api
  admin_mode
  sudo
  ```

##### Stripe

  ```
  credit_note_read
  credit_note_write
  coupon_read
  promotion_code_read
  terminal_reader_read
  terminal_reader_write
  secret_write
  token_read
  token_write
  transfer_read
  transfer_write
  charge_read
  charge_write
  apple_pay_domain_read
  apple_pay_domain_write
  terminal_connection_token_write
  ```

## New Filters for Navigating Incidents with Discovered Permissions

The **Secret Scopes** filter enables you to filter incidents based on the
permissions associated with your secret. This lets you quickly identify
incidents involving secrets with the most impactful permissions.

Additionally, the **Secret Analyzer** lets you filter incidents by their
analyzer statuses, such as "Successful" and "Failed."

![Secrets Analyzer Filters](/img/secrets-detection/secrets-analyzers/secrets_analyzer_filters.png)

## When is the analysis triggered ?

This chapter outlines the automated system for secret analysis. The system performs regular checks on secrets to ensure analysis results are up-to-date.

### Backpopulate Task

A backpopulate task runs every 15 minutes to identify any secrets missing analysis and initiates the analysis process for them. This ensures continuous monitoring of all secrets in the system.

### Immediate Task Scheduling

Tasks are scheduled for immediate execution in the following scenarios:
- **Incident Creation**: When a new incident is created, analysis is scheduled immediately and typically completes within a few minutes.
- **Manual Trigger**: When a user manually triggers an analysis, the task is scheduled immediately and typically completes within a few minutes.

### Periodic Re-checking

For secrets that have already been analyzed, the system implements a periodic re-checking mechanism.

#### Validity Check and Analysis

Secrets with validity status of **VALID**, **NOT_CHECKED**, or **FAILED_TO_CHECK** are re-checked periodically until they are found invalid. During these checks, both validity verification and analysis are performed.

#### Check Frequency

The frequency of checks varies based on several factors:
1. **Incident Status**: Whether the incident is open, resolved, or ignored
2. **Incident Age**: Whether the incident is recent (less than 1 year old) or old

This approach prevents excessive API calls that could trigger rate limits on the checked services, which would compromise the accuracy of the checks.

#### Default Check Periods (in days)

| Status & Age | Business Account |
|-------------|-----------------|
| Open & Recent | 1 |
| Open & Old | 7 |
| Resolved & Recent | 30 |
| Resolved & Old | 178 |
| Ignored & Recent | 178 |
| Ignored & Old | Never |

*Note: "Never" indicates that no automatic re-checking is scheduled for these categories.*

## Available Analyzers

-   [Airtable API Key](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/airtable_apikey#secret-analyzer)
-   [Algolia Keys](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/algolia_keys#secret-analyzer)
-   [Artifactory Access Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/artifactory_access_token#secret-analyzer)
-   [Artifactory Reference Token With Host](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/artifactory_reference_token_with_host#secret-analyzer)
-   [Artifactory Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/artifactory_token#secret-analyzer)
-   [Auth0 Keys](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/auth0_keys#secret-analyzer)
-   [Bitbucket Access Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/bitbucket_access_token#secret-analyzer)
-   [BitBucket App Password](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/bitbucket_app_password#secret-analyzer)
-   [Buildkite API Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/buildkite_api_token#secret-analyzer)
-   [CircleCI Personal Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/circleci_personal_token#secret-analyzer)
-   [DigitalOcean Spaces Keys](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/digitalocean_spaces_token#secret-analyzer)
-   [Fastly Personal Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/fastly_personal_token#secret-analyzer)
-   [GitHub Personal Access Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/github_access_token#secret-analyzer)
-   [GitLab Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/gitlab_token#secret-analyzer)
-   [HubSpot Private Application Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/hubspot_private_app_token#secret-analyzer)
-   [Hugging Face user access token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/hugging_face_user_access_token#secret-analyzer)
-   [IBM Cloud Key](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/ibm_cloud_key#secret-analyzer)
-   [Jira Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/jira_token#secret-analyzer)
-   [MongoDB Credentials](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/mongodb_credentials#secret-analyzer)
-   [MySQL Credentials](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/mysql_credentials#secret-analyzer)
-   [OpenAI Admin API Key](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/openai_admin_apikey#secret-analyzer)
-   [OpenAI API Key](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/openai_apikey#secret-analyzer)
-   [OpenAI Project API Key](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/openai_project_apikey#secret-analyzer)
-   [OpenAI Project API Key v2](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/openai_project_apikey_v2#secret-analyzer)
-   [OpenAI Service Account](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/openai_service_account#secret-analyzer)
-   [PayPal OAuth2 Keys](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/paypal_oauth2_keys#secret-analyzer)
-   [Plaid Keys](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/plaid_keys#secret-analyzer)
-   [PostgreSQL Credentials](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/postgresql_credentials#secret-analyzer)
-   [SendGrid Key](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/sendgrid_key#secret-analyzer)
-   [SendinBlue Key](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/sendinblue_key#secret-analyzer)
-   [Shopify Generic App Token With Subdomain](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/shopify_generic_app_token_subdomain#secret-analyzer)
-   [Slack App Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/slack_app_token#secret-analyzer)
-   [Slack User Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/slack_user_token#secret-analyzer)
-   [Slack Bot Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/slackbot_token#secret-analyzer)
-   [Square Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/square_token#secret-analyzer)
-   [Stripe Keys](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/stripe_keys#secret-analyzer)
-   [Terraform Cloud Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/terraform_cloud_token#secret-analyzer)
-   [Xray Access Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/xray_access_token#secret-analyzer)
-   [Zendesk Token](https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/detectors/specifics/zendesk_token#secret-analyzer)

## Infrastructure

If your account is on our SaaS environment (EU or US), please be aware that all requests made by the Secret Analyzer will originate [from these listed IP addresses.](/internal-monitoring/integrate-sources/monitored-perimeter#troubleshooting-connectivity-problems)
