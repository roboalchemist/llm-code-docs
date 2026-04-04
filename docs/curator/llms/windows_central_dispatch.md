# Source: https://docs.curator.interworks.com/setup/central_dispatch/windows_central_dispatch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows Central Dispatch

> Configure distributed processing with Central Dispatch on Windows systems

Each section below has steps you can follow, all steps must be followed to set up Central Dispatch accordingly.

## 1. Curator install and folder Creation

1. Install Curator using Apache installer like usual.
2. Ensure the following folders exist, and if not, use a Windows Explorer window to create them
   * `C:\InterWorks\Curator\vhosts`
   * `C:\InterWorks\Curator\archives`

## 2. `curator.conf` file adjustments

1. Move Central Dispatch portal to subfolder of htdocs
   1. Make directory `C:\InterWorks\Curator\htdocs\centraldispatch`
   2. Move all other files and folders in `htdocs` directory to `centraldispatch` directory using Windows Explorer
2. Save SSL/TLS certificates and key files to `C:\InterWorks\Curator\certs` directory (create if it doesn’t exist)
3. Update `curator.conf` Located in `C:\InterWorks\Curator`
   1. Point the default virtualhost’s document root and directory to `C:\InterWorks\Curator\htdocs\centraldispatch`
   2. Use wildcard subdomain for servername and/or serveralias (do not use \* in the path)
   3. Add include statement at the bottom to look for configuration files in `C:\InterWorks\Curator\vhosts` directory:
      1. IncludeOptional `C:\InterWorks\Curator\vhosts\`
   4. Configure it to listen on 443 and point at the certs and key in the certs directory by uncommenting the lines at
      the bottom section.
   5. Add these 2 lines to the 443 VirtualHost (usually under the DocumentRoot)
      1. ErrorLog `${APACHE_LOG_DIR}/centraldispatch_error.log`
      2. CustomLog `${APACHE_LOG_DIR}/centraldispatch_access.log` combined
4. Update the existing Curator cron scheduled task to fix the path to the (now) Central Dispatch portal (i.e.
   `C:\InterWorks\Curator\htdocs\centraldispatch\artisan`).
5. Restart apache using the shortcuts on the desktop. If you receive an error message about access, then right click on
   the `stop.bat` and `start.bat` scripts within `C:\InterWorks\Curator` and run as administrator.  Ensure the portal still
   works as expected.

## 3. Create the Worker Database User

1. Open the `worker_database_user.sql` example script in a text-editor, located in the
   `C:\InterWorks\Curator\htdocs\centraldispatch\plugins\interworks\centraldispatch\workers` directory.

2. Change the username and password as needed before executing.

3. Open a terminal and run the command below to create the new user

   ```bash  theme={null}
   mysql -u root -p -e "source C:\InterWorks\Curator\htdocs\centraldispatch\plugins\interworks\centraldispatch\workers\worker_database_user.sql"
   ```

4. NOTE: You will be prompted to enter a password. Use the root user's password that was created when you installed
   Curator. Refer to the [Windows Installation here](/setup/installation/windows_installation).

## 4. Create script and vhost files

1. Navigate to the `C:\InterWorks\Curator\htdocs\centraldispatch\plugins\interworks\centraldispatch\workers` directory
2. Create a copy of `php_worker.example.php`, rename it to `php_worker.php`, and move it to `C:\InterWorks\Curator`.
3. Create a copy of `vhost.template.example.conf`, rename it to `vhost.template.conf`, and move it to
   `C:\InterWorks\Curator`.
4. You will have created the following files
   * `C:\InterWorks\Curator\php_worker.php`
   * `C:\InterWorks\Curator\vhost.template.conf`

## 5. Worker Script Setup

NOTE: Within PHP, use forward slashes, not backslashes for directory separators.  Outside of PHP, use backslashes.

1. Open `php_worker.php` in a text editor
2. Modify the user section:
   1. For the `DB_ENV_DISPATCHER` set the `user` and `pass` values to the user and password you set using the script in
      the **Create the Worker Database User** section above.
   2. `DB_ENV_INSTANCE` uses the `root` user's details for simplicity. This ensures you can provision with the highest
      access. Alternatively, if you do not want to use the `root` user for this create a separate user and use those details.
3. Modify vhost section:
   1. Uncomment `directory` for "C:/InterWorks/Curator/vhosts" (update path as needed).
   2. Uncomment `template` for `C:/InterWorks/Curator/vhost.template.conf` (update path as needed).
4. Modify worker section:
   1. Uncomment `source_directory` for "C:/InterWorks/Curator/htdocs/centraldispatch" (update path as needed).
   2. Uncomment `archive_directory` for "C:/InterWorks/Curator/archives" (update path as needed).
      1. Modify `$DEFAULT_BACKEND_EMAIL` as needed
      2. Modify `$WINDOWS_INSTALL_DIR` if not using C:/InterWorks/Curator (i.e. if installed to D:\InterWorks\Curator)

## 6. vhost Template Setup

1. Determine the Apache version you're using by running `C:\InterWorks\Curator\libs\Apache24\bin\httpd -v` in a Command
   Prompt window
2. Open `C:\InterWorks\Curator\vhost.template.conf` in a text editor
   1. If using Apache 2.2:
      1. Ensure lines 22-23 **do not** start with a '#', enabling those lines.
      2. Ensure line 25 starts with a '#', disabling that line.
   2. If using Apache 2.4:
      1. Ensure line 25 **does not** start with a '#', enabling that line.
      2. Ensure lines 22-23 start with a '#', disabling those lines.
3. Schedule worker by running the command in the `worker_scheduled_task.bat` example script. Tweak as needed. It
   defaults to 15 minutes.

## 7. Register and Test Dispatcher

1. In the Central Dispatch Curator portal’s backend, register the workers with the dispatcher at **Backend** >
   **Settings** > **Central Dispatch** > **Central Dispatch Settings**. Probably with these settings:
   1. Host URL: localhost
   2. Worker name: localhost (or use something more descriptive)
   3. Install Path: C:/InterWorks/Curator/htdocs/
2. Attempt to deploy a new managed instance at Backend > Central Dispatch > Managed Instances.

## Manual Back Out of Deployment

In case of a failure during a deployment, Central Dispatch is not yet able to automatically back out the deployment to
try again. You can determine the nature of the failure by visiting the Managed Instance record in the backend of the
Central Dispatch portal and scrolling to the bottom of the page. There will be an error field that will show any issues
the worker had during the deployment.

To back out a deployment, it's important to determine which step it failed at so you'll know which of the following steps
you'll need to take to back it out. They are in reverse order of the deployment, so you can skip steps if the deployment
didn't make it that far. When in doubt, just perform all of the steps.

1. Remove scheduled task with the name of this managed instance by opening the Windows Task Scheduler.

2. Remove the vhost record specific to this managed instance in the `C:\InterWorks\Curator\vhosts directory` (adjust drive
   letter as needed).

3. Remove site-specific SSL/TLS keys if the managed instance supplied them. These will be in the
   `C:\InterWorks\Curator\certs directory` (adjust drive letter as needed).

4. Remove the portal code for the managed instance in the `C:\InterWorks\Curator\htdocs directory` (adjust drive letter
   as needed).

5. Drop the database specific to the managed instance by using HeidiSQL and the root database credentials
   (see `C:\InterWorks\Curator\info.txt`). The SQL statement to drop the database would be:

   ```SQL  theme={null}
   DROP DATABASE '<database name>';
   ```

6. Delete the database user specific to the managed instance by using HeidiSQL and the root database credentials
   (see `C:\InterWorks\Curator\info.txt`). The SQL statement to drop the database would be:

   ```SQL  theme={null}
   DROP USER IF EXISTS '<username>'@'localhost';;
   ```
