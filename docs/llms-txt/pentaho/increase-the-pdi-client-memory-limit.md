# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/pdi-design-tools-and-utilities/increase-the-pdi-client-memory-limit.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/pdi-design-tools-and-utilities/increase-the-pdi-client-memory-limit.md

# Increase the PDI client memory limit

As a best practice, increase PDI's memory limit so the Pentaho Server and the PDI client (Spoon) can perform memory-intensive tasks, process or sort large datasets and run complex transformations and jobs. You will need to increase the memory limit for both the Pentaho Server and the PDI client. If you choose not to increase the memory limit, PDI uses the default memory settings that are defined in your startup scripts.

**Note:** Instead of modifying the PDI client startup script, you can also set the environment variable *PENTAHO\_DI\_JAVA\_OPTIONS* equal to *-Xmx2g -XX:MaxPermSize=256m* on your client.

#### Modify the PDI client startup script

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
