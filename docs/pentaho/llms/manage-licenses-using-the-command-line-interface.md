# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/manage-the-pentaho-system/manage-pentaho-licenses/manage-licenses-using-the-command-line-interface.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/manage-licenses-using-the-command-line-interface.md

# Manage licenses using the command line interface

You can set the license path environment variable or you can install, update, list, or remove license files.

## Setting the license path environment variable

To ensure that the Pentaho Server uses the same location to store and retrieve your Pentaho licenses, you must create a *PENTAHO\_LICENSE\_INFORMATION\_PATH* system environment variable for your Pentaho user account if it does not exist. It does not matter what location you choose; however, the location needs to be available to the user account(s) that run the Pentaho Server.

### Set the license path environment variable on Linux

Perform the following steps to set the environment variable for the license path in Linux.

1. Open the `/etc/environment` file with any text editor.
2. Add this line in a convenient place (changing the path if necessary):

   ```
   export PENTAHO_LICENSE_INFORMATION_PATH=/home/pentaho/.elmLicInfo.plt
   ```

   The license information file is saved in the `/home/user/…/.pentaho` folder.
3. Log out and log back into the operating system for the change to take effect.
4. Verify that the variable is properly set using the following command.

   ```
   env | grep PENTAHO_LICENSE_INFORMATION_PATH
   ```

The *PENTAHO\_LICENSE\_INFORMATION\_PATH* variable is now set.

### Set the license path environment variable on Windows

Perform the following steps to set the environment variable for the license path in Windows.

Move the installed license `.elmLicInfo.plt` file from where it was installed (`C:\Users\<user>\.pentaho`) to `C:\Windows\ServiceProfiles\LocalService\.pentaho` or to the location where you are running the Windows service.

1. Under Windows settings, locate and open the Windows system environment variables file for editing.
2. In the System Variable section, click **New**.

   A dialog box will ask for a variable name and value.
3. Type `PENTAHO_LICENSE_INFORMATION_PATH` into the **name** field, and specify the directory where you intend to install the licenses. Type `.elmLicInfo.plt` in the **value** field, then click **OK**.

   ```
   C:/pentaho/.elmLicInfo.plt
   ```

   The license information file is saved in the `/home/user/…/.pentaho` folder.
4. In the parent window, click **Apply Changes**.
5. Restart your computer for the change to take effect.
6. Verify that the variable is properly set, using the following command at the command prompt:

   ```
   echo %PENTAHO_LICENSE_INFORMATION_PATH%
   ```

The *PENTAHO\_LICENSE\_INFORMATION\_PATH* variable is now set.

If you run Tomcat automatically as a Windows service, you must also configure it to run on the Windows user account where the `.elmLicInfo.plt` file is located.

## Install or update license files from the command line

To install or update license files, follow the steps below.

1. Navigate to the `/license-installer/` directory where the Pentaho PDI tool is installed (the `license-installer` subfolder).
2. Run the license installation script as follows to see examples of how to use it:
   * Linux:

     ```
     install_license.sh --help
     ```
   * MacOS:

     ```
     install_license.sh --help
     ```
   * Windows:

     ```
     install_license.bat --help
     ```
