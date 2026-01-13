# Source: https://docs.datadoghq.com/agent/troubleshooting/permissions.md

# Source: https://docs.datadoghq.com/account_management/rbac/permissions.md

---
title: Datadog Role Permissions
description: >-
  Complete reference of Datadog permissions, including managed roles, custom
  roles, sensitive permissions, and the permissions list.
breadcrumbs: Docs > Account Management > Access Control > Datadog Role Permissions
source_url: https://docs.datadoghq.com/rbac/permissions/index.html
---

# Datadog Role Permissions

## Permissions{% #permissions %}

Permissions define the type of access a user has to a given resource. Typically, permissions give a user the right to read, edit, or delete an object. Permissions underlie the access rights of all roles, including the three managed roles and custom roles.

### Sensitive permissions{% #sensitive-permissions %}

Some Datadog permissions provide access to more privileged functionality that is important to be aware of, such as:

- Access to change organization settings
- Access to read potentially sensitive data
- Access to perform privileged operations

Sensitive permissions are flagged in the Roles and Permissions interfaces to identify that they may need increased scrutiny. As a best practice, administrators configuring roles should pay special attention to these permissions, and confirm which of these permissions are assigned to their roles and users.

### Preview mode permissions{% #preview-mode-permissions %}

Some permissions appear in "preview mode" before becoming fully enforced. During this period:

- Preview permissions are marked in the app with a "Preview" badge
- They do not restrict access until the preview period ends
- The preview typically lasts 2-4 weeks before enforcement begins
- Administrators should configure roles appropriately during this period

Preview mode gives your organization's administrators the ability to opt into certain new permissions, so they can prevent losing access to resources that were previously unrestricted. Release notes associated with each preview mode permission indicate when the permission is created and when it will be enforced. While these permissions don't restrict access during preview, Datadog recommends updating role configurations before they become enforced to prevent disruption.

## Roles{% #roles %}

### Managed roles{% #managed-roles %}

By default, existing users are associated with one of the three managed roles:

- Datadog Admin Role
- Datadog Standard Role
- Datadog Read Only Role

