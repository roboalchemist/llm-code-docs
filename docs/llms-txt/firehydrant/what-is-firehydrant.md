# Source: https://docs.firehydrant.com/docs/what-is-firehydrant.md

# What is FireHydrant?

<Image align="center" src="https://files.readme.io/5ce4f13-color-og.png" />

## What is FireHydrant?

FireHydrant is a complete alerting and incident management platform. From ensuring your responders are notified, to automating toil, efficiently assembling the right teams, standardizing communications, facilitating better retrospectives, and gathering metrics, FireHydrant helps organizations improve their reliability and resilience.

## Why use FireHydrant?

With FireHydrant, you can:

* Alert and page your responders about events coming from any monitoring tool
* Automate manual tasks such as creating incident Slack channels, Jira tickets, meeting bridges, and more
* Integrate with alerting and monitoring integrations to automatically create incidents from alerts
* Standardize processes and tailor them for different situations, product areas, and teams, among other criteria
* Keep track of your apps, services, environments, and their relationships, and automatically pull in responders based on impacted product area
* Maintain traceability of incident management data, communications, and action items
* Learn valuable lessons from your incidents, and use that knowledge to improve your infrastructure and processes

## Key Components

### Signals

<Image align="center" border={false} caption="Overview of Signals" src="https://files.readme.io/99641e71bbfb61735590d6d869b7469b77870f34b43623e8e6feffaabfb4e3b1-Untitled-2025-08-11-1605.png" width="650px" />

FireHydrant's Signals platform offers flexible alerting and on-call management for your teams. With the ability to configure [On-Call Schedules](https://docs.firehydrant.com/docs/signals-on-call-schedules), [Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies), and the ability to connect to practically any [event source](https://docs.firehydrant.com/docs/custom-event-source), FireHydrant is your single source of truth for when your monitoring tools sound the alarm.

Alongside the above, FireHydrant offers:

* [Alerts & Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) to allow your teams to flexibly subscribe to and route only the events they care about, reducing alert fatigue
* [Live Call Routing](https://docs.firehydrant.com/docs/live-call-routing) to provide a phone number for your end users to phone in and report incidents, either via a voicemail or directly connecting to an on-call responder
* [Migration Tool](https://docs.firehydrant.com/docs/signals-migration-tool) for quickly and easily migrating existing setups in PagerDuty, Opsgenie, or VictorOps to FireHydrant's [Terraform](https://docs.firehydrant.com/docs/terraform-provider) output
* A [Mobile Application](https://docs.firehydrant.com/docs/signals-mobile-application) so responders can receive/respond to alerts and browse incidents right from their mobile devices
* [Team Support Hours](https://docs.firehydrant.com/docs/team-support-hours) for preventing any alerts outside of working hours from paging or waking up your responders unnecessarily

To get started, visit [Introduction to Signals](https://docs.firehydrant.com/docs/signals-introduction).

### Incidents

<Image align="center" alt="The &#x22;Command Center&#x22;, or incident home" border={false} caption="The &#x22;Command Center&#x22;, or incident home" src="https://files.readme.io/bc077dd1cb22b73e85e15d20512f6f6b7b9e59f986684557c98b855e2ef081c7-CleanShot_2025-09-10_at_13.15.392x.jpg" width="650px" />

Incidents are the bread and butter of FireHydrant. FireHydrant's incidents help your team stay organized and respond to situations efficiently while alleviating the need for "scribe" or "note-taking" roles by tracking incident events automatically.

Incidents can be created through the FireHydrant UI, from Slack, through our API, or through integrations. Combined with the numerous other platform offerings below, from automation, to tracking your catalog, to managing tasks and conducting informed retrospectives, FireHydrant is here to help you Automate, Respond, Learn, and Improve.

### Runbooks

<Image align="center" alt="Runbook Automation for Different Triggers " border={false} caption="Runbook Automation for Different Triggers" src="https://files.readme.io/4b6b3a8-runbooks.png" width="650px" />

Runbooks are what make FireHydrant unique and powerful. Say goodbye to wikis and endless static playbooks; FireHydrant enables you to automate your processes, including step execution with conditional logic.

Runbooks can be tailored to different situations and severities, by teams, by product/service, and more, and they can even be layered together. With FireHydrant Runbooks, your team can stay focused on fighting fires instead of reading documentation and manually toiling.

See our [Runbooks Basics](https://docs.firehydrant.com/docs/runbooks-basics) for more information.

### Service Catalog

<Image align="center" alt="Service entries in the Catalog" border={false} caption="Service entries in the Catalog" src="https://files.readme.io/f718599af5d2e121c4ccef1194cd75cb006b5049cfd5ea6ea266ef9187b7cd15-CleanShot_2025-09-10_at_14.46.302x.jpg" width="650px" />

FireHydrant hosts a Catalog for your infrastructure to help your team stay organized. With the Catalog, you can track which properties are impacted by an incident, any dependencies between items, and who owns these properties + should be involved in an incident, among other things.

Combined with [Alerting Providers](https://docs.firehydrant.com/docs/integrations-overview) and [Slack](https://docs.firehydrant.com/docs/slack-integration), you can automatically pull in the right people and teams for the right parts of your system having issues in only a few seconds.

You can manage your FireHydrant Catalog from Web, API, or Terraform, or you can import these services from various providers. See our [Service Catalog Basics](https://docs.firehydrant.com/docs/service-catalog-basics) for more information.

### Role & Task Management

<Image align="center" alt="Notification received in Slack when assigned to roles and tasks" border={false} caption="Notification received in Slack when assigned to roles and tasks" src="https://files.readme.io/0b72bb3-tasks-roles.png" />

FireHydrant has complete task and role management built into the platform. Rather than context-switching to external wikis or playbooks, you can pre-define important to-do items within FireHydrant and track task completion as incident timeline items.

In addition, you can customize incident roles for your organization's needs, allowing every responder to know exactly what is expected of them when they're pulled into an incident.

### Retrospectives

<Image align="center" alt="Incident Retrospectives in FireHydrant" border={false} caption="Incident Retrospectives in FireHydrant" src="https://files.readme.io/79ce4d0-retrospectives.png" width="650px" />

Once an incident is resolved, FireHydrant helps teams facilitate better incident reviews with built-in Retrospectives. Retrospectives gather and contextualize information and timeline events from all throughout the incident so your team has a clear view of what happened and why it happened, and can have conversations about how to prevent future occurrences.

More importantly, teams can list out Contributing Factors, customize questions/answers in Lessons Learned, and create follow-up action items in linked external ticketing tools to plan work in future sprints.

Learn more about [FireHydrant's Retrospectives here](https://docs.firehydrant.com/docs/incident-followup)

### Integrations

<Image align="center" alt="FireHydrant Alerting and Incident Management Platform" border={false} caption="FireHydrant Alerting and Incident Management Platform" src="https://files.readme.io/67f5b14ea5b399d7fea57d2263cf009da794d418312471b09dc733dd8b172983-CleanShot_2024-09-25_at_11.14.442x.png" />

FireHydrant supports a growing list of integrations. From chat providers like Slack, to alerting providers like PagerDuty and Opsgenie, and others like Zoom, Google Docs, Jira, Zendesk, Kubernetes, Okta, etc., FireHydrant can meet your team where it currently works.

For a complete overview, see [Integrations Overview](https://docs.firehydrant.com/docs/integrations-overview).

## Other features

### Incident Types

You can fill in information for your incidents ad-hoc, or you can pre-define \[ for your operators to easily declare. This is useful to remove the cognitive load for your teams to declare specific types of situations, pulling in the right responders and resources every time.

### Team Management

[FireHydrant's Teams](https://docs.firehydrant.com/docs/team-configuration) allow you to quickly assign a group of people to an incident from Slack or the UI. They're also a great way to see which groups own the services in your application stack.

### Severities

On top of customizing your severities, FireHydrant reduces the stress of figuring out how severe an incident is by enabling you to configure a [Severity Matrix](https://docs.firehydrant.com/docs/severity-matrix). If certain functionality is down, automatically assign severities. Now, your incident response team can create incidents and be confident that the correct severity is applied.

### Change events ingestion

Many incidents are caused by deploys or configuration changes. With FireHydrant, you can easily view your deploy events associated with different pieces of infrastructure so you can more quickly track the cause of your incidents. FireHydrant supports [ingesting Change Events](https://docs.firehydrant.com/docs/change-events) via the API as well as through our [Kubernetes](https://docs.firehydrant.com/docs/kubernetes-integration) and [AWS CloudTrail](https://docs.firehydrant.com/docs/aws-cloudtrail-integration) integrations.

### Status pages

FireHydrant offers two out-of-box status page features: [incident-specific status pages](https://docs.firehydrant.com/docs/internal-status-pages) and [system-wide, global status pages](https://docs.firehydrant.com/docs/status-page-overview). Incident-specific status pages are private, temporary status pages that expire after 48 hours of your incident being resolved. Global status pages can be public or private, and they are meant to show the status of your platform or application's individual components at any given time.

FireHydrant also offers an integration with [Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration)

### Analytics

FireHydrant gives you a quick view of your historical incidents and infrastructure health so you know where to focus your efforts and how you can improve your incident response process moving forward. [Analytics](https://docs.firehydrant.com/docs/analytics-basics) include breakdowns of incidents by system components, response metrics like remediation time, and much more.

## Next Steps

With all of the above stated, check out the following resources:

* Check out FireHydrant's [Product Demo](https://docs.firehydrant.com/docs/product-demo) for a glimpse of FireHydrant in action
* See the [Quickstart Guides](https://docs.firehydrant.com/docs/quickstart-guides) to dive right into FireHydrant
* Browse the [overview of integrations](https://docs.firehydrant.com/docs/integrations-overview) that FireHydrant supports
* Browse our [comprehensive guides](https://docs.firehydrant.com/docs/declare-and-respond) that fully explain all of FireHydrant's capabilities