# Source: https://docs.datadoghq.com/account_management/org_settings/domain_allowlist.md

---
title: Domain Allowlist
description: >-
  Restrict email domains that can receive monitor and scheduled report
  notifications with domain allowlist controls.
breadcrumbs: Docs > Account Management > Domain Allowlist
source_url: https://docs.datadoghq.com/org_settings/domain_allowlist/index.html
---

# Domain Allowlist

{% callout %}
##### Get Started with Domain Allowlist

Domain Allowlist is generally available for customers with Enterprise plans. If you're interested in this feature but are not an Enterprise customer, contact Datadog support.

[Request Access](https://docs.datadoghq.com/help/)
{% /callout %}

With [Domain Allowlist](https://app.datadoghq.com/organization-settings/domain-allowlist), you can restrict the email domains that can receive notifications. The notifications in scope include all notifications from:

- Monitors
- Scheduled Reports
- Events

When Domain Allowlist is enabled, only email domains in your allowlist can receive notifications in scope. If you try to send a notification in scope to an email domain that is not in your allowlist, a warning appears.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/domain_allowlist/verification.6d6db7d593925cb4e72db6fb4d7e25a2.png?auto=format"
   alt="Screenshot of monitor settings in the UI, the 'Notify your team' dialog. The notification mentions a Gmail address, but gmail.com is not in the allowlist. A warning appears, reading 'In message: The email domain @gmail.com is not part of the allowed domain list and will not receive this notification.'" /%}

This document describes how to access and modify your allowlist by using the UI. To use the API instead, see [Domain Allowlist API](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist_api).

## Usage{% #usage %}

Access your [**Domain Allowlist**](https://app.datadoghq.com/organization-settings/domain-allowlist) under **Organization Settings**. To read or edit your Domain Allowlist, you need the **Org Management** permission.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/domain_allowlist/enabled.d82169cb08ec41b000097b036a504c33.png?auto=format"
   alt="Screenshot showing the Domain Allowlist UI, with the allowlist containing one email domain." /%}

The **Domains Currently In Use** section displays the email domains of all emails mentioned in your **monitor** notifications, not including domains in use for other types of notifications. You can still configure sending notifications in scope to email domains that are not in your allowlist, but if Domain Allowlist is enabled, email domains that are not in your allowlist do not receive notifications for the products in scope.

### Enable or disable Domain Allowlist{% #enable-or-disable-domain-allowlist %}

Use the **Enable** or **Disable** button.

To enable Domain Allowlist, you must add one or more domains to the allowlist. If you remove all domains from the allowlist, Domain Allowlist is automatically disabled.

When Domain Allowlist is disabled, all email domains can receive notifications, even if the allowlist contains domains.

### Add or remove a domain{% #add-or-remove-a-domain %}

To add an email domain to the allowlist, enter the domain in the form `@<DOMAIN NAME>.<TOP-LEVEL DOMAIN>`. For example, `@gmail.com`.

To remove a domain from the allowlist, select the delete icon.

## Further Reading{% #further-reading %}

- [Domain Allowlist](https://app.datadoghq.com/organization-settings/domain-allowlist)
- [Domain Allowlist API](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist_api)
