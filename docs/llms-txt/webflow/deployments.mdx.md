# Source: https://developers.webflow.com/webflow-cloud/deployments.mdx

***

title: Deployments
slug: deployments
subtitle: Learn about deployments in Webflow Cloud
description: Learn about deployments in Webflow Cloud
-----------------------------------------------------

Deployments automatically build and publish your application to Webflow Cloud. Each deployment creates a new version of your app in the associated environment. Webflow Cloud automatically triggers deployments when you push changes to the branch linked to that environment.

<Note>
  Publishing your Webflow site won't trigger a Webflow Cloud deployment. The deployment process for Webflow Cloud apps is decoupled from the Webflow site publishing process.
</Note>

[Learn more about environments →](/webflow-cloud/environments)

***

See the below documentation for guidance on:

* [Continuous deployment](#continuous-deployment)
* [Deployment process](#deployment-process)
* [Deployment history](#deployment-history)
* [Build logs](#build-logs)
* [Runtime logs](#runtime-logs)
* [Rolling back deployments](#rolling-back-deployments)

***

## Continuous deployment

Webflow Cloud supports continuous integration and deployment (CI/CD) through GitHub. When you connect your GitHub repository, Webflow Cloud automatically:

* Watches for changes in your connected branches
* Triggers new deployments when changes are detected
* Updates your environments with the latest code

<Tip title="Deploying using the Webflow CLI">
  You can also manually deploy your local environment using the Webflow CLI. In your terminal, run the following command to deploy your project to Webflow Cloud:

  ```bash
  webflow cloud deploy
  ```
</Tip>

### Setting up continuous deployment with GitHub

1. Navigate to Webflow Cloud and select your project
2. Click "Connect GitHub"
3. Follow the instructions to connect your GitHub repository or multiple repositories
4. Select a GitHub repository to connect your Webflow Cloud app to
5. Create or select an [environment](/webflow-cloud/environments) to deploy to
6. Choose the branch you want to deploy to the selected environment

<Warning>
  If you have access to over 100 repositories, you may not see a list of your repositories to select from. To create a project from a repository, paste the link to your repository into the GitHub repository field.
</Warning>

## Manual deployments

There are two ways to manually deploy your environment:

1. **Deploy using the Webflow CLI**<br />
   Run the following command in your terminal:

   ```bash
   webflow cloud deploy
   ```

2. **Deploy in the Webflow Cloud dashboard**<br />
   Navigate to your environments dashboard and click the "Deploy latest build" button.

## Deployment process

Webflow Cloud serves your app through a streamlined deployment process:

1. Clones your GitHub repository
2. Detects your app's framework
3. Installs dependencies
4. Builds your application
5. Deploys to your specified environment

Each step is logged and available for review in the [build logs.](#build-logs)

## Deployment history

<Frame>
  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/ec9ca2a494f9489838b169e0d71fb9b2155796105ee6c9ed90b9e7fbaf29ecf8/products/webflow-cloud/pages/introduction/assets/deployment-dashboard-05-20.png" alt="Deployment history" />
</Frame>

Each deployment appears in your environment's deployment history. The history provides:

* Deployment status (building, deploying, success, cancelled,failure)
* Deployment date and time
* Build and deployment duration
* Build and runtime logs

**In the event of a failed deployment, your environment continues running your last successful deployment**, ensuring zero downtime.

## Build logs

Build logs provide detailed information about how Webflow Cloud builds and deploys your app. To view build logs:

1. In Webflow Cloud, click your project name to open the Environments Dashboard
2. Click the environment name to open the Deployment Dashboard
3. Click the Deployment ID (Commit SHA) to view the build log for that deployment

Build logs are particularly helpful for:

* Debugging failed deployments
* Optimizing build performance
* Understanding dependency installation issues
* Tracking build progress

## Runtime logs

<Frame background="subtle">
  <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/17df44d6bc6b8361df2b6113413d185e6837f4c1949ff35c3d74e7a4fc448fc5/products/webflow-cloud/pages/introduction/assets/runtime-logs.png" alt="Runtime logs" />
</Frame>

Runtime logs show you what's happening on your application's server after deployment. These logs capture server-side activity, including:

* Server-side function execution
* Application errors and exceptions
* Server-side console logs and debugging output

For example, if your application includes an API endpoint and a user makes a request to that endpoint, you'll see the corresponding server-side activity in the runtime logs.

To view runtime logs:

1. In Webflow Cloud, click your project name to open the Environments Dashboard
2. Click the environment name to open the Deployment Dashboard
3. Select the "Runtime Logs" tab

<Note>
  Runtime logs are helpful for debugging server-side issues and monitoring your application's API behavior in production.
</Note>

## Rolling back deployments

If you need to revert to a previous version of your app:

1. Navigate to your GitHub repository
2. Revert your working branch to the desired commit
3. Push the changes to trigger a new deployment

<Warning>
  Rolling back a deployment creates a new deployment with the previous code version. It doesn't restore the exact state of the previous deployment.
</Warning>

## Deployment locations

# Frequently asked questions

### Build issues

<Accordion title="Why is Webflow Cloud not identifying my project at build?">
  Webflow Cloud currently supports Next.js and Astro projects. Make sure:

  * Your project is using one of these frameworks
  * You have included a configuration file (`next.config.js` or `astro.config.mjs`) with the necessary Webflow Cloud-specific configurations.
</Accordion>

<Accordion title="Why aren't my environment variables used at build?">
  Environment variables are only available at runtime, not during the build process.
</Accordion>

<Accordion title="Why are my assets not showing up?">
  This is typically related to base path configuration. Check your asset paths and ensure they're configured for your environment. For more information on base path configuration, see [base path configuration](/webflow-cloud/bring-your-own-app#3-manage-assets-and-apis) section of the Bring Your Own App documentation.
</Accordion>

<Accordion title="Which build runs on my production site if I had a successful build followed by a failed build?">
  The most recent successful build will continue running. Failed deployments never impact your live site.
</Accordion>

### Deployment issues

<Accordion title="How do I rollback to a previous deployment?">
  To rollback to a previous deployment:

  1. Revert your branch to the desired commit in GitHub
  2. Push the changes to trigger a new deployment with the previous version
</Accordion>

<Accordion title="Why can't I see my latest deployment in my dashboard?">
  Try refreshing your page - new deployments may not appear immediately in the dashboard.
</Accordion>

<Accordion title="Can I preview specific deployments?">
  No, only the most recent successful deployment for each environment can be previewed.
</Accordion>

<Accordion title="Can I share deployment previews?">
  Preview access is limited to the most recent successful deployment for each environment.
</Accordion>

<Accordion title="Why doesn't a deployment start when I push to my Github repo?">
  The [Webflow Cloud GitHub App](https://github.com/apps/webflow-cloud/installations/select_target) may not have access to your repository. To check, go to the `Webflow Cloud` tab in your Webflow site settings and click "Install GitHub App." Follow the prompts on GitHub to ensure Webflow has access to read from your repository. Once you grant access, try committing to the branch that Webflow Cloud should be monitoring for deployments in your app.
</Accordion>

### Publishing issues

<Accordion title="Will my Webflow Cloud app deployment automatically publish my Webflow site, and vice versa?">
  No, the deployment process for Webflow Cloud apps does not automatically publish your Webflow site, and publishing your Webflow site does not trigger a Webflow Cloud deployment.
</Accordion>
