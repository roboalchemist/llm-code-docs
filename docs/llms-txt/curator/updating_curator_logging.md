# Source: https://docs.curator.interworks.com/server_management/system_administration/updating_curator_logging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating Curator Logging

> Manual steps to update Curator logging system structure and prevent log files from consuming excessive disk space.

In a recent update to Curator, we changed the structure of the logging system.  In some instances, the
automated update may not work due to server configuration issues.  Below you'll find the steps to manually
update the logging file.  Following the steps below will ensure your logs do not consume too much space on
your server.

## Add Logging.php file to your config folder (Linux)

1. SSH to your webserver
2. cd into your config folder - on a standard install it will be: `cd /var/www/html/config`
3. Retrieve the file from the Curator website and rename it using the command below:
   `wget -O logging.php https://curator.interworks.com/file/logging.php.txt`
4. Ensure permissions on the file are set correctly, on a standard install you will want to ensure the apache
   user is the owner of the file:
   `sudo chown apache:apache logging.php`

## Add Logging.php file to your config folder (Windows)

1. Start a remote session / RDP in to your webserver
2. Navigate to the webserver root folder and find the config file - on a standard install it will be C:\InterWorks\Curator\config
3. Download the logging file from the Assets section on the left-hand nav
4. Place the file into the config folder and rename it to **logging.php**
5. Ensure the permissions on the file are correct (confer with our [filesystem permissions guide](/server_management/system_administration/filesystem_permissions))
