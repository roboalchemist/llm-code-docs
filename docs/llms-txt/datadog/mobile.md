# Source: https://docs.datadoghq.com/mobile.md

---
title: Datadog Mobile App
description: >-
  Monitor your infrastructure on-the-go with the Datadog mobile app for iOS and
  Android, featuring dashboards, alerts, incidents, and on-call management.
breadcrumbs: Docs > Datadog Mobile App
source_url: https://docs.datadoghq.com/index.html
---

# Datadog Mobile App

The Datadog Mobile app enables you to view alerts from Datadog on your mobile device. When receiving an alert through On-Call, Slack, or email, you can investigate issues by opening monitor graphs and dashboards on your mobile device.

## Installing{% #installing %}

Download the app from the [Apple App Store](https://apps.apple.com/app/datadog/id1391380318) for your iOS device, or from the [Google Play store](https://play.google.com/store/apps/details?id=com.datadog.app) for your Android device.

### Logging in{% #logging-in %}

You can log in using standard authentication, Google authentication, or [SAML](https://docs.datadoghq.com/account_management/saml/#pagetitle) - for both the US and the EU region.

#### Enabling SAML{% #enabling-saml %}

SAML login requires you to set up and authenticate your SAML provider with Datadog using your default iOS/Android browser. For SAML IdP-initiated login, refer to the end of this section. To authenticate SAML:

1. In the mobile app, select your data center region (for example, US1) in the upper right corner.
1. Press the log-in button.
1. Click the "Using Single Sign-On (SAML)?" link.
1. Enter your company email and send the email.
1. While on your mobile device, open the email and click on the indicated link through your default browser.
1. Enter your org's SAML credentials to be rerouted to an authenticated session of the Datadog mobile app.

Optionally, you may also authenticate through a QR Code or manual entry, outlined below.

##### QR code{% #qr-code %}

1. In a browser, navigate to your [Datadog account Personal Settings Organizations](https://app.datadoghq.com/personal-settings/organizations) page and click **Log in to Mobile App** for the organization you are currently logged into. This pops up a QR code.
1. Use your default phone camera app to scan the QR code and then tap the suggested link to open the Datadog App. You will be automatically logged in.

**Note**: If you click the **Log in to Mobile App** button of an organization you are not currently logged into, the org UUID is automatically inserted into the login screen. You still have to provide authentication using your standard method.

##### Manual entry{% #manual-entry %}

1. To manually enter the SAML ID, open the Datadog Mobile app and press the "Using Single Sign-On (SAML)?" button.
1. Press the "Use another method to login" button, and enter the SAML ID manually.

By clicking **Authorize** when logging in, you link the mobile device you're using to your account. For security purposes, you will have to go through this flow once per month.

##### SAML IdP initiated login{% #saml-idp-initiated-login %}

If you keep getting errors while trying to login with SAML, your identity provider may enforce IdP-initiated login. For more information regarding enabling IdP initiated SAML, please see our IdP initiated SAML page [IdP Initiated SAML page](https://docs.datadoghq.com/account_management/saml/mobile-idp-login/)

##### Subdomain login{% #subdomain-login %}

1. Tap subdomain and enter your custom [subdomain](https://docs.datadoghq.com/account_management/multi_organization/#custom-sub-domains).
1. Proceed with login steps as prompted.

### Switch organizations{% #switch-organizations %}

To switch organizations, navigate to the **Settings** page on the mobile app and click on **Organization**.

**Note**: You may need to reauthenticate when you switch organizations.

### Log out{% #log-out %}

To log out, navigate to the **Settings** page on the mobile app and click on **Log Out**. Confirm **Yes** that you are sure.

## On-Call{% #on-call %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/on_call_may_2025.611ed0d75670a35b0ade16f52443b8f4.png?auto=format"
   alt="iOS on-call page showing shifts, schedules, and escalation options" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_On_Call.9f6eef88092a4f1647e49d48edaba08c.png?auto=format"
   alt="Android on-call page showing shifts, schedules, and escalation options" /%}

{% /tab %}

The On-Call page provides a comprehensive view of On-Call shifts, schedules, pages, and escalation policies. You can filter the information by user, team, urgency, status, or date to quickly find relevant details. Tapping **Escalate** prompts you to confirm the escalation to the next policy level. Tapping **Declare Incident** prompts you to enter a title and provide relevant incident attributes.

You can initiate a page to an individual or team, and also override existing shifts by tapping on the shift you would like to override. You can view Bits AI SRE monitor investigations for initial findings and conclusions. For more information, see [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/).

To configure On-Call notifications on your mobile device, see the guide to [Set up your Mobile Device for Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/guides/configure-mobile-device-for-on-call/?tab=ios).

## Incidents{% #incidents %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/incident_may_2025.5face9adebf4b47927a3889a909ea6eb.png?auto=format"
   alt="Incidents page in the Datadog On-call mobile app" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_Incident.f0af2123506cd665dfe95a60557bc196.png?auto=format"
   alt="Incidents page in the Datadog On-call mobile app" /%}

{% /tab %}

On the Incidents page, you can view, search, and filter all incidents that you have access to in your Datadog account to ensure response and resolution from anywhere. You can also declare and edit incidents, and seamlessly communicate to your teams through integrations with Slack, Zoom, and many more. For more information about Incidents, see [Datadog Incident Management](https://docs.datadoghq.com/monitors/incident_management).

### Create an incident{% #create-an-incident %}

1. Navigate to the incident list by tapping on the Incidents Tab in the bottom bar.
1. Tap the **+** button in the top right corner.
1. Give your incident a title, severity, and commander.

## Notification Center{% #notification-center %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_notification_center.f1ddcf23eb4ab046559dce31319c2db2.png?auto=format"
   alt="ios Notification center in the Datadog mobile app" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_notification_center.b8382534dbc3d23be2b15b84d7bb6fea.png?auto=format"
   alt="Android Notification center in the Datadog mobile app" /%}

{% /tab %}

The Notification Center lists all push notifications received so that notification context is never lost. You can filter by notification type.

## Dashboards{% #dashboards %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/dashboard_may_2025_v2.6df01f1e46016281becb64ec581d5119.png?auto=format"
   alt="iOS dashboard page showing list of dashboards with search and filter options" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_Dashboards.35a2930ba2eaa49555d0c38239f40431.png?auto=format"
   alt="Android dashboard page showing list of dashboards with search and filter options" /%}

{% /tab %}

On the Dashboards page, you can view and search all of the dashboards that you have access to in your Datadog org, and filter them using the same template variables you have set up in the Datadog web app. Quickly filter your dashboards using template variable saved views. For more information about template variable saved views, see [Dashboard Saved Views](https://docs.datadoghq.com/dashboards/template_variables/#saved-views). Click on an individual dashboard to view it. Click timeframe on bottom right to customize the dashboard range.

**Note**:

- To set up or edit a dashboard, you need to [log in to the Datadog browser app](https://app.datadoghq.com/dashboard/lists). For more information, see [Dashboards](https://docs.datadoghq.com/dashboards/).
- Dashboard links configured in UTC open in UTC on the mobile app. For more information, see [Dashboard Configurations](https://docs.datadoghq.com/dashboards/configure/#configuration-actions).
- Not all widget types are available, which means they do not display data on the mobile app. This includes Topology Map, List Widget (all data sources), Legacy treemap widget, and SLO Summary widget.

## Monitors{% #monitors %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/monitor_may_2025.e954c20f2270654dcf9f46299bb0a500.png?auto=format"
   alt="iOS monitors page showing list of monitors with search and filter options" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_Monitors.86dd8fcb5f5dea1e842e0232f8a5373f.png?auto=format"
   alt="Android monitors page showing list of monitors with search and filter options" /%}

{% /tab %}

On the Monitors page, you can view and search all of the monitors that you have access to in your Datadog org. You can specify by field name and build-specific search queries based on your tagging strategy. For more information about search, see the [Manage Monitors Search section](https://docs.datadoghq.com/monitors/manage/#search).

For example, to filter on metric monitors related to the SRE team that is being alerted, use the query `"status:Alert type:Metric team:sre"`. Click into individual alerts to see details, which can be filtered by type and by alert time. You can also mute the alert. Your ten most recent searches are saved so that you have faster access to previous queries. Furthermore, you can filter your monitor list using saved views, which surface when you activate the search bar. You can also view and run synthetic tests when viewing your synthetic monitors.

**Note**: To set up or edit monitors, notifications, or saved views, you must use the [Datadog web app](https://app.datadoghq.com/monitors). All monitors set up in the web app are visible in the mobile app. For more information, see [Creating monitors](https://docs.datadoghq.com/monitors/types).

## Notebooks{% #notebooks %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/notebook_may_2025.d61c2cfe141c80422920b7aa2d192db2.png?auto=format"
   alt="iOS notebooks page showing list of notebooks with search and filter options" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_Notebooks.6f3cc82eb804545b53b484ffa1bed7eb.png?auto=format"
   alt="Android notebooks page showing list of notebooks with search and filter options" /%}

{% /tab %}

On the Notebooks page, you can view and search all of the notebooks that you have access to in your Datadog org, and filter them by tags. Notebook tags allow you to filter by favorites, team, and type. See [notebook tags](https://docs.datadoghq.com/notebooks/#notebook-tags) for more information.

**Note**: To set up or edit a notebook, you need to [log in to the Datadog browser app](https://app.datadoghq.com/dashboard/lists). For more information, see [Notebooks](https://docs.datadoghq.com/notebooks/).

## Traces{% #traces %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/trace_may_2025.9df5d17449b6a20c25cdc09ae7fe49d4.png?auto=format"
   alt="iOS traces page showing list of traces with search and filter options" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_Traces.d0a9087f07505aa7447ce96abadebc04.png?auto=format"
   alt="Android traces page showing list of traces with search and filter options" /%}

{% /tab %}

On the Traces page, you can view and search all of the traces that you have access to in your Datadog org. You can narrow the list through saved views or build specific search queries based on your tagging strategy. For more information about search, see [Trace Explorer Query Syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).

For example, to filter on traces with the tag `#env:prod` or the tag `#test`, use the query `"env:prod" OR test`. Click into individual services to expand associated spans, and select spans to view info, errors, and related logs. You can also open traces from services and logs.

**Only available on iOS**: Watchdog Insights point to latency outliers and error outliers. For more information, see [Watchdog Insights](https://docs.datadoghq.com/watchdog/insights/?tab=logmanagement).

## Logs{% #logs %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/iOS_logs_v2.8525af75c4aea552919108995cb18da6.png?auto=format"
   alt="iOS logs page showing list of logs with search and filter options" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_Logs.24327eb22e3cf20847b50a113760bc69.png?auto=format"
   alt="Android logs page showing list of logs with search and filter options" /%}

{% /tab %}

On the Logs page, you can view and search all of the logs or flex logs that you have access to in your Datadog org. You can narrow the list through saved views or query filters. For more information about search, see [Log Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/).

You can also group by log patterns and select different log attributes for clustering or grouping results. For more information about log patterns, see [Grouping Logs Into Patterns](https://docs.datadoghq.com/logs/explorer/analytics/patterns/).

**Note**: To toggle on flex logs, navigate to the logs list and tap on the top right to select enable flex logs.

**Only available on iOS**: Watchdog Insights point to log anomalies and outliers. For more information, see [Watchdog Insights for Logs](https://docs.datadoghq.com/logs/explorer/watchdog_insights/).

## Services{% #services %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/service_may_2025_v2.bf129cd866e5ecfafb42be93b6115e31.png?auto=format"
   alt="iOS services page showing list of services with search and filter options" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/Android_Services.3a5d8b1009a3b27c58ae28b9e18c45a5.png?auto=format"
   alt="Android services page showing list of services with search and filter options" /%}

{% /tab %}

On the Services page, you can view, search and filter all services that you have access to in your Datadog account from the Datadog Mobile App to ensure the health of your service from anywhere. You can also view recent deployments, resources, SLOs, and monitors associated with that service. For more information about investigative tools for your services, see [manage Software Catalog](https://docs.datadoghq.com/software_catalog/manage/).

## Bits AI{% #bits-ai %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_bits_chat.433d74553d0f63892a625aaf2a105456.png?auto=format"
   alt="Bits AI chatbot interface in ios where a user asks about a service" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_bits_chat.efd1449054de44ab8797fbca43b42368.png?auto=format"
   alt="Bits AI chatbot interface in Android where a user asks about a service" /%}

{% /tab %}

On the Bits AI home page, you can ask questions about your organization's system health. Bits AI supports natural language querying for logs and APM traces. For more information, see [Chat with Bits AI](https://docs.datadoghq.com/bits_ai/chat_with_bits_ai/).

### Bits AI SRE{% #bits-ai-sre %}

{% tab title="iOS" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/ios_bits_sre.53e107dfbc36d957e49dd91a14aa7e8e.png?auto=format"
   alt="Bits AI SRE investigation results displayed on an On-Call page" /%}

{% /tab %}

{% tab title="Android" %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/android_bits_sre.c57be8a11e6829612a50c74a236381c3.png?auto=format"
   alt="Bits AI SRE investigation results displayed on an On-Call page" /%}

{% /tab %}

When enabled, Bits AI SRE initiates investigations directly on On-Call pages. These investigations present initial findings and conclusions to help responders identify potential root causes and next steps. For more information, see [Bits AI SRE](https://docs.datadoghq.com/bits_ai/bits_ai_sre/).

## Frequently Asked Question{% #frequently-asked-question %}

### How do I remain logged into the mobile app?{% #how-do-i-remain-logged-into-the-mobile-app %}

Upon successful authentication to the mobile app, you will remain logged in for 90 days.

**Note**: If you have notifications enabled, proactive notifications will be sent 10 days prior to token expiration.

### Will I still receive notifications if I am automatically signed out?{% #will-i-still-receive-notifications-if-i-am-automatically-signed-out %}

If you are automatically logged out during the 90 day token period, you will still be able to receive notifications and will be prompted to log in again.

**Note**: If you manually log out from the app, you will stop receiving notifications.

### Why am I not receiving notifications?{% #why-am-i-not-receiving-notifications %}

Check that you have notifications enabled for the Datadog app in your device app settings. If you would like to ensure that notifications bypass Do Not Disturb, check that Critical Alerts is toggled on.

### What happens if a user is disabled?{% #what-happens-if-a-user-is-disabled %}

The mobile app token will be invalid and force the user to log out.

## Troubleshooting{% #troubleshooting %}

For help with troubleshooting, [contact Datadog support](https://docs.datadoghq.com/help/). You can also send a message in the [Datadog public Slack](https://chat.datadoghq.com/) [\#mobile-app](https://datadoghq.slack.com/archives/C0114D5EHNG) channel.

## Further Reading{% #further-reading %}

- [Shortcut Configurations](https://docs.datadoghq.com/mobile/shortcut_configurations/)
- [Learn about Monitors and Alerting](https://docs.datadoghq.com/monitors/)
- [Learn about Dashboards](https://docs.datadoghq.com/dashboards/)
- [Improve your on-call experience with Datadog mobile dashboard widgets](https://www.datadoghq.com/blog/datadog-mobile-widgets/)
- [Getting started with the Datadog mobile app](https://www.datadoghq.com/blog/mobile-app-getting-started/)
- [Reduce your mean time to repair with the Datadog mobile app](https://www.datadoghq.com/blog/mobile-app-reduce-mttr/)
