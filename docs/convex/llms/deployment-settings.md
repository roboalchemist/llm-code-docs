# Source: https://docs.convex.dev/dashboard/deployments/deployment-settings.md

# Settings

The [deployment settings page](https://dashboard.convex.dev/deployment/settings) gives you access to information and configuration options related to a specific deployment (**production**, your personal **development** deployment, or a **preview** deployment).

## URL and Deploy Key[​](#url-and-deploy-key "Direct link to URL and Deploy Key")

The [URL and deploy key page](https://dashboard.convex.dev/deployment/settings) shows:

* The URL this deployment is hosted at. Some Convex integrations may require the deployment URL for configuration.
* The URL that HTTP Actions for this deployment should be sent to.
* The deployment's deploy key, used to [integrate with build tools such as Netlify and Vercel](/production/hosting/.md) and [syncing data with Fivetran and Airbyte](/production/integrations/streaming-import-export.md).

![Deployment Settings Dashboard Page](/assets/images/deployment_settings-58661797d5cadbc484d3d36dde845c04.png)

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

The [environment variables page](https://dashboard.convex.dev/deployment/settings/environment-variables) lets you add, change, remove and copy the deployment's [environment variables](/production/environment-variables.md).

![deployment settings environment variables page](/assets/images/deployment_settings_env_vars-e148766325f85db3409292b10f202bba.png)

## Authentication[​](#authentication "Direct link to Authentication")

The [authentication page](https://dashboard.convex.dev/deployment/settings/authentication) shows the values configured in your `auth.config.js` for user [authentication](/auth.md) implementation.

## Backup & Restore[​](#backup--restore "Direct link to Backup & Restore")

The [backup & restore page](https://dashboard.convex.dev/deployment/settings/backups) lets you [backup](/database/backup-restore.md) the data stored in your deployment's database and file storage. On this page, you can schedule periodic backups.

![deployment settings export page](/assets/images/backups-7e17da1541fc3eb26194a96ab33414ea.png)

## Integrations[​](#integrations "Direct link to Integrations")

The integrations page allows you to configure [log streaming](/production/integrations/.md), [exception reporting](/production/integrations/.md), and [streaming export](/production/integrations/streaming-import-export.md) integrations.

## Pause Deployment[​](#pause-deployment "Direct link to Pause Deployment")

On the [pause deployment page](https://dashboard.convex.dev/deployment/settings/pause-deployment) you can [pause your deployment](/production/pause-deployment.md) with the pause button.

![deployment settings pause deployment page](/assets/images/deployment_settings_pause-4e036413269bccced2d58a99d2bb6f98.png)
