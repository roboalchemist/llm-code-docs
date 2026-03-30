# Source: https://render.com/docs/professional-features.md

# Professional Features — Enable powerful platform capabilities with a Professional, Organization, or Enterprise plan.

With a *Professional* plan or higher, you can invite [workspace members](team-members) to collaborate on your Render apps and infrastructure. You also gain access to powerful operational features, such as service autoscaling and environment isolation.

You can upgrade any *Hobby* workspace to a *Professional* workspace from its *Billing* page in the [Render Dashboard](https://dashboard.render.com).

> For a full comparison of plan types, see the [pricing page](/pricing).

## Feature categories

### Service ops

*Professional* workspaces and higher gain access to:

| Feature | Description |
| --- | --- |
| *[Autoscaling](scaling#autoscaling)* | Automatically scale services up and down according to their memory and CPU load. |
| *[Preview environments](preview-environments)* | Spin up an ephemeral copy of your entire production environment for safe and comprehensive integration testing. |
| *[Performance build pipeline](build-pipeline#pipeline-tiers)* | Run builds and other pre-deploy tasks with significantly more memory and CPU. |

### Networking

*Professional* workspaces and higher gain access to:

| Feature | Description |
| --- | --- |
| *[Network-isolated environments](projects#blocking-cross-environment-traffic)* | Block private network traffic from crossing the boundary of individual project environments. |
| *[Private links](private-link)* | Securely connect your infrastructure to non-Render providers hosted on AWS. |

*Enterprise orgs* also gain access to:

| Feature | Description |
| --- | --- |
| *Expanded [inbound IP rules](inbound-ip-rules)* | Configure which IP addresses can connect to your web services and static sites over the public internet. |

### Observability

*Professional* workspaces and higher gain access to:

------

###### Feature

*[HTTP request logs](logging#http-request-logs)*

###### Description

Automatically log details for every HTTP request to your web services from the public internet.

---

###### Feature

*[Response latency metrics](service-metrics#response-latency)*

###### Description

Track your web service's response times with common helpful percentiles (p50, p75, p90, and p99).

---

###### Feature

*[Metrics streaming](metrics-streams)*

###### Description

Push service metrics to your OpenTelemetery-compatible observability provider.

---

###### Feature

*[Log stream overrides](log-streams#overriding-defaults)*

###### Description

- With a *Professional* plan, you can disable log streaming for any individual service.
- With an *Organization* or *Enterprise* plan, you can also forward any individual service's logs to a different destination.

---

###### Feature

*[Webhooks](webhooks)*

###### Description

- With a *Professional* plan, send webhook event notifications to one destination.
- With an *Organization* or *Enterprise* plan, send different sets of notifications to up to 100 destinations.

------

### Compliance

*Organization* workspaces and higher gain access to:

------

###### Feature

*[Audit logs](audit-logs)*

###### Description

View and export a history of material actions performed by workspace members.

---

###### Feature

*Additional [member roles](team-members#member-roles)*

###### Description

- With an *Organization* plan, assign the *Contributor* role to technical contributors who don't need access to sensitive fields (such as connection strings and environment variables).
- With an *Enterprise* plan, also gain access to the *Viewer* and *Billing* roles.

---

###### Feature

*[HIPAA-enabled workspaces](hipaa-compliance)*

###### Description

Run HIPAA-compliant applications and store protected health information on access-restricted hosts.

---

###### Feature

*[Compliance documentation](certifications-compliance)*

###### Description

View Render's SOC 2 Type 2 report, ISO 27001 certificate, and internal security policy. Viewing these documents also requires signing an NDA.

------

### Increased limits and retention

*Professional* workspaces and higher receive:

- Unlimited [projects](projects) and environments
  - *Hobby* workspaces can create up to one project with up to two environments.
- Unlimited [custom domains](custom-domains)
  - *Hobby* workspaces can add up to two total custom domains.
- Increased monthly included amounts of [pipeline minutes](build-pipeline#pipeline-minutes) and [bandwidth usage](outbound-bandwidth)
- Increased retention of past builds for [rollbacks](rollbacks)
- Increased retention of historical [service metrics](service-metrics) and [logs](logging)