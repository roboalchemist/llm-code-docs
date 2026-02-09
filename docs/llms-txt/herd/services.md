# Source: https://herd.laravel.com/docs/macos/herd-pro-services/services.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Services

# Services

Herd Pro provides an interface that allows you to spin up complementary services to your site easily. These services can be databases, queues and broadcasting systems, but also search engines and storage providers that mimic your production environment.

You can combine these services with a [herd.yml](/macos/sites/herd-yaml) in your project and store the site configuration for a project within the repository. This makes it super easy for others to spin up a development environment with all services in seconds.

## Installing Services

To install a service, go to the settings and select the services tab. In this tab, you can add new services and manage existing ones.

Every service has a binary directory where the applications files live and a data directory where the service stores the data and custom configuration. You can access both folders by right-clicking the service and selecting the destination.

<Frame>
  <img alt="Screenshot of service settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1e9ddb35805c0f24be4cc37832ecc9f7" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=143a7e51e9b92ed5189c1d64f04130ea 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=08309c5a6b46d8d09bbaddb00c957c5c 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3aec2a3121209890f92af9728a31965e 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=80f9b060ec397fb7cdf863fdd6978fc9 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1eccb7cd7383fa6154a32f5f8073e50c 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a2edeac7a8d42e5634472ce2c0f4af97 2500w" />
</Frame>

## Managing Services

All services have a right click menu with actions for the individual service. These actions always include a force quit option and directory shortcuts but also provide individual actions that a tailored to the service.

## Available Services

Herd Pro ships with the following services:

* [MySQL](/macos/herd-pro-services/mysql)
* [MariaDB](/macos/herd-pro-services/mariadb)
* [PostgreSQL](/macos/herd-pro-services/postgresql)
* [MongoDB](/macos/herd-pro-services/mongodb)
* [Redis](/macos/herd-pro-services/redis)
* [Laravel Reverb](/macos/herd-pro-services/laravel-reverb)
* [Typesense](/macos/herd-pro-services/typesense)
* [Meilisearch](/macos/herd-pro-services/meilisearch)
* [MinIO](/macos/herd-pro-services/minio)

You can see which versions Herd provides in the [version matrix](/macos/herd-pro-services/service-versions).

## Deleting Services

You can delete services via right-clicking on them in the service manager and selecting delete.
