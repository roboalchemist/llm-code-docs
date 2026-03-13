# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/monitored-perimeter.md

# Manage your monitored perimeter

> Manage your monitored perimeter: source statuses, scanning types, visibility, criticality settings, and connectivity troubleshooting.

# Monitored Perimeter Management

Learn how to effectively manage, monitor, and troubleshoot your integrated sources using GitGuardian's perimeter dashboard and tools.

:::tip New to source integrations?
For guidance on **which sources to integrate** and **how they compare**, see our [Sources Integration Overview](./overview).
:::

## Understanding your perimeter

Your perimeter encompasses all the sources you've integrated with GitGuardian for secret monitoring. This includes repositories, container registries, messaging platforms, documentation systems, and more.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EmO_opxPOJo?controls=0&modestbranding=1&watchlater=0" title="Understanding Your Perimeter With GitGuardian Video" frameBorder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

Your [perimeter page](https://dashboard.gitguardian.com/perimeter?sort_health=_&sort_ic=_&sort_source=false) has two main objectives:

1. Identify which of your sources are at risk
2. Ensure that your entire perimeter is well protected by GitGuardian

![Perimeter page](/img/internal-monitoring/integrate-sources/perimeter/plain.png)

For effective navigation in the perimeter table, users can leverage [Saved views](../../platform/collaboration-and-sharing/saved-views.md) to switch between different sets of filters. The feature includes non-editable GitGuardian views such as "All sources," "Critical sources," "Scanning issues",  "With open secret incidents", "Without honeytoken".

At the bottom of the right-hand side panel, the **scope section** gives you a
quick summary of the different integrations (VCS types) that have been
integrated with GitGuardian, alongside a breakdown of sources per integration.

![Perimeter scope](/img/internal-monitoring/integrate-sources/perimeter/scope.png)

## Differences between historical scanning and real-time protection

### Real-time monitoring

The first protection and the most effective one for secrets remediation is
the **real-time monitoring**.

As you may have read in our
[How Internal Monitoring works section](../core-concepts/how-internal-monitoring-works.md),
real-time monitoring means that every single push event (and its commits) is
scanned for secrets as soon as they arrive on your VCS server (post-receive
hooks).

We use the same concept for other data sources, such as Slack and Jira, through the subscription to specific events.

We then **alert you instantly**, which will save you time in the remediation
process. Indeed, **the longer a secret is exposed, the harder the remediation
gets.**

On the right-hand side panel, we indicate **the percentage of sources covered**,
based on the number of sources you integrated with GitGuardian. Note that some
sources may not be eligible to be monitored because of plan restrictions.

Note that the table of sources displayed on the Perimeter page only contains
sources that are monitored in real-time. The sources that are not selected in
the integration settings page are not displayed.

![real-time protection coverage](/img/internal-monitoring/integrate-sources/perimeter/real_time_protection_coverage.png)

For performance reasons, we limit the number of commits scanned per push event. By default, this limit is 1,000 scanned commits/push event, but this can be customized per workspace on demand.

### Incremental scanning

GitGuardian provides ongoing protection through scheduled automated scans of your content when the integration does not offer Webhooks support.

New and modified content is systematically monitored at regular intervals, ensuring comprehensive coverage and timely detection of any secret exposures. Your source remains under GitGuardian's protection, giving you confidence that secrets won't go unnoticed.

### Historical scanning

The second type of protection offered is the ability to **scan the commit
history** of all the sources you integrated with GitGuardian.

![historical scan coverage](/img/internal-monitoring/integrate-sources/perimeter/historical_scan_coverage.png)

Size limitations apply to historical scans, depending on your plan:

- Free: you can scan sources up to 1GB,
- Business and trial: you can scan sources up to 12 GB.

:::info
For performance reasons, if a historical scan is requested for a repository that has had no new commits on any branch since the last historical scan, GitGuardian will skip the scan to avoid reprocessing the entire history. However, if the tokenscanner version has changed since the last historical scanâwith GitGuardian having introduced new detectorsâthe scan will proceed, even if there are no new commits.
:::

#### Potential Errors During Historical Scanning and Their Resolutions

| Reason | Error Message | Steps to Resolve |
|---|---|---|
| DMCA takedown | The source is unavailable due to a [DMCA](https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy) takedown. | Contact the source owner to discuss the DMCA takedown. |
| Access to the repository is disabled | The source has been disabled. | Reach out to the source owner to request re-enabling access to the repository. |
| Account has been disabled | The sourceâs account has been disabled. | Contact the source owner to resolve the account issues and regain access. |
| Access to repository restricted by IP | The sourceâs account has a configured IP allow list. | Contact the source owner to review and adjust the IP allow list. |
| Repository not found | The source could not be found. Please retry and contact the source owner if it persists. | Double-check the repository URL and retry. Contact the source owner if the issue persists. |
| Clone operation stuck or too slow | The connection to the server is slow or stuck. | Contact the VCS administrator to investigate server connection issues. |
| VCS not ready or responded with an error | The server did not respond after multiple attempts. | Reach out to the VCS administrator to ensure the server is operational and retry the scan. |
| Repository disabled in GitLab project | The git repository in the GitLab project has been disabled. | Enable the ârepositoryâ functionality in the settings of the GitLab project. |
| The repository has been deleted | The target repository has been deleted. | Contact the VCS administrator to confirm and address the deletion of the repository. |
| VCS authentication error | The authentication to the VCS has failed. | Verify authentication token under Settings > Integrations and contact the VCS administrator if needed. |
| Rate limit error | The rate limit has been exceeded. | Wait for the rate limit to reset or contact the VCS administrator for a resolution. |
| Too Large | The historical scan failed because it exceeded the authorized size limit. | Contact GitGuardian [support](mailto:support@gitguardian.com) to discuss options for scanning larger repositories. For self-hosted environments, consider adjusting the `repo_scan_size_limit` in the [preferences](../../self-hosting/management/application-management/preferences#policy) within the [Admin area](../../self-hosting/management/application-management/admin-area#settings). |
| Timeout | The historical scan failed due to a timeout error because it exceeded the authorized time limit for an individual scan. | Contact GitGuardian [support](mailto:support@gitguardian.com) for troubleshooting and to potentially extend the scan time limit. For self-hosted environments, consider adjusting the `repo_scan_time_limit_in_sec` in the [preferences](../../self-hosting/management/application-management/preferences#policy) within the [Admin area](../../self-hosting/management/application-management/admin-area#settings). |
| Timeout Pending | The historical scan failed due to a timeout error because it exceeded the authorized time limit for a bulk scan. Please contact our [support](mailto:support@gitguardian.com). | Contact GitGuardian support to address bulk scan timeouts and explore alternative solutions. For self-hosted environments, consider adjusting the `repo_scan_pending_limit_in_hours` in the [preferences](../../self-hosting/management/application-management/preferences#policy) within the [Admin area](../../self-hosting/management/application-management/admin-area#settings). |
| Scan worker error | The scan failed due to an internal worker error, often caused by memory limitations. | Please reach out to our [support team](mailto:support@gitguardian.com). If you are running GitGuardian in a self-hosted environment, consider increasing the memory allocation for workers to resolve the issue. Additionally, generate a [Support Bundle](../../self-hosting/troubleshoot/support) for further troubleshooting purposes. |
| Engine error | The scan failed due to an internal engine error. | Please reach out to our [support team](mailto:support@gitguardian.com). If you are running GitGuardian on a self-hosted environment, generate a [Support Bundle](../../self-hosting/troubleshoot/support) for troubleshooting purposes. |
| Process received SIGKILL | The scan process was forcibly terminated (SIGKILL). | Please reach out to our [support team](mailto:support@gitguardian.com). If you are running GitGuardian on a self-hosted environment, generate a [Support Bundle](../../self-hosting/troubleshoot/support) for troubleshooting purposes. |
| Filename too long | A filename inside the repository is too long. | Due to internal limitations, repositories with filenames longer than 255 bytes (approximately > 200 characters, depending on the characters used) prevent repositories from being scanned. You can find these files with commands such as `find . -type f \| awk -F/ '{if(length($NF)>200) print}'`.
| Git reference not found | The reference doesn't exist anymore. | This usually happens if the repository uses a submodule but the given reference for the submodule doesn't exist anymore. Contact the source owner to verify the submodules configuration.
| Failsafe limit reached | The source has too many issues to scan. | A failsafe limit of 200,000 incidents per source is in place. This threshold is unlikely to be reached during normal usage, but if you do encounter it, please contact our [support team](mailto:support@gitguardian.com). |
| Container image file not found in registry | A layer of the container image was not found in the registry and could not be downloaded. | Verify that the container image still exists in the registry and has not been deleted or garbage-collected. |
| Unknown | The scan failed due to an unknown error. | Please reach out to our [support team](mailto:support@gitguardian.com). If you are running GitGuardian on a self-hosted environment, generate a [Support Bundle](../../self-hosting/troubleshoot/support) for troubleshooting purposes. |

Historical scanning is also available for Slack. You can scan the entire history of your monitored public and private Slack channels. Conversations and archived channels are not supported.
Note that historical scanning is subject to the Slack's API rate limiting. We can scan up to 10.000 messages/min per Slack workspace.
Historical Scan reports of Slack and VCS are sent separately.

## Source status

### Monitored source

A source is considered as monitored when the GitGuardian platform is listening for any activity on that source.
This is the outcome of:
- successfully integrating GitGuardian with the source
- and having a plan that supports its monitoring.

Monitored sources are listed on the [Perimeter page](https://dashboard.gitguardian.com/perimeter).

### No longer monitored source

A source is considered as no longer monitored when the GitGuardian is no longer listening to any activity on that source.
This may be the result of
- uninstalling GitGuardian from the source,
- or excluding the source from the monitored perimeter,
- or a change in your plan that no longer supports this source.

A source that is no longer monitored presents a risk, as no occurrence will be created after a secret has been published in it.
Such a source is identified with a striked shield icon next to it.
![no longer monitored source](/img/internal-monitoring/integrate-sources/perimeter/source_no_longer_monitored.png)

No longer monitored sources are no longer listed on the [Perimeter page](https://dashboard.gitguardian.com/perimeter).

### Deleted source

A source is considered deleted only when GitGuardian receives evidence of its actual deletion. This means that we don't consider a source deleted just because it has been removed from GitGuardian, but rather only when it has been truly erased. Eg: the repository is deleted on GitHub.

Such a source is identified with a bin icon next to it.
![deleted source](/img/internal-monitoring/integrate-sources/perimeter/source_deleted.png)

Deleted sources are no longer listed on the [Perimeter page](https://dashboard.gitguardian.com/perimeter).

## Source visibility

A source is defined by a visibility scope. Depending on the installed instance, a source can be:
- `public`: anyone with access to the Internet can view the contents of this source. Your secret is publicly exposed and presents a higher security risk.
- `internal` (specific to GitLab): internal GitLab projects can be viewed by any authenticated user except external users. Such a GitLab project is identified by a shield icon next to it.
- `private`: Only authorized users with access to the source can view its contents. Such a source is identified by a lock icon next to it.

![source visibility](/img/internal-monitoring/integrate-sources/perimeter/source_private.png)

## Source criticality

The source criticality feature enables you to assess and assign a level of importance to your monitored sources, helping you prioritize your incidents effectively. This feature allows you to categorize them as low, medium, high, or critical, or leave it unfilled, based on the potential severity of a security incident's impact. Its value depends on the business context of your source, which will be determined by factors such as the nature of the handled data and its connection to resources in a production environment.

![business criticality edit](/img/internal-monitoring/integrate-sources/perimeter/business_criticality_edit.png)

## Bulk actions on perimeter sources

Bulk actions on the perimeter page allow you to manage multiple sources simultaneously, streamlining your perimeter monitoring workflow.

### How to use bulk actions

1. Navigate to your [perimeter page](https://dashboard.gitguardian.com/perimeter)
2. Select multiple sources using checkboxes
3. The bulk actions toolbar appears at the top
4. Choose your desired action

:::tip
Use the header checkbox to select all sources on the page, or click "Select all X sources" to select all matching your current filters.
:::

### Available actions

#### Source management
- **Set criticality**: Update business criticality levels (Critical, High, Medium, Low) for multiple sources
- **Scan**: Launch historical scans on selected sources (if scanning is enabled)

### Best practices

- **Filter first**: Use search and filters to narrow your source selection
- **Verify selection**: "Select all" button only selects the displayed sources. Use the "Select all sources that match the filters" to select the entire selection.
- **Criticality assessment**: Set source criticality based on business impact and production environments
- **Scan**: Consider system load when launching bulk historical scans (self-hosted)

### Permissions

Source bulk actions require appropriate workspace permissions:
- **Manager**: Can perform source criticality updates and launch scans
- **Member**: Can launch scans on sources within their team's perimeter but cannot update source criticality.

## Adding new sources to your perimeter

To expand your monitored perimeter with new integrations, see our comprehensive [Sources Integration Overview](./overview) which provides:

- **Capability comparison** across all source types
- **Integration guides** organized by category
- **Strategic guidance** on prioritizing integrations
- **Getting started recommendations**

The overview includes detailed information about all available integrations including VCS, container registries, messaging platforms, documentation systems, and custom sources.

## Troubleshooting connectivity problems

Most often, connectivity problems arise because a firewall, proxy server,
corporate network, or other network is configured in a way that blocks
GitGuardian.

In case you need to authorize incoming/outgoing connections to/from the SAAS
application, this paragraph provides the necessary information.

### Allowing incoming connections from GitGuardian's IP addresses

:::tip Retrieve IP addresses programmatically
GitGuardian exposes its egress IP addresses through unauthenticated API endpoints. You can use these to keep your firewall rules in sync automatically:
- **US**: `GET https://api.gitguardian.com/v1/ips` ([API reference](https://api.gitguardian.com/docs#tag/IPs))
- **EU**: `GET https://api.eu1.gitguardian.com/v1/ips` ([API reference](https://api.eu1.gitguardian.com/docs#tag/IPs))
:::

GitGuardian US uses the following IPs:

- 35.161.89.114/32
- 35.162.178.46/32
- 35.163.105.95/32
- 35.83.131.170/32
- 44.224.13.10/32
- 44.231.207.147/32
- 44.239.165.162/32
- 52.25.45.243/32
- 54.184.247.227/32
- 54.188.183.19/32
- 54.189.40.226/32
- 54.212.233.107/32

GitGuardian EU uses the following IP addresses:

- 18.153.164.184/32
- 18.158.109.52/32
- 18.184.72.235/32
- 18.198.133.200/32
- 3.127.11.54/32
- 3.64.118.208/32
- 3.75.125.128/32
- 3.76.233.226/32
- 52.28.29.48/32

These IP addresses are used for:

- [VCS integrations](./vcs-integrations/github) (eg: GitHub, GitLab)
- [Container Registries integrations](./container-registries-integrations/amazon-ecr) (eg: Amazon ECR, Azure Container Registries, Docker Hub, Google Artifact Registry, JFrog Container Registry)
- [Messaging integrations](./messaging-integrations/slack) (eg: Slack, Microsoft Teams)
- [Ticketing integrations](./ticketing-integrations/jira-cloud) (eg: Jira Cloud, Jira Data Center, ServiceNow)
- [Documentation integrations](./documentation-integrations/confluence-cloud) (eg: Confluence Cloud, Confluence Data Center)
- [Alerting integrations](../../platform/configure-alerting/alerting-and-notifications) (eg: Slack, Microsoft Teams, PagerDuty, ...)
- [Validity checks](../../secrets-detection/customize-detection/validity-checks)

### Allowing outgoing connections to GitGuardian's domains

Requests to GitGuardian use IP addresses that change regularly. It is advised to whitelist domains instead.

The following domains are used by GitGuardian US:

- dashboard.gitguardian.com
- hook.gitguardian.com
- api.gitguardian.com

The following domains are used by GitGuardian EU:
- dashboard.eu1.gitguardian.com
- hook.eu1.gitguardian.com
- api.eu1.gitguardian.com

All endpoints are using HTTPS. HTTP is exclusively used to redirect to HTTPS.
