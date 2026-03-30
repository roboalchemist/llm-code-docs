# Source: https://docs.curator.interworks.com/server_management/system_administration/filesystem_permissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filesystem Permissions

> Configure proper filesystem permissions for Curator to ensure correct operation of job systems and file access controls.

Curator needs full access to its filesystem to run correctly.

Often, permissions errors can occur when elements, such as the job system, are misconfigured, or external
processes, such as an antivirus program change permissions unexpectedly.

Use the processes below to correct errant file permissions.

***Linux:***

1. Determine the user running Curator. This can be found on the Settings->Curator->Status page. On most
   systems, this will be either "apache" or "www-data" (Ubuntu).
2. SSH into the webserver that is running Curator.
3. In the terminal, run a "chown" command for the user you found in Step 1.
   Here are some examples:

   **RHEL, Amazon Linux AMI 1/2, CentOS:**

   ```Linux  theme={null}
   sudo chown -Rf apache:apache /var/www/html;
   ```

   **Ubuntu:**

   ```Ubuntu  theme={null}
   sudo chown -Rf www-data:www-data /var/www/html;
   ```

***Windows:***

1. Find where Curator is installed on your system. Often, this is in *C:\InterWorks\Curator*.

2. Within this directory, look for a folder named "htdocs" or "wwwdata".

   *Note: If your system has an "htdocs" folder, your Curator installation is running Apache. If your system
   has a "wwwdata" folder, your Curator installation is running a legacy IIS install.*

3. Right click on the "htdocs" or "wwwdata" folder and select "Properties".

4. On the folder's "Properties" page, **deselect** the "Read-only" attribute and hit "Apply".

5. After this process has completed, select the "Security" tab.

6. On the Security tab, click "Advanced".

7. If your folder is "htdocs" make sure "SYSTEM" is the folder's owner. If your folder is "wwwdata", IUSR
   should own the folder.

8. Reselect the correct user as the owner. (Note: do this again, even if it looks correct.)

9. Check the box labeled "Replace owner on sub-containers and objects".

10. Check the box labeled "Replace all child object permission entries."

11. Hit "Apply"

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/server_management/system_administration/permissions_fix.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=b04f5c3c0bb90888e7ca84fea21d4f2e" alt="Windows: Permission Fix" data-og-width="769" width="769" data-og-height="525" height="525" data-path="assets/images/server_management/system_administration/permissions_fix.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/server_management/system_administration/permissions_fix.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=3f9edf202fd0c411d547435944f1476e 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/server_management/system_administration/permissions_fix.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=15faf36d206cb2ebeb48a43946581866 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/server_management/system_administration/permissions_fix.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=0ff518f5c2e7bfad08582d1cc50911f1 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/server_management/system_administration/permissions_fix.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6e8a49fc9bc6c2905cc96c57dfaf4ec5 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/server_management/system_administration/permissions_fix.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=adb99666ebc74df1274133ba8ff1b126 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/server_management/system_administration/permissions_fix.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6c0e7f949fd368c6ab991e4b613cce7c 2500w" />

## Automated Permissions Reset for Windows

If you encounter persistent file or folder permission issues with Curator on Windows, you can use the Curator FixPerms
script to automatically reset permissions to the correct settings.

### Usage Instructions

1. Download the FixPerms script from the link: [Curator\_FixPerms.exe](https://api.curator.interworks.com/Curator_FixPerms.exe)

2. Right-click on Curator\_FixPerms.exe and select Run as Administrator.

3. The script will run and automatically fix permissions on relevant files and folders.

*Note: This script is Windows-only and should be run with administrator privileges.*