All users with one of these roles can read data, except for [individually read-restricted](https://docs.datadoghq.com/account_management/rbac/granular_access) resources. Admin and Standard users have write permissions on assets. Admin users have additional read and write permissions for sensitive assets relating to user management, org management, billing, and usage.

Managed roles are created and maintained by Datadog. Their permissions may be automatically updated by Datadog as new features are added or permissions change. Users cannot modify managed roles directly, but they can clone them to create custom roles with specific permissions. If necessary, users can delete managed roles from their account.

### Custom roles{% #custom-roles %}

Create a custom role to combine permissions into new roles. A custom role gives you the ability to define a persona, for example, a billing administrator, and then assign the appropriate permissions for that role. After creating a role, assign or remove permissions to this role directly by [updating the role in Datadog](https://docs.datadoghq.com/account_management/users/#edit-a-user-s-roles), or through the [Datadog Permission API](https://docs.datadoghq.com/api/latest/roles/#list-permissions).

Unlike Managed Roles, custom roles do not receive new permissions when Datadog releases new products and features. Custom roles only receive new permissions to maintain compatibility when Datadog releases a new permission gating existing functionality.

**Note**: When adding a new custom role to a user, make sure to remove the managed Datadog role associated with that user to enforce the new role permissions.

## Permissions list{% #permissions-list %}

The following table lists the name, description, and default role for all available permissions in Datadog. Each asset type has corresponding read and write permissions.

Each managed role inherits all of the permissions from the less powerful roles. Therefore, the Datadog Standard Role has all of the permissions listed in the table with Datadog Read Only as the default role. Additionally, the Datadog Admin Role contains all of the permissions from both the Datadog Standard and the Datadog Read Only Role.

## API and Application Keys{% #api-and-application-keys %}

Find below the list of permissions for the api and application keys assets:

| Name                                       | Description                                                                                                                                                             | Default Role           |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| User App Keys(`user_app_keys`)             | View and manage Application Keys owned by the user.                                                                                                                     | Datadog Standard Role  |
| Org App Keys Read(`org_app_keys_read`)     | View Application Keys owned by all users in the organization.                                                                                                           | Datadog Standard Role  |
| Org App Keys Write(`org_app_keys_write`)   | Manage Application Keys owned by all users in the organization.                                                                                                         | Datadog Admin Role     |
| API Keys Read(`api_keys_read`)             | List and retrieve the key values of all API Keys in your organization.                                                                                                  | Datadog Standard Role  |
| API Keys Write(`api_keys_write`)           | Create and rename API Keys for your organization.                                                                                                                       | Datadog Admin Role     |
| Client Tokens Read(`client_tokens_read`)   | Read Client Tokens. Unlike API keys, client tokens may be exposed client-side in JavaScript code for web browsers and other clients to send data to Datadog.            | Datadog Read Only Role |
| Client Tokens Write(`client_tokens_write`) | Create and edit Client Tokens. Unlike API keys, client tokens may be exposed client-side in JavaScript code for web browsers and other clients to send data to Datadog. | Datadog Standard Role  |
| API Keys Delete(`api_keys_delete`)         | Delete API Keys for your organization.                                                                                                                                  | Datadog Admin Role     |

## APM{% #apm %}

Find below the list of permissions for the apm assets:

| Name                                                                                            | Description                                                                                                                                                                             | Default Role           |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| APM Read(`apm_read`)                                                                            | Read and query APM and Trace Analytics.                                                                                                                                                 | Datadog Read Only Role |
| APM Retention Filters Read(`apm_retention_filter_read`)                                         | Read trace retention filters. A user with this permission can view the retention filters page, list of filters, their statistics, and creation info.                                    | Datadog Read Only Role |
| APM Retention Filters Write(`apm_retention_filter_write`)                                       | Create, edit, and delete trace retention filters. A user with this permission can create new retention filters, and update or delete to existing retention filters.                     | Datadog Admin Role     |
| APM Service Ingest Read(`apm_service_ingest_read`)                                              | Access service ingestion pages. A user with this permission can view the service ingestion page, list of root services, their statistics, and creation info.                            | Datadog Read Only Role |
| APM Service Ingest Write(`apm_service_ingest_write`)                                            | Edit service ingestion pages' root services. A user with this permission can edit the root service ingestion and generate a code snippet to increase ingestion per service.             | Datadog Admin Role     |
| APM Apdex Manage Write(`apm_apdex_manage_write`)                                                | Set Apdex T value on any service. A user with this permission can set the T value from the Apdex graph on the service page.                                                             | Datadog Admin Role     |
| APM Tag Management Write(`apm_tag_management_write`)                                            | Edit second primary tag selection. A user with this permission can modify the second primary tag dropdown in the APM settings page.                                                     | Datadog Admin Role     |
| APM Primary Operation Write(`apm_primary_operation_write`)                                      | Edit the operation name value selection. A user with this permission can modify the operation name list in the APM settings page and the operation name controller on the service page. | Datadog Standard Role  |
| Dynamic Instrumentation Write(`debugger_write`)                                                 | Edit Dynamic Instrumentation configuration. Create or modify Dynamic Instrumentation probes that do not capture function state.                                                         | Datadog Admin Role     |
| Dynamic Instrumentation Read(`debugger_read`)                                                   | View Dynamic Instrumentation configuration.                                                                                                                                             | Datadog Read Only Role |
| APM Generate Metrics(`apm_generate_metrics`)                                                    | Create custom metrics from spans.                                                                                                                                                       | Datadog Standard Role  |
| APM Pipelines Write(`apm_pipelines_write`)                                                      | Add and change APM pipeline configurations.                                                                                                                                             | Datadog Admin Role     |
| APM Pipelines Read(`apm_pipelines_read`)                                                        | View APM pipeline configurations.                                                                                                                                                       | Datadog Read Only Role |
| Service Catalog Write(`apm_service_catalog_write`)                                              | Add, modify, and delete service catalog definitions when those definitions are maintained by Datadog.                                                                                   | Datadog Standard Role  |
| Service Catalog Read(`apm_service_catalog_read`)                                                | View service catalog and service definitions.                                                                                                                                           | Datadog Read Only Role |
| APM Remote Configuration Write(`apm_remote_configuration_write`)                                | Edit APM Remote Configuration.                                                                                                                                                          | Datadog Admin Role     |
| APM Remote Configuration Read(`apm_remote_configuration_read`)                                  | View APM Remote Configuration.                                                                                                                                                          | Datadog Standard Role  |
| Continuous Profiler Read(`continuous_profiler_read`)                                            | View data in Continuous Profiler.                                                                                                                                                       | Datadog Read Only Role |
| Dynamic Instrumentation Capture Variables(`debugger_capture_variables`)                         | Create or modify Dynamic Instrumentation probes that capture function state: local variables, method arguments, fields, and return value or thrown exception.                           | Datadog Admin Role     |
| API Catalog Write(`apm_api_catalog_write`)                                                      | Add, modify, and delete API catalog definitions.                                                                                                                                        | Datadog Standard Role  |
| API Catalog Read(`apm_api_catalog_read`)                                                        | View API catalog and API definitions.                                                                                                                                                   | Datadog Read Only Role |
| Read Continuous Profiler Profile-Guided Optimization (PGO) Data(`continuous_profiler_pgo_read`) | Read and query Continuous Profiler data for Profile-Guided Optimization (PGO).                                                                                                          | Datadog Read Only Role |
| Dynamic Instrumentation Write Pre-Prod(`debugger_write_pre_prod`)                               | Edit Dynamic Instrumentation configuration. Create or Modify Dynamic Instrumentation probes targeted at pre-prod environments.                                                          | Datadog Standard Role  |
| APM Service Renaming Write(`apm_service_renaming_write`)                                        | Edit service renaming. A user with this permission can modify service renaming rules.                                                                                                   | Datadog Admin Role     |

## Access Management{% #access-management %}

Find below the list of permissions for the access management assets:

| Name                                                           | Description                                                                                                                                                                                                                                                                                                                | Default Role           |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| User Access Invite(`user_access_invite`)                       | Invite other users to your organization.                                                                                                                                                                                                                                                                                   | Datadog Standard Role  |
| User Access Manage(`user_access_manage`)                       | Disable users, manage user roles, manage SAML-to-role mappings, and configure logs restriction queries.                                                                                                                                                                                                                    | Datadog Admin Role     |
| Service Account Write(`service_account_write`)                 | Create, disable, and use Service Accounts in your organization.                                                                                                                                                                                                                                                            | Datadog Admin Role     |
| Org Management(`org_management`)                               | Edit org configurations, including authentication and certain security preferences such as configuring SAML, renaming an org, configuring allowed login methods, creating child orgs, subscribing & unsubscribing from apps in the marketplace, and enabling & disabling Remote Configuration for the entire organization. | Datadog Admin Role     |
| Org Connections Write(`org_connections_write`)                 | Control which organizations can query your organization's data.                                                                                                                                                                                                                                                            | Datadog Admin Role     |
| Org Connections Read(`org_connections_read`)                   | View which organizations can query data from your organization. Query data from other organizations.                                                                                                                                                                                                                       | Datadog Read Only Role |
| Governance Console Read(`governance_console_read`)             | View the Governance Console.                                                                                                                                                                                                                                                                                               | Datadog Standard Role  |
| Governance Console Write (Preview)(`governance_console_write`) | Enforce Governance controls via the Governance Console. Note: This permission is in Preview Mode and will be enforced soon.                                                                                                                                                                                                | Datadog Admin Role     |

## App Builder & Workflow Automation{% #app-builder--workflow-automation %}

Find below the list of permissions for the app builder & workflow automation assets:

| Name                                                   | Description                                                                                                  | Default Role           |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ---------------------- |
| Workflows Read(`workflows_read`)                       | View workflows.                                                                                              | Datadog Read Only Role |
| Workflows Write(`workflows_write`)                     | Create, edit, and delete workflows.                                                                          | Datadog Standard Role  |
| Workflows Run(`workflows_run`)                         | Run workflows.                                                                                               | Datadog Standard Role  |
| Connections Read(`connections_read`)                   | List and view available connections. Connections contain secrets that cannot be revealed.                    | Datadog Read Only Role |
| Connections Write(`connections_write`)                 | Create and delete connections.                                                                               | Datadog Standard Role  |
| Connections Resolve(`connections_resolve`)             | Resolve connections.                                                                                         | Datadog Standard Role  |
| Apps View(`apps_run`)                                  | View and run Apps in App Builder.                                                                            | Datadog Standard Role  |
| Apps Write(`apps_write`)                               | Create, edit, publish, and delete Apps in App Builder.                                                       | Datadog Standard Role  |
| Private Action Runner Read(`on_prem_runner_read`)      | View and search Private Action Runners for Workflow Automation and App Builder.                              | Datadog Read Only Role |
| Private Action Runner Contribute(`on_prem_runner_use`) | Attach a Private Action Runner to a connection.                                                              | Datadog Standard Role  |
| Private Action Runner Write(`on_prem_runner_write`)    | Create and edit Private Action Runners for Workflow Automation and App Builder.                              | Datadog Admin Role     |
| Actions Datastore Read(`apps_datastore_read`)          | Allows read access to the data within the Actions Datastore.                                                 | Datadog Read Only Role |
| Actions Datastore Write(`apps_datastore_write`)        | Allows modification of data within the Actions Datastore, including adding, editing, and deleting records.   | Datadog Standard Role  |
| Actions Datastore Manage(`apps_datastore_manage`)      | Allows management of the Actions Datastore, including creating, updating, and deleting the datastore itself. | Datadog Standard Role  |
| Connection Groups Write(`connection_groups_write`)     | Create, delete and update connection groups.                                                                 | Datadog Standard Role  |
| Connection Groups Read(`connection_groups_read`)       | Read and use connection groups.                                                                              | Datadog Read Only Role |
| Actions Interface Run(`actions_interface_run`)         | Execute actions in the Bits AI Action Interface.                                                             | Datadog Standard Role  |
| Forms Read(`apps_form_read`)                           | View and respond to Forms.                                                                                   | Datadog Read Only Role |
| Forms Manage(`apps_form_manage`)                       | Create, update, and manage Forms.                                                                            | Datadog Standard Role  |

## Application Security{% #application-security %}

Find below the list of permissions for the application security assets:

| Name                                   | Description              | Default Role          |
| -------------------------------------- | ------------------------ | --------------------- |
| AI Guard Evaluate(`ai_guard_evaluate`) | Evaluate AI Guard rules. | Datadog Standard Role |

## Billing and Usage{% #billing-and-usage %}

Find below the list of permissions for the billing and usage assets:

| Name                                                   | Description                                                                  | Default Role       |
| ------------------------------------------------------ | ---------------------------------------------------------------------------- | ------------------ |
| Billing Read(`billing_read`)                           | View your organization's subscription and payment method but not make edits. | Datadog Admin Role |
| Billing Edit(`billing_edit`)                           | Manage your organization's subscription and payment method.                  | Datadog Admin Role |
| Usage Read(`usage_read`)                               | View your organization's usage and usage attribution.                        | Datadog Admin Role |
| Usage Edit(`usage_edit`)                               | Manage your organization's usage attribution set-up.                         | Datadog Admin Role |
| Usage Notifications Read(`usage_notifications_read`)   | Receive notifications and view currently configured notification settings.   | Datadog Admin Role |
| Usage Notifications Write(`usage_notifications_write`) | Receive notifications and configure notification settings.                   | Datadog Admin Role |

## Bits AI{% #bits-ai %}

Find below the list of permissions for the bits ai assets:

| Name                                                   | Description                            | Default Role           |
| ------------------------------------------------------ | -------------------------------------- | ---------------------- |
| Bits Investigations Read(`bits_investigations_read`)   | Read Bits investigations.              | Datadog Read Only Role |
| Bits Investigations Write(`bits_investigations_write`) | Run and configure Bits investigations. | Datadog Standard Role  |

## Case and Incident Management{% #case-and-incident-management %}

Find below the list of permissions for the case and incident management assets:

| Name                                                                         | Description                                                                  | Default Role           |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------- |
| Incidents Read(`incident_read`)                                              | View incidents in Datadog.                                                   | Datadog Read Only Role |
| Incidents Write(`incident_write`)                                            | Create, view, and manage incidents in Datadog.                               | Datadog Standard Role  |
| Incident Settings Read(`incident_settings_read`)                             | View Incident Settings.                                                      | Datadog Standard Role  |
| Incident Settings Write(`incident_settings_write`)                           | Configure Incident Settings.                                                 | Datadog Standard Role  |
| Private Incidents Global Access(`incidents_private_global_access`)           | Access all private incidents in Datadog, even when not added as a responder. | None                   |
| Cases Read(`cases_read`)                                                     | View Cases.                                                                  | Datadog Read Only Role |
| Cases Write(`cases_write`)                                                   | Create and update cases.                                                     | Datadog Standard Role  |
| Incident Notification Settings Read(`incident_notification_settings_read`)   | View Incidents Notification settings.                                        | Datadog Standard Role  |
| Incident Notification Settings Write(`incident_notification_settings_write`) | Configure Incidents Notification settings.                                   | Datadog Standard Role  |
| Case Management Shared Settings Write(`cases_shared_settings_write`)         | Configure shared settings for Case Management.                               | Datadog Standard Role  |

## Cloud Cost Management{% #cloud-cost-management %}

Find below the list of permissions for the cloud cost management assets:

| Name                                                               | Description                                                                                                                             | Default Role           |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Cloud Cost Management Read(`cloud_cost_management_read`)           | View Cloud Cost pages and the cloud cost data source in dashboards and notebooks. For more details, see the Cloud Cost Management docs. | Datadog Read Only Role |
| Cloud Cost Management Write(`cloud_cost_management_write`)         | Configure cloud cost accounts and global customizations. For more details, see the Cloud Cost Management docs.                          | Datadog Standard Role  |
| Cloud Cost Report Schedules Write(`generate_ccm_report_schedules`) | View all report schedules and manage only the ones they've created.                                                                     | Datadog Standard Role  |
| Cloud Cost Report Schedules Manage(`manage_ccm_report_schedules`)  | View, create, and fully manage all report schedules across the organization.                                                            | Datadog Admin Role     |

## Cloud Network Monitoring{% #cloud-network-monitoring %}

Find below the list of permissions for the cloud network monitoring assets:

| Name                                                         | Description                     | Default Role           |
| ------------------------------------------------------------ | ------------------------------- | ---------------------- |
| Network Connections Read(`network_connections_read`)         | Read Cloud Network Connections. | Datadog Read Only Role |
| Network Health Insights Read(`network_health_insights_read`) | Read Network Health Insights.   | Datadog Read Only Role |

## Cloud Security Platform{% #cloud-security-platform %}

Find below the list of permissions for the cloud security platform assets:

| Name                                                                                   | Description                                                                                                                                                         | Default Role           |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Security Rules Read(`security_monitoring_rules_read`)                                  | Read Detection Rules.                                                                                                                                               | Datadog Read Only Role |
| Security Rules Write(`security_monitoring_rules_write`)                                | Create and edit Detection Rules.                                                                                                                                    | Datadog Standard Role  |
| Security Signals Read(`security_monitoring_signals_read`)                              | View Security Signals.                                                                                                                                              | Datadog Read Only Role |
| Security Signals Write(`security_monitoring_signals_write`)                            | Modify Security Signals.                                                                                                                                            | Datadog Standard Role  |
| Security Filters Read(`security_monitoring_filters_read`)                              | Read Security Filters.                                                                                                                                              | Datadog Read Only Role |
| Security Filters Write(`security_monitoring_filters_write`)                            | Create, edit, and delete Security Filters.                                                                                                                          | Datadog Admin Role     |
| Application Security Management Event Rules Read(`appsec_event_rule_read`)             | View Application Security Management Event Rules.                                                                                                                   | Datadog Read Only Role |
| Application Security Management Event Rules Write(`appsec_event_rule_write`)           | Edit Application Security Management Event Rules.                                                                                                                   | Datadog Standard Role  |
| Security Notification Rules Read(`security_monitoring_notification_profiles_read`)     | Read Notification Rules.                                                                                                                                            | Datadog Read Only Role |
| Security Notification Rules Write(`security_monitoring_notification_profiles_write`)   | Create, edit, and delete Notification Rules.                                                                                                                        | Datadog Standard Role  |
| Cloud Workload Security Agent Rules Read(`security_monitoring_cws_agent_rules_read`)   | Read Cloud Workload Security Agent Rules.                                                                                                                           | Datadog Read Only Role |
| Cloud Workload Security Agent Rules Write(`security_monitoring_cws_agent_rules_write`) | Create, edit, and delete Cloud Workload Security Agent Rules.                                                                                                       | Datadog Standard Role  |
| Application Security Management Protect Read(`appsec_protect_read`)                    | View blocked attackers.                                                                                                                                             | Datadog Read Only Role |
| Application Security Management Protect Write(`appsec_protect_write`)                  | Manage blocked attackers.                                                                                                                                           | Datadog Standard Role  |
| Application Security Management 1-click Enablement Read(`appsec_activation_read`)      | View whether Application Security Management has been enabled or disabled on services via 1-click enablement with Remote Configuration.                             | Datadog Read Only Role |
| Application Security Management 1-click Enablement Write(`appsec_activation_write`)    | Enable or disable Application Security Management on services via 1-click enablement.                                                                               | Datadog Standard Role  |
| Security Monitoring Findings Read(`security_monitoring_findings_read`)                 | View a list of findings that include both misconfigurations and identity risks.                                                                                     | Datadog Standard Role  |
| Security Monitoring Findings Write(`security_monitoring_findings_write`)               | Mute CSPM Findings.                                                                                                                                                 | Datadog Standard Role  |
| Vulnerability Management Write(`appsec_vm_write`)                                      | Update status or assignee of vulnerabilities.                                                                                                                       | Datadog Standard Role  |
| Security Suppressions Read(`security_monitoring_suppressions_read`)                    | Read Rule Suppressions.                                                                                                                                             | Datadog Read Only Role |
| Security Suppressions Write(`security_monitoring_suppressions_write`)                  | Write Rule Suppressions.                                                                                                                                            | Datadog Standard Role  |
| Vulnerability Management Read(`appsec_vm_read`)                                        | View infrastructure, application code and library vulnerabilities. This does not restrict access to the vulnerability data source through the API or inventory SQL. | Datadog Read Only Role |
| Security Pipelines Read(`security_pipelines_read`)                                     | View Security Pipelines.                                                                                                                                            | Datadog Read Only Role |
| Security Pipelines Write(`security_pipelines_write`)                                   | Create, edit, and delete Security Pipelines.                                                                                                                        | Datadog Admin Role     |
| Cloud Workload Security Agent Actions(`security_monitoring_cws_agent_rules_actions`)   | Managing actions on Cloud Workload Security Agent Rules.                                                                                                            | Datadog Admin Role     |
| Security Comments Write(`security_comments_write`)                                     | Write comments into vulnerabilities.                                                                                                                                | Datadog Standard Role  |
| Security Comments Read(`security_comments_read`)                                       | Read comments of vulnerabilities.                                                                                                                                   | Datadog Read Only Role |

## CoTerm{% #coterm %}

Find below the list of permissions for the coterm assets:

| Name                         | Description                | Default Role           |
| ---------------------------- | -------------------------- | ---------------------- |
| CoTerm Write(`coterm_write`) | Write terminal recordings. | Datadog Standard Role  |
| CoTerm Read(`coterm_read`)   | Read terminal recordings.  | Datadog Read Only Role |

## Compliance{% #compliance %}

Find below the list of permissions for the compliance assets:

| Name                                       | Description                                                      | Default Role       |
| ------------------------------------------ | ---------------------------------------------------------------- | ------------------ |
| Audit Trail Read(`audit_logs_read`)        | View Audit Trail in your organization.                           | Datadog Admin Role |
| Audit Trail Write(`audit_logs_write`)      | Configure Audit Trail in your organization.                      | Datadog Admin Role |
| Data Scanner Read(`data_scanner_read`)     | View Sensitive Data Scanner configurations and scanning results. | Datadog Admin Role |
| Data Scanner Write(`data_scanner_write`)   | Edit Sensitive Data Scanner configurations.                      | Datadog Admin Role |
| Data Scanner Unmask(`data_scanner_unmask`) | Unmask (view) sensitive data that was previouly masked.          | Datadog Admin Role |

## Containers{% #containers %}

Find below the list of permissions for the containers assets:

| Name                                                                      | Description                                         | Default Role          |
| ------------------------------------------------------------------------- | --------------------------------------------------- | --------------------- |
| Containers Write Image Trend Metrics(`containers_generate_image_metrics`) | Create or edit trend metrics from container images. | Datadog Standard Role |

## Cross-Product Features{% #cross-product-features %}

Find below the list of permissions for the cross-product features assets:

| Name                                               | Description                                                                                                            | Default Role          |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Saved Views Write(`saved_views_write`)             | Modify Saved Views across all Datadog products.                                                                        | Datadog Standard Role |
| Facets Write(`facets_write`)                       | Manage facets for products other than Log Management, such as APM Traces. To modify Log Facets, use Logs Write Facets. | Datadog Standard Role |
| CSV Report Schedules Write(`generate_log_reports`) | Schedule CSV reports. View CSV report schedules created by other users.                                                | Datadog Standard Role |
| CSV Report Schedules Manage(`manage_log_reports`)  | Edit CSV report schedules created by other users.                                                                      | Datadog Admin Role    |

## DDSQL Editor{% #ddsql-editor %}

Find below the list of permissions for the ddsql editor assets:

| Name                                   | Description                | Default Role           |
| -------------------------------------- | -------------------------- | ---------------------- |
| DDSQL Editor Read(`ddsql_editor_read`) | View and use DDSQL Editor. | Datadog Read Only Role |

## Dashboards{% #dashboards %}

Find below the list of permissions for the dashboards assets:

| Name                                                           | Description                                                                                                                                         | Default Role           |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Dashboards Read(`dashboards_read`)                             | View dashboards.                                                                                                                                    | Datadog Read Only Role |
| Dashboards Write(`dashboards_write`)                           | Create and change dashboards.                                                                                                                       | Datadog Standard Role  |
| Shared Dashboards Public Write(`dashboards_public_share`)      | Create, modify and delete shared dashboards with share type 'Public'. These dashboards can be accessed by anyone on the internet.                   | Datadog Standard Role  |
| Dashboards Report Write(`generate_dashboard_reports`)          | Schedule PDF reports from a dashboard.                                                                                                              | Datadog Standard Role  |
| Shared Dashboards Invite-only Write(`dashboards_invite_share`) | Create, modify and delete shared dashboards with share type 'Invite-only'. These dashboards can only be accessed by user-specified email addresses. | Datadog Standard Role  |
| Shared Dashboards Embed Write(`dashboards_embed_share`)        | Create, modify and delete shared dashboards with share type 'Embed'. These dashboards can be embedded on user-specified domains.                    | Datadog Standard Role  |
| Shared Graphs Write(`embeddable_graphs_share`)                 | Generate public links to share embeddable graphs externally.                                                                                        | Datadog Standard Role  |

## Data Streams Monitoring{% #data-streams-monitoring %}

Find below the list of permissions for the data streams monitoring assets:

| Name                                                                                 | Description                                                                | Default Role       |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------------------ |
| Data Streams Monitoring Capture Messages(`data_streams_monitoring_capture_messages`) | Capture messages from Kafka topics in the Data Streams Monitoring product. | Datadog Admin Role |

## Database Monitoring{% #database-monitoring %}

Find below the list of permissions for the database monitoring assets:

| Name                                                                             | Description                                            | Default Role           |
| -------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------- |
| Database Monitoring Read(`dbm_read`)                                             | View Database Monitoring data.                         | Datadog Read Only Role |
| Database Monitoring Parameterized Queries Read(`dbm_parameterized_queries_read`) | View Parameterized SQL Queries in Database Monitoring. | Datadog Read Only Role |

## Disaster Recovery{% #disaster-recovery %}

Find below the list of permissions for the disaster recovery assets:

| Name                                                              | Description                          | Default Role           |
| ----------------------------------------------------------------- | ------------------------------------ | ---------------------- |
| Datadog Disaster Recovery Read(`disaster_recovery_status_read`)   | View the disaster recovery status.   | Datadog Read Only Role |
| Datadog Disaster Recovery Write(`disaster_recovery_status_write`) | Update the disaster recovery status. | Datadog Admin Role     |

## Error Tracking{% #error-tracking %}

Find below the list of permissions for the error tracking assets:

| Name                                                                             | Description                                                                                                                                                      | Default Role           |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Error Tracking Issue Write(`error_tracking_write`)                               | Edit Error Tracking issues.                                                                                                                                      | Datadog Standard Role  |
| Error Tracking Settings Write(`error_tracking_settings_write`)                   | Disable Error Tracking, edit inclusion filters, and edit rate limit.                                                                                             | Datadog Admin Role     |
| Error Tracking Exclusion Filters Write(`error_tracking_exclusion_filters_write`) | Add or change Error Tracking exclusion filters.                                                                                                                  | Datadog Admin Role     |
| Error Tracking Read(`error_tracking_read`)                                       | View Error Tracking data, including stack traces, error messages, and context. Also includes issue classifications and statuses such as For Review and Reviewed. | Datadog Read Only Role |

## Events{% #events %}

Find below the list of permissions for the events assets:

| Name                                                             | Description                                                                       | Default Role          |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------- |
| Event Correlation Config Read(`event_correlation_config_read`)   | Read Event Correlation Configuration data such as Correlation Rules and Settings. | Datadog Standard Role |
| Event Correlation Config Write(`event_correlation_config_write`) | Manage Event Correlation Configuration such as Correlation Rules and Settings.    | Datadog Standard Role |
| Event Config Write(`event_config_write`)                         | Manage general event configuration such as API Emails.                            | Datadog Standard Role |

## Feature Flags{% #feature-flags %}

Find below the list of permissions for the feature flags assets:

| Name                                                                    | Description                                          | Default Role           |
| ----------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------- |
| Feature Flag Write(`feature_flag_config_write`)                         | Edit Feature Flag Configurations.                    | Datadog Standard Role  |
| Feature Flag Read(`feature_flag_config_read`)                           | View Feature Flag Configurations.                    | Datadog Read Only Role |
| Feature Flag Environment Write(`feature_flag_environment_config_write`) | Ability to modify Feature Flag Environment settings. | Datadog Standard Role  |
| Feature Flag Environment Read(`feature_flag_environment_config_read`)   | Ability to view Feature Flag Environment settings.   | Datadog Read Only Role |

## Fleet Automation{% #fleet-automation %}

Find below the list of permissions for the fleet automation assets:

| Name                                                   | Description                                   | Default Role          |
| ------------------------------------------------------ | --------------------------------------------- | --------------------- |
| Agent Flare Collection(`agent_flare_collection`)       | Collect an Agent flare with Fleet Automation. | Datadog Standard Role |
| Agent Upgrade(`agent_upgrade_write`)                   | Upgrade Datadog Agents with Fleet Automation. | Datadog Admin Role    |
| Agent Configuration Management(`fleet_policies_write`) | Create and deploy Agent configurations.       | Datadog Admin Role    |

## Infrastructure{% #infrastructure %}

Find below the list of permissions for the infrastructure assets:

| Name                                                                             | Description                                                               | Default Role           |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------- |
| Cloudcraft Read(`cloudcraft_read`)                                               | View infrastructure diagrams in the Cloudcraft product.                   | Datadog Read Only Role |
| Infrastructure Resource Policies Read(`infrastructure_resource_policies_read`)   | View Resource Policies under infrastructure products.                     | Datadog Read Only Role |
| Infrastructure Resource Policies Write(`infrastructure_resource_policies_write`) | Create, edit, and delete Resource Policies under infrastructure products. | Datadog Standard Role  |

## Integrations{% #integrations %}

Find below the list of permissions for the integrations assets:

| Name                                                       | Description                                                                                          | Default Role           |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------- |
| AWS Configurations Manage(`aws_configurations_manage`)     | Add or remove but not edit AWS integration configurations.                                           | Datadog Standard Role  |
| Azure Configurations Manage(`azure_configurations_manage`) | Add or remove but not edit Azure integration configurations.                                         | Datadog Standard Role  |
| GCP Configurations Manage(`gcp_configurations_manage`)     | Add or remove but not edit GCP integration configurations.                                           | Datadog Standard Role  |
| Integrations Manage(`manage_integrations`)                 | Install, uninstall, and configure integrations.                                                      | Datadog Standard Role  |
| Integrations Read(`integrations_read`)                     | View integrations and their configurations.                                                          | Datadog Standard Role  |
| OCI Configurations Manage(`oci_configurations_manage`)     | Add or remove but not edit Oracle Cloud integration configurations.                                  | Datadog Standard Role  |
| AWS Configuration Read(`aws_configuration_read`)           | View but not add, remove, or edit AWS integration configurations.                                    | Datadog Standard Role  |
| Azure Configuration Read(`azure_configuration_read`)       | View but not add, remove, or edit Azure integration configurations.                                  | Datadog Standard Role  |
| GCP Configuration Read(`gcp_configuration_read`)           | View but not add, remove, or edit GCP integration configurations.                                    | Datadog Standard Role  |
| OCI Configuration Read(`oci_configuration_read`)           | View but not add, remove, or edit Oracle Cloud integration configurations.                           | Datadog Standard Role  |
| AWS Configuration Edit(`aws_configuration_edit`)           | Edit but not add or remove AWS integration configurations.                                           | Datadog Standard Role  |
| Azure Configuration Edit(`azure_configuration_edit`)       | Edit but not add or remove Azure integration configurations.                                         | Datadog Standard Role  |
| GCP Configuration Edit(`gcp_configuration_edit`)           | Edit but not add or remove GCP integration configurations.                                           | Datadog Standard Role  |
| OCI Configuration Edit(`oci_configuration_edit`)           | Edit but not add or remove Oracle Cloud integration configurations.                                  | Datadog Standard Role  |
| Repository Info Read (Preview)(`repo_info_read`)           | View data from Git repositories. Note: This permission is in Preview Mode and will be enforced soon. | Datadog Read Only Role |
| Repository Settings Write (Preview)(`repo_settings_write`) | Edit Git repositories settings. Note: This permission is in Preview Mode and will be enforced soon.  | Datadog Standard Role  |

## LLM Observability{% #llm-observability %}

Find below the list of permissions for the llm observability assets:

| Name                                               | Description                                                                                                                           | Default Role           |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| LLM Observability Read(`llm_observability_read`)   | View LLM Observability.                                                                                                               | Datadog Read Only Role |
| LLM Observability Write(`llm_observability_write`) | Create, Update, and Delete LLM Observability resources including User Defined Evaluations, OOTB Evaluations, and User Defined Topics. | Datadog Standard Role  |

## Log Management{% #log-management %}

Find below the list of permissions for the log configuration assets and log data, along with the typical category of user you'd assign this permission to. See the recommendations on how to assign permissions to team members in the [Logs RBAC guide](https://docs.datadoghq.com/logs/guide/logs-rbac).

| Name                                                         | Description                                                                                                                                                                                                                                | Default Role           |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| Logs Modify Indexes(`logs_modify_indexes`)                   | Read and modify all indexes in your account. This includes the ability to grant the Logs Read Index Data and Logs Write Exclusion Filters permission to other roles, for some or all indexes.                                              | Datadog Standard Role  |
| Logs Write Exclusion Filters(`logs_write_exclusion_filters`) | Add and change exclusion filters for all or some log indexes. Can be granted in a limited capacity per index to specific roles via the Logs interface or API. If granted from the Roles interface or API, the permission has global scope. | Datadog Standard Role  |
| Logs Write Pipelines(`logs_write_pipelines`)                 | Add and change log pipeline configurations, including the ability to grant the Logs Write Processors permission to other roles, for some or all pipelines.                                                                                 | Datadog Standard Role  |
| Logs Write Processors(`logs_write_processors`)               | Add and change some or all log processor configurations. Can be granted in a limited capacity per pipeline to specific roles via the Logs interface or API. If granted via the Roles interface or API the permission has global scope.     | Datadog Standard Role  |
| Logs Write Archives(`logs_write_archives`)                   | Add and edit Log Archives.                                                                                                                                                                                                                 | Datadog Admin Role     |
| Logs Generate Metrics(`logs_generate_metrics`)               | Create custom metrics from logs.                                                                                                                                                                                                           | Datadog Standard Role  |
| Logs Read Data(`logs_read_data`)                             | Read log data. In order to read log data, a user must have both this permission and Logs Read Index Data. This permission can be restricted with restriction queries. Restrictions are limited to the Log Management product.              | Datadog Read Only Role |
| Logs Read Archives(`logs_read_archives`)                     | Read Log Archives location and use it for rehydration.                                                                                                                                                                                     | Datadog Read Only Role |
| Logs Write Historical Views(`logs_write_historical_view`)    | Rehydrate logs from Archives.                                                                                                                                                                                                              | Datadog Standard Role  |
| Logs Write Facets(`logs_write_facets`)                       | Create or edit Log Facets.                                                                                                                                                                                                                 | Datadog Standard Role  |
| Logs Delete Data(`logs_delete_data`)                         | Delete data from your Logs, including entire indexes.                                                                                                                                                                                      | Datadog Admin Role     |
| Logs Write Forwarding Rules(`logs_write_forwarding_rules`)   | Add and edit forwarding destinations and rules for logs.                                                                                                                                                                                   | Datadog Admin Role     |
| Flex Logs Configuration Write(`flex_logs_config_write`)      | Manage your organization's flex logs configuration.                                                                                                                                                                                        | Datadog Admin Role     |
| Read Logs Workspaces(`logs_read_workspaces`)                 | View Logs Workspaces.                                                                                                                                                                                                                      | Datadog Read Only Role |
| Write Logs Workspaces(`logs_write_workspaces`)               | Create, update, and delete Logs Workspaces.                                                                                                                                                                                                | Datadog Standard Role  |
| Logs Configuration Read(`logs_read_config`)                  | Read logs configuration.                                                                                                                                                                                                                   | Datadog Read Only Role |

Log Management RBAC also includes two legacy permissions, superseded by finer-grained and more extensive `logs_read_data` permission:

| Name                                                                                                                               | Description                          | Default Role           |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------------- |
| [Logs Live Tail](https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/#logs_live_tail)(`logs_live_tail`)                    | Access the live tail feature         | Datadog Read Only Role |
| [Logs Read Index Data](https://docs.datadoghq.com/logs/guide/logs-rbac-permissions/#logs_read_index_data) (`logs_read_index_data`) | Read a subset log data (index based) | Datadog Read Only Role |

## Metrics{% #metrics %}

Find below the list of permissions for the metrics assets:

| Name                                             | Description                                          | Default Role          |
| ------------------------------------------------ | ---------------------------------------------------- | --------------------- |
| Metric Tags Write(`metric_tags_write`)           | Edit and save tag configurations for custom metrics. | Datadog Standard Role |
| Host Tags Write(`host_tags_write`)               | Add and change tags on hosts.                        | Datadog Standard Role |
| Metrics Metadata Write(`metrics_metadata_write`) | Edit metadata on metrics.                            | Datadog Standard Role |

## Monitors{% #monitors %}

Find below the list of permissions for the monitors assets:

| Name                                                              | Description                                                                                                                                                     | Default Role           |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Monitors Read(`monitors_read`)                                    | View monitors.                                                                                                                                                  | Datadog Read Only Role |
| Monitors Write(`monitors_write`)                                  | Edit, delete, and resolve individual monitors.                                                                                                                  | Datadog Standard Role  |
| Manage Downtimes(`monitors_downtime`)                             | Set downtimes to suppress alerts from any monitor in an organization. Mute and unmute monitors. The ability to write monitors is not required to set downtimes. | Datadog Standard Role  |
| Monitor Configuration Policy Write(`monitor_config_policy_write`) | Create, update, and delete monitor configuration policies.                                                                                                      | Datadog Admin Role     |

## Network Device Monitoring{% #network-device-monitoring %}

Find below the list of permissions for the network device monitoring assets:

| Name                                                             | Description                                                                                                                  | Default Role           |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| NDM Netflow Enrichments Write(`ndm_netflow_port_mappings_write`) | Write NDM Netflow enrichment mappings.                                                                                       | Datadog Standard Role  |
| NDM Device Profiles View(`ndm_device_profiles_view`)             | View NDM device profiles.                                                                                                    | Datadog Standard Role  |
| NDM Device Profiles Edit(`ndm_device_profiles_edit`)             | Edit NDM device profiles.                                                                                                    | Datadog Admin Role     |
| NDM Read(`ndm_devices_read`)                                     | Read NDM data directly. Note: even without this permission, NDM data can be retrieved via general infrastructure query APIs. | Datadog Read Only Role |
| NDM Device Tags Write(`ndm_device_tags_write`)                   | Write NDM device tags.                                                                                                       | Datadog Standard Role  |
| NDM Geomap Locations Write(`ndm_geomap_locations_write`)         | Write NDM Geomap locations.                                                                                                  | Datadog Admin Role     |
| NDM Device Config Read(`ndm_device_config_read`)                 | Read NDM device configurations.                                                                                              | Datadog Admin Role     |

## Notebooks{% #notebooks %}

Find below the list of permissions for the notebooks assets:

| Name                               | Description                  | Default Role           |
| ---------------------------------- | ---------------------------- | ---------------------- |
| Notebooks Read(`notebooks_read`)   | View notebooks.              | Datadog Read Only Role |
| Notebooks Write(`notebooks_write`) | Create and change notebooks. | Datadog Standard Role  |

## Observability Pipelines{% #observability-pipelines %}

Find below the list of permissions for the observability pipelines assets:

| Name                                                                                | Description                                             | Default Role           |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------- |
| Observability Pipelines Read(`observability_pipelines_read`)                        | View pipelines in your organization.                    | Datadog Read Only Role |
| Observability Pipelines Write(`observability_pipelines_write`)                      | Edit pipelines in your organization.                    | Datadog Standard Role  |
| Observability Pipelines Delete(`observability_pipelines_delete`)                    | Delete pipelines from your organization.                | Datadog Admin Role     |
| Observability Pipelines Deploy(`observability_pipelines_deploy`)                    | Deploy pipelines in your organization.                  | Datadog Admin Role     |
| Observability Pipelines Live Capture Read(`observability_pipelines_capture_read`)   | View captured events of pipelines in your organization. | Datadog Read Only Role |
| Observability Pipelines Live Capture Write(`observability_pipelines_capture_write`) | Capture live events of pipelines in your organization.  | Datadog Standard Role  |

## On-Call{% #on-call %}

Find below the list of permissions for the on-call assets:

| Name                                 | Description                                                                                    | Default Role           |
| ------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------- |
| On-Call Read(`on_call_read`)         | View On-Call teams, schedules, escalation policies and overrides.                              | Datadog Read Only Role |
| On-Call Write(`on_call_write`)       | Create, update, and delete On-Call teams, schedules and escalation policies.                   | Datadog Standard Role  |
| On-Call Page(`on_call_page`)         | Page On-Call teams and users.                                                                  | Datadog Standard Role  |
| On-Call Responder(`on_call_respond`) | Acknowledge, resolve pages and edit overrides. Allow users to configure their On-Call profile. | Datadog Standard Role  |
| On-Call Admin(`on_call_admin`)       | Manage sensitive and advanced On-Call settings.                                                | Datadog Admin Role     |

## Orchestration{% #orchestration %}

Find below the list of permissions for the orchestration assets:

| Name                                                                                | Description                                                                                                                | Default Role           |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Custom Resource Definition Write(`orchestration_custom_resource_definitions_write`) | Enable, disable and update custom resource indexing.                                                                       | Datadog Standard Role  |
| Workload Scaling Write(`orchestration_workload_scaling_write`)                      | Enable, disable, and configure workload autoscaling. Apply workload scaling recommendations.                               | Datadog Admin Role     |
| Workload Scaling Read (Preview)(`orchestration_workload_scaling_read`)              | View workload autoscaling objects and recommendations. Note: This permission is in Preview Mode and will be enforced soon. | Datadog Read Only Role |
| Autoscaling Manage(`orchestration_autoscaling_manage`)                              | Manage autoscaling cluster level configuration.                                                                            | Datadog Admin Role     |

## Processes{% #processes %}

Find below the list of permissions for the processes assets:

| Name                                                     | Description                                | Default Role           |
| -------------------------------------------------------- | ------------------------------------------ | ---------------------- |
| Processes Generate Metrics(`processes_generate_metrics`) | Create custom metrics from processes.      | Datadog Standard Role  |
| Process Tags Read(`process_tags_read`)                   | View Process Tag Rules.                    | Datadog Read Only Role |
| Process Tags Write(`process_tags_write`)                 | Create, edit and delete Process Tag Rules. | Datadog Standard Role  |

## Product Analytics{% #product-analytics %}

Find below the list of permissions for the product analytics assets:

| Name                                                                   | Description                                                                                                   | Default Role           |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Profiles Read(`audience_management_read`)                              | View Audience Management data.                                                                                | Datadog Read Only Role |
| Profiles Write(`audience_management_write`)                            | Modify Audience Management data.                                                                              | Datadog Standard Role  |
| Product Analytics Apps Write (Preview)(`product_analytics_apps_write`) | Configure Product Analytics applications. Note: This permission is in Preview Mode and will be enforced soon. | Datadog Standard Role  |

## Real User Monitoring{% #real-user-monitoring %}

Find below the list of permissions for the real user monitoring assets:

| Name                                                        | Description                                                                                                                                                                                               | Default Role           |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| RUM Apps Write(`rum_apps_write`)                            | Create, edit, and delete RUM applications. Creating a RUM application automatically generates a Client Token. In order to create Client Tokens directly, a user needs the Client Tokens Write permission. | Datadog Standard Role  |
| RUM Apps Read(`rum_apps_read`)                              | View RUM Applications data.                                                                                                                                                                               | Datadog Read Only Role |
| RUM Session Replay Read(`rum_session_replay_read`)          | View Session Replays.                                                                                                                                                                                     | Datadog Read Only Role |
| RUM Generate Metrics(`rum_generate_metrics`)                | Create custom metrics from RUM events.                                                                                                                                                                    | Datadog Standard Role  |
| RUM Delete Data(`rum_delete_data`)                          | Delete data from RUM.                                                                                                                                                                                     | Datadog Admin Role     |
| RUM Playlist Write(`rum_playlist_write`)                    | Create, update, and delete RUM playlists. Add and remove sessions from RUM playlists.                                                                                                                     | Datadog Standard Role  |
| RUM Session Replay Extend Retention(`rum_extend_retention`) | Extend the retention of Session Replays.                                                                                                                                                                  | Datadog Admin Role     |
| RUM Retention Filters Read(`rum_retention_filters_read`)    | View RUM Retention filters data.                                                                                                                                                                          | Datadog Read Only Role |
| RUM Retention Filters Write(`rum_retention_filters_write`)  | Write RUM Retention filters.                                                                                                                                                                              | Datadog Standard Role  |
| RUM Settings Write(`rum_settings_write`)                    | Write RUM Settings.                                                                                                                                                                                       | Datadog Admin Role     |

## Reference Tables{% #reference-tables %}

Find below the list of permissions for the reference tables assets:

| Name                                             | Description                        | Default Role           |
| ------------------------------------------------ | ---------------------------------- | ---------------------- |
| Reference Tables Write(`reference_tables_write`) | Create or modify Reference Tables. | Datadog Standard Role  |
| Reference Tables Read(`reference_tables_read`)   | View Reference Tables.             | Datadog Read Only Role |

## Serverless{% #serverless %}

Find below the list of permissions for the serverless assets:

| Name                                                                         | Description                                                                            | Default Role           |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------- |
| Serverless AWS Instrumentation Read(`serverless_aws_instrumentation_read`)   | View remote instrumentation configuration for serverless workloads.                    | Datadog Read Only Role |
| Serverless AWS Instrumentation Write(`serverless_aws_instrumentation_write`) | Add, update, and remove remote instrumentation configuration for serverless workloads. | Datadog Admin Role     |

## Service Level Objectives{% #service-level-objectives %}

Find below the list of permissions for the service level objectives assets:

| Name                                        | Description                                                                                                                                                      | Default Role           |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| SLOs Read(`slos_read`)                      | View SLOs and status corrections.                                                                                                                                | Datadog Read Only Role |
| SLOs Write(`slos_write`)                    | Create, edit, and delete SLOs.                                                                                                                                   | Datadog Standard Role  |
| SLOs Status Corrections(`slos_corrections`) | Apply, edit, and delete SLO status corrections. A user with this permission can make status corrections, even if they do not have permission to edit those SLOs. | Datadog Standard Role  |

## Sheets{% #sheets %}

Find below the list of permissions for the sheets assets:

| Name                         | Description               | Default Role           |
| ---------------------------- | ------------------------- | ---------------------- |
| Sheets Read(`sheets_read`)   | View Sheets.              | Datadog Read Only Role |
| Sheets Write(`sheets_write`) | Create and change Sheets. | Datadog Standard Role  |

## Software Delivery{% #software-delivery %}

Find below the list of permissions for the software delivery assets:

| Name                                                                 | Description                                                                                                            | Default Role           |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| CI Visibility Read(`ci_visibility_read`)                             | View CI Visibility.                                                                                                    | Datadog Read Only Role |
| CI Visibility Tests Write(`ci_visibility_write`)                     | Edit flaky tests and delete Test Services.                                                                             | Datadog Standard Role  |
| CI Provider Settings Write(`ci_provider_settings_write`)             | Edit CI Provider settings. Manage GitHub accounts and repositories for enabling CI Visibility and job logs collection. | Datadog Admin Role     |
| CI Visibility Settings Write(`ci_visibility_settings_write`)         | Configure CI Visibility settings. Set a repository default branch, enable GitHub comments, and delete test services.   | Datadog Standard Role  |
| CI Visibility Ingestion Control Write(`ci_ingestion_control_write`)  | Edit CI Ingestion Control exclusion filters.                                                                           | Datadog Admin Role     |
| CI Visibility Pipelines Write(`ci_visibility_pipelines_write`)       | Create CI Visibility pipeline spans using the API.                                                                     | Datadog Standard Role  |
| PR Gate Rules Read(`quality_gate_rules_read`)                        | View PR Gate Rules.                                                                                                    | Datadog Read Only Role |
| PR Gate Rules Write(`quality_gate_rules_write`)                      | Edit PR Gate Rules.                                                                                                    | Datadog Admin Role     |
| Static Analysis Settings Write(`static_analysis_settings_write`)     | Edit Static Analysis settings.                                                                                         | Datadog Admin Role     |
| CD Visibility Read(`cd_visibility_read`)                             | View CD Visibility.                                                                                                    | Datadog Read Only Role |
| DORA Settings Write(`dora_settings_write`)                           | Edit the settings for DORA.                                                                                            | Datadog Standard Role  |
| Code Analysis Read(`code_analysis_read`)                             | View Code Analysis.                                                                                                    | Datadog Read Only Role |
| Quality Gates Evaluations(`quality_gates_evaluations_read`)          | Allow quality gates evaluations.                                                                                       | Datadog Read Only Role |
| Test Optimization Read(`test_optimization_read`)                     | View Test Optimization.                                                                                                | Datadog Read Only Role |
| Test Optimization Write(`test_optimization_write`)                   | Manage flaky tests for Test Optimization.                                                                              | Datadog Standard Role  |
| Test Optimization Settings Write(`test_optimization_settings_write`) | Create, delete and update Test Optimization settings.                                                                  | Datadog Standard Role  |
| DORA Metrics Read(`dora_metrics_read`)                               | View DORA metrics.                                                                                                     | Datadog Read Only Role |
| Code Coverage read(`code_coverage_read`)                             | View Code Coverage data.                                                                                               | Datadog Read Only Role |
| DORA Metrics Write(`dora_metrics_write`)                             | Edit DORA metrics.                                                                                                     | Datadog Standard Role  |

## Status Pages{% #status-pages %}

Find below the list of permissions for the status pages assets:

| Name                                                       | Description                              | Default Role           |
| ---------------------------------------------------------- | ---------------------------------------- | ---------------------- |
| Status Pages Settings Read(`status_pages_settings_read`)   | View pages and settings in Status Pages. | Datadog Read Only Role |
| Status Pages Settings Write(`status_pages_settings_write`) | Configure page settings in Status Pages. | Datadog Admin Role     |
| Status Pages Notice Write(`status_pages_incident_write`)   | Publish notices in Status Pages.         | Datadog Admin Role     |

## Synthetic Monitoring{% #synthetic-monitoring %}

Find below the list of permissions for the synthetic monitoring assets:

| Name                                                                    | Description                                                                                                 | Default Role           |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------- |
| Synthetics Private Locations Read(`synthetics_private_location_read`)   | View, search, and use Synthetics private locations.                                                         | Datadog Standard Role  |
| Synthetics Private Locations Write(`synthetics_private_location_write`) | Create and delete private locations in addition to having access to the associated installation guidelines. | Datadog Admin Role     |
| Synthetics Global Variable Read(`synthetics_global_variable_read`)      | View, search, and use Synthetics global variables.                                                          | Datadog Standard Role  |
| Synthetics Global Variable Write(`synthetics_global_variable_write`)    | Create, edit, and delete global variables for Synthetics.                                                   | Datadog Standard Role  |
| Synthetics Read(`synthetics_read`)                                      | List and view configured Synthetic tests and test results.                                                  | Datadog Read Only Role |
| Synthetics Write(`synthetics_write`)                                    | Create, edit, and delete Synthetic tests.                                                                   | Datadog Standard Role  |
| Synthetics Default Settings Read(`synthetics_default_settings_read`)    | View the default settings for Synthetic Monitoring.                                                         | Datadog Standard Role  |
| Synthetics Default Settings Write(`synthetics_default_settings_write`)  | Edit the default settings for Synthetic Monitoring.                                                         | Datadog Standard Role  |

## Teams{% #teams %}

Find below the list of permissions for the teams assets:

| Name                         | Description                                                                                                                                               | Default Role          |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Teams Manage(`teams_manage`) | Manage Teams. Create, delete, rename, and edit metadata of all Teams. To control Team membership across all Teams, use the User Access Manage permission. | Datadog Standard Role |

## Watchdog{% #watchdog %}

Find below the list of permissions for the watchdog assets:

| Name                                           | Description             | Default Role          |
| ---------------------------------------------- | ----------------------- | --------------------- |
| Watchdog Alerts Write(`watchdog_alerts_write`) | Manage Watchdog Alerts. | Datadog Standard Role |

## Further reading{% #further-reading %}

- [Learn how to create, update and delete a Role](https://docs.datadoghq.com/account_management/rbac/)
- [Manage your permissions with the Permission API](https://docs.datadoghq.com/api/v2/roles/#list-permissions)
\*Log Rehydration is a trademark of Datadog, Inc.