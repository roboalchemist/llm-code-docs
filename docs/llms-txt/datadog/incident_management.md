# Source: https://docs.datadoghq.com/incident_response/incident_management.md

---
title: Incident Management
description: Create and manage incidents
breadcrumbs: Docs > Incident Management
source_url: https://docs.datadoghq.com/incident_management/index.html
---

# Incident Management

{% callout %}
##### Join an enablement webinar session

Explore and register for Foundation Enablement sessions. Learn how Datadog Incident Management enables DevOps teams and SREs to more effectively manage their incident response workflows from start to finish, saving time and reducing frustration when it matters most.

[SIGN UP](https://www.datadoghq.com/technical-enablement/sessions/?tags.topics-0=Incidents)
{% /callout %}

Datadog Incident Management helps your team members identify, mitigate, and analyze disruptions and threats to your organization's services. With Incident Management, you can design an automation-enhanced response process that helps your teams assemble around a shared framework and toolkit. You can also use incident analytics to evaluate the effectiveness of your incident response process.

Incidents live in Datadog alongside your metrics, traces, and logs. Your teams can declare incidents from monitor alerts, security signals, events, cases, and more. You can also configure monitors to [declare incidents automatically](https://docs.datadoghq.com/incident_response/incident_management/declare#from-a-monitor).

## Get Started{% #get-started %}

Incident Management requires no installation. Get started by taking a Learning Center course, reading our guided walkthrough, or declaring an incident.

- [Learn about Datadog Incident Management by working through a hands-on examples](https://learn.datadoghq.com/courses/intro-to-incident-management)
- [Guided walkthrough of an Incident workflow](https://docs.datadoghq.com/getting_started/incident_management/)
- [Declare an incident](https://docs.datadoghq.com/incident_response/incident_management/declare)

## View your incidents{% #view-your-incidents %}

To view your incidents, go to the [Incidents](https://app.datadoghq.com/incidents) page to see a feed of all ongoing incidents.

- Filter your incidents through the properties listed on the left, including Status, Severity, and Time To Repair (hours).
- Use the Search field to enter tag attributes or keywords.
- Export your search results with the Export button at the top of the incident list.
- Configure additional fields that appear for all incidents in [Incident Settings](https://app.datadoghq.com/incidents/settings).

You can also view your Incidents list from your mobile device home screen and manage/create incidents by downloading the [Datadog Mobile App](https://docs.datadoghq.com/mobile), available on the [Apple App Store](https://apps.apple.com/app/datadog/id1391380318) and [Google Play Store](https://play.google.com/store/apps/details?id=com.datadog.app).

{% image
   source="https://datadog-docs.imgix.net/images/service_management/mobile/iOS_Incident_V2.e869960f9a218c34e15b8b5dbfffbbe0.png?auto=format"
   alt="Two views in the Datadog Mobile App: one showing an incidents list with high-level details about each incident, and one showing a detailed panel for a single incident" /%}

## Describing the incident{% #describing-the-incident %}

When declaring an incident, it is critical to provide a comprehensive description, detailing what happened, why it occurred, and related attributes to ensure all stakeholders in the incident management process are fully informed. The essential elements of an incident declaration include a title, severity level, and incident commanders. Effective incident management documentation includes:

- Updating incident details, including its status, impact, root cause, detection methods, and service impacts.
- Forming and managing a response team, using custom responder roles, and leveraging metadata attributes for detailed incident assessment.
- Configuring notifications to keep all stakeholders informed throughout the incident resolution process.

For more information, see the [Describe an Incident](https://docs.datadoghq.com/incident_response/incident_management/describe) documentation.

## Evaluate incident data{% #evaluate-incident-data %}

Incident Analytics provides insights into the efficiency and performance of your incident response process by allowing you to aggregate and analyze statistics from past incidents. Key metrics, such as time to resolution and customer impact, can be tracked over time. You can query these analytics using graph widgets in dashboards and notebooks. Datadog offers customizable templates, such as the Incident Management Overview Dashboard and a Notebook Incident Report, to help you get started.

For more details on the measures collected and step-by-step graph configurations to visualize your data, see [Incident Management Analytics](https://docs.datadoghq.com/incident_response/incident_management/analytics/).

## Integrations{% #integrations %}

Incident Management integrates closely with other Datadog products, including:

- [Datadog Status Pages](https://docs.datadoghq.com/incident_response/status_pages/) to create public or private status pages and connect them to incidents.
- [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/) to escalate pages into incidents and manually or automatically page teams from an incident.
- [Datadog Notebooks](https://docs.datadoghq.com/notebooks/) to draft and review postmortems.
- [Datadog Workflow Automation](https://docs.datadoghq.com/actions/workflows/) to build and execute automations.

### Third-party integrations{% #third-party-integrations %}

Incident Management integrates with third-party applications, including:

- [Atlassian Statuspage](https://docs.datadoghq.com/integrations/statuspage/) to create and update Statuspage incidents.
- [Confluence](https://docs.datadoghq.com/integrations/confluence/) to generate incident postmortems.
- [CoScreen](https://docs.datadoghq.com/coscreen) to launch collaborative meetings with multi-user screen sharing, remote control, and built-in audio and video chat.
- [CoTerm](https://docs.datadoghq.com/coterm) to follow terminal-based incident remediation activities in real time.
- [Jira](https://docs.datadoghq.com/integrations/jira/) to create a Jira ticket for an incident.
- [Microsoft Teams](https://docs.datadoghq.com/integrations/microsoft-teams/?tab=datadogapprecommended#datadog-incident-management-in-microsoft-teams) to create channels and video meetings for incidents.
- [PagerDuty](https://docs.datadoghq.com/integrations/pagerduty/) and [OpsGenie](https://docs.datadoghq.com/integrations/opsgenie/) to page your on-call engineers and auto-resolve pages upon incident resolution.
- [ServiceNow](https://docs.datadoghq.com/integrations/servicenow/) to create a ServiceNow tickets for incidents.
- [Slack](https://docs.datadoghq.com/integrations/slack/?tab=slackapplicationbeta#using-the-slack-app) to create channels for incidents.
- [Webhooks](https://docs.datadoghq.com/integrations/webhooks/) to send incident notifications using webhooks (for example, [sending SMS to Twilio](https://docs.datadoghq.com/integrations/webhooks/#sending-sms-through-twilio)).
- [Zoom](https://docs.datadoghq.com/integrations/zoom-incident-management/) to launch video calls for incidents.

## Billing{% #billing %}

Incident Management is a seat-based SKU. To learn more about how Incident Management is billed and how to manage seats within Datadog, visit our [pricing page](https://www.datadoghq.com/pricing/?product=incident-response#products) and the [Incident Response billing documentation](https://docs.datadoghq.com/account_management/billing/incident_response/).

## Further Reading{% #further-reading %}

- [Check out the latest Incident Management releases! (App login required).](https://app.datadoghq.com/release-notes?category=Incident%20Management)
- [Incident Management Analytics](https://docs.datadoghq.com/dashboards/querying/#incident-management-analytics)
- [Join an interactive session to improve your Incident Management](https://dtdg.co/fe)
- [More efficient pair programming with Datadog CoScreen](https://www.datadoghq.com/blog/pair-programming-coscreen-datadog/)
- [Best practices for writing incident postmortems](https://www.datadoghq.com/blog/incident-postmortem-process-best-practices/)
- [Automate common security tasks and stay ahead of threats with Datadog Workflows and Cloud SIEM](https://www.datadoghq.com/blog/automate-security-tasks-with-workflows-and-cloud-siem/)
- [Ensure high service availability with Datadog Service Management](https://www.datadoghq.com/blog/datadog-service-management/)
- [Security and SRE: How Datadog's combined approach aims to tackle security and reliability challenges](https://www.datadoghq.com/blog/datadogs-approach-sre-security/)
- [Unify remediation and communication with Datadog Incident Response](https://www.datadoghq.com/blog/incidents-ai-workbench-status-page/)
