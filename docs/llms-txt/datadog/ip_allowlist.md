# Source: https://docs.datadoghq.com/account_management/org_settings/ip_allowlist.md

---
title: IP Allowlist
description: >-
  Control network access to Datadog by restricting API and UI access to specific
  IP addresses or CIDR ranges for enterprise security.
breadcrumbs: Docs > Account Management > IP Allowlist
---

# IP Allowlist

{% callout %}
##### Get Started with IP Allowlist

The IP allowlist feature is available for customers on an enterprise plan only. Request access by contacting support.

[Request Access](https://docs.datadoghq.com/help/)
{% /callout %}

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/ip_allowlist_list.04dc53f1b42307558e88bbd2b91de9fb.png?auto=format"
   alt="Screenshot showing the IP allowlist UI, containing four IP ranges" /%}

The IP allowlist controls which networks can be used to access your data in Datadog. By limiting allowed networks, you can protect your resources from data exfiltration and insider threats.

When the IP allowlist is enabled, only IP addresses or CIDR ranges in the allowlist can access the Datadog API and UI.

### Blocked and allowed resources{% #blocked-and-allowed-resources %}

If a user's IP is not contained in the IP allowlist, they are effectively blocked from accessing and using:

- Datadog's web UI
- Datadog's public [API](https://docs.datadoghq.com/api/latest/), including both documented and unpublished endpoints
- Datadog's mobile apps (iOS, Android)
- Third-party integrations and applications that access Datadog through OAuth

The IP allowlist feature does not block access to the following:

- Data ingest endpoints to which the Agent sends data, such as metrics, traces, and logs
- The [validate API key](https://docs.datadoghq.com/api/latest/authentication/#validate-api-key) endpoint, which the Agent uses before submitting data
- [Agent flare submission](https://docs.datadoghq.com/agent/troubleshooting/send_a_flare/)
- [Public dashboards](https://docs.datadoghq.com/dashboards/sharing/)

Applications and integrations that submit telemetry from the Agent (metrics, traces, and logs), and those that use an API key provided by the user, are not impacted by the IP allowlist. Datadog recommends utilizing the [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/) to monitor for IP addresses from third party applications and integrations.

To allow mobile app clients to connect to Datadog when the IP allowlist feature is enabled, Datadog recommends that the mobile devices connect to an allowed network range via VPN.

### Functionality{% #functionality %}

Only users with the **Org Management** permission can configure the IP allowlist.

With the IP allowlist API or UI, you can:

- Check the status of the IP allowlist. Whether the IP allowlist is on or off determines whether your organization is restricting requests by IP address allowlist membership.
- Turn the IP allowlist on and off.
- Show the IP addresses (as CIDR ranges) that are covered by your IP allowlist.
- Add IP addresses (IPv4 or IPv6) or CIDR ranges to the IP allowlist with an optional note.
- Edit the note for an IP address already in the IP allowlist.
- Delete a single entry from the IP allowlist.
- Replace the whole IP allowlist with new entries (only available through the API).

### Lockout prevention{% #lockout-prevention %}

When you enable or modify the IP allowlist, the system enforces constraints to make sure you can still access your data:

- At least one entry in the IP allowlist contains your current IP
- The allowlist contains at least one entry

## Managing the IP allowlist in the UI{% #managing-the-ip-allowlist-in-the-ui %}

**Note:** The IP allowlist page only appears in the UI if your Datadog organization has the feature turned on.

To find the [IP allowlist UI](https://app.datadoghq.com/organization-settings/ip-allowlist):

1. Navigate to **Organization Settings** from your account menu.
1. Under **Security**, select **IP Allowlist**.

The IP allowlist table lists the CIDR ranges contained in the IP allowlist.

### Enable and disable the IP allowlist{% #enable-and-disable-the-ip-allowlist %}

A banner at the top of the page shows the enabled or disabled status of the IP allowlist. It also shows your IP and whether that IP is in the allowlist.

To toggle the IP allowlist status, click the **Enable** or **Disable** button.

### Add IP addresses or CIDR ranges{% #add-ip-addresses-or-cidr-ranges %}

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/add_ip_2.507ace2d58fa261b0062bc35c24f0bab.png?auto=format"
   alt="Screenshot showing a dialog box titled Add IP to allowlist" /%}

1. Click the **Add IP** button at the top right of the page.
1. Enter a valid IP address or CIDR range.
1. Optionally, add a note, for example, to remind yourself why you are allowing access to certain addresses.
1. Click **Confirm**.

### Edit IP addresses or CIDR ranges{% #edit-ip-addresses-or-cidr-ranges %}

1. In the IP allowlist table, hover over the row you wish to edit.
1. Click the pencil (**Edit**) icon.
1. Change the descriptive **Note** text.
1. Click **Confirm**.

### Delete IP addresses or CIDR ranges{% #delete-ip-addresses-or-cidr-ranges %}

1. In the IP allowlist table, hover over the row you wish to delete.
1. Click the trash can (**Delete**) icon and confirm you want to delete it.

## Managing the IP allowlist programmatically{% #managing-the-ip-allowlist-programmatically %}

To manage the IP allowlist through the API, see the [IP Allowlist API documentation](https://docs.datadoghq.com/api/latest/ip-allowlist/).

See the [`ip_allowlist` resource](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/ip_allowlist) to manage the IP allowlist in Terraform.
