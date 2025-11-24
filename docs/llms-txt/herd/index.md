# Source: https://herd.laravel.com/docs/macos/changelog/index.md

# Changelog

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
