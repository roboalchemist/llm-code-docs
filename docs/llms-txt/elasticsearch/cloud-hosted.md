# Source: https://www.elastic.co/docs/release-notes/cloud-hosted

﻿---
title: Elastic Cloud Hosted release notes
description: Review the changes, fixes, and more in each release of Elastic Cloud Hosted. Enables AWS PrivateLink cross-region support. AWS now supports cross-region...
url: https://www.elastic.co/docs/release-notes/cloud-hosted
products:
  - Elastic Cloud Hosted
---

# Elastic Cloud Hosted release notes
Review the changes, fixes, and more in each release of Elastic Cloud Hosted.
<admonition title="December 2024 and earlier release notes">
  To view release notes from December 2024 and earlier, go to [Elastic Cloud release notes](https://www.elastic.co/guide/en/cloud-hosted/current/ec-release-notes.html).
</admonition>

<changelog>
</changelog>


## October 2025


### Features and enhancements

- **Enables AWS PrivateLink cross-region support.** AWS now supports cross-region PrivateLink, so that your Elastic Cloud deployment can be in a different region than the PrivateLink endpoints or the clients that consume the deployment endpoints. Refer to [Setting up a cross-region PrivateLink connection](https://www.elastic.co/docs/deploy-manage/security/private-connectivity-aws#ec-aws-inter-region-private-link) to learn more.

- **Updates API to record cluster logs on integration test failure.** The Elastic Cloud API now supports downloading cluster logs for all cluster types and not just Elasticsearch clusters.

- **Introduces verification for role mapping configurations as part of Elastic Cloud SAML SSO setup.** Any organization owner role mapping must be verified before saving the configuration to ensure users retain appropriate access after logging in with SAML SSO. You can also use the emulated SAML SSO login flow to test and verify other role mappings to help with the configuration process.


## September 2025


### Fixes

**Reports snapshot estimates using the organization ID.** To better track snapshot storage costs in multi-user organizations, estimates now rely on the organization ID rather than the user ID.

## August 2025


### Features and enhancements

- **Updates the Help popover.** A **Getting started** option is now available in the popover while the **Cloud support** page was removed in favor of `https://support.elastic.co`.

- **Adds configuration for `share.url_expiration.*`.**  Adds the `share.url_expiration.enabled`, `share.url_expiration.duration`, `share.url_expiration.check_interval`, and `share.url_expiration.url_limit` configuration options for controlling how unused URLs are cleaned up.

- **Renames AI4SOC to Elastic AI SOC Engine.** The AI for SOC tier was renamed to Elastic AI SOC Engine (EASE).

- **Adds missing trace context to `/users/auth/methods`.** To enhance APM traces, a missing trace context was added.

- **Change to default endpoint alias behavior.** New deployments that don’t specify an endpoint alias now get a default alias based on the deployment name plus a short random ID (for example, `my-deployment-abc123`). This prevents conflicts when multiple deployments share the same name. It is still possible to define a custom endpoint alias explicitly, but the value must be unique.


## Late July 2025


### Features and enhancements

- **Adds the ability to proxy integrations server instances.** Traffic filter tokens for Kibana are generated to configure agentless in supported versions.

- **Improves IAM endpoints consistency.** Aligning the `SaasUsersRoutes` and `SaasUserRoutes` specifications reduces discrepancies in transaction naming.

- **Adds endpoints to manage role mappings individually.** Roles can now be added, updated, and deleted individually. To delete multiple role mappings simultaneously, specify the roles you want to delete in a comma separated list in the path, for example `DELETE /organizations/{orgid}/role_mappings/role1,role2,role3`.

- **Adds missing tail-based sampling (TBS) configuration.** `apm-server.sampling.tail.storage_limit` and `apm-server.sampling.tail.discard_on_write_failure` are now included in the Elastic APM TBS configuration.

- **Makes Organization IdP routes public.** Organization IdP routes are now public in the OpenAPI specifications.

- **Changes to network security features.** Network security allows you to control how your deployments can be accessed.
  - Features related to network security have been renamed for clarity:
  - **Traffic filtering** is now referred to as network security.
- **Traffic filtering rule sets** are now referred to as network security policies.
- **IP traffic filters** are now referred to as IP filters.
- **Private link traffic filters** are now referred to as private connection policies, and connections over private link are referred to as private connectivity.
- Additional options have been added to allow you to easily review and manage policies and protected resources.


### Fixes

- **Restricts self-service subscription level changes to admin users.** This update disables self-service for subscription level changes in FedRAMP High environments.

- **Response alternative types are now added to the Swagger definition.** When you define an endpoint using an endpoint specification, you might need to map different types of responses it can return. Swagger generation considers only the primary return types and request bodies defined in the endpoint specification and doesn't account for these alternative response types. This change modifies the endpoint specification so that response alternative types are now appended to the model classes list referenced by the Swagger generator.


## Early July 2025


### Features and enhancements

- **Navigation updates:**
  - **Monitoring** in the **Deployment** navigation now combines the previously separate **Health** and **Monitoring** items, for better structure. Select **Monitoring** to go to the health status overview page.
- **Access & Security**, **Extensions**, **Organization**, and **Billing** have been grouped together in the lower part on the navigation, with **Access & Security** expanded by default for easier access, and added icons for each item to aid visual distinction and recognition.

- **Route name added to request logs.**
  Log entries now include the route name as a separate attribute. This attribute reflects the name of the endpoint that handled the request, making it easier to troubleshoot when building dashboards.


## June 2025


### Fixes

- **Compare claimed domains in a case-insensitive way.** When comparing claimed domains for Single Sign-on (SSO) the check is no longer case sensitive.


## Late May 2025


### Features and enhancements

- **AutoOps expanded availability.**
  AutoOps is now available to Elastic Cloud Hosted users in all AWS regions. Check [AutoOps regions](https://www.elastic.co/docs/deploy-manage/monitor/autoops/ec-autoops-regions).


### Fixes

- **Update the override message** The "Override all safety checks" warning message has been expanded for greater clarity.


## Early May 2025


### Features and enhancements

- **Return the invalid characters in the error message** The error response now includes the offending characters when a role mapping contains them.

- **Surface role mapping syntax errors** Improved validation and error handling around role mapping rules


## April 2025


### Features and enhancements

- **AutoOps expanded availability.**
  AutoOps is now available to Elastic Cloud Hosted users in additional AWS regions. Check [AutoOps regions](https://www.elastic.co/docs/deploy-manage/monitor/autoops/ec-autoops-regions).

- **Supports 8.16 for logs shipping.** Support 8.16 for discover link redirection in logs shipping.

- **Removes Enterprise Search from deployment page.** Hides the Enterprise Search link in version 9.

- **Adds support for dots in the role mappings.** Dots (`.`) can be used as part of the role mappings and the groups that are returned by the custom IdPs to match to.

- **Displays error when users try to login, are MFA required but have to active factor.** Users that have SMS only as a multifactor authentication method won't be able to use it.

- **Enables AccountForMemoryUsageByLaunchScripts in production.** Slight tweak of memory settings to improve stability for the smallest containers.


### Fixes

- **SLO: Use groupBy `*` instead of empty string.** Fixes SLO groupBy.

- **Fetches fresh allocator data.** Fetches fresh allocator data every time the instance size override modal is opened to ensure updated data.

- **Max and min validation of sizes in instance configuration should be diferent for storage size.** Fixes a bug where the discrete sizes for an instance configuration using storage as the sizing unit were validated against the limits set for memory. This is now changed to reflect the storage multiplier in use for the instance configuration.

- **Fixes cached errors in upgrade modal.** Suppresses a warning error when we try to upgrade to another version.


## March 2025


### Features and enhancements

- **Upgrades Beats version.** Upgrades metricbeat and filebeat for allocator-metricbeat and beats-runner to version 8.17.2.


### Fixes

- **Fixes an issue with beats-runner 8.17.0 image.** The beats-runner 8.17.0 image could not properly start up beats services due to improper command-line flags.


## February 2025


### Features and enhancements

- **Upcoming removal of SMS multifactor authentication method.** In October, we made multifactor authentication mandatory for all users. As an additional security measure, the SMS MFA method will be removed in April. If you’re still using SMS, you will be prompted to set up a more secure MFA method, and your registered SMS MFA devices will be automatically deleted from Elastic Cloud.


### Fixes

- **Fixes an issue for indices with blocks literally set as `null` instead of `false`.** If an index is created with the literal `null` value rather than `false` for a block in its settings, then that is what Elasticsearch returns even if it should be interpreted as false. With this fix, Elasticsearch Service now properly maps this to false.
- **Disables `prompt=login` and sign out of Okta before initiating SSO.** Fixes an issue when using organization SAML SSO where users are required to re-authenticate with the external IdP due to `ForceAuthn=true` being sent in SAML requests. SAML requests will now send `ForceAuthn=false`.


## January 2025


### Features and enhancements

- **Updates EOL banner.** Updates the informational banner about the deprecation of Enterprise Search.
- **For Fleet, Allows the configuration of `xpack.fleet.enableManagedLogsAndMetricsDataviews`.** Adds the `xpack.fleet.enableManagedLogsAndMetricsDataviews` setting to configure the automatic creation of global dataviews logs-* and metrics-*. (issue: [#202807](https://github.com/elastic/kibana/issues/202807))
- **AutoOps expanded availability.** AutoOps is now available to Elastic Cloud Hosted users in additional AWS regions: Oregon (us-west-2), Ireland (eu-west-1), and Singapore (ap-southeast-1). AutoOps will continue to be deployed to other AWS regions in the coming weeks. To track AutoOps availability, check [AutoOps regions](https://www.elastic.co/docs/deploy-manage/monitor/autoops/ec-autoops-regions).
- **Template Optimizer.** AutoOps now examines both new and updated templates, identifying specific fields that can be optimized for better performance.
- **New Deployment Performance Metrics Charts.** AutoOps provides aggregate metrics at the cluster level for key performance indicators. The data is tier-based, offering users a comprehensive understanding of each tier and the entire cluster.
- **Passthrough hosted otel bound firehose requests.** Passthrough hotel bound firehose requests and avoid processing by the proxy’s firehose middleware.
- **Deprecate Cloud Defend billing alerts.** Following the deprecation of Cloud Defend in Serverless, removes the billing logic associated with the feature.
- **AutoOps shards view improvements.** Improved navigation include a new time slider, ability to filter nodes by tier, and revised color schema.
- **AutoOps feedback button.** A new feedback button has been introduced, allowing users to easily share their thoughts and suggest ideas for improvement.


### Fixes

- **Add the field dry_run to the rest of stateless components.** Adds the field `dry_run` to stateless components in the response of the endpoint `GET api/v1/deployments/{DEPLOYMENT_ID}`. Also removes a check in the UI that is no longer required.
- **Bulk item level failures are treated as successfully delivered.** Check the response body for bulk item level failures even when the HTTP request returns 200 from Elasticsearch. (issue: [#11768](https://github.com/elastic/kibana/issues/11768))