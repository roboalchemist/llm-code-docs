# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/getting-started-with-the-platform-deployment-options-getint-for-jira-data-center-jira-server.md

# Getint for Jira Data Center

## Getint for Jira Data Center & Server: Architecture & Deployment Guide

### Overview

Getint for Jira Data Center and Server is a native application built using the Atlassian Plugins SDK (P2 framework). Unlike the Cloud version, which is a SaaS service, the Data Center version resides entirely within your infrastructure. This deployment type is designed for high-availability environments and organizations with strict data residency requirements.

### 1. Technical Architecture

The application runs as a native plugin within the Jira Java Virtual Machine (JVM).

* **Clustered Environments**: For Jira Data Center instances with multiple nodes, Getint uses a cluster lock mechanism. This ensures that synchronization tasks are executed on only one node at a time, preventing data conflicts or duplicate syncs.
* **Scheduling**: The app initiates a background scheduled job to handle data integration. While users define the sync interval in the settings, the actual execution is managed by the Jira internal scheduler.
* **Internal Communication**: The app communicates with Jira via the Jira Java API and the Internal REST API.

### 2. Data Storage & Security

This deployment model is "Firewall-Friendly" and does not require outbound access to external Getint servers.

* **Local Storage**: All configuration details, mapping logic, and synchronization metadata are stored within your own Jira Database (in dedicated Getint tables).
* **File Storage**: Synchronization logs and temporary files are stored in the `JIRA_HOME/log/getint` directory (or the root `JIRA_HOME` If no log folder exists.)
* **Zero External Connectivity**: When deployed in a standalone on-premise capacity, the platform operates independently of `getint.io` servers. No ticket data ever leaves your internal network.

{% hint style="info" %}
We know Data Center admins have to be careful about storage bloat. If you ever decide to uninstall the app, feel free to clear out any leftover Getint database tables and log files. It’s completely safe to delete them, and it’s actually a great way to keep your instance optimized and clutter-free.
{% endhint %}

### 3. Installation & Licensing

Following the 2025 standard, installation is managed directly via the Atlassian Marketplace.

1. Navigate to the [Atlassian Marketplace](https://marketplace.atlassian.com).
2. Search for Getint and select the version compatible with Data Center.
3. Click Get it now or Try it free.
4. Log in to your Jira instance as a System Administrator.
5. Navigate to Administration (Gear Icon) > Manage Apps.
6. Upload the `.jar` or `.obr` file if you downloaded it manually, or confirm the installation from the Marketplace prompt.
7. License Verification: Access the license settings within the Getint menu to apply your Marketplace license key.

### 4. User Access & Permissions

To manage integrations, users must be granted specific access through Jira Groups.

* Admin Access: System Administrators see the "Getint" menu by default.
* Delegated Access: To allow non-admin users to manage specific integrations, create a group following the naming convention: `getint-jira-[target-tool]` (e.g., `getint-jira-azure-devops`).
* Service Account: We recommend using a dedicated "Service User" to establish the connection. This provides a clear audit trail in issue histories (e.g., "Updated by Getint Integration").

### 5. Key Comparison: Data Center vs. Cloud

| **Feature**     | **Data Center (Native)**     | **Jira Cloud (SaaS)** |
| --------------- | ---------------------------- | --------------------- |
| Hosting         | Customer Infrastructure      | Getint (AWS)          |
| Data Storage    | Local Database & JIRA\_HOME  | Getint Infrastructure |
| Cluster Support | Native Cluster Lock          | Multi-tenant SaaS     |
| Maintenance     | Managed by Customer          | Managed by Getint     |
| External Access | Not Required (Firewall safe) | Required (SaaS model) |

For organizations ready to begin their integration, you can initiate a 30-day free trial directly through the **Atlassian Marketplace** to evaluate the platform in your sandbox or production environment. If your deployment involves complex high-availability configurations or specific security requirements, you can schedule a technical consultation with a Getint specialist. For more information, feel free to contact us at our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjrKGRyToPPdWu8WzVABo%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=29e3b121-8c4c-4ea7-b9c2-9c66a3308838" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
