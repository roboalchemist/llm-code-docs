# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/monitoring-system-performance/third-party-monitoring-with-snmp.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/third-party-monitoring-with-snmp.md

# Third-party monitoring with SNMP

You can use the Simple Network Management Protocol (SNMP) plugin to integrate third-party tools for monitoring Data Integration (DI) events.

The information received through SNMP will help you figure out the run-time for your transformations or jobs and identify unusually long-running events impacting network performance. These SNMP events can be directly tied to a particular point in time within the execution, such as the moment a transformation started, or a Kettle step finished execution. These events can be used in a broader scope, such as a successful database connection or a Carte server initialization.

The SNMP plugin works by leveraging existing extension points within the Kettle ecosystem to generate events. These events are then converted into SNMP traps, such as unsolicited or asynchronous messages, that are sent along from an SNMP agent. From there, the events are forwarded to the SNMP manager, which is passively listening for such messages.

## Before you begin

To configure a third-party SNMP monitoring tool to receive trap events from the server, you must first download the `pentaho-monitoring-plugin-mib-assembly-10.2.0.0-<build number>.zip` file from the [Support Portal](https://support.pentaho.com/hc/en-us). The ZIP file contains a MIB file that you must upload to the monitoring tool.

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
2. In the Pentaho card, click **Download**.

   The Downloads page opens.
3. In the **10.x** list, click **Pentaho 10.2 GA Release**.
4. Scroll to the bottom of the Pentaho 10.2 GA Release page.
5. In the file component section, navigate to the `Client Tools/PDI(Spoon)/Plugins` folder.
6. Download the `pentaho-monitoring-plugin-mib-assembly-10.2.0.0-<build number>.zip` file to a temporary directory.
7. In the temporary directory, unpack the `pentaho-monitoring-plugin-mib-assembly-10.2.0.0-<build number>.zip` file.

   The unpacked file contains the `PENTAHO-MIB-V2C.mib` file.

Download and install a third-party SNMP monitoring tool, such as [Nagios](https://www.nagios.org/), and then configure the tool to receive trap events from the server by using the IP addresses of your Data Integration and monitoring servers.

## Send traps through a centralized monitoring server

One option for setting up SNMP monitoring on your network is to use one of your existing Pentaho Server as a JMS monitoring server to handle the trap events it receives from a queue. This server then forwards those events available through SNMP to whichever third-party monitoring tool you have installed.

![Diagram shows the flow of three JMS events, first to a monitoring server, and then to a third party enterprise monitoring tool](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-d59e5ec9a56264ff74899818802d83c54e7877a5%2FSNMP_op1.jpg?alt=media)

### Step 1: Configure a Pentaho Server to send SNMP trap events to a Pentaho monitoring server

Configure a Pentaho server to send SNMP trap events to a designated Pentaho JMS monitoring server so that the JMS monitoring server can send those events to a third-party monitoring tool. A designated Pentaho JMS monitoring server receives SNMP trap events from multiple Pentaho servers in an environment.

For information about setting up specific types of events to monitor, see [Configuring the type of events to be monitored](#configuring-the-type-of-events-to-be-monitored).

You must know the IP address of the designated Pentaho JMS monitoring server.

If the Pentaho server and the designated Pentaho JMS monitoring server are on different machines with different IP addresses, verify that the servers are able to establish communication by pinging.

1. Stop the Pentaho server.
2. On the Pentaho server that you want to configure to send SNMP trap events, navigate to the `pentaho-solutions/system/karaf/system/pentaho/pentaho-osgi-config/10.2.0.0-<build number>` directory.
3. Open the `pentaho-osgi-config-10.2.0.0-<build number>snmp.cfg` file in a text editor.
4. Update the **fromHost** property by entering the IP address of the Pentaho server that you are configuring.
5. Update the **toHost** property by entering the IP address of the designated Pentaho JMS monitoring server.
6. Update the port number to match the Pentaho server SNMP port number.

   **Note:** The default SNMP port number is 162.
7. Save and close the `pentaho-osgi-config-10.2.0.0-<build number>-snmp.cfg` file.
8. Navigate to the `pentaho-solutions/system/karaf/etc/` directory.
9. Open the `org.apache.karaf.features.cfg` file in a text editor.
10. Update the **featuresBoot** property by adding the following values:

    ```
    pentaho-brokering-jms,\
    pentaho-monitoring-to-snmp,\
    ```
11. Save and close the `org.apache.karaf.features.cfg` file.
12. (Optional) In the `pentaho-server/pentaho-solutions/system/karaf/etc/` directory, if the `pentaho.snmp.cfg` file is present, delete it.

    **Note:** Anytime you make changes to the `pentaho-osgi-config-10.2.0.0-<build number>-snmp.cfg`file, you must delete the `pentaho.snmp.cfg` file so that the system can generate a new `pentaho.snmp.cfg` file with your changes when the server starts.
13. Start the Pentaho Server.

Kettle jobs and transformations that are executed on the Pentaho Server send SNMP trap events to the designated Pentaho JMS monitoring server.

### Step 2: Configure the monitoring tool to recieve trap events

The Pentaho Server is already configured by default to handle messages. A management information database (MIB) is used for managing entities in a communications network. The structure is hierarchical with each entry assigned an object identifier (OID).

**Note:** We are using Nagios as an example in this section, but if you are using a different tool, these processes will be different.

#### Upload the MIB file to a monitoring tool

Upload the `PENTAHO-MIB-V2C.mib` file to a third-party SNMP monitoring tool so that you can convert the MIB file to a configuration file.

1. Access the third-party SNMP tool web interface.
2. Locate an option for managing MIBs.
3. Navigate to the temporary directory where you unpacked the `pentaho-monitoring-plugin-mib-assembly-10.2.0.0-<build number>.zip` in [Before you begin](#before-you-begin).

   The directory contains the `PENTAHO-MIB-V2C.mib` file.
4. Upload the `PENTAHO-MIB-V2C.mib` file to the monitoring tool.

#### Convert the MIB file to a configuration file

1. Access the monitoring server through SSH protocol with the root user, for example:

   ```
   ssh root@10.100.9.174
   ```
2. After successfully logging in, find the directory containing your uploaded MIB file, such as: `/usr/share/snmp/mibs/`
3. Run the `snmpttconvertmib` command, stating the path to the uploaded file, and the path for the compiled output file:

   ```
   snmpttconvertmib
   --in=<PATH_TO_UPLOADED_MIB_FILE>
   --out=<PATH_TO_COMPILED_OUTPUT_FILE>--
   exec='/usr/local/bin/snmptraphandling.py "$r" "SNMP Traps" "$s" "$@" "$-*"'
   ```

In this example, we have compiled a configuration file, which we called `pentaho.di.conf`, based on the previously uploaded Pentaho MIB file:

`snmpttconvertmib --in=/usr/share/snmp/mibs/PENTAHO-MIB-V2C.mib --out=/etc/snmp/pentaho.di.conf --exec='/usr/local/bin/snmptraphandling.py "$r" "SNMP Traps" "$s" "$@" "$-*"`

#### Add the newly generated configuration file to the SNMP initialization file

Follow these steps to add the `.conf` file to the `snmpt.ini` file:

1. Open and edit the `file /etc/snmp/snmptt.ini` using a text editor.
2. Locate the `[TrapFiles]` section; it should be at the bottom of the file.
3. Place the entry for your newly created `config` file after the main one but before the END declaration.

   For example, if you use a default `snmptt.ini` file, it should look something like this:

   ```
   [TrapFiles] snmptt_conf_files = <<END
   /etc/snmp/snmptt.conf
   /etc/snmp/pentaho.di.conf END
   ```
4. Save and close the file.
5. Restart the monitoring server and the snmpttservice:

   ```
   /etc/rc.d/init.d/nagios stop 
   /etc/init.d/snmptt stop (wait ~5 seconds)
   /etc/init.d/snmptt start
   /etc/rc.d/init.d/nagios start
   ```

## Send traps from PDI tools to monitoring tool

Instead of sending traps through a centralized monitoring server first, you can set up your SNMP system to have the trap events sent directly from PDI client tools, such as Pan, Kitchen, or the PDI client. A couple of different ways are available to set up the monitoring application through these tools.

![Diagram shows three SNMP events flowing directly into a third party enterprise monitoring tool](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-8b628ab120ffcfdb1f964ecd0af0c92bce36ee92%2FSNMP_op2b.jpg?alt=media)

Follow one of these options to configure your SNMP environment to run through the PDI client tools.

### From all PDI client tools

Follow this option to configure your SNMP environment to run through the PDI client tools:

1. Locate the below directory and open the `org.pentaho.features.cfg` file with any text editor.

   ```
   data-integration/system/karaf/system/pentaho/pentaho-osgi-config/6.0.0
   ```
2. Add `pentaho-monitoring-to-snmp` as a feature at the end of the `featuresBoot` list.
3. If your SNMP port is something other than the default (port 162), change it in this file to match your port.
4. Save and close the file.

### From a specific PDI client tool such as Carte

Follow this option to configure your SNMP environment to run through a specific PDI client tool, such as Carte:

1. Find the `org.pentaho.features.cfg` file in that client's `etc` folder.
2. Add `pentaho-monitoring-to-snmp` to the `runtimeFeatures` list.

   By default, everything BUT the PDI client features are disabled, so you will have to uncomment the `runtimeFeatures` for the other tools.
3. If your SNMP port is something other than the default (port 162), you will need to change it in this file to match your port.
4. Save and close the file.

## Configuring the type of events to be monitored

The Pentaho Server will monitor by default all possible event types occurring when executing a kettle job or transformation, but you can also specify the type of events you want to monitor by removing items from the list. These steps describe how to specify events.

1. Locate the directory: `/pentaho-server/pentaho-solutions/system/karaf/system/pentaho-osgi-config-6.0.0-pdi-monitoring`
2. Open and edit the `monitoring.properties` file as needed.
3. Locate the property for **extension.point.plugins.enabled**, which holds a comma-separated list of event types for which SNMP trap events will be sent to the monitoring server.
   1. Immediately above that property, a comment section lists all possible event types, as well as a brief description for each event type.
   2. Edit that list, leaving only the items you would like to use as SNMP trap events.
4. Save the file and restart the Pentaho Server.

## Available extension points

Here is a list of the extension points that are used for SNMP monitoring of the Pentaho Server. These events are run by default, but if you want fewer events to run, just remove items from this list and save the file.

| Extension Points                   | Description                                                                            |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| **TransformationPrepareExecution** | A transformation to prepare execution                                                  |
| **TransformationStart**            | A transformation has started                                                           |
| **TransformationHeartbeat**        | A signal sent at regular intervals to indicate that the transformation is still active |
| **TransformationFinish**           | A transformation finishes                                                              |
| **JobStart**                       | A job starts                                                                           |
| **JobHeartbeat**                   | A signal sent at regular intervals to indicate that the job is still active            |
| **JobFinish**                      | A job finishes                                                                         |
| **JobBeforeJobEntryExecution**     | Before a job entry executes                                                            |
| **JobAfterJobEntryExecution**      | After a job entry executes                                                             |
| **DatabaseConnected**              | After a successful connection to a database                                            |
| **DatabaseDisconnected**           | After a successful disconnection to a database                                         |
| **CarteStartup**                   | Right after the Carte webserver has started                                            |
| **CarteShutdown**                  | Right before the Carte webserver shuts down                                            |
