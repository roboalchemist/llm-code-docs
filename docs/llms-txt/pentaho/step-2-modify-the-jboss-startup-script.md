# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-jboss-connections-and-web-app-servers/prepare-jboss-web-application-servers/step-5-configure-pentaho-settings-for-jboss/add-jboss-logging/configure-and-start-the-pentaho-server-after-manual-installation/configure-the-pentaho-server-for-linux/step-2-modify-the-jboss-startup-script.md

# Step 2: Modify the JBoss startup script

The JBoss startup script must be modified to include the **JAVA\_OPTS** variable.

**JAVA\_OPTS** indicates the amount of memory to allocate. It also indicates where Pentaho licenses are installed. Specific instructions on how to modify the startup script depend on your operating system.

Perform the following steps to modify the JBoss startup script:​​​​​​

1. Make sure the JBoss web application server is not running. Open a Terminal window and type `ps -A` at the prompt.

   If the server is running, stop it.
2. Use a text editor to open the `standalone.conf` file, which is in the `bin` subdirectory of your JBoss home directory.
3. Modify the **Xms** memory settings in the **JAVA\_OPTS** line to be at least 4096 MB.

   If you have the resources and are concerned with performance, change the **Xmx** value to at least 6144 MB.
4. Add the following options to the **JAVA\_OPTS** line:

   ```
   -Djava.awt.headless=true -Djava.io.tmpdir=/tmp/ -Dpentaho.installed.licenses.file=$PENTAHO_INSTALLED_LICENSE_PATH
   ```
5. Specify the option to pass to the Java VM, as shown below.

   ```java
   # Specify options to pass to the Java VM.
       if [ "x$JAVA_OPTS" = "x" ]; then
           JAVA_OPTS="-Xms4096m \
           -Xmx6144m \
           -XX:MaxPermSize=256m \
           -DDI_HOME=$DI_HOME
           -Dsun.rmi.dgc.client.gcInterval=3600000 \
           -Dsun.rmi.dgc.server.gcInterval=3600000 \
           -Djava.awt.headless=true \
           -Djava.io.tmpdir=/tmp/ \
           -Dpentaho.installed.licenses.file=$PENTAHO_INSTALLED_LICENSE_PATH

   ```

   **Note:** You may need to adjust these settings for your environment. For instance, if you do not have a `/tmp/` directory, you may want to change that setting to `/var/tmp/` or some other location.
6. Save and close the file.
7. Locate the `bin` subdirectory in the JBoss home directory and open the `standalone.sh` file with a text editor.
8. Find the section for **# Setup JBOSS\_HOME** and add this after it.

   ```
   INSTALL_HOME==`cd "$DIRNAME/../.."; pwd`
   DI_HOME=$INSTALL_HOME/pentaho-solutions/system/kettle

   ```
9. Save and close the file.
