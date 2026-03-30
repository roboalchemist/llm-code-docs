# Source: https://docs.getint.io/getting-started-with-the-platform/deployment-options/jira-cloud.md

# Getint for Jira Cloud

## Getint for Jira Cloud: Deployment & Architecture Guide

### Overview

Getint for Jira Cloud operates as a SaaS (Software as a Service) application. Unlike legacy Jira Server plugins that ran natively within the Java Virtual Machine (JVM) of the host server, the Cloud version functions as an external service that interacts with your Jira instance via secure web protocols.

This deployment model ensures that the integration platform runs independently of your Jira infrastructure, preventing performance impact on your primary project management environment.

### Technical Architecture

The integration relies on a distributed architecture comprising two main components: the Atlassian Connect App and the Getint Platform.

#### The Interface (Iframe-Based Loading)

When a user accesses Getint via the Jira Apps menu, the following process occurs:

* **Request Initiation**: Jira Cloud sends a request to Getint servers to load the application interface.
* **Iframe Execution**: The Getint administration panel loads within a secure iframe inside the Jira UI. This panel is hosted externally on Getint's infrastructure.
* **User Functionality**: From this panel, administrators configure integrations, map fields, and view synchronization reports.

#### Data Synchronization (REST API)

Actual data processing and synchronization occur via the Jira Cloud REST API:

* **External Execution**: The sync engine runs on Getint’s servers, not within Jira.
* **API Requests**: Getint sends authenticated HTTP requests to Jira to read issue data, write updates, upload attachments, or post comments.
* **Storage**: Configuration data (mappings, settings) and synchronization logs are stored on the Getint infrastructure.

### Deployment & Configuration

#### Installation (Direct via Atlassian Marketplace)

In 2025, the standard installation flow starts directly at the external marketplace rather than searching from within the Jira instance.

1. Navigate to [marketplace.atlassian.com](https://marketplace.atlassian.com) in your browser.
2. Search for **Getint** and select the application from the search results.
3. Click the **Try it free** button in the top right corner.
4. If prompted, log in with your Atlassian credentials.
5. Select the Jira Cloud site where you want to install the app from the dropdown menu.
6. Click **Start free trial** to confirm. The app will be installed on your selected instance, and you will be redirected to the success page.

#### User Group Setup

For Jira instances with restrictive permissions, you must follow a specific group naming convention.

* Required Format: `getint-jira-[target-tool]`
* Examples:
  * `getint-jira-azure` (for Jira to Azure DevOps)
  * `getint-jira-servicenow` (for Jira to ServiceNow)

#### Authentication Requirements

Because the application runs externally, it requires explicit authorization to access your Jira data. Getint uses API Token authentication rather than user passwords, adhering to Atlassian's security standards.

Required Credentials:

* User Email: The email address of the Jira account used for the integration (we recommend a dedicated service account).
* API Token: An Atlassian API Token generated from [id.atlassian.com](https://id.atlassian.com/manage-profile/security/api-tokens).

*Note: The Jira account used for the connection must have the necessary permissions (Browse Projects, Create Issues, Edit Issues) for all projects you intend to synchronize.*

### Security & Data Residency

* Infrastructure: The Getint platform is hosted on AWS (Amazon Web Services).
* Data Handling: While configuration and logs are stored on Getint servers to facilitate the service, the application connects directly to your Jira instance to process ticket data.
* Compliance: The application operates under the Atlassian Cloud Fortified program standards.

### Comparison: Cloud vs. Data Center

| **Deployment** | **Jira Cloud (SaaS)**  | **Jira Data Center (Native)** |
| -------------- | ---------------------- | ----------------------------- |
| Hosting        | Hosted by Getint (AWS) | Hosted on Customer Server     |
| Connectivity   | REST API (HTTP)        | Native Java API               |
| Maintenance    | Managed by Getint      | Managed by Customer           |
| Updates        | Automatic              | Manual Update Required        |

### Deployment Best Practices

* **Dedicated Integration User**: We recommend creating a "Service User" in Jira Cloud for the integration. This ensures that sync activities are not tied to a specific employee's account and provides a clear audit trail in the issue history (e.g., "Updated by Getint Sync").
* **Filter Early**: Use Getint's JQL-based filtering to only sync the tickets you need. This reduces unwanted syncs and optimizes performance.
* **Log Retention**: Customize your log retention settings in the Getint dashboard to align with your organization’s internal data privacy policies.

*For organizations with restricted cloud access, Getint also offers an On-Premise deployment option that can be installed on private servers behind your firewall.*

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjrKGRyToPPdWu8WzVABo%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=29e3b121-8c4c-4ea7-b9c2-9c66a3308838" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
