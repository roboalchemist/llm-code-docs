# Source: https://docs.curator.interworks.com/upgrading_migration/upgrading/dependency_updates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dependency Updates

> Instructions for updating PHP, Apache, or MariaDB dependencies on your Curator webserver.

Curator's upstream dependencies (PHP, Apache, and MariaDB) require periodic updates to maintain security, performance,
and compatibility with the latest Curator features.

*Note: Before upgrading any dependencies, it is a good idea to ensure that you have a recent Curator backup available.*

## PHP Dependencies by Curator Version

| Curator Version | Minimum PHP Version | Maximum PHP Version |
| --------------- | ------------------- | ------------------- |
| 2023.03.01      | 8.0                 | 8.0                 |
| 2024.10.04      | 8.0                 | 8.1                 |
| 2025.07-03      | 8.0                 | 8.3                 |
| 2025.09-03      | 8.1                 | 8.3                 |
| 2026.04-01      | 8.3                 | 8.3                 |

### Important Notes

* Always ensure your PHP environment meets or exceeds the minimum version requirement for your Curator installation.
* Upgrading Curator may require upgrading your PHP version.
* Check your current PHP version with `php --version`.

## Windows

First and foremost: ensure all relevant Windows Updates have been applied to your server.

Next, update Curator dependencies.

Curator bundles PHP and Apache upgrades into a simple utility package to make updating them as easy as possible.

To update Curator's dependencies, simply download our **[Curator Dependency Update Utility](https://portals.interworks.com/Curator_PHP_Upgrade_Util.exe)**.

Once downloaded, simply double-click the utility to run updates.
PHP and Apache will be upgraded automatically by this utility.

**Note: Internet access is required for this process. Systems without internet access will need to upgrade manually.**

### Manual Dependency Updates

If your server has restrictions that prevent the utility from downloading files automatically, you can manually download
the required files and run the upgrade utility locally.

To manually upgrade dependencies:

1. Download the **[Curator Dependency Update Utility](https://portals.interworks.com/Curator_PHP_Upgrade_Util.exe)** on
   a system with internet access.

2. Download the following files to the same directory as the utility.
   <Warning>File names must match exactly as shown below for the utility to recognize them.</Warning>
   * **vc\_redist.exe** - VC Redistributables: [https://api.curator.interworks.com/file/vc\_redist](https://api.curator.interworks.com/file/vc_redist)
   * **php.zip** - PHP package: [https://api.curator.interworks.com/file/php\_apache](https://api.curator.interworks.com/file/php_apache)
   * **apache.zip** - Apache updates: [https://api.curator.interworks.com/file/apache](https://api.curator.interworks.com/file/apache)

3. Transfer all files (the utility and the three downloaded files) to your Curator server.

4. Ensure all five files are in the same directory, such as having them all on your Desktop,
   then double-click the utility to run the upgrade.

*Note: The utility will detect the locally available files and use them instead of attempting to download them. If the
file names do not match exactly, the utility will not recognize them and will attempt to download them from the internet.*

### Manual MariaDB Updates

To manually upgrade MariaDB, download the [MariaDB package](https://api.curator.interworks.com/file/mariadb) using
the link below.

*Note:* To upgrade MariaDB, you will need your root database password.
If you do not know this password, check your installation directory for an *Curator.txt* file, which contains
the default credentials.

### MariaDB on Windows

To upgrade MariaDB on Windows, first stop the *CuratorDB* Service, using Window's *Services* app.

You can open Window's *Services* by simply searching for *Services* using the Window's start bar.

To stop the *CuratorDB* process, find it in the *Services* list, then right click on it and click *Stop*.

Next, find Curator's MariaDB installation folder.

*Note:* This can usually be found in C:\InterWorks\Curator\libs\MariaDB.

Rename to MariaDB's *bin* folder to *bin.bkp*.

After a successful upgrade, you can delete this backup directory.

Then, download the latest [MariaDB](https://api.curator.interworks.com/file/mariadb) package.
Unzip this package over top of Curator's MariaDB installation.

Finally, open PowerShell in Administrative mode and run MariaDB's upgrade utility.
To open Powershell in Administrative mode, use the search widget in Window's start bar.
Search for Powershell, then Right-Click on Powershell and click "Run As Administrator".

Navigate to MariaDB's bin directory and run the upgrade utility.

```bash  theme={null}
cd C:\InterWorks\Curator\libs\MariaDB\bin
mysql_upgrade_service.exe --service=CuratorDB
```

Note: if you have trouble with the MariaDB's *service* upgrade utility, you can also use the non-service version.
To do this, first restart MariaDB in Window's *Services* app, and then run this command:

```bash  theme={null}
mysql_upgrade.exe -u root -p --force
```

## Linux

Linux's upstream repositories handle dependency updates, so first ensure you are running a recent version of your Linux distribution.

If you're not sure, you can take a look at our recommended distributions on the [Linux Installation page](/setup/installation/linux_installation).

To update Curator's Linux dependencies, SSH into your web server and cd into the webroot directory
(typically /var/www/html) and ensure you're using a user that has full sudo access, and run the command below.

This command will upgrade PHP, MariaDB, Apache, and any other operating system dependencies required by Curator:

```bash  theme={null}
curl -s -o php_upgrade_util.sh https://api.curator.interworks.com/scripts/php_upgrade_util.sh && chmod +x ./php_upgrade_util.sh && ./php_upgrade_util.sh
```
