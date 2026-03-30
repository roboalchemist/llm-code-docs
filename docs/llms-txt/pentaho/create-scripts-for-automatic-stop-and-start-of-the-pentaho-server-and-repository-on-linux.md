# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration/starting-and-stopping-the-pentaho-server-on-linux/create-scripts-for-automatic-stop-and-start-of-the-pentaho-server-and-repository-on-linux.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/create-scripts-for-automatic-stop-and-start-of-the-pentaho-server-and-repository-on-linux.md

# Create scripts for automatic stop and start of the Pentaho server and repository on Linux

If you used the manual installation to install Pentaho on Linux, you must create scripts for automatic start on boot and stop at shutdown for the Pentaho Server and Pentaho Repository.

You must have root permissions.

Complete the following procedure to create scripts for automatic start on boot and stop at shutdown:

1. Navigate to `/etc/init.d/` and create a file named `pentaho`.
2. Open the `pentaho` file and enter the following content:

   ```xml
   #!/bin/sh
   ### BEGIN INIT INFO
   # Provides: start-pentaho stop-pentaho
   # Required-Start: networking postgresql
   # Required-Stop: postgresql
   # Default-Start: 2 3 4 5
   # Default-Stop: 0 1 6
   # Description: Pentaho Server
   ### END INIT INFO

   case "$1" in
   "start")
   su - pentaho -c "/home/pentaho/pentaho/server/pentaho-server/start-pentaho.sh"
   ;;
   "stop")
   su - pentaho -c "/home/pentaho/pentaho/server/pentaho-server/stop-pentaho.sh"
   ;;
   *)
   echo "Usage: $0 { start | stop }"
   ;;
   esac
   exit 0
   ```
3. (Optional): Update the script for the following situations:
   * If you are not using Red Hat Enterprise Linux, modify the details of the script to work with the operating system, shells, and init systems that you are using. The operating system must be a distribution of either Linux or another Unix-like operating system. The script was tested only on Red Hat Enterprise Linux.
   * If you are using an account other than the `pentaho` local user account to start services, replace `pentaho` with your account name.
   * If you are using a MySQL or Oracle repository instead of the PostgreSQL repository, replace `postgresql` with either `mysql` or `oracle`.
   * If the solution repository is running on the same machine as the server, change `postgresql` to the name of the `init` script for your database.
   * If the solution repository is running on a remote computer, remove `postgresql` entirely and adjust the paths to the Pentaho Server scripts to match your situation.
4. Save and close the `pentaho` file.
5. Navigate to the `/home/pentaho/pentaho/server/pentaho-server` folder and open the `start-pentaho.sh` file in a text editor.
6. In the `start-pentaho.sh` file, change the last `if` statement to match the following example:

   ```xml
   if [ "$?" = 0 ]; then
     cd "$DIR/tomcat/bin"
     export CATALINA_OPTS="-Xms4096m -Xmx6144m -XX:MaxPermSize=256m -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000"
     env JAVA_HOME=$_PENTAHO_JAVA_HOME sh ./startup.sh
   fi
   ```
7. Save and close the `start-pentaho.sh` file.
8. Make the init script executable by running the following command:

   ```xml
   chmod +x /etc/init.d/pentaho
   ```
9. Add the init script to the standard run levels by using the `update-rc.d` command, so that it runs when the system starts, and stops when the system is shut down or rebooted.

   **Note:** If you are not using an operating system distribution that is based on Debian, the following `update-rc.d` command might not exist on your computer. If that is the case, consult the documentation for the distribution you are using or contact the distribution's support department to determine how to add init scripts to the default run levels. For example, you might use the following command:

   ```xml
   update-rc.d pentaho defaults
   ```
