# Source: https://docs.firehydrant.com/docs/integrations-overview.md

# Integrations Overview

<Image alt="FireHydrant Alerting and Incident Management Platform" align="center" src="https://files.readme.io/e944a746c45a6d7faa1a4b8127df70dfe76921b01419cc21bd526f1d55f50943-CleanShot_2024-09-25_at_11.14.442x.png">
  FireHydrant Alerting and Incident Management Platform
</Image>

FireHydrant centralizes your incident management processes by integrating with the tools you already use. This article is a high-level overview of our integrations and what you can do with them. For help setting up specific integrations, reference our integration guides within the article below or on the left under their respective sections.

## Alerting integrations

FireHydrant offers an extensible, powerful [alerting product, Signals](https://docs.firehydrant.com/docs/signals-introduction). However, we also integrate with other alerting tools like [Opsgenie](https://docs.firehydrant.com/docs/opsgenie-integration), [PagerDuty](https://docs.firehydrant.com/docs/pagerduty-integration), and [Splunk On-Call (VictorOps)](https://docs.firehydrant.com/docs/splunk-on-call-victorops-integration) to unlock the following features:

* Kick off your incident response process directly from an alert
* Import services from your alerting tool into FireHydrant's [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)
* Connect on-call schedules so responders can [look up and page on-call personnel](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)
* [Automatically paging service owners](https://docs.firehydrant.com/docs/auto-alerting-services) when services are impacted on incidents
* ...and more!

To learn more, reference our [Introduction to Signals](https://docs.firehydrant.com/docs/signals-introduction) docs, or for 3rd-party alerting, see the left under **Integrations > Alerting & Monitoring**.

## Monitoring integrations

On top of alerting tools, FireHydrant also supports direct integrations with several monitoring providers so that any alerts raised in those platforms can automatically kick off incidents in FireHydrant. Those providers include:

* [Alertmanager](https://docs.firehydrant.com/docs/alertmanager-integration)
* [BugSnag](https://docs.firehydrant.com/docs/bugsnag-integration)
* [Datadog](https://docs.firehydrant.com/docs/datadog-integration)
* [Honeycomb](https://docs.firehydrant.com/docs/honeycomb-integration)
* [New Relic](https://docs.firehydrant.com/docs/new-relic-integration)

Like the alerting tools, these integrations also support [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).

> 📘 Note:
>
> If you are using FireHydrant's **Signals**, visit [Configuring Event Sources](https://docs.firehydrant.com/docs/signals-configuring-event-sources) to learn how to integrate your monitoring tools with FireHydrant's alerting platform.

## Messaging integrations

FireHydrant integrates with Slack so you can declare and respond to incidents where your team is already collaborating. The Slack integration allows you to conduct entire incidents end-to-end, including:

* Declaring incidents and kicking off Runbook automation
* Assigning roles and teams to an incident
* Seeing who is on-call and paging teams and people
* Adding notes to incidents
* Capturing key messages and all events in the incident timeline
* Resolving incidents
* ...and more

FireHydrant currently has integrations with [Slack](https://docs.firehydrant.com/docs/slack-integration) and [Microsoft Teams](https://docs.firehydrant.com/docs/microsoft-teams-integration).

## Ticketing integrations

FireHydrant integrates with project issue tracking tools like [Jira](https://docs.firehydrant.com/docs/jira-cloud-integration), [Asana](https://docs.firehydrant.com/docs/asana-integration), [Linear](https://docs.firehydrant.com/docs/linear-integration), [Shortcut](https://docs.firehydrant.com/docs/shortcut-integration), and [ServiceNow](https://docs.firehydrant.com/docs/servicenow-integration) to enable the following capabilities:

* Automatically creating FireHydrant incidents from new tickets in the external tool
* Automatically create a ticket in the external tool when you declare an incident in FireHydrant
* Capturing follow-ups as tickets in the external tool and linking those to the original incident ticket
* ...and more

Refer to our ticketing integration docs under **Integrations> Ticketing** to learn more.

## Video Conferencing integrations

FireHydrant integrates with video conferencing tools, like [Zoom](https://docs.firehydrant.com/docs/zoom-integration), [Google Meet](https://docs.firehydrant.com/docs/google-meet-integration), and [Webex](https://docs.firehydrant.com/docs/webex-integration), to support the following functionality:

* Automatically create a conference bridge when you declare an incident
* Configure whether you want the call to be recorded (applies only to certain integrations)
* Use template variables to dynamically name the meeting topic and agenda (for example, using the incident severity, incident name, and incident description)

Refer to our video conferencing integration docs on the left under **Integrations> Video Conferencing** to learn more.

## Other integrations

FireHydrant integrates with other tools, such as change event streams and external status pages. Here are some of the different integrations you can configure on FireHydrant:

* Publish incidents to [Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration)
  * **Note**: FireHydrant also has proprietary [status pages](https://docs.firehydrant.com/docs/status-page-overview), hosted on the FireHydrant platform
* Export retrospective data into collaborative document management tools, like [Google Docs](https://docs.firehydrant.com/docs/google-docs-integration) and [Confluence Cloud](https://docs.firehydrant.com/docs/confluence-cloud-integration)
* Import services and change events from [GitHub](https://docs.firehydrant.com/docs/github-integration)
* Use [Kubernetes](https://docs.firehydrant.com/docs/kubernetes-integration) to automatically ingest change events and catalog services deployed in your clusters to FireHydrant
* Turn failed checks from [Checkly](https://docs.firehydrant.com/docs/checkly-integration) into alerts or incidents on FireHydrant
* Ingest change events from [AWS CloudTrail](https://docs.firehydrant.com/docs/aws-cloudtrail-integration)
* Manage your FireHydrant configuration and account with [Terraform](https://registry.terraform.io/providers/firehydrant/firehydrant/latest)
* Link [Zendesk](https://docs.firehydrant.com/docs/zendesk-integration) tickets to incidents to track customer impact and automatically post incident updates to those tickets as internal notes

Reference our other integration docs on the left under **Integrations> Other** to learn more.

## Next Steps

The most common integrations users will configure on FireHydrant are [Slack](https://docs.firehydrant.com/docs/slack-integration) for chat, [Google Meet](https://docs.firehydrant.com/docs/google-meet-integration)/[Zoom](https://docs.firehydrant.com/docs/zoom-integration) for video conferencing, and [Signals](https://docs.firehydrant.com/docs/signals-introduction), [PagerDuty](https://docs.firehydrant.com/docs/pagerduty-integration), or [Opsgenie](https://docs.firehydrant.com/docs/opsgenie-integration). If you're not sure where to start, start with those!