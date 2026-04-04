# Deployment history and logs {#deploy-history-and-logs}

For each Strapi Cloud project, you can access the history of all deployments that occurred and their details including build and deployment logs. This information is available in the *Deployments* tab.

## Viewing the deployment history {#viewing-deploy-history}

In the *Deployments* tab is displayed a chronological list of cards with the details of all historical deployments for your project.

, with a direct link to your git provider, and commit message
- Deployment status:
    - *Deploying*
    - *Done*
    - *Canceled*
    - *Build failed*
    - *Deployment failed*
- Last deployment time (when the deployment was triggered and the duration)
- Branch

## Accessing deployment details & logs

From the *Deployments* tab, you can hover a deployment card to make the ![See logs button](/img/assets/icons/Eye.svg) **Show details** button appear. Clicking on this button will redirect you to the *Deployment details* page which contains the deployment's detailed logs.

, with a direct link to your git provider, and commit message used for this deployment
- *Status*, which can be *Building*, *Deploying*, *Done*, *Canceled*, *Build failed*, or *Deployment failed*
- *Source*: the branch and commit message for this deployment
- *Duration*: the amount of time the deployment took and when it occurred