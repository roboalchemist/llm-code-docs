# Source: https://docs.datadoghq.com/incident_response/incident_management/integrations/status_pages.md

# Source: https://docs.datadoghq.com/incident_response/status_pages.md

---
title: Status Pages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > Status Pages
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
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/shopist_status_page2.dbd4b0ef6089c9110a1e08a0f868aab4.png?auto=format"
   alt="Example status page showing service components with their current status and recent incident updates" /%}

Status Pages is part of Datadog's Incident Response suite, alongside On-Call and Incident Management. It lets your team proactively communicate **service availability**, **incidents**, and **planned maintenance** with customers or internal stakeholders through a shareable web page.

Use Status Pages to:

- Share the availability of critical systems and features
- Communicate service disruptions clearly during incidents
- Announce scheduled maintenance and planned downtime in advance
- Reduce inbound support volume with proactive email notifications

## Configure permissions{% #configure-permissions %}

There are three RBAC permissions that are relevant to Status Pages. Users with the Datadog Admin Role have all the necessary permissions.

To create, update, or publish Status Pages, you must have `status_pages_settings_read`, `status_pages_settings_write`, and `status_pages_incident_write` RBAC permissions. For more information, see [Access Control](https://docs.datadoghq.com/account_management/rbac/).

| Name                                                   | Description                                                                                                         | Default Role           |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Status Pages Settings Readstatus_pages_settings_read   | View the list of Status Pages, the settings of each Status Page, their Notices, and launched Internal Status Pages. | Datadog Read Only Role |
| Status Pages Settings Writestatus_pages_settings_write | Create and launch new Status Pages, and configure Status Pages settings.                                            | Datadog Admin Role     |
| Status Pages Notice Writestatus_pages_incident_write   | Publish and update Incidents.                                                                                       | Datadog Admin Role     |

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

You can add components to your status page either on initial setup or through the status page settings:

1. From your status page, click **Settings** and select the **Components** tab.
1. Create individual components or a group of related components. You can associate notices with these components to reflect impact on your status page.
1. Select a visualization type:
   1. Bars and Uptime Percentage
   1. Bars Only
   1. Component Name Only

### Component hierarchy{% #component-hierarchy %}

If multiple notices affect the same component, the notice with the greatest impact takes precedence: Major Outage > Partial Outage > Degraded Performance > Maintenance > Operational

## Publish your status page{% #publish-your-status-page %}

After you save your status page settings, click **Launch Status Page** to make the page available at its URL.

If you selected:

- **Public**, the page is immediately accessible to all visitors.
- **Internal**, access is limited to authenticated Datadog users in your organization.

## Add a notice{% #add-a-notice %}

Notices are messages published to a status page to communicate system status. Status Pages support two types of notices: **degradations** for unplanned service impact and **maintenance windows** for planned downtime.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/select_notice_type_status_page.02deb3be62eef0ce4233a921105a84f1.png?auto=format"
   alt="Status page notice type selector with degradation and scheduled maintenance options" /%}

### Publish a degradation{% #publish-a-degradation %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/shopist_status_page_degradations.6c547d25759dc798b93a5e2756944d9a.png?auto=format"
   alt="Example status page showing service components experience degradation" /%}

Degradation notices communicate **unplanned service impact**, such as incidents or service disruptions. Use degradation notices to keep users informed as an issue is investigated, mitigated, and resolved.

From a status page, click **Publish Notice** and select **Degradation**, then provide:

| Field                   | Description                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| **Notice title**        | Short, clear description of the issue*Example: Increased error rates in US region*                       |
| **Status**              | Current state of the issue:- Investigating- Identified- Monitoring- Resolved                             |
| **Message**             | Additional details for your users*Example: We are aware of the issue and are actively working on a fix.* |
| **Components impacted** | One or more components affected by the degradation                                                       |
| **Impact**              | Impact level per component:- Operational- Degraded Performance- Partial Outage- Major Outage             |
| **Notify subscribers**  | Toggle to send updates to subscribed users                                                               |

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/publish_status_page_degradation.4f77bc188dfffdc29b576ff2f75aa068.png?auto=format"
   alt="Example publish notice modal for degradations" /%}

After a degradation notice is reviewed and published, it:

- Appears on the **Status Pages List** under Active Notices.
- Updates the uptime bars for impacted components.
- Is visible in the notice history timeline.

You can publish updates over time and mark the notice as **Resolved** when the issue is fully mitigated.

### Schedule a maintenance window{% #schedule-a-maintenance-window %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/shopist_maintenance_example.986133754af461c3e4f5df00f37613ce.png?auto=format"
   alt="Example status page showing service components undergoing maintenance" /%}

Maintenance windows allow you to proactively communicate planned downtime or service impact before it happens. Unlike degradations which are used for unplanned incidents, maintenance windows are scheduled in advance for infrastructure upgrades, system maintenance, database migrations, and other planned work. This allows you to keep customers informed and reduce support volume.

From the status page, click **Schedule Maintenance**, or click **Publish Notice** and select **Scheduled Maintenance**. Then, provide the following details:

| Field                   | Description                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------- |
| **Notice title**        | Clear description of the maintenance activity*Example: Database infrastructure upgrade* |
| **Maintenance window**  | Scheduled start and end time for the maintenance                                        |
| **Messages**            | Messages that are automatically published as the maintenance progresses                 |
| **Components impacted** | Components affected during the maintenance window                                       |
| **Notify subscribers**  | Toggle to send advance notification to subscribers                                      |

{% image
   source="https://datadog-docs.imgix.net/images/service_management/status_pages/publish_status_page_maintenance.774ab646b9f05beaee7d2b43a123c34c.png?auto=format"
   alt="Example publish notice modal for maintenance windows" /%}

After reviewing and scheduling, the maintenance window:

- Appears under **Upcoming Maintenance** on the status page
- Automatically updates component status to **Maintenance** when the window begins
- Returns components to **Operational** when the window ends (unless manually overridden)

You can post updates if plans change or reschedule the maintenance window as needed.

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
