# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/install-a-local-license-server-windows.md

# Install a local license server on Windows

To use Pentaho software, a user must have a valid entitlement in a cloud or local license server that can be verified by the license manager. If you cannot access a cloud license server, but need a license server behind your firewall, you can install a local license server.

The local license server is a command line tool that is used to activate acquired licenses and perform various administrative tasks.

You can install the local license server on the same server or virtual machine that hosts the Pentaho Server because the local license server requires only limited resources. A local license server cannot be deployed in a Docker container.

Verify that the server or virtual machine where you plan to install the local license server meets the following requirements:

* CPU Cores: 2GHz - 2 Cores
* RAM: 4 GB
* Storage: 200 MB
* Set JAVA\_HOME as an environment variable.
* Port 7070 must be open for communication with the local license server.

You must also have Windows administrator privileges for certain tasks.

Perform the following steps to install and activate the local license server on the Windows operating system:

1. Download the local license server file from the [Support Portal](https://support.pentaho.com/hc/en-us).
   1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
   2. In the Pentaho card, click **Download**.

      The Downloads page opens.
   3. In the **10.x** list, click **Pentaho 10.2 GA Release**.
   4. Scroll to the bottom of the Pentaho 10.2 GA Release page.
   5. In the file component section, navigate to the `Utilities and Tools/Local License Server` folder.
   6. Download one of the following local license server files for the version of Pentaho that you have installed:
      * `enterprise-local-license-server-10.2.0.0-<*build\_version*>.zip`
      * `enterprise-local-license-server-10.2.0.3-<*build\_version*>-windows-<*jdk\_version*>.zip`
2. Unzip the local license server file in the folder where you want to install the local license server. For example, you can unzip the file in the following folder: `<*installation\_path*>\enterprise-local-license-server-<*pentaho\_version*>-<*build\_version*>`
3. Navigate to the folder where you unzipped the local license server file.
4. To install the license server as a service, navigate to the `<*installation\_path*>\enterprise-local-license-server\server` folder and run the following command:

   ```
   flexnetls.bat -install
   ```
5. Start the local license server by running the following command:

   ```
   flexnetls.bat -start
   ```
6. To change the username and password after deploying the server, navigate to the `<*installation\_path*>\enterprise-local-license-server\enterprise` folder and run the following command:

   ```
   flexnetlsadmin -server http://<*server\_ip\_address*>:7070/api/1.0/instances/~ -authorize admin <*old\_password*> -users -edit admin <*new\_password*>
   ```

   **Note:**

   The default admin user account information is included in the file `producer-settings.xml`, which is located in the `<*installation\_path*>\enterprise-local-license-server\server` folder:

   * Default username: `admin`
   * Default password: `Password!01`\
     For more information, see `FNE_LicenseServerAdminGuide.pdf` in the `/enterprise-local-license-server/documentation` folder.
7. Perform the following steps to verify system and server status:
   1. Verify the status of the license server using the following command:

      ```
      flexnetls.bat -status
      ```

      If the server is running, it reports the status `Service running`.
   2. Open the Windows Services application by running the command `services.msc` at the Windows command line and verify that the service `FlexNet License Server - <*admin\_name*>` has started.
8. After verifying the system and server status, navigate to the folder where the `flexnetlsadmin.bat` file is located using the following command:

   ```
   cd \<*destination\_folder*>\enterprise-local-license-server\enterprise
   ```
9. Using the following command, activate and populate the pool of licenses on the server with the activation ID emailed to you by Hitachi Vantara:

   ```
   flexnetlsadmin.bat -authorize <*admin\_name*> <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -activate -id <*activation\_id*> -count <*no\_of\_entitlements\_you\_want\_to\_activate*>
   ```

   Where `<no_of_entitlements_you_want_to_activate>` is an integer value equal to or less than the purchased quantity emailed to you by Hitachi Vantara.

Use the following commands to verify the status of the server and which licenses have been activated:

* **Server status command**

  ```
  flexnetlsadmin.bat -authorize admin <*password*> -server <*licenseServer\_baseURL*> -status
  ```
* **Activated licenses command**

  ```
  flexnetlsadmin.bat -authorize admin <*password*> -server <*licenseServer\_baseURL*> -licenses -verbose
  ```

For instructions on installing a license, see [Install licenses using PUC](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Install/Pentaho%20installation/Pentaho%20Installation%20\(overview%20cp\)/Acquire%20and%20install%20enterprise%20licenses/Install%20licenses%20using%20PUC=GUID-BBFF7838-ED4A-4252-803F-A90041648CA8=5=en=.md) or [Install licenses using PUC](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-licenses-using-puc).
