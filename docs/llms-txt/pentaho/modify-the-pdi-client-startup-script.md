# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/pdi-design-tools-and-utilities/increase-the-pdi-client-memory-limit/modify-the-pdi-client-startup-script.md

# Modify the PDI client startup script

1. Exit from the PDI client if it is currently running.
2. Open the PDI client startup script with a text editor. The name of startup script depends on your operating system.
   * Windows Name and Location of Startup Script: `pentaho/design-tools/data-integration/Spoon.bat`
   * Linux Name and Location of Startup Script: `pentaho/design-tools/data-integration/Spoon.sh`
3. Modify the -Xmx value so that it specifies a larger upper memory limit.

   In this example, 2g (two gigabytes) of heap space has been allocated.

   ```
   PENTAHO_DI_JAVA_OPTIONS="-Xmx2g -XX:MaxPermSize=256m"
   ```
4. Save and close the startup file.
5. Start the PDI client and ensure that there are no memory-related errors.

   If you see an error, repeat these steps to increase the memory again.

PDI client now has higher memory limits.

You need to [increase the Pentaho Server memory limit](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/increase-the-pentaho-server-memory-limit) as well.
