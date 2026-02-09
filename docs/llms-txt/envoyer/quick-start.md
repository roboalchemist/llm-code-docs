# Source: https://docs.envoyer.io/quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.envoyer.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Quick Start

> There are just a few simple and intuitive steps to get started.

## Overview

The following documentation provides a step-by-step guide to configure your application and infrastructure for zero downtime deployments with Envoyer.

## Source Control Providers

Once you have subscribed to a plan, you will need to connect Envoyer with your preferred source control provider. Envoyer supports GitHub, Bitbucket, GitLab, and self-hosted GitLab.

From the onboarding screen, select your provider and follow the authentication flow for that provider. This grants Envoyer permission to interact with your repositories on your behalf.

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/source-provider.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=4fd3cf9394edf5ab2edd1e686765be27" alt="Selecting a source control provider" data-og-width="1122" width="1122" data-og-height="996" height="996" data-path="images/source-provider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/source-provider.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=702e7a70f04e571bdb8a9c26180e6ad0 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/source-provider.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=9ba21e19a967358de957954f378a4c1a 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/source-provider.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=e3e73a8db7fa0f26b8a657ee6f2a73a5 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/source-provider.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=44b5f7577c66fba3974e2fea2fc36e20 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/source-provider.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=e0062ec4f44e4e35eb7f6ef1b352c66b 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/source-provider.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=0e67a859b62938fd5418b62ca8e333ba 2500w" />
</Frame>

Once you've connected to your source control provider, this step of the onboarding flow will be complete. Should you wish to connect additional providers, you may do so from the [integrations](https://envoyer.io/user/profile#/integrations) panel of your account.

## Projects

With your source control provider connected, you can now configure your first project.

Click the "Add project" button to open the project creation modal.

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/create-project.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=a543066e719aad54282f75a72dad449c" alt="Selecting a source control provider" data-og-width="1070" width="1070" data-og-height="1578" height="1578" data-path="images/create-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/create-project.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=c4a4e11ef11bed6bd964607b836d0d3d 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/create-project.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=2ed583f5d7ba358e8204627ec0c108f7 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/create-project.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=d6dc455d53e05127ccc531dfe87b1085 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/create-project.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=cc0fc14d752a26ba9a06e96e0336b206 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/create-project.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=065b616ce8fbcca13dadc73bcbbd88d0 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/create-project.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=dd41dc5c623f977d272bfcd078571e7f 2500w" />
</Frame>

Give your project a descriptive name and select the source control provider associated with your application.

Finally, enter the repository information in the format `organization/repository` along with the branch name you want to deploy. Envoyer will automatically deploy the provided branch unless this is overridden at the start of a deployment.

## Servers

With your project created, you now need to tell Envoyer which server or servers to deploy to. There are three ways to do this.

### Import From Forge

