# Source: https://docs.gitguardian.com/self-hosting/management/application-management/preferences.md

# Configure preferences

> Configure application-level preferences for your GitGuardian self-hosted instance.

In order to configure preferences to fine tune your GitGuardian instance, navigate to **Settings > General > Preferences**.

:::warning
Please be careful some preferences allow you to activate features in beta mode. If in doubt, please seek advice from [GitGuardian team](../../troubleshoot/support).
:::

## Table of Preferences

### General

| Preference                          | Default Value | Description                                                                                                                                                                    |
| ----------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `token_expire_in_days`              | 7             | Lifespan, in days, of invitations and password reset links                                                                                                                     |
| `presence_check_enabled`            | true          | Enable secret presence check. For more info, please refer to [Investigate incidents page](../../../internal-monitoring/remediate/investigate-incidents#secret-presence-checks) |
| `presence_check_display_enabled`    | true          | Enable display of secret presence checks                                                                                                                                       |
| `background_presence_check_enabled` | true          | Enable automatic secret presence check in background tasks                                                                                                                     |
| `validity_check_enabled`            | true          | Enable secret validity check                                                                                                                                                   |
| `background_validity_check_enabled` | true          | Enable automatic secret validity check in background tasks                                                                                                                     |

### SAML SSO

For more info, please refer to the [SAML SSO page](../../../platform/enterprise-administration/saml-sso-configuration).

| Preference                        | Default Value | Description                                                          |
| --------------------------------- | ------------- | -------------------------------------------------------------------- |
| `use_model_signature_settings`    | true          | Enable the manual configurations of the SAML signatures requirements |
| `is_custom_nameid_format_enabled` | false         | Enable the choice of NameID format                                   |

### Bitbucket

For more info, please refer to the [Bitbucket integration documentation](../../../internal-monitoring/integrate-sources/vcs-integrations/bitbucket).

| Preference                | Default Value | Description                                                                                         |
| ------------------------- | ------------- | --------------------------------------------------------------------------------------------------- |
| `min_delay_between_syncs` | 60            | Minimum delay, in minutes, between two consecutive synchronizations of a Bitbucket installation     |
| `auth_error_grace_period` | 0             | Minimum period, in minutes, of repeated authentication errors after which a token should be revoked |

### On Premise

| Preference                            | Default Value | Description                                                                                                                                                            |
| ------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bitbucket_disable_admin_check`       | false         | Disable Bitbucket integration Admin Check when creating integration                                                                                                    |
| `prometheus_metrics_active`           | false         | Activate Prometheus Metrics Exporter on `/metrics`. For more info, please refer to [Applicative metrics page](/self-hosting/management/application-management/metrics) |
| `custom_telemetry_active`             | true          | Enable sending telemetry metrics to GitGuardian                                                                                                                        |
| `openai_api_key`                      | -             | OpenAI API key                                                                                                                                                         |
| `tls_client_force_second_factor_auth` | false         | Multi-factor authentication option for Certificate-Based Authentication                                                                                                |

### Notifier

For more info, please refer to the [Custom webhook page](../../../platform/configure-alerting/notifiers-integrations/custom-webhook).

| Preference                          | Default Value | Description                                                |
| ----------------------------------- | ------------- | ---------------------------------------------------------- |
| `max_webhooks_per_integration_type` | 1000          | Maximum number of configured webhooks per integration type |

### Source Scanner (VCS)

For more info, please refer to the [Historical scanning page](../../../internal-monitoring/integrate-sources/monitored-perimeter#historical-scanning).

| Preference                         | Default Value | Description                                                          |
| ---------------------------------- | ------------- | -------------------------------------------------------------------- |
| `minutes_between_scans_per_source` | 0             | Minimum minutes between two scans on the same source. (0 = disabled) |

### Source Scanner

| Preference                                       | Default Value | Description                                                                      |
| ------------------------------------------------ | ------------- | -------------------------------------------------------------------------------- |
| `servicenow_data_source_recurrent_scan_interval` | 21600         | Minimum seconds between two recurrent scans on ServiceNow sources.               |
| `aws_ecr_recurrent_scan_interval`                | 172800        | Minimum seconds between two recurrent scans on Amazon ECR sources.               |
| `azure_cr_recurrent_scan_interval`               | 172800        | Minimum seconds between two recurrent scans on Azure Container Registry sources. |
| `google_artifact_recurrent_scan_interval`        | 172800        | Minimum seconds between two recurrent scans on Google Artifact Registry sources. |
| `docker_hub_recurrent_scan_interval`             | 172800        | Minimum seconds between two recurrent scans on Docker Hub sources.               |
| `jfrog_artifact_recurrent_scan_interval`         | 172800        | Minimum seconds between two recurrent scans on JFrog Container Registry sources. |
| `microsoft_teams_recurrent_scan_interval`        | 21600         | Minimum seconds between two recurrent scans on Microsoft Teams sources.          |
| `microsoft_teams_recurrent_scan_window`          | 1209600       | Time window, in seconds, for Microsoft Teams recurrent scans.                    |
| `jfrog_package_registry_recurrent_scan_interval` | 28800         | Minimum seconds between two recurrent scans on JFrog Package Registry sources.   |
| `sharepoint_online_recurrent_scan_interval`      | 21600         | Minimum seconds between two recurrent scans on SharePoint Online sources.        |
| `microsoft_onedrive_recurrent_scan_interval`     | 21600         | Minimum seconds between two recurrent scans on Microsoft OneDrive sources.       |

### Container Registries

| Preference                                  | Default Value | Description                                                                                                |
| ------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------- |
| `enable_repository_scoped_layers_cache`     | false         | Include repository name in layers cache keys to scope cache per repository. This allows creating multiple secret occurrences instead of just one when we encounter the same layer with the same secret across different images.

### Policy

| Preference                         | Default Value | Description                                                                                                                                                                                                          |
| ---------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `is_repo_size_controlled`          | false         | Limit size of repositories for historical scan. (removed in _2024.9.0_)                                                                                                                                              |
| `repo_scan_size_limit`             | 1073741824    | Maximum repository size for historical scan, in Byte. For more info, please refer to the following [page](../../../internal-monitoring/integrate-sources/monitored-perimeter#historical-scanning).                   |
| `repo_scan_pending_limit_in_hours` | 168           | Timeout, in hours, of the queue time of a repository's historical scan. For more info, please refer to the following [page](../../../internal-monitoring/integrate-sources/monitored-perimeter#historical-scanning). |
| `repo_scan_time_limit_in_sec`      | 7200          | Timeout, in seconds, for historical scan of repository. For more info, please refer to the following [page](../../../internal-monitoring/integrate-sources/monitored-perimeter#historical-scanning).                 |
| `maximum_scan_size`                | 1048576       | Maximum document size for secrets detection scan via API, in bytes.                                                                                                                                                  |
| `repo_scan_max_commit_length`      | 1073741824    | Maximum total length of a commit to scan, in Byte, larger commits are truncated (-1 = unlimited).                                                                                                                    |
| `displayed_content_max_size`       | 10485760      | Maximum displayed content size, in Byte. Introduced in 2023.11.                                                                                                                                                      |
| `displayed_content_max_lines`      | 100000        | Maximum displayed content lines. Introduced in 2023.11.                                                                                                                                                              |
| `skip_unchanged_scans`             | True          | This setting allows skipping the historical scan of a repository if it has not changed since the last scan.                                                                                                          |

### Public API

For more info, please refer to our [API documentation](../../../platform/gitguardian-suite/api).

| Preference                    | Default Value | Description                                                                                                                                                     |
| ----------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `maximum_multifile_documents` | 20            | Maximum number of files in a multi-file document for scanning via API                                                                                           |
| `maximum_token_per_account`   | 150           | Maximum number of API keys allowed per workspace                                                                                                                |
| `maximum_token_per_member`    | 5             | Maximum number of personal access tokens allowed per member                                                                                                     |
| `quotas`                      | 10000000      | Monthly sliding quotas for API calls (removed in _2024.7.0_)                                                                                                    |
| `max_page_size`               | 100           | Upper bound of the `per_page` parameter in the Public API which controls the number of data returned in [paginated endpoints](../../../api-docs/pagination.md). |

### GitHub

For more info, please refer to the [GitHub integration documentation](../../../internal-monitoring/integrate-sources/vcs-integrations/github).

| Preference                        | Default Value | Description                                                                                                                                                                                       |
| --------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `is_actionable_checkrun_enabled`  | false         | Enables action buttons on checkruns (removed in _2024.2.0_)                                                                                                                                       |
| `check_runs_overrides_labels_ghe` | false         | Enable overriding the check run settings with repository labels on GitHub Enterprise Server                                                                                                       |
| `commit_collector_max_workers`    | 4             | Maximum number of calls per worker for the commit collector. Higher number will make the commit collection faster, but is more prone to reach GitHub rate limits. Expected value between 1 and 4. |

### Filters

| Preference           | Default Value | Description                                                                                          |
| -------------------- | ------------- | ---------------------------------------------------------------------------------------------------- |
| `ai_filters_enabled` | false         | Enable AI filters on the compatible pages, it requires an [OpenAI API key](#on-premise) to be setup. |

### Health Checks

For more info, please refer to the [Checking environment health page](../../troubleshoot/health-check).

| Preference                      | Default Value | Description                                                                   |
| ------------------------------- | ------------- | ----------------------------------------------------------------------------- |
| `periodic_enabled`              | true          | Enable periodic health checks.                                                |
| `periodic_interval`             | 1h            | Removed in _2024.7.0_, now configurable with `spread_periodic_range_minutes`. |
| `spread_periodic_range_minutes` | 60            | Interval between two runs of periodic health checks (in minutes).             |

### Teams

For more info, please refer to the [teams page](../../../platform/collaboration-and-sharing/teams).

| Preference  | Default Value | Description                                                                           |
| ----------- | ------------- | ------------------------------------------------------------------------------------- |
| `max_teams` | 500           | Maximum of team allowed on an account. â ï¸ Exceeding this limit may impact performance. |

### Remediation Tracking

For more info, please refer to the [Remediation tracking page](../../../internal-monitoring/remediate/prioritize-incidents#impacted-perimeter).

| Preference                         | Default Value | Description                                                                                                   |
| ---------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------- |
| `scan_after_push_force_rate_limit` | 300           | Rate limit in seconds for scan started by the file tracking engine. Applied per source, branch and scan type. |

### Custom tags

| Preference                                    | Default Value | Description                                                                                                            |
| --------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `max_custom_tag_keys_per_workspace`           | 50            | The maximum number of custom tags keys per workspace. `oneword` custom tags count as 1 key                             |
| `max_custom_tag_values_per_key_per_workspace` | 50            | The maximum number of custom tags values for a given key. `oneword` custom tags count as 1 value for the `oneword` key |
| `max_custom_tags_per_resource`                | 100           | The maximum number of custom tags linked to 1 resource (e.g. honeytoken, private incident, etc)                        |

<!-- ### Code Fixing

|| Preference                    | Default Value | Description                                                                                                       |
|| ----------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------- |
|| `llm_name`                    | -             | Name of the LLM used to fix code, must be defined in https://docs.litellm.ai/docs/providers                       |
|| `llm_api_key`                 | -             | LLM API key used to fix code                                                                                      |
|| `max_per_location_request`    | 50            | Maximum number of code fixing requests per location request. Each code fix request makes an API call to the LLM.  | -->

### Background Presence Check Frequencies

For more info, please refer to the [Investigate incidents page](../../../internal-monitoring/remediate/investigate-incidents#secret-presence-checks).

| Preference        | Default Value | Description                                                                                                            |
| ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `ignored_old`     | 0             | Frequency, in days, of automated checks for presence in git history for ignored secret incidents more than 1 year old  |
| `ignored_recent`  | 178           | Frequency, in days, of automated checks for presence in git history for ignored secret incidents less than 1 year old  |
| `open_old`        | 7             | Frequency, in days, of automated checks for presence in git history for open secret incidents more than 1 year old     |
| `open_recent`     | 1             | Frequency, in days, of automated checks for presence in git history for open secret incidents less than 1 year old     |
| `resolved_old`    | 178           | Frequency, in days, of automated checks for presence in git history for resolved secret incidents more than 1 year old |
| `resolved_recent` | 30            | Frequency, in days, of automated checks for presence in git history for resolved secret incidents less than 1 year old |

### Background Validity Check Frequencies

For more info, please refer to the [Validity checks page](../../../secrets-detection/customize-detection/validity-checks).

| Preference        | Default Value | Description                                                                                                |
| ----------------- | ------------- | ---------------------------------------------------------------------------------------------------------- |
| `ignored_old`     | 178           | Frequency, in days, of automated secret validity checks for ignored secret incidents more than 1 year old  |
| `ignored_recent`  | 30            | Frequency, in days, of automated secret validity checks for ignored secret incidents less than 1 year old  |
| `open_old`        | 7             | Frequency, in days, of automated secret validity checks for open secret incidents more than 1 year old     |
| `open_recent`     | 1             | Frequency, in days, of automated secret validity checks for open secret incidents less than 1 year old     |
| `resolved_old`    | 178           | Frequency, in days, of automated secret validity checks for resolved secret incidents more than 1 year old |
| `resolved_recent` | 30            | Frequency, in days, of automated secret validity checks for resolved secret incidents less than 1 year old |
