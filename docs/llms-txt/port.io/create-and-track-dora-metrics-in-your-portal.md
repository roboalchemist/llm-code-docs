# Source: https://docs.port.io/guides/all/create-and-track-dora-metrics-in-your-portal.md

# Create & track DORA metrics in your portal

[YouTube video player](https://www.youtube.com/embed/Tnef7-mdKes)

<br />

This guide will walk you through the setup and use of DORA metrics in your portal.<br /><!-- -->We will learn how to configure DORA metrics, track them, and view insights to drive engineering improvements.

This guide sets up all the foundational components and works out of the box with [GitHub](/build-your-software-catalog/sync-data-to-catalog/git/github/.md) and [PagerDuty](/build-your-software-catalog/sync-data-to-catalog/incident-management/pagerduty/.md) integrations.

If you define GitLab as your preferred deployment method, complete this guide, then proceed to the [GitLab guide](/guides/all/set-up-deployments-dora-gitlab.md) to adjust the relevant components.

If you define Jira issues as your preferred deployment and incident method, complete this guide, then proceed to the [Jira guide](/guides/all/setup-dora-metrics-jira.md) to adjust the relevant components.

## Port DORA metrics overview[â](#port-dora-metrics-overview "Direct link to Port DORA metrics overview")

The DORA Metrics experience helps you track the four key engineering performance indicators: **Deployment frequency**, **Lead time for changes**, **Mean time to recovery (MTTR)**, and **Change failure rate**.

This experience provides:

* A prebuilt setup for collecting DORA metrics.
* Flexible configuration of what counts as deployments and incidents.
* Automated data ingestion via integrations and APIs.
* A centralized dashboard for visibility and insights.

### New components[â](#new-components "Direct link to New components")

When you install the DORA Metrics experience, Port automatically generates the following components to help you configure, ingest, and visualize your engineering performance data:

#### Blueprints

* `Deployment` and `Incident` â the main components used to calculate your DORA metrics.

#### Dashboard pages

* `Set up your deployments` â A dashboard page to define what qualifies as a *deployment* in your organization.
* `Set up your incidents` â A dashboard page to define what qualifies as an *incident* in your organization.
* `DORA metrics` â A dashboard page that helps you track your organization's engineering performance over time.

#### Self-service actions

* `Create a deployment` â an action that creates a deployment.
  <br />
  <!-- -->
  By default, the dashboard page will contain multiple actions to create a deployment, one for each definition of a deployment.
* `Create an incident` â an action that creates an incident.
  <br />
  <!-- -->
  By default, the dashboard page will contain multiple actions to create an incident, one for each definition of an incident.

#### Integration mapping

When a user executes the self-service action to define deployments or incidents, the relevant [integration mapping](/build-your-software-catalog/customize-integrations/configure-mapping.md) (according to the selected deployment/incident method) is updated with a new block.

This automates a manual step that would otherwise require editing the integration mapping directly.

*Note:* filters in the action use an `AND` operator. To achieve `OR` logic, run the action multiple times with different filter sets.

#### Additional components

Port also creates supporting technical mechanisms to ensure stable and reliable data ingestion:

* **Blueprints** â Used to avoid accidental data loss during resyncs.<br /><!-- -->For example, closed pull requests are deleted on resync by default to avoid ingesting historical data.<br /><!-- -->To preserve relevant data:

  * Closed PRs are first ingested into a hidden `_deployment_event` blueprint.
  * An automation that upserts the data into the main `Deployment` blueprint.
  * This ensures only the hidden blueprint is affected by resync deletions.

* **Automations** â Ensure reliable data flow from configuration to ingestion:

  * Your self-service actions define how deployments and incidents are tracked.
  * These definitions update integration mappings, which ingest data into hidden blueprints.
  * Automations then upsert that data into the main blueprints, protecting it from resync deletions.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To set up DORA metrics in your portal, you will need:

* Admin permissions (in order to install the experience and execute self-service actions).
* A connected GitHub integration (for deployment tracking) or access to custom API setup.
* A connected PagerDuty integration or access to custom API setup.

## Set up DORA metrics[â](#set-up-dora-metrics "Direct link to Set up DORA metrics")

1. Go to your [software catalog](https://app.getport.io/organization/catalog).

2. Click on the `+ New` button in the left sidebar, then choose `New experience`.

3. In the modal, choose `New DORA metrics dashboard`.

4. Choose a title for your dashboard and click `Create`.

   ![](/img/guides/doraChooseName.png)

## Configure your deployments & incidents[â](#configure-your-deployments--incidents "Direct link to Configure your deployments & incidents")

After installation, you need to:

1. **Configure Deployments:**

   * Choose the relevant deployment method according to your organization's definition of a deployment (Merged PRs, GitHub Workflows, GitHub Releases, Github Deployments, Custom API, etc).
   * Apply filters (target branch, PR labels, etc) to align with your process.

2. **Configure Incidents:**

   * Choose the relevant incident method according to your organization's definition of an incident (PagerDuty, Custom API, etc).
   * Connect to a source like PagerDuty or configure via Custom API.

## Track results[â](#track-results "Direct link to Track results")

Navigate to the DORA metrics dashboard created in the "DORA setup & dashboard" folder in your [software catalog](https://app.getport.io/organization/catalog).

Once your data starts accumulating, you will see visualized metrics including:

* Deployment frequency.
* Lead time for changes.
* Mean time to recovery (MTTR).
* Change failure rate.

These metrics give you a high-level view of your engineering velocity and reliability, helping your team identify areas for improvement.

![](/img/guides/doraDashboardExample.png)
