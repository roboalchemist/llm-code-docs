# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/increase-the-pentaho-server-memory-limit/increase-pentaho-server-memory-limit-for-installations-on-linux.md

# Increase Pentaho Server memory limit for installations on Linux

If you used the Pentaho Installation Wizard to install PDI on your Linux machine, you can increase memory limits by editing a variable in one of the Pentaho-supplied scripts. If you did not use the installation wizard, see [Increase Pentaho Server memory limit for custom installations on Windows or Linux](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/increase-the-pentaho-server-memory-limit/increase-pentaho-server-memory-limit-for-custom-installations-on-windows-or-linux).

1. Go to `/pentaho/server/pentaho-server/tomcat/bin/` directory and run the `./shutdown.sh` command to stop the appropriate server.
2. Change the directory to `pentaho-server/tomcat/scripts`.
3. Edit the `ctl.sh` file.
4. Locate the line under `start tomcat`, which looks like this:

   ```java
   export JAVA OPTS="-Dpentaho.installed.licenses.file=/opt/pentaho/.installedLicenses.xml -Xms128m Xmx768m -XX-MaxPermSize=256m -Dsun.rmi.dyc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000"
   ```
5. Set the memory to a minimum of `4096 M` and a maximum of `6144 M`, depending on your computer's memory capabilities.
6. Start the Tomcat server or service.

Your Tomcat server now has increased minimum and maximum memory limits. You can adjust the **JvmMx** parameter to specify a higher maximum limit if you prefer. However, if the Java virtual machine refuses to start with increased limits, then you must add more RAM to your system, stop some memory-intensive services, or reduce the maximum memory limit. This problem occurs when there is not enough contiguous memory available to assign to the JVM.

Make sure to also [increase the Spoon memory limit](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/configure-the-design-tools-and-utilities/pdi-design-tools-and-utilities/increase-the-pdi-client-memory-limit).
