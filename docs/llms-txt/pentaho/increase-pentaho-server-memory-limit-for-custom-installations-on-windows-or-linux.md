# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/increase-the-pentaho-server-memory-limit/increase-pentaho-server-memory-limit-for-custom-installations-on-windows-or-linux.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/increase-pentaho-server-memory-limit-for-custom-installations-on-windows-or-linux.md

# Increase Pentaho Server memory limit for custom installations on Windows or Linux

If you used a custom method to install PDI on a Windows or Linux machine, consider increasing the PDI's memory limit so that the Pentaho Server and the PDI client (also known as Spoon) can perform memory-intensive tasks, like sorting, grouping large datasets, or running complex transformations and jobs.

You must increase the memory limit for both the Pentaho Server and the PDI client. If you do not increase the memory limit, PDI uses the default memory settings in the PDI startup scripts.

For instructions on increasing memory limits by editing the Tomcat startup script, see the topic [Configure and start the Pentaho Server after manual installation](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/configure-and-start-the-pentaho-server-after-manual-installation).

For instructions on increasing the memory limit in PDI client, see the topic [Modify the PDI client startup script](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/broken-reference).
