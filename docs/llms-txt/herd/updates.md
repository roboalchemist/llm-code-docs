# Source: https://herd.laravel.com/docs/macos/getting-started/updates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://herd.laravel.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Updates

# Herd Updates

Herd regularly checks for new updates in the background and notifies you when a new version is available. You can disable the updater in the settings if you prefer to do that manually but we recommend to always keep Herd up to date.

To manually check for updates, click the "Check for Updates" button in the Herd menu in the macOS menu bar. This checks for Herd, PHP and Node.js updates at the same time.

## PHP versions

Herd allows you to download and install different PHP versions with a single click.
When a new PHP version is available, Herd notifies you about the update in the menu bar.

Minor PHP patch versions in Herd can lag a few days behind their official release because they get tested extensively after they've been compiled specifically for Herd.

You can choose the PHP versions which you want to install or update in the "PHP" tab of the preferences.

The supported PHP versions are:

* 8.5
* 8.4 (default)
* 8.3
* 8.2
* 8.1
* 8.0
* 7.4

If you want to learn more about PHP versions and their management in Herd, go to [Manage PHP versions](/macos/technology/php-versions).

## Laravel Installer

You can create new Laravel applications via the `laravel` command line utility or the [Site Manager](/macos/sites/managing-sites).

While Herd always ships with the latest version of the Laravel CLI, you may want to update in between Herd updates if there's a nightly change.
You can install this update via the PHP Settings tab.

<Frame>
  <img alt="Image of the PHP Settings of Herd with a highlight on the update button for Laravel" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings-php-update-laravel.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8a3abb4040cdb3e7370a852012fdee47" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings-php-update-laravel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings-php-update-laravel.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cc220cae09eaffebc518b96ca090b7d8 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings-php-update-laravel.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=58fcca024221fe00ad2d8fd1f2a34fe1 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings-php-update-laravel.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=26cd0755020b5066585811bc5f467dfe 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings-php-update-laravel.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4f7cf89caa837697905dd260bd24f2a3 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings-php-update-laravel.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5e2b52a339224887df35acf3609c46eb 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings-php-update-laravel.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2d04c560317499695c68d94a418fba93 2500w" />
</Frame>

## Composer and Expose

You can update Composer and Expose to their latest version with their integrated `self-update` commands but usually get them with Herd updates, too.

```bash  theme={null}
composer self-update
expose self-update
```

## Node.js versions

Herd ships with [nvm](https://github.com/nvm-sh/nvm) and allows you to install and use multiple Node.js versions at the same time. Officially, Herd supports the latest versions of the following major versions:

* 22.x
* 20.x
* 18.x
* 16.x

However, you may manually install any available Node.js version via the [CLI](/macos/technology/node-versions#via-the-cli).

If you want to learn more about Node.js versions and their management in Herd, go to [Manage Node.js versions](/macos/technology/node-versions).
