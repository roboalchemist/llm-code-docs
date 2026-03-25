# Source: https://docs.envzero.com/guides/cost-monitoring/cost-monitoring.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set Cost Monitoring

> Enable real-time cloud cost monitoring for environments and projects in env zero

env zero simplifies cloud cost management by integrating real-time monitoring directly into your IaC workflows. It precisely connects costs to specific changes, providing clear visibility across projects and environments. This allows teams to track budgets, identify anomalies, and make informed financial decisions, all while maintaining control within their existing processes.

## Actual Cost

With cost monitoring enabled in env zero, you will be able to see the cost of each Environment and Project you are running. The cost data will come directly from your cloud provider, and will include any costs incurred by your cloud resources, including fixed and usage-based costs.

<Info>
  **Project Costs**

  To be able to see a project's costs you need to have the Edit Project Settings permission.
</Info>

We utilize [Terratag](https://www.terratag.io/) to automatically tag all of your cloud resources and determine exactly how much they cost over time.

### Create cloud provider API credentials

In order to set up cost monitoring you will need to provide credentials that enable env zero to query your cloud provider's billing API. Below are guides for how to set up credentials in each cloud provider:

* [AWS Costs](/guides/cost-monitoring/aws-costs)
* [GCP Costs](/guides/cost-monitoring/gcp-costs)
* [Azure Costs](/guides/cost-monitoring/setup-azure-costs)

### Credentials Management

When creating a credential in env zero, it can be assigned to one of two scopes: `Organization` or `Project`.

* **Organization Scope**: When a credential is created via the organization credentials page (Organization Settings > Credentials), it is assigned to the `Organization` scope. This makes it available to all projects within the organization.
* **Project Scope**: When a credential is created via the project credentials page (Project Settings > Credentials), it is assigned to the `Project` scope. This makes it available to that specific project and any of its sub-projects.

All credentials, regardless of scope, are visible on the organization credentials page. To create or update credentials in a specific scope, you must have the `MANAGE_CREDENTIALS` permission at that scope level (organization or project). By default, both `Project Admin` and `Organization Admin` roles include this permission.\
For example, to create or edit credentials in the project "My Project," you need the `MANAGE_CREDENTIALS` permission for that project.

#### Use case example

A common reason to scope credentials is to separate access between environments. For instance, if you have distinct development and production projects, you can ensure that users in the development project do not have access to production credentials.

### Enable cost monitoring

1. Go to the **Project Settings** of the desired project
2. Select the **Credentials** tab
3. Check the appropriate cloud provider checkbox, and select the credential you created in the steps linked above
4. Click **Save**
5. To add the relevant tags to those environments' resources, you will need to redeploy all the relevant environments for which you would like to monitor costs

### Accuracy and incurred costs

* env zero tags your Terraform resources, in order to query your cloud provider for the actual costs. You can see which tags are applied in the Terraform plan. Some resources might not be tagged, in which case the cost reported by env zero will be lower than expected.
* env zero will call your cloud provider's API to query the cost. This might incur additional charges from your cloud provider.

### Viewing Costs

#### Environment Costs

After enabling cost monitoring for a project, all subsequent environments under that project would be monitored.\
To view an environment's cost, go to that environment's page, and click on the COST tab.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cost-monitoring/fbf9b49-screenshot_2023-07-24_at_10.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=16bf598afc610e12d730bc6acb396820" alt="Interface screenshot showing configuration options" width="2634" height="1236" data-path="images/guides/cost-monitoring/fbf9b49-screenshot_2023-07-24_at_10.png" />
</Frame>

#### Project Costs

After enabling cost monitoring for a project, simply click Project Costs on the left-side panel

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cost-monitoring/0161570-proj_costs.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=22fff522bf00475f033bf1bd20b6f429" alt="Interface screenshot showing configuration options" width="488" height="584" data-path="images/guides/cost-monitoring/0161570-proj_costs.png" />
</Frame>

#### Organization Costs

After enabling costs for projects, you can view all of them under Organization Costs.\
To get to the Organization Costs page, click on the Dashboards in the bottom left, then click the COST tab.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cost-monitoring/d3ba14c-costs_2_fix.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=2ce0cd11b85d706c65836ce0bd896369" alt="Interface screenshot showing configuration options" width="3356" height="1728" data-path="images/guides/cost-monitoring/d3ba14c-costs_2_fix.png" />
</Frame>

<Note>
  Project Based Calculation

  Only projects with cost monitoring enabled would be accounted for.
</Note>

##### Filter By Project

By default, the graph would display an accumulation of all project costs. You can filter by specific projects to view multiple projects' costs simultaneously. When chosen, each project's cost would be displayed separately.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cost-monitoring/5725794-screenshot_2023-07-25_at_9.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=fc0e4cb64ab7b2f3a0607ac805cba344" alt="Interface screenshot showing configuration options" width="2678" height="581" data-path="images/guides/cost-monitoring/5725794-screenshot_2023-07-25_at_9.png" />
</Frame>

<Info>
  **Project Filter**

  If a project title appears grayed out, it means that cost monitoring has not been configured for that specific project.
</Info>

Built with [Mintlify](https://mintlify.com).
