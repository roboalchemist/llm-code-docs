# Source: https://docs.datadoghq.com/incident_response/status_pages.md

---
title: Status Pages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Status Pages
source_url: https://docs.datadoghq.com/status_pages/index.html
---

# Status Pages

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/shopist_status_page.7d7820a094382955da89d3e1e5dc7702.png?auto=format"
   alt="Example status page showing service components with their current status and recent incident updates" /%}

Status Pages is part of Datadog's Incident Response suite, alongside On-Call and Incident Management. It lets your team proactively communicate **service availability** and **incidents** with customers or internal stakeholders through a shareable web page.

Use Status Pages to:

- Share the availability of critical systems and features
- Communicate service disruptions clearly during incidents
- Reduce inbound support volume with proactive email notifications

## Configure permissions{% #configure-permissions %}

There are three RBAC permissions that are relevant to Status Pages. Users with the Datadog Admin Role have all the necessary permissions.

To create, update, or publish Status Pages, you must have `status_pages_settings_read`, `status_pages_settings_write`, and `status_pages_incident_write` RBAC permissions. For more information, see [Access Control](https://docs.datadoghq.com/account_management/rbac/).

| Name                                                   | Description                                                                                                            | Default Role           |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Status Pages Settings Readstatus_pages_settings_read   | View the list of Status Pages, the settings of each Status Pages, their Incidents, and launched Internal Status Pages. | Datadog Read Only Role |
| Status Pages Settings Writestatus_pages_settings_write | Create and launch new Status Pages, and configure Status Pages settings.                                               | Datadog Admin Role     |
| Status Pages Notice Writestatus_pages_incident_write   | Publish and update Incidents.                                                                                          | Datadog Admin Role     |

## Create a status page{% #create-a-status-page %}

1. In Datadog, navigate to [**Status Pages**](https://app.datadoghq.com/status-pages).
1. Click **Create Status Page** and follow the onboarding flow:
| Field                                                         | Description                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Status Page Type**                                          | Choose who can access the page:- **Public** - Anyone with the link can view- **Internal** - Only authenticated users within your Datadog organization can view                                                                                                                                               |
| **Page name**                                                 | Displayed as the page header (if no logo is uploaded).*Example: Acme Cloud Platform*                                                                                                                                                                                                                         |
| **Domain Prefix**                                             | Used as your status page subdomain prefix. For more information on custom domains, see the Set a custom domain section.*Example: shopist â shopist.statuspage.datadoghq.com*- Must be **globally unique**- Lowercase, alphanumeric, and hyphenated- May affect links if changed later                        |
| **Subscriptions** *(optional)*                                | Enable users to receive email notifications about status page updates. When subscriptions are enabled, users can sign up to get notified about new notices and updates. You can turn subscriptions on or off for each status page. **Note**: Email subscriptions are double opt-in, email must be confirmed. |
| **Company logo, Favicon, or Email Header Image** *(optional)* | Upload a logo, favicon, or image to personalize the appearance of your status page and email notifications.                                                                                                                                                                                                  |
1. (Optional) Add components to show the status of individual services.
1. Click **Save Settings**.Important alert (level: info): A status page **is not Live** after you save your settings. To make the page available, publish your status page.

## Add components{% #add-components %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/status_page_components.7b3663dd5cd28e954b7fc23a283f5b9c.png?auto=format"
   alt="Status page component configuration with live preview panel" /%}

Components are the building blocks of your status page. Each one represents a service or feature your users care about. Some examples of components include:

- API Gateway
- Web Dashboard
- Database Cluster
- US Region Services

You can add components to your status page either on intial setup or through the status page settings:

1. From your status page, click **Settings** and select the **Components** tab.
1. Create individual components or a group of related components. You can associate notices with these components to reflect impact on your status page.
1. Select a visualization type:
   1. Bars and Uptime Percentage
   1. Bars Only
   1. Component Name Only

## Publish your status page{% #publish-your-status-page %}

After you save your status page settings, click **Launch Status Page** to make the page available at its URL.

If you selected:

- **Public**, the page is immediately accessible to all visitors.
- **Internal**, access is limited to authenticated Datadog users in your organization.

## Add a notice{% #add-a-notice %}

Notices on Status Pages are carefully crafted messages posted to a public website to communicate system status. When an issue arises, you can communicate it clearly through your status page.

1. From a status page, click **Publish Notice** to open a "Publish Status Page Notice" modal and provide:
| Field                    | Description                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| **Title**                | Short, clear description of the incident*Example: Increased error rates on US region*           |
| **Status**               | Current state of the incident:- Investigating- Identified- Monitoring- Resolved                 |
| **Message** *(optional)* | Additional details for your users*Examples: known cause, expected resolution time*              |
| **Components impacted**  | One or more components impacted by the incident                                                 |
| **Impact**               | Level of impact per component:- Operational- Degraded Performance- Partial Outage- Major Outage |
| **Notify Subscribers**   | Toggle to send the notice to subscribers                                                        |
1. Click **Publish Notice**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/publish_status_page_incident_1.74ee82bdfac1abc227d0292e2b84c354.png?auto=format"
   alt="Screenshot of the Status Page Notice creation modal with fields filled out" /%}

After a notice is published, the notice:

- Appears on the Status Pages List under **Active Notices**.
- Updates the uptime bars for impacted components.
- Is visible in the notice history timeline.

You can post **updates** over time to keep users informed, and then mark the notice as **Resolved**.

## Email subscriptions{% #email-subscriptions %}

Email subscriptions on status pages are **double opt-in**. After entering an email to subscribe, users receive a confirmation email and must click the confirmation link to activate their subscription. During this process, users can choose to receive notifications for the entire status page or select specific components they want to monitor. Users can manage their preferences and update their subscriptions at any time through the subscription management link included in notification emails.

For **internal** status pages, the subscription process is the same, but users must log in to the same Datadog organization to confirm their subscription and receive notifications.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/status_pages_subscription.ebadf5007b15579ebf177ffd2e1f630f.png?auto=format"
   alt="Screenshot of the Status Page subscription modal with fields filled out" /%}

## Set a custom domain{% #set-a-custom-domain %}

To match your branding, you have the option to map your status page to a custom domain like `status.acme.com`.

1. From your status page, click **Settings**.
1. Select **Custom Domain**.
1. Follow the instructions to enter your domain and add DNS records.
1. Datadog automatically detects the DNS configuration and provisions an SSL certificate.

{% alert level="warning" %}
Custom domains require access to your DNS provider to add a CNAME or A record.
{% /alert %}

**Note**:

- DNS propagation may take several minutes.
- You can revert to the default Datadog domain at any time.
- Ensure DNS changes are made by someone with access to your domain registrar.

## Further reading{% #further-reading %}

- [Keep stakeholders informed with Datadog Status Pages](https://www.datadoghq.com/blog/status-pages)
- [Learn more about Incident Management](https://docs.datadoghq.com/incident_response/incident_management/)
- [Learn more about On-Call Scheduling](https://docs.datadoghq.com/incident_response/on-call/)
- [Integrate Datadog Status Pages with Incident Management](https://docs.datadoghq.com/incident_response/incident_management/integrations/status_pages)
- [Keep stakeholders informed with Datadog Status Pages](https://www.datadoghq.com/blog/status-pages/)
