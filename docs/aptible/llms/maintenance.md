# Source: https://www.aptible.com/docs/core-concepts/architecture/maintenance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Maintenance

> Learn about how Aptible simplifies infrastructure maintenance

# Overview

At Aptible, we are committed to providing a managed infrastructure solution that empowers you to focus on your applications while we handle the essential maintenance tasks, ensuring the continued reliability and security of your services.

To this extent, Aptible may schedule maintenance on your resources for several reasons, including but not limited to:

* **EC2 Hardware**: Aptible hardware is hosted on AWS EC2 (See: [Architecture](/core-concepts/architecture/overview)). Hardware can occasionally fail or require replacement. Aptible ensures that these issues are promptly addressed without disrupting your services.
* **Platform Security Upgrades**: Security is a top priority. Aptible handles security upgrades to protect your infrastructure from vulnerabilities and threats.
* **Platform Feature Upgrades**: Aptible continuously improves the platform to provide enhanced features and capabilities. Some upgrades may result in scheduled maintenance on various resources.
* **Database-Specific Security Upgrades**: Critical patches and security updates for supported database types are essential to keep your data secure. Aptible ensures that these updates are applied promptly.

Aptible will notify you of upcoming maintenance ahead of time, including the maintenance window, expectations for automated maintenance, and instructions for self-serve maintenance (if applicable).

# Maintenance Notifications

Our commitment to transparency ensures that you are always aware of scheduled maintenance windows and the reasons behind each maintenance type.

To notify you of upcoming maintenance, we will update our [status page](https://status.aptible.com/) and/or use your Ops Alert contact settings on your organization to notify you, providing you with the information you need to manage your resources effectively.

# Performing Maintenance

Scheduled maintenance can be handled in one of two ways

* **Automated Maintenance:** Aptible will automatically execute maintenance during scheduled windows, eliminating the need for manual intervention. You can trust us to manage these tasks efficiently and be monitored by our SRE team. During this time, Aptible will perform a restart operation on all impacted resources, as identified in the maintenance notifications.
* **Self-Service Maintenance (if applicable):** For maintenance impacting apps and databases, Aptible may provide a self-service option for performing the maintenance yourself. This allows you to perform the maintenance during the best window for you.

## Self-service Maintenance

Aptible may provide instructions for self-service maintenance for apps and databases. When available, you can perform maintenance by restarting the affected app or database before the scheduled window. Many operations, such as deploying an app, scaling a database, or creating a new [Release](/core-concepts/apps/deploying-apps/releases/overview), will also complete scheduled maintenance.

To identify which apps or databases require maintenance and view the scheduled maintenance window for each resource, you can use the following Aptible CLI commands:

* [`aptible maintenance:apps`](/reference/aptible-cli/cli-commands/cli-maintenance-apps)
* [`aptible maintenance:dbs`](/reference/aptible-cli/cli-commands/cli-maintenance-dbs)

<Info> Please note that you need at least "read" permissions to see the apps and databases requiring a restart. To ensure you are viewing information for all environments, its best this is reviewed by an Account Owner, Aptible Deploy Owner, or any user with privileges to all environments. </Info>
