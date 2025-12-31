# Source: https://herd.laravel.com/docs/macos/advanced-usage/herd-cli.md

# Command Line

# Herd Command Line Interface

The following commands are available in the Laravel Herd CLI tool. Each command allows you to manage development environment settings and configurations directly from the command line.

## Common Commands

You can get the full list of commands by running `herd list` in your terminal.

* [herd composer](#herd-composer)
* [herd coverage](#herd-coverage)
* [herd debug](#herd-debug)
* [herd edit](#herd-edit)
* [herd init](#herd-init)
* [herd ini](#herd-ini)
* [herd isolate](#herd-isolate)
* [herd isolate-node](#herd-isolate-node)
* [herd isolated](#herd-isolated)
* [herd isolated-node](#herd-isolated-node)
* [herd link](#herd-link)
* [herd links](#herd-links)
* [herd log](#herd-log)
* [herd logs](#herd-logs)
* [herd open](#herd-open)
* [herd park](#herd-park)
* [herd parked](#herd-parked)
* [herd php](#herd-php)
* [herd restart](#herd-restart)
* [herd secure](#herd-secure)
* [herd secured](#herd-secured)
* [herd share](#herd-share)
* [herd site-information](#herd-site-information)
* [herd start](#herd-start)
* [herd stop](#herd-stop)
* [herd tinker](#herd-tinker)
* [herd unisolate](#herd-unisolate)
* [herd unisolate-node](#herd-unisolate-node)
* [herd unlink](#herd-unlink)
* [herd unsecure](#herd-unsecure)
* [herd use](#herd-use)
* [herd which](#herd-which)
* [herd which-php](#herd-which-php)
* [herd init:fresh](#herd-initfresh)

***

## herd composer

The `herd composer` command proxies composer calls to the isolated PHP version of a site. We recommend setting up an alias for your terminal so that running `composer` on the command line always uses `herd composer` and uses the correct PHP version for your site.

## herd coverage

You can run `herd coverage` to run PHP commands with Xdebug coverage enabled and it always uses the the isolated PHP executable.

## herd debug

Run `herd debug` and automatically load your `debug.ini` for this command. The `debug.ini` usually includes Xdebug so if you want to debug artisan commands, this is how to do it from your terminal.

## herd edit

The `herd edit` command opens the current directory in the configured IDE.

## herd ini

The `herd ini` command automatically opens the `php.ini` file for your current global PHP version in your configured IDE.
When running this command in an isolated project path, Herd will open the php.ini file for the isolated PHP version.

You may also specify which version you want to use:

```
herd ini 8.0
```

## herd init

If a `herd.yml` file is present in the directory, Herd configures your application according to the manifest file. Without a `herd.yml`, the command starts the wizard to create one.

## herd isolate

The command tells Herd to use a specific PHP version for this directory when serving sites or using the `herd composer` or `herd php` commands.

```bash  theme={null}
herd use 8.2
herd use 8.3
herd use 8.4
```

## herd isolate-node

Similar to the `herd isolate` comand for PHP, the `herd isolate-node` command sets a specific Node.js version for a directory. The difference to the PHP version of the command is that `herd isolate-node` creates and NVM config file that autoamtically switches the global node version if you enter this directory – so you can't run multiple versions in different directories in parallel.

## herd isolated

The `isolated`command lists all sites with isolated PHP versions and givey you a quick overview where they are.

## herd isolated-node

Analog to the PHP command, the `isolate-node` command lists all sites with isolated Node.js versions.

## herd link

You can register applications outsite of a parked path via the `herd link` command. It also supports linking multiple domains to a single application.

```bash  theme={null}
# Link the current directory as some-site.test
herd link some-site
# Link the same application via some-other-domain.test
herd link some-other-domain
```

## herd links

You can display all linked sites via `herd links`.

```bash  theme={null}
+------------------+-----+------------------------------+------------------------------------+-------------+---------+
| Site             | SSL | URL                          | Path                               | PHP Version |         |
+------------------+-----+------------------------------+------------------------------------+-------------+---------+
| beyondco.de      |     | http://beyondco.de.test      | /Users/seb/Code/beyondco.de        | 8.2         | v21.3.0 |
| herd.laravel.com |     | http://herd.laravel.com.test | /Users/seb/Code/herd.laravel.com   | 8.3         | 21      |
| tinkerwell.app   |  X  | https://tinkerwell.app.test  | /Users/seb/Code/tinkerwell-site    | 8.1         | v21.3.0 |
+------------------+-----+------------------------------+------------------------------------+-------------+---------+
```

## herd log

You can tail any logs from Herd via the `herd log` command. If you run it without an argument, it displays all available log files and if your specify a service, it tails the logs of this service.

```bash  theme={null}
herd log
herd log nginx
```

## herd logs

If you're using [Herd Pro](https://herd.laravel.com/checkout), you can open the Log Viewer via `herd logs` from your terminal.

## herd open

The `herd open` command opens the current directory in a browser.

## herd park

You can park additional directories via the `herd park` command and make all subdirectories available via their `.test` domains.

## herd parked

Type `herd parked`to lists all sites in parked paths.

## herd php

The `herd php` command runs PHP commands using the isolated executable for the site.

```bash  theme={null}
herd php artisan inspire
```

## herd restart

You can restart all Herd services via the `herd restart` command.

## herd secure

Generate a trusted TLS certificate by running `herd secure` in the directory of am application.

## herd secured

Run `herd secured` to list all currently secured sites with the expiration date of the certificate.

## herd share

You can share local applications via the `herd share` command and [Expose](https://expose.dev).

## herd site-information

The `herd site-information` command displays information based on the driver of the application. For Laravel applications, this is the result of the `php artisan about` command but you can replace that with a custom driver.

## herd start

Start all Herd services with `herd start`.

## herd stop

Stop all Herd services – from nginx and dnsmasq to all Herd Pro services – via  `herd stop`.

## herd tinker

You can hop into a tinker session with your Laravel application via `herd tinker`. If Herd detects [Tinkerwell](https://tinkerwell.app) on your machine, it automatically opens the application in Tinkerwell.

## herd unisolate

If you've isolated the application at your current terminal path to a specific PHP version and want to use the global version again, you can run `herd unisolate` to remove the isolation.

## herd unisolate-node

Like `herd isolate`, the `unisolate-node` command removes the isolation to a specific Node.js version. The command uses Herd's nvm under the hood so make sure to have that installed first.

## herd unlink

You can remove the configuration for a linked site by running the `herd unlink` command in the linked directory.

## herd unsecure

Run `herd unsecure` to remove the TLS certificate of the domain and the automated redirect to HTTPS from nginx. Make sure to restart your browser session or clear your redirect cache because your browser will still try to send you to the HTTPS URL instead of simply serving the site via HTTP.

## herd use

The command `herd use` changes the global PHP version that Herd uses to serve all sites that don't have an isolated version.

```bash  theme={null}
herd use 8.3
herd use 8.4
```

## herd which

In case that you are debugging issues with your custom Herd driver, you can run `herd which` to see which driver Herd detects for the application at your current terminal path.

## herd which-php

You can run `herd which php` to see which PHP binary Herd uses to serve the application at your current terminal path.

## herd init:fresh

Initializes a fresh Herd manifest file.

Herd also ships with the Forge CLI and you can run `forge` commands like `forge ssh` from any local site that you link via the Forge Integration without specifying a server.
