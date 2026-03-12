# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss/add-jboss-logging/configure-and-start-the-pentaho-server-after-manual-installation/configure-the-pentaho-server-for-linux/step-1-modify-the-tomcat-startup-script.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss/add-jboss-logging/configure-and-start-the-pentaho-server-after-manual-installation/configure-the-pentaho-server-for-windows/step-1-modify-the-tomcat-startup-script.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/configure-and-start-the-pentaho-server-after-manual-installation/configure-the-pentaho-server-for-linux/step-1-modify-the-tomcat-startup-script.md

# Step 1: Modify the Tomcat startup script

The Tomcat startup script must be modified to include the **CATALINA\_OPTS** variable.

**CATALINA\_OPTS** indicates the amount of memory to allocate. It also indicates where Pentaho licenses are installed.

**Note:** The startup process will fail if an environment variable setting is not valid or is incorrect. When modifying any environment variable in the startup file, make sure its setting is valid and correct.

Perform the following steps to include the **CATALINA\_OPTS** variable:

1. Copy all the JAR files from the `server'/pentaho-server/pentaho-solutions/native-lib/linux/x86_64` folder to the `~/webapps/pentaho/WEB-INF/lib` folder.
2. Add the LIBPATH variable to the Tomcat `startup.sh` file as follows:

   ```
   export LIBPATH=~/native-lib/linux/x86_64
   ```
3. Make sure the Tomcat web application server is not running.
   1. Open a Terminal window.
   2. Type `ps -A` at the prompt.
   3. If the server is running, stop it.
4. Use a text editor to open the startup `.sh` file, which is in the `pentaho/server/pentaho-server/tomcat/bin` directory.
5. Locate the **#Check that target executable exists** line and add this code above it.

   `DI_HOME=<your pentaho directory>/pentaho-solutions/system/kettle`
6. Add the Java option **pentaho.installed.licenses.file to CATALINA\_OPTS**.

   You need to modify the setting of the **CATALINA\_OPTS** variable at the end of the file by adding the Java option. See the following example.

   ```java
   EXPORT CATALINA_OPTS="-Xms4096m -Xmx6144m -Djava.library.path=%LIBPATH% -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000 
   -Dpentaho.installed.licenses.file=$PENTAHO_INSTALLED_LICENSE_PATH -DDI_HOME=$DI_HOME"

   ```
7. Save and close the file.
