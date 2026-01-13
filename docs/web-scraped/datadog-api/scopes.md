# Source: https://docs.datadoghq.com/api/latest/scopes

## [Authorization scopes for OAuth clients](https://docs.datadoghq.com/api/latest/scopes/#authorization-scopes-for-oauth-clients)
Scopes are an authorization mechanism that allow you to limit and define the specific access applications have to an organization’s Datadog data. When authorized to access data on behalf of a user or service account, applications can only access the information explicitly permitted by their assigned scopes.
This page lists only the authorization scopes that can be assigned to OAuth clients. To view the full list of assignable permissions for scoped application keys, see [Datadog Role Permissions](https://docs.datadoghq.com/account_management/rbac/permissions/#permissions-list).
  * **OAuth clients** → Can only be assigned authorization scopes (limited set).
  * **Scoped application keys** → Can be assigned any Datadog permission.


The best practice for scoping applications is to follow the principle of least privilege. Assign only the minimum scopes necessary for an application to function as intended. This enhances security and provides visibility into how applications interact with your organization’s data. For example, a third-party application that only reads dashboards does not need permissions to delete or manage users.
You can use authorization scopes with OAuth2 clients for your [Datadog Apps](https://docs.datadoghq.com/developers/datadog_apps/#oauth-api-access).
#### API Management, Synthetics
Scope name
Description
Endpoints that require this scope
apm_api_catalog_read
View API catalog and API definitions.
[Get all global variables](https://docs.datadoghq.com/api/latest/synthetics/#get-all-global-variables)  
[List APIs](https://docs.datadoghq.com/api/latest/api-management/#list-apis)  
[Get an API](https://docs.datadoghq.com/api/latest/api-management/#get-an-api)  

apm_api_catalog_write
Add, modify, and delete API catalog definitions.
[Delete an API](https://docs.datadoghq.com/api/latest/api-management/#delete-an-api)  
[Update an API](https://docs.datadoghq.com/api/latest/api-management/#update-an-api)  
[Create a new API](https://docs.datadoghq.com/api/latest/api-management/#create-a-new-api)  

synthetics_global_variable_read
View, search, and use Synthetics global variables.
[Get all global variables](https://docs.datadoghq.com/api/latest/synthetics/#get-all-global-variables)  
[Get a global variable](https://docs.datadoghq.com/api/latest/synthetics/#get-a-global-variable)  

synthetics_global_variable_write
Create, edit, and delete global variables for Synthetics.
[Create a global variable](https://docs.datadoghq.com/api/latest/synthetics/#create-a-global-variable)  
[Delete a global variable](https://docs.datadoghq.com/api/latest/synthetics/#delete-a-global-variable)  
[Edit a global variable](https://docs.datadoghq.com/api/latest/synthetics/#edit-a-global-variable)  

synthetics_private_location_read
View, search, and use Synthetics private locations.
[Get all locations (public and private)](https://docs.datadoghq.com/api/latest/synthetics/#get-all-locations-public-and-private)  
[Get a private location](https://docs.datadoghq.com/api/latest/synthetics/#get-a-private-location)  

synthetics_private_location_write
Create and delete private locations in addition to having access to the associated installation guidelines.
[Create a private location](https://docs.datadoghq.com/api/latest/synthetics/#create-a-private-location)  
[Delete a private location](https://docs.datadoghq.com/api/latest/synthetics/#delete-a-private-location)  
[Edit a private location](https://docs.datadoghq.com/api/latest/synthetics/#edit-a-private-location)  

synthetics_read
List and view configured Synthetic tests and test results.
[Get details of batch](https://docs.datadoghq.com/api/latest/synthetics/#get-details-of-batch)  
[Get the list of all Synthetic tests](https://docs.datadoghq.com/api/latest/synthetics/#get-the-list-of-all-synthetic-tests)  
[Get an API test](https://docs.datadoghq.com/api/latest/synthetics/#get-an-api-test)  
[Get a browser test](https://docs.datadoghq.com/api/latest/synthetics/#get-a-browser-test)  
[Get a browser test's latest results summaries](https://docs.datadoghq.com/api/latest/synthetics/#get-a-browser-tests-latest-results-summaries)  
[Get a browser test result](https://docs.datadoghq.com/api/latest/synthetics/#get-a-browser-test-result)  
[Get a Mobile test](https://docs.datadoghq.com/api/latest/synthetics/#get-a-mobile-test)  
[Search Synthetic tests](https://docs.datadoghq.com/api/latest/synthetics/#search-synthetic-tests)  
[Fetch uptime for multiple tests](https://docs.datadoghq.com/api/latest/synthetics/#fetch-uptime-for-multiple-tests)  
[Get a test configuration](https://docs.datadoghq.com/api/latest/synthetics/#get-a-test-configuration)  
[Get an API test's latest results summaries](https://docs.datadoghq.com/api/latest/synthetics/#get-an-api-tests-latest-results-summaries)  
[Get an API test result](https://docs.datadoghq.com/api/latest/synthetics/#get-an-api-test-result)  

synthetics_write
Create, edit, and delete Synthetic tests.
[Create a test](https://docs.datadoghq.com/api/latest/synthetics/#create-a-test)  
[Create an API test](https://docs.datadoghq.com/api/latest/synthetics/#create-an-api-test)  
[Edit an API test](https://docs.datadoghq.com/api/latest/synthetics/#edit-an-api-test)  
[Create a browser test](https://docs.datadoghq.com/api/latest/synthetics/#create-a-browser-test)  
[Edit a browser test](https://docs.datadoghq.com/api/latest/synthetics/#edit-a-browser-test)  
[Delete tests](https://docs.datadoghq.com/api/latest/synthetics/#delete-tests)  
[Create a mobile test](https://docs.datadoghq.com/api/latest/synthetics/#create-a-mobile-test)  
[Edit a Mobile test](https://docs.datadoghq.com/api/latest/synthetics/#edit-a-mobile-test)  
[Trigger Synthetic tests](https://docs.datadoghq.com/api/latest/synthetics/#trigger-synthetic-tests)  
[Trigger tests from CI/CD pipelines](https://docs.datadoghq.com/api/latest/synthetics/#trigger-tests-from-ci/cd-pipelines)  
[Patch a Synthetic test](https://docs.datadoghq.com/api/latest/synthetics/#patch-a-synthetic-test)  
[Edit a test](https://docs.datadoghq.com/api/latest/synthetics/#edit-a-test)  
[Pause or start a test](https://docs.datadoghq.com/api/latest/synthetics/#pause-or-start-a-test)  

#### APM, Spans
Scope name
Description
Endpoints that require this scope
apm_read
Read and query APM and Trace Analytics.
[Get service list](https://docs.datadoghq.com/api/latest/apm/#get-service-list)  
[Aggregate spans](https://docs.datadoghq.com/api/latest/spans/#aggregate-spans)  
[Get a list of spans](https://docs.datadoghq.com/api/latest/spans/#get-a-list-of-spans)  
[Search spans](https://docs.datadoghq.com/api/latest/spans/#search-spans)  

#### Agentless Scanning, Domain Allowlist, Downtimes, IP Allowlist, Monitors
Scope name
Description
Endpoints that require this scope
org_management
Edit org configurations, including authentication and certain security preferences such as configuring SAML, renaming an org, configuring allowed login methods, creating child orgs, subscribing & unsubscribing from apps in the marketplace, and enabling & disabling Remote Configuration for the entire organization.
[Create AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-scan-options)  
[Delete AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-aws-scan-options)  
[Update AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-aws-scan-options)  
[Create Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-azure-scan-options)  
[Delete Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-azure-scan-options)  
[Update Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-azure-scan-options)  
[Create GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-gcp-scan-options)  
[Delete GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-gcp-scan-options)  
[Update GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-gcp-scan-options)  
[Create AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  
[Get IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#get-ip-allowlist)  
[Update IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#update-ip-allowlist)  

security_monitoring_findings_read
View a list of findings that include both misconfigurations and identity risks.
[List AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-scan-options)  
[Get AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-scan-options)  
[List Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-azure-scan-options)  
[Get Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-azure-scan-options)  
[List GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-gcp-scan-options)  
[Get GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-gcp-scan-options)  
[List AWS on demand tasks](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-on-demand-tasks)  
[Get AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-on-demand-task)  
[List findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-findings)  
[Get a finding](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-finding)  
[List security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-security-findings)  
[Search security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#search-security-findings)  

monitors_write
Edit, delete, and resolve individual monitors.
[Create a monitor](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor)  
[Delete a monitor](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor)  
[Edit a monitor](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor)  
[Mute a monitor](https://docs.datadoghq.com/api/latest/monitors/#mute-a-monitor)  
[Unmute a monitor](https://docs.datadoghq.com/api/latest/monitors/#unmute-a-monitor)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  

monitors_downtime
Set downtimes to suppress alerts from any monitor in an organization. Mute and unmute monitors. The ability to write monitors is not required to set downtimes.
[Schedule a downtime](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime)  
[Cancel downtimes by scope](https://docs.datadoghq.com/api/latest/downtimes/#cancel-downtimes-by-scope)  
[Cancel a downtime](https://docs.datadoghq.com/api/latest/downtimes/#cancel-a-downtime)  
[Update a downtime](https://docs.datadoghq.com/api/latest/downtimes/#update-a-downtime)  
[Get all downtimes](https://docs.datadoghq.com/api/latest/downtimes/#get-all-downtimes)  
[Schedule a downtime](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime)  
[Cancel a downtime](https://docs.datadoghq.com/api/latest/downtimes/#cancel-a-downtime)  
[Get a downtime](https://docs.datadoghq.com/api/latest/downtimes/#get-a-downtime)  
[Update a downtime](https://docs.datadoghq.com/api/latest/downtimes/#update-a-downtime)  
[Get active downtimes for a monitor](https://docs.datadoghq.com/api/latest/downtimes/#get-active-downtimes-for-a-monitor)  

monitors_read
View monitors.
[Get all downtimes](https://docs.datadoghq.com/api/latest/downtimes/#get-all-downtimes)  
[Get a downtime](https://docs.datadoghq.com/api/latest/downtimes/#get-a-downtime)  
[Get all monitors](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitors)  
[Check if a monitor can be deleted](https://docs.datadoghq.com/api/latest/monitors/#check-if-a-monitor-can-be-deleted)  
[Monitors group search](https://docs.datadoghq.com/api/latest/monitors/#monitors-group-search)  
[Monitors search](https://docs.datadoghq.com/api/latest/monitors/#monitors-search)  
[Validate a monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor)  
[Get a monitor's details](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitors-details)  
[Get active downtimes for a monitor](https://docs.datadoghq.com/api/latest/downtimes/#get-active-downtimes-for-a-monitor)  
[Validate an existing monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor)  
[Get all monitor notification rules](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-notification-rules)  
[Get a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-notification-rule)  
[Get all monitor configuration policies](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-configuration-policies)  
[Get a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-configuration-policy)  
[Get all monitor user templates](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-user-templates)  
[Get a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-user-template)  

#### Agentless Scanning, Domain Allowlist, IP Allowlist, Monitors, Security Monitoring
Scope name
Description
Endpoints that require this scope
org_management
Edit org configurations, including authentication and certain security preferences such as configuring SAML, renaming an org, configuring allowed login methods, creating child orgs, subscribing & unsubscribing from apps in the marketplace, and enabling & disabling Remote Configuration for the entire organization.
[Create AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-scan-options)  
[Delete AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-aws-scan-options)  
[Update AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-aws-scan-options)  
[Create Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-azure-scan-options)  
[Delete Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-azure-scan-options)  
[Update Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-azure-scan-options)  
[Create GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-gcp-scan-options)  
[Delete GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-gcp-scan-options)  
[Update GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-gcp-scan-options)  
[Create AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  
[Get IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#get-ip-allowlist)  
[Update IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#update-ip-allowlist)  

security_monitoring_findings_read
View a list of findings that include both misconfigurations and identity risks.
[List AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-scan-options)  
[Get AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-scan-options)  
[List Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-azure-scan-options)  
[Get Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-azure-scan-options)  
[List GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-gcp-scan-options)  
[Get GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-gcp-scan-options)  
[List AWS on demand tasks](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-on-demand-tasks)  
[Get AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-on-demand-task)  
[List findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-findings)  
[Get a finding](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-finding)  
[List security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-security-findings)  
[Search security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#search-security-findings)  

monitors_write
Edit, delete, and resolve individual monitors.
[Create a monitor](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor)  
[Delete a monitor](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor)  
[Edit a monitor](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor)  
[Mute a monitor](https://docs.datadoghq.com/api/latest/monitors/#mute-a-monitor)  
[Unmute a monitor](https://docs.datadoghq.com/api/latest/monitors/#unmute-a-monitor)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  

monitors_read
View monitors.
[Get all downtimes](https://docs.datadoghq.com/api/latest/downtimes/#get-all-downtimes)  
[Get a downtime](https://docs.datadoghq.com/api/latest/downtimes/#get-a-downtime)  
[Get all monitors](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitors)  
[Check if a monitor can be deleted](https://docs.datadoghq.com/api/latest/monitors/#check-if-a-monitor-can-be-deleted)  
[Monitors group search](https://docs.datadoghq.com/api/latest/monitors/#monitors-group-search)  
[Monitors search](https://docs.datadoghq.com/api/latest/monitors/#monitors-search)  
[Validate a monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor)  
[Get a monitor's details](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitors-details)  
[Get active downtimes for a monitor](https://docs.datadoghq.com/api/latest/downtimes/#get-active-downtimes-for-a-monitor)  
[Validate an existing monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor)  
[Get all monitor notification rules](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-notification-rules)  
[Get a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-notification-rule)  
[Get all monitor configuration policies](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-configuration-policies)  
[Get a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-configuration-policy)  
[Get all monitor user templates](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-user-templates)  
[Get a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-user-template)  

code_analysis_read
View Code Analysis.
[Post dependencies for analysis](https://docs.datadoghq.com/api/latest/static-analysis/#post-dependencies-for-analysis)  
[POST request to resolve vulnerable symbols](https://docs.datadoghq.com/api/latest/static-analysis/#post-request-to-resolve-vulnerable-symbols)  
[Ruleset get multiple](https://docs.datadoghq.com/api/latest/security-monitoring/#ruleset-get-multiple)  
[Returns a list of Secrets rules](https://docs.datadoghq.com/api/latest/security-monitoring/#returns-a-list-of-secrets-rules)  

security_monitoring_filters_read
Read Security Filters.
[List resource filters](https://docs.datadoghq.com/api/latest/security-monitoring/#list-resource-filters)  
[Get all security filters](https://docs.datadoghq.com/api/latest/security-monitoring/#get-all-security-filters)  
[Get a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-security-filter)  

security_monitoring_filters_write
Create, edit, and delete Security Filters.
[Update resource filters](https://docs.datadoghq.com/api/latest/security-monitoring/#update-resource-filters)  
[Create a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-security-filter)  
[Delete a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-security-filter)  
[Update a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-security-filter)  

security_monitoring_rules_read
Read Detection Rules.
[Create a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-custom-framework)  
[Delete a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-custom-framework)  
[Get a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-custom-framework)  
[Update a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-custom-framework)  
[List rules](https://docs.datadoghq.com/api/latest/security-monitoring/#list-rules)  
[Get a rule's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-rules-details)  
[Convert an existing rule from JSON to Terraform](https://docs.datadoghq.com/api/latest/security-monitoring/#convert-an-existing-rule-from-json-to-terraform)  
[Get a job's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-jobs-details)  

security_monitoring_rules_write
Create and edit Detection Rules.
[Create a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-custom-framework)  
[Delete a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-custom-framework)  
[Update a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-custom-framework)  
[Create a detection rule](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-detection-rule)  
[Convert a rule from JSON to Terraform](https://docs.datadoghq.com/api/latest/security-monitoring/#convert-a-rule-from-json-to-terraform)  
[Test a rule](https://docs.datadoghq.com/api/latest/security-monitoring/#test-a-rule)  
[Validate a detection rule](https://docs.datadoghq.com/api/latest/security-monitoring/#validate-a-detection-rule)  
[Delete an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-an-existing-rule)  
[Update an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#update-an-existing-rule)  
[Test an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#test-an-existing-rule)  
[Run a threat hunting job](https://docs.datadoghq.com/api/latest/security-monitoring/#run-a-threat-hunting-job)  
[Cancel a threat hunting job](https://docs.datadoghq.com/api/latest/security-monitoring/#cancel-a-threat-hunting-job)  

security_monitoring_signals_read
View Security Signals.
[Get a quick list of security signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-quick-list-of-security-signals)  
[Get a list of security signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-list-of-security-signals)  
[Get a signal's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-signals-details)  
[List hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#list-hist-signals)  
[Search hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#search-hist-signals)  
[Get a hist signal's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-hist-signals-details)  
[Get a job's hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-jobs-hist-signals)  

security_monitoring_suppressions_read
Read Rule Suppressions.
[Get all suppression rules](https://docs.datadoghq.com/api/latest/security-monitoring/#get-all-suppression-rules)  
[Get suppressions affecting future rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-suppressions-affecting-future-rule)  
[Get suppressions affecting a specific rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-suppressions-affecting-a-specific-rule)  
[Get a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-suppression-rule)  
[Get a suppression's version history](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-suppressions-version-history)  

security_monitoring_suppressions_write
Write Rule Suppressions.
[Create a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-suppression-rule)  
[Validate a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#validate-a-suppression-rule)  
[Delete a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-suppression-rule)  
[Update a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-suppression-rule)  

#### Agentless Scanning, Domain Allowlist, IP Allowlist, Security Monitoring, Static Analysis
Scope name
Description
Endpoints that require this scope
org_management
Edit org configurations, including authentication and certain security preferences such as configuring SAML, renaming an org, configuring allowed login methods, creating child orgs, subscribing & unsubscribing from apps in the marketplace, and enabling & disabling Remote Configuration for the entire organization.
[Create AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-scan-options)  
[Delete AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-aws-scan-options)  
[Update AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-aws-scan-options)  
[Create Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-azure-scan-options)  
[Delete Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-azure-scan-options)  
[Update Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-azure-scan-options)  
[Create GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-gcp-scan-options)  
[Delete GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-gcp-scan-options)  
[Update GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-gcp-scan-options)  
[Create AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  
[Get IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#get-ip-allowlist)  
[Update IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#update-ip-allowlist)  

security_monitoring_findings_read
View a list of findings that include both misconfigurations and identity risks.
[List AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-scan-options)  
[Get AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-scan-options)  
[List Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-azure-scan-options)  
[Get Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-azure-scan-options)  
[List GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-gcp-scan-options)  
[Get GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-gcp-scan-options)  
[List AWS on demand tasks](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-on-demand-tasks)  
[Get AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-on-demand-task)  
[List findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-findings)  
[Get a finding](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-finding)  
[List security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-security-findings)  
[Search security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#search-security-findings)  

monitors_write
Edit, delete, and resolve individual monitors.
[Create a monitor](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor)  
[Delete a monitor](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor)  
[Edit a monitor](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor)  
[Mute a monitor](https://docs.datadoghq.com/api/latest/monitors/#mute-a-monitor)  
[Unmute a monitor](https://docs.datadoghq.com/api/latest/monitors/#unmute-a-monitor)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  

code_analysis_read
View Code Analysis.
[Post dependencies for analysis](https://docs.datadoghq.com/api/latest/static-analysis/#post-dependencies-for-analysis)  
[POST request to resolve vulnerable symbols](https://docs.datadoghq.com/api/latest/static-analysis/#post-request-to-resolve-vulnerable-symbols)  
[Ruleset get multiple](https://docs.datadoghq.com/api/latest/security-monitoring/#ruleset-get-multiple)  
[Returns a list of Secrets rules](https://docs.datadoghq.com/api/latest/security-monitoring/#returns-a-list-of-secrets-rules)  

security_monitoring_filters_read
Read Security Filters.
[List resource filters](https://docs.datadoghq.com/api/latest/security-monitoring/#list-resource-filters)  
[Get all security filters](https://docs.datadoghq.com/api/latest/security-monitoring/#get-all-security-filters)  
[Get a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-security-filter)  

security_monitoring_filters_write
Create, edit, and delete Security Filters.
[Update resource filters](https://docs.datadoghq.com/api/latest/security-monitoring/#update-resource-filters)  
[Create a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-security-filter)  
[Delete a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-security-filter)  
[Update a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-security-filter)  

security_monitoring_rules_read
Read Detection Rules.
[Create a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-custom-framework)  
[Delete a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-custom-framework)  
[Get a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-custom-framework)  
[Update a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-custom-framework)  
[List rules](https://docs.datadoghq.com/api/latest/security-monitoring/#list-rules)  
[Get a rule's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-rules-details)  
[Convert an existing rule from JSON to Terraform](https://docs.datadoghq.com/api/latest/security-monitoring/#convert-an-existing-rule-from-json-to-terraform)  
[Get a job's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-jobs-details)  

security_monitoring_rules_write
Create and edit Detection Rules.
[Create a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-custom-framework)  
[Delete a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-custom-framework)  
[Update a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-custom-framework)  
[Create a detection rule](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-detection-rule)  
[Convert a rule from JSON to Terraform](https://docs.datadoghq.com/api/latest/security-monitoring/#convert-a-rule-from-json-to-terraform)  
[Test a rule](https://docs.datadoghq.com/api/latest/security-monitoring/#test-a-rule)  
[Validate a detection rule](https://docs.datadoghq.com/api/latest/security-monitoring/#validate-a-detection-rule)  
[Delete an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-an-existing-rule)  
[Update an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#update-an-existing-rule)  
[Test an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#test-an-existing-rule)  
[Run a threat hunting job](https://docs.datadoghq.com/api/latest/security-monitoring/#run-a-threat-hunting-job)  
[Cancel a threat hunting job](https://docs.datadoghq.com/api/latest/security-monitoring/#cancel-a-threat-hunting-job)  

security_monitoring_signals_read
View Security Signals.
[Get a quick list of security signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-quick-list-of-security-signals)  
[Get a list of security signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-list-of-security-signals)  
[Get a signal's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-signals-details)  
[List hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#list-hist-signals)  
[Search hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#search-hist-signals)  
[Get a hist signal's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-hist-signals-details)  
[Get a job's hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-jobs-hist-signals)  

security_monitoring_suppressions_read
Read Rule Suppressions.
[Get all suppression rules](https://docs.datadoghq.com/api/latest/security-monitoring/#get-all-suppression-rules)  
[Get suppressions affecting future rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-suppressions-affecting-future-rule)  
[Get suppressions affecting a specific rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-suppressions-affecting-a-specific-rule)  
[Get a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-suppression-rule)  
[Get a suppression's version history](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-suppressions-version-history)  

security_monitoring_suppressions_write
Write Rule Suppressions.
[Create a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-suppression-rule)  
[Validate a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#validate-a-suppression-rule)  
[Delete a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-suppression-rule)  
[Update a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-suppression-rule)  

#### Agentless Scanning, Security Monitoring, Static Analysis
Scope name
Description
Endpoints that require this scope
org_management
Edit org configurations, including authentication and certain security preferences such as configuring SAML, renaming an org, configuring allowed login methods, creating child orgs, subscribing & unsubscribing from apps in the marketplace, and enabling & disabling Remote Configuration for the entire organization.
[Create AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-scan-options)  
[Delete AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-aws-scan-options)  
[Update AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-aws-scan-options)  
[Create Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-azure-scan-options)  
[Delete Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-azure-scan-options)  
[Update Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-azure-scan-options)  
[Create GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-gcp-scan-options)  
[Delete GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-gcp-scan-options)  
[Update GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-gcp-scan-options)  
[Create AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  
[Get IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#get-ip-allowlist)  
[Update IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#update-ip-allowlist)  

security_monitoring_findings_read
View a list of findings that include both misconfigurations and identity risks.
[List AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-scan-options)  
[Get AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-scan-options)  
[List Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-azure-scan-options)  
[Get Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-azure-scan-options)  
[List GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-gcp-scan-options)  
[Get GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-gcp-scan-options)  
[List AWS on demand tasks](https://docs.datadoghq.com/api/latest/agentless-scanning/#list-aws-on-demand-tasks)  
[Get AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#get-aws-on-demand-task)  
[List findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-findings)  
[Get a finding](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-finding)  
[List security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#list-security-findings)  
[Search security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#search-security-findings)  

code_analysis_read
View Code Analysis.
[Post dependencies for analysis](https://docs.datadoghq.com/api/latest/static-analysis/#post-dependencies-for-analysis)  
[POST request to resolve vulnerable symbols](https://docs.datadoghq.com/api/latest/static-analysis/#post-request-to-resolve-vulnerable-symbols)  
[Ruleset get multiple](https://docs.datadoghq.com/api/latest/security-monitoring/#ruleset-get-multiple)  
[Returns a list of Secrets rules](https://docs.datadoghq.com/api/latest/security-monitoring/#returns-a-list-of-secrets-rules)  

security_monitoring_filters_read
Read Security Filters.
[List resource filters](https://docs.datadoghq.com/api/latest/security-monitoring/#list-resource-filters)  
[Get all security filters](https://docs.datadoghq.com/api/latest/security-monitoring/#get-all-security-filters)  
[Get a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-security-filter)  

security_monitoring_filters_write
Create, edit, and delete Security Filters.
[Update resource filters](https://docs.datadoghq.com/api/latest/security-monitoring/#update-resource-filters)  
[Create a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-security-filter)  
[Delete a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-security-filter)  
[Update a security filter](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-security-filter)  

security_monitoring_rules_read
Read Detection Rules.
[Create a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-custom-framework)  
[Delete a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-custom-framework)  
[Get a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-custom-framework)  
[Update a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-custom-framework)  
[List rules](https://docs.datadoghq.com/api/latest/security-monitoring/#list-rules)  
[Get a rule's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-rules-details)  
[Convert an existing rule from JSON to Terraform](https://docs.datadoghq.com/api/latest/security-monitoring/#convert-an-existing-rule-from-json-to-terraform)  
[Get a job's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-jobs-details)  

security_monitoring_rules_write
Create and edit Detection Rules.
[Create a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-custom-framework)  
[Delete a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-custom-framework)  
[Update a custom framework](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-custom-framework)  
[Create a detection rule](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-detection-rule)  
[Convert a rule from JSON to Terraform](https://docs.datadoghq.com/api/latest/security-monitoring/#convert-a-rule-from-json-to-terraform)  
[Test a rule](https://docs.datadoghq.com/api/latest/security-monitoring/#test-a-rule)  
[Validate a detection rule](https://docs.datadoghq.com/api/latest/security-monitoring/#validate-a-detection-rule)  
[Delete an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-an-existing-rule)  
[Update an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#update-an-existing-rule)  
[Test an existing rule](https://docs.datadoghq.com/api/latest/security-monitoring/#test-an-existing-rule)  
[Run a threat hunting job](https://docs.datadoghq.com/api/latest/security-monitoring/#run-a-threat-hunting-job)  
[Cancel a threat hunting job](https://docs.datadoghq.com/api/latest/security-monitoring/#cancel-a-threat-hunting-job)  

security_monitoring_signals_read
View Security Signals.
[Get a quick list of security signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-quick-list-of-security-signals)  
[Get a list of security signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-list-of-security-signals)  
[Get a signal's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-signals-details)  
[List hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#list-hist-signals)  
[Search hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#search-hist-signals)  
[Get a hist signal's details](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-hist-signals-details)  
[Get a job's hist signals](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-jobs-hist-signals)  

security_monitoring_suppressions_read
Read Rule Suppressions.
[Get all suppression rules](https://docs.datadoghq.com/api/latest/security-monitoring/#get-all-suppression-rules)  
[Get suppressions affecting future rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-suppressions-affecting-future-rule)  
[Get suppressions affecting a specific rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-suppressions-affecting-a-specific-rule)  
[Get a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-suppression-rule)  
[Get a suppression's version history](https://docs.datadoghq.com/api/latest/security-monitoring/#get-a-suppressions-version-history)  

security_monitoring_suppressions_write
Write Rule Suppressions.
[Create a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#create-a-suppression-rule)  
[Validate a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#validate-a-suppression-rule)  
[Delete a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#delete-a-suppression-rule)  
[Update a suppression rule](https://docs.datadoghq.com/api/latest/security-monitoring/#update-a-suppression-rule)  

#### CI Visibility Pipelines, CI Visibility Tests, Test Optimization
Scope name
Description
Endpoints that require this scope
ci_visibility_read
View CI Visibility.
[Aggregate pipelines events](https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/#aggregate-pipelines-events)  
[Get a list of pipelines events](https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/#get-a-list-of-pipelines-events)  
[Search pipelines events](https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/#search-pipelines-events)  
[Aggregate tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#aggregate-tests-events)  
[Get a list of tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#get-a-list-of-tests-events)  
[Search tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#search-tests-events)  

test_optimization_read
View Test Optimization.
[Aggregate tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#aggregate-tests-events)  
[Get a list of tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#get-a-list-of-tests-events)  
[Search tests events](https://docs.datadoghq.com/api/latest/ci-visibility-tests/#search-tests-events)  
[Search flaky tests](https://docs.datadoghq.com/api/latest/test-optimization/#search-flaky-tests)  

#### Case Management, Error Tracking
Scope name
Description
Endpoints that require this scope
cases_read
View Cases.
[Search cases](https://docs.datadoghq.com/api/latest/case-management/#search-cases)  
[Get all projects](https://docs.datadoghq.com/api/latest/case-management/#get-all-projects)  
[Get the details of a project](https://docs.datadoghq.com/api/latest/case-management/#get-the-details-of-a-project)  
[Get the details of a case](https://docs.datadoghq.com/api/latest/case-management/#get-the-details-of-a-case)  
[Remove the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#remove-the-assignee-of-an-issue)  
[Update the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-assignee-of-an-issue)  

cases_write
Create and update cases.
[Create a case](https://docs.datadoghq.com/api/latest/case-management/#create-a-case)  
[Create a project](https://docs.datadoghq.com/api/latest/case-management/#create-a-project)  
[Remove a project](https://docs.datadoghq.com/api/latest/case-management/#remove-a-project)  
[Archive case](https://docs.datadoghq.com/api/latest/case-management/#archive-case)  
[Assign case](https://docs.datadoghq.com/api/latest/case-management/#assign-case)  
[Update case attributes](https://docs.datadoghq.com/api/latest/case-management/#update-case-attributes)  
[Delete custom attribute from case](https://docs.datadoghq.com/api/latest/case-management/#delete-custom-attribute-from-case)  
[Update case custom attribute](https://docs.datadoghq.com/api/latest/case-management/#update-case-custom-attribute)  
[Update case description](https://docs.datadoghq.com/api/latest/case-management/#update-case-description)  
[Update case priority](https://docs.datadoghq.com/api/latest/case-management/#update-case-priority)  
[Update case status](https://docs.datadoghq.com/api/latest/case-management/#update-case-status)  
[Update case title](https://docs.datadoghq.com/api/latest/case-management/#update-case-title)  
[Unarchive case](https://docs.datadoghq.com/api/latest/case-management/#unarchive-case)  
[Unassign case](https://docs.datadoghq.com/api/latest/case-management/#unassign-case)  
[Remove the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#remove-the-assignee-of-an-issue)  
[Update the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-assignee-of-an-issue)  

error_tracking_read
Read Error Tracking data.
[Search error tracking issues](https://docs.datadoghq.com/api/latest/error-tracking/#search-error-tracking-issues)  
[Get the details of an error tracking issue](https://docs.datadoghq.com/api/latest/error-tracking/#get-the-details-of-an-error-tracking-issue)  
[Remove the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#remove-the-assignee-of-an-issue)  
[Update the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-assignee-of-an-issue)  
[Update the state of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-state-of-an-issue)  

error_tracking_write
Edit Error Tracking issues.
[Remove the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#remove-the-assignee-of-an-issue)  
[Update the assignee of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-assignee-of-an-issue)  
[Update the state of an issue](https://docs.datadoghq.com/api/latest/error-tracking/#update-the-state-of-an-issue)  

#### Cloud Cost Management
Scope name
Description
Endpoints that require this scope
cloud_cost_management_read
View Cloud Cost pages and the cloud cost data source in dashboards and notebooks. For more details, see the Cloud Cost Management docs.
[List custom allocation rules](https://docs.datadoghq.com/api/latest/cloud-cost-management/#list-custom-allocation-rules)  
[Get custom allocation rule](https://docs.datadoghq.com/api/latest/cloud-cost-management/#get-custom-allocation-rule)  
[List Cloud Cost Management AWS CUR configs](https://docs.datadoghq.com/api/latest/cloud-cost-management/#list-cloud-cost-management-aws-cur-configs)  
[Get cost AWS CUR config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#get-cost-aws-cur-config)  
[List Cloud Cost Management Azure configs](https://docs.datadoghq.com/api/latest/cloud-cost-management/#list-cloud-cost-management-azure-configs)  
[Get cost Azure UC config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#get-cost-azure-uc-config)  
[Get a budget](https://docs.datadoghq.com/api/latest/cloud-cost-management/#get-a-budget)  
[List budgets](https://docs.datadoghq.com/api/latest/cloud-cost-management/#list-budgets)  
[List Custom Costs files](https://docs.datadoghq.com/api/latest/cloud-cost-management/#list-custom-costs-files)  
[Get Custom Costs file](https://docs.datadoghq.com/api/latest/cloud-cost-management/#get-custom-costs-file)  
[List Google Cloud Usage Cost configs](https://docs.datadoghq.com/api/latest/cloud-cost-management/#list-google-cloud-usage-cost-configs)  
[Get Google Cloud Usage Cost config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#get-google-cloud-usage-cost-config)  
[List tag pipeline rulesets](https://docs.datadoghq.com/api/latest/cloud-cost-management/#list-tag-pipeline-rulesets)  
[Validate query](https://docs.datadoghq.com/api/latest/cloud-cost-management/#validate-query)  
[Get a tag pipeline ruleset](https://docs.datadoghq.com/api/latest/cloud-cost-management/#get-a-tag-pipeline-ruleset)  

cloud_cost_management_write
Configure cloud cost accounts and global customizations. For more details, see the Cloud Cost Management docs.
[Create custom allocation rule](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-custom-allocation-rule)  
[Reorder custom allocation rules](https://docs.datadoghq.com/api/latest/cloud-cost-management/#reorder-custom-allocation-rules)  
[Delete custom allocation rule](https://docs.datadoghq.com/api/latest/cloud-cost-management/#delete-custom-allocation-rule)  
[Update custom allocation rule](https://docs.datadoghq.com/api/latest/cloud-cost-management/#update-custom-allocation-rule)  
[Create Cloud Cost Management AWS CUR config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-cloud-cost-management-aws-cur-config)  
[Delete Cloud Cost Management AWS CUR config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#delete-cloud-cost-management-aws-cur-config)  
[Update Cloud Cost Management AWS CUR config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#update-cloud-cost-management-aws-cur-config)  
[Create Cloud Cost Management Azure configs](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-cloud-cost-management-azure-configs)  
[Delete Cloud Cost Management Azure config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#delete-cloud-cost-management-azure-config)  
[Update Cloud Cost Management Azure config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#update-cloud-cost-management-azure-config)  
[Create or update a budget](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-or-update-a-budget)  
[Delete a budget](https://docs.datadoghq.com/api/latest/cloud-cost-management/#delete-a-budget)  
[Upload Custom Costs file](https://docs.datadoghq.com/api/latest/cloud-cost-management/#upload-custom-costs-file)  
[Delete Custom Costs file](https://docs.datadoghq.com/api/latest/cloud-cost-management/#delete-custom-costs-file)  
[Create Google Cloud Usage Cost config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-google-cloud-usage-cost-config)  
[Delete Google Cloud Usage Cost config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#delete-google-cloud-usage-cost-config)  
[Update Google Cloud Usage Cost config](https://docs.datadoghq.com/api/latest/cloud-cost-management/#update-google-cloud-usage-cost-config)  
[Create tag pipeline ruleset](https://docs.datadoghq.com/api/latest/cloud-cost-management/#create-tag-pipeline-ruleset)  
[Reorder tag pipeline rulesets](https://docs.datadoghq.com/api/latest/cloud-cost-management/#reorder-tag-pipeline-rulesets)  
[Delete tag pipeline ruleset](https://docs.datadoghq.com/api/latest/cloud-cost-management/#delete-tag-pipeline-ruleset)  
[Update tag pipeline ruleset](https://docs.datadoghq.com/api/latest/cloud-cost-management/#update-tag-pipeline-ruleset)  

#### Dashboard Lists, Dashboards, Powerpack
Scope name
Description
Endpoints that require this scope
dashboards_read
View dashboards.
[Get all dashboards](https://docs.datadoghq.com/api/latest/dashboards/#get-all-dashboards)  
[Get all dashboard lists](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-all-dashboard-lists)  
[Get a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-a-dashboard-list)  
[Get a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#get-a-shared-dashboard)  
[Get a dashboard](https://docs.datadoghq.com/api/latest/dashboards/#get-a-dashboard)  
[Get items of a Dashboard List](https://docs.datadoghq.com/api/latest/dashboard-lists/#get-items-of-a-dashboard-list)  
[Get all powerpacks](https://docs.datadoghq.com/api/latest/powerpack/#get-all-powerpacks)  
[Get a Powerpack](https://docs.datadoghq.com/api/latest/powerpack/#get-a-powerpack)  

dashboards_write
Create and change dashboards.
[Delete dashboards](https://docs.datadoghq.com/api/latest/dashboards/#delete-dashboards)  
[Restore deleted dashboards](https://docs.datadoghq.com/api/latest/dashboards/#restore-deleted-dashboards)  
[Create a new dashboard](https://docs.datadoghq.com/api/latest/dashboards/#create-a-new-dashboard)  
[Create a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#create-a-dashboard-list)  
[Delete a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#delete-a-dashboard-list)  
[Update a dashboard list](https://docs.datadoghq.com/api/latest/dashboard-lists/#update-a-dashboard-list)  
[Delete a dashboard](https://docs.datadoghq.com/api/latest/dashboards/#delete-a-dashboard)  
[Update a dashboard](https://docs.datadoghq.com/api/latest/dashboards/#update-a-dashboard)  
[Create a new powerpack](https://docs.datadoghq.com/api/latest/powerpack/#create-a-new-powerpack)  
[Delete a powerpack](https://docs.datadoghq.com/api/latest/powerpack/#delete-a-powerpack)  
[Update a powerpack](https://docs.datadoghq.com/api/latest/powerpack/#update-a-powerpack)  

dashboards_embed_share
Create, modify, and delete shared dashboards with share type 'embed'.
[Create a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#create-a-shared-dashboard)  
[Revoke a shared dashboard URL](https://docs.datadoghq.com/api/latest/dashboards/#revoke-a-shared-dashboard-url)  
[Update a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#update-a-shared-dashboard)  

dashboards_invite_share
Create, modify, and delete shared dashboards with share type 'invite'.
[Create a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#create-a-shared-dashboard)  
[Revoke a shared dashboard URL](https://docs.datadoghq.com/api/latest/dashboards/#revoke-a-shared-dashboard-url)  
[Update a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#update-a-shared-dashboard)  
[Revoke shared dashboard invitations](https://docs.datadoghq.com/api/latest/dashboards/#revoke-shared-dashboard-invitations)  
[Get all invitations for a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#get-all-invitations-for-a-shared-dashboard)  
[Send shared dashboard invitation email](https://docs.datadoghq.com/api/latest/dashboards/#send-shared-dashboard-invitation-email)  

dashboards_public_share
Generate public and authenticated links to share dashboards or embeddable graphs externally.
[Create a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#create-a-shared-dashboard)  
[Revoke a shared dashboard URL](https://docs.datadoghq.com/api/latest/dashboards/#revoke-a-shared-dashboard-url)  
[Update a shared dashboard](https://docs.datadoghq.com/api/latest/dashboards/#update-a-shared-dashboard)  

#### Datasets, Roles, Users
Scope name
Description
Endpoints that require this scope
user_access_manage
Disable users, manage user roles, manage SAML-to-role mappings, and configure logs restriction queries.
[Create a dataset](https://docs.datadoghq.com/api/latest/datasets/#create-a-dataset)  
[Delete a dataset](https://docs.datadoghq.com/api/latest/datasets/#delete-a-dataset)  
[Edit a dataset](https://docs.datadoghq.com/api/latest/datasets/#edit-a-dataset)  
[Create role](https://docs.datadoghq.com/api/latest/roles/#create-role)  
[Delete role](https://docs.datadoghq.com/api/latest/roles/#delete-role)  
[Update a role](https://docs.datadoghq.com/api/latest/roles/#update-a-role)  
[Create a new role by cloning an existing role](https://docs.datadoghq.com/api/latest/roles/#create-a-new-role-by-cloning-an-existing-role)  
[Revoke permission](https://docs.datadoghq.com/api/latest/roles/#revoke-permission)  
[Grant permission to a role](https://docs.datadoghq.com/api/latest/roles/#grant-permission-to-a-role)  
[Remove a user from a role](https://docs.datadoghq.com/api/latest/roles/#remove-a-user-from-a-role)  
[Add a user to a role](https://docs.datadoghq.com/api/latest/roles/#add-a-user-to-a-role)  
[Disable a user](https://docs.datadoghq.com/api/latest/users/#disable-a-user)  
[Update a user](https://docs.datadoghq.com/api/latest/users/#update-a-user)  

user_access_read
View users and their roles and settings.
[List all users](https://docs.datadoghq.com/api/latest/users/#list-all-users)  
[Get all datasets](https://docs.datadoghq.com/api/latest/datasets/#get-all-datasets)  
[Get a single dataset by ID](https://docs.datadoghq.com/api/latest/datasets/#get-a-single-dataset-by-id)  
[List permissions](https://docs.datadoghq.com/api/latest/roles/#list-permissions)  
[List roles](https://docs.datadoghq.com/api/latest/roles/#list-roles)  
[List role templates](https://docs.datadoghq.com/api/latest/roles/#list-role-templates)  
[Get a role](https://docs.datadoghq.com/api/latest/roles/#get-a-role)  
[List permissions for a role](https://docs.datadoghq.com/api/latest/roles/#list-permissions-for-a-role)  
[Get all users of a role](https://docs.datadoghq.com/api/latest/roles/#get-all-users-of-a-role)  
[List all users](https://docs.datadoghq.com/api/latest/users/#list-all-users)  
[Get user details](https://docs.datadoghq.com/api/latest/users/#get-user-details)  
[Get a user permissions](https://docs.datadoghq.com/api/latest/users/#get-a-user-permissions)  

user_access_invite
Invite other users to your organization.
[Send invitation emails](https://docs.datadoghq.com/api/latest/users/#send-invitation-emails)  
[Get a user invitation](https://docs.datadoghq.com/api/latest/users/#get-a-user-invitation)  
[Create a user](https://docs.datadoghq.com/api/latest/users/#create-a-user)  

#### Domain Allowlist, Downtimes, Monitors
Scope name
Description
Endpoints that require this scope
monitors_write
Edit, delete, and resolve individual monitors.
[Create a monitor](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor)  
[Delete a monitor](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor)  
[Edit a monitor](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor)  
[Mute a monitor](https://docs.datadoghq.com/api/latest/monitors/#mute-a-monitor)  
[Unmute a monitor](https://docs.datadoghq.com/api/latest/monitors/#unmute-a-monitor)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  

org_management
Edit org configurations, including authentication and certain security preferences such as configuring SAML, renaming an org, configuring allowed login methods, creating child orgs, subscribing & unsubscribing from apps in the marketplace, and enabling & disabling Remote Configuration for the entire organization.
[Create AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-scan-options)  
[Delete AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-aws-scan-options)  
[Update AWS scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-aws-scan-options)  
[Create Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-azure-scan-options)  
[Delete Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-azure-scan-options)  
[Update Azure scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-azure-scan-options)  
[Create GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-gcp-scan-options)  
[Delete GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#delete-gcp-scan-options)  
[Update GCP scan options](https://docs.datadoghq.com/api/latest/agentless-scanning/#update-gcp-scan-options)  
[Create AWS on demand task](https://docs.datadoghq.com/api/latest/agentless-scanning/#create-aws-on-demand-task)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  
[Get IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#get-ip-allowlist)  
[Update IP Allowlist](https://docs.datadoghq.com/api/latest/ip-allowlist/#update-ip-allowlist)  

monitors_downtime
Set downtimes to suppress alerts from any monitor in an organization. Mute and unmute monitors. The ability to write monitors is not required to set downtimes.
[Schedule a downtime](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime)  
[Cancel downtimes by scope](https://docs.datadoghq.com/api/latest/downtimes/#cancel-downtimes-by-scope)  
[Cancel a downtime](https://docs.datadoghq.com/api/latest/downtimes/#cancel-a-downtime)  
[Update a downtime](https://docs.datadoghq.com/api/latest/downtimes/#update-a-downtime)  
[Get all downtimes](https://docs.datadoghq.com/api/latest/downtimes/#get-all-downtimes)  
[Schedule a downtime](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime)  
[Cancel a downtime](https://docs.datadoghq.com/api/latest/downtimes/#cancel-a-downtime)  
[Get a downtime](https://docs.datadoghq.com/api/latest/downtimes/#get-a-downtime)  
[Update a downtime](https://docs.datadoghq.com/api/latest/downtimes/#update-a-downtime)  
[Get active downtimes for a monitor](https://docs.datadoghq.com/api/latest/downtimes/#get-active-downtimes-for-a-monitor)  

monitors_read
View monitors.
[Get all downtimes](https://docs.datadoghq.com/api/latest/downtimes/#get-all-downtimes)  
[Get a downtime](https://docs.datadoghq.com/api/latest/downtimes/#get-a-downtime)  
[Get all monitors](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitors)  
[Check if a monitor can be deleted](https://docs.datadoghq.com/api/latest/monitors/#check-if-a-monitor-can-be-deleted)  
[Monitors group search](https://docs.datadoghq.com/api/latest/monitors/#monitors-group-search)  
[Monitors search](https://docs.datadoghq.com/api/latest/monitors/#monitors-search)  
[Validate a monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor)  
[Get a monitor's details](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitors-details)  
[Get active downtimes for a monitor](https://docs.datadoghq.com/api/latest/downtimes/#get-active-downtimes-for-a-monitor)  
[Validate an existing monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor)  
[Get all monitor notification rules](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-notification-rules)  
[Get a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-notification-rule)  
[Get all monitor configuration policies](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-configuration-policies)  
[Get a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-configuration-policy)  
[Get all monitor user templates](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-user-templates)  
[Get a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-user-template)  

#### Downtimes, Monitors
Scope name
Description
Endpoints that require this scope
monitors_downtime
Set downtimes to suppress alerts from any monitor in an organization. Mute and unmute monitors. The ability to write monitors is not required to set downtimes.
[Schedule a downtime](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime)  
[Cancel downtimes by scope](https://docs.datadoghq.com/api/latest/downtimes/#cancel-downtimes-by-scope)  
[Cancel a downtime](https://docs.datadoghq.com/api/latest/downtimes/#cancel-a-downtime)  
[Update a downtime](https://docs.datadoghq.com/api/latest/downtimes/#update-a-downtime)  
[Get all downtimes](https://docs.datadoghq.com/api/latest/downtimes/#get-all-downtimes)  
[Schedule a downtime](https://docs.datadoghq.com/api/latest/downtimes/#schedule-a-downtime)  
[Cancel a downtime](https://docs.datadoghq.com/api/latest/downtimes/#cancel-a-downtime)  
[Get a downtime](https://docs.datadoghq.com/api/latest/downtimes/#get-a-downtime)  
[Update a downtime](https://docs.datadoghq.com/api/latest/downtimes/#update-a-downtime)  
[Get active downtimes for a monitor](https://docs.datadoghq.com/api/latest/downtimes/#get-active-downtimes-for-a-monitor)  

monitors_read
View monitors.
[Get all downtimes](https://docs.datadoghq.com/api/latest/downtimes/#get-all-downtimes)  
[Get a downtime](https://docs.datadoghq.com/api/latest/downtimes/#get-a-downtime)  
[Get all monitors](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitors)  
[Check if a monitor can be deleted](https://docs.datadoghq.com/api/latest/monitors/#check-if-a-monitor-can-be-deleted)  
[Monitors group search](https://docs.datadoghq.com/api/latest/monitors/#monitors-group-search)  
[Monitors search](https://docs.datadoghq.com/api/latest/monitors/#monitors-search)  
[Validate a monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-a-monitor)  
[Get a monitor's details](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitors-details)  
[Get active downtimes for a monitor](https://docs.datadoghq.com/api/latest/downtimes/#get-active-downtimes-for-a-monitor)  
[Validate an existing monitor](https://docs.datadoghq.com/api/latest/monitors/#validate-an-existing-monitor)  
[Get all monitor notification rules](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-notification-rules)  
[Get a monitor notification rule](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-notification-rule)  
[Get all monitor configuration policies](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-configuration-policies)  
[Get a monitor configuration policy](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-configuration-policy)  
[Get all monitor user templates](https://docs.datadoghq.com/api/latest/monitors/#get-all-monitor-user-templates)  
[Get a monitor user template](https://docs.datadoghq.com/api/latest/monitors/#get-a-monitor-user-template)  

monitors_write
Edit, delete, and resolve individual monitors.
[Create a monitor](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor)  
[Delete a monitor](https://docs.datadoghq.com/api/latest/monitors/#delete-a-monitor)  
[Edit a monitor](https://docs.datadoghq.com/api/latest/monitors/#edit-a-monitor)  
[Mute a monitor](https://docs.datadoghq.com/api/latest/monitors/#mute-a-monitor)  
[Unmute a monitor](https://docs.datadoghq.com/api/latest/monitors/#unmute-a-monitor)  
[Get Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#get-domain-allowlist)  
[Sets Domain Allowlist](https://docs.datadoghq.com/api/latest/domain-allowlist/#sets-domain-allowlist)  

#### Events
Scope name
Description
Endpoints that require this scope
events_read
Read Events data.
[Get a list of events](https://docs.datadoghq.com/api/latest/events/#get-a-list-of-events)  
[Get an event](https://docs.datadoghq.com/api/latest/events/#get-an-event)  
[Get a list of events](https://docs.datadoghq.com/api/latest/events/#get-a-list-of-events)  
[Get an event](https://docs.datadoghq.com/api/latest/events/#get-an-event)  

#### Hosts
Scope name
Description
Endpoints that require this scope
hosts_read
List hosts and their attributes.
[Get all hosts for your organization](https://docs.datadoghq.com/api/latest/hosts/#get-all-hosts-for-your-organization)  
[Get the total number of active hosts](https://docs.datadoghq.com/api/latest/hosts/#get-the-total-number-of-active-hosts)  

#### Incident Services, Incident Teams, Incidents
Scope name
Description
Endpoints that require this scope
incident_read
View incidents in Datadog.
[Get a list of incidents](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-incidents)  
[Get incident notification template](https://docs.datadoghq.com/api/latest/incidents/#get-incident-notification-template)  
[Get a list of incident types](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-incident-types)  
[Get incident type details](https://docs.datadoghq.com/api/latest/incidents/#get-incident-type-details)  
[Search for incidents](https://docs.datadoghq.com/api/latest/incidents/#search-for-incidents)  
[Get the details of an incident](https://docs.datadoghq.com/api/latest/incidents/#get-the-details-of-an-incident)  
[List an incident's impacts](https://docs.datadoghq.com/api/latest/incidents/#list-an-incidents-impacts)  
[Get a list of an incident's integration metadata](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-an-incidents-integration-metadata)  
[Get incident integration metadata details](https://docs.datadoghq.com/api/latest/incidents/#get-incident-integration-metadata-details)  
[Get a list of an incident's todos](https://docs.datadoghq.com/api/latest/incidents/#get-a-list-of-an-incidents-todos)  
[Get incident todo details](https://docs.datadoghq.com/api/latest/incidents/#get-incident-todo-details)  
[Get a list of all incident services](https://docs.datadoghq.com/api/latest/incident-services/#get-a-list-of-all-incident-services)  
[Get details of an incident service](https://docs.datadoghq.com/api/latest/incident-services/#get-details-of-an-incident-service)  
[Get a list of all incident teams](https://docs.datadoghq.com/api/latest/incident-teams/#get-a-list-of-all-incident-teams)  
[Get details of an incident team](https://docs.datadoghq.com/api/latest/incident-teams/#get-details-of-an-incident-team)  

incident_settings_write
Configure Incident Settings.
[Create an incident type](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-type)  
[Delete an incident type](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-type)  
[Update an incident type](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-type)  
[Create a new incident service](https://docs.datadoghq.com/api/latest/incident-services/#create-a-new-incident-service)  
[Delete an existing incident service](https://docs.datadoghq.com/api/latest/incident-services/#delete-an-existing-incident-service)  
[Update an existing incident service](https://docs.datadoghq.com/api/latest/incident-services/#update-an-existing-incident-service)  
[Create a new incident team](https://docs.datadoghq.com/api/latest/incident-teams/#create-a-new-incident-team)  
[Delete an existing incident team](https://docs.datadoghq.com/api/latest/incident-teams/#delete-an-existing-incident-team)  
[Update an existing incident team](https://docs.datadoghq.com/api/latest/incident-teams/#update-an-existing-incident-team)  

incident_notification_settings_read
View Incident Notification Rule Settings.
[Get an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#get-an-incident-notification-rule)  

incident_notification_settings_write
Configure Incidents Notification Rule settings.
[Create an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-notification-rule)  
[Delete an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-notification-rule)  
[Update an incident notification rule](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-notification-rule)  
[Create incident notification template](https://docs.datadoghq.com/api/latest/incidents/#create-incident-notification-template)  
[Delete a notification template](https://docs.datadoghq.com/api/latest/incidents/#delete-a-notification-template)  
[Update incident notification template](https://docs.datadoghq.com/api/latest/incidents/#update-incident-notification-template)  

incident_write
Create, view, and manage incidents in Datadog.
[Create an incident](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident)  
[Get incident notification template](https://docs.datadoghq.com/api/latest/incidents/#get-incident-notification-template)  
[Delete an existing incident](https://docs.datadoghq.com/api/latest/incidents/#delete-an-existing-incident)  
[Update an existing incident](https://docs.datadoghq.com/api/latest/incidents/#update-an-existing-incident)  
[Create incident attachment](https://docs.datadoghq.com/api/latest/incidents/#create-incident-attachment)  
[Delete incident attachment](https://docs.datadoghq.com/api/latest/incidents/#delete-incident-attachment)  
[Update incident attachment](https://docs.datadoghq.com/api/latest/incidents/#update-incident-attachment)  
[Create an incident impact](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-impact)  
[Delete an incident impact](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-impact)  
[Create an incident integration metadata](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-integration-metadata)  
[Delete an incident integration metadata](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-integration-metadata)  
[Update an existing incident integration metadata](https://docs.datadoghq.com/api/latest/incidents/#update-an-existing-incident-integration-metadata)  
[Create an incident todo](https://docs.datadoghq.com/api/latest/incidents/#create-an-incident-todo)  
[Delete an incident todo](https://docs.datadoghq.com/api/latest/incidents/#delete-an-incident-todo)  
[Update an incident todo](https://docs.datadoghq.com/api/latest/incidents/#update-an-incident-todo)  

#### Metrics
Scope name
Description
Endpoints that require this scope
metrics_read
View custom metrics.
[Get active metrics list](https://docs.datadoghq.com/api/latest/metrics/#get-active-metrics-list)  
[Get metric metadata](https://docs.datadoghq.com/api/latest/metrics/#get-metric-metadata)  
[Search metrics](https://docs.datadoghq.com/api/latest/metrics/#search-metrics)  
[Get a list of metrics](https://docs.datadoghq.com/api/latest/metrics/#get-a-list-of-metrics)  
[List tags by metric name](https://docs.datadoghq.com/api/latest/metrics/#list-tags-by-metric-name)  
[List tag configuration by name](https://docs.datadoghq.com/api/latest/metrics/#list-tag-configuration-by-name)  

timeseries_query
Query Timeseries data.
[Query timeseries points](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-points)  
[Query scalar data across multiple products](https://docs.datadoghq.com/api/latest/metrics/#query-scalar-data-across-multiple-products)  
[Query timeseries data across multiple products](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-data-across-multiple-products)  

#### Org Connections
Scope name
Description
Endpoints that require this scope
org_connections_read
Read cross organization connections.
[List Org Connections](https://docs.datadoghq.com/api/latest/org-connections/#list-org-connections)  

org_connections_write
Create, edit, and delete cross organization connections.
[Create Org Connection](https://docs.datadoghq.com/api/latest/org-connections/#create-org-connection)  
[Delete Org Connection](https://docs.datadoghq.com/api/latest/org-connections/#delete-org-connection)  
[Update Org Connection](https://docs.datadoghq.com/api/latest/org-connections/#update-org-connection)  

#### Service Definition, Service Scorecards, Software Catalog
Scope name
Description
Endpoints that require this scope
apm_service_catalog_read
View service catalog and service definitions.
[Get a list of entities](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entities)  
[Preview catalog entities](https://docs.datadoghq.com/api/latest/software-catalog/#preview-catalog-entities)  
[Get a list of entity kinds](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entity-kinds)  
[Get a list of entity relations](https://docs.datadoghq.com/api/latest/software-catalog/#get-a-list-of-entity-relations)  
[List all rule outcomes](https://docs.datadoghq.com/api/latest/service-scorecards/#list-all-rule-outcomes)  
[List all rules](https://docs.datadoghq.com/api/latest/service-scorecards/#list-all-rules)  
[Get all service definitions](https://docs.datadoghq.com/api/latest/service-definition/#get-all-service-definitions)  
[Get a single service definition](https://docs.datadoghq.com/api/latest/service-definition/#get-a-single-service-definition)  

apm_service_catalog_write
Add, modify, and delete service catalog definitions when those definitions are maintained by Datadog.
[Create or update entities](https://docs.datadoghq.com/api/latest/software-catalog/#create-or-update-entities)  
[Delete a single entity](https://docs.datadoghq.com/api/latest/software-catalog/#delete-a-single-entity)  
[Create or update kinds](https://docs.datadoghq.com/api/latest/software-catalog/#create-or-update-kinds)  
[Delete a single kind](https://docs.datadoghq.com/api/latest/software-catalog/#delete-a-single-kind)  
[Update Scorecard outcomes asynchronously](https://docs.datadoghq.com/api/latest/service-scorecards/#update-scorecard-outcomes-asynchronously)  
[Create outcomes batch](https://docs.datadoghq.com/api/latest/service-scorecards/#create-outcomes-batch)  
[Create a new rule](https://docs.datadoghq.com/api/latest/service-scorecards/#create-a-new-rule)  
[Delete a rule](https://docs.datadoghq.com/api/latest/service-scorecards/#delete-a-rule)  
[Update an existing rule](https://docs.datadoghq.com/api/latest/service-scorecards/#update-an-existing-rule)  
[Create or update service definition](https://docs.datadoghq.com/api/latest/service-definition/#create-or-update-service-definition)  
[Delete a single service definition](https://docs.datadoghq.com/api/latest/service-definition/#delete-a-single-service-definition)  

#### Service Level Objective Corrections, Service Level Objectives
Scope name
Description
Endpoints that require this scope
slos_corrections
Apply, edit, and delete SLO status corrections. A user with this permission can make status corrections, even if they do not have permission to edit those SLOs.
[Create an SLO correction](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#create-an-slo-correction)  

slos_read
View SLOs and status corrections.
[Get all SLOs](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-all-slos)  
[Check if SLOs can be safely deleted](https://docs.datadoghq.com/api/latest/service-level-objectives/#check-if-slos-can-be-safely-deleted)  
[Get all SLO corrections](https://docs.datadoghq.com/api/latest/service-level-objective-corrections/#get-all-slo-corrections)  
[Search for SLOs](https://docs.datadoghq.com/api/latest/service-level-objectives/#search-for-slos)  
[Get an SLO's details](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-an-slos-details)  
[Get Corrections For an SLO](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-corrections-for-an-slo)  
[Get an SLO's history](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-an-slos-history)  
[Create a new SLO report](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-a-new-slo-report)  
[Get SLO report](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-slo-report)  
[Get SLO report status](https://docs.datadoghq.com/api/latest/service-level-objectives/#get-slo-report-status)  

slos_write
Create, edit, and delete SLOs.
[Create an SLO object](https://docs.datadoghq.com/api/latest/service-level-objectives/#create-an-slo-object)  
[Bulk Delete SLO Timeframes](https://docs.datadoghq.com/api/latest/service-level-objectives/#bulk-delete-slo-timeframes)  
[Delete an SLO](https://docs.datadoghq.com/api/latest/service-level-objectives/#delete-an-slo)  
[Update an SLO](https://docs.datadoghq.com/api/latest/service-level-objectives/#update-an-slo)  

#### Teams
Scope name
Description
Endpoints that require this scope
teams_manage
Manage Teams. Create, delete, rename, and edit metadata of all Teams. To control Team membership across all Teams, use the User Access Manage permission.
[Create a team](https://docs.datadoghq.com/api/latest/teams/#create-a-team)  
[Create a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#create-a-team-hierarchy-link)  
[Remove a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-hierarchy-link)  
[Link Teams with GitHub Teams](https://docs.datadoghq.com/api/latest/teams/#link-teams-with-github-teams)  
[Remove a team](https://docs.datadoghq.com/api/latest/teams/#remove-a-team)  

teams_read
Read Teams data. A User with this permission can view Team names, metadata, and which Users are on each Team.
[Get all teams](https://docs.datadoghq.com/api/latest/teams/#get-all-teams)  
[Create a team](https://docs.datadoghq.com/api/latest/teams/#create-a-team)  
[Get team hierarchy links](https://docs.datadoghq.com/api/latest/teams/#get-team-hierarchy-links)  
[Create a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#create-a-team-hierarchy-link)  
[Remove a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-hierarchy-link)  
[Get a team hierarchy link](https://docs.datadoghq.com/api/latest/teams/#get-a-team-hierarchy-link)  
[Delete team connections](https://docs.datadoghq.com/api/latest/teams/#delete-team-connections)  
[List team connections](https://docs.datadoghq.com/api/latest/teams/#list-team-connections)  
[Create team connections](https://docs.datadoghq.com/api/latest/teams/#create-team-connections)  
[Get team sync configurations](https://docs.datadoghq.com/api/latest/teams/#get-team-sync-configurations)  
[Get all member teams](https://docs.datadoghq.com/api/latest/teams/#get-all-member-teams)  
[Add a member team](https://docs.datadoghq.com/api/latest/teams/#add-a-member-team)  
[Remove a member team](https://docs.datadoghq.com/api/latest/teams/#remove-a-member-team)  
[Remove a team](https://docs.datadoghq.com/api/latest/teams/#remove-a-team)  
[Get a team](https://docs.datadoghq.com/api/latest/teams/#get-a-team)  
[Update a team](https://docs.datadoghq.com/api/latest/teams/#update-a-team)  
[Get links for a team](https://docs.datadoghq.com/api/latest/teams/#get-links-for-a-team)  
[Create a team link](https://docs.datadoghq.com/api/latest/teams/#create-a-team-link)  
[Remove a team link](https://docs.datadoghq.com/api/latest/teams/#remove-a-team-link)  
[Get a team link](https://docs.datadoghq.com/api/latest/teams/#get-a-team-link)  
[Update a team link](https://docs.datadoghq.com/api/latest/teams/#update-a-team-link)  
[Get team memberships](https://docs.datadoghq.com/api/latest/teams/#get-team-memberships)  
[Add a user to a team](https://docs.datadoghq.com/api/latest/teams/#add-a-user-to-a-team)  
[Remove a user from a team](https://docs.datadoghq.com/api/latest/teams/#remove-a-user-from-a-team)  
[Update a user's membership attributes on a team](https://docs.datadoghq.com/api/latest/teams/#update-a-users-membership-attributes-on-a-team)  
[Get team notification rules](https://docs.datadoghq.com/api/latest/teams/#get-team-notification-rules)  
[Create team notification rule](https://docs.datadoghq.com/api/latest/teams/#create-team-notification-rule)  
[Delete team notification rule](https://docs.datadoghq.com/api/latest/teams/#delete-team-notification-rule)  
[Get team notification rule](https://docs.datadoghq.com/api/latest/teams/#get-team-notification-rule)  
[Update team notification rule](https://docs.datadoghq.com/api/latest/teams/#update-team-notification-rule)  
[Get permission settings for a team](https://docs.datadoghq.com/api/latest/teams/#get-permission-settings-for-a-team)  
[Update permission setting for team](https://docs.datadoghq.com/api/latest/teams/#update-permission-setting-for-team)  
[Get user memberships](https://docs.datadoghq.com/api/latest/teams/#get-user-memberships)  

#### Usage Metering
Scope name
Description
Endpoints that require this scope
billing_read
View your organization's billing information.
[Get Monthly Cost Attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-monthly-cost-attribution)  
[Get cost across multi-org account](https://docs.datadoghq.com/api/latest/usage-metering/#get-cost-across-multi-org-account)  
[Get estimated cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-estimated-cost-across-your-account)  
[Get historical cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-historical-cost-across-your-account)  
[Get projected cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-projected-cost-across-your-account)  

usage_read
View your organization's usage and usage attribution.
[Get hourly usage for analyzed logs](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-analyzed-logs)  
[Get hourly usage for audit logs](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-audit-logs)  
[Get hourly usage for Lambda](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-lambda)  
[Get billable usage across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-billable-usage-across-your-account)  
[Get hourly usage for CI visibility](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-ci-visibility)  
[Get hourly usage for CSM Pro](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-csm-pro)  
[Get hourly usage for cloud workload security](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-cloud-workload-security)  
[Get hourly usage for database monitoring](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-database-monitoring)  
[Get hourly usage for Fargate](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-fargate)  
[Get hourly usage for hosts and containers](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-hosts-and-containers)  
[Get hourly usage attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-attribution)  
[Get hourly usage for incident management](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-incident-management)  
[Get hourly usage for indexed spans](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-indexed-spans)  
[Get hourly usage for ingested spans](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-ingested-spans)  
[Get hourly usage for IoT](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-iot)  
[Get hourly usage for logs](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-logs)  
[Get hourly logs usage by retention](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-logs-usage-by-retention)  
[Get hourly usage for logs by index](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-logs-by-index)  
[Get monthly usage attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-monthly-usage-attribution)  
[get hourly usage for network flows](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-network-flows)  
[Get hourly usage for network hosts](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-network-hosts)  
[Get hourly usage for online archive](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-online-archive)  
[Get hourly usage for profiled hosts](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-profiled-hosts)  
[Get hourly usage for RUM units](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-rum-units)  
[Get hourly usage for RUM sessions](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-rum-sessions)  
[Get hourly usage for sensitive data scanner](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-sensitive-data-scanner)  
[Get hourly usage for SNMP devices](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-snmp-devices)  
[Get usage across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-usage-across-your-account)  
[Get hourly usage for synthetics checks](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-checks)  
[Get hourly usage for synthetics API checks](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-api-checks)  
[Get hourly usage for synthetics browser checks](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-synthetics-browser-checks)  
[Get hourly usage for custom metrics](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-custom-metrics)  
[Get all custom metrics by hourly average](https://docs.datadoghq.com/api/latest/usage-metering/#get-all-custom-metrics-by-hourly-average)  
[Get active billing dimensions for cost attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-active-billing-dimensions-for-cost-attribution)  
[Get Monthly Cost Attribution](https://docs.datadoghq.com/api/latest/usage-metering/#get-monthly-cost-attribution)  
[Get hourly usage for application security](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-application-security)  
[Get billing dimension mapping for usage endpoints](https://docs.datadoghq.com/api/latest/usage-metering/#get-billing-dimension-mapping-for-usage-endpoints)  
[Get cost across multi-org account](https://docs.datadoghq.com/api/latest/usage-metering/#get-cost-across-multi-org-account)  
[Get estimated cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-estimated-cost-across-your-account)  
[Get historical cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-historical-cost-across-your-account)  
[Get hourly usage by product family](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-by-product-family)  
[Get hourly usage for Lambda traced invocations](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-lambda-traced-invocations)  
[Get hourly usage for observability pipelines](https://docs.datadoghq.com/api/latest/usage-metering/#get-hourly-usage-for-observability-pipelines)  
[Get projected cost across your account](https://docs.datadoghq.com/api/latest/usage-metering/#get-projected-cost-across-your-account)  

#### Webhooks Integration
Scope name
Description
Endpoints that require this scope
create_webhooks
Create webhooks integrations.
[Create a webhooks integration](https://docs.datadoghq.com/api/latest/webhooks-integration/#create-a-webhooks-integration)  

#### Workflow Automation
Scope name
Description
Endpoints that require this scope
workflows_read
View workflows.
[List workflow instances](https://docs.datadoghq.com/api/latest/workflow-automation/#list-workflow-instances)  
[Get a workflow instance](https://docs.datadoghq.com/api/latest/workflow-automation/#get-a-workflow-instance)  

workflows_run
Run workflows.
[Execute a workflow](https://docs.datadoghq.com/api/latest/workflow-automation/#execute-a-workflow)  

![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=24546ac7-72ae-4451-8b75-d4ec3fab7743&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=7935ae67-a159-466e-bbee-29224c27f170&pt=Authorization%20Scopes&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fscopes%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=24546ac7-72ae-4451-8b75-d4ec3fab7743&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=7935ae67-a159-466e-bbee-29224c27f170&pt=Authorization%20Scopes&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fscopes%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=95fdc5d3-1caf-4408-a3e5-0584fccf6c79&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Authorization%20Scopes&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fscopes%2F&r=&lt=1484&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=268200)
