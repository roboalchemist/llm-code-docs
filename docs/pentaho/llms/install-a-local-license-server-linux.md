# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/install-a-local-license-server-linux.md

# Install a local license server on Linux

To use Pentaho software, a user must have a valid entitlement in a cloud or local license server that can be verified by the license manager. If you cannot access a cloud license server, but need a license server behind your firewall, you can install a local license server.

The local license server is a command line tool that is used to activate acquired licenses and perform various administrative tasks.

You can install the local license server on the same server or virtual machine that hosts the Pentaho Server because the local license server requires only limited resources. A local license server cannot be deployed in a Docker container.

* Verify that the server or virtual machine where you plan to install the local license server meets the following requirements:
  * CPU Cores: 2GHz - 2 Cores
  * RAM: 4 GB
  * Storage: 200 MB
  * JAVA\_HOME must be set as an environment variable.
  * Port 7070 must be open for communication with the local license server.
* Verify that you have sudo privileges, which are needed for certain tasks.
* If you are installing a local license server on Redhat Linux with FIPS mode enabled, configure Java as described in the following articles:
  * [Configuring Red Hat build of OpenJDK 11 on RHEL with FIPS](https://docs.redhat.com/en/documentation/red_hat_build_of_openjdk/11/html-single/configuring_red_hat_build_of_openjdk_11_on_rhel_with_fips/index)
  * [Configuring Red Hat build of OpenJDK 17 on RHEL with FIPS](https://docs.redhat.com/en/documentation/red_hat_build_of_openjdk/17/html-single/configuring_red_hat_build_of_openjdk_17_on_rhel_with_fips/index#proc-providing-feedback-on-redhat-documentation)

Perform the following steps to install and activate the local license server on a Linux operating system:

1. Download the local license server file from the [Support Portal](https://support.pentaho.com/hc/en-us).
   1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
   2. In the Pentaho card, click **Download**.

      The Downloads page opens.
   3. In the **10.x** list, click **Pentaho 10.2 GA Release**.
   4. Scroll to the bottom of the Pentaho 10.2 GA Release page.
   5. In the file component section, navigate to the `Utilities and Tools/Local License Server` folder.
   6. Download one of the following local license server files for the version of Pentaho that you have installed:
      * `enterprise-local-license-server-10.2.0.0-<*build\_version*>.tar.gz`
      * `enterprise-local-license-server-10.2.0.3-<*build\_version*>-linux-<*jdk\_version*>.tar.gz`
2. Set the necessary permissions to open the downloaded file using one of the following commands for the version of Pentaho that you have installed:
   * ```
     ```

chmod 777 enterprise-local-license-server-10.2.0.0-<*build\_version*>.tar.gz

````

    -   ```
chmod 777 enterprise-local-license-server-10.2.0.3-<*build\_version*>-linux-<*jdk\_version*>.tar.gz
````

3. Open the download package using one of the following commands for the version of Pentaho that you have installed:
   * ```
     ```

tar -xvzf enterprise-local-license-server-10.2.0.0-<*build\_version*>.tar.gz -C <*destination\_folder*>

````

    -   ```
tar -xvzf enterprise-local-license-server-10.2.0.3-<*build\_version*>-linux-<*jdk\_version*>.tar.gz -C <*destination\_folder*>
````

4. Navigate to the folder where the installation file is located using the following command:

   ```
   cd /<*destination\_folder*>/enterprise-local-license-server/server
   ```
5. Run the license server executable by using one of the following commands:
   * If access to Java's temporary directory is not restricted, run the following command:

     ```
     sudo ./install-systemd.sh
     ```
   * If your admin has restricted access to Java's temporary directory, run the following command to install the license server and create a new temporary directory for Java at the full path that you specify:

     ```
     sudo ./install-systemd.sh --tmpdir=<*full\_path\_to\_temp\_directory*>
     ```
6. If the `Install VMUUID license daemon?` prompt is shown, enter one of the following options as the answer:
   * `y`: If you are installing the license server on a virtual machine, answer yes to allow the license server to use the virtual machine's UUID as a potential hostid because it can be more stable than other hostid types in a virtual environment.
   * `n`: If you are installing the license server on physical hardware, answer no.**Note:** The VMUUID license daemon prompt can appear for Java version 2025.02.0 or newer.
7. Start the local license server using the following command:

   ```
   sudo systemctl start flexnetls-pentaho
   ```
8. After deploying the server, navigate to the folder where the `flexnetlsadmin.sh` file is located using the following command:

   ```
   cd /<*destination\_folder*>/enterprise-local-license-server/enterprise
   ```
9. Change the admin password by running the following command:

   ```
   flexnetlsadmin.sh -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~ > -authorize <*defaultAdminName*> {<*defaultAdminPassword*>|-<*passwordConsoleInput*>} -users -edit admin {<*newAdminPassword*>!|-<*passwordConsoleInput*>}
   ```

   Default admin user account information is included in the `producer-settings.xml` file:

   * Default username: `admin`
   * Default password: `Password!01`\
     For more information, see `FNE_LicenseServerAdminGuide.pdf` in the `/enterprise-local-license-server/documentation` folder.
10. Perform the following steps to verify system and server status:
    1. Verify the `systemd` status to see if the `Flex Net` service is running using the following command:

       ```
       sudo systemctl -l status flexnetls-pentaho
       ```
    2. If the system status verification shows that the`Flex Net` service is running, verify the status of the `Flex Net` server using the following command:

       ```
       ./flexnetlsadmin.sh -authorize admin <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -status
       ```
11. Using the following command, activate and populate the pool of licenses on the server with the activation ID emailed to you by Hitachi Vantara:

    ```
    ./flexnetlsadmin.sh -authorize <*admin\_name*> <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -activate -id <*activation\_id*> -count <no_of_entitlements_you_want_to_activate>
    ```

    Where `<*no\_of\_entitlements\_you\_want\_to\_activate*>` is an integer value equal to or less than the purchased quantity emailed to you by Hitachi Vantara.

    **Note:** If security restrictions prevent your license server from reaching the back office URL, you can use the offline activation method. See [Activate offline entitlements for a local license server](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-and-manage-a-local-license-server/activate-offline-entitlements-for-a-local-license-server).

The local license server is installed and active. You can access and issue commands to the local license server by using a URL like the following example: `http://<*server\_ip\_address*>:7070/api/1.0/instances/~`.

Use the following command to verify which licenses have been activated:

```
./flexnetlsadmin.sh -authorize admin <*password*> -server <http://<*server\_ip\_address*>:7070/api/1.0/instances/~> -licenses -verbose
```

For instructions on installing a license, see [Install licenses using PUC](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Install/Pentaho%20installation/Pentaho%20Installation%20\(overview%20cp\)/Acquire%20and%20install%20enterprise%20licenses/Install%20licenses%20using%20PUC=GUID-BBFF7838-ED4A-4252-803F-A90041648CA8=5=en=.md) or [Install licenses using PUC](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses/install-licenses-using-puc).
