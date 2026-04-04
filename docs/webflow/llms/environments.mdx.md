# Source: https://developers.webflow.com/webflow-cloud/environments.mdx

***

title: Environments
slug: environments
subtitle: Learn about environments in Webflow Cloud
description: Learn about environments in Webflow Cloud
------------------------------------------------------

Environments are unique, isolated containers where your app is deployed. Deploy your app to multiple environments—such as production, staging, or development—using branches from your GitHub repository. Each environment is fully separate, giving you the flexibility to test, preview, and release features independently.

Environments automatically update when a deployment succeeds, with zero-downtime between versions. If a deployment fails, the environment continues serving your last successful deployment, ensuring continuous availability.

[Learn more about deployments →](/webflow-cloud/deployments)

***

See the below documentation for guidance on:

* [Creating environments](#creating-environments)
* [Managing environments](#managing-environments)
* [Creating environment variables](#create-an-environment-variable)
* [Managing environment variables](#managing-environment-variables)

***

# Managing environments

<Frame>
  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/15f4ce278e763bd111bd8b9576b7b582a3990d0c712a01de5120e4a3645e129c/products/webflow-cloud/pages/introduction/assets/environment-dashboard-05-20.png" alt="Environment dashboard" />
</Frame>

## Creating environments

When you create a Webflow Cloud project, you'll be prompted to add your first environment. You can create additional environments (like staging and development) to support your development workflow.

To set up an additional environment, follow these steps:

1. In Webflow Cloud, select your project name to open the Environments Dashboard.
2. Click **Create New Environment**.
3. Select the GitHub branch you want this environment to track.
4. Define the mount path (URL path) for your environment.
5. Click **Create Environment**.

Every push to the selected branch will trigger a deployment to this environment.

## Mount paths

Each environment is assigned a unique URL path under your Webflow domain. When you deploy to an environment, your application becomes accessible at its designated path. This path-based routing allows you to:

* Host multiple environments under a single domain
* Maintain separate URLs for staging, development, and production versions
* Seamlessly integrate with Webflow's existing routing system

Mount paths are unique to each environment and are used to route traffic to the correct environment. Each mount path must be unique across all environments within a project.

## Changing mount paths

If you've already deployed an environment to your site with a mount path and you want to change it, follow these steps:

1. Click the ellipsis icon **...** for the environment.
2. Select **Edit**.
3. Change the mount path to your desired new path and save the changes.
4. Publish your Webflow site.
5. Trigger a deployment to the environment to propagate the mount path change.

## Route conflicts

If a route conflict occurs between your Webflow Cloud application and your Webflow site, the Webflow Cloud application route takes precedence.

For instance, if you have a Webflow site at `mydomain.com` with the following:

* A Webflow Cloud app mounted at `/users`
* A Webflow page also created at `/users`

When a user visits `mydomain.com/users`, they will see the Webflow Cloud app, not the static page on your Webflow site.

To avoid conflicts:

* Choose mount paths that don't conflict with existing or planned Webflow pages
* Consider using distinct paths like `/app` for your Webflow Cloud applications
* Document your app routes to prevent future conflicts when creating new Webflow pages

## Edit an environment

1. Click the ellipsis icon **...** next to the environment.
2. Select **Edit**.
3. Modify the mount path or other details.
4. Save your changes.
5. If you change the mount path, redeploy your environment so code references to the mount path are also updated.

## Unpublish an environment

To remove the environment from your domain entirely, delete the Webflow Cloud environment.

**Deleting the environment by itself doesn't remove it from your domain.**

## Delete an environment

Delete an environment to remove it from Webflow Cloud. Deleting an environment doesn't delete the GitHub branch. Conversely, deleting a GitHub branch doesn't delete the environment — you must delete the environment manually from the dashboard.

1. Click the ellipsis icon **...** next to the environment.
2. Select **Delete**.
3. Confirm the deletion.

<Warning>
  If you delete a GitHub branch, the associated environment won't automatically be deleted. You must remove it manually from the dashboard.
</Warning>

<Warning>
  Deleting an environment permanently removes all deployments associated with it.
</Warning>

## Access control and permissions

Anyone with access to your deployed mount path can view the environment. For example, if deployed to /staging, anyone with the URL can access the staging version of your site.

# Managing environment variables

Environment variables enable secure storage and management of sensitive data and configuration settings. Each environment supports up to 110 environment variables, which are accessible exclusively during runtime. For enhanced security, you can mark variables as secrets, which are then encrypted and masked in the Environment Variables dashboard. To view the value of a secret variable, click the eye icon to toggle its visibility.

## Create an environment variable

### Add a single variable

1. Open the Deployments Dashboard for the environment.
2. Click **Environment Variables**.
3. Click **Add variable** > **Add single variable**.
4. Enter a Key and Value.
5. (Optional) Mark as a Secret to mask sensitive values like API keys or client secrets.
6. Push a commit to trigger a new deployment using the updated variables.

### Bulk import variables

1. Open the Deployments Dashboard for the environment.
2. Click **Environment Variables**.
3. Click **Add variable** > **Bulk import**.
4. Drag and drop a `.env` file into the modal, or click to select a file.
5. Review the variables to be imported. Toggle **Secret** for any variables that contain sensitive values.
6. Click **Import**.
7. Push a commit to trigger a new deployment using the updated variables.

<Note>
  If any key names appear to contain sensitive data, Webflow Cloud will display
  a warning and highlight those variables so you can mark them as secrets before
  importing.
</Note>

<Note title="Environment variables are available at runtime only">
  Environment variables aren't available at build time—only during runtime. If your app requires build-time configuration, consider alternative strategies.
</Note>

## Edit an environment variable

1. In the Environment Variables dashboard, click the **...** next to a variable.
2. Select **Edit**.
3. Modify the Key and Value.
4. (Optional) Mark as a Secret to mask sensitive values like API keys or client secrets.
5. Make changes to your code and push a new commit to apply the updated environment variables.

## Delete an environment variable

1. In the Environment Variables dashboard, click the **...** next to a variable.
2. Select **Delete**.
3. Make changes to your code and push a new commit to apply the removal of this environment variable.

## Visibility of environment variables

Anyone with access to the Webflow Cloud project can view environment variables. Keep sensitive values stored as Secrets.

# Frequently asked questions

## Projects

<Accordion title="I'm having trouble connecting to GitHub">
  Follow these steps to connect your GitHub repository:

  1. Ensure you have admin access to the repository
  2. Check that you've granted the necessary permissions to Webflow Cloud
  3. Try disconnecting and reconnecting the GitHub integration
</Accordion>

<Accordion title="Why don't I see a list of my GitHub repositories?">
  If you have access to over 100 repositories, you may not see a list of your repositories. To create a project from a repository, paste the link to your repository into the GitHub repository field.
</Accordion>

<Accordion title="Can I use BitBucket or GitLab to deploy to Webflow Cloud?">
  No, currently only GitHub is supported for deployments to Webflow Cloud.
</Accordion>

<Accordion title="Can I load my Webflow site data into my app?">
  Yes, you can access your Webflow site data using our [APIs and SDKs](/data/reference/rest-introduction).
</Accordion>

<Accordion title="How do I deploy an API/backend to Webflow Cloud without a frontend?">
  Today, Webflow Cloud doesn't support pure API/backend frameworks, though we plan to in the future. Currently only Next.js and Astro are supported - both of which are designed for full stack development (frontend and backend).

  However, you can still use any of these full-stack frameworks to build an API without needing to add page/frontend files.
</Accordion>

## Environment access and visibility

<Accordion title="Who can see my environments?">
  Any user with access to your Webflow site can view your projects and environments.
</Accordion>

<Accordion title="Who can see my environment variables?">
  Any user with access to your Webflow site can view your projects and environments.
</Accordion>

<Accordion title="What happens if my path route conflicts with my Webflow site's structure?">
  When a route conflict occurs between your Webflow Cloud application and your Webflow site, the Webflow Cloud app route takes precedence. The system will first check for matching routes in your Webflow site pages, and if found, serve the Webflow Cloud page instead of your Webflow site page.
</Accordion>

<Accordion title="Can I see environment variables on previous deployments?">
  No, environment variables are only available for the current deployment.
</Accordion>

<Accordion title="How do I unpublish my environment from my Webflow site?">
  To unpublish an environment from your domain, delete the Webflow Cloud environment.
</Accordion>
