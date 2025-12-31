# Herd Documentation

Source: https://herd.laravel.com/docs/llms-full.txt

---

# AI Integrations
Source: https://herd.laravel.com/docs/macos/advanced-usage/ai-integrations



# AI Integrations

Laravel Herd ships with a powerful MCP (Model Context Protocol) server that can speed up your development process, by providing useful tools to your AI agents.
Your AI agent should make use of the tools automatically (when needed), but you can also manually trigger and use the available tools in your MCP client/IDE.

## Installation

The easiest way to install the Herd MCP server is by making use of [Laravel Boost](https://boost.laravel.com). Boost automatically installs the Herd MCP server and makes it available in your IDEs.
If you are not using Boost, you may manually install the Herd MCP server.

## Manual Installation

<Note>While you may install the Herd MCP server globally, we recommend installing it per-project. This way, you gain access to more fine-grained tools which leads to better AI agent results.</Note>

## Manual configuration

This is the standard configuration that works in most MCP clients.
Make sure to replace `YOUR-SITE-PATH` with the base path to your Laravel project or remove the `env` key with the site path if you're using the global installation.

```json  theme={null}
{
    "herd": {
        "command": "php",
        "args": [
            "/Applications/Herd.app/Contents/Resources/herd-mcp.phar"
        ],
        "env": {
            "SITE_PATH": "YOUR-SITE-PATH"
        }
    }
}
```

<AccordionGroup>
  <Accordion title="Claude Code">
    Use the Claude Code CLI to add the Herd MCP server. In the root of your project, run the following command:

    ```bash  theme={null}
    claude mcp add herd php /Applications/Herd.app/Contents/Resources/herd-mcp.phar -e SITE_PATH="$(pwd)"
    ```

    This will automatically set the `SITE_PATH` to the project root.
  </Accordion>

  <Accordion title="Cursor">
    Go to `Cursor Settings` -> `Tools & Integrations` -> `New MCP Server`.

    Then, paste the MCP server configuration.
  </Accordion>

  <Accordion title="Junie">
    Follow the instructions in the [Junie documentation](https://www.jetbrains.com/help/junie/model-context-protocol-mcp.html#bksdkr_21) to install the Herd MCP server using the standard configuration above.
  </Accordion>

  <Accordion title="Windsurf">
    Follow the instructions in the [Windsurf documentation](https://docs.windsurf.com/windsurf/cascade/mcp) to install the Herd MCP server using the standard configuration above.
  </Accordion>
</AccordionGroup>

## Available Prompts

### `debug_site`

Perform debug operations on a site. This includes retrieving executed query information, dispatched jobs, logs, dumps calls, outgoing HTTP requests and more.

## Available Resources

### `site_information`

Returns information about the current site, such as the correct local URL, environment variables, used PHP versions and Node versions.

## Available Tools

The Herd MCP server provides the following tools to your AI agents:

### `find_available_services`

Get a list of available services (such as MySQL, Typesense, Redis, Laravel Reverb, Typesense, etc.) on your system. This will also return the environment variables needed for each service to connect and configure it.

### `install_service`

Install a service on your system. This will download the service's binary, configure it, and start it.

**Parameters:**

* `type`: The type of service to install.
* `port`: The port to use for the service.

### `start_or_stop_service`

Start or stop a Herd provided service on your system.

**Parameters:**

* `shouldStart`: Whether to start or stop the service.
* `type`: The type of service to start/stop.
* `port`: The port of the service to start/stop.
* `version`: The version of the service to start/stop.

### `get_all_php_versions`

Get a list of all PHP versions and their status (installed, in-use, etc.) from Herd.

### `install_php_version`

Installs or updates a specific PHP version on your system

**Parameters:**

* `version`: The PHP version to install (e.g. `8.3`).

### `get_all_sites`

Get a list of all sites provided by Laravel Herd on your system. This includes information such as site names, URLs, paths, secure status, environment variables, the PHP version that is used, and more.

### `secure_or_unsecure_site`

Secure or unsecure a site by enabling or disabling HTTPS. The site will then be available at `https://{siteName}.test`.

**Parameters:**

* `shouldSecure`: Whether to secure or unsecure the site.
* `siteName`: The name of the site to secure/unsecure.

### `isolate_or_unisolate_site`

Isolate or Un-isolate a site. Isolating means that the site will use a specific PHP version, rather than the global PHP version. Un-isolating removes this isolation and uses the global PHP version for the site.

**Parameters:**

* `shouldIsolate`: Whether to isolate or unisolate the site.
* `siteName`: The name of the site to isolate/unisolate.
* `phpVersion`: The PHP version to use for the site.

### `get_last_deployment_information`

Returns information about the last deployment from Laravel Forge, if the local site is linked with a Forge site.


# Directories and Files
Source: https://herd.laravel.com/docs/macos/advanced-usage/directories-and-files



# Herd Directories and Files

You may find the following files and directories helpful while you are troubleshooting issues with Herd.

## Main directory

The main directory contains all the following config files and directories and is a good start when troubleshooting issues with Herd. You may delete this folder if you plan to re-install Herd from scratch.

```bash  theme={null}
~/Library/Application Support/Herd/
```

## Binaries

You can find all binaries of Herd in this directory. This includes binaries like composer or expose that ship with Herd as well as downloaded binaries like the latest PHP versions.

```bash  theme={null}
~/Library/Application Support/Herd/bin
```

## Config

All config files for all Herd services live in this directory.

```bash  theme={null}
~/Library/Application Support/Herd/config
```

### nginx

The nginx directory contains a `herd.conf` and the `nginx.conf`. Herd uses both to decide which sites it serves and what happens to files. In case you see a `Bad Gateway` error, there could be an issue in one of these files.

```bash  theme={null}
~/Library/Application Support/Herd/config/nginx
```

Site-specific Nginx configuration files are located in the following directory:

```bash  theme={null}
~/Library/Application Support/Herd/config/valet/Nginx
```

### php

This directory contains all `php.ini` files for all PHP versions on your machine. If you use Herd Pro, it also contains `debug.ini` files that Xdebug uses when you enable it for a request. If you're in debug mode, Herd loads the normal `php.ini` and applies the `debug.ini` on top.

```bash  theme={null}
~/Library/Application Support/Herd/config/php
```

### Log

Herd stores all logs of nginx and php-fpm in this directory. It may also contain mail logs if you use Herd Pro.

```bash  theme={null}
~/Library/Application Support/Herd/Log
```


# Command Line
Source: https://herd.laravel.com/docs/macos/advanced-usage/herd-cli



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


# Shortcuts
Source: https://herd.laravel.com/docs/macos/advanced-usage/shortcuts



# Shortcuts

Herd comes with global shortcuts that integrate with your system and make accessing your current project easier than ever.

You can set up these global shortcuts in the settings.

<Frame>
  <img alt="Screenshot of shortcut settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=09c0d5e7dd753d6b8f9b46f26fb969ea" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_shortcuts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0ce05efb12620f749c8009c1bbe732ee 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8ad26897fb96de60d49dc0da581642a0 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=28e1d47b48ad137ed37d4215afc73673 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=16699190e22595bd35f284357e859191 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=65f33c307eeda1de75a3c9e6e58eefa5 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6db8a6b3c6e9ce44053e4f15dbbed475 2500w" />
</Frame>

Herd supports the following shortcuts:

* Open `php artisan tinker` or [Tinkerwell](https://tinkerwell.app) for the active project
* Open the path of the active project in your terminal
* Open the list of sites in Herd
* Open Dumps
* Enable/Disable dump interception
* Clear all dumps
* Open Mails
* Open Log Viewer

Every time you serve a site by opening the site in your browser, this site becomes the active project and Herd remembers its URL and path.

## Terminals

When a shortcut opens a terminal, Herd uses the terminal that you select in the settings. Herd supports the default Terminal, [iTerm](https://iterm2.com/) and [Warp](https://www.warp.dev/) – but Warp does not come with the possibility to run commands after it opens, so it doesn't have the same convenience as the default Terminal or iTerm.


# Social Authentication
Source: https://herd.laravel.com/docs/macos/advanced-usage/social-auth



# Implementing Social Authentication

When implementing social authentication in your Laravel application, you may face the issue that Herd's `.test`
domain is not recognized by the social authentication providers. This is because they often require a public top-level
domain (TLD) for their callback URLs. Herd does not support changing the `.test` domain to a public TLD, because
that would introduce serious security issues to your machine – but we can work around this.

## Using the fwd.host Webservice

We've created a web service that acts as a proxy for your redirects and does not store any data. You can use this service
to handle social authentication callbacks by setting your callback URLs to `https://fwd.host/http://your-herd-site.test/auth/callback`.

This way, the social authentication provider will redirect to `fwd.host`, which will then forward the request to your Herd site.

You can see the setup in the following screenshot:

<img src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=814d601ef3ce2050cd09c3df58f1c007" alt="Social Authentication Setup" data-og-width="2302" width="2302" data-og-height="1720" height="1720" data-path="images/docs/google-oauth-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9d21f517f270cbadd29aa0a7a08aff48 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e2dd9f8392d3f66562d04da1f9516304 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=791c0988a80fac5a566615ceaa1a1b3b 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ed193bb809eee279eb3963e8c9033eb1 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=81b69d62297bb67c4ccb12c77889e98b 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/google-oauth-setup.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dfcdc0dca72961bb443efeb5030c8369 2500w" />

The `fwd.host` service will forward the request to your Herd site, allowing you to handle the social authentication as usual.
For security reasons, the redirects are limited to Herd sites with `.test` domains only, so you cannot use this service to redirect to any other site.


# Changelog
Source: https://herd.laravel.com/docs/macos/changelog/index



<Update label="1.23.0" description="2025-11-04">
  ## New features

  * Herd Pro now adds support for installing Valkey 7.x and 8.x services
  * Reopening Herd now opens up the General settings screen

  ## Fixes and Improvements

  * Updated the Laravel installer and Composer to the latest versions
  * Improved the overall site UI performance
  * Improved the onboarding process for new users
  * Fixed deprecation warning that appeared when using Adminer
  * Fixed an issue where copying the site URL would copy the path instead
  * Fixed a rare crash that could occur when securing a linked site via the UI
  * Fixed an issue where the query interception would throw an error when no database version could be determined
</Update>

<Update label="1.22.3" description="2025-09-18">
  ## Fixes and Improvements

  * We fixed a macOS Tahoe issue when trying to link an existing site via the site wizard.
  * You can now run `herd db` via the CLI to open the current database connection in TablePlus.
  * Herd Pro users can now install any available service version, not just the latest one.

  Note: Version 1.22.2 was skipped due to an internal build issue
</Update>

<Update label="1.22.1" description="2025-08-20">
  ## Fixes and Improvements

  * The MCP server now supports Junie's MCP protocol version
  * We fixed an issue where mails without the `Message-ID` header would not update in the UI properly
  * When toggling the dump interception, the `dump` calls behave as they should and return the dumped values.
</Update>

<Update label="1.22.0" description="2025-08-13">
  ## New Features

  Herd now ships with an MCP server that gives your AI clients tools and resources to interact with Herd, manage sites, services, PHP versions and much more.

  ## Fixes and Improvements

  * Fixed onboarding loop when Valet is detected
  * Fixed a bug where the wrong IDE opened when clicking on file locations in dumps
  * Updated the built-in cacert.pem file
</Update>

<Update label="1.21.0" description="2025-07-14">
  ## New features

  * You can now start using PHP 8.5 alpha1!
  * The Dumps UI can now detect Laravel Cache activity
  * Onboarding now allows users to select a different path to park instead of `~/Herd`

  ## Fixes and Improvements

  * Zed is added to the list of available IDEs
  * The shortcut settings are horizontally resizable
</Update>

<Update label="1.20.2" description="2025-05-28">
  ## Fixes and Improvements

  * We fixed an issue with dark-mode support for the new SQL highlighting in the Dumps window
  * We fixed an issue that resulted in a crash when sending mails to the local mailserver
</Update>

<Update label="1.20.1" description="2025-05-27">
  ## Fixes and Improvements

  * We fixed an issue with the mailserver in combination with CC email recipients
  * The selected dump type filter now remains in effect after clearing the dumps
  * Searching for text within collapsible strings in the dumps window is now possible
  * New instances of the “Reverb” service now contain a debugging dashboard that can be opened from the services window
  * Updated the built-in cacert.pem file
</Update>

<Update label="1.20.0" description="2025-04-16">
  ## New features

  * The "Sites" window is now integrated into the settings and received a major design overhaul
  * You can now add "aliases" (links) right from the sites UI, by right-clicking on a site in the list
  * Sites with aliases/links now get grouped together
  * You can now hide sites that do not have a valid driver
  * Sites can be grouped individually
  * The PHP ini settings can now be configured for each installed PHP version individually

  ## Fixes and Improvements

  * Updated the built-in Composer binary
  * Using `herd isolate` with a PHP version that is not yet installed, now installs the specified version
  * We fixed an issue where NVM / Node would not get properly detected if your default shell is bash
  * We fixed an issue with NVM not being properly installed on macOS Sequoia 15.4
  * The ability to delete sites was moved to the context menu
</Update>

<Update label="1.19.0" description="2025-04-02">
  ## New features

  * We updated the settings to have a completely refreshed design 💅
  * We prepared Herd to be ready for our official Raycast extension, which will be available soon 👀

  ## Fixes and Improvements

  * The font size for the log viewer can now be adjusted using CMD+/CMD-
  * Cursor is now added to the list of IDEs
  * The site wizard now filters out project paths that no longer exist
  * We fixed a bug where not all service names and ports were detected when using `herd init`
</Update>

<Update label="1.18.0" description="2025-03-11">
  ## New features

  * MariaDB is now available as a service to install (requires Herd Pro)
  * You can now create a new Laravel project using a community starter kit
  * We added support for a new custom URL that allows you to open the site wizard with your custom starter-kit prefilled

  ## Fixes and Improvements

  * Updated the Laravel installer to the latest version
  * Updated cacert.pem to the latest version
</Update>

<Update label="1.17.0" description="2025-03-03">
  ## New features

  * The site wizard now allows you to choose whether you want to use Volt in combination with the new Livewire starter kit or not
  * You can now quick-connect to your services (like MySQL, Redis, etc.) from the menubar
  * We added the ability to easily update the Laravel installer from the "PHP" settings

  ## Fixes and Improvements

  * Updated the Laravel installer to the latest version
  * Updated Composer to the latest version
  * We fixed a potential crash when navigating the site creation wizard with the arrow keys
  * Running `herd open` from the command line no longer shows the Herd dock icon
</Update>

<Update label="1.16.0" description="2025-02-24">
  ## New features

  * We updated the site creation wizard to use the new Laravel Vue, React and Livewire starter kits
  * We added a global shortcut option to quickly open the site creation wizard
  * We added a "Create New Site" option in the menubar to quickly open the site creation wizard
  * You can now right-click on your database services to copy the connection URL to your clipboard

  ## Fixes and Improvements

  * Updated the Laravel installer to the latest version
  * Updated Expose to the latest version
</Update>

<Update label="1.15.0" description="2025-02-19">
  ## New features

  * We added a new option to create secure Minio services
  * This releases includes Expose 3.0 and allows you to configure the default Expose server and custom domain in your Herd settings

  ## Fixes and Improvements

  * Updated composer to the latest version
  * Updated the Laravel installer to the latest version
  * Fixed an issue where deleting the Herd keychain passwords could result in an application crash
  * Fixed an issue when using `herd proxy` without the secure flag
  * Fixed an issue when running `herd init` with PHP 8.4
</Update>

<Update label="1.14.1" description="2025-01-10">
  ## New features

  * We re-wrote the internal mail server to be more performant (and by that reduced the app size by 50%)
  * The default PHP version for new Herd installations is now 8.4

  ## Fixes and Improvements

  * Fixed in issue in 1.14.0 that could result in a 502 Bad Gateway when intercepting a lot of dumps, queries, views, etc.
  * Updated Expose to be PHP 8.4 compatible
  * Updated Composer to the latest version
  * Updated the Laravel installer to the latest version
  * Running `herd open` now properly starts Herd if it's not running already
  * Xdebug 8.4 now contains the correct PHP extension for Intel-based Macs
  * When SSHing into a Forge server, you're no longer in the public folder
  * Various UI improvements for the site wizard
  * Fixed an issue when the only installed PHP version was 8.4
  * Running `herd ini` in an isolated project now opens the isolated PHP version's ini file
  * Fixed an issue that would show deprecation warnings in the Expose token configuration screen
  * The app now notifies you when your Herd Pro license expires soon
  * Fixed an issue where the site information would not be shown in the site settings
</Update>

<Update label="1.14.0" description="2025-01-09">
  ## New features

  * We re-wrote the internal mail server to be more performant (and by that reduced the app size by 50%)
  * The default PHP version for new Herd installations is now 8.4

  ## Fixes and Improvements

  * Updated Expose to be PHP 8.4 compatible
  * Updated Composer to the latest version
  * Updated the Laravel installer to the latest version
  * Running `herd open` now properly starts Herd if it's not running already
  * Xdebug 8.4 now contains the correct PHP extension for Intel-based Macs
  * When SSHing into a Forge server, you're no longer in the public folder
  * Various UI improvements for the site wizard
  * Fixed an issue when the only installed PHP version was 8.4
  * Running `herd ini` in an isolated project now opens the isolated PHP version's ini file
  * Fixed an issue that would show deprecation warnings in the Expose token configuration screen
  * The app now notifies you when your Herd Pro license expires soon
  * Fixed an issue where the site information would not be shown in the site settings
</Update>

<Update label="1.13.0" description="2024-11-27">
  ## New features

  * When re-opening "Herd" (for example via Spotlight) while the app is already running, the menubar will now be opened
  * We added PHP 8.4 compatible versions of Xdebug and our Herd dump interception feature

  ## Fixes and Improvements

  * Updated composer to the latest version
  * Added a check so that `composer self-update` will not be overwritten when restarting Herd
  * Updated the built-in Laravel Installer
  * Fixed an issue where the "SSH" button would not do anything in combination with the macOS default Terminal
  * Fixed a warning that could occur when running `herd init`
</Update>

<Update label="1.12.0" description="2024-11-13">
  ## New Features

  * We added a new `herd ini` CLI command that opens up the ini file in your configured IDE.

  ## Fixes and Improvements

  * Improved PHP 8.4 support
  * Fixed an issue where the automatic Xdebug detection would not work
  * Fixed a deprecation issue that could show up in a specific edge case
  * Fixed a potential crash when searching in the Sites window and closing/reopening the UI
</Update>

<Update label="1.11.2" description="2024-10-29">
  ## Fixes and Improvements

  * We updated the site creation defaults to match with the Laravel CLI installer (Pest is now the default test runner)
  * We fixed an issue where custom MySQL configuration values would not be used
  * Fixed a race-condition related crash that could occur with a lot of dumps coming in at once
  * Opening the terminal via the GUI now works for sites with spaces
  * `herd init` now successfully automatically starts already existing services
  * The `herd.yml` file now supports multiple services of the same type + version on different ports across multiple projects
  * Clicking on settings/services now properly brings the window to the front
  * Running `herd link` will now remove any existing link for the project first
  * `herd init` will no longer add the folder name as a project alias
  * We added the `PHP_INI_SCAN_DIR` directive to FPM, so that FPM can load additional php.ini files in your config folders
  * We fixed an issue where the Herd dock icon would remain visible when using a specific macOS setting
  * Fixed an infinite open/close loop when using the site creation wizard on older macOS versions
  * Fixed an issue where the `herd_auto_prepend_file` directive would get ignored
  * Fixed an issue when trying to intercept HTTP requests without cookies
  * Using the dump features in combination with Lumen no longer throws an error
  * Updated the Laravel Installer
</Update>

<Update label="1.11.1" description="2024-10-01">
  ## Fixes

  * Fixed an issue when using the forge CLI without a linked Herd integration
  * Fixed NVM detection in combination with "GREP\_OPTIONS"
  * Disabling dump interception features now force-stops FPM instances
  * Ignore stderr output when running AppleScript commands
  * Updated mailserver binaries to fix timeout issue and Symfony asset handling
  * Pressing "Esc" when editing a Herd service now properly reset the form
  * We added a "Watch via CLI" toggle in the dump settings, so queries no longer get sent to the dump UI when running PHP from the CLI (for example by running tests)
  * Clicking on Dump tabs now works on macOS 15
  * Updated the Laravel Installer
</Update>

<Update label="1.11.0" description="2024-09-12">
  # New Features

  * **Forge Integration:** Connect local sites with Laravel Forge and deploy them from the Herd UI or via CLI
  * **Profiler:** Quickly identify bottlenecks in your application by making use of the `herd profile` CLI command and the `/herd-profiler` route
  * **Herd.yml:** Share site configurations with your team
  * **Reverb TLS support:** Launch secure Reverb instances with effortless TLS certificates
  * **Dump Improvements:** Dump Eloquent queries, outgoing HTTP requests, logs, jobs and Blade views without installing a package

  # Fixes

  * When you manually change your nginx configuration to serve on all IP addresses, Adminer will no longer be served on unsecured sites
  * The `herd proxy` command is now fully functional
  * The IDE can be started from the sites list again
  * Changing the max upload file size in the PHP settings now also updates the nginx configuration
  * When running `herd secure`, you will only need to trust the CA certificate once. Future `herd secure` calls will no longer require your admin password.
  * We fixed an issue where setting an invalid "Dump" port could crash Herd
</Update>

<Update label="1.9.1" description="2024-07-10">
  # New Features

  * We’ve added PHP 8.4 alpha 1 to the PHP download manager
  * Herd Pro: Services create and honor configuration files for MySQL, PostgresQL and redis
  * Herd Pro: You can open the path of service binaries via right click from the service settings
  * You can star a favorite sites within the Sites UI to sort it to the top
  * We added a herd edit command to open your favorite IDE in the current working directory of your terminal

  # Fixes

  * Disable binary log files for MySQL service
  * Fixes a problem when isolating sites with PHP 8.4
</Update>

<Update label="1.9.0" description="2024-07-10">
  # New Features

  * We’ve added PHP 8.4 alpha 1 to the PHP download manager
  * Herd Pro: Services create and honor configuration files for MySQL, PostgresQL and redis
  * Herd Pro: You can open the path of service binaries via right click from the service settings
  * You can star a favorite sites within the Sites UI to sort it to the top
  * We added a herd edit command to open your favorite IDE in the current working directory of your terminal

  # Fixes

  * Disable binary log files for MySQL service
</Update>

<Update label="1.8.0" description="2024-07-01">
  ## New Features

  * The Sites UI has moved to its own window. You can check a preview of your site, get information about your application, open the database and much more!
  * Sites can now be deleted

  ## Fixes and Updates

  * We updated the drivers for Statamic
  * We fixed an issue where services like FPM would be marked as inactive, even though they were running
  * The beta version of macOS Sequoia showed an empty window on application startup, which is now fixed
  * We fixed a rare crash that could occur when opening the log viewer with specific sites
</Update>

<Update label="1.7.1" description="2024-06-13">
  ## Fixes

  * Fixed an issue where the helper service could consume 100% CPU or crash
  * Fixed an issue where new users were not able to resolve `.test` domains
</Update>

<Update label="1.7.0" description="2024-06-12">
  ## New Features

  * You can now change the sort order of `dump()` cards in the Dump UI
  * Clicking on a dump location now opens your configured IDE
  * The font-size of dumps can be changed using CMD +/-
  * The log viewer is now framework agnostic and has support for WordPress log files

  ## Fixes and Updates

  * We updated the built-in Laravel installer and composer versions
  * Opening the dumps window no longer causes a CPU/energy consumption spike
  * Herd no longer requires a sudoers file and uses a privileged helper instead
</Update>

<Update label="1.6.1" description="2024-05-07">
  ## Fixes and Updates

  * We updated the built-in Laravel installer and composer versions
  * You can now select the parked path in a UI picker when creating a Laravel site via the wizard
  * Fixed a minor UI glitch when opening/closing service settings
  * Fixed an issue where random empty Node versions would appear in the UI
  * `herd stop` and `herd start` now properly starts and stops all services
  * Herd now supports an accessibility mode for people with color blindness
  * We fixed an issue where long service logs would cause the app to become slow/unresponsive
  * You can now skip Herd's NVM installation during the onboarding process
  * `herd log` now uses the correct paths
  * Fixed an issue where the Node update badge kept being visible
</Update>

<Update label="1.6.0" description="2024-04-15">
  ## New Features

  * PostgreSQL 14, 15 and 16 are now available including popular extensions (PostGIS, pgrouting, pgvector, and more)
  * Typesense can now be setup as a Laravel Scout compatible search service
  * Service binaries now get symlinked during installation for easier access
  * Services like PostgreSQL, Redis and MySQL now give you an "Open in TablePlus" option in the UI
  * We added a local "clear dump" shortcut (CMD+K) when the "Dumps" window is focused
  * You can now use the new `herd coverage` CLI command to start PHP scripts with code coverage enabled

  ## Fixes and Updates

  * We updated the built-in Laravel Installer
  * The log viewer properly handles logs with the same timestamp and log level
  * A very bad internet connection no longer leads to deactivated Herd Pro licenses
  * The Xdebug browser extension detection properly works with trace and profile mode
  * We improved the NVM installation and detection error handling
  * Fixed an issue where a "warpified" shell would lead to errors using NVM from the UI
  * Fixed some Laravel Reverb related environment variables
  * We renamed "Real-Time" in the services view to "Broadcasting"
</Update>

<Update label="1.5.0" description="2024-03-12">
  This updates adds an exciting new Herd Pro feature: **Services**

  You can now easily create and manage all of your loca development services inside of Herd. Start a new MySQL server, spin up Redis for your local queue driver, integrate Laravel Scout using a local Meilisearch server, simulate S3 uploads using MinIO, or start your next real-time application using Laravel Reverb.
</Update>

<Update label="1.4.2" description="2024-03-05">
  * Updated nginx to the latest version and migrated your secured config files
  * Updated the Kirby driver
  * Fixed an issue where Herd could become unresponsive due to the log viewer
  * Fixed an issue where the Herd debug socket would not properly start/update
</Update>

<Update label="1.4.1" description="2024-02-13">
  * When using an unsupported shell, the sites list is no longer empty
  * Fixed an issue where non-HTML mails (for example Wordpress) would not show up in the Herd Pro Mail UI
  * The "Mail" service is no longer visible, when not using Herd Pro
  * The onboarding now downloads PHP 8.3 by default
  * Fixed an issue when only serving PHP 7.4 sites
  * Updated the built-in Composer binary
</Update>

<Update label="1.4.0" description="2024-02-05">
  ## 1.4.0 Changelog

  This update adds new features, improves existing ones, and comes with an upgrade option to Herd Pro. While Herd Basic ships with everything that you need to develop Laravel applications, Herd Pro introduces new capabilities and convenience functions for professional users.
  Get Herd Pro at [herd.laravel.com](https://herd.laravel.com) or open the settings to start the upgrade process.

  ### Herd Basic

  * Added the possibility to install and use NVM (Node Version Manager) within Herd to quickly manage your Node environments
  * Added optional Xdebug extension
  * Added an opt-in beta channel for the latest updates
  * Added an option to disable notifications for PHP updates
  * Added an option to select your IDE to quickly open a project from the sites list or the log viewer

  ### Herd Pro

  * Dumps: Intercept `dump` and `dd` calls and display them in an external window
  * Mail: Use the internal mail server and client to test and debug local emails
  * Logs: Trail and search through local log files of all your projects
  * Xdebug detection: Automatically enable Xdebug when setting a breakpoint in PHPStorm or enabling the debug mode via a browser extension
</Update>

<Update label="1.3.2" description="2024-01-11">
  * Added a new "Force Stop All" option (visible when pressing option key while the menubar is open) to make it easier to stop stray services
  * Fixed default output buffering when configuring PHP versions
  * Fixed `herd share` issue when sharing secured sites
  * Fixed an issue where symlinked `.zshrc` files would be overwritten
</Update>

<Update label="1.3.1" description="2023-10-11">
  * You can now easily configure common PHP.ini settings in the UI
  * Fixed a bug where memory\_limit=-1 would not be properly pre-loaded in the UI
  * Added support for the new Livewire Volt functional/class API option in the app creation wizard
  * Update the built-in Laravel installer
</Update>

<Update label="1.3.0" description="2023-10-11">
  * You can now easily configure common PHP.ini settings in the UI
  * Added support for the new Livewire Volt functional/class API option in the app creation wizard
  * Update the built-in Laravel installer
</Update>

<Update label="1.2.2" description="2023-09-27">
  * Update the built-in Laravel installer
  * Added support for new Jetstream options in the app creation wizard
  * Added support for the new Livewire/Alpine Breeze starter kit in the app creation wizard
</Update>

<Update label="1.2.1" description="2023-09-25">
  * Removed the height of the menubar icon
  * Fixed a bug when trying to access a secured Herd site, from within another secured site
</Update>

<Update label="1.2.0" description="2023-08-21">
  * The Sites UI can now be opened via a global shortcut
  * We added a Laravel project creation wizard in the Sites UI
  * You can now configure a global shortcut to open "php artisan tinker" or Tinkerwell in the last visited site path
  * The Sites UI now also has a button/icon to manually open tinker/Tinkerwell in a given path
  * You can now configure a global shortcut to open the last visited site in the Terminal
  * Configure the default Terminal that Herd should open (Terminal, iTerm2 or Warp)
  * Herd now supports custom Valet drivers properly
  * We fixed a bug where the "Herd" folder would get recreated on every application start, even if it wasn't used.
  * We fixed a security related issue in Herd. You will need to provide your password after the update is installed to apply the new settings automatically.
</Update>

<Update label="1.1.2" description="2023-08-04">
  * The Laravel installer is now updated to version 5 and uses Laravel Prompts
</Update>

<Update label="1.1.1" description="2023-07-28">
  * Fixed an issue where copied custom Valet drivers would not load properly
</Update>

<Update label="1.1.0" description="2023-07-28">
  ## New Features

  * Herd now downloads the latest PHP 8.2 binaries during onboarding
  * Each PHP version has its own php.ini file and folder
  * The site list can be refreshed from the UI
  * Sites can be opened in the default browser from the UI
  * Custom Laravel Valet drivers now get migrated during onboarding

  ## Bugfixes

  * Fixed site list not showing up in some scenarios
  * Fixed a bug when securing / unsecuring sites from the UI
  * Fixed an issue where nginx on Intel Macs still required a Homebrew dependency
</Update>

<Update label="1.0.8" description="2023-07-17">
  * Updated the built-in Laravel Installer
</Update>

<Update label="1.0.7" description="2023-07-17">
  * Updated the built-in Laravel installer
</Update>

<Update label="1.0.6" description="2023-07-12">
  * Improved styling of 404 page
  * Fixed `start / stop / restart` commands
  * Fixed `use` command
  * Updated PHP 8.2 binaries for Intel chips
  * Ensures that Herd is located inside the Applications folder to prevent "File not found" error
</Update>

<Update label="1.0.4" description="2023-06-29">
  # Initial release
</Update>


# Dumps
Source: https://herd.laravel.com/docs/macos/debugging/dumps



# Debugging with Dumps

The Dumps feature can automatically intercept all `dump()` calls in your code and display them in a separate window instead of rendering them in the browser or CLI. But that's not all, it can also show HTTP requests, logs, Eloquent queries, dispatched jobs and Blade views to give you all the integrations that you need when debugging your app.

## Using Dump features

You may open the Dumps Window via the Herd system tray menu or open it with a globally configurable shortcut that you can define in the [shortcut settings](/macos/advanced-usage/shortcuts).

In order to enable dump interception and record debug information, click on the antenna icon in the title bar of the window. The icon will flash to indicate that dump interception is enabled.
Once enabled, you may use the `dump()` function as usual. Instead of printing the dump to your browser or terminal, Herd will open a window when a new dump becomes available.

<Frame>
  <img alt="Empty state of the dump interceptor window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7973a904c46a0dc312a1ee2725f8fe8f" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_empty.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=705d5dd6a54bc84ba928330f4bcdc197 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=38bd222ca3acba2d0dbb39ef3b39eb2a 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=79853ad0b4e11a170da6df6cc97221eb 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=06c21aa6b1cddcf9732796e00335ff41 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a7b92ce7836403291bab73a169bdedc4 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_empty.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=588c2aa98ba24efc6b6405bafb6eb45e 2500w" />
</Frame>

New dumps are automatically added to the top of the window, and you can clear the window by pressing the icon in the title bar of the dump window. All dumps are searchable so you can easily find what you are looking for.

By default, Herd only displays the output of the latest request, but you can enable persistent storage between requests in the settings. This keeps a history until you close the Dumps Window.

## Settings

You can select which features you need when you start debugging, so that your requests stay as fast as usual and there's no bloat when digging into a problem.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3b975ef5a985eb2051d8015d73d64a92" data-og-width="1844" width="1844" data-og-height="1342" height="1342" data-path="images/docs/dumps_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a3ce4cef8e7af2c5bd71f8cc549e1cb0 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=29cbe8f9f64e084d45280079f41e6d28 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=19c8014aa53e82cd33f2387469eb2e80 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b452cc108274a1006e4821ab70fe3bf6 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d940a060b7211ef941f030dc71e416fc 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7ac8ec169b70cdad36a87080fd8028a1 2500w" />
</Frame>

## Dumps

When enabled, all dumps that you run via Laravels' `dump()` or `dd()` methods automatically go to the Dumps Windows instead of your browser. This has the advantage that the dump doesn't break your layout and SPAs still work.

This also sends `dump()` calls from queued jobs to the dump window that you wouldn't see in your browser when working with real queues.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dbb2744e5da4680251b9cc53470a58d8" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_dumps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c5d347e21953a8c71401645852a84f52 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=19ccdbef3cc55bdc058875a1b4b843f2 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=da11d625775e0c89fb00ee76e0c98590 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=94c896c42dcd7112e4abfee68c24e8d2 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7b9a36da2a35b803d5ba58eb2b48d045 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_dumps.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=435d785ec47d592fc6550101fd0f40d3 2500w" />
</Frame>

## Queries

You can display and debug Eloquent queries by enabling the query feature in the settings. If you want to debug specific queries, you can select the duration for these queries and skip fast ones which are good to go.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3c9b2df17fdb07f514b8b629062a6d1e" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_queries.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c7912a761607e4aca0b3e802699643fd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cfeded8e039d7122631c7e84dd416dae 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ee62c16030165b595438c187b392f648 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=be56d44a0d3bc98dfc7f0be301c9397c 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e6a1b4ff5ddd0173749b3c5984a06450 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_queries.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8384c5202acdb3b9780a929dd3b023ee 2500w" />
</Frame>

## Jobs

Enable job logging to get a list of all jobs that your application runs. This is super useful when you work with the sync driver and are not sure if all jobs are properly triggered.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=17edcb26c0209c8a4d0b50acb973c6cc" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_jobs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b2e459d4c4bbd40006720761c16e3b4b 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ca4e266c8534dab594ae9734f1edb37a 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1806e609efa993ba3fe6c548cb441943 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=29a615d5299abc81c934c3fea72b17c2 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4ea40ea5c84f17c4a4baaa2848094604 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_jobs.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dfe63cfeb97d12226f28db4b825aeaa9 2500w" />
</Frame>

## Views

Sometimes, you want to know which data gets passed to a view and which views your application loads on a specific site. This tab lists all views that Laravel renders during a request.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2b641e70287d56f352a5a27ecd8a5f9c" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_views.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a5b68586ae7337563b474523df5828c1 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8332c987ef604a504e9ea553ee3e2b33 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0234bab3984288b0cee382c286d6dbb6 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=233c9ca7832780c8f3e5cc14dbb6777d 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6fe6eb6cc4be00a4235f81d5e800ac56 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_views.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f742cd71c26c2b8f3bce1e41f4324705 2500w" />
</Frame>

## HTTP

The request tab displays all outgoing HTTP requests of your application, so if you're working with an API, these calls show up in the Dumps Window and allow you to inspect them without searching through logs etc.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cf803e7594d260eccaaf4bb9e9151ca7" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_http.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8d806c654a54b9d11b8db71d951e47da 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ecd25ff0b48b031b23db8d659fb03e52 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7412fad1f05b0f4975ae826a2d00def7 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=770a51ce159b362d553b80418acae88a 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=943226cfbc27468c4543952fed47c43f 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_http.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=058a95a0e66a4aa1700c52f16d68afd5 2500w" />
</Frame>

## Logs

You can get all logs of a request without using Herd's Log Viewer or digging through log files.

<Frame>
  <img alt="Dump Window" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dc2835c70da47ce8a5fb14dc25302f54" data-og-width="1654" width="1654" data-og-height="1166" height="1166" data-path="images/docs/dumps_logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7b0ce7dba9cc5c25b7c5effa5a268fe2 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7e1505019d523af2c05e74f9c5dc9611 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=44dc4e886f2fc5cafc500d66d4a1b770 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ce6fbf79d665071f43d7b51e38de511f 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b87bf6fb54b1d4085db859f3c5974cbd 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_logs.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5865ff7ae4d6062b85fe03a2d2048549 2500w" />
</Frame>

## Troubleshooting

The dumps feature uses Herds' own PHP extension so make sure it is present in your `php.ini` and the path to the extension is correct. If you think that there is a problem with the path, simply quit Herd, remove the extension from the ini file and start Herd again. This will add the extension to the configuration file with the correct path.

```ini  theme={null}
extension=/Applications/Herd.app/Contents/Resources/herd-ext/herd-83-arm64.so
```

Technically, Herd uses this extension to inject code into your codebase in very early stages of the bootstrapping process. So if you're facing issues within your application, you might want to disable some or all of the features in the [settings](#settings).


# Log Viewer
Source: https://herd.laravel.com/docs/macos/debugging/logs



# Inspect local log files

If you don't want to run a terminal command like `tail` or tail the logs with [Laravel Pail](https://laravel.com/docs/11.x/logging#tailing-log-messages-using-pail), you can use Herd's integrated log viewer. It allows you to inspect your log files in great detail and makes searching through logs a breeze.

If you are only interested in the logs of the latest request, you man use the [log view](/macos/debugging/dumps#logs) of the [Dumps](/macos/debugging/dumps) feature to get the most recent logs automatically.

<Note>
  This feature requires PHP 8.0 or later
</Note>

Herd automatically polls for new logs every few seconds as long as the Logs window is open.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=722a74dd322c7ae6e4f814297dc11a7e" data-og-width="2454" width="2454" data-og-height="1512" height="1512" data-path="images/docs/log-viewer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a1b672928847ec2027725de8dedc06c5 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=99932afca188d8f00c32d07a6e926a52 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=98b86757352ea0696509ce3b84a2fa03 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6d7279117c4554c96b032ad969de144a 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=28886826d371c2614ec0bba2b6b6aca5 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/log-viewer.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6c72789e4efdce24c3853bb04956bfc1 2500w" />
</Frame>

## Selecting a Project and Log File

By default, the log window shows the latest log file of the last project that you visited in your browser. This allows you to quickly find the latest log file, but you can also switch between all projects that Herd knows and serves.

If your project includes more than one log file, for example when using daily log rotation, you can select the log file on the left.

## Searching in Log Files

The search bar at the top searches through all logs and allows you to pinpoint all log entries that match your search query. You can hit Cmd+F in the text area that shows the details of the entry and search within this single entry.

## Custom log paths

Herd looks for logs in the framework-specific standard directory, such as `storage/logs` for Laravel. You can change that directory and even add multiple log directories by using a [custom driver](/macos/extending-herd/custom-drivers#customize-herds-behaviour) for that application.


# Profiler
Source: https://herd.laravel.com/docs/macos/debugging/profiler



# Profiling Applications

Herd supports a customized version of the [SPX profiler](https://github.com/beyondcode/php-spx) for PHP. The profiler allows you to identify bottlenecks in your application and supports profiling web and CLI requests.

## Installing the profiler extension

You can download and install the profiler extension by running this command in your terminal:

```bash  theme={null}
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/beyondcode/php-spx/HEAD/install.sh)"
```

This command downloads the extension and moves it to your Herd application directory and also adds it to all your existing `php.ini` files. If you install a new version, please run this command again to add it to this version automatically.

The extension does not profile requests automatically and requires environment variables or specific headers to record and profile the request, so you can keep it enabled without slowing down your normal setup.

## Profiling Web Requests

You can either open the profiler dashboard from the site configuration of the Site Manager or by opening the `/herd-profiler` route of your application. This route is dynamically added to requests when you enable the profiler in the settings.

### The Profiler Dashboard

Herd uses the SPX extension for PHP to profile your application and display a customized dashboard of your requests. Please make sure to enable the profiling on the top left.

<Frame>
  <img alt="Profiler Dashboard" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8ffc773f2f36d372ad69485d657119f6" data-og-width="2780" width="2780" data-og-height="1998" height="1998" data-path="images/docs/profiler_home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a12fc74bc7ce4ddd49a4c1a88aa63e85 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1135b84d7dabf4a5017ecd4d493afcbb 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e434cc64447717e866aea4e091b2b574 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=25ad2b21d6681c1bc42bdc8a1758fe37 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2ddb2c7b9efe5e182fac51b86577f0fc 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_home.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ff194df4ea6db72de07eb958cfb5da7e 2500w" />
</Frame>

### Results

If you click on a web request in the dashboard, it loads a breakdown of the request and allows you to inspect function calls and other operations in great detail.

<Frame>
  <img alt="Profiler Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5d1beaef8cbac4c8bfbdadd652966c49" data-og-width="2780" width="2780" data-og-height="1998" height="1998" data-path="images/docs/profiler_graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a77e8a04e1a3f6c6d5636827d95a7fe7 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=eb294dbe43e8b630d9c8eb631e8edead 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e4b4aa989c4f80736406b37d44a774e1 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=07046fc0bd56d82052ded457c28761ad 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=80152cbdaf48d3ed3af8af4a0b11ff9e 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_graph.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7b9bb51896147dbf8f3e586a725d2421 2500w" />
</Frame>

## Profiling CLI scripts

While you can profile web requests via the dashboard, SPX has a profiler for CLI requests as well. When the SPX extension is active, you can run PHP scripts with `herd profile` to trigger the profiling process. As an example, you can profile artisan commands with this command:

```bash  theme={null}
herd profile artisan inspire
```

This profiles the command and displays the results directly in your terminal.

<Frame>
  <img alt="Profiler Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=419bdf862fecaac956ab213db874d9e4" data-og-width="2002" width="2002" data-og-height="1086" height="1086" data-path="images/docs/profiler_cli.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=26370ecfe8b2742726a02512ee9e7d90 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=003d26bb704446e783bf942d09960d5b 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c29923905d8423ace4d80d822ba58bec 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a8576aed16b8c335e1857d9766e28626 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=bc3ed9066a95ef04d53a64898b347e80 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/profiler_cli.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ea5e91dcce6d2e7012c06ef36fca6405 2500w" />
</Frame>

## Profiling long-running CLI scripts

When you have long-running CLI scripts, such as daemonized processes, you might want to see profiling information regularly, instead of only seeing them once you end your PHP script.

You can do this by running:

```bash  theme={null}
herd profile --live artisan long-running-task
```

You can learn more about SPX in the [official documentation](https://github.com/NoiseByNorthwest/php-spx).


# Tinker
Source: https://herd.laravel.com/docs/macos/debugging/tinker



# Launching Tinker

Laravel Tinker is a REPL for Laravel, and it allows you to interact with your application via the command line. While you usually start it via the terminal by running `php artisan tinker` or `herd tinker`, Herd provides a convenient button in the actions column in the sites settings as well as a global shortcut that instantly opens the active project automatically.

<Note>
  Herd integrates natively with [Tinkerwell](https://tinkerwell.app) and gives you a fantastic tinker experience with multi-line code editing, autocompletion, and SSH access to your applications.
</Note>

## Open Tinker from the site settings

You can run the Tinker site action from the [Site Manager](/macos/sites/managing-sites) to start a new tinker or Tinkerwell session directly in your site.

<Frame>
  <img alt="Tinker button in the site manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=764428860a4ff3a27c6a190cd356beb7" data-og-width="1872" width="1872" data-og-height="1122" height="1122" data-path="images/docs/sites_actions_tinker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=dca4ecdd340e4b8f549fe61933a75d6f 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3b289646e381fe6b3b339e2680d38b6a 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3b138322002bf217a2361450a49b8d83 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=16bc7f7ed8c20edaea543e4fffaf1a80 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=42c4673523ea794cc48b7f6e0b84b6eb 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions_tinker.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=461e84b5ccc2975374ca6cd63dff5ff4 2500w" />
</Frame>

## Open Tinker with a global shortcut

Herd allows you to define global system shortcuts and Tinker is part of this configuration. By pressing the global tinker shortcut, Herd starts a tinker session for the last site that you visited via your browser.

<Frame>
  <img alt="Tinker Shortcut Settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ce4b61afb1f57650423bb4896fa47c65" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_shortcuts_tinker.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c8ad1723788f6f16a29c84271d4fbeb3 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fbc3d1cf4b07885e97efc8b911da1a06 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=770ef9391e2bbd98f9df47719ad480e0 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=541288637502e1c71a954f82c45d3aa4 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ad21ceb8c8a15a2fce19e88ac1f7ee5c 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_shortcuts_tinker.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e897365d8de8e64da355b1c46ab88791 2500w" />
</Frame>

# Tinkerwell Integration

[Tinkerwell](https://tinkerwell.app) users benefit from the deep integration between both tools, so if you are running `herd tinker`, click the button in the site settings or press the global shortcut and Herd detects Tinkerwell on your machine, Tinkerwell opens a new tab with the most recent Herd project automatically.

This allows you to quickly iterate on complex Eloquent queries or debug some code. It also provides autocompletion and a familiar multi-line code editor experience that goes beyond a simple REPL.

<Frame>
  <a href="https://tinkerwell.app">
    <img alt="Tinkerwell with a complex Eloquent query" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d5e8cb39e5b93c1eef9b80e6034a02e5" data-og-width="2618" width="2618" data-og-height="1720" height="1720" data-path="images/docs/tinker-tinkerwell.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=94dfc8e446dd8bfdefd8b0eb1533f4ab 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=aa479b6622361e78aaf1c7d7d1e57cb8 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6ce7f9b891f4902f98857a60e7583e8f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3e21c433bce09e0d6d15daec1593a324 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=335ba30872c027ca8bd0e5abbe489a3e 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/tinker-tinkerwell.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b2c8d1966135960cdbae323c8b0bb247 2500w" />
  </a>
</Frame>

Tinkerwell ships with support for all of Herds PHP versions and automatically loads the correct configuration files.


# Xdebug
Source: https://herd.laravel.com/docs/macos/debugging/xdebug



# Using Xdebug with Herd

Herd includes support for [Xdebug](https://xdebug.org/), a popular and powerful debugger for PHP.
The free version of Herd ships with Xdebug's PHP extensions out-of-the-box, but you need to manually enable the extension when you need it.

If Xdebug is too much for you and you prefer debugging via dumps, check out the [Dumps](/macos/debugging/dumps) of Herd Pro.

<Note>
  Looking for an even easier way to debug your applications? Check out [Herd Pro's Xdebug integration](/macos/debugging/xdebug-detection).
  It can automatically detect breakpoints in your application and enable Xdebug on-the-fly when necessary.
</Note>

## Enabling Xdebug manually

In order to activate Xdebug, you need to add the appropriate PHP extension to your `php.ini` file. The extensions are located in the Herd application bundle, which you can find in your Applications folder.
The exact location depends on your PHP version and device architecture.

The following extensions are available:

```bash  theme={null}
# Apple Silicon
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-74-arm64.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-80-arm64.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-81-arm64.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-82-arm64.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-83-arm64.so

# Intel
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-74-x86.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-80-x86.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-81-x86.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-82-x86.so
/Applications/Herd.app/Contents/Resources/xdebug/xdebug-83-x86.so
```

After you have located the correct version of Xdebug, you need to append the necessary configuration to your `php.ini` file. For example, the setup for PHP 8.3 on an Apple Silicon Mac looks like this:

```ini php.ini theme={null}
zend_extension=/Applications/Herd.app/Contents/Resources/xdebug/xdebug-83-arm64.so
xdebug.mode=debug,develop
xdebug.start_with_request=yes
xdebug.start_upon_error=yes
```

After saving the changes to your `php.ini` file, you need to restart Herd's services from the menu bar icon, or by running the following command in your terminal:

```bash  theme={null}
herd restart
```

For more information about the available Xdebug settings, please refer to the [official Xdebug documentation](https://xdebug.org/docs/).


# Xdebug Detection
Source: https://herd.laravel.com/docs/macos/debugging/xdebug-detection



# Automatically use Xdebug

Herd Pro is able to detect Xdebug headers in HTTP requests or breakpoints in PHPStorm and routes these requests to a PHP process with Xdebug automatically. This keeps your site super fast on all normal requests but provides advanced debugging capabilities with Xdebug when needed.

<Note>
  If Xdebug is too much for you and you prefer debugging via dumps, check out the Herd take on [Dumps](/macos/debugging/dumps).
</Note>

## Setup with PhpStorm

Go to the debugging settings of Herd Pro and select the configuration to detect breakpoints within PhpStorm automatically.

<Frame>
  <img alt="Debugger Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9e81ce721ccbd7124acd16ecf232c32e" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_debugger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f39f377cfcdc9ac9ed31d3459fc1aeb1 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=95fd49cf07c14b424b079300a116bdce 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2bfc5b2510618d692a172a31561d9d98 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3eb9e2aba8386d23b4d8bc7c6ef227f6 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=80a3c8e802ecad468d4b49cd685b0fb9 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_debugger.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=576e90a1deb0117c8ab10d5ac3233718 2500w" />
</Frame>

When you set or remove a breakpoint in PhpStorm and save the file, this creates a temporary file within the `.idea` folder of your project. Herd parses these files to detect breakpoints.

<Note>
  Please make sure to listen for PHP Debug Connections in PhpStorm after setting the breakpoint so that Xdebug can connect to PhpStorm properly.
</Note>

### Configure PhpStorm to ignore the dump loader

Herd serves sites via a PHP script and if you've dumps enabled, it also uses a `dump-loader.php` file for custom bootstrapping of your application. If you want to debug with Xdebug, it makes sense to configure PHPStorm to ignore this dump loader. You can do that in the settings of PhpStorm by unchecking the boxes for:

* Force break at first line when no path mapping specified
* Force break at first line when a script is outside the project

<Frame>
  <img alt="PHPStorm settings for Xdebug" src="https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=80f7cb10a141eb4059fd44407fa086ed" data-og-width="1964" width="1964" data-og-height="1444" height="1444" data-path="images/docs/xdebug_phpstorm_dump_loader.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=280&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=657609fc2d28245dec793ac50fdde033 280w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=560&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=e3a42e8a3d4f060fdf72332ed39052ca 560w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=840&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=8ec4e40a69e3957fd1d65f322175fdb7 840w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=1100&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=cc1fae3ab352abf5222510f03c368dad 1100w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=1650&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=1231909ebd7cb89186693cbb7c8d58bc 1650w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/docs/xdebug_phpstorm_dump_loader.png?w=2500&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=692b17622a8d3377628f736b7e10570c 2500w" />
</Frame>

If you do not use PHPStorm, you can use browser extensions for Xdebug to automatically load Xdebug.

## Setup with browser extensions

Herd uses the headers of Xdebug browser extensions that you can install via the [Chrome Web Store](https://chromewebstore.google.com/detail/xdebug-extension/aoelhdemabeimdhedkidlnbkfhnhgnhm) or [Firefox Addons](https://addons.mozilla.org/firefox/addon/xdebug-helper-for-firefox).

Once you enable the Xdebug feature in the browser extension, Herd serves the request via a PHP process with an enabled Xdebug extensions.

## Using Xdebug on the command line

You can run CLI commands via `herd debug ..` instead of using `php ...` to use the php binary with Xdebug enabled. For example, if you are debugging an artisan command, you can run `herd debug artisan your:command` to trigger your breakpoint.

## Code Coverage

Herd has a `coverage` command that allows you to run Xdebug's coverage mode on your test suite:

```bash  theme={null}
herd coverage ./vendor/bin/pest --coverage
```

## Troubleshooting

If the detection does not work, please make sure to save the file with the breakpoint after setting or removing the breakpoint.


# Custom Drivers
Source: https://herd.laravel.com/docs/macos/extending-herd/custom-drivers



# Custom Drivers

You can extend Herd with your own drivers to support customized setups of supported frameworks or to add new frameworks and applications that Herd doesn't support out of the box. You can also change the application information tab in the [Site Manager](/macos/sites/managing-sites) or add additional log file directories for the [Log Viewer](/macos/debugging/logs).

## Creating a driver

Herd internally leverages a heavily customized version of [Laravel Valet](https://laravel.com/docs/11.x/valet) for serving sites, and it includes all [drivers](https://github.com/laravel/valet/tree/master/cli/Valet/Drivers) that Valet provides. These drivers are a good start when creating your own custom driver, and it often makes sense to further extend them than starting from scratch.

<Note>
  Please make sure to name the custom driver according to the driver convention. It needs to end on `ValetDriver.php` and a good name for a custom Laravel driver would be `MyLaravelValetDriver.php`.
</Note>

Place your custom driver in the related valet directory on your machine and Herd loads it before serving a site automatically.

```
~/Library/Application Support/Herd/config/valet/Drivers
```

## Customize Herds behaviour

### Log paths

You can customize the paths where the [log viewer](/macos/debugging/logs) looks for log files by adjusting the `logFilesPaths()` method in the driver. The default looks like this:

```php  theme={null}
    /**
     * Get the logs paths for the application to show in Herds log viewer.
     */
    public function logFilesPaths() {
        return [
            "/storage/logs"
        ];
    }
```

The given paths are relative to the application root.

### Application Information

The [Site Manager](/macos/sites/managing-sites) shows a tabular overview of your application in the information tab and you can customize this information to your needs. The default for Laravel applications is the output of the `php artisan about` command.

If you want to customize the overview table, you can do so by defining this method in your applications' custom driver and returning an array like the following:

```php  theme={null}
    public function siteInformation(string $sitePath, string $phpBinary): array
    {
        return [
            "Overview" => [
                "Site Name" => "Laravel Airport",
                "Runway operational" => true,
            ],
            "Flights" => [
                "Today" => 10,
                "Yesterday" => 5,
                "This week" => 22,
            ],
        ];
    }
```

Herd injects the path to the current site and the PHP binary to this method so that you can perform more specific commands and even run code with the correct php version.

## Custom Laravel Driver Example

This example of a custom driver extends the existing Laravel Driver and modifies it to serve the application from a `web` instead of the `public` directory.

```php  theme={null}

namespace Valet\Drivers\Custom;

use Valet\Drivers\LaravelValetDriver;

class CustomLaravelValetDriver extends LaravelValetDriver
{
    /**
     * Determine if the driver serves the request.
     */
    public function serves(string $sitePath, string $siteName, string $uri): bool
    {
        return file_exists($sitePath.'/web/index.php') &&
               file_exists($sitePath.'/artisan');
    }

    /**
     * Determine if the incoming request is for a static file.
     */
    public function isStaticFile(string $sitePath, string $siteName, string $uri)/*: string|false */
    {
        if (file_exists($staticFilePath = $sitePath.'/web'.$uri)
           && is_file($staticFilePath)) {
            return $staticFilePath;
        }

        $storageUri = $uri;

        if (strpos($uri, '/storage/') === 0) {
            $storageUri = substr($uri, 8);
        }

        if ($this->isActualFile($storagePath = $sitePath.'/storage/app/public'.$storageUri)) {
            return $storagePath;
        }

        return false;
    }

    /**
     * Get the fully resolved path to the application's front controller.
     */
    public function frontControllerPath(string $sitePath, string $siteName, string $uri): ?string
    {
        if (file_exists($staticFilePath = $sitePath.'/web'.$uri)
           && $this->isActualFile($staticFilePath)) {
            return $staticFilePath;
        }

        return $sitePath.'/web/index.php';
    }

        /**
     * Get the logs paths for the application to show in Herds log viewer.
     */
    public function logFilesPaths() {
        return ["/storage/logs"];
    }

    /**
     * Display information about the application in the information tab of the Sites UI.
     * For Laravel, it's the output of the `php artisan about` command.
     */
    public function siteInformation(string $sitePath, string $phpBinary): array
    {
        try {
            $process = new Process([
                $phpBinary,
                'artisan',
                'about',
                '--json'
            ], $sitePath);

            $process->mustRun();

            $result = json_decode($process->getOutput(), true);
        } catch (\Exception $e) {
            $result = [];
        }

        return [
            ...$result,
        ];
    }
}
```

This example driver provides a good overview about the possibilities and make use of the `phpBinary` and `$sitePath` variables.


# Supported Frameworks
Source: https://herd.laravel.com/docs/macos/extending-herd/supported-frameworks



# Supported Frameworks

You may think that Herd is for Laravel development only, but thanks to the foundational work of [Laravel Valet](https://laravel.com/docs/11.x/valet#custom-valet-drivers), it ships with drivers for many other frameworks and web applications.

## Supported Frameworks

* [Laravel](https://laravel.com)
* [CakePHP 3](https://cakephp.org/)
* [Slim](https://www.slimframework.com/)
* [Symfony](https://symfony.com/)
* [Zend](https://framework.zend.com/)

## Content Management Systems

* [Bedrock](https://roots.io/bedrock/)
* [Contao](https://contao.org/en/)
* [Craft](https://craftcms.com/)
* [Drupal](https://www.drupal.org/)
* [ExpressionEngine](https://expressionengine.com)
* [Jigsaw](https://jigsaw.tighten.com/)
* [Joomla!](https://www.joomla.org/)
* [Kirby](https://getkirby.com/)
* [OctoberCMS](https://octobercms.com/)
* [Sculpin](https://sculpin.io/)
* [Statamic](https://statamic.com/)
* [WordPress](https://wordpress.org/)

## Ecommerce

* [Magento 2](https://business.adobe.com/products/magento/magento-commerce.html)

If Herd does not support your framework out of the box, or you use a custom setup for your application, you can create a [custom driver](/macos/extending-herd/custom-drivers) to serve your site with Herd.


# Databases
Source: https://herd.laravel.com/docs/macos/getting-started/databases



# Using databases with Herd

Herd ships with PHP extensions to support for all major databases, so if you're using MySQL, MariaDB, PostgreSQL, Redis or SQLite, we've got you covered. New Laravel applications use SQLite as default, and you don't need an additional database service to get up and running.

If you plan to use MySQL, PostgreSQL or Redis, you can either download the database service from its vendor, use a free tool like DBngin to manage the database service or upgrade to  [Herd Pro](https://herd.laravel.com/checkout).

Herd Pro provides a convenient user interface to manage services for [MySQL](/macos/herd-pro-services/mysql), [MariaDB](/macos/herd-pro-services/mariadb), [PostgreSQL](/macos/herd-pro-services/postgresql), [MongoDB](/macos/herd-pro-services/mongodb), [Typesense](/macos/herd-pro-services/typesense), [Meilisearch](/macos/herd-pro-services/meilisearch), [MinIO](/macos/herd-pro-services/minio), and [Redis](/macos/herd-pro-services/redis), and [Laravel Reverb](/macos/herd-pro-services/laravel-reverb) and you can get them up and running in seconds.

<Frame>
  <img alt="Herd Pro Services" src="https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/features/services.png?fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=d55de8ba5821d184afc9253c76d4a6c6" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/features/services.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/features/services.png?w=280&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=56b2255dc0f07b83c98b8e611830485f 280w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/features/services.png?w=560&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=491f86c258816d09796cc82f29628968 560w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/features/services.png?w=840&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=8cb9c5254a2a6c21b891272eaae2dad5 840w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/features/services.png?w=1100&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=57842478e5219323de0d94d7c97529ac 1100w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/features/services.png?w=1650&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=b400b7760d0e1a01e28d5f073b4c02f5 1650w, https://mintcdn.com/herd/8sm4YnmqUuRPQUjM/images/features/services.png?w=2500&fit=max&auto=format&n=8sm4YnmqUuRPQUjM&q=85&s=087e84b0446ebd023bfd697eadd0992b 2500w" />
</Frame>


# Installation
Source: https://herd.laravel.com/docs/macos/getting-started/installation



export const InlineNewsletterForm = ({id}) => <div className="newsletter-card-container">
        <Card>
            <div className="newsletter-card-content">
                <h1 className="font-medium text-2xl sm:text-3xl text-gray-800 dark:text-white">Laravel Herd Quick Wins</h1>
                <div className="text-lg text-gray-800 dark:text-white mb-4">Make the most of Herd in your first week — even if you're new to Laravel. Written for the 50,000+ devs using Herd every day.</div>
            </div>
            
            <script src="https://f.convertkit.com/ckjs/ck.5.js"></script>
            <form action={`https://app.kit.com/forms/${id}/subscriptions`} method="post" data-sv-form={id} data-uid="19dc730a0c" data-format="inline" data-version="5" className="pt-2 mb-8" data-options="{&quot;settings&quot;:{&quot;after_subscribe&quot;:{&quot;action&quot;:&quot;message&quot;,&quot;success_message&quot;:&quot;Success! Please check your email to confirm your subscription.&quot;,&quot;redirect_url&quot;:&quot;&quot;},&quot;analytics&quot;:{&quot;google&quot;:null,&quot;fathom&quot;:null,&quot;facebook&quot;:null,&quot;segment&quot;:null,&quot;pinterest&quot;:null,&quot;sparkloop&quot;:null,&quot;googletagmanager&quot;:null},&quot;modal&quot;:{&quot;trigger&quot;:&quot;timer&quot;,&quot;scroll_percentage&quot;:null,&quot;timer&quot;:5,&quot;devices&quot;:&quot;all&quot;,&quot;show_once_every&quot;:15},&quot;powered_by&quot;:{&quot;show&quot;:false,&quot;url&quot;:&quot;https://kit.com/features/forms?utm_campaign=poweredby&amp;utm_content=form&amp;utm_medium=referral&amp;utm_source=dynamic&quot;},&quot;recaptcha&quot;:{&quot;enabled&quot;:false},&quot;return_visitor&quot;:{&quot;action&quot;:&quot;show&quot;,&quot;custom_content&quot;:&quot;&quot;},&quot;slide_in&quot;:{&quot;display_in&quot;:&quot;bottom_right&quot;,&quot;trigger&quot;:&quot;timer&quot;,&quot;scroll_percentage&quot;:null,&quot;timer&quot;:5,&quot;devices&quot;:&quot;all&quot;,&quot;show_once_every&quot;:15},&quot;sticky_bar&quot;:{&quot;display_in&quot;:&quot;top&quot;,&quot;trigger&quot;:&quot;timer&quot;,&quot;scroll_percentage&quot;:null,&quot;timer&quot;:5,&quot;devices&quot;:&quot;all&quot;,&quot;show_once_every&quot;:15}},&quot;version&quot;:&quot;5&quot;}">
                <div data-style="clean">
                    <ul class="formkit-alert formkit-alert-error" data-element="errors" data-group="alert"></ul>
                    <div data-element="fields" className="formkit-fields">
                        <input className="formkit-input w-full" name="email_address" aria-label="Email Address" placeholder="Email Address" required type="email" style={{
  borderColor: "rgb(227, 227, 227)",
  minWidth: "350px",
  flexGrow: 0
}} />
                        <button data-element="submit" className="py-3 w-full px-8 bg-brand text-white font-bold rounded-lg">
                            <span>Subscribe</span>
                        </button>
                    </div>
                </div>
            </form>
        </Card>
    </div>;

<CardGroup cols={2}>
  <Card title="Download Herd" icon="download" href="https://herd.laravel.com/download">
    Download Laravel Herd
  </Card>

  <Card title="Purchase Herd Pro" icon="credit-card" href="https://herd.laravel.com/checkout">
    Purchase a license for Herd Pro
  </Card>
</CardGroup>

# Why Herd?

Herd is a blazing fast, native Laravel and PHP development environment for macOS.
It provides everything that you need to get started with Laravel development. It ships with PHP, [nginx](https://nginx.org/en/), [dnsmasq](https://en.wikipedia.org/wiki/Dnsmasq) and [Node.js](https://nodejs.org/).

You can integrate Herd with [Laravel Forge](https://forge.laravel.com) and use a single tool from setting up your site locally to deploying it on a remote server.

[Herd Pro](https://herd.laravel.com/#features) completes your development environment with service management for databases, caches, and more. It comes with testing and debugging tools tailored to Laravel and you'll love them when you're working on web applications every day.

After installing Herd, it serves all sites on your machine via `*.test` domains – it's like [Laravel Valet](https://laravel.com/docs/valet) but has no dependencies and doesn't need Homebrew. It ships with its own, pre-compiled binaries which makes it blazing fast to install and use.

More than 50,000 web developers use Herd every day to create awesome web applications for their users, and [they love it](https://herd.laravel.com/#testimonials).

<InlineNewsletterForm id="7711601" />

# Requirements

Herd requires macOS 12.0 or higher.

# Installation

You can download the latest version of Herd [here](https://herd.laravel.com/download).

After downloading the DMG file, double-click the file to open it, and drag the Herd icon to the Applications folder. Once Herd is installed, open it from your Applications folder which triggers the onboarding process.

The onboarding process downloads the latest PHP version and installs a Herd background service on your machine. This background service needs admin permissions and is responsible for handling nginx and dnsmasq.

After the installation process is complete, you have a fully-functioning PHP and Laravel development environment. This means you can invoke the `herd`, `php`, `laravel`, and `composer` binaries from your terminal:

```shell  theme={null}
herd --version
php --version
laravel --version
composer --version
node --version
```

Herd does not alter any existing services on your system, and if it's not for you, you can easily switch back to your previous setup.

If you migrate from a different development setup, we've dedicated guides for [Laravel Sail](/macos/migration-guides/sail) and [MAMP/MAMP PRO](/macos/migration-guides/mamp) and a quick one from Laravel Valet below.

User from a different setups or beginners can go to the next chapter and [learn how to manage your sites](/macos/getting-started/sites) with Herd.

# Migrate from Valet

Herd makes it easy to migrate all of your existing Valet sites, certificates and settings to Herd.
Upon opening Herd for the first time, Herd automatically detects your existing Valet installation and migrates all existing sites, certificates and settings to Herd.

If Valet is still running, Herd asks you to stop Valet before continuing with the installation.

It is important to note that Herd will does not modify your existing Valet installation in any way. This means that you can easily switch back to Valet at any time.
Just quit Herd and run `valet start` to start Valet again.

## Using Herd with Fish

If you are using the [Fish](https://fishshell.com/) shell, you need to run the following command to add the Herd binaries to your path:

```shell  theme={null}
fish_add_path -U $HOME/Library/Application\ Support/Herd/bin/
```


# Sites
Source: https://herd.laravel.com/docs/macos/getting-started/sites



# Sites

Herd uses the concept of *parked* paths and *linked* directories for serving sites. You can access every site in a parked path via `<directory-name>.test`. By default, Herd parks the `~/Herd` directory for you. Any PHP application in this directory is available via its `.test` domain automatically. If you have other locations for your projects, you can add them as parked paths in the general settings or link individual projects as a linked directory.

<Frame>
  <img alt="General Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c19852d44fecabeb5bc19eedc5e8e453" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/general.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=22afd9e1fa032bb21b9155850730ce93 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4869478d1f5a4152914c4a7d2167a8f0 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e1e778bc29630e44d5f9198cd41497a1 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=097afd2821b2723239b6e5aa63923d92 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3bff520c6616897ce59adf0038dd5449 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/general.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=68f07df21797b6c7ada48ed577906c1a 2500w" />
</Frame>

Aside from Laravel, Herd [supports many frameworks](/macos/extending-herd/supported-frameworks) and applications out-of-the-box. If your framework is not in the list, you can create a [custom driver](/macos/extending-herd/custom-drivers) to run it with Herd.

## Creating your first site

The fastest way to manage your sites and to create new applications is the command line.

```shell  theme={null}
cd ~/Herd
laravel new my-new-site
cd my-new-site
herd open
herd edit
```

These commands go into your Herd directory, create a brand new Laravel application and open it in your browser. The `herd edit` command even opens your favorite IDE.

## Linking an existing site

You can link an existing site with a specific domain via the `link` command from any directory on your machine. The `link` command uses the directory name as domain name if you don't set additional parameters.

```shell  theme={null}
cd ~/Sites/your-project
herd link
herd link custom-domain
```

These commands create Herd configurations, and you can now access the application via `your-project.test` and `custom-domain.test`. This is useful if you want to use an application from multiple domains, for example in multi-tenancy environments or if you don't store all your projects in a single code directory.

## Via the GUI

If you prefer creating and linking sites via a graphical user interface, you can use Herd's site wizard to create new Laravel applications or link existing projects.

You can start the site wizard by opening the [Site Manager](/macos/sites/managing-sites) from the Herd menu bar icon and selecting the plus icon at the top left.

<Frame>
  <img src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e036cb8184e43e2c20e61521982d4545" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_wizard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=71559417801774d79796d3a538c151e7 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a19b9c7e83e2ba48fe3862fcf88331cb 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=83160e018710fe921d71987ae9befa3a 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e8da1ee4e77c6e49645f7eacd4f7654b 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4eeb18e2fc28519972ee9125eb85f520 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_wizard.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a8819615eb8f41d422b946d121e2e837 2500w" />
</Frame>

## Unlinking an existing site

You may remove a previously created link, by using the `unlink` command from any directory on your machine. The `unlink` command uses the directory name as domain name if you don't set additional parameters.

```shell  theme={null}
cd ~/Sites/your-project
herd unlink
herd unlink custom-domain
```

These commands remove any previous created links to your site.

## Application Information

The "Information" tab gives you a brief overview of the application. Laravel apps display the content of the `php artisan about` command, but you can customize the overview by using a [custom driver](/macos/extending-herd/custom-drivers) for your site.

## Integrations

Herd allows linking your local site with first-party Laravel cloud services and makes triggering common tasks like deployments super easy. At the moment, Herd supports connecting to sites on Laravel Forge with the [Forge integration](/macos/integrations/laravel-forge).


# Updates
Source: https://herd.laravel.com/docs/macos/getting-started/updates



# Herd Updates

Herd regularly checks for new updates in the background and notifies you when a new version is available. You can disable the updater in the settings if you prefer to do that manually but we recommend to always keep Herd up to date.

To manually check for updates, click the "Check for Updates" button in the Herd menu in the macOS menu bar. This checks for Herd, PHP and Node.js updates at the same time.

## PHP versions

Herd allows you to download and install different PHP versions with a single click.
When a new PHP version is available, Herd notifies you about the update in the menu bar.

Minor PHP patch versions in Herd can lag a few days behind their official release because they get tested extensively after they've been compiled specifically for Herd.

You can choose the PHP versions which you want to install or update in the "PHP" tab of the preferences.

The supported PHP versions are:

* 8.4
* 8.3 (default)
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


# Laravel
Source: https://herd.laravel.com/docs/macos/guides/laravel



# How to set up a Laravel application

Herd's main purpose is serving Laravel developers by providing a fully integrated development stack with PHP and nginx at its core. Both services are complemented with all tools that you need to work on almost any Laravel application. This means that Herd is the right tool, no matter if you are just starting as a beginner or work with Laravel for a decade.

This guide covers all steps that you need to follow to get up and running with a new Laravel application but also works if you replace the application creation step with checking out an existing git repository.

## Code Directory

Herd uses the concept of *parked paths* for serving sites via `.test` domains. By default, Herd creates and parks the `~/Herd` directory and every folder that you create in this directory is reachable via its own domain.

Let's open your terminal and go into the directory:

```bash  theme={null}
cd ~/Herd
```

## Database Choices

Laravel ships with an SQLite database for your application by default but if you are familiar with MySQL or PostgreSQL, you should get a database instance up and running before you create or check our your application.

<Note>
  [Herd Pro]() allows you to install database instances and other complementary services directly from Herd – but you can also download and run the database of your choice separately.
</Note>

## Installing Laravel

The easiest way to download and install a fresh Laravel application is the command line. Herd ships with the Laravel installer, and it's already available in your CLI, so switch pack to the terminal and run the following command. The first line creates the application, the second line switches in your application directory for further commands.

```bash  theme={null}
laravel new my-first-application
cd my-first-application
```

If you have an existing Laravel application and git is available on your terminal, simply clone the repository and follow the setup guide for the application's readme file. It's usually something like this:

```bash  theme={null}
git clone path-to-your-repository
cd repository-name
cp .env.example .env
composer install
herd php artisan key:generate
herd php artisan migrate
```

## Visit your application in the browser

Your application is now up and running, and you can visit it via it's `.test` domain. Herd provides a command to open your browser directly from your terminal.

```bash  theme={null}
herd open
```

You can now start working on your application, if you've set up a favorite editor, in the Herd settings, you can open the editor via the command `herd edit`.

[Herd Pro](/#features) users can set up additional services and start using the integrated dump debugging feature, work with emails and check our their logs, so if you are using Herd Pro, this is how they work.

## Set up Services

You can set up and manage [services](/macos/herd-pro-services/services) directly in Herd with a convenient interface. Simply head over to the services tab in the settings and add the service that you need. Herd supports many widely used services like databases, caches, and search-, and storage engines.

### Databases

* [MySQL](/macos/herd-pro-services/mysql)
* [PostgreSQL](/macos/herd-pro-services/postgresql)
* [MongoDB](/macos/herd-pro-services/mongodb)

### Caches and Queues

* [Redis](/macos/herd-pro-services/redis)

### Boradcasting and Realtime

* [Laravel Reverb](/macos/herd-pro-services/laravel-reverb)

### Search

* [Meilisearch](/macos/herd-pro-services/meilisearch)
* [Typesense](/macos/herd-pro-services/typesense)

### Storage

* [MinIO](/macos/herd-pro-services/minio)

You can install all these services with a few clicks and decide if you want to start them with Herd automatically or only on demand.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1e9ddb35805c0f24be4cc37832ecc9f7" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=143a7e51e9b92ed5189c1d64f04130ea 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=08309c5a6b46d8d09bbaddb00c957c5c 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3aec2a3121209890f92af9728a31965e 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=80f9b060ec397fb7cdf863fdd6978fc9 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1eccb7cd7383fa6154a32f5f8073e50c 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a2edeac7a8d42e5634472ce2c0f4af97 2500w" />
</Frame>

## Debug with Dumps

The most common debugging method in Laravel is using the helpers for `dump()` or `dd()`. While `dd` stands for `dump and die` and stops your application, `dump` simply displays some output. Herd Pro has a separate dump window that displays this information in a great way and also allows you to listen for Eloquent queries, logs and more. As a first test, you can invoke the dump function and print out the simple string `hello from your app`.

Go to your terminal and start a tinker session by running the tinker command of the Herd command line interface. It proxies the tinker command of Laravel but always uses the application PHP:

```bash  theme={null}
herd tinker
```

Once tinker has started, you can use the dump helper to output the string:

```bash  theme={null}
dump("hello from your app");
```

When running this simple command, this opens the dump window and displays the string. You can use the `dump` and `dd` helper anywhere in your application to debug browser requests and CLI commands.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3b975ef5a985eb2051d8015d73d64a92" data-og-width="1844" width="1844" data-og-height="1342" height="1342" data-path="images/docs/dumps_settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a3ce4cef8e7af2c5bd71f8cc549e1cb0 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=29cbe8f9f64e084d45280079f41e6d28 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=19c8014aa53e82cd33f2387469eb2e80 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b452cc108274a1006e4821ab70fe3bf6 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d940a060b7211ef941f030dc71e416fc 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dumps_settings.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7ac8ec169b70cdad36a87080fd8028a1 2500w" />
</Frame>

## Test Emails

Testing emails can be cumbersome and even result in sending emails to your users when you're connected to a real mail service. Herd solves this by running a local email server that catches your mails and sends them to an internal email client that you can use for testing the email.

To enable the email server for your application, go to the `env` file in the root of your application directory and make sure to update the mail settings according to the following configuration.

```bash  theme={null}
MAIL_MAILER=smtp
MAIL_HOST=127.0.0.1
MAIL_PORT=2525
MAIL_USERNAME=${APP_NAME}
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS="hello@example.com"
MAIL_FROM_NAME="${APP_NAME}"
```

Every time when your application sends an email, it uses Herd's integrated mail service. If it's the first email from this application, it creates an inbox for this application based on the name of the application so that you can easily identify emails and where they are from.

Please make sure that your application name does not include any special characters or if it does, simply change the `MAIL_USERNAME` in the configuration above to something easily identifiable.

So after you've setup up the mail service, let's test the configuration by creating a test email and sending it via tinker.

```bash  theme={null}
herd php artisan make:mail TestMail --markdown
herd tinker
```

Send the email in your tinker session via the mail facade.

```php  theme={null}
Mail::to('sebastian@beyondcode.com')->send(new \App\Mail\TestMail());
```

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a05f97270532e7f58f75ca0c71698d7a" data-og-width="2774" width="2774" data-og-height="1712" height="1712" data-path="images/docs/mails-intro.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5fe04d828d9379ffbfe0c4358d117abd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d70f76c42f366bec471a215074af8bab 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c812270bd4bb81c7b7991247745adf6f 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0736a427709e0d1cc00549fc9d9ed9c9 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=64a6c303ddf269634f3a9a9b7e1a9a49 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=99907f4c16654a68080ecf1e3c0d49f1 2500w" />
</Frame>

After setting up your first Laravel application in Herd, you can now follow the docs to learn more about all features in more detail and fully leverage Herd when using it every day.


# WordPress
Source: https://herd.laravel.com/docs/macos/guides/wordpress



# How to set up a WordPress site

While Herd was mainly developed with Laravel in mind, most concepts apply to working with WordPress, too. Herd supports standard WordPress setups as well as Bedrock with its different folder structure. This guide covers the installation of a standard WordPress site via a zip file but you can apply the same concepts when using the WordPress CLI or cloning a git repository.

## Code Directory

Herd uses the concept of *parked paths* for serving sites via `.test` domains. By default, Herd creates and parks the `~/Herd` directory and every folder that you create in this directory is reachable via its own domain.

This means that you can simply move or install a site to this directory and don't have to create it via the Site Manager in Herd – it just works.

## Database Setup

While Laravel uses SQLite as default, WordPress requires either MySQL or MariaDB as database service for your site. You can set up this database via a free tool like [dbngin](https://dbngin.com) or set up a database instance via a [Herd service](/macos/herd-pro-services/services).

<Note>
  [Herd Pro]() allows you to install database instances and other complementary services directly from Herd – but you can also download and run the database of your choice separately.
</Note>

## Local Domains

As described above, Herd serves all directories in your parked paths via local `.test` domains. This means that you can move a site into the directory `my-wordpress-site` and access it via [http://my-wordpress-site.test](http://my-wordpress-site.test).

If you are running a multisite and want to point multiple domains to a single WordPress installation, you can use Herd links to create more local domains. You can either do that via the Site Manager as described in the chapter [linking sites](/macos/getting-started/sites#linking-an-existing-site) or use the terminal with the commands below.

```bash  theme={null}
cd ~/Herd/my-wordpress-site
herd link my-second-domain
```

These commands go into your site directory and create the local domain [http://my-second-domain.test](http://my-second-domain.test) to your site. It's now accessible via both domains and you can proceed with your normal configuration.

## Drivers

Herd uses drivers to detect frameworks and serve sites to your browser. These drivers support standard WordPress installations and Bedrock but you can write [custom drivers](/macos/extending-herd/custom-drivers) if you are using a different setup for your site. So if your setup is supported by default, you can skip this step but it's important to know that customized installations might need a custom driver or there will simply be a 404 error.

## Installation

The installation of a new WordPress site is straight forward. At first, you need to set up a database. Herd Pro users can go to `Settings > Services` and select their MySQL instance and then open TablePlus or AdminerEvo in the menu on the right to create the database. If you are familiar with MySQL on the command line, you can do that as well.

After that, simply follow these steps:

1. Download the latest version of WordPress from the [official site](https://wordpress.org/download/)
2. Extract the zip file into a parked Herd directory, for example `~/Herd`
3. Rename the directory to your domain, in this guide, we're using the local domain `wordpress-guide.test`, so the directory name is `wordpress-guide`.
4. Go to [http://wordpress-guide.test](http://wordpress-guide.test) and follow the installation process.

If you are using a different port for your database instance, make sure to add this port to the database host during the installation. When using Herd, the database username is `root` and has no password.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b8b42cbcaa62cd3b3ad5bdaad990c71e" data-og-width="1570" width="1570" data-og-height="1352" height="1352" data-path="images/docs/guides_wordpress_database.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a915cb826c5addc45f18c126fadc336a 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=08505e86b49b8837ef23742f83c15263 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5bfb0dd99bf5112099998ba5887ca323 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=eaf692677092428a43f4e37505ab06aa 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c82bf7921b47695e53f4fb78c9bf2947 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_database.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4cc083a2baae911d8545c902072d7b2a 2500w" />
</Frame>

Your WordPress site is now running via Herd and you can start working on it.

## Debugging with Dumps

[Herd Pro](/#plans) allows you to debug your site with a convenient `dump` helper. So if you're working on plugins and need to output data for debugging purposes, this is super powerful. In this example, we\`re creating a very basic plugin and dumping a string and all existing posts of the fresh WordPress install.

```php  theme={null}
/*
Plugin Name: My Herd Plugin
Plugin URI: https://example.com/my-herd-plugin
Description: A simple plugin to demonstrate WordPress plugin development.
Version: 1.0
Author: Your Name
Author URI: https://example.com
License: GPL2
*/

// Hook into an action
add_action('wp_head', 'my_custom_function');

function my_custom_function() {
    dump("Hello from Herd 👋");
    dump(get_posts());
}
```

When opening any page of your site, the function runs and sends the debug output to the dumps window where it looks like this example.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3794b56425f6ed2e9f87ab57bdaf3280" data-og-width="1914" width="1914" data-og-height="1660" height="1660" data-path="images/docs/guides_wordpress_dumps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=183f6716062bc5b61088c9a145b82bcd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=10855adf35fb9591ef3591be72b143ce 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cd1381bd9d2eb18dff2d75662d37a08b 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b4798242a440a3f1eb99ae00de45aa3d 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b73f71f7e22a2186560da91e32ae2ceb 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_dumps.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=54f4fe178b74ee9d6dfcd2d1d8361b9c 2500w" />
</Frame>

## Test Emails

Testing emails can be cumbersome and even result in sending emails to your users when you're connected to a real mail service. Herd solves this by running a local email server that catches your mails and sends them to an internal email client that you can use for testing the email.

The quickest way to set up mails in Herd Pro is by defining a mailer in the `functions.php`. Simply paste the following snippet to the end of your `functions.php` to receive emails in Herd.

```php  theme={null}
function herd_mailer($phpmailer) {
    $phpmailer->isSMTP();
    $phpmailer->Host = '127.0.0.1';
    $phpmailer->SMTPAuth = true;
    $phpmailer->Port = 2525;
    $phpmailer->Username = 'WordPress';
    $phpmailer->Password = '';
}

add_action('phpmailer_init', 'herd_mailer');
```

Every time when your application sends an email, it uses Herd's integrated mail service. If it's the first email from this application, it creates an inbox for this application based on the username of the configuration so that you can easily identify emails and where they are from.

You can test this feature by logging out of your site and using the password reset form to trigger an email.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=131f3b183c1da67a1a6143dd94934499" data-og-width="2134" width="2134" data-og-height="1304" height="1304" data-path="images/docs/guides_wordpress_mails.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b0747bcf08b25316db08074e71f498eb 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5b07c818918c8923ac88979c6d4eb2c1 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c9b8d4e411fc993b4e4c9f76f3a08c5f 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ea430aa911399a2110a876e5c63016fb 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=80e205a5acff0788d624f0d8ce6cacc5 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/guides_wordpress_mails.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=318abdddd2a121e8a5ff3ddf96c01136 2500w" />
</Frame>

After setting up your first WordPress site in Herd, you can now follow the docs to learn more about all features in more detail and fully leverage Herd when using it every day.


# Laravel Reverb
Source: https://herd.laravel.com/docs/macos/herd-pro-services/laravel-reverb



# Setting up a Laravel Reverb instance

[Laravel Reverb](https://reverb.laravel.com/) is a first-party WebSocket server for Laravel applications. It's open source and uses the Pusher protocol, making it the first choice for real-time communication between client and server in Laravel applications. If you want to learn more about Reverb, check out [Real-time games with Laravel](https://laracasts.com/series/real-time-games-with-laravel) on Laracasts.

While you can install it as a package into your existing application, it often makes sense to have a dedicated WebSocket server for all your applications.

Herd provides a convenient way to set up a dedicated Reverb instance on your machine with a few clicks. It even comes secured with an optional TLS certificate.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0f679516cc6864c6f0347ccc279c627a" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-reverb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4f17e3e4f12f353ea2b91cf5c2ebb876 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=58d11542936fa9864ca43c925941fe8e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=587e72ee734b04a4a873fc5d45174fbf 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1be3c57db1fac350e33a9372273e396e 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=13794e486f54d70f19025c4098e9f28b 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-reverb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ae81d8d6613af803277a74bac277337b 2500w" />
</Frame>

## Connecting from your Laravel application

Laravel Reverb starts the WebSocket server on port `8080` but you can change it when creating a new service in case you're already running a different service on that port or want to run multiple instances in parallel.
After installing Reverb, you can use the following environment variables to configure the service for your application.

```bash  theme={null}
REVERB_APP_ID=1001
REVERB_APP_KEY=laravel-herd
REVERB_APP_SECRET=secret
REVERB_HOST="0.0.0.0"
REVERB_PORT=8080
```

Check out the [Laravel Echo documentation](https://laravel.com/docs/11.x/broadcasting#client-reverb) to learn how to connect your application frontend to the Laravel Reverb server.

## Logs

Reverb constantly logs information to the running process, so if you are debugging Reverb connection,s you can open the output of the Reverb process by pressing the Open button in the logs area on the right side.

<Frame>
  <img alt="Reverb Logs" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8b98984c650ba9734012936c12c8e43d" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_reverb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4c5c4c2447c5d14e2638afcd972fd857 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=aba09bf84e670e8e0fc84738bded0879 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2668b432dddddb1e557b5165bbec3599 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f736a01e31b9cf1a6797bc06400952a3 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=70ae09a2c8680390801784714fe771f2 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_reverb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2a57106d85e23ecc5c17c041382b6f07 2500w" />
</Frame>

## Updates

Reverb uses composer and Herd supports updating Reverb to it's latest version via the Herd UI. Simply right click to open the context menu and select "update".

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| Reverb  | 1.x     |


# Mail
Source: https://herd.laravel.com/docs/macos/herd-pro-services/mail



# Working with emails

When you are working with emails locally, you need to make sure that these emails don't leave your machine and get sent to real users but it's also important to inspect them easily.

Herd Pro provides an SMTP mail server on your local machine that catches all outgoing emails instead of sending them to the world. It displays them in Herds own email client and provides rich debugging capabilities for all types of emails.

This saves you from sending emails to real users and frees you up from paying cloud services for developer email inboxes, not even requiring you to dig through log files when using the log driver. It's also super fast and organizes all emails per site.

<Frame>
  <img alt="Herd Pro Mail Server with a mail" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a05f97270532e7f58f75ca0c71698d7a" data-og-width="2774" width="2774" data-og-height="1712" height="1712" data-path="images/docs/mails-intro.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5fe04d828d9379ffbfe0c4358d117abd 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d70f76c42f366bec471a215074af8bab 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c812270bd4bb81c7b7991247745adf6f 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0736a427709e0d1cc00549fc9d9ed9c9 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=64a6c303ddf269634f3a9a9b7e1a9a49 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-intro.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=99907f4c16654a68080ecf1e3c0d49f1 2500w" />
</Frame>

## Setup

<Note>
  When using `laravel new` or Herd's site creation wizard, Herd configures the mail server in your `.env` file for you automatically.
</Note>

The mail server uses the SMTP protocol to accept mails but instead of sending them to their recipient, it saves them to an internal database.

You can use the settings below and add them to your local `.env` file to receive mails in the Herd Pro mail app.

<Tabs>
  <Tab title="Laravel">
    ```bash .env theme={null}
    MAIL_MAILER=smtp
    MAIL_HOST=127.0.0.1
    MAIL_PORT=2525
    MAIL_USERNAME=${APP_NAME}
    MAIL_PASSWORD=null
    MAIL_ENCRYPTION=null
    MAIL_FROM_ADDRESS="hello@example.com"
    MAIL_FROM_NAME="${APP_NAME}"
    ```
  </Tab>

  <Tab title="WordPress">
    ```php functions.php theme={null}
    function herd_mailer($phpmailer) {
        $phpmailer->isSMTP();
        $phpmailer->Host = '127.0.0.1';
        $phpmailer->SMTPAuth = true;
        $phpmailer->Port = 2525;
        $phpmailer->Username = 'WordPress';
        $phpmailer->Password = '';
    }

    add_action('phpmailer_init', 'herd_mailer');
    ```
  </Tab>

  <Tab title="Other Frameworks">
    Please refer to your framework specific documentation on how to configure outgoing emails and use the provided SMTP server host, port and username to connect to Laravel Herd.
  </Tab>
</Tabs>

The mail client groups incoming mails by the username of the mail sender. This allows you to create a dedicated inbox for each project.
Either specify a unique username manually, or use the `APP_NAME` environment variable to automatically use your application's name as the inbox name. Depending on your application name, you might need to set the username for your mailbox manually before emails show up in Herd.

## Changing the port

By default, the Herd Pro mail server runs on port `2525` but you can customize this configuration in the settings.

<Frame>
  <img alt="Herd Pro Mail Server Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d5d82bd5e094f047fba0a6d3ab9148b1" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_mail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=3cee717f65ee50c0170f4f2c249713f3 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b26158ab0ca5d3873e99246f58093c9d 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9348902335df6e5d1a8058b619a159e8 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7cde40c4866a304cb2a1003f0e86c0d0 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=34acfa7de14890f6430ac1b28e1b7dad 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_mail.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8e7d3ba7e87ca11b046fd42923380f5a 2500w" />
</Frame>

## Inspecting mails

You may inspect the header values of an email by opening the sidebar of the email window at the top right.

The HTML source of the email or the raw email content are available via right-click on the email itself. They open in a new window, and you can open raw or HTML content of multiple mails at the same time.

<Frame>
  <img alt="Herd Pro Mail Server with a mail" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=092a2ed1314d5138b08f192d0bb33383" data-og-width="2774" width="2774" data-og-height="1712" height="1712" data-path="images/docs/mails-headers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=787e5717e0441d2ba005ef63ad189630 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=64f0a511ba23643101cb218794b33bc3 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d1764021224c945f85fe3dddcf5e2016 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c53bbeade8273206b94aa706f2248d5f 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=985a3b73a57654c1c0053bda7e6cb745 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/mails-headers.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d3344c3cc84238439beda6b1ccecc32e 2500w" />
</Frame>

## Attachments

Herd stores all attachments in your Herd application directory and creates a folder for each email with all attached files. You can either open them from this folder or directly from the email.

```
~/Library/Application Support/Herd/Log/mail
```

## Deleting mails

You can delete single emails by selecting the email and pressing the `Backspace` key but if you want to get rid of a whole inbox, you can use the trash icon in the top bar of the mail window.

## Troubleshooting

If you accidentally sent thousands of emails to Herd or something is wrong, you can check the SQLite database file where Herd stores all emails. You can find the file at:

```
~/Library/Application Support/Herd/HerdCoreData.sqlite
```

You can truncate all mail related tables in this file without breaking the rest of the application.


# MariaDB
Source: https://herd.laravel.com/docs/macos/herd-pro-services/mariadb



# Installing MariaDB via Herd Pro

MariaDB is a drop-in, fully compatible replacement for MySQL, and it's the default database engine for many Linux distributions. Many popular hosting platforms like [Laravel Forge](https://forge.laravel.com) support MariaDB databases out of the box, making the switch from local to production a breeze.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a5d392bf631c3aa8b9a4135c465c8a86" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-mariadb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9c4610815f1eee56a993bcd7ca89a9da 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9804affd57620035855bb95939d88f1e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=31f8b7730d02b0e87de2f27fbc80c5c1 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2a19b39065e4a22116c8cd22d37dbc15 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c7f5d19b0b778a34e15ee5a44b0ce954 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mariadb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c87efa27093044b5760830c4614520f0 2500w" />
</Frame>

## Configuration

Herd provides a sensible default configuration for your MariaDB instance that works seamlessly for new setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

Enabling the autostart option automatically starts a service instance when you start Herd.

If you want to modify the settings of the database, you can right click the service in the settings and open its data directory. In this data directory, there is a `my.cnf` that this specific MariaDB instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

While Laravel applications can create a database when running the migrations for the first time, it's a good practice to set up the database within the database instance yourself.

The service details on the right side of the selected service allow you to open TablePlus or AdminerEvo with a single click. Herd automatically detects TablePlus on your machine and provides a connection string to access the database instance. If you don't use TablePlus, it opens AdminerEvo where it inserts the correct login credentials for you.

<Frame>
  <img alt="MariaDB Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=462afebaf471423a072e27ccf437f233" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_mariadb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8741f6bd32f987383137926b26a11528 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b779e3143501e4fc52c5e797c2f1f18d 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5a94e5cb096f06562f4929bec3b7a1d8 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9c2ccb0a0a8ee218ebf778bd19aa739e 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0cb6ea5e270264a33526e20706f06503 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mariadb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0944dbe72a47a0ca7f99dcb051e2f56b 2500w" />
</Frame>

## Connecting from your Laravel application

To connect your application to the server, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.

```env  theme={null}
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3307
DB_DATABASE=laravel # set this to your project database
DB_USERNAME=root
DB_PASSWORD=
```

## Database service migrations

Whether you set up a newer version of MariaDB or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Connecting via CLI

Herd symlinks the `mariadb` CLI to your PATH, so you can connect to the database via the command line.
As Laravel Herd allows you to start multiple MariaDB servers, you should specify the port to connect to the correct instance.

For example, to connect to the MariaDB server running on port 3306, you can use the following command:

```bash  theme={null}
mariadb -u root -h 127.0.0.1 -P 3306 -p
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| MariaDB | 10.11.6 |


# Meilisearch
Source: https://herd.laravel.com/docs/macos/herd-pro-services/meilisearch



# Set up Meilisearch for Laravel Scout

Meilisearch is a powerful search engine for your application, working perfectly with [Laravel Scout](https://laravel.com/docs/11.x/scout). It allows you to add a search engine with great relevancy, typo correction, and more to your application by simply adding the `Searchable` Trait to a model.

<Frame>
  <img alt="Screenshot of Meilisearch settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d72a51d32be226143441c1c7131394eb" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-meilisearch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fbf39ee7d84da13575e0f360578d03d8 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f64bf3ae0c341c344e1d6ef15787dc8c 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6f6ec069040b592f1fa21bc10e317e70 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1aa732268f504cc88209783dfa9d3bc3 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ea57beac79d36d70c81565ae63eb3b27 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a62cf4652288af214cc9d8c0f0bd3837 2500w" />
</Frame>

## Connecting from your Laravel application

Like with all Herd services, you can configure the port as well as the service name of your Meilisearch instance and add the following environment variables to your `.env` file.

```env  theme={null}
SCOUT_DRIVER=meilisearch
MEILISEARCH_HOST=http://127.0.0.1:7700
MEILISEARCH_KEY=LARAVEL-HERD
```

When using the Meilisearch driver you will need to install the Meilisearch PHP SDK via the composer package manager:

```bash  theme={null}
composer require meilisearch/meilisearch-php http-interop/http-factory-guzzle
```

You can find additional information about using Laravel Scout with Meilisearch in the [Laravel documentation](https://laravel.com/docs/11.x/scout#meilisearch).

## Using Meilisearch

You can open the Meilisearch Dashboard or the logs of the service from the right side of the service details.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=381dca368dda29b60cba76b48aa21eb9" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_meilisearch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7af381cf85755ee911f9f9d1420f3150 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e926ed5200b2a4ca8c9d699b85530ed3 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=85a35336e1de5316ed945062be005677 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f894923f1e871379cf3c1d60da521490 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=093b93ebe27c6daeb0e43603f8461de6 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_meilisearch.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f8929586252d29a2d922302c6f510259 2500w" />
</Frame>

## Dashboard

The Meilisearch dashboard is accessible via `http://locahost:port` or by using the dashboard button in the services list.

<Frame>
  <img alt="Screenshot of the Meilisearch dashboard" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=85fa215d160b130a895cc6cbac189730" data-og-width="2882" width="2882" data-og-height="1984" height="1984" data-path="images/docs/setup-meilisearch-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f5ac4eaac05f1a5d0aaafa87c8cb690b 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a70c9edd4940c1fe8a53a165a605ab79 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=45fd6912e718756273e695f65bc2f808 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=bbd2d08612ba0642e367cd6a7923bab2 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9ed554fb54ba45d2ab0ea7fe867cd644 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-meilisearch-dashboard.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=70ecd49107d885f68fd866369901d802 2500w" />
</Frame>

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service     | Version |
| ----------- | ------- |
| Meilisearch | 1.9.0   |


# MinIO
Source: https://herd.laravel.com/docs/macos/herd-pro-services/minio



# Set up MinIO

MinIO is an open-source, S3 compatible object storage and works perfectly if you want to use the same APIs locally that you use on your production environment. You can set up MinIO as a Herd service and log into its dashboard to create your first storage bucket with the same credentials that you use as environment variables.

<Frame>
  <img alt="Screenshot of minio settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3f961357945e0f3bfae4d4bca5472bb8" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-minio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2ff8e42fddedcdcce32c2150df67c058 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d6246dc5c1a2ebb8e44a7580cdb05c4e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8e8fafe49839a7425f3c8580c188f410 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c3144e8885f8332378bf8ec7371ab5a8 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=eb571ea89f3611c556a598e24351b8fb 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=71a84daba8bfedcb968418d6c393d02e 2500w" />
</Frame>

## Configuration

Before you can connect your application to MinIO, you need to create a first bucket within the dashboard. The easiest way to access the dashboard or view the logs of the service is via the Herd service configuration.

<Frame>
  <img alt="Screenshot of the MinIO configuration" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=69c2f4331f300ac1b610d2db4b985506" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_minio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=36d8c8b2949f5971ffeb8209487a7080 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=55805e9fead2a2e680bf4c645b9c9de9 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=dfe5b486dcdae16c15bc33430156891f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=43e5868242cd80bd189383d2f6ce45d8 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2eb93d67a5a94fa36e24f79e52ab725a 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_minio.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6e4f9d0f7d7b7c4e72b0dcba11fd31f8 2500w" />
</Frame>

## Dashboard

You can access the MinIO dashboard via `http://localhost:PORT` or by using the dashboard button in the services list. Log in with the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to create your first bucket and use the object storage like in your production environment.

<Frame>
  <img alt="Screenshot of the MinIO dashboard" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1bb8feeac9813ec43bab6473fe902332" data-og-width="2666" width="2666" data-og-height="1710" height="1710" data-path="images/docs/setup-minio-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f927fe3d161ee49f7365b33a90bd676a 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4300308ef79e53aa45d8ba815404527e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=40c267a85137ebbb55530f93b6b9249f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=bae7e1afa13ed9ef8678ed590d4eca27 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c51fcfc397c31a7db0c5ddf6a4752697 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-minio-dashboard.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3ad9cf7b58dccb320e8512a95c86703d 2500w" />
</Frame>

## Configuration

After setting the name, port, and autostart options and starting up the service, please log into the dashboard and create a bucket to be able to upload files.

You can then adjust your `.env` file in order to connect to your local MinIO service.

```env  theme={null}
AWS_BUCKET=herd-bucket # Your bucket name
AWS_ACCESS_KEY_ID=herd
AWS_SECRET_ACCESS_KEY=secretkey
AWS_USE_PATH_STYLE_ENDPOINT=true
AWS_URL=http://localhost:9000/YOUR-BUCKET-NAME
AWS_ENDPOINT=http://localhost:9000
```

You can find additional information about configuring MinIO with Laravel in the [Laravel documentation](https://laravel.com/docs/11.x/filesystem#amazon-s3-compatible-filesystems).

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version            |
| ------- | ------------------ |
| MinIO   | RELEASE.2024-06-29 |


# MongoDB
Source: https://herd.laravel.com/docs/macos/herd-pro-services/mongodb



# Installing MongoDB via Herd Pro

You can install the [MongoDB Community Edition](https://www.mongodb.com/products/self-managed/community-edition) from the service management section of the settings. This uses the MongoDB PHP extension and allows a seamless use of MongoDB in your application during development.

<Frame>
  <img alt="Screenshot of MongoDB settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=30da82302d5bd9a0fff9bb5760cc3ba8" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_mongodb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cfc310cad3460bc7af1043241835bf6d 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=41d16e27801de5fb9c104015e3560929 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fb3b143c48826de1e85d085eb16d574f 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f40ca6246dbc22379d3f893ced199df5 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e28132690607ea6b1cccd51e4e15d401 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mongodb.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=eb2686f2853eb557ae2bf5a7dda3fe4a 2500w" />
</Frame>

## Configuration

Herd starts your MongoDB instance with sensible defaults that work great for new setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

If you want to modify the settings of the service, you can right-click on the service in the settings and open its data directory. In this data directory, there is a `mongodb.conf` that this MongoDB instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

You can create databases in your MongoDB instance by using the tooling that you can download on the [official website](https://www.mongodb.com/docs/database-tools/) or use tools like TablePlus that work with a variety of database engines.

## Connecting from your Laravel application

In order to use MongoDB in combination with Laravel, you may use the `mongodb/laravel-mongodb` composer package.

Run the following command to add the dependency to your application:

```bash  theme={null}
composer require mongodb/laravel-mongodb
```

To connect your application to the database server, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.
Add these settings to your `.env` file.

```env  theme={null}
DB_CONNECTION=mongodb
DB_PORT=27020
DB_URI="mongodb://127.0.0.1:27020/laravel"
```

Please refer to the [Laravel MongoDB](https://www.mongodb.com/docs/drivers/php/laravel-mongodb/current/quick-start/download-and-install/#add-laravel-mongodb-to-the-dependencies) documentation for additional help.

## Database service migrations

Whether you set up a newer version of MongoDB or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| MongoDB | 7.0.12  |


# MySQL
Source: https://herd.laravel.com/docs/macos/herd-pro-services/mysql



# Installing MySQL via Herd Pro

MySQL is the most popular relational database engine for web development, and setting up a database server with a few clicks makes it incredibly easy to follow tutorials or get up and running with a professional setup in minutes. Many popular hosting platforms like [Laravel Forge](https://forge.laravel.com) support MySQL databases out of the box, making the switch from local to production a breeze.

If you are new to Laravel and want to move from SQLite to a database service, MySQL is the best choice for most applications.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d69ab65c52b0d79a18f8582e4ecbc59d" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-mysql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=daecc665a758ac3b4f5c6228e2d48db9 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7e61d98b0fc8aa0bf4c89d4ee7ab541c 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5cc01e9eaf08836fbe4d15d2be67de9d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cdffe8c5c1bc018530e882fcc8d60f2f 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a62cc97354c83f873b5d76f189e2ed59 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-mysql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2337900e88da64d2fcda3fe0771d16f6 2500w" />
</Frame>

## Configuration

Herd provides a sensible default configuration for your MySQL instance that works seamlessly for new setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

Enabling the autostart option automatically starts a service instance when you start Herd.

If you want to modify the settings of the database, you can right click the service in the settings and open its data directory. In this data directory, there is a `my.cnf` that this specific MySQL instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

While Laravel applications can create a database when running the migrations for the first time, it's a good practice to set up the database within the database instance yourself.

The service details on the right side of the selected service allow you to open TablePlus or AdminerEvo with a single click. Herd automatically detects TablePlus on your machine and provides a connection string to access the database instance. If you don't use TablePlus, it opens AdminerEvo where it inserts the correct login credentials for you.

<Frame>
  <img alt="MySQL Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=881d70dcb9912411b9da399de9ca89be" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_mysql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=16cad02f11777f61b74953fe8ca5b8a7 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a9facd40370b8b19a60c6fb2aa491685 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=98a745314da488df10b01fe9772421d5 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=635f78a8a5e90e6209938f41b49bf317 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fe9ac0593e0f82029ab58a6e0c9298c3 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_mysql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=264296cb906146a29775621d11bfad97 2500w" />
</Frame>

## Connecting from your Laravel application

To connect your application to the server, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.

```env  theme={null}
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3307
DB_DATABASE=laravel # set this to your project database
DB_USERNAME=root
DB_PASSWORD=
```

## Database service migrations

Whether you set up a newer version of MySQL or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Connecting via CLI

Herd symlinks the `mysql` CLI to your PATH, so you can connect to the database via the command line.
As Laravel Herd allows you to start multiple MySQL servers, you should specify the port to connect to the correct instance.

For example, to connect to the MySQL server running on port 3306, you can use the following command:

```bash  theme={null}
mysql -u root -h 127.0.0.1 -P 3306 -p
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| MySQL   | 8.4.\*  |
| MySQL   | 8.0.36  |


# PostgreSQL
Source: https://herd.laravel.com/docs/macos/herd-pro-services/postgresql



# Installing PostgreSQL via Herd Pro

PostgreSQL is a powerful, open-source object-relational database system that is known for its reliability and robustness.
Laravel Herd Pro extends PostgreSQL by providing a number of popular extensions:

* [PostGIS](https://postgis.net/) - adds support for geographic objects to the PostgreSQL database, making it easy to store and query spatial data.
* [pgrouting](https://pgrouting.org/) - adds routing functionality to PostgreSQL, allowing you to calculate the shortest path between two points.
* [pgvector](https://github.com/pgvector/pgvector) - a vector similarity search extension for PostgreSQL, which allows you to search for (among other things) OpenAI embeddings in your database.

<Frame>
  <img alt="Screenshot of PostgreSQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=bc79104b778b7c618e2a6a0867e44aff" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-postgresql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8afac0656461906d9a4e9c7c6b5a1007 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a6d405362d29fa212969c6fbf83ccb3e 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4f48bce811fc67773149d1347aea63c1 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4754847fd67c5b9ad15985c0c74c5365 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5fbdcb46e195c58fc671b8a5be97de22 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-postgresql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fbba81c1a21738ec88f36d71ac3ea1b1 2500w" />
</Frame>

## Configuration

Herd uses a common default configuration for your PostgreSQL instance that works seamlessly for most setups, and you can change the port of the service to run it in parallel to existing installations on your machine.

Enabling the autostart option automatically starts a service instance when you start Herd.

If you want to modify the settings of the database, you can right-click the service in the settings and open its data directory. In this data directory, there is a `postgresql.conf` that this specific PostgreSQL instance loads on startup.

Make sure to restart the service if you make changes to this configuration.

## Creating databases

Before you can connect your application to the database service, you need an actual database within the instance of the service. Herd provides a convenient way to open TablePlus or AdminerEvo in case that you don't use TablePlus.

When clicking on the related button for these tools on the right side of the service details, Herd opens a connection to the database in your preferred tool and automatically logs you in.

<Frame>
  <img alt="MySQL Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ecc2e3add8e7a47fcff20c13895dd489" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_postgresql.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fd6a02c06c9c80cd1ee13ed040cbd1ef 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=df764f595d984c126b17c66d7d8c5248 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1efbcb16d40a2ddb94ceb32905beb3f3 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4ec8cd5912c36cce01197526930e5635 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=67d9f57ceac95d4fceee4645e1d72095 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_postgresql.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4ca42b754b308c74f2dfd27f50783721 2500w" />
</Frame>

## Connecting from your Laravel application

To connect it within your application, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.

```env  theme={null}
DB_CONNECTION=pgsql
DB_HOST=127.0.0.1
DB_PORT=5432
DB_DATABASE=laravel # set this to your project database
DB_USERNAME=root
DB_PASSWORD=
```

## Database service migrations

Whether you set up a newer version of PostgreSQL or migrate from existing instances on your machine, the most comfortable way is to use a database client like [TablePlus](https://tableplus.com/) to export and import the database tables.

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service    | Version |
| ---------- | ------- |
| PostgreSQL | 14.x    |
| PostgreSQL | 15.x    |
| PostgreSQL | 16.x    |
| PostgreSQL | 17.x    |


# Redis
Source: https://herd.laravel.com/docs/macos/herd-pro-services/redis



# Setting up Redis

Redis is a fast in-memory data store that is very versatile, and most Laravel applications use it for caching or as queue service. While you may go with the `sync` driver for queues and the `file` driver for caches locally, it's often useful to have the same development setup that you use in production.

<Note>
  Keep in mind that using the `dump()` function in queued jobs only works if you pair it with the [Dumps](/macos/debugging/dumps) feature, otherwise dumps happen in the background, and you won't see them.
</Note>

You can set up a new Redis instance via the services tab of the settings.

<Frame>
  <img alt="Screenshot of MySQL settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=52dfa1ee87d018b5aec4c274e75b1efb" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-redis.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3ac25accf9a1a848417760edf3cfe8a6 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d27c456b7f617705362b206f95e2760f 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3d42515395d93c6c072d99a019faa299 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f8f4b3d9c6ccdb4a14588327a188cff9 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0966cd58faf9c216d91e022f5f78018f 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-redis.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e0e210d343e423af6d80b3cef9b34364 2500w" />
</Frame>

## Configuration

Redis comes with a sensible default configuration, making it easy to use for local development without any changes. If you want change the port of the Redis service or decide if you want to automatically start it with Herd, you can do that in the settings of the service.

You can modify the configuration by right-clicking the service in the settings and open its data directory. In this data directory, there is a `redis.conf` that this specific Redis instance loads on startup.

Make sure to restart the service if you make changes to this configuration file.

## Accessing the Redis instance

You usually don't need dedicated Redis databases within your redis instance but if you decide to do that or want to debug the content of your Redis database, you can open TablePlus directly from the menu on the right side.

<Frame>
  <img alt="MySQL Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b7c7474e06c40e073e109cfc3b8a133e" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_redis.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=93faabe5042256a57b607213e4697cd0 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3b7bf7d96a9723994216d19c6fbf0b6a 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2439d204a45e4fffbb3efa7a4bd01fed 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=52cc5a6d4127321f90f7c768a3934519 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5a6536a3cd4d2fd9f850b3c5a64d2df4 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_redis.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=be0ec9d0930a2630957ee2749944ef70 2500w" />
</Frame>

## Connecting from your Laravel application

To connect it within your application, you can use the credentials that are listed next to the running service in the settings, or you can use the ones below.

```env  theme={null}
# Driver configuration
CACHE_DRIVER=redis
QUEUE_CONNECTION=redis
SESSION_DRIVER=redis

# Redis setup
REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6138
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| Redis   | 7.0.0   |


# Version Matrix
Source: https://herd.laravel.com/docs/macos/herd-pro-services/service-versions



# Services Version List

This page provides an overview of available Herd services on macOS in different versions. New versions are available regularly and they work great for general purpose development, but you can always install very specific versions by downloading them from their vendor or by using Brew or Docker.

## Databases

| Service    | Version |
| :--------- | ------- |
| MariaDB    | 10.11.6 |
| MongoDB    | 7.0.x   |
| MySQL      | 8.0.x   |
| MySQL      | 8.4.x   |
| MySQL      | 9.4.x   |
| PostgreSQL | 14.x    |
| PostgreSQL | 15.x    |
| PostgreSQL | 16.x    |
| PostgreSQL | 17.x    |
| PostgreSQL | 18.x    |

## Caches & Queues

| Service | Version |
| :------ | ------- |
| Redis   | 7.0.x   |
| Redis   | 7.4.x   |
| Valkey  | 7.2.x   |
| Valkey  | 8.0.x   |
| Valkey  | 8.1.x   |

## Broadcasting

| Service | Version |
| :------ | ------- |
| Reverb  | 1.x     |

## Search

| Service     | Version |
| :---------- | ------- |
| Meilisearch | 1.x     |
| Typesense   | 0.26    |
| Typesense   | 29.x    |

## Storage

| Service | Version            |
| :------ | ------------------ |
| MinIO   | RELEASE.2024-XX-XX |
| MinIO   | RELEASE.2025-XX-XX |


# Services
Source: https://herd.laravel.com/docs/macos/herd-pro-services/services



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


# Typesense
Source: https://herd.laravel.com/docs/macos/herd-pro-services/typesense



# Set up Typesense for Laravel Scout

Typesense is a lightning-fast open source search engine for your application, working perfectly with [Laravel Scout](https://laravel.com/docs/11.x/scout). It allows you to add a search engine with great relevancy, typo correction, and more to your application by simply adding the `Searchable` Trait to a model.

Herd makes setting up a Typesense service super easy:

<Frame>
  <img alt="Screenshot of Typesense settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6b7debd8169c3ebfcfb5d569b3169fcd" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/setup-typesense.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2291761b846bffb9a4bcfad2a6e21b29 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3e059c0376b8da624bf71b551934d323 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=199d15ad073422f7b1eb49004370a803 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=edeb7dd47dc8a1dca86dd4106bca2ae4 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3dcd71dcf83ab6adeea2cde987ccaa5c 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-typesense.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4486a86a1d5d1c82e57994c3537bfcd3 2500w" />
</Frame>

## Connecting from your Laravel application

Like with all Herd services, you can configure the port as well as the service name of your Typesense instance and then add the following environment variables to your `.env` file.

```env  theme={null}
SCOUT_DRIVER=typesense
TYPESENSE_API_KEY=LARAVEL-HERD
TYPESENSE_HOST=localhost
```

If you're using a different port, you can simply copy the connections details from the right side of the service settings. The Typesense detail view also gives you a quick access to the logs of the service.

<Frame>
  <img alt="Typesense settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5728acbd0db1ce3847e1c9a6f755101a" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/settings_services_typesense.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ebb7a81a12337b341c29947c0b1e2dc6 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f10a221d926c83f96cdddbf9415d5b05 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=838305f6a6d47a34f9a1b6e316b767bf 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f39d158a7fa27f76e370d5802a536cf5 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=27db1815b4abd32d437cd373bd8a4601 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_typesense.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=660fd2aea294ad1b570ee210aa6fc1eb 2500w" />
</Frame>

When using the Typesense with Laravel Scout you will need to install the Typesense PHP SDK via the Composer package manager:

```bash  theme={null}
composer require typesense/typesense-php
```

You can find additional information about using Laravel Scout with Typesense in the [Laravel documentation](https://laravel.com/docs/11.x/scout#typesense)

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service   | Version |
| --------- | ------- |
| Typesense | 0.26    |


# Valkey
Source: https://herd.laravel.com/docs/macos/herd-pro-services/valkey



# Setting up Valkey

Valkey is an alternative to Redis that is API compatible and can be used as a cache and queue driver in Laravel
applications. It's free and open source, making it a great choice for local development since Redis pivoted to a less
developer friendly license.

<Note>
  Keep in mind that using the `dump()` function in queued jobs only works if you pair it with the [Dumps](/macos/debugging/dumps) feature, otherwise dumps happen in the background, and you won't see them.
</Note>

You can set up a new Valkey instance via the services tab of the settings.

<Frame>
  <img alt="Screenshot of Valkey settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d694ba29d47fd0cda010e0125f47cd6e" data-og-width="1800" width="1800" data-og-height="1236" height="1236" data-path="images/docs/setup-valkey.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=239a73dad8cce80a3c8c79f41261993b 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=443278dd6194c8fb18402f8618187ace 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b4f4e2f3457d9771d7ee75c214430da3 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=94c8ce6aee0064ddf702a6275e4ab99c 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8148996ae2442fefee53c1447e20ef99 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/setup-valkey.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=107986a8a0193573fc8da9c6706e0aa0 2500w" />
</Frame>

## Configuration

Valkey comes with a sensible default configuration, making it easy to use for local development without any changes. If you want to change the port of the Valkey service or decide if you want to automatically start it with Herd, you can do that in the settings of the service.

You can modify the configuration by right-clicking the service in the settings and opening its data directory. In this data directory, there is a `valkey.conf` that this specific Valkey instance loads on startup.

Make sure to restart the service if you make changes to this configuration file.

## Accessing the Valkey instance

You usually don't need dedicated databases within your Valkey instance, but if you decide to do that or want to debug the content of your database, you can open TablePlus directly from the menu on the right side.

<Frame>
  <img alt="Valkey Sidebar" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d7fa29ca04ac0263d6b673dfbe78ba35" data-og-width="1800" width="1800" data-og-height="1236" height="1236" data-path="images/docs/settings_services_valkey.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a8e031afd3f4b0d3ff036afba38dfa24 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=609a0884d693bbcdf598dfd2566c5e20 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7380e2d2382436b178ff07b71cf84a23 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9155b73d1920f88227aab55c975fbc87 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7c9646c583e1b645753cee5a7ea83ffa 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_services_valkey.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f00b407df69e97a3efaffcd8163ffa44 2500w" />
</Frame>

## Connecting from your Laravel application

To connect it within your application, you can use the credentials that are listed next to the running service in the
settings, or you can use the ones below. Since Valkey is API compatible with Redis, the configuration is the same.

```env  theme={null}
# Driver configuration
CACHE_DRIVER=redis
QUEUE_CONNECTION=redis
SESSION_DRIVER=redis

# Redis setup
REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379
```

## Versions

Herd Pro allows you to install the following versions directly from the services tab of the settings. New versions are available regularly.

| Service | Version |
| ------- | ------- |
| Valkey  | 7.2.x   |
| Valkey  | 8.0.x   |
| Valkey  | 8.1.x   |


# Laravel Forge
Source: https://herd.laravel.com/docs/macos/integrations/laravel-forge



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


# Migrating from MAMP
Source: https://herd.laravel.com/docs/macos/migration-guides/mamp



# How to migrate from MAMP to Herd

If you're currently using MAMP or MAMP Pro for your local PHP development and want to switch to Herd, this guide will
help you migrate your setup smoothly. Herd provides several advantages over MAMP, including:

* Deeply Integrated Laravel Support
* Advanced Web Development Debugging Tools
* Database Instance Management for MySQL, PostgreSQL, MongoDB and redis
* Additional Service Management for TypeSense, MeiliSearch, MinIO and Laravel Reverb
* First Party Laravel Forge Integration
* Native Xdebug Integration and Detection

## Before You Begin

Before starting the migration process, make sure you have:

1. A list of all your active MAMP sites
2. Database exports of all your databases
3. [Installed Herd](/macos/getting-started/installation)

## Exporting MAMP Databases

The first step is to export all your databases from MAMP. You can do this using phpMyAdmin that ships with MAMP or via the command line.

### Via phpMyAdmin

1. Open MAMP and start your servers
2. Navigate to phpMyAdmin (usually at [http://localhost:8888/phpMyAdmin](http://localhost:8888/phpMyAdmin))
3. Select each database you want to export
4. Click "Export" in the top menu
5. Choose "Quick" export method and "SQL" format
6. Click "Go" to download the SQL file

### Via Command Line

If you prefer using the command line, you can use the MySQL executable that ships with MAMP:

```bash  theme={null}
"/Applications/MAMP/Library/bin/mysqldump" -u root -p database_name > database_name.sql
```

## Setting Up Databases in Herd

After exporting your databases, you'll need to set them up in Herd. You have several options:

### Option 1: Herd Pro Services (Recommended)

If you're using [Herd Pro](/macos/herd-pro-services/services), you can install MySQL directly from the Services panel:

1. Open Herd settings
2. Go to the Services tab
3. Click the + button and select MySQL
4. Import your database dumps using TablePlus or AdminerEvo directly from the service panel

### Option 2: Standalone MySQL

If you're using the free version of Herd, you can:

1. Install MySQL separately via Homebrew or download it from mysql.com
2. Import your databases using the mysql command line tool:

```bash  theme={null}
mysql -u root database_name < database_name.sql
```

## Migrating Sites

### Step 1: Document Current Sites

First, make a list of your current MAMP sites and their document roots. In MAMP Pro, you can find these in the Hosts section of the application.

### Step 2: Set Up Herd Directory

Herd uses a central directory for serving sites. By default, this is `~/Herd`. You can also add additional [parked paths](/macos/getting-started/sites) in the settings.

### Step 3: Move Your Projects

1. Create your desired directory structure in your Herd directory
2. Move or copy your project files to this new location
3. Access your sites via their new `.test` domains automatically

For example, if your site was at:

```
/Applications/MAMP/htdocs/mysite
```

Move it to:

```
~/Herd/mysite
```

It will then be accessible at `http://mysite.test`

## Updating Configuration

### PHP Version

MAMP and Herd handle PHP versions differently. In Herd, you can:

1. Set a global PHP version via the menu bar or CLI:

```bash  theme={null}
herd use 8.2
```

2. [Set per-site PHP versions](/macos/technology/php-versions#per-site-php-versions) either through the Site Manager or CLI:

```bash  theme={null}
cd ~/Herd/mysite
herd isolate 8.1
```

### Database Connections

Update your database configuration in your applications. For Laravel applications, modify your `.env` file:

```env  theme={null}
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306 # Or the port you configured in Herd
DB_DATABASE=your_database
DB_USERNAME=root
DB_PASSWORD=
```

### Virtual Hosts

Unlike MAMP, Herd doesn't require manual virtual host configuration. Simply placing your project in a [parked directory](/macos/getting-started/sites) makes it accessible via its `.test` domain. If you need custom domains, you can use the `link` command:

```bash  theme={null}
cd ~/Herd/mysite
herd link custom-domain
```

### SSL Certificates

If you were using SSL certificates in MAMP, you can secure your sites in Herd with a single command:

```bash  theme={null}
cd ~/Herd/mysite
herd secure
```

This automatically generates and installs a trusted SSL certificate for your local domain.

## PHP Extensions

Herd includes most common PHP extensions by default. If you need additional extensions, check the [PHP Extensions](/macos/technology/php-extensions) documentation for installation instructions.

## Mail Testing

If you were using MAMP's built-in mail catching, Herd Pro offers an [improved mail testing feature](/macos/herd-pro-services/mail) that captures all outgoing emails and provides a modern interface for inspection.

## Troubleshooting

### Common Issues

1. **Database Connection Issues**: Ensure you're using the correct port for your database connection. If you're using Herd Pro's MySQL service, check the port in the Services panel.

2. **PHP Version Mismatch**: If your application requires a specific PHP version, use `herd isolate` to set the correct version for that project.

3. **Missing Extensions**: Check the [PHP Extensions](/macos/technology/php-extensions) documentation if you need to install additional extensions.

For more help, consult the [troubleshooting guide](/macos/troubleshooting/common-issues) or reach out to the [community support](/macos/troubleshooting/support).

## Final Steps

1. Test all your migrated sites and ensure they work as expected
2. Verify database connections and functionality
3. Test any special PHP configurations or requirements
4. Once everything is working, you can uninstall MAMP

After completing this migration, you'll have a faster, more modern development environment that's easier to maintain and better integrated with macOS.


# Migrating from Sail
Source: https://herd.laravel.com/docs/macos/migration-guides/sail



# How to migrate from Laravel Sail to Herd

If you're currently using Laravel Sail for local development and want to switch to Herd, this guide will walk you through the migration process. While both tools provide excellent development environments, they have different approaches to managing services and dependencies.

## Understanding the Differences

Laravel Sail uses Docker containers to provide isolated development environments, while Herd takes a native approach by running services directly on your machine. Here are the key differences:

<CardGroup cols={2}>
  <Card title="Laravel Sail" icon="docker">
    * Uses Docker containers
    * Requires Docker Desktop
    * Services defined in docker-compose.yml
    * Container-based isolation
  </Card>

  <Card title="Herd" icon="elephant">
    * Uses native services
    * No Docker required
    * Services managed via Herd UI/CLI
    * Native performance
  </Card>
</CardGroup>

## Migration Steps

### 1. Stop Sail Services

Before switching to Herd, make sure to stop all running Sail containers:

```bash  theme={null}
./vendor/bin/sail down
```

### 2. Install Herd

Download and install Herd from the [official website](https://herd.laravel.com). Follow the [installation instructions](/macos/getting-started/installation) to get Herd up and running on your machine.

### 3. Update Environment Configuration

Your `.env` file likely contains Docker-specific configurations. Here's how to update common settings:

#### Database Configuration

If you're using MySQL:

```env  theme={null}
# From Sail
DB_HOST=mysql
DB_PORT=3306

# To Herd
DB_HOST=127.0.0.1
DB_PORT=3306 # Default Herd MySQL port
```

#### Redis Configuration

If you're using Redis:

```env  theme={null}
# From Sail
REDIS_HOST=redis

# To Herd
REDIS_HOST=127.0.0.1
```

#### Mail Configuration

If you're using Mailhog with Sail, switch to Herd's mail service:

```env  theme={null}
# From Sail
MAIL_HOST=mailhog
MAIL_PORT=1025

# To Herd
MAIL_MAILER=smtp
MAIL_HOST=127.0.0.1
MAIL_PORT=2525
MAIL_USERNAME=${APP_NAME}
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
```

### 4. Set Up Required Services

<Note>
  If you're using [Herd Pro](https://herd.laravel.com/checkout), you can install services directly from the Herd UI. The free version requires manual installation of additional services.
</Note>

Review your `docker-compose.yml` file to identify which services your application needs. Common services include:

* Database (MySQL/PostgreSQL)
* Redis
* Meilisearch

For Herd Pro users, you can install these services via the Services tab in settings. Free version users should install these services separately.

### 5. Remove Sail Dependencies

You can now remove Sail from your project:

```bash  theme={null}
composer remove laravel/sail --dev
```

Also, clean up Sail-related files:

* `docker-compose.yml`
* `docker/` directory
* Any custom Dockerfile configurations

### 6. Update Development Scripts

Update your `composer.json` scripts section to remove Sail commands. For example:

```json  theme={null}
{
    "scripts": {
        // Remove these Sail-based scripts
        "sail:up": "./vendor/bin/sail up -d",
        "sail:down": "./vendor/bin/sail down"
    }
}
```

### 7. Create Herd Configuration (optional)

Create a `herd.yml` file in your project root to define project-specific configurations either manually or by running `herd init`:

```yaml  theme={null}
name: your-project-name
php: '8.3'
services:
    mysql:
        version: 8.0.36
        port: '${DB_PORT}'
    redis:
        version: 7.0.0
        port: '${REDIS_PORT}'
```

### 8. Initialize the Project

Initialize your project with Herd:

```bash  theme={null}
herd init
```

This command will configure your project according to the `herd.yml` file and set up any required services.

## Common Challenges

### Database Migration

If you need to migrate your data from Sail's MySQL container:

1. Export your database from Sail:

```bash  theme={null}
./vendor/bin/sail mysql --execute="SHOW DATABASES" > databases.txt
./vendor/bin/sail mysqldump your_database > database_backup.sql
```

2. Import into Herd's MySQL:

```bash  theme={null}
mysql -u root -P 3306 -h 127.0.0.1 -e "CREATE DATABASE your_database_name;"
mysql -u root -P 3306 -h 127.0.0.1 your_database_name < database_backup.sql
```

### File Permissions

Since Herd runs services natively rather than in containers, you might need to adjust file permissions:

```bash  theme={null}
chmod -R 755 storage bootstrap/cache
```

## Using Herd in a Team

When working with a team, make sure to:

1. Share your `herd.yml` configuration file via version control
2. Document any specific service requirements
3. Standardize PHP versions across the team

## Getting Help

If you encounter issues during migration:

1. Check the [troubleshooting guides](/macos/troubleshooting/common-issues)
2. Join the [community support](/macos/troubleshooting/support)

[Herd Pro](https://herd.laravel.com/checkout) users can also access priority email support for migration assistance.


# Herd.yml
Source: https://herd.laravel.com/docs/macos/sites/herd-yaml



# Sharing project configurations

When working in a team, it's important to ensure that everyone uses the same PHP version, certificate settings, and service versions. You can use the `herd.yml` file to manage these configurations within your repository.

## Creating the `herd.yml` file

The easiest way to create the `herd.yml` file is by running the `herd init` command in your project directory.

```bash  theme={null}
herd init
```

This command starts a wizard to guide you through the setup process of the `herd.yml` file. If you run `herd init` in a project that already has this file, it configures your site accordingly. Re-running the command after a change, applies all additional configurations but does not remove existing ones.

The setup allows you to configure the following settings:

* Project Name
* Aliases (aka multiple domains)
* PHP Version
* TLS/SSL Certificates

[Herd Pro](https://herd.laravel.com/checkout) users can also specify [services](/macos/herd-pro-services/service-versions) in their `herd.yml` and to install them automatically. By default, Herd preselects the services that are present in your `.env` file, but you can add more if needed.

The list contains the latest versions of these services and if you need other versions, check the section about [editing the `herd.yml` file](#editing-the-codeherdymlcode-file).

```bash  theme={null}
 ~ herd-website  (main)
› herd init --fresh

 ┌ What is the name of your project? ───────────────────────────┐
 │ herd-website                                                 │
 └──────────────────────────────────────────────────────────────┘

...

 ┌ Do you want to add additional services? ─────────────────────┐
 │ › ◻ Meilisearch (1.6.2)                                    ┃ │
 │   ◻ MinIO (RELEASE.2024-03-05)                             │ │
 │   ◼ MySQL (8.0.36)                                         │ │
 │   ◻ PostgreSQL (16)                                        │ │
 │   ◼ Redis (7.0.0)                                          │ │
 └────────────────────────────────────────────────── 2 selected ┘
  Use the space bar to select options.
```

After running the wizard, a `herd.yml` file will be created in your project root. To overwrite an existing file, you can use the `herd init --fresh` command and generate a new file.

## Setting up a project via `herd.yml`

If a `herd.yml` file exists in your project, Herd can automatically apply the necessary configuration via the `herd init` command.

```bash  theme={null}
herd init
```

Running `herd init` checks for the presence of an `.env` file and if not, asks if the `.env.example` file should be copied. After that, this command applies the configurations, including installing and isolating the specific PHP version, aliases, services and more:

```bash  theme={null}
 ~ herd-website  (main)
› herd init

   INFO  Setting up your project…

   INFO  PHP 8.3 is installed.

   INFO  Site is secured.

   INFO  Mysql is running on port 3346

   INFO  Installing service Redis
   INFO  Redis is running on port 6379

   DONE  Your application is ready to go!
```

## Editing the `herd.yml` file

Here is an example of a `herd.yml` file using all possible customizations:

```yaml  theme={null}
name: herd-website
php: '8.3'
secured: true
aliases:
    - herd-laravel
services:
    mysql:
        version: 8.0.36
        port: '${DB_PORT}'
    redis:
        version: 7.0.0
        port: '${REDIS_PORT}'
```

Instead of referencing your applications' `.env` file with the placeholder (e.g. `${REDIS_PORT}`) you can set a fixed port as well - just keep in mind that your team members may use these ports already.

You can check out a list of available services and versions [here](/macos/herd-pro-services/service-versions).


# Managing Sites
Source: https://herd.laravel.com/docs/macos/sites/managing-sites



# Manage Sites in Herd

If you've read the [Sites](/macos/getting-started/sites) introduction of the [Getting Started](/macos/getting-started/about-herd) section, you are already familiar with the concept of parked paths and linked directories – but how do you use them if you have many sites and use different technologies for them?

## Folder structure

We recommend to put all PHP based sites in your Herd directory until you reach a point where it makes sense to split them into a folder structure that makes sense for you. This could be sites per client, or if you run different technologies like Next.js, you can serve them from a different folder via `npm run dev`.

This setup keeps the [Site Manager](/macos/sites/managing-sites) clean and easy to use because you can simply unpark a directory in case that you don't work on these sites for a few weeks.

If you don't mind a long list in the Site Manager, you can also [mark your most important sites as favorites](#favorites) to display them at the beginning of the list.

## Site Manager

You can manage your sites via the CLI or open the Site Manager via the menu bar icon. This section of the docs explains all features of the Site Manager.

<Frame>
  <img alt="Open the Site Manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0458732c0a855679a6cc050665efefc0" data-og-width="880" width="880" data-og-height="460" height="460" data-path="images/docs/sites_sites.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e68ca7cc5fe19a5f3a683a9552f55844 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a56a27ff92df79149aa6597b88ae08dd 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=110c91c27d4beb69446fc5c23095389d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=300f13f6813c3a31df8a8adce9a9fb1a 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ec22fa89c25e6f2ce409b13b49948607 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_sites.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9d35ba43c8a9253a716ba7cdf66c115f 2500w" />
</Frame>

The Site Manager window is divided into the list of all your sites on the left side and a site management panel for the selected site on the right side.

You can hide the site list if you are working with mainly one site but also refresh the list in case that you are making changes to your parked or linked directories via the CLI and while the Site Manager is open.

Clicking on the plus button opens the site wizard that allows you to create Laravel applications or link existing ones that are not in a parked directory.

<Frame>
  <img alt="Open the Site Manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=67cd996dd8522976d07ddadb486d7e9d" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e3a6a4af25b22ccea7b8ee07a7a0c844 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=132cdc66df6ab564d4ce14c7d3eb7a56 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=711915b2bd7f05c1085c49a084e65e2a 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=05a75f433634d45a891b89ad2584556c 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2020a2940b6b8da3227f2b308db49a6d 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_overview.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=97425c316e095b4565be7bf69d36c53b 2500w" />
</Frame>

The right side of the Sites Manager is dedicated to the selected site and always shows a general tab where you can isolate this site to a specific PHP version. This tells Herd to serve this site with a specific PHP version and not to use the [global configuration](/macos/technology/php-versions#using-different-php-versions-via-the-gui) that you apply in the settings.

If you select a specific Node.js version, Herd creates an `.nvmrc` file in your project directory. This tells your terminal to switch to the selected Node and NPM version automatically.

### Information

The information tab shows driver specific information about the application. For Laravel applications, that's the content of the `php artisan about` command, but you can customize this with a [custom driver](/macos/extending-herd/custom-drivers).

### Integrations

You can connect a Herd site with one or more sites on Laravel Forge. You can learn more about this feature in [Forge Integration](/macos/integrations/laravel-forge) docs.

## Site Actions

Site Actions are like shortcuts from the site manager. They allow you to open your favorite terminal directly in the project directory, start a [Tinker(-well)](/macos/debugging/tinker) session or launch your IDE.

If you open the database, Herd tries to open the application database with its tables in TablePlus but uses AdminerEvo in case that you don't use TablePlus. This gives you quick access to the database on the basis of your `.env` file.

The log action is available for Herd Pro users and opens the [Log Viewer](/macos/debugging/logs) that ships with [Herd Pro](https://herd.laravel.com/checkout). The Profiler action enables and disables the [profiling feature](/macos/debugging/profiler).

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c85b423e650939b18e736ac0efac14c0" data-og-width="1872" width="1872" data-og-height="1122" height="1122" data-path="images/docs/sites_actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=024b530396e76dba91b8552f77e9df03 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c9628e2f385aa9aa3617666328fe1510 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=3c2f53539036439c3bc10e0faaba7b87 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0c180a34f0ec88c005905555121f8ec6 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=516b3674d903000cbb231464e6995cab 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_actions.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=8928f5ee21b006cf80fbdc3131fcc5b2 2500w" />
</Frame>

### Securing Sites

You can serve sites via HTTPS instead of HTTP if your application requires this via [Securing Sites](/macos/sites/securing-sites).

### Groups

If you are working with many sites at the same time and don't want to use multiple parked directories that you add and remove when you need them, you can group sites and they automatically appear in your own site structure on the left side.

<Frame>
  <img alt="Groups in the Site Manager" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=222167ecf7ba32d8919a5d40e188fc3e" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_groups.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=eb378047e22eb00860e71ad21a6c3497 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e9eb17b206b351f5a2394ae2b8d761a8 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=64a28161b9a2142698608832aea1c2ee 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f18af9a02a71e5ab6d5edc9f130ead0b 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=302ff9c4ef829030fe44cdfeaf299e9b 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_groups.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=71906e3253edd1feb45da92697a2dfff 2500w" />
</Frame>

### Deleting Sites

You can fully delete parked sites from your Herd directory with the trash icon. This is identical to deleting their folder with all files, so use this carefully.

## Best Practices

It's a good practice to name your local sites like your domains and subdomains to easily access them in your browser. As an example, the Herd website usually lives in the directory `~/Code/herd.laravel.com` so that it's accessible via `http://herd.laravel.com.test`. The Laravel website is in the directory `~/Code/laravel.com`, etc.

<Note>
  Directory names must not start with `www.`. Herd strips this part to allow you to access your local site via `www.laravel.com` and `laravel.com`.
</Note>


# Nginx Configuration
Source: https://herd.laravel.com/docs/macos/sites/nginx-configuration



# Advanced Nginx Configuration

Herd ships with a default Nginx configurations that is suitable for most projects. However, you can customize the
Nginx settings to fit your specific needs. You can do this in multiple ways and depending on your requirements. Some
settings can (and **must**) be configured via the Herd UI, while others require you to edit the Nginx configuration files directly.

## Via Herd

The most common configurations that usually require changes in your Nginx configuration are the maximum file upload size and the memory limit.
You can change these settings via the Herd UI within the PHP settings section. You can either configure them for all
PHP versions or set specific values per PHP version.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ae85e28aa0c761497d5f08c59dba198b" data-og-width="1460" width="1460" data-og-height="1300" height="1300" data-path="images/docs/nginx-php-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f815b3454614663d7dd74d9117419766 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b2b55c50bbdaae3e42c8644867854e92 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9006f0c3e98d4b76a1f1625c67654ba8 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=383fcfb8f83b62c0f7efe9d780d09ef8 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dc2c263831bd081462e525cb93739918 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-settings.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=399463c5e0c19f51904e66c6e9292e58 2500w" />
</Frame>

You can also change the PHP version for a specific site via the Herd UI. You can either do that in the sites settings or
via the command line by running `herd isolate 8.3` (or any other version you want to use). This creates a dedicated nginx
configuration file for the specified PHP version and use this version for all web request of the current site.

To use the same version via the command line, you can run `herd php artisan ...` or `herd composer ...` instead of just using `php artisan ...` or `composer ...`.
This will ensure that the correct PHP version is used for the command.

If you secure a site with a TLS/SSL certificate, this creates a dedicated Nginx configuration file for the site and you
can make further changes to the Nginx configuration for this site in this file (see below).

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=30612f7cbdc58b29c6e35d6caa4449c6" data-og-width="1800" width="1800" data-og-height="1102" height="1102" data-path="images/docs/nginx-php-versions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8488ec9029dd12b00bfa25ed75ee6d8f 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=0766ca141417d11f864cd79ceec0206e 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=f82f5f735b085314d12c7c6713889e33 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e29c37369a1a5e34e7875a53a5140c6e 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=00d2b87b958053d69d9eeefa618656c3 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/nginx-php-versions.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1b119b300c3b3e2355648a35ca39cfb3 2500w" />
</Frame>

## Customizing the global nginx configuration

Herd comes with default configuration files that are in your Herd configuration directory a `~/Library/Application Support/Herd/config/nginx`.
This directory contains the files `nginx.conf` and `herd.conf` that Herd loads on every request. You can edit these files
to make global changes to all projects – but we recommend only changing site-specific files because we might rewrite these files in future updates.

## Customizing the site-specific nginx configuration

If you isolate the PHP version for a site or secure it with a TLS/SSL certificate, Herd creates a dedicated Nginx
configuration file for this site. This file is located at `~/Library/Application Support/Herd/config/valet/Nginx` and named
after the site domain. For example, if your site is `herd.laravel.com.test`, the file will be named `herd.laravel.com.test`.

You can edit this file to make site-specific changes to the Nginx configuration but make sure to keep Herd specific elements like the
isolated PHP version or references to the TLS/SSL certificate intact.

## CORS

Herd does not ship with a specific CORS configuration because we believe that your local environment should match your
standard production environment as closely as possible. If you need to configure CORS for your project, you can do that similar to
how you would do it in production and either create a global CORS configuration for all sites or add the required header in your site-specific file.

```
# CORS Rules
add_header Access-Control-Allow-Origin *;
# END of CORS Rules #
```

### CORS in Laravel

For the Laravel framework, you publish the CORS middleware as described
in the [Laravel documentation](https://laravel.com/docs/12.x/routing#cors).


# Securing Sites
Source: https://herd.laravel.com/docs/macos/sites/securing-sites



# Securing Sites with TLS

By default, Herd serves sites over HTTP.
However, if you would like to serve a site over encrypted TLS using HTTP/2, you may secure your sites. This is sometimes necessary when working with redirect URLs and other scenarios.

## Via the GUI

You can secure/unsecure a site in the [Site Manager](/macos/sites/managing-sites). You can open the Sites window via the Herd menu bar icon and selecting "Sites".

If you see a closed lock icon, the site is secure and if there is crossed out lock, the site does not have a certificate and is served via HTTP.

<Frame>
  <img alt="Secure Sites" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c65c8e6b90fe38ff3148452fc0e0c1be" data-og-width="1868" width="1868" data-og-height="1122" height="1122" data-path="images/docs/sites_secure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1d2d73721585cf4defb780676c83d2d0 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b7bdda1fc266bad91f537a262080442d 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cd305ae76d5fd80a3d7c46e18968491e 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=d17986a9cd5f91dda2bda5ca0a5a6558 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=706675c1c17b9689c6feffc48b34a4aa 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites_secure.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=cc82e311d0f626467593e1c88bd79060 2500w" />
</Frame>

Clicking on the lock icon toggles the status of the site. If you're securing the site, you may need to confirm one or more permission related popups to create the local certificate.

## Via the CLI

If you prefer to use the CLI, you can use the `herd secure` command to secure/unsecure a site.
For example, if Herd serves your site via the `example-site.test` domain, you need run the following command to secure it:

```shell  theme={null}
# secure the current working directory
herd secure

# secure example-site.test from anywhere
herd secure example-site 
```

To "unsecure" a site and revert back to serving its traffic over plain HTTP, use the `unsecore` command.
Like the `secure` command, this command accepts the sitename that you wish to unsecure:

```shell  theme={null}
# unsecure the current working directory
herd unsecure

# unsecure example-site.test from anywhere
herd unsecure example-site 
```

After unsecuring a site, you man need to restart your browser session because many browsers like Google Chrome cache redirects to HTTPS and will give you a hard time.

## Listing all secure sites

The Herd CLI has a command to list all sites that have a local TLS certificate. You may want to use that for debugging purposes.

```shell  theme={null}
herd secured
```

This gives you a similar output to this:

```
+----------------------------+----------------------------+
| Site                       | Valid Until                |
+----------------------------+----------------------------+
| expose.dev.test            | 2024-08-10 12:07:38 GMT    |
| herd-templates.test        | 2024-09-05 25:12:77 GMT    |
| reverb-110.test            | 2024-09-11 13:44:56 GMT    |
| tinkerwell.app.test        | 2024-10-16 19:53:32 GMT    |
+----------------------------+----------------------------+
```


# Sharing Sites
Source: https://herd.laravel.com/docs/macos/sites/sharing-sites



# How to share a site

Herd makes it easy to share your local sites with the world. This is great for testing your sites on different devices, receiving webhooks, or sharing them with clients and colleagues.
Herd uses [Expose](https://expose.dev) to share your sites.

## Sharing sites via Expose

<Note>
  Expose may not be available in all geographical regions due to regulatory reasons. If Expose isn't available in your country, try [ngrok](#sharing-sites-via-ngrok).
</Note>

To share your site using Expose, you first need to [create a free Expose account](https://expose.dev/register).
Once you have obtained your authentication token, you can configure it in the "Expose" tab of the preferences window.

<Frame>
  <img alt="Expose Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1b64103b11b8a97ba9558f491afaebd9" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_expose.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=03719af3085a3faeb0375acb50261671 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=ba384558581c053ca6132a5436ee1c79 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=862297472aaa2c584bb16f2753b56435 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=dfb47f6bede5a6dd3a6a7fd7eec529c8 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=16ade982d6e26e08dacb0fcb0d8d5e54 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_expose.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=863f1683c617b7e2493d059f8291c07b 2500w" />
</Frame>

Or you can use the CLI:

```shell  theme={null}
expose token YOUR_TOKEN_HERE
```

Once you configured your authentication token, you can share your sites by running `herd share` or `expose share` in the site directory that you want to share.

```shell  theme={null}
cd ~/Herd/example-site

herd share

# Share a linked site:
herd share http://your-local-site.test

# You can share a secured site with:
herd share https://your-secured-local-site.test
```

You can specify a subdomain or server region for best performance and by adding parameters for them to the `share` command.

```shell  theme={null}
herd share https://example-site.test --subdomain=my-project-name --server=us-1
```

## Sharing with basic authentication

You may protect your share links with basic authentication by using the `--basicAuth` argument when sharing your site.

```shell  theme={null}
herd share https://example-site.test --basicAuth="user:password"
```

## Sharing sites via ngrok

If you want to use ngrok, install it according to their instructions. After that, you can share Herd sites via the terminal:

```shell  theme={null}
ngrok http --host-header=rewrite unsecured-site.test
ngrok http --host-header=rewrite secured-site.test:443
```


# Manage Node.js
Source: https://herd.laravel.com/docs/macos/technology/node-versions



# Managing Node.js versions

Herd ships with [nvm](https://github.com/nvm-sh/nvm), the Node version manager which allows the management of multiple [Node.js](https://nodejs.org/) versions on your machine. By default, Herd automatically installs the latest available version of Node.js for you.

Herd requires a specific nvm version and can't use existing nvm installations. If you are migrating from a previous nvm setup, please consult the [Troubleshooting](#troubleshooting) section if it doesn't work as expected.

## Via the GUI

You may install and update the Node.js versions on your machine via the Herd GUI. Simply click on the button and Herd will take care of the rest.

<Frame>
  <img src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d71e7bda428edc2fb8d13b5456bdee95" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=934de439892b01a69a57d742a070583c 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5ff3dfb77e4b5cea71801bbc9f88370e 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=2468322860df5c986b1b20b3f4a79413 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4afd8042624ba43249a9e3517fe847fa 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=b32675e6048a50ea5892455f7c93b15f 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6931a37540ffa876d14a5947e482090b 2500w" />
</Frame>

## Via the CLI

You can use `nvm` on your command line to install, update and switch between Node.js versions any time. To switch to a different version, simply enter `nvm use VERSION` and nvm runs all required commands to change the version and make it accessible in your terminal.
For more information about nvm, take a look at the [official nvm documentation](https://github.com/nvm-sh/nvm?tab=readme-ov-file#usage).

### Commands that you might use regularly

```bash  theme={null}
# Install node 20
nvm install 20

# Uninstall node 20
nvm uninstall 20

# Switch to node 20
nvm use 20

## Display all commands
nvm help
```

# Per-site Node versions

By default, the Node version available via CLI will be the most recent one.

However, if you need to support different Node.js versions for different sites, you may use the isolated Node functionality.
This configures Herd to use the specified Node version for the site, regardless of the global Node version.

If you use oh-my-zsh, Herd automatically detects the Node.js version to use when changing directories via your terminal.

## Via the CLI

You may use the `herd isolate-node` command to specify which Node.js version a particular folder should use. The `isolate-node` command configures
Herd/nvm to use the specified Node.js version for the site located in your current working directory:

```bash  theme={null}
cd ~/Herd/example-site
 
herd isolate-node 21
```

If your site name does not match the name of the directory that contains it, you may specify the site name using the `--site` option:

```bash  theme={null}
herd isolate-node 21 --site="site-name"
```

You can be as specific as you want, when isolating Node.js versions:

```bash  theme={null}
herd isolate-node 16.13.2
```

You may execute the `isolated-node` command to display a list of all of your isolated sites and their Node.js versions:

```bash  theme={null}
herd isolated-node
```

To revert a site back to the globally installed Node.js version, you may invoke the `unisolate-node` command from the site's root directory:

```bash  theme={null}
herd unisolate-node
```

## Updating Node.js

If you open the Node settings, Herd checks if there are new versions available and displays an update button next to every version that you can update.

<Frame>
  <img alt="Update Node.js in the Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8a0556b87455cdfa4cdfb144a6626629" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_node_update.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=5373cd10b35562bb98ef85fb29cac63b 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=76f7dfc022a33eddb76d3038a0cbdca0 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8ad859b62d8bdf39262585ec18051883 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=6e42efd9b53dd1518457e7f041737244 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=a6683618126b60df2fdac9ff9e971466 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_node_update.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9f1f9414f5dbf74018f1a52ad9c82344 2500w" />
</Frame>

Herd uses nvm under the hood and this means that existing versions are kept when pressing the update button. The update downloads and installs the latest version and makes this one the preferred version for the related major version.

## Uninstalling Node

If you want to uninstall a specific version, either consult the [official nvm documentation](https://github.com/nvm-sh/nvm) or run the uninstall command from your terminal.

```
nvm uninstall VERSION
```

You can verify which versions you have with the command `nvm list`. So if you want to uninstall node 18.20.4, run `nvm uninstall 18.20.4`.

## Troubleshooting

Herd parses command output to determine your current Node.js version. If it can't parse the output because there is output that it doesn't understand, or you are using an unsupported shell, it displays `Unknown` for your node version in the sites list. Herd is an opinionated development environment that relies on bash or zsh, so other shells can lead to errors.

There are situations where Herd can not install nvm and keeps displaying the install button for nvm in the settings. This can happen if there are traces of a previous install on your system – this could be a broken node symlink or nvm paths in your `.zshrc` file.


# PHP Extensions
Source: https://herd.laravel.com/docs/macos/technology/php-extensions



# Included PHP Extensions

Herd includes the most common PHP extensions that also come pre-installed on any [Laravel Forge](https://forge.laravel.com)  provisioned server. This means that you can use the following extensions without any additional setup:

### bcmath

The BCMath extension provides arbitrary-precision arithmetic. It allows you to work with large numbers and perform mathematical operations with high precision, which is particularly useful in financial applications.

### bz2

The BZ2 extension enables data compression using the bzip2 algorithm. This reduces file sizes and improves storage efficiency.

### calendar

The Calendar extension provides functions to convert between different calendar formats. It supports conversions between Julian, Gregorian, and Jewish calendars, among others.

### ctype

The Ctype extension provides functions to check for and convert between character types. It is useful for validating and sanitizing text input.

### curl

The cURL extension enables HTTP requests using various protocols. It is essential for integrating with third-party APIs and fetching external data.

### dba

The DBA extension allows you to interact with flat-file databases, like DBM. It provides a simple way to store and retrieve key-value pairs.

### dom

The DOM extension provides a complete API for working with XML documents via the Document Object Model. It simplifies XML parsing and manipulation.

### exif

The Exif extension reads Exchangeable Image File (Exif) metadata from images. It allows you to access camera information, orientation, GPS data, and more.

### ffi

The Foreign Function Interface (FFI) extension allows PHP to call functions written in other languages (like C) directly, providing the ability to use libraries written in those languages.

### fileinfo

The Fileinfo extension detects file types based on file signatures. It is useful for security checks and content-type validation.

### filter

The Filter extension provides a simple way to sanitize and validate data, particularly user input, ensuring data integrity and security.

### ftp

The FTP extension provides functions for accessing files on FTP servers. It simplifies the process of transferring files over FTP.

### gd

The GD extension offers functions for creating and manipulating images. It supports several image formats and provides capabilities like resizing, cropping, and drawing shapes.

### gmp

The GMP extension provides functions for arbitrary-precision arithmetic using the GNU Multiple Precision (GMP) library. It is ideal for cryptographic applications.

### iconv

The Iconv extension provides functions for converting between different character encodings. It ensures text compatibility across various languages and encoding formats.

### igbinary

The Igbinary extension provides an alternative binary serialization format. It reduces storage space and speeds up data deserialization.

### imagick

The Imagick extension provides an interface to the ImageMagick library, enabling advanced image processing capabilities, such as resizing, blurring, and color correction.

### imap

The IMAP extension provides functions to interact with email servers using IMAP, POP3, and NNTP protocols. It is useful for reading, composing, and sending emails.

### intl

The Intl extension provides internationalization functions, including formatting numbers, dates, currencies according to locale, and handling text in different languages.

### ldap

The LDAP extension allows PHP to interact with LDAP (Lightweight Directory Access Protocol) directories. It is useful for managing centralized user directories and authenticating users.

### lz4

The LZ4 extension provides fast compression and decompression using the LZ4 algorithm. It is suitable for applications requiring high-speed data compression.

### mbstring

The Multibyte String (Mbstring) extension provides functions to handle multibyte encodings, making it essential for processing non-ASCII text.

### mongodb

The MongoDB extension allows PHP to interact with MongoDB databases. It is essential for building applications that use MongoDB as the data store.

### mysqli

The MySQLi extension provides an improved interface to MySQL databases. It supports prepared statements, transactions, and multiple query results.

### opcache

The Opcache extension improves PHP performance by caching precompiled script bytecode, reducing the need for PHP to recompile scripts on each request.

### openssl

The OpenSSL extension enables secure data transmission using SSL and TLS protocols. It provides functions for encryption, decryption, and handling of digital certificates.

### pcntl

The PCNTL extension enables process control functions, allowing you to manage parallel processing and signal handling in PHP.

### pdo

The PHP Data Objects (PDO) extension provides a unified interface for database access. It supports prepared statements and various database drivers.

### pdo\_mysql

The PDO\_MySQL extension provides a PDO driver for MySQL databases, enabling secure and efficient access to MySQL using prepared statements.

### pdo\_pgsql

The PDO\_PgSQL extension provides a PDO driver for PostgreSQL databases, allowing secure and efficient access to PostgreSQL using prepared statements.

### pdo\_sqlite

The PDO\_SQLite extension provides a PDO driver for SQLite databases, facilitating lightweight and embedded database access with minimal configuration.

### pdo\_sqlsrv

The PDO\_SQLSRV extension provides a PDO driver for Microsoft SQL Server databases, enabling secure and efficient access to SQL Server using prepared statements.

### pgsql

The PgSQL extension provides native PostgreSQL database functions, offering comprehensive access to PostgreSQL features.

### phar

The Phar extension enables packaging PHP applications into a single file archive (PHAR). It simplifies application distribution and deployment.

### posix

The POSIX extension provides functions for POSIX-like system calls, useful for handling process management and file permissions.

### readline

The Readline extension provides interactive command-line editing capabilities. It enhances the CLI experience by supporting history and line editing.

### redis

The Redis extension allows PHP to interact with the Redis in-memory data structure store. It is essential for caching, message brokering, and real-time data processing.

### session

The Session extension manages session data between requests. It simplifies storing and retrieving user-specific data securely.

### shmop

The SHMOP extension allows PHP to read and write shared memory segments. It is useful for IPC (Inter-Process Communication).

### simplexml

The SimpleXML extension provides a simple interface for parsing and manipulating XML documents. It makes working with XML data intuitive and efficient.

### soap

The SOAP extension provides functions for building and consuming SOAP-based web services. It simplifies integrating with legacy systems that use SOAP.

### sockets

The Sockets extension provides functions for low-level socket communication, enabling PHP to create network clients and servers.

### sodium

The Sodium extension provides modern cryptography functions. It is useful for encryption, decryption, password hashing, and digital signatures.

### sqlsrv

The SQLSRV extension allows PHP to interact with Microsoft SQL Server databases. It is essential for building applications that use SQL Server as the data store.

### sqlite3

The SQLite3 extension provides native functions for interacting with SQLite databases, offering efficient and lightweight database access.

### sysvmsg

The SysVMsg extension allows PHP to send and receive System V IPC messages. It is useful for messaging between multiple processes.

### sysvsem

The SysVSem extension provides functions for managing System V semaphores, which are useful for synchronizing multiple processes.

### sysvshm

The SysVShm extension allows PHP to read and write System V shared memory segments. It is useful for sharing data between multiple processes.

### tokenizer

The Tokenizer extension provides functions to parse PHP code into tokens, making it useful for syntax highlighting and static analysis.

### xml

The XML extension provides a basic set of tools for working with XML data, allowing for parsing and validation.

### xmlreader

The XMLReader extension provides a fast, non-caching XML parser, suitable for processing large XML files efficiently.

### xmlwriter

The XMLWriter extension offers functions for creating XML documents via a writer API, providing efficient XML generation.

### xsl

The XSL extension allows you to transform XML documents using XSLT stylesheets. It enables flexible data transformation between XML formats.

### zip

The Zip extension provides functions for creating, modifying, and extracting files from ZIP archives, simplifying archive management.

### zlib

The Zlib extension provides functions for data compression and decompression using the zlib library. It is useful for reducing storage space and network bandwidth.

# Installing PHP extensions

You may add additional PHP extensions that are not included out of the box with Herd, by installing them via [Homebrew](https://brew.sh) and [pecl](https://pecl.php.net/). The reason for this is that most of these extension have dependencies and can not be statically compiled, and therefore shipped, with Herd.

## Adding extensions

To install additional extensions via Homebrew, you can compile them with the following commands. At first, Homebrew needs a base PHP for compiling the extension. This base PHP is only used for compiling the extension and Herd keeps using the static binaries, so you can still use the built-in Herd updater for PHP.

```bash  theme={null}
brew install php
```

Once PHP is installed via Homebrew, you may install the extension:

```bash  theme={null}
pecl install [extension-name]
```

This creates an `[extension].so` extension file that you can now activate and use with Laravel Herd.

On an M1/M2 Mac, the extension can be found at `/opt/homebrew/lib/php/pecl`.
On an Intel Mac, it will be at `/usr/local/lib/php/pecl`.

## Activating extensions

You may activate your custom extensions by editing your `php.ini` file.
This file is located at `~/Library/Application Support/Herd/config/php/<version>/php.ini.`.

```bash  theme={null}
# Absolute path to the extension.so file
extension=/opt/homebrew/lib/php/pecl/20220829/[extension].so
```


# PHP Settings
Source: https://herd.laravel.com/docs/macos/technology/php-settings



# Changing PHP settings

The values that most developers change are the memory limit and the max upload size. You can modify them in the settings and don't need to go deep into configuration files.

<Frame>
  <img alt="Screenshot of settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=280cf026f25d384aad7b5a9e71639ef0" data-og-width="1460" width="1460" data-og-height="1226" height="1226" data-path="images/docs/settings_php_config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0755d54cb22be60d2ade51f4f283ca72 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=2a1e4c980d8efffed9b0180f3c1d1877 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f1a325853ccd6c1f2879894b51586c9d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=0836c3a7cd78ebe20b4296da5f1a8261 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4d1f82e13c30a3e32472ac0d7a38a8e0 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_config.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=69c049d38cf53ab1bdb080ee81c89c5c 2500w" />
</Frame>

Herd gives you easy access to the PHP configuration files on your machine, the easiest way to get to the file is to select the php.ini directory from the context menu of the settings.

<Frame>
  <img alt="Screenshot of context menu" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=842bf0e50500c9dbe0aae22afaba86af" data-og-width="1460" width="1460" data-og-height="1226" height="1226" data-path="images/docs/settings_php_ini.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c9ef495bdf25217bd3dbdc6152e47733 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1c79b81c17b5de14bc6a584f2a71c795 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ee6081b74ebb4f5fc489afbd1d6ced7d 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=e5e7599b87da4f1e0d07dbeb2e2a29fb 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=849ee1978e7c198c71c55c10d15a05cb 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_ini.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=39a98ffb3ca0b3c0afa16b351dd266a7 2500w" />
</Frame>

Each PHP version has its own `php.ini` file at `~/Library/Application Support/Herd/config/php/<version>/php.ini`.
You can edit this file to change or add PHP settings for a specific PHP version.

<Note>
  If you want to quickly access your php.ini file via the CLI, you may use the `herd ini` command.
</Note>

All saved changes are immediately available in the CLI, but you need to restart all Herd services to apply the changes to HTTP requests via nginx.

You can restart all services by clicking "Stop all" and then "Start all" in the Herd dropdown menu in the menu bar – it just takes 1-2 seconds. If a service does not restart properly, or you believe that there is a stale process still running with old settings, you can press the `Option` key when the menu is open and select `Force stop all`.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=f33cb90c9526a4545cf88e815b726db6" data-og-width="1030" width="1030" data-og-height="522" height="522" data-path="images/docs/stop-all.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=6a73e3438bc6146966481d14c79752f1 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=50daf5112c710f525b6ceea0995487b2 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=1558ddccb3ae9a28e944ec3ecfd49ba7 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=fee9f4b1a90a75d818998923ca0fd41c 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ab9d0051cf3634c8c3813c153892e3c8 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/stop-all.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=482edfa477152444f206c5258a5a2f48 2500w" />
</Frame>

Alternatively, you can use the `herd restart` command in the terminal.

```shell  theme={null}
herd restart
```


# Manage PHP
Source: https://herd.laravel.com/docs/macos/technology/php-versions



# Using different PHP versions

Herd ships with the latest stable PHP version by default. Currently, that's PHP 8.3.
However, you may install and use different PHP versions for your sites and configure Herd that every project uses the version that it needs.

## Using different PHP versions via the GUI

You can manage your PHP versions in the "PHP" tab of the preferences window. This window allows you to install and update PHP versions with a single click.

<Frame>
  <img alt="PÜHP Settings" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=01e2b296bcf1083c067a64448fb3a59e" data-og-width="1460" width="1460" data-og-height="1102" height="1102" data-path="images/docs/settings_php.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=814d5205dcab367927c8c4f5857c397f 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=56305abf49727320292bc7f9723cd94d 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=caea1f2fd4438b6d5a51e1d4a3da4f7b 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=c1f32ae6a2b783271955312bde4ab462 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=e3b2351c2a3656ff51aead67c1b50b6a 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/settings_php.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1805d75e46bb7f0207e95237a9dd543c 2500w" />
</Frame>

In order to change the global PHP version that Herd uses by default, select it in the dropdown menu in the menu bar.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cf9561d5a37eaa389c670e0244a08ec8" data-og-width="828" width="828" data-og-height="796" height="796" data-path="images/docs/dropdown_php.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=1a443bd6c891dabad1d20cbdf79e2614 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=09a171194bad039dbf92514e328a412e 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8f832bb23eb99419c2dfb7cc57581632 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=625332547196638116df0914971417ed 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=35fae0d81c6e69a95b6f3ef2df518ef6 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/dropdown_php.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8a097a32c55bb66fb3788fc4a42d4038 2500w" />
</Frame>

Herd uses the global PHP version for all sites that are not [isolated](#per-site-php-versions).

## Using different PHP versions via the CLI

If you prefer to use the CLI, you can use the `herd use` command to set the global PHP version.

```shell  theme={null}
herd use 8.2
```

# Per-site PHP versions

By default, Herd uses the global PHP version to serve all your sites. However, if you need to support different PHP versions for different sites, you may use the isolate function.  This configures Herd to use a specific PHP version for a site, regardless of the global PHP version.

## Per site PHP versions via the GUI

You can configure the PHP version per site in the [Site Manager](/macos/sites/managing-sites). This gives you a list of all your sites and allows you to configure the PHP version that each site uses.

Just select the PHP version that you want to use for the site in the dropdown menu.

<Frame>
  <img alt="" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=43d575bfeec38ade48f0b1069ca3323a" data-og-width="1800" width="1800" data-og-height="1196" height="1196" data-path="images/docs/sites.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ac0f52cb86238074a2b66b04dc09615c 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=dbab61657028c779f437b463c73941ce 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=9448dd15ca3cffb589862c0e5eb4b3d6 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=a6a9911ecd770528c2b357f6593f1ace 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=06807e86f4ea012969518118d31df970 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/sites.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=c75c44b14e5267d073ecb0c5ea7b6788 2500w" />
</Frame>

## Per site PHP versions via the CLI

If you prefer to use the CLI, you can use the `herd isolate` command to specify which PHP version a particular site should use.
The `isolate` command configures Herd to use the specified PHP version for the site located in your current working directory:

```shell  theme={null}
cd ~/Herd/example-site

herd isolate 8.0
```

If your site name does not match the name of the directory that contains it, you may specify the name using the `--site` option:

```shell  theme={null}
herd isolate 8.0 --site="site-name"
```

For convenience, you may use the `herd php`, `composer`, and `which-php` commands to proxy calls to the appropriate PHP CLI or tool based on the configured PHP version for the current directly and site:

```shell  theme={null}
herd php
herd composer
herd which-php
```

You may execute the `isolated` command to display a list of all of your isolated sites and their PHP and Node.js versions:

```shell  theme={null}
herd isolated
```

To revert a site back to Herd's globally installed PHP version, you may invoke the `unisolate` command from the root directory of the site:

```shell  theme={null}
herd unisolate
```

## Uninstalling PHP versions

You can uninstall PHP versions from the PHP settings. Simply right-click on a version and delete it via the context menu.

<Frame>
  <img alt="Delete PHP from Settings" src="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=7e71c4f9cb248234d1f43127df5300ed" data-og-width="1460" width="1460" data-og-height="1226" height="1226" data-path="images/docs/settings_php_delete.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=280&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=10f64d8605134efe0b4143f9e0d82b85 280w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=560&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=ebf73d931912bd79bca61a241d404c34 560w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=840&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=4bad7c030b785e88ac80d5a150554f39 840w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=1100&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=b589088c9de724583f888d76cd375ff5 1100w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=1650&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=858ee29f74a2a98cf49cd2c51ff15d48 1650w, https://mintcdn.com/herd/DeXoYubPfJnYhPtY/images/docs/settings_php_delete.png?w=2500&fit=max&auto=format&n=DeXoYubPfJnYhPtY&q=85&s=5f0465ab0c6da0a2622f616f0e3b1b30 2500w" />
</Frame>

If you prefer deleting a PHP version manually, you can go into the Herd application directory and delete the files from your system. Once you reopen the settings, you can reinstall them.

```
~/Library/Application Support/Herd/bin
```


# Common Issues
Source: https://herd.laravel.com/docs/macos/troubleshooting/common-issues



# Resolving Common Issues

If you are on this site, we're sorry. We are working to create the most robust and easiest to use local development environment for Laravel – but Herd is still a tool early in its lifecycle, and we aren't there yet. On this page, you'll find common issues and a solution to resolve them.

If the documentation and the following tips don't resolve your issue, please head over to the [support section](/macos/troubleshooting/support).

## Herd Debug Logs

You can enable debug logs for Herd by starting it via the command line. The logs usually provide enough information so that you can either fix the problem yourself or create an issue in the [community repository](/macos/troubleshooting/support#community-support).

```
open /Applications/Herd.app --args --enable-logfile
```

This command writes a `Herd_Debug.log` file to your log directory at `~/Library/Application Support/Herd/Log`.

## Bad Gateway

This can happen if the nginx configuration for your site is broken, or PHP FPM did not start properly.

You can find the configuration files at the following path:

```
/Users/seb/Library/Application Support/Herd/config/valet/Nginx
```

A good practice to fix the config file for a single site is by isolating the site to a specific PHP version or securing it with a TLS certificate. You can always switch back to the previous PHP version or unsecure the site but all these commands regenerate the configuration file to fix the issue.

If this does not help, please create an issue with the broken config file in the [community repository](/macos/troubleshooting/support#community-support).

## 404 Errors

If Herd can not properly detect a driver for your site or can't find the site at all, Herd displays a custom 404 error page. This error page mostly has a useful hint how to fix the problem but it case it does not, the most common problem is that the directory of the project includes `www` in the name.

Herd strips `www` from directory names so that all sites are accessible via their domain with and without `www` prefix.

The solution to this is renaming the directory from `www.your-site.com` to `your-site.com`. This allows yout to access the site at `http://your-site.com.test`. If the site had specific configurations, you need to apply them again after this change because Herd treats this site as a new one.

## DNS Errors

DNS errors happen when either dnsmasq isn't running or when there is a different local DNS server installed on your machine.

Please make sure that dnsmasq is running and there are no errors in the logs. Dnsmasq gets started by the background service of Herd, please go to [the helper service isn't running](#the-helper-service-isnt-running) to resolve the issue.

If there's still a problem, another instance of dnsmasq could be running on your system. This mostly happens if you migrate from Valet to Herd and Herd isn't able to remove the brew service. You can run `brew services list` to see if Homebrew still manages a dnsmasq instance and `brew services stop dnsmasq` to shut it down. After that, restart all Herd services and you should be good to go.

**VPN clients may interfere with DNS resolution**

Some VPN clients install macOS Network Extensions which intercept DNS traffic, even if the VPN connection itself is not active.
This may prevent Herd from resolving `.test` domains correctly via its internal `dnsmasq` resolver.

When your browser returns `ERR_CONNECTION_RESET` or `curl` shows `Recv failure: Connection reset by peer`, it is likely that a VPN client is interfering with DNS resolution.

To resolve this issue, you can try the following steps:

* Fully uninstall the VPN client if not required.

* Alternatively, disable any "DNS Proxy" or "DNS Intercept" options in the VPN configuration.

* After uninstalling, reboot your Mac to clear all DNS overrides.

You can verify whether a VPN system extension is active using:

```bash  theme={null}
systemextensionsctl list
```

Look for entries such as:

`com.vpnnet.vpnclient.macos.vpn.nwestension`

## Herd shows the welcome screen on every start

This means that the helper service isn't running in the background. Please follow [The helper service isn't running](#the-helper-service-isnt-running) to resolve the issue.

## The helper service isn't running

Herd uses a helper service that runs with admin permissions to start dnsmasq and nginx. This comes with the benefit that there are no admin permissions required for the main application and if anyone finds a way to exploit Herd, they can not compromise your system.

<Frame>
  <img alt="Login Items" src="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/login_items.png?fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=7b1fbea792c7d22d2b49cd922d22acd9" data-og-width="1530" width="1530" data-og-height="1322" height="1322" data-path="images/docs/login_items.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/login_items.png?w=280&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=717f0cbfd62dbaeee5a00036622e7cf3 280w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/login_items.png?w=560&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=cc4828394e18b3823772685075d78e50 560w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/login_items.png?w=840&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=8e7cda2d46f6fb9bce97ca71013c2429 840w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/login_items.png?w=1100&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=d350aa89875b4674a258a818d66f9943 1100w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/login_items.png?w=1650&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=9eb3f3cb0b5324b7707ebbeb986e48e9 1650w, https://mintcdn.com/herd/pbdN92VyM5BkjAJV/images/docs/login_items.png?w=2500&fit=max&auto=format&n=pbdN92VyM5BkjAJV&q=85&s=4439f85857d9b5da802ecc052e55c63e 2500w" />
</Frame>

To allow the Herd helper service to run in the background, please go to the "Login Items" section of your system settings and make sure that either `Herd` or `Beyond Code GmbH` ([us](https://beyondcode.com)) are allowed to run in the background.


# ODBC Drivers
Source: https://herd.laravel.com/docs/macos/troubleshooting/odbc-drivers



# Using Microsoft ODBC Drivers on macOS

You might encounter the following error message when trying to use the Microsoft ODBC Driver for SQL Server on macOS:

> "This extension requires the Microsoft ODBC Driver for SQL Server to communicate with SQL Server."

In order to install the missing ODBC driver, please take a alook at the latest official [ODBC Driver installation guide](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver16#microsoft-odbc-18) from Microsoft.

After installing the driver, you will need to manually symlink the Homebrew installed driver to the default location where the Microsoft ODBC Driver for SQL Server expects it to be. This can be done by running the following command:

<CodeGroup>
  ```bash ARM macOS theme={null}
  sudo ln -s /opt/homebrew/etc/odbcinst.ini /etc/odbcinst.ini
  sudo ln -s /opt/homebrew/etc/odbc.ini /etc/odbc.ini
  ```

  ```bash Intel macOS theme={null}
  sudo ln -s /usr/local/etc/odbcinst.ini /etc/odbcinst.ini
  sudo ln -s /usr/local/etc/odbc.ini /etc/odbc.ini
  ```
</CodeGroup>


# Restarting Services
Source: https://herd.laravel.com/docs/macos/troubleshooting/restarting-services



# Restarting Herd Services

It might happen that Herd displays that a service like `FPM` is not running for a specific PHP version. This can happen if Herd is unable to properly shut down all background services when you close the app or migrate from a previous setup.

## Via the GUI

You may force a restart of all Herd services by clicking on the Herd icon in the menu bar and holding the `option` key `⌥`.
This will change the `Stop all` menu item to `Force stop all`. Click on it to forcefully stop all Herd services, and then click on `Start all` to restart them.

## Via the terminal

To kill all stray services, go to your terminal and perform the `killall` command for every service that is still running, naming the services.

## Force a shutdown of all Herd services

This command shuts down all processes that Herd might run (PHP 7.4 - 8.4, Nginx and Dnsmasq).

### Shutdown all Herd services on Apple Silicon Macs

```shell  theme={null}
sudo killall nginx-arm64 dnsmasq-arm64 \
php74-fpm \
php80-fpm \
php81-fpm \
php82-fpm \
php83-fpm \
php84-fpm
```

### Shutdown all Herd services on Intel Macs

```shell  theme={null}
sudo killall nginx-x86 dnsmasq-x86 \
php74-fpm \
php80-fpm \
php81-fpm \
php82-fpm \
php83-fpm \
php84-fpm
```

## Restart the background service

Herd has a background service that is responsible for running nginx and dnsmasq as root on your machine. You can shutdown this services by terminating if via the activity monitor of macOS and searching for a service with the name `de.beyondco.herd.helper`.


# Support
Source: https://herd.laravel.com/docs/macos/troubleshooting/support



# Community Support

If you encounter any technical issues that you can't solve with the docs or the troubleshooting section, please check the issues in the [community repository](https://github.com/beyondcode/herd-community/issues?q=).

If there is no closed issue that solves your problem, please create a new one so that we can follow up and make the solution available to everyone until we can provide a fix.

## Email support

[Herd Pro](/#plans) or [Herd for Teams](/#plans) users can get priority email support at [support@beyondco.de](mailto:support@beyondco.de). We usually respond within a few hours during weekdays.

Also do not hesitate to email us if you have a license or billing related question.

## Security Related Issues

If you discover any security related issues, please email [support@beyondco.de](mailto:support@beyondco.de) instead of using the issue tracker.


# Uninstalling Herd
Source: https://herd.laravel.com/docs/macos/troubleshooting/uninstalling



# Uninstalling Herd

In case you want to uninstall Herd from your machine, you may use the uninstall script that Herd provides:

<Warning>
  Please backup your data of Herd Pro services before running the uninstaller. The uninstaller deletes all application files, configurations and services like databases and storage.
</Warning>

To automatically uninstall Herd, all data within Herd Pro services and all of its settings, run the following command in your terminal:

```bash bash theme={null}
/Applications/Herd.app/Contents/Resources/uninstall
```

<Accordion title="Manual Uninstall Steps">
  1. Quit Herd by clicking on the icon in the menu bar and selecting "Quit".
  2. Run the following command in your shell. This will reset the permissions of Herd to start its services.
     ```shell  theme={null}
     $ sudo rm /etc/sudoers.d/herd
     ```
  3. Make a backup of your Herd Pro services `~/Library/Application Support/Herd/config/services`
  4. Delete the `~/Library/Application Support/Herd` folder.
  5. Remove Herd from your Applications folder.
  6. Open your `~/.zshrc` or `~/.bashrc` file and remove the modifications to the `PATH` environment variable that Herd injected as well as all other Herd related modifications that are marked with `# Herd`.
  7. Go to `/etc/resolver/test` and either delete this file or check its contents. This maps all domains with `.test` to a local nameserver and can be removed if it's only pointing to 127.0.0.1.
  8. Delete the last config traces from the system defaults with `defaults delete de.beyondco.herd`
</Accordion>

## Re-installing Herd

1. Uninstall Herd as described above.
2. Download the latest version of Herd from the website and install it from scratch.


