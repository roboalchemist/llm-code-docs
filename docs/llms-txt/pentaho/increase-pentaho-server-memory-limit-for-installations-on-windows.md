# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/increase-the-pentaho-server-memory-limit/increase-pentaho-server-memory-limit-for-installations-on-windows.md

# Increase Pentaho Server memory limit for installations on Windows

If you used the Pentaho Installation Wizard to install the Pentaho Server on a Windows machine, you can increase the server's memory limits by editing the Java memory settings for Tomcat. Tomcat is the web application server that the Pentaho Server runs on, and is installed by the Pentaho Installation Wizard. If you did not use the installation wizard or you are not running PDI on a Windows machine, refer to the appropriate section below.

1. Stop the Pentaho Server if it is running.
2. Type `services.msc` into the **Windows Search Box**.
3. Find the Pentaho Server name and open it so you can find the **service name**.

   The**service name** should appear at the top of the first tab (**General**). It will be **pentahoserver**.
4. Go into the bin file (`C:\pentaho\server\pentaho-server\tomcat\bin\`) and rename the `tomcat8w.exe` file to match the **service name** (`pentahoserverw.exe`).

   This will ensure that the server starts with the software.
5. After you have renamed the file, open it by double-clicking on it.

   This will not open the file, it will allow you to edit it. You may need to right-click and select **Run as Administrator**. This depends on your user permission settings.

   The **Properties Window** will open.
6. Select the **Java** tab.
7. Set the memory setting to a minimum of `4096 M` and a maximum of `6144 M`, depending on your computer's memory capabilities.
8. [Start the Tomcat server or service](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration).

Your Tomcat server now has increased minimum and maximum memory limits. You can adjust the **JvmMx** parameter to a higher number if you prefer. However, if the Java virtual machine refuses to start with increased limits, then you will have to add more RAM to your system, stop some memory-intensive services, or reduce the maximum memory limit. This problem occurs when there is not enough contiguous memory available to assign to the JVM.

Make sure to also [increase the Spoon memory limit](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/pdi-design-tools-and-utilities/increase-the-pdi-client-memory-limit).
