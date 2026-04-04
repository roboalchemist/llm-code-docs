# Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/troubleshooting_upgrades.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Upgrades

> Common upgrade issues and solutions to help resolve problems during the Curator update process.

Occasionally, you may run into issues during the upgrade process. We've provided some common scenarios and
how to quickly resolve them below.

**NOTE:** While running updates, it is always a good idea to have someone on standby during your upgrade who
has access to the server that Curator is running on, as most of these debugging solutions require
server-level access.

## Re-run the Upgrade With an Alternate Method

Curator can be upgraded in several different ways, so if you run into an issue upgrading in a specific way,
try using an alternative method to upgrade.

For example, there may be an issue with running the "one click" upgrade on your system.

Try upgrading via the Curator API, or using the Manual Upgrade method.

Both of these upgrade methods are detailed in our [System Upgrade Guide](/upgrading_migration/upgrading/system_upgrade).

## Dependency Upgrades

If Curator requires dependency updates before upgrading, such as PHP, follow the steps provided in our
[dependency upgrades](/upgrading_migration/upgrading/dependency_updates)
documentation.

## Updating the Curator Database (Running Migrations)

Curator's database is often modified during the upgrade process, and if database changes are not completed
successfully database errors can occur.

If you run into any database errors after upgrading, or during the upgrade process, re-running Curator's
database migrations can resolve these errors.
You can safely rerun these migrations multiple times without any adverse effects.

**To Re-run the Curator Database Migrations From Your Browser:**

1. Visit your Curator url in a web browser, but add `/up` to your URL, for example: `https://curator.example.com/up`
2. You should be directed to a page that contains "success" followed by a list of the steps taken to finish
   the migration. If you see errors instead, make note of the errors seen and contact Curator support for
   further assistance.

**To Re-run the Curator Database Migrations From the Web Server:**

1. Open a command prompt/terminal.
2. *Double-check* that you are running the terminal/command prompt as the same user that is running Curator
   (you can find this information on the backend of Curator under **Settings** > **Curator** > **Status**).
3. Use the `cd` command to move the command prompt into your webroot (e.g. `cd /var/www/html` on Linux or
   `cd C:\InterWorks\Curator\htdocs` on Windows).
4. Type `php artisan winter:up` and then press ENTER.
5. Any remaining database migrations will run, and display status messages in green.
6. If there are any errors during this process, please take a screenshot and send it to Curator support.

## File System Permissions Issues

If Curator's logs contain errors relating to filesystem permissions on your Curator site, or the site itself
is rendering an error that says "failed to cache..." or "permission denied...", or "no such file found...",
use the following steps to resolve this issue:

1. Click the "clear cache" button on the backend of Curator
2. Use our [Filesystem Permissions Guide](/server_management/system_administration/filesystem_permissions)
   to fix any errant file permissions settings.

## Fix Corrupted Files

If Curator is displaying an error message stating "vendor files are missing" or some pages may throw a
warning message that some files were not able to be found, you can re-download the Curator system files to
your web server using the steps below:

***Fixing Corrupted File Systems on Linux:***

1. `cd` into your webroot directory (e.g. `/var/www/html`)
2. Run the commands below, replacing the `[curator_key]` in the URL with your Curator license key. If you
   don't know your license key, reach out to your account manager for more information.

   wget -O latest.zip "[https://api.curator.interworks.com/get\_version.php?key=\[curator\_key\]\&kernel=473\&version=latest](https://api.curator.interworks.com/get_version.php?key=\[curator_key]\&kernel=473\&version=latest)";
   unzip latest.zip;
   rm -Rf plugins/interworks;
   rm -Rf vendor;
   cp core/. . -Rf

   NOTE: You may replace `latest` in the URL above with a specific version
3. Manually rerun database migrations using the steps provided in the **Updating Curator Database** section.
4. Visit your Curator site in a web browser to confirm whether your site is back up and running.

***Fixing Corrupted File Systems on Windows:***

1. From a web-browser visit the URL below to download a .zip file with your Curator filesystem, replacing the
   `[curator_key]` in the URL with your Curator license key. If you don't know your license key, reach out to
   your account manager for more information.
   `https://api.curator.interworks.com/get_version.php?key=[curator_key]&kernel=473&version=latest`
2. Make a backup of your webroot in case of any errors that occur in the steps below.
3. Unzip the file that was downloaded from **Step 1** into your webroot (e.g. `C:\InterWorks\Curator\htdocs`)
   and replace all files with the newly extracted files.
4. Manually rerun database migrations using the steps provided in the **Updating Curator Database** section.
5. Visit your Curator site in a web browser to confirm whether your site is back up and running.

## Event Log Troubleshooting

***Event Log Retrieval if You Can Access the Curator Backend in a Web Browser:***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Logs** > **Event Log** section using the left-hand menu.
3. Look for any "upgrade" related errors.
4. Reach out to support for further troubleshooting.

***Event Log Retrieval if You Cannot Access the Curator Backend in a Web Browser:***

1. Log on to the web server that hosts Curator.
2. Find the Curator event logs:
   * **Windows**: `C:\InterWorks\Curator\htdocs\storage\logs`
   * **Linux**: `/var/www/html/htdocs/storage/logs`
3. Find the log file with today's date (e.g. system-2025-03-17.log ).
4. Copy the file and send it to Curator support.