Envoyer has a first-party integration with [Laravel Forge](https://forge.laravel.com) - Laravel's preferred server provisioning and management platform - and you may import servers directly from Forge into your project.

Click the "Provide API Token" option from the onboarding screen and provide a [Forge API token](https://forge.laravel.com/profile/api). From the project overview, you may now select the "Import" option to open the import modal. From here, select the server and site you wish to import. Envoyer will retrieve the connection details of the server and automatically add an SSH key which allows it to connect.

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-forge.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=6f24fc4e965e5a063e1cbedbf92d5515" alt="Import from Forge" data-og-width="1188" width="1188" data-og-height="716" height="716" data-path="images/import-forge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-forge.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=ec9e27b95f4332915a1f4ab8a64cdfbb 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-forge.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=821296e0a749c60b05aadb07b2e69001 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-forge.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=5c725579603fac02fadb7e48770e0003 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-forge.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=608273172c550f795c5a961a5386a677 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-forge.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=b594cab1ed6e5494604806a00d1e8c93 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-forge.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=2e2b1f273a9d4eb814ed4b7dda71d1c0 2500w" />
</Frame>

### Manual Import

Don't worry if you're not using Forge; you may configure your server manually. Select the "Configure" option from the onboarding screen in the "Manual Configuration" section. After adding the [connection details](/projects/servers#server-configuration) for your server, add the provided SSH key to the `~/.ssh/authorized_keys` file for the users Envoyer should connect to the server as.

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-manual.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=428b89f467b2db7067f5a7fbb2fd4f29" alt="Manual Import" data-og-width="1672" width="1672" data-og-height="1938" height="1938" data-path="images/import-manual.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-manual.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=0270b8dc8702e078abccd32f9222e3b3 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-manual.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=50d24fc5dcf6971d7a985911a0142d69 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-manual.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=a443d1cd42b2ff34c3012153d667f78f 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-manual.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=88b4f0a36139b7d9e0b4c7dbd4b8f129 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-manual.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=3a6d164fa0639ff821002ea4fe3796ab 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/import-manual.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=d88184f1970daeb938fd37bd24e5cda8 2500w" />
</Frame>

### Connect From Forge

It's also possible to attach a server to your Envoyer project [directly from Forge](https://forge.laravel.com/docs/integrations/envoyer#envoyer). When creating a new site on Laravel Forge, you may choose "Configure with Envoyer," allowing you to select the Envoyer project you wish the site to be attached to. Doing so will automatically configure the connection between Envoyer and Forge, install an SSH key, and set the path from which the project should be served.

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-connect.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=edaf0d98943c943ce715fb22e1a78888" alt="Connect from Forge" data-og-width="2002" width="2002" data-og-height="1132" height="1132" data-path="images/forge-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-connect.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=12e29c46e39fb5b6a44a6b97ac7a72a1 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-connect.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=19f06761e55458cd7ab30645ce2403f2 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-connect.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=93665b26bb038e293f56c2c0e877bca8 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-connect.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=4584e808af62d4ae4e8cc6610f5bfe04 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-connect.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=4ff4f42b8f5ccca1b95b49edc83d7d25 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/forge-connect.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=9ac16aaa22b3c92cc7eb23df701204ef 2500w" />
</Frame>

## Deployments

The final part of your journey to zero downtime deployments is configuring what should happen during the deployment itself.

Envoyer provides a lot of flexibility and control over your deployments - you can read more about that in the [hooks](/projects/deployment-hooks) section, but for your first deployment, there are only two things to consider:

1. Which directory on your server(s) should Envoyer deploy your application?
2. Which directory should your application be served from?

You may configure the deployment directory by opening the "Update server" modal from your project's "Servers" tab.

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/project-path.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=3b9c976953622c618262ee27f1b7fa76" alt="Updating the project path" data-og-width="1592" width="1592" data-og-height="474" height="474" data-path="images/project-path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/project-path.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=0ed4ecec3f4caaf096df9c45a2eafb9c 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/project-path.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=daf0a76f1c33c573d8d451933aacaacc 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/project-path.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=72983d0a7bed161a3dbb5b2888ab497e 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/project-path.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=c59d62d46dd51854e11f27acac01fb47 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/project-path.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=1e684f49f63098ec59ea628260e55365 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/project-path.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=3aa947023f7aa69356d1add012e82e30 2500w" />
</Frame>

Envoyer creates a `releases` directory in which your latest code is copied when you initiate a deployment. A `current` symlink is also created that links to the latest release.

If your deployment path is `/home/forge/app.com`, you should set your web server's document root directory to `/home/forge/app.com/current/public`.

<Info>
  When adding a server to Envoyer from Forge, the application path and the web root are set automatically.
</Info>

Finally, Envoyer can manage your application's environment variables across all servers associated with a project. You should likely configure this before your first deployment.

You may do so by selecting "Manage Environment" from the project overview page. First, you must provide a key to encrypt the variables stored on our servers and choose the servers. Next, you can enter your variables and select which servers you wish to sync them to. Envoyer will then connect to the selected servers and sync the variables to a `.env` file in your chosen project path.

<Warning>
  When using Envoyer, you should always manage your Environment variables via Envoyer's UI.
</Warning>

<Frame>
    <img src="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/environment.png?fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=f8d19301c35b0eaf1c3100cab91da7f7" alt="Manage environment" data-og-width="1672" width="1672" data-og-height="1616" height="1616" data-path="images/environment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/environment.png?w=280&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=6ba28d4620341977bd37790b68d52f27 280w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/environment.png?w=560&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=b988d98857cbcc39ddd59b8a92b8036b 560w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/environment.png?w=840&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=1f7bd64d171b4259ea4781e497534030 840w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/environment.png?w=1100&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=406c2fe8bf26a6efa11a41a9af90e502 1100w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/environment.png?w=1650&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=a04bbb328a811771f74d03be39c7818b 1650w, https://mintcdn.com/envoyer/t2bz6kuyoDJvJvYR/images/environment.png?w=2500&fit=max&auto=format&n=t2bz6kuyoDJvJvYR&q=85&s=3e601bdd39362eb085d150c1237f8a42 2500w" />
</Frame>

With these steps completed, you may deploy your project by clicking the "Deploy" button from your project overview, which will open the deployment modal, allowing you to choose the branch or tag you wish to deploy.

Envoyer will attempt to connect to each server and clone the code of the chosen branch or tag of the configured repository into a new release directory. Next, Composer dependencies are installed before the symlink is updated, making the new release live.

<Check>
  Congratulations, you've just successfully completed your first zero downtime deployment.
</Check>
