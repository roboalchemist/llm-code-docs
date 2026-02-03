# Source: https://herd.laravel.com/docs/macos/integrations/laravel-forge.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Laravel Forge

# Laravel Forge

Herd has a seamless integration with [Laravel Forge](https://forge.laravel.com) and allows you to interact and deploy your Herd site directly on Forge. After connecting your site, you are able to deploy the site, open an SSH connection, grab your environment variables or open the site within Forge with a single click.

## Connect Herd with your Laravel Forge account

To use the Forge integration, you need to set up at least one Forge account in the Integrations tab of the settings. Select `Connect Service` and select Laravel Forge. Herd supports multiple Forge accounts in case you have separate accounts for your personal sites and sites that you manage at work.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_connect.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e21b4bd560754a477e097a9413b9e652" data-og-width="1600" width="1600" data-og-height="1122" height="1122" data-path="images/docs/integrations_forge_connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_connect.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f102bee9855be1eadca81175fb22193e 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_connect.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=223ebb41258bba0caae2ac374c99762e 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_connect.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0f52ef0a4d7ca2b10bd98066d9670065 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_connect.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9a2b629e2f775c298f39c3fd55e6da72 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_connect.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a092bf23a9b750667b8531dd61e08be0 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_connect.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=adfdfe5b49031919f560a95d72b3dd35 2500w" />
</Frame>

During the setup process, Herd connects to your Laravel Forge account and obtains an OAuth token during the authorization.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_auth.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4643168e691581729f126e01b8b95446" data-og-width="2242" width="2242" data-og-height="1432" height="1432" data-path="images/docs/integrations_forge_auth.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_auth.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a799e483870d4f152105138d3222a4a2 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_auth.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c518f4b0daa22620f64bca21ce74017f 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_auth.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c2fc42920fa4ff7c7e1612a52f6bfec7 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_auth.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2fb13b842281d5a9b833c085f84501c5 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_auth.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=282a8b6833da4632f71a29f48909e9fa 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_auth.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8b63430afdd6448e13762375e76f245d 2500w" />
</Frame>

When Forge and Herd are connected, it shows up in the integrations list. This means that you are ready to link local sites with sites on Forge now.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_connected.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b4cc24ef2565f16352b0cf4ac2402f86" data-og-width="1600" width="1600" data-og-height="1102" height="1102" data-path="images/docs/integrations_connected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_connected.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=971e0125b63e9566603ad3f1abc09e61 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_connected.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=44d329816fef2a3e60d5ef8fa998fb82 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_connected.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=deae7f6c60245428b22efc7b20c0f2ca 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_connected.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7a250fb1919b649d8bd51a87bc4ad6b8 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_connected.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=539415287ac15e11b0ffe79bc352fe54 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_connected.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2f82309905603700a5a89c9d0cbfa8a3 2500w" />
</Frame>

## Link a Herd site with Laravel Forge

When the integration is set up, you can open the Sites panel, select a site and press the button to connect this site to one or more sites on Forge. This allows you to access development, staging and production environments directly from one Herd site.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c60994a647b27bbee4e4d1e2a957a44f" data-og-width="1800" width="1800" data-og-height="1258" height="1258" data-path="images/docs/integrations_forge_site.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=51472310e6f8cf8bab7078206f1ff35f 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ce9a5dbe85547de9fa195ffff91f2e16 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=75b13c41ae0e6e6f83d026912d2868d9 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=fd074bd7958eb4e4e4181c0b7da0daad 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=bc2eebe89b0dd44ebcc4ca552bb0d5ec 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5d27168d78a5b9fd64b258181f706dc4 2500w" />
</Frame>

After you've selected a site, you can deploy the site with the icon in the main toolbar or use the other functions on the right side of the panel.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site_features.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=15c038100af3be630cdbee885629b55d" data-og-width="1800" width="1800" data-og-height="1258" height="1258" data-path="images/docs/integrations_forge_site_features.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site_features.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ce87fa62ae3fadc1564f6e33196e0f3d 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site_features.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5b32118baef0496dd437ebf811607b6a 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site_features.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=873d6166b898e2da96817a41b5514132 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site_features.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1ac4b664183c1b4561aa2c033155a34a 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site_features.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8b839cc9ea08186899d98d573373d997 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/integrations_forge_site_features.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=39f3432223a26f647bf17d58419473eb 2500w" />
</Frame>

### Forge

The Forge button open your site in Forge and gives you access to all Forge features.

### SSH

You can directly open an SSH connection in your favorite terminal from the site menu.

### `.env`

If you want to copy some environment variables from a Forge site to recreate the same setup locally, you can open your `.env` file with the .env button.

## CLI

The Herd integration with the Forge CLI allows you to omit servers and sites from commands which makes it super easy to interact with your sites via the command line. Just run `forge` to see all available commands or go through the list below.

```bash  theme={null}
  command          Execute a CLI command
  deploy           Deploy a site
  open             Open a site in forge.laravel.com
  ssh              Start an SSH session
  tinker           Tinker with a site

  daemon:list      List the daemons
  daemon:logs      Retrieve the latest daemon log messages
  daemon:restart   Restart a daemon
  daemon:status    Get the current status of a daemon

  database:logs    Retrieve the latest database log messages
  database:restart Restart the database
  database:shell   Start a database shell
  database:status  Get the current status of the database

  deploy:logs      Retrieve the latest deployment log messages

  env:pull         Download the environment file for the given site
  env:push         Upload the environment file for the given site

  nginx:logs       Retrieve the latest Nginx log messages
  nginx:restart    Restart Nginx
  nginx:status     Get the current status of Nginx

  php:logs         Retrieve the latest PHP log messages
  php:restart      Restart PHP
  php:status       Get the current status of PHP

  server:current   [current] Determine your current server
  server:list      List the servers
  server:switch    [switch] Switch to a different server

  site:list        List the sites
  site:logs        Retrieve the latest site log messages

  ssh:configure    Configure SSH key based secure authentication
  ssh:test         Test the SSH key based secure authentication connection
```

If the CLI detects more than one linked site, it asks you which one you want to use before running the command:

```bash  theme={null}
 ┌ Select the Forge integration to use: ────────────────────────┐
 │ › ● herd.laravel.com                                         │
 │   ○ latest.herdphp.com                                       │
 └──────────────────────────────────────────────────────────────┘
```

## Version Control

Herd stores the server and site ids in a `herd.yml` within the root of your project. This way, everyone on your team can directly access the site if they have access to the site in Forge. If you want to fully leverage the `herd.yml`, read more [here](/macos/sites/herd-yaml).

```yaml  theme={null}
integrations:
  forge:
    herd.laravel.com:
      server-id: 12345
      site-id: 67890

```
