# Source: https://docs.gitguardian.com/platform/security-data-privacy/data-retention.md

# Data retention

> Describes GitGuardian's data retention policies for workspace data, incidents, audit logs, and account information.

GitGuardian takes data collection and privacy very seriously.

In order to perform monitoring effectively, GitGuardian needs to process multiple data and collects only what is actually needed for the product to meet the monitoring and remediation expectations.

### Commits with incidents only

As explained in the [How Internal Monitoring works section](../../internal-monitoring/core-concepts/how-internal-monitoring-works.md), GitGuardian integrates with your VCS on the server side. Therefore, every commit reaching the server and belonging to the perimeter will be scanned for secrets.

A commit consists of:

- its actual content: the patches containing the additions and/or deletions of code in the different files. A commit can have several patches.
- its metadata:
   - commit date
   - author date
   - committer email
   - committer name
   - author email
   - [author name](../glossary#author-vs-committer)
   - commit SHA

GitGuardian collects:

- The metadata of all the events including mostly push events. Push events metadata contains commits metadata.
  We do this in order to keep track of all the activity and compute analytics.

- The precise patch of the commits for which GitGuardian has detected secrets
  This in order for the secret to be displayed in the dashboard to help with remediation. Plus if the git history is overwritten by the developer, GitGuardian becomes the only place where the security team can access the secret in order to perform the remediation and access logs checking.

#### What happens during historical scans?

During a historical scan, GitGuardian goes through all existing commits on the repository across all branches. The patches containing secrets are collected for the same reasons as mentioned above. The other commits are not collected.
We also collect some metadata about the historical scan performed in order to compute analytics and improve the robustness of the algorithms:

- Number of commits scanned
- Number of branches scanned

### Perimeter sourcesâ metadata

When integrating with GitGuardian, you allow the monitoring of specific GitHub repositories or GitLab projects you own. They constitute the sources of your perimeter. GitGuardian collects the metadata of those sources:

- Name
- Size (in bytes)
- Visibility (public/private)
- VCS unique identifier
- Number of stars
- Number of forks
- Number of watchers

We use such information to give you an overview of your entire perimeter analytics and the ability to filter the secret incidents by sources. Metadata are also crucial to allow seamless integration between GitGuardian and your VCS.

### VCS members basic information

GitGuardian has read-access to your VCS members:

- Members of your GitHub organization (private and public members)
- Members of your GitLab instance in case of an instance-level integration.

It is necessary for GitGuardian to compute the number of seats for billing purposes.

If you would rather have your data completely isolated, you might want to self-host GitGuardian.

### SaaS Europe: GDPR Compliance

For customers in the European Union, GitGuardian offers a SaaS solution that is fully compliant with the [General Data Protection Regulation (GDPR)](https://gdpr.eu/what-is-gdpr/). This ensures that all data processing and retention adhere to the strict privacy and data protection regulations mandated by GDPR. Data is stored and processed within the EU, providing peace of mind and compliance assurance for EU-based organizations. 

If you are interested, please reach out to the GitGuardian team at [support@gitguardian.com](mailto:support@gitguardian.com). Please note that we do not support migration of existing workspace from our US platform to the EU platform at this time.
