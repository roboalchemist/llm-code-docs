# Source: https://docs.curator.interworks.com/setup/central_dispatch/linux_central_dispatch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Central Dispatch

> Set up distributed processing capabilities with Central Dispatch on Linux systems

1. Install Curator using  [Linux installer](/setup/installation/linux_installation)
   like usual.

2. You *can*  make a new directory called  `centraldispatch`  at  `/var/www`  and move the contents of the webroot
   (`/var/www/html`) there or you can leave it as is. The newly deployed instances will be located at
   `/var/www/instance-name`  while the main Central Dispatch site remains at `/var/www/html` or `/var/www/centraldispatch`.
   The rest of the guide will assume `/var/www/html`  so change all of the commands to the correct path if you chose
   `/var/www/centraldispatch`.

3. Set up SSL for this initial instance. This
   [blog by the great and powerful Orr](https://interworks.com/blog/morr/2019/10/24/portals-for-tableau-101-setting-up-ssltls-certificates-for-https/)
   will get you most of the way there.  NOTE: Ubuntu systems are slightly different.

4. There should already be a default conf file that has an **IncludeOptional** line that points to a directory where
   additional vhost conf files can go. Make sure you know where the newly added vhost conf files should go:
   * Ubuntu:
     * Default conf:  `etc/apache2/apache2.conf`
     * Includes vhost conf files:  `etc/apache2/sites-enabled/*.conf`
     * Ubuntu is a little different and actually stages the conf files here before being enabled:  `/etc/apache2/sites-available/*.conf`
   * Everything else:
     * Default conf:  `/etc/httpd/conf/httpd.conf`
     * Includes vhost conf files:  `/etc/httpd/conf.d/*.conf`

5. Create database user using the `worker_database_user.sql` example script at
   `/var/www/html/plugins/interworks/centraldispatch/workers` directory. Tweak the password if you'd like before executing.
   * Run the sql file:

     ```bash  theme={null}
     mysql -u root -p curator < worker_database_user.sql
     ```

   * Enter root password

   * Test if the new user is there:  **mysql -u worker -p**

   * Enter worker password

6. Create directory  `/var/www/archives`

7. Set up worker script
   1. Copy php\_worker.example.php script to php\_worker.php in the `/var/www/html/plugins/interworks/centraldispatch/workers`
      directory:

      ```bash  theme={null}
      sudo cp php_worker.example.php php_worker.php
      ```

   2. Copy `vhost.template.example.conf` to `vhost.template.conf` in the same directory.

      ```bash  theme={null}
      sudo cp vhost.template.example.conf vhost.template.conf
      ```

   3. Make sure apache user owns everything:

      ```bash  theme={null}
      sudo chown -R $APACHEUSER:$APACHEUSER /var/www
      ```

   4. Tweak paths as needed in  `php_worker.php`
      1. DB\_ENV\_DISPATCHER uses details from step 5 above.
      2. DB\_ENV\_INSTANCE uses the root database details to be able to provision users as needed. Can set up dispatcher
         user with these permissions if you don’t want to use the root account.
      3. Modify vhost section:
         1. Uncomment `directory` and modify as needed to where the vhost conf files should go from step 4.
         2. Uncomment `template` for `/var/www/html/plugins/interworks/centraldispatch/workers/vhost.template.conf`.
      4. Modify worker section:
         1. Uncomment `source_directory` for `/var/www/html`.
         2. Uncomment `archive_directory` for `/var/www/archives`.
      5. Modify \$DEFAULT\_BACKEND\_EMAIL as needed.
      6. Modify \$LINUX\_APACHE\_RESTART to the relevant apache restart command for your distro.
      7. Modify \$LINUX\_APACHE\_USER to the relevant apache user for your distro.

   5. Tweak vhost template as needed in workers directory
      1. Comment out the #apache 2.2 lines (lines 22-23) and uncomment out the #apache 2.4 lines unless using Apache 2.2.
      2. Update SSLCertificateChainFile, SSLCertificateFile, and SSLCertificateKeyFile as needed.

   6. Schedule root to run worker with the following command. Feel free to change the frequency (this one is every 15
      minutes). Also, make sure to change  `$APACHEUSER`  to the relevant apache user in the chown command (this makes
      sure the application owns all the files even though root is making everything).

      ```bash  theme={null}
      (sudo crontab -l ; echo "*****/15 * * * * sudo php
      /var/www/html/plugins/interworks/centraldispatch/workers/php_worker.php >> /dev/null 2>&1 && sudo chown -R $APACHEUSER:$APACHEUSER /var/www****") | sudo crontab -
      ```

8. Restart apache

9. In the Central Dispatch Curator portal’s backend, register the workers with the dispatcher at **Backend** >
   **Settings** > **Central Dispatch** > **Central Dispatch Settings**. Probably with these settings:
   1. Host URL: localhost
   2. Worker name: localhost (or use something more descriptive)
   3. Install Path:  `/var/www`

10. Attempt to deploy a new managed instance at Backend > Central Dispatch > Managed Instances.

## Manual Back Out of Deployment

In case of a failure during a deployment, Central Dispatch is not yet able to automatically back out the deployment to
try again. You can determine the nature of the failure by visiting the Managed Instance record in the backend of the
Central Dispatch portal and scrolling to the bottom of the page. There will be an error field that will show any issues
the worker had during the deployment.

To back out a deployment, it's important to determine which step it failed at so you'll know which of the following
steps you'll need to take to back it out. They are in reverse order of the deployment, so you can skip steps if the
deployment didn't make it that far. When in doubt, just perform all of the steps.

1. Remove cron job with the name of this managed instance by using `sudo -u <apache user> crontab -e` to edit.
   *Note: This will use VI as the default editor in case you need to look up how to edit the file.*

2. If using Ubuntu, disable the vhost entry by running `sudo a2dissite <managed instance vhost record without .conf>`

3. Remove the vhost record specific to this managed instance in the vhosts directory (see step 4 above to determine
   location). The command will be similar to `sudo rm /etc/apache2/sites-available/<managed instance vhost record>`

4. Remove site-specific SSL/TLS certificate, key, and (optional) chain certificate, if the managed instance supplied
   them. These should be in the /etc/apache2/certs/ directory. The commands will be similar to these two commands below:

   ```bash  theme={null}
   sudo rm /etc/apache2/certs/<name of manage instance crt file>
   ```

   ```bash  theme={null}
   sudo rm /etc/apache2/certs/<name of managed instance key file>
   ```

5. Remove the portal code for the managed instance in the /var/www/ directory. The command will be similar to
   `sudo rm -Rf /var/www/<managed instance web root directory name>`

6. Drop the database specific to the managed instance by using `mysql -u root -p` and the root database credentials
   (see `/var/www/info.txt`). The SQL statement to drop the database would be: `DROP DATABASE '<database name>';`

7. Delete the database user specific to the managed instance by using `mysql -u root -p` and the root database
   credentials (see `/var/www/info.txt`). The SQL statement to drop the database would be:

   ```SQL  theme={null}
   DROP USER IF EXISTS '<username>'@'localhost';
   ```
