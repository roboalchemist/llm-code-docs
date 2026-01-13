# Source: https://docs.datadoghq.com/account_management/guide/manage-datadog-with-terraform.md

---
title: Manage Datadog with Terraform
description: >-
  Use Terraform to manage your Datadog organization, users, roles, teams,
  credentials, and service accounts through infrastructure as code.
breadcrumbs: >-
  Docs > Account Management > Account Management Guides > Manage Datadog with
  Terraform
source_url: https://docs.datadoghq.com/guide/manage-datadog-with-terraform/index.html
---

# Manage Datadog with Terraform

## Overview{% #overview %}

You can use [Terraform](https://www.terraform.io/) to interact with the Datadog API and manage your Datadog organization, child organizations, users, credentials, permissions, and more. This guide provides example use cases for managing Datadog with Terraform, with links to commonly used Datadog resources and data sources in the Terraform registry.

You can also [import](https://developer.hashicorp.com/terraform/cli/import) your existing resources into your Terraform configuration for future management through Terraform, and reference existing resources as Terraform [data sources](https://developer.hashicorp.com/terraform/language/data-sources).

## Setup{% #setup %}

If you haven't already, configure the [Datadog Terraform provider](https://docs.datadoghq.com/integrations/terraform/) to interact with Datadog APIs on your behalf.

## Users, roles, teams, and service accounts{% #users-roles-teams-and-service-accounts %}

The following resources and data sources enable you to follow the security principle of least privilege, providing only the privileges needed for essential activities to the users, teams, and service accounts operating in your Datadog organizations.

### Users{% #users %}

Create your account's [users](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/user) and assign them any of the default or [custom roles](https://docs.datadoghq.com/account_management/rbac/?tab=datadogapplication#custom-roles) available. You can also use the [AuthN mapping](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/authn_mapping) resource to automatically assign roles to users based on their SAML attributes. You can also import your existing users, roles, and AuthN mappings into your Terraform configuration.

The [user data source](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/user) can be used to retrieve information about existing users in your Terraform configuration for use in other resources, such as the Datadog team membership resource.

### Roles{% #roles %}

Datadog provides three managed roles for user permissions, but you can also use the [role resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/role) to create and manage custom roles.

The [role data source](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/role) can be used to retrieve information about existing roles for use in other resources, such as the Datadog user resource.

### Teams{% #teams %}

Use the [Datadog Team](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/team) resource to associate specific resources with a group of users and filter their Datadog experience to prioritize those resources. Manage team membership with the [team membership](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/team_membership) resource, and control who can manage the team with the [team permission setting](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/team_permission_setting) resource.

The [team data source](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/team) and [team memberships data source](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/team_memberships)can be used to retrieve information about existing teams and team memberships, respectively, for use in other resources.

See the [Teams page](https://docs.datadoghq.com/account_management/teams/) for more information.

### Service accounts{% #service-accounts %}

The [service account](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/service_account) resource provides a non-interactive account that can be used to own [service account application keys](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/service_account_application_key) and other resources that are shared across your teams.

The [service account data source](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/service_account) can be used to retrieve information about existing service accounts for use in other resources.

See [Service Accounts](https://docs.datadoghq.com/account_management/org_settings/service_accounts) for more information.

## Credentials{% #credentials %}

### API and app keys{% #api-and-app-keys %}

[API keys](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/api_key) allow for the submission of data to your Datadog account, and [Application keys](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/application_key) allow resources to be created in your Datadog account. You can also import your existing credentials.

The [API key data source](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/api_key) and [application key data source](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/data-sources/application_key) can be used to retrieve information about existing credentials already being managed with Terraform.

## Organizations{% #organizations %}

Organization-level resources provide the ability to manage organization settings for both single-account and multi-account environments.

### Organization settings{% #organization-settings %}

Configure account access and widget sharing capabilities for any of your accounts with the [organization settings](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/organization_settings) resource. For example, you can manage the IdP endpoints, login URLs, and whether or not SAML strict mode is enabled. See [Single Sign On With SAML](https://docs.datadoghq.com/account_management/saml/) for more information.

You can also import your existing organization settings into your Terraform configuration.

### Child organizations{% #child-organizations %}

{% alert level="info" %}
The Multi-organization Account feature is not enabled by default. Contact Datadog support to have it enabled.
{% /alert %}

If you need to maintain separate, isolated environments, you can create [child orgs](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/child_organization) under a main parent org. From the parent account, you can track the usage of any associated sub-accounts, and users with access to multiple orgs can switch between them with a single click.

See [Managing Multiple-Organization Accounts](https://docs.datadoghq.com/account_management/multi_organization/) for more information.

**Note**: Child orgs do not inherit the SAML configurations of the parent org.

## Restriction policies{% #restriction-policies %}

Restriction policies are associated to a specific **resource**, and define the level of access provided to roles, teams, or users. Use the [restriction policy](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/restriction_policy) resource to create and manage your restriction policies, or import your existing restriction policies into your Terraform configuration.

## Further reading{% #further-reading %}

- [Plan and Usage Settings](https://docs.datadoghq.com/account_management/plan_and_usage/)
- [Streamline collaboration throughout your organization with Datadog Teams](https://www.datadoghq.com/blog/datadog-teams/)
