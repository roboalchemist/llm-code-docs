# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/change-the-java-vm-memory-limits.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/change-the-java-vm-memory-limits.md

# Change the Java VM memory limits

The Tomcat server has a relatively low memory allotment by default, which can cause out-of-memory errors by the Pentaho Server. If you are running out of memory even though your server has a lot of RAM, you probably need to increase the resources allocated to the JRE instance that runs the Pentaho software you're trying to improve performance on. Adjusting the memory limit is an easy configuration change to make, but the instructions differ depending on the client tool or Web application server you're using. Refer only to the sections below that apply to your situation.

**Note:** If you are running multiple Pentaho programs concurrently, the sum of their JVM maximum memory limits must not exceed the available RAM minus system overhead.

## Archive or manual deployment

To increase the memory limit, perform the following steps:

1. Stop the Tomcat server or service.
2. Because you are modifying your own Tomcat instance and have performed a manual deployment of the Pentaho Server WAR, edit the `~/.bashrc` for the user account that starts the Tomcat service, or whatever configuration file or dialog box that contains global system variables on your Pentaho Server machine. Set or modify the *CATALINA\_OPTS* system variable to include reasonable minimum and maximum memory settings using the -Xms and -Xmx options. Ensure you customize these settings to fit the needs of your system.

   ```
   export CATALINA_OPTS="-Xms4096m -Xmx6144m" 
   ```
3. If you are using a Pentaho-supplied Tomcat instance provided in Pentaho Server archive packages, edit the `start-pentaho` scripts (`.bat` for Windows, and `.sh` for Linux), and modify the *CATALINA\_OPTS* environment variable, adjusting the values of Xms and Xmx in the same manner as the previous step.

   ```
   export CATALINA_OPTS="-XMs4096m -Xmx6144m -XX:MaxPermSize=256m -
                       Dsun.rmi.dgc.client.gcInterval=3600000
                       -Dsun.rmi.dgc.server.gcInterval=3600000"
   ```
4. If you are modifying a Windows service for Tomcat, you must use the `tomcat8.exe` command to reconfigure the service parameters within a command line window. You can access Windows Services by going to the **Windows Start Menu** and typing `services` in the **Search Programs and Files** box.

   ```
   tomcat8 //US//Tomcat8 --JvmMs=4096m --JvmMx=6144m
   ```
5. Start the Tomcat server or service.

Your Tomcat server now has increased minimum and maximum memory limits. You can adjust the `JvmMx` number (this parameter specifies the maximum limit) to a higher number if you prefer. However, if the Java virtual machine refuses to start with increased limits, then you will have to add more RAM to your system, stop some memory-intensive services, or reduce the maximum memory limit to a lower number. This problem occurs when there is not enough contiguous memory available to assign to the JVM, and appears to happen on Windows at lower thresholds than on other operating systems.

## Aggregation Designer

Pentaho Aggregation Designer's startup script uses the default memory settings for your Java environment, which may be insufficient for your work. If you are experiencing an `OutOfMemory` exception, you must increase the amount of heap space available to Aggregation Designer by changing the Java options that set memory allocation. Perform the following steps to increase the amount of heap space:

**Note:** In the examples below, the memory size notations are `m` for megabytes and `g` for gigabytes. You can use whichever is most appropriate for your situation.

1. Exit Aggregation Designer if it is currently running.
2. Edit the `startaggregationdesigner` script and modify your Java command to include an -Xmx line that specifies a large upper memory limit.

   Linux/Solaris shell script:

   ```
   "$_PENTAHO_JAVA" $LICENSEPARAMETER -Xmx2g -jar "$DIR/lib/launcher-1.0.0.jar"

   ```

   Windows batch file:

   ```
   "%_PENTAHO_JAVA%" %LICENSEPARAMETER% -Xmx2g -jar "%~dp0lib\launcher-1.0.0.jar"

   ```
3. Start Aggregation Designer and ensure that there are no memory-related exceptions.

The Java virtual machine instance that Aggregation Designer uses now has access to more heap space, which should solve `OutOfMemory` exceptions and increase performance.

## Pentaho Data Integration

Pentaho Data Integration's startup script uses the default memory settings for your Java environment, which may be insufficient for your work. If you're experiencing an `OutOfMemory` exception, you must increase the amount of heap space available to PDI by changing the Java options that set memory allocation. Perform the following steps to increase the amount of heap space:

1. Exit the PDI client if it is currently running.
2. Edit your PDI client startup script and modify the -Xmx value so that it specifies a large upper memory limit.

   ```
   PENTAHO_DI_JAVA_OPTIONS="-Xmx2g -XX:MaxPermSize=256m"
   ```
3. Start the PDI client and ensure that there are no memory-related exceptions.

The Java virtual machine instance that the Pentaho Server uses now has access to more heap space, which should solve `OutOfMemory` exceptions and increase performance.

## Report Designer

Pentaho Report Designer's startup script uses the default memory settings for your Java environment, which may be insufficient for your work. If you're experiencing an `OutOfMemory` exception, you must increase the amount of heap space available to Report Designer by changing the Java options that set memory allocation. Perform the following steps to increase the amount of heap space:

**Note:** In the examples below, the memory size notations are `m` for megabytes and `g` for gigabytes. You can use whichever is most appropriate for your situation.

1. Exit Report Designer if it is currently running.
2. Edit the `report-designer` script and modify the value of -Xmx to allocate more memory to Report Designer's JVM instance.

   Linux/Solaris shell script:

   ```
   "$_PENTAHO_JAVA" "-Dpentaho.installed.licenses.file=$PENTAHO_INSTALLED_LICENSE_PATH" -XX:MaxPermSize=256m -Xmx2g -jar "$DIR/launcher.jar" $@

   ```

   Windows batch file:

   ```
   set OPT="-XX:MaxPermSize=256m" "-Xmx2g"

   ```
3. Start Report Designer and ensure that there are no memory-related exceptions.

The Java virtual machine instance that Report Designer uses now has access to more heap space, which should solve `OutOfMemory` exceptions and increase performance.

## Weka

Weka uses the memory settings passed to it from the Java command line or the script that invokes it. If you are experiencing an `OutOfMemory` exception, you must increase the amount of heap space available to Weka by changing the Java options that set memory allocation. Perform the following steps to increase the amount of heap space:

**Note:** In the examples below, the memory size notations are `m` for megabytes and `g` for gigabytes. You can use whichever is most appropriate for your situation.

1. Exit Weka if it is currently running.
2. If you are running Weka standalone from the command line, modify your Java command to include an -Xmx line that specifies a large upper memory limit.

   ```
   java -Xmx2g weka.jar
   ```
3. If you are running Weka as part of a script, change your Java invocation so that it includes the above `-Xmx` setting.
4. Start Weka and ensure that there are no memory-related exceptions.

The Java virtual machine instance that Weka uses now has access to more heap space, which should solve `OutOfMemory` exceptions and increase performance.
