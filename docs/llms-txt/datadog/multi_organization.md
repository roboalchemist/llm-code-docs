# Source: https://docs.datadoghq.com/account_management/multi_organization.md

---
title: Managing Multiple-Organization Accounts
description: >-
  Manage multiple child organizations from a parent account with separate
  billing, usage tracking, and access control for managed service providers.
breadcrumbs: Docs > Account Management > Managing Multiple-Organization Accounts
---

# Managing Multiple-Organization Accounts

## Overview{% #overview %}

It is possible to manage multiple child-organizations from one parent-organization account. This is typically used by managed service providers that have customers which should not have access to each others' data.

The multi-organization account feature is not enabled by default. Contact [Datadog support](https://docs.datadoghq.com/help/) to have it enabled.

## Capabilities{% #capabilities %}

Users can be added to the parent-organization and multiple child-organizations. Users switch between organizations from the [user account settings menu](https://docs.datadoghq.com/account_management/#managing-your-organizations).

Organizations within a parent organization do not have access to each other's data. To enable cross-organization metric queries, see [cross-organization visibility](https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility/).

The parent-organization can view the usage of individual child-organizations, allowing the parent to track usage trends.

Account settings, such as allow-listed IP addresses, are not inherited by child-organizations from their parent-organization.

## Child organizations{% #child-organizations %}

### Create{% #create %}

1. After the feature is enabled, see the [New Organization Page](https://app.datadoghq.com/account/new_org).
1. Enter the name of the child-organization you wish to create. **The child-organization name cannot exceed 32 characters.**
1. Optionally, invite admin users to your child-organization:
   - Enter one or more email addresses.
   - Invited users are assigned the [Datadog Admin role](https://docs.datadoghq.com/account_management/rbac/permissions/#advanced-permissions). You can invite more users in Organization Settings after creating your organization.
   - If the user does not have a password, Datadog sends an email invitation with a link to set a password and join the new child-organization.
1. Click **Create**.

The new child-organization inherits the parent-organization's plan and is added to the parent-organization's billing account. If you want to update the child-organization's billing, [contact your sales representative](mailto:success@datadoghq.com).

### Content{% #content %}

Onboarding a new sub-organization with a set of baseline dashboards and monitors can be done programmatically with the [Datadog API](https://docs.datadoghq.com/api/) and tools such as Terraform, see [Managing Datadog with Terraform](https://www.datadoghq.com/blog/managing-datadog-with-terraform). Additionally, scripts can be used to backup existing dashboards and [monitors](https://docs.datadoghq.com/monitors/manage/) as code.

### Custom sub-domains{% #custom-sub-domains %}

The custom sub-domain feature is not enabled by default. Contact [Datadog support](https://docs.datadoghq.com/help/) to have it enabled.

If you are a member of multiple organizations, custom sub-domains help you identify the source of an alert or notification. Also, they can immediately switch you to the organization associated with the sub-domain.

For example, the URL **https:/event/event?id=1** is associated with an event in Organization A. If a user is a member of both Organization A and Organization B, but is viewing Datadog within the context of Organization B, then that URL returns a `404 Not Found error`. The user must switch to Organization A using the [user account settings menu](https://docs.datadoghq.com/account_management/#managing-your-organizations), then revisit the URL. However, with custom sub-domains, the user could navigate to **https://org-a.
{% user-datadog-site /%}
/event/event?id=1** which would automatically switch the user's context to Organization A and display the correct page.

**Note**: If you have a custom Datadog subdomain, manually edit the links from the Datadog documentation with your subdomain name. For example, a link redirecting to **https:/account/settings** becomes **https://<custom\_sub-domain\_name>.
{% user-datadog-site /%}
/account/settings**.

## Set up SAML{% #set-up-saml %}

SAML setup is *not* inherited by child-organizations from the parent-organization. SAML must be configured for each child-organization individually.

To configure SAML for multi-organizations:

1. Create a new organization.
1. Invite SAML users.
1. Login as a SAML user and [set up SAML](https://docs.datadoghq.com/account_management/saml/).

### SAML strict parent organizations{% #saml-strict-parent-organizations %}

Under some circumstances, you may be unable to access a newly created child organization. When an organization requires users to log in using SAML, its user accounts may lack passwords. Since child organizations do not inherit SAML settings from their parents, logging into the child organization requires a password that does not exist.

To ensure that you can log into a child organization created from a SAML strict parent organization, take the following steps in the parent organization:

1. Click **Organization Settings** from the account menu in the bottom of the left side navigation, or select **Organization Settings** from the header dropdown at the top of the Personal Settings page.
1. In the left page menu, select **Users**.
1. Select your user profile.
1. Set the **Override Default Login Methods** toggle to the on position.
1. Under **Select user's login methods**, place a checkmark in the **Password** checkbox.
1. Ensure your account has a password. If you need help setting a password, contact [Datadog support](https://docs.datadoghq.com/help/).

Following the steps above ensures that you can log into the parent account using an email and password combination. After creating your child organization, you can also log into it using your email and password.

If you already created the child organization and are locked out, following the procedure allows you to log in.

## Multi-org usage{% #multi-org-usage %}

The parent-organization can view the total and billable usage of all their organizations (child and parent organizations) by hovering over their username on the bottom left corner and navigating to [**Plan & Usage** > **Usage & Cost**](https://app.datadoghq.com/billing/usage?cost_summary).

The Usage page shows the aggregate usage of the parent-organization and all its child-organizations. There are two tabs on the Usage page:

- Overall
- Individual Organizations

### Overall usage{% #overall-usage %}

This tab contains a Month-to-Date Total Usage section and an Overall Usage section.

The Month-to-Date Total Usage section summarizes your month-to-date usage of hosts, containers, custom metrics, and any other part of the platform you've used during the month, across your parent-organization and all its child-organizations.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/multi-org-v2.0e8130579fada75643c86f9e18bcedc3.png?auto=format"
   alt="Month-to-Date Usage" /%}

Most accounts by default can view "Billable" usage, which shows usage that contributes to your final bill. This view also breaks out on-demand usage above your commitments and allocations. The "All" view shows you all usage, including non-billable usage such as product trials.

The Overall Usage section shows the monthly aggregate usage across all organizations over the past 6 months. The usage shown here is "All" usage not "Billable" usage, which means it does not adjust for trial periods or other billing changes used to calculate your final bill. This information can be downloaded as a CSV file.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/multi-org-v2-trends.0f0d54e091f97d6bc703cd30c990796e.png?auto=format"
   alt="Overall Usage Long-term trends" /%}

Both the Month-to-Date Total Usage section and the Overall Usage section can be filtered by clicking on product specific sub-tabs. In the "Log Management" sub-tab, you can view the Logs Usage by Index table, which displays your month-to-date and last month's indexed log usage by:

- Index name
- Organization
- Retention period in days
- Indexed log count broken down between live and rehydrated logs
- The index's contribution percentage to the overall indexed log usage

This data can be downloaded as a CSV file.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/multi-org-v2-logs-by-index.a6a87c018324e2a69a500f97dced681c.png?auto=format"
   alt="Multi-org Logs Usage by Index" /%}

### Individual organization usage{% #individual-organization-usage %}

On the **Individual Organizations** usage tab, you can view the usage of your child organizations in absolute units or as a percentage of total usage.

The default view is the "Billable" view, which shows usage that contributes to your final bill. This view removes child organizations that are not billable such as trial organizations, and other adjustments that provide a more accurate summary of what drives your bill. Switch to the "All" view to see the unadjusted, raw usage of your parent-organization and all child-organizations. Both views can be downloaded as a CSV file.

To view the [Usage Details](https://docs.datadoghq.com/account_management/plan_and_usage/usage_details/) of a child-organization, you can click on the child-organization's name.

## Usage attribution{% #usage-attribution %}

The parent-organization can view the usage of child-organizations by existing tag keys in the [Usage Attribution](https://docs.datadoghq.com/account_management/billing/usage_attribution/) page. Admins can hover over their username at the bottom left, then navigate to: [**Plan & Usage > Usage Attribution**](https://app.datadoghq.com/billing/usage-attribution).

When enabled at the parent-organization level, usage attribution shows usage aggregated across all organizations. This can be useful if you would like to attribute the usage of your child-organizations to certain projects, teams, or other groupings.

Functionalities include:

- Changing and adding new tag keys (up to three).
- Accessing monthly usage in both the UI and as a .tsv download (tab separated values)
- Accessing daily usage in a .tsv file for most usage types.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/usage_attribution/Usage-Attribution-Monthly-Facets.16ffd9066008bae5047c6283455de25d.png?auto=format"
   alt="Monthly Usage Attribution Report" /%}

Usage attribution can also be enabled at the child-organization level. When enabled at this level, the tags are only applied to that specific child-organization and can only be viewed in that child-organization. Tags applied at the child-organization level do not rollup and cannot be viewed in the parent-organization.

Usage Attribution is an advanced feature included in the Enterprise plan. For all other plans, contact your account representative or [success@datadoghq.com](mailto:success@datadoghq.com).

## Further Reading{% #further-reading %}

- [Best practices for managing Datadog organizations at scale](https://docs.datadoghq.com/account_management/multi_organization/)
- [Configure SAML for your Datadog account](https://docs.datadoghq.com/account_management/saml/)
- [Learn about Usage Details](https://docs.datadoghq.com/account_management/billing/usage_details)
- [Set-up Usage Attribution](https://docs.datadoghq.com/account_management/billing/usage_attribution)
- [Cross-Organization Visibility](https://docs.datadoghq.com/account_management/org_settings/cross_org_visibility)
