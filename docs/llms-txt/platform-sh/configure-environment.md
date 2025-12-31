# Source: https://docs.upsun.com/administration/web/configure-environment.md

# Configure environments

From your project's main page in the Console, you can see all your environments as a list or a project tree:

![List of all environments as a tree](https://docs.upsun.com/images/management-console/environments.png "0.5")

In this overview, the names of inactive environments are lighter.
Selecting an environment allows you to see details about it,
such as its [activity feed](#activity-feed), [services](#service-information),
[metrics](https://docs.upsun.com../../increase-observability/metrics.md), and [backups](https://docs.upsun.com../../environments/backup.md).

## Activity Feed

When you access an environment in the Console, you can see its [activity feed](https://docs.upsun.com../../increase-observability/logs/access-logs.md#activity-logs).
This allows you to check which activities have happened or are currently happening on the selected environment:

![Environment activity list](https://docs.upsun.com/images/management-console/activity.png "0.5")

You can filter activities by type (such as merge, sync, or redeploy).

## Actions on environments

Each environment offers ways to keep environments up to date with one another:

* [Branch **Branch**](https://docs.upsun.com/glossary.md#branch) to create a new child environment.
* [Merge

       **Merge**](https://docs.upsun.com/glossary.md#merge) to copy the current environment into its parent.
* [ **Sync**](https://docs.upsun.com/glossary.md#sync)
  to copy changes from its parent environment into the current environment.

There are also additional options:

* Settings **Settings** to [configure the environment](#environment-settings).
* More **More** to get more options.
* **URLs** to access the deployed environment from the web.
* **SSH** to access your project using SSH.
* **Code**
  * **CLI** for the command to get your project set up locally with the [Upsun CLI](https://docs.upsun.com../cli.md).
  * **Git** for the command to clone the codebase via Git.

    If you're using Upsun as your primary remote repository, the command clones from the project.
    If you have set up an [external integration](https://docs.upsun.com../../integrations/source.md),
    the command clones directly from the integrated remote repository.

    If the project uses an external integration to a repository that you haven't been given access to,
    you can't clone until your access has been updated.
    See how to [troubleshoot source integrations](https://docs.upsun.com../../integrations/source/troubleshoot.md).

## Environment URL

When you access an environment in the Console, you can view its URL. While the environment is loading in the Console, a `Waiting for URL...` message is displayed instead of the URL. If this message isn't updated once your [default environment](https://docs.upsun.com../../environments/_index.md#default-environment)'s information is loaded, follow these steps:

1. Check that [you have defined routes](https://docs.upsun.com../../define-routes.md) for your default environment.
2. Verify that your [application](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md), [services](https://docs.upsun.com../../add-services.md), and [routes](https://docs.upsun.com../../define-routes.md) configurations are correct.
3. Check that your default environment is [active](https://docs.upsun.com../../environments/deactivate-environment.md#reactivate-an-environment).

## Environment settings

To access the settings of an environment, click Settings **Settings** within that environment.

![Settings for an environment](https://docs.upsun.com/images/management-console/env-settings.png "0.75")

### Environment name

Under **Environment name**, you can edit the name and type of your environment and view its parent environment:

![Environment status](https://docs.upsun.com/images/management-console/env-name.png "0.5")

### Status

Under **Status**, you can check whether or not your environment is [active](https://docs.upsun.com/glossary.md#active-environment).

![Environment status](https://docs.upsun.com/images/management-console/env-status.png "0.5")

For preview environments, you can [change their status](https://docs.upsun.com../../environments/deactivate-environment.md).

### Outgoing emails

Under **Outgoing emails**, you can allow your environment to [send emails](https://docs.upsun.com../../development/email.md):

![Environment email](https://docs.upsun.com/images/management-console/env-email.png "0.75")

### Hide from search engines

Under **Hide from search engines**, you can tell [search engines to ignore the site](https://docs.upsun.com../../environments/search-engine-visibility.md):

![Environment search](https://docs.upsun.com/images/management-console/env-search.png "0.5")

### HTTP access control

Under **HTTP access control**, you can [control access to your environment using HTTP methods](https://docs.upsun.com../../environments/http-access-control.md):

![Settings control access with password and by IP](https://docs.upsun.com/images/management-console/settings-basics-access-control.png "0.5")

### Variables

Under **Variables**, you can define [environment variables](https://docs.upsun.com../../development/variables/_index.md):

![Configure Upsun environment variables](https://docs.upsun.com/images/management-console/settings-variables-environment.png "0.6")

## Service information

For each environment, you can view information about how your routes, services, and apps are currently configured.

To do so, click **Services**.
By default, you see configured routes.

### Routes

The **Router** section shows a list of all the [routes configured on your environment](https://docs.upsun.com../../define-routes.md).
You can see each route's type and check if caching and server side includes have been enabled for it.

To view the configuration file where your routes are set up, click **Configuration**.

### Applications

To see detailed information about an app container,
select it in the tree or list on the left-hand side:

![Services: app overview](https://docs.upsun.com/images/management-console/service-tab/app-overview.png "0.5")

The **Overview** tab gives you information about your app.
You can see:

* The language version, the container size, the amount of persistent disk,
  the number of cron jobs, and the command to SSH into the container.
* A summary of [metrics for the environment](https://docs.upsun.com../../increase-observability/metrics.md).
* All cron jobs with their name, frequency, and command.
* All workers with their name, size, amount of persistent disk, and command to SSH into the container.

To view [the configuration file where your app is set up](https://docs.upsun.com../../create-apps/), click **Configuration**.

### Services

To see detailed information about a [running service](https://docs.upsun.com../../add-services.md),
select it in the tree or list on the left-hand side:

![Services: service overview](https://docs.upsun.com/images/management-console/service-tab/service-overview.png "0.5")

The **Overview** gives you information about the selected service.
You can see the service version, the container size, and the disk size, if you've configured a persistent disk.
You can also see a summary of [metrics for the environment](https://docs.upsun.com../../increase-observability/metrics.md).

To view the configuration file where your services are set up, click **Configuration**.

