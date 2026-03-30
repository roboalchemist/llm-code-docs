# Source: https://console.groq.com/docs/projects

---
description: Learn how to organize your Groq applications and manage resources with Projects - including rate limits, usage tracking, and team permissions.
title: Projects - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

# Projects

Projects provide organizations with a powerful framework for managing multiple applications, environments, and teams within a single Groq account. By organizing your work into projects, you can isolate workloads to gain granular control over resources, costs, access permissions, and usage tracking on a per-project basis.

## [Why Use Projects?](#why-use-projects)

* **Isolation and Organization:** Projects create logical boundaries between different applications, environments (development, staging, production), and use cases. This prevents resource conflicts and enables clear separation of concerns across your organization.
* **Cost Control and Visibility:** Track spending, usage patterns, and resource consumption at the project level. This granular visibility enables accurate cost allocation, budget management, and ROI analysis for specific initiatives.
* **Team Collaboration:** Control who can access what resources through project-based permissions. Teams can work independently within their projects while maintaining organizational oversight and governance.
* **Operational Excellence:** Configure rate limits, monitor performance, and debug issues at the project level. This enables optimized resource allocation and simplified troubleshooting workflows.

## [Project Structure](#project-structure)

Projects inherit settings and permissions from your organization while allowing project-specific customization. Your organization-level role determines your maximum permissions within any project.

Each project acts as an isolated workspace containing:

* **API Keys:** Project-specific credentials for secure access
* **Rate Limits:** Customizable quotas for each available model
* **Usage Data:** Consumption metrics, costs, and request logs
* **Team Access:** Role-based permissions for project members

The following are the roles that are inherited from your organization along with their permissions within a project:

* **Owner:** Full access to creating, updating, and deleting projects, modifying limits for models within projects, managing API keys, viewing usage and spending data across all projects, and managing project access.
* **Developer:** Currently same as Owner.
* **Reader:** Read-only access to projects and usage metrics, logs, and spending data.

## [Getting Started](#getting-started)

### [Creating Your First Project](#creating-your-first-project)

**1\. Access Projects**: Navigate to the **Projects** section at the top lefthand side of the Console. You will see a dropdown that looks like **Organization** / **Projects**.

  
**2\. Create Project:** Click the rightside **Projects** dropdown and click **Create Project** to create a new project by inputting a project name. You will also notice that there is an option to **Manage Projects** that will be useful later.

> **Note:** Create separate projects for development, staging, and production environments, and use descriptive, consistent naming conventions (e.g. "myapp-dev", "myapp-staging", "myapp-prod") to avoid conflicts and maintain clear project boundaries.

  
**3\. Configure Settings**: Once you create a project, you will be able to see it in the dropdown and under **Manage Projects**. Click **Manage Projects** and click **View** to customize project rate limits.

> **Note:** Start with conservative limits for new projects, increase limits based on actual usage patterns and needs, and monitor usage regularly to adjust as needed.

  
**4\. Generate API Keys:** Once you've configured your project and selected it in the dropdown, it will persist across the console. Any API keys generated will be specific to the project you have selected. Any logs will also be project-specific.

  
**5\. Start Building:** Begin making API calls using your project-specific API credentials

### [Project Selection](#project-selection)

Use the project selector in the top navigation to switch between projects. All Console sections automatically filter to show data for the selected project:

* API Keys
* Batch Jobs
* Logs and Usage Analytics

## [Rate Limit Management](#rate-limit-management)

### [Understanding Rate Limits](#understanding-rate-limits)

Rate limits control the maximum number of requests your project can make to models within a specific time window. Rate limits are applied per project, meaning each project has its own separate quota that doesn't interfere with other projects in your organization. Each project can be configured to have custom rate limits for every available model, which allows you to:

* Allocate higher limits to production projects
* Set conservative limits for experimental or development projects
* Customize limits based on specific use case requirements

Custom project rate limits can only be set to values equal to or lower than your organization's limits. Setting a custom rate limit for a project does not increase your organization's overall limits, it only allows you to set more restrictive limits for that specific project. Organization limits always take precedence and act as a ceiling for all project limits.

### [Configuring Rate Limits](#configuring-rate-limits)

To configure rate limits for a project:

1. Navigate to **Projects** in your settings
2. Select the project you want to configure
3. Adjust the limits for each model as needed

### [Example: Rate Limits Across Projects](#example-rate-limits-across-projects)

Let's say you've created three projects for your application:

* myapp-prod for production
* myapp-staging for testing
* myapp-dev for development

**Scenario:**

* Organization Limit: 100 requests per minute
* myapp-prod: 80 requests per minute
* myapp-staging: 30 requests per minute
* myapp-dev: Using default organization limits

**Here's how the rate limits work in practice:**

1. myapp-prod  
   * Can make up to 80 requests per minute (custom project limit)  
   * Even if other projects are idle, cannot exceed 80 requests per minute  
   * Contributing to the organization's total limit of 100 requests per minute
2. myapp-staging  
   * Limited to 30 requests per minute (custom project limit)  
   * Cannot exceed this limit even if organization has capacity  
   * Contributing to the organization's total limit of 100 requests per minute
3. myapp-dev  
   * Inherits the organization limit of 100 requests per minute  
   * Actual available capacity depends on usage from other projects  
   * If myapp-prod is using 80 requests/min and myapp-staging is using 15 requests/min, myapp-dev can only use 5 requests/min

**What happens during high concurrent usage:**

If both myapp-prod and myapp-staging try to use their maximum configured limits simultaneously:

* myapp-prod attempts to use 80 requests/min
* myapp-staging attempts to use 30 requests/min
* Total attempted usage: 110 requests/min
* Organization limit: 100 requests/min

In this case, some requests will fail with rate limit errors because the combined usage exceeds the organization's limit. Even though each project is within its configured limits, the organization limit of 100 requests/min acts as a hard ceiling.

## [Usage Tracking](#usage-tracking)

Projects provide comprehensive usage tracking including:

* Monthly spend tracking: Monitor costs and spending patterns for each project
* Usage metrics: Track API calls, token usage, and request patterns
* Request logs: Access detailed logs for debugging and monitoring

Dashboard pages will automatically be filtered by your selected project. Access these insights by:

1. Selecting your project in the top left of the navigation bar
2. Navigate to the **Dashboard** to see your project-specific **Usage**, **Metrics**, and **Logs** pages

## [Next Steps](#next-steps)

* **Explore** the [Rate Limits](https://console.groq.com/docs/rate-limits) documentation for detailed rate limit configuration
* **Learn** about [Groq Libraries](https://console.groq.com/docs/libraries) to integrate Projects into your applications
* **Join** our [developer community](https://community.groq.com) for Projects tips and best practices

Ready to get started? Create your first project in the [Projects dashboard](https://console.groq.com/settings/projects) and begin organizing your Groq applications today.