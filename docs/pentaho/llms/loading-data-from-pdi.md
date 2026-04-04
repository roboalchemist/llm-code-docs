# Source: https://docs.pentaho.com/pdia-data-integration/loading-data-from-pdi.md

# Loading data from PDI

Load data from Pentaho Data Integration (PDI) to external tools.

Use these features to run outside the PDI client, run remotely, expose virtual tables, and capture lineage.

### In this article

* [Run transformations and jobs from the command line](#run-transformations-and-jobs-from-the-command-line)
* [Run and monitor remotely with Carte](#run-and-monitor-remotely-with-carte)
* [Expose transformation output with Pentaho Data Services](#expose-transformation-output-with-pentaho-data-services)
* [Capture lineage with the OpenLineage plugin](#capture-lineage-with-the-openlineage-plugin)

### Run transformations and jobs from the command line

You can use command line tools to execute PDI content outside the PDI client.

Use them in scripts and schedulers, like `cron`.

Use **Pan** to run transformations.

Use **Kitchen** to run jobs.

<details>

<summary>Command-line reference (Pan, Kitchen, ZIP, export, Hadoop)</summary>

#### Startup script options

Pan and Kitchen recognize the startup-script options used by the PDI client.

These options are in `Spoon.bat` (Windows) and `Spoon.sh` (Linux).

To use these options with Pan or Kitchen, add them to your startup script.

**Note:** The default directory for the startup script is `design-tools/data-integration`.

| Option                         | Description                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **FILTER\_GTK\_WARNINGS**      | Suppresses GTK warnings from `spoon.sh` and `kitchen.sh`. Set to `true` to suppress warnings. Leave empty to show warnings.                       |
| **SKIP\_WEBKITGTK\_CHECK**     | Suppresses warnings about missing `libwebkitgtk` when launching the PDI client. Set to `true` to suppress warnings. Leave empty to show warnings. |
| **KETTLE\_HOME**               | Identifies the user's home directory for PDI configuration files. Use it to change the location of files normally in `<user home>/.kettle`.       |
| **KETTLE\_LOG\_SIZE\_LIMIT**   | Limits the log size for transformations and jobs that do not set a log size limit property.                                                       |
| **KETTLE\_JNDI\_ROOT**         | Changes the Simple JNDI path, which contains `jdbc.properties`.                                                                                   |
| **KETTLE\_DIR**                | Directory where the PDI client is installed.                                                                                                      |
| **KETTLE\_REPOSITORY**         | Repository that Kettle connects to at startup.                                                                                                    |
| **LIBPATH**                    | Value passed as the `-Djava.library.path` Java parameter.                                                                                         |
| **PENTAHO\_DI\_JAVA\_OPTIONS** | Additional Java arguments when running Kettle. Use it for settings like memory limits.                                                            |

#### Pan (run transformations)

Pan runs transformations from a PDI repository (database or enterprise) or a local file.

The options are the same for the shell script and batch file.

**Note:** Windows uses the forward slash (`/`) and colon (`:`) syntax. If option values contain spaces, quote the full argument. Example: `"-param:MASTER_HOST=192.168.1.3" "-param:MASTER_PORT=8181"`.

```
pan.sh -option=value arg1 arg2
```

```
pan.bat /option:value arg1 arg2
```

Example:

```
sh pan.sh -rep=initech_pdi_repo -user=pgibbons -pass=lumburgh -trans=TPS_reports_2011
```

```
pan.bat /rep:initech_pdi_repo /user:pgibbons /pass:lumburgh /trans:TPS_reports_2011
```

| Switch        | Purpose                                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| rep           | Enterprise repository name.                                                                                                                          |
| user          | Repository username.                                                                                                                                 |
| pass          | Repository password.                                                                                                                                 |
| trans         | Name of the transformation to run.                                                                                                                   |
| dir           | Repository directory that contains the transformation, including the leading slash.                                                                  |
| file          | Local `.ktr` file path.                                                                                                                              |
| level         | Logging level: Basic, Detailed, Debug, Rowlevel, Error, Nothing.                                                                                     |
| logfile       | Log file path.                                                                                                                                       |
| listdir       | Lists directories in the specified repository.                                                                                                       |
| listtrans     | Lists transformations in the specified repository directory.                                                                                         |
| listrep       | Lists available repositories.                                                                                                                        |
| exprep        | Exports all repository objects to one XML file.                                                                                                      |
| norep         | Prevents Pan from logging into a repository. Useful when environment variables like `KETTLE_REPOSITORY` are set, but you want to run a local `.ktr`. |
| safemode      | Runs in safe mode with extra checking.                                                                                                               |
| version       | Shows version, revision, and build date.                                                                                                             |
| param         | Sets a named parameter in `name=value` format. Example: `-param:Foo=bar`.                                                                            |
| listparam     | Lists information about named parameters in the specified transformation.                                                                            |
| metrics       | Gathers metrics during execution.                                                                                                                    |
| maxloglines   | Maximum number of log lines kept internally. `0` keeps all lines (default).                                                                          |
| maxlogtimeout | Maximum age (minutes) of a log line kept internally. `0` keeps lines indefinitely (default).                                                         |

**Pan status codes**

Pan returns one of these status codes:

| Status code | Definition                                                     |
| ----------- | -------------------------------------------------------------- |
| 0           | Transformation ran without a problem.                          |
| 1           | Errors occurred during processing.                             |
| 2           | Unexpected error during loading or running the transformation. |
| 3           | Unable to prepare and initialize the transformation.           |
| 7           | Transformation could not be loaded from XML or the repository. |
| 8           | Error loading steps or plugins.                                |
| 9           | Command line usage was printed.                                |

#### Kitchen (run jobs)

Kitchen runs jobs from a PDI repository (database or enterprise) or a local file.

The options are the same for the shell script and batch file.

**Note:** Windows uses the forward slash (`/`) and colon (`:`) syntax. If option values contain spaces, quote the full argument. Example: `"-param:MASTER_HOST=192.168.1.3" "-param:MASTER_PORT=8181"`.

```
kitchen.sh -option=value arg1 arg2
```

```
kitchen.bat /option:value arg1 arg2
```

| Switch        | Purpose                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rep           | Enterprise or database repository name.                                                                                                                  |
| user          | Repository username.                                                                                                                                     |
| pass          | Repository password.                                                                                                                                     |
| job           | Name of the job (as it appears in the repository) to run.                                                                                                |
| dir           | Repository directory that contains the job, including the leading slash.                                                                                 |
| file          | Local `.kjb` file path.                                                                                                                                  |
| level         | Logging level: Basic, Detailed, Debug, Rowlevel, Error, Nothing.                                                                                         |
| logfile       | Log file path.                                                                                                                                           |
| listdir       | Lists subdirectories within the specified repository directory.                                                                                          |
| listjob       | Lists jobs in the specified repository directory.                                                                                                        |
| listrep       | Lists available repositories.                                                                                                                            |
| export        | Exports all linked resources of the specified job. Argument is a ZIP filename.                                                                           |
| norep         | Prevents Kitchen from logging into a repository. Useful when environment variables like `KETTLE_REPOSITORY` are set, but you want to run a local `.kjb`. |
| version       | Shows version, revision, and build date.                                                                                                                 |
| param         | Sets a named parameter in `name=value` format. Example: `-param:FOO=bar`.                                                                                |
| listparam     | Lists information about named parameters in the specified job.                                                                                           |
| maxloglines   | Maximum number of log lines kept internally. `0` keeps all lines (default).                                                                              |
| maxlogtimeout | Maximum age (minutes) of a log line kept internally. `0` keeps lines indefinitely (default).                                                             |

Example:

```
sh kitchen.sh -rep=initech_pdi_repo -user=pgibbons -pass=lumburghsux -job=TPS_reports_2011
```

```
kitchen.bat /rep:initech_pdi_repo /user:pgibbons /pass:lumburghsux /job:TPS_reports_2011
```

**Kitchen status codes**

Kitchen returns one of these status codes:

| Status code | Definition                                          |
| ----------- | --------------------------------------------------- |
| 0           | Job ran without a problem.                          |
| 1           | Errors occurred during processing.                  |
| 2           | Unexpected error during loading or running the job. |
| 7           | Job could not be loaded from XML or the repository. |
| 8           | Error loading steps or plugins.                     |
| 9           | Command line usage was printed.                     |

#### Import `.kjb` or `.ktr` files from a ZIP archive

Pan and Kitchen can read PDI content from ZIP files.

Use the `!` switch.

Windows example:

```
Kitchen.bat /file:"zip:file:///C:/Pentaho/PDI Examples/Sandbox/linked_executable_job_and_transform.zip!Hourly_Stats_Job_Unix.kjb"
```

Linux and Solaris example (escape `!`):

```
./kitchen.sh -file:"zip:file:////home/user/pentaho/pdi-ee/my_package/linked_executable_job_and_transform.zip\!Hourly_Stats_Job_Unix.kjb"
```

#### Export repository content from the command line

To export repository objects into XML format using command-line tools, pass named parameters when calling Kitchen or Pan.

Example (Kitchen):

```
call kitchen.bat /file:C:\Pentaho_samples\repository\repository_export.kjb ^
"/param:rep_name=PDI2000" "/param:rep_user=admin" "/param:rep_password=password" ^
"/param:rep_folder=/public/dev" ^
"/param:target_filename=C:\Pentaho_samples\repository\export\dev.xml"
```

| Parameter         | Description         |
| ----------------- | ------------------- |
| `rep_folder`      | Repository folder   |
| `rep_name`        | Repository name     |
| `rep_password`    | Repository password |
| `rep_user`        | Repository username |
| `target_filename` | Target filename     |

**Note:** You can use obfuscated passwords with **Encr**, the command line tool for encrypting strings for storage and use by PDI.

Example batch file that checks for errors:

```bat
@echo off
ECHO This is an example of a batch file calling repository_export.kjb

cd C:\Pentaho\pdi-ee-<version>\data-integration

call kitchen.bat /file:C:\Pentaho_samples\repository\repository_export.kjb "/param:rep_name=PDI2000" ^
"/param:rep_user=admin" "/param:rep_password=password" "/param:rep_folder=/public/dev" ^
"/param:target_filename=C:\Pentaho_samples\repository\export\dev.xml"

if errorlevel 1 goto error
echo Export finished successful.
goto finished

:error
echo ERROR: An error occurred during repository export.
:finished
REM Allow the user to read the message when testing.
pause
```

#### Use Pan and Kitchen with a Hadoop cluster

To use Pan or Kitchen on a Hadoop cluster, configure Pentaho to run transformations and jobs with the PDI client or the Pentaho Server.

You do not need these configurations if the PDI client connects to the Pentaho Repository.

To use Pan and Kitchen from a repository directly on the Pentaho Server, create the named cluster definition in the server repository.

See [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article).

**Note:** If the PDI client and Pentaho Server run on the same platform, cluster configuration files in `/home/<user>/.pentaho/metastore` can be overwritten. Use the same cluster connection names on both hosts.

**Configure the PDI client**

1. Create a connection to the Hadoop cluster where you want to run the job or transformation.
2. Create and test the job or transformation in the PDI client.
3. Go to `design-tools/data-integration/plugins/pentaho-big-data-plugin`.
4. Open `plugin.properties` in a text editor.
5. Set `hadoop.configurations.path` to the directory that contains `metastore`.

   Example: `hadoop.configurations.path=/home/<user>/.pentaho`

   The default metastore location is `/home/<user>/.pentaho/metastore`.
6. Save and close `plugin.properties`.

**Configure the Pentaho Server**

1. If the server is on a different host, copy the `metastore` directory and its contents from the PDI client to a location the server can access.

   The default metastore location for the PDI client is `/home/<user>/.pentaho/metastore`.
2. Go to `pentaho-server/pentaho-solutions/system/kettle/plugins/pentaho-big-data-plugin`.
3. Open `plugin.properties` in a text editor.
4. Set `hadoop.configurations.path` to the directory that contains `metastore`.
5. Save and close `plugin.properties`.

</details>

### Run and monitor remotely with Carte

Carte is a lightweight web server for running PDI transformations and jobs remotely.

It receives the transformation or job (as XML) plus the run configuration.

It also exposes endpoints to monitor, start, and stop executions.

<details>

<summary>Carte setup and reference (clusters, security, client config)</summary>

* [Carte clusters](#carte-clusters)
* [Set up servers](#set-up-servers)
* [Configure the PDI client](#configure-the-pdi-client)
* [Run transformations in a cluster](#run-transformations-in-a-cluster)
* [Schedule and run remotely](#schedule-and-run-remotely)
* [Stop Carte](#stop-carte)

#### Carte clusters

Use a Carte cluster to distribute transformation processing across multiple Carte servers.

A cluster includes:

* One **master** node that tracks execution.
* Two or more **slave** nodes that do the work.

You can also run a single Carte instance as a standalone remote execution engine.

Define one or more Carte servers in the PDI client (Spoon), then send jobs and transformations to them.

{% hint style="info" %}
You can cluster Pentaho Server for failover. If you use Pentaho Server as the cluster master (dynamic cluster), enable the proxy trusting filter. See [Schedule jobs to run on a remote Carte server](#schedule-jobs-to-run-on-a-remote-carte-server).
{% endhint %}

**Cluster types**

**Static cluster**

Static clusters have a fixed schema.

You define the master and slave nodes at design time.

Static clusters fit smaller, stable environments.

**Dynamic cluster**

Dynamic clusters discover slave nodes at run time.

Slave nodes are registered with the master.

PDI monitors slaves every 30 seconds to see if they are available.

Dynamic clusters fit cloud-like environments where nodes come and go.

#### Set up servers

**Prerequisites**

* Copy required JDBC drivers and PDI plugins from your dev system to each Carte instance.
* If you will run content from a Pentaho Repository, copy `repositories.xml` from your workstation’s `.kettle` directory to the same location on each Carte server.

**Set up a static cluster (start slave servers)**

1. Start each slave server with the host and port you want to expose:

   ```sh
   ./carte.sh 127.0.0.1 8081
   ```
2. Verify each server is reachable from your PDI client.
3. (Optional) Create an init/startup script to start Carte on boot.

{% hint style="info" %}
When Carte runs embedded in Pentaho Server, configuration is controlled by `slave-server-config.xml` under `.../pentaho-solutions/system/kettle/`. Stop Pentaho Server before editing that file.
{% endhint %}

**Set up a dynamic cluster**

Dynamic clusters use two configuration files:

* `carte-master-config.xml` for the master.
* `carte-slave-config.xml` for each slave.

You can rename the files.

Keep the required XML structure and values.

**Configure a Carte master server**

1. Copy required JDBC drivers and plugins to the master host.
2. Create `carte-master-config.xml` using this template:

   ```xml
   <slave_config>
     <!-- On a master server, the slaveserver node describes this Carte instance -->
     <slaveserver>
       <name>Master</name>
       <hostname>yourhostname</hostname>
       <port>9001</port>
       <username>cluster</username>
       <password>cluster</password>
       <master>Y</master>
     </slaveserver>
   </slave_config>
   ```

   The master `<name>` must be unique in the cluster.
3. Start Carte using the master config file:

   ```sh
   ./carte.sh carte-master-config.xml
   ```
4. Verify the master is running.
5. (Optional) Create an init/startup script for boot-time startup.

**Configure Carte slave servers**

1. Ensure the master is running.
2. Copy required JDBC drivers and plugins to each slave host.
3. Create `carte-slave-config.xml` using this template:

   ```xml
   <slave_config>
     <!-- The masters node defines the load-balancing Carte instance(s) managing this slave -->
     <masters>
       <slaveserver>
         <name>Master</name>
         <hostname>yourhostname</hostname>
         <port>9000</port>
         <!-- Uncomment if you want DI Server to act as the load balancer -->
         <!-- <webAppName>pentaho</webAppName> -->
         <username>cluster</username>
         <password>cluster</password>
         <master>Y</master>
       </slaveserver>
     </masters>

     <report_to_masters>Y</report_to_masters>

     <!-- The slaveserver node describes this slave instance -->
     <slaveserver>
       <name>SlaveOne</name>
       <hostname>yourhostname</hostname>
       <port>9001</port>
       <username>cluster</username>
       <password>cluster</password>
       <master>N</master>
     </slaveserver>
   </slave_config>
   ```

   Each slave `<name>` must be unique in the cluster.
4. (Optional) To use the master’s Kettle properties on a slave, add these tags inside the slave’s `<slaveserver>`:

   ```xml
   <get_properties_from_master>Master</get_properties_from_master>
   <override_existing_properties>Y</override_existing_properties>
   ```
5. Start Carte using the slave config file:

   ```sh
   ./carte.sh carte-slave-config.xml
   ```
6. If you use Pentaho Repository content, copy `repositories.xml` to each slave’s `.kettle` directory.
7. Restart the master and slave servers. Restart Pentaho Server if it participates.

{% hint style="info" %}
Carte and PDI track object age for transformations and jobs. Objects are purged only when servers are idle. Purge verification runs every 20 seconds.
{% endhint %}

**Configure schedule and remote execution log cleanup**

These settings live in `slave-server-config.xml`.

Stop Pentaho Server before editing this file.

* `max_log_lines`: Max log lines per execution. Use `0` for no limit.
* `max_log_timeout_minutes`: Remove log lines older than this value. Use `0` for no timeout.
* `object_timeout_minutes`: Remove execution entries older than this value. Use `0` for no timeout.

Example:

```xml
<slave_config>
  <max_log_lines>0</max_log_lines>
  <max_log_timeout_minutes>0</max_log_timeout_minutes>
  <object_timeout_minutes>0</object_timeout_minutes>
</slave_config>
```

#### Security and advanced server settings

**Configure Carte servers for SSL**

Carte SSL uses the JKS keystore format.

Keep the keystore in a restricted-access directory.

Carte runs on Jetty.

For Jetty SSL details, see: <https://wiki.eclipse.org/Jetty/Howto/Configure_SSL>.

1. Stop Carte.
2. Open `carte-master-config.xml`.
3. Add these values inside the master server `<slaveserver>`:

   * `keyStore` (required): Path to the keystore file.
   * `keyStorePassword` (required): Keystore password.
   * `keyPassword` (optional): Private key password. Omit if it matches `keyStorePassword`.

   Example:

   ```xml
   <sslConfig>
     <keyStore>D:\KEY_STORE\Pentaho</keyStore>
     <keyStorePassword>OBF:...</keyStorePassword>
     <keyPassword>OBF:...</keyPassword>
   </sslConfig>
   ```

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Use the <code>encr</code> tool in the <code>data-integration</code> directory to obfuscate passwords: <code>encr.bat -carte &#x3C;password></code> (Windows) or <code>encr.sh -carte &#x3C;password></code> (Linux).</p></div>
4. Add the same `<sslConfig>` block to each `carte-slave-config.xml`.
5. Start Carte.
6. Access Carte over HTTPS:

   ```
   https://<host>:<port>/
   ```

**Configure Carte servers for JAAS**

You can use JAAS for user authentication.

1. Create a JAAS config file (example below) and save it as `carte-ldap.jaas.conf` on the Carte host:

   ```conf
   Kettle {
     org.eclipse.jetty.jaas.spi.LdapLoginModule required
     debug="true"
     contextFactory="com.sun.jndi.ldap.LdapCtxFactory"
     hostname="localhost"
     port="389"
     bindDn="cn=admin,dc=example,dc=com"
     bindPassword="admin"
     authenticationMethod="simple"
     forceBindingLogin="true"
     userBaseDn="ou=People,dc=example,dc=com"
     userRdnAttribute="uid"
     userIdAttribute="uid"
     userPasswordAttribute="userPassword"
     userObjectClass="inetOrgPerson";
   };

   Kettle2 {
     org.eclipse.jetty.jaas.spi.PropertyFileLoginModule required
     debug="true"
     file="/installs/common/carte.users";
   };
   ```

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Set <code>debug="false"</code> in production environments.</p></div>
2. Add these Java options to `Spoon.bat` (Windows) or `spoon.sh` (Linux), updating the path:

   ```
   -Djava.security.auth.login.config=<install path>/openldap/carte-ldap.jaas.conf -Dloginmodulename=Kettle
   ```
3. Start Carte. Verify the server does not prompt for BASIC authentication.

**Change Jetty server parameters**

Carte uses an embedded Jetty server.

Only change these settings if you need to tune connection handling.

* `acceptors`: Threads dedicated to accepting connections. Keep it at or below CPU count.
* `acceptQueueSize`: Backlog size before the OS starts rejecting connections.
* `lowResourcesMaxIdleTime`: Close idle connections faster under high load.

Jetty docs:

* <http://wiki.eclipse.org/Jetty/Howto/Configure_Connectors#Configuration_Options>
* <https://wiki.eclipse.org/Jetty/Howto/High_Load>

**Set Jetty parameters in a Carte config file**

Add this block inside `<slave_config>` in `carte-slave-config.xml`:

```xml
<jetty_options>
  <acceptors>2</acceptors>
  <acceptQueueSize>2</acceptQueueSize>
  <lowResourcesMaxIdleTime>2</lowResourcesMaxIdleTime>
</jetty_options>
```

Adjust values, then save the file.

**Set Jetty parameters in `kettle.properties`**

Set these variables to numeric values:

* `KETTLE_CARTE_JETTY_ACCEPTORS`
* `KETTLE_CARTE_JETTY_ACCEPT_QUEUE_SIZE`
* `KETTLE_CARTE_JETTY_RES_MAX_IDLE_TIME`

#### Configure the PDI client

**Initialize slave servers**

1. Open a transformation.
2. In **Explorer View**, select the **Slave** tab.
3. Select **New**.
4. Enter the slave server connection details:

   * Server name
   * Hostname or IP address
   * Port (leave blank for port 80)
   * Web App Name (required only for Pentaho Server)
   * User name and password
   * **Is the master**

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>For clustered executions, define one master and the rest as slaves.</p></div>
5. Select **OK**.

**Create a cluster schema**

In **Explorer View**, right-click **Kettle cluster schemas**, then select **New**.

Configure:

* **Schema name**
* **Port**: Starting port for slave step numbering.
* **Sockets buffer size**
* **Sockets flush interval rows**
* **Sockets data compressed?**
* **Dynamic cluster**: Enable if a master Carte server performs failover.
* **Slave Servers**: Add one master and any number of slaves.

#### Run transformations in a cluster

* Open the **Run Options** window (toolbar **Run** context menu or `F8`).
* Select a run configuration that runs the transformation in clustered mode.
* To run a clustered transformation from a job, open the **Transformation** job entry, then set **Run this transformation in a clustered mode?** on the **Advanced** tab.
* To assign a cluster to a step, right-click the step, select **Clusters**, then pick a cluster schema.
* When running clustered transformations, enable **Show transformations** to see the generated transformations that run on the cluster.

#### Schedule and run remotely

**Schedule jobs to run on a remote Carte server**

These changes are required to schedule a job to run on a remote Carte server.

They are also required if Pentaho Server acts as the load balancer in a dynamic Carte cluster.

1. Stop Pentaho Server and the remote Carte server.
2. Copy `repositories.xml` from your workstation’s `.kettle` directory to the same location on the Carte host.
3. Open `.../tomcat/webapps/pentaho/WEB-INF/web.xml`.
4. In the **Proxy Trusting Filter** section, add the Carte server IP to `TrustedIpAddrs`.
5. Uncomment the proxy trusting filter mappings between the `<!-- begin trust -->` and `<!-- end trust -->` markers.
6. Save `web.xml`.
7. Add `-Dpentaho.repository.client.attemptTrust=true` to the Carte startup script:
   * **Windows (`Carte.bat`)**: add to the `OPT` line.
   * **Linux (`Carte.sh`)**: add to the `OPT` variable before `export OPT`.
8. Start the Carte server and Pentaho Server.

**Run transformations and jobs from a repository on the Carte server**

Copy `repositories.xml` from the user’s `.kettle` directory to the Carte host’s `$HOME/.kettle` directory.

Carte also looks for `repositories.xml` in the directory where you started Carte.

#### Stop Carte

You can stop Carte from the command line or from a URL.

**Stop from the CLI**

Arguments:

```
Carte <Interface address> <Port> [-s] [-p <arg>] [-u <arg>]
```

Example:

```
Carte 127.0.0.1 8080 -s -p amidala4ever -u dvader
```

Options:

* `-h, --help`: Help text.
* `-s, --stop`: Stop the running Carte server.
* `-u, --username <arg>`: Admin user name.
* `-p, --password <arg>`: Admin password.

**Stop from a URL**

```
http://localhost:8080/kettle/stopCarte
```

</details>

### Expose transformation output with Pentaho Data Services

Use Pentaho Data Services to expose a transformation step as a virtual table.

Query it over JDBC using SQL.

{% hint style="info" %}
You need a Pentaho Server and repository to publish a data service.
{% endhint %}

<details>

<summary>Pentaho Data Services guide (install, create, test, optimize)</summary>

Prototyping a data model can be time consuming, particularly when it involves setting up databases, creating the data model and setting up a data warehouse, then negotiating accesses so that analysts can visualize the data and provide feedback.

One way to streamline this process is to make the output of a [transformation](https://docs.pentaho.com/pdia-data-integration/basic-concepts-of-pdi) step a Pentaho Data Service.

The output of the transformation step is exposed by the data service so that the output data can be queried as if it were stored in a physical table, even though the results of the transformation are not stored in a physical database.

Instead, results are published to the Pentaho Server as a virtual table.

{% hint style="info" %}
You must have a Pentaho Server and repository to publish the data service.
{% endhint %}

The virtual table is a JDBC-compliant data source that you and others can connect to or query with SQL, provided they can access the server and the transformation.

The Pentaho Data Service can be connected to or queried by a JDBC-compliant tool such as Pentaho Report Designer, Pentaho Interactive Reports, and CTools as well as other compatible tools like RStudio, DBVisualizer, or SQuirreL.

The Pentaho Data Service can also be used in some instances where building and maintaining a data warehouse is sometimes impractical or inefficient, especially when you need to quickly blend and visualize fast-moving or quickly evolving data sets on the fly.

For example, if you want to compare your product prices with your competitors, you can create a transformation that blends prices from your in-house data sources and competitor prices.

Then, you can convert the output step in the transformation into a Pentaho Data Service that creates a virtual table for querying when you connect to the Pentaho Server.

You or others can connect to and query the virtual table, as you would any other JDBC data source to visualize the results in Analyzer or another tool.

The Pentaho Data Service also has a testing tool.

This tool generates several logs and reports that you can use to refine the data service and determine where to apply specialized optimizations.

You can also define parameters that others can use to pose customized queries.

For example, you can create a data service that publishes a virtual “fact” table of a moderately-sized research dataset to a Pentaho Server.

You can test and add optimizations and parameters, such as gender or test type so that the data service runs more quickly.

Then, you can share connection and parameter information with a group of researchers, who can query the virtual table.

Researchers can use Pentaho Interactive Reporting, a dashboard created with CTools, or an application of their choice, such as RStudio, to analyze and visualize the research dataset.

Pentaho Data Services support a subset of SQL.

For details, see [SQL support reference](#sql-support-reference).

{% hint style="info" %}
Install the Pentaho Data Services plugin before you create data services.
{% endhint %}

#### In this article

* [Install](#install-pentaho-data-services)
* [Create](#create-a-regular-or-streaming-pentaho-data-service)
* [Open or edit](#open-or-edit-a-pentaho-data-service)
* [Delete](#delete-a-pentaho-data-service)
* [Test](#test-a-pentaho-data-service)
* [SQL support reference](#sql-support-reference)
* [Optimize](#optimize-a-pentaho-data-service)
* [Publish](#publish-a-pentaho-data-service)
* [Share](#share-a-pentaho-data-service-with-others)
* [Monitor](#monitor-a-pentaho-data-service)

#### Install Pentaho Data Services

Pentaho Data Services plugin is an optional plugin.

**Pentaho Data Integration**

Install the plugin in Pentaho Data Integration by using the Plugin Manager. For instructions, see [Install plugins in PDI client](https://docs.pentaho.com/pdia-data-integration/use-plugin-manager#install-plugins).

**Pentaho Server**

Install the plugin on Pentaho Server by using the Plugin manager. For instructions, see [Install plugins in PUC](https://app.gitbook.com/s/dbSFXbJFiObHB299lSSa/pentaho-user-console/modern-design/plugin-manager#install-plugins-in-puc).

After you have installed the plugin, add the driver for the Pentaho Data Services plugin by completing the following steps:

1. In the PDI client, open a new transformation.
2. In the **View** tab, expand the **Configurations** section.
3. Right-click **Data Service** and select **Driver Details**.
4. In the **Driver Details** window, click **Get Pentaho Driver**.
5. In the **Save As** window, indicate where you want to save the `PDI-Data-Service-Driver-Pentaho.jar` file, then click **Save**.
6. Move or copy the `PDI-Data-Service-Driver-Pentaho.jar` into the `pentaho-server/tomcat/webapps/pentaho/WEB-INF/lib` folder.
7. Close the transformation without saving.
8. Restart the Pentaho Server.

#### Create a regular or streaming Pentaho Data Service

You can create either a regular data service or a [streaming analytics](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/streaming-analytics) service.

Streaming data services are commonly used when creating streaming dashboards with CTools.

1. [Create or open a transformation](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/work-with-transformations-cp).
2. Save the transformation to the Pentaho Server.
3. Right-click the transformation step that outputs the data you want.
4. Select **Data Services** > **New**.
5. Enter a unique name in **Service Name (Virtual Table Name)**.
6. Confirm **Output step** is the step you selected.
7. Optional: Select **Streaming** for **Data Service Type**.
8. Select **OK**.

**Data service badge**

After you create a Pentaho Data Service from a step, a data service badge is added to that step.

The badge indicates whether the step has a regular or streaming data service.

![Regular and streaming data service badge types](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-e4e6d0e8ee6aef0d4ba868b60ce4133c58e42950%2FPDITransStep_DataService_Badges.png?alt=media)

#### Open or edit a Pentaho Data Service

To open a data service for viewing or editing, do one of the following in the PDI client:

* In **Explore** > **View**, select **Data Services**. Right-click a data service, then select **Edit**.
* Right-click the step with the data service badge, then select **Data Services** > **Edit**.

#### Delete a Pentaho Data Service

To delete a data service, do one of the following in the PDI client:

* In **Explore** > **View**, select **Data Services**. Right-click a data service, then select **Delete**.
* Right-click the step with the data service badge, then select **Data Services** > **Delete**.

#### Test a Pentaho Data Service

After creating your data service, test it to ensure that it runs properly and generates the data you need.

Testing can uncover bottlenecks in your transformation and help you decide which [optimization techniques](#optimize-a-pentaho-data-service) to apply.

**Run a basic test**

To run a basic test on a regular data service:

1. Verify **Data Service Type** is set to **Regular**.
2. Open the **Test Data Service** window using one of the following:
   * In the Data Service window, select **Test Data Service**.
   * In **Explore** > **View** > **Data Services**, right-click a data service and select **Test**.
   * Right-click the step with the data service badge, then select **Data Services** > **Test**.
3. Optional: Adjust settings:
   * **Log Level**. Controls how much detail appears in logs.
   * **Max Rows**. Limits how many rows appear in results.
4. Select **Execute SQL**.
5. Review the output in [Examine test results](#examine-test-results).
6. Optional: If you need a clean run, [clear the cache](#clear-the-cache) and test again.
7. Select **Close**.
8. Optional: Add an [optimization](#optimize-a-pentaho-data-service).
9. [Publish the data service](#publish-a-pentaho-data-service).

**Run a streaming optimization test**

When you test streaming data, the stream is partitioned into windows (batches).

Windows can be time-based or row-based.

To test a streaming data service:

1. Verify **Data Service Type** is set to **Streaming**.
2. Open the **Test Data Service** window.
3. Select a window mode (**Time Based** or **Row Based**).
4. Configure window settings:
   * **Window Size**
   * **Every**
   * **Limit**
5. Optional: Adjust **Log Level** and **Max Rows**.
6. Select **Execute SQL**.
7. Review the output in [Examine test results](#examine-test-results).
8. Select **Stop** to stop execution.
9. Select **Close**.
10. Optional: Add an [optimization](#optimize-a-pentaho-data-service).
11. [Publish the data service](#publish-a-pentaho-data-service).

**Run an optimization test**

If you have added an optimization, run a test that passes the optimization parameter.

Example query:

```sql
SELECT * FROM Mars WHERE rover='Curiosity'
```

* Select **Preview Optimization** in the Test Data Service window.
* Use [Examine test results](#examine-test-results) to interpret results.

**Examine test results**

Test results appear in the tabs in the bottom half of the Test Data Service window.

When you test or run a data service, two transformations run:

* The service transformation. This is the transformation you built.
* The generated transformation. PDI generates this based on executed SQL.

The following table describes the tabs and what to look for:

| Tab                                  | Description                                           | Tips                                                                                                               |
| ------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Query Results**                    | Events during the test run and query results.         | Verify results. For streaming, watch updates per window.                                                           |
| **Optimized Queries**                | Processing information and results of optimizations.  | Verify optimizations applied correctly. Compare with **Service Metrics** and **Generated Transformation Logging**. |
| **Service Transformation Logging**   | Logs from the service transformation.                 | Check for design or runtime issues. Compare with **Generated Transformation Logging**.                             |
| **Generated Transformation Logging** | Logs from the generated transformation.               | Check SQL support issues. See [SQL support reference](#sql-support-reference).                                     |
| **Service Metrics**                  | GANTT chart timings for the service transformation.   | Find bottlenecks. Compare with **SQL Trans Metrics**.                                                              |
| **SQL Trans Metrics**                | GANTT chart timings for the generated transformation. | Find bottlenecks. Compare with **Service Metrics**.                                                                |

#### SQL support reference

The Pentaho Data Service is designed to support a subset of SQL clauses and literals that are useful for data blending, optimizations, and other scenarios.

Limitations and constraints are listed at the end.

**Supported SQL literals**

The Pentaho Data Service supports the following literals:

* Strings use single quotation marks. Escape a single quote using another single quote: `''`.
* Dates use square brackets. Supported formats:
  * `[yyyy/MM/dd HH:mm:ss.SSS]`
  * `[yyyy/MM/dd HH:mm:ss]`
  * `[yyyy/MM/dd]`
* For an `IN` list, date formats can use single quotes and dashes, for example:
  * `SELECT * FROM BUILDS WHERE BuildDate IN ('2015-03-18', '2015-03-22')`
  * You cannot use bracketed date formats in an `IN` list.
* `Number` and `BigNumber` cannot use grouping symbols. Use `.` for decimals, for example `123.45`.
* Integers contain digits only.
* Boolean values can be `TRUE` or `FALSE`.

**Supported SQL clauses**

The Pentaho Data Service supports the following clauses.

| Clause     | What is supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SELECT`   | <ul><li><code>COUNT(field)</code></li><li><code>COUNT(\*)</code></li><li><code>COUNT(DISTINCT field)</code></li><li><code>DISTINCT \<fields></code></li><li><code>IIF (condition, true-value or field, false-value or field)</code></li><li><code>CASE WHEN condition THEN true-value ELSE false-value END</code></li><li><code>SUM</code></li><li><code>AVG</code></li><li><code>MIN</code></li><li><code>MAX</code></li><li>Aliases with <code>AS</code> or with spaces. Example: <code>SUM(sales) AS "Total Sales"</code> or <code>SUM(sales) TotalSales</code></li><li>Constant expressions. See <strong>Supported SQL literals</strong>.</li></ul>                                                                                                                  |
| `FROM`     | <ul><li>Only one Pentaho service name.</li><li>Aliases for the service name.</li><li>Omit the service name to query an empty row. <code>SELECT 1</code> and <code>SELECT 1 FROM dual</code> are the same.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `WHERE`    | <ul><li>Nested brackets</li><li><code>AND</code>, <code>OR</code>, <code>NOT</code> followed by brackets (example: <code>NOT (A=5 OR C=3)</code>)</li><li>Precedence</li><li>Literals (String and Integer)</li><li><code>PARAMETER('parameter-name')='value'</code> (always evaluates to <code>TRUE</code>)</li><li>Operators: <code>=</code>, <code><</code>, <code>></code>, <code><=</code>, <code>=<</code>, <code>>=</code>, <code>=></code>, <code><></code></li><li><code>LIKE</code> (wildcards: <code>%</code>, <code>?</code>)</li><li><code>REGEX</code></li><li><code>IS NULL</code>, <code>IS NOT NULL</code></li><li><code>IN</code></li><li>Conditions on <code>IIF</code> or its alias</li><li><code>DATE\_TO\_STR(date-field, \<mask>)</code></li></ul> |
| `GROUP BY` | <ul><li>Group on fields. Not on <code>IIF()</code>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `LIMIT`    | <ul><li><code>LIMIT</code></li><li><code>LIMIT offset, count</code></li><li><code>LIMIT count OFFSET offset</code></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `HAVING`   | <ul><li>Apply conditions to aggregates, not aliases.</li><li>Use identical strings for expressions.</li><li>Use conditions on aggregations not in <code>SELECT</code>.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `ORDER BY` | <ul><li>Order on any column, even if not in the result.</li><li>Order on <code>IIF</code> or <code>CASE-WHEN</code> expressions.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**Other development considerations**

Keep these constraints in mind:

* You cannot `JOIN` one data service virtual table to another.
* Data services use the Memory Group By step to group. Watch memory consumption for many groups.
* You cannot specify the same field twice in the same `SELECT` clause.
* Calculations and functions like string concatenation are not supported in queries. Do them in the transformation.

#### Optimize a Pentaho Data Service

As you [test your data service](#test-a-pentaho-data-service), you might see bottlenecks or steps that could run more efficiently.

If you want to improve performance, apply an optimization technique.

**Service cache**

This optimization stores results in a cache.

By default, caching is enabled and results are stored for an hour.

Use this technique when result sets are modest and you expect repeat queries.

**How the service cache optimization works**

If you run the data service while results are cached, PDI can run your query against cached data instead of running the full transformation.

This behavior depends on:

* Whether the cached dataset contains all the records required by the new query
* Other optimizations you apply

![PDI Data Service Cache Optimization Workflow](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-167306f1bf086040aad8143933af5b1997702215%2FPDITransStep_DataService_CacheOptimization.png?alt=media)

When you run tests from the Test Data Service window and change the SQL, PDI does not use the cache.

Tests only return up to **Max Rows**, so using cached results could return incomplete results.

**Adjust the cache duration**

1. In the Data Service window, select the **Service Cache** tab.
2. Select **Enable Caching**.
3. Update **Cache Duration (seconds)**.
4. Select **OK**.
5. [Run an optimization test](#run-an-optimization-test).
6. [Publish the data service](#publish-a-pentaho-data-service).

**Disable the cache**

1. In the Data Service window, select the **Service Cache** tab.
2. Clear **Enable Caching**.
3. Select **OK**.

**Clear the cache**

1. In the Data Service window, select the **Service Cache** tab.
2. Clear **Enable Caching**.
3. Select **OK**.
4. Open the Data Service window again and return to the **Service Cache** tab.
5. Select **Enable Caching**.

**Query pushdown**

Use Query Pushdown to translate the SQL `WHERE` clause into a corresponding `WHERE` clause in:

* Table Input steps
* MongoDB Input steps

The input queries are filtered and handled at the source.

**How query pushdown works**

To apply Query Pushdown, set the optimization values, then add the optimization parameter to the input step query.

The optimization uses a parameter in place of the `WHERE` clause, for example:

`SELECT * FROM 'employee' WHERE ${countryParam}`

![PDI Data Service Query Pushdown Optimization Workflow](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-f6236200cc28552baffe4c396e92b42e726c20d1%2FPDITransStep_DataService_QueryPushdownOptimizationWorkflow.png?alt=media)

**Add the query pushdown parameter to Table Input or MongoDB Input**

1. [Create a transformation](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/work-with-transformations-cp/create-a-transformation) with a Table Input or MongoDB Input step.
2. [Run your transformation](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/work-with-transformations-cp/run-your-transformation).
3. Open the input step.
4. Add a parameter where your `WHERE` clause value belongs:
   * SQL: `SELECT * FROM media WHERE ${countryParam}`
   * MongoDB: `{$match : ${mongoDbParam}}`
5. Press CTRL+SPACE to list parameters.
6. Select **Replace Variables in Script?**.
7. Select **OK**.
8. [Set up query pushdown parameter optimization](#set-up-query-pushdown-parameter-optimization).

**Set up query pushdown parameter optimization**

1. Open the Data Service window and select the **Query Pushdown** tab.
2. Select the plus sign near **Parameters**.
3. Enter the name of the optimization parameter you used in the input query.
4. Select **OK**.
5. Select the step that contains the parameter in **Step Name**.
6. In **Definitions**, map fields:
   * **Data Service Field**. Field name as it appears in transformation output.
   * **Step Field**. Field name as it appears in the data source.
7. Optional: Select **Get Optimizations** to generate optimizations automatically.
8. Select **OK**.
9. Test and publish:
   * [Run an optimization test](#run-an-optimization-test).
   * [Publish the data service](#publish-a-pentaho-data-service).

**Disable the query pushdown optimization**

To disable this optimization, select **Disable an Optimization** in the Data Services window.

**Parameter pushdown**

Parameter Pushdown can be applied to any step in the transformation.

It maps a field value to a transformation parameter for simple equality conditions (example: `WHERE region="South"`).

**How parameter pushdown works**

To set up Parameter Pushdown, configure the optimization, then add the parameter to the step.

![PDI Parameter Pushdown Optimization Workflow](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2Fgit-blob-fee15d9d09577c968f5b27c90b7f4d39a995ec7c%2FPDITransStep_DataService_ParameterPushdownOptimizationWorkflow.png?alt=media)

**Add the parameter pushdown parameter to the step**

1. [Create a transformation](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/work-with-transformations-cp/create-a-transformation).
2. [Run your transformation](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/transforming-data-with-pdi-archive/work-with-transformations-cp/run-your-transformation).
3. Add the parameter to a step, such as JSON Input or REST Client.
4. Select **OK**.
5. [Set up parameter pushdown optimization](#set-up-parameter-pushdown-optimization).

**Set up parameter pushdown optimization**

1. Open the Data Service window and select the **Parameter Pushdown** tab.
2. In **WHERE Clause Column**, enter the data service field name from the existing list.
3. Update **Transformation Parameter** as needed. The name must be unique in the data service.
4. Optional: Update **Value Format**. Default `%s` is usually sufficient.
5. Select **OK**.
6. Test and publish:
   * [Run an optimization test](#run-an-optimization-test).
   * [Publish the data service](#publish-a-pentaho-data-service).

**Streaming optimization**

This optimization limits the batch size used for processing.

Streaming records are partitioned into windows (batches) for processing.

**How streaming optimization works**

You can optimize processing by setting either:

* **Rows Limit**. Maximum rows in a window.
* **Time Limit**. Maximum elapsed time to create a window.

**Adjust the row or time limits**

1. In the Data Service window, select the **Streaming** tab.
2. Update **Rows Limit** or **Time Limit**.
3. Select **OK**.
4. Test and publish:
   * [Run an optimization test](#run-an-optimization-test).
   * [Publish the data service](#publish-a-pentaho-data-service).

#### Publish a Pentaho Data Service

To publish your data service, save the transformation containing the data service to the Pentaho Repository.

To validate that your data service was published:

1. Ensure external assets required by the transformation are accessible on the server.
2. Open a browser and log in to the Pentaho Server.
3. List data services on the server, for example:

   ```
   http://<Pentaho Server Host:Port>/pentaho/kettle/listServices
   ```

#### Share a Pentaho Data Service with others

Once your data service is created and tested, you can share it so others can connect and query it.

**Share prerequisites**

1. Ensure the user or group has permissions to:
   * Access the Pentaho Server and run queries.
   * Read and run the transformation that contains the data service.
2. Provide the data service name as saved in the Pentaho Repository.
3. If you use optimizations, provide names and definitions for any parameters.
4. Provide connection instructions:
   * [Connect from a Pentaho tool](#connect-to-the-pentaho-data-service-from-a-pentaho-tool)
   * [Connect from a non-Pentaho tool](#connect-to-the-pentaho-data-service-from-a-non-pentaho-tool)

**Connect to the Pentaho Data Service from a Pentaho tool**

A Pentaho Data Service is a virtual table containing the output of a step in a PDI transformation.

You can connect to and query:

* A regular data service from Pentaho tools such as Report Designer, Analyzer, and the PDI client.
* A streaming data service from a dashboard created with CTools.

{% hint style="info" %}
You need the data service name and permission to run the transformation and access the Pentaho Server.
{% endhint %}

Connection parameters:

* **Connection Name**. Unique name of the data service.
* **Connection Type**. Pentaho Data Services.
* **Access**. Native (JDBC).
* **Hostname**. Pentaho Server hostname or IP address. Default is `localhost` for local installs.
* **Port Number**. Pentaho Server port. Default is `8080`.
* **Web App Name**. Default is `pentaho`.
* **Username**. A user allowed to run the data service.
* **Password**. Password for that user.

Optional connection parameters:

* `proxyhostname`. Proxy server for HTTP connections.
* `proxyport`. Proxy server port.
* `nonproxyhosts`. Hosts that bypass the proxy. Separate multiple hosts with commas.
* `debugtrans`. File path where PDI saves the generated debug transformation. Example: `/tmp/debug.ktr`.
* `PARAMETER_[optionname]=value`. Sets a transformation parameter. Example: `PARAMETER_model=E6530`.
* `secure`. Set to `TRUE` for HTTPS. Default is HTTP.

**Connect to the Pentaho Data Service from a non-Pentaho tool**

You can connect to and query a data service from tools like RStudio or SQuirreL.

To connect and query, you need the data service name and permission to run the transformation and access the server.

To use a non-Pentaho tool, install the data service JDBC driver, then create a connection in your tool.

**Step 1: Download the Pentaho Data Service JDBC driver**

You can download the driver using the PDI client or manually.

**Download using the PDI client**

1. Open the transformation and identify the step with the data service badge.
2. Open **Driver Details** using one of the following:
   * Right-click the step and select **Data Service** > **Driver Details**.
   * In **Explore** > **View** > **Data Services**, right-click a data service and select **Driver Details**.
   * In the Data Services window, select **Driver Details**.
3. In **Driver Details**, select **Get Third-Party Driver**.
4. Save `Pentaho-Data-Service-Driver.zip`.
5. Select **Close**.

**Download manually**

1. Go to `<Pentaho installation directory>/design-tools/data-integration/plugins/pdi-dataservices-ee-plugin/Data Service JDBC Driver`.
2. Copy `pdi-dataservice-driver-thirdparty-<release-version>.jar`.

{% hint style="info" %}
These steps assume you installed the Pentaho Data Services plugin. See [Install Pentaho Data Services](#install-pentaho-data-services).
{% endhint %}

**Step 2: Install the Pentaho Data Service JDBC driver**

1. Extract the driver files and copy them to your application's JDBC driver directory.
2. Start and stop the application.
3. Create a connection using the instructions in [Connect to the Pentaho Data Service from a non-Pentaho tool](#connect-to-the-pentaho-data-service-from-a-non-pentaho-tool).

**Step 3: Create a connection from a non-Pentaho tool**

Most tools let you create a JDBC connection by specifying a driver class and connection string.

Driver class:

`org.pentaho.di.trans.dataservice.jdbc.ThinDriver`

Connection string format:

```
jdbc:pdi://<Pentaho Server Hostname:Port>/kettle?option=value&option=value
```

Example:

```
jdbc:pdi://localhost:8080/kettle?webappname=pentaho
```

`webappname` is required when the data service runs on Pentaho Server.

**Query a Pentaho Data Service**

You can query a data service using SQL.

If the transformation uses a parameter, you can assign a value in your SQL query.

Limitations:

* SQL support is limited. See [SQL support reference](#sql-support-reference).
* Data services can be queried only with SQL.

**Example: query with a parameter**

Syntax:

```sql
SELECT * FROM '<data-service-name>'
WHERE PARAMETER('<parameter_name>') = '<parameter_value>'
```

Example:

```sql
SELECT *
FROM 'employeeList'
WHERE PARAMETER('employeeRegion') = 'USA EAST'
```

#### Monitor a Pentaho Data Service

To monitor a data service, enter one of the following URLs in your browser:

* List names of data services:

  ```
  http://<Pentaho Server Host:Port>/pentaho/kettle/listServices
  ```
* List data service status:

  ```
  http://<Pentaho Server Host:Port>/pentaho/kettle/status
  ```

Replace `<Pentaho Server Host:Port>` with the host name or IP address and port for the Pentaho Server running the data service.

You must be authenticated and authorized on the Pentaho Server to access these endpoints.

</details>

### Capture lineage with the OpenLineage plugin

Use the OpenLineage plugin to emit standardized lineage events from PDI.

Use these events in Pentaho Data Catalog (PDC) for end-to-end data flow visibility.

<details>

<summary>OpenLineage plugin guide (setup, configuration, supported steps)</summary>

The Pentaho Data Integration (PDI) OpenLineage plugin enables PDI to emit rich, standardized OpenLineage events that can be consumed by Pentaho Data Catalog (PDC) to capture how data moves and is transformed in PDI ETL pipelines.

PDC uses information it captures to provide visual end-to-end transparency of data flows, which improves data observability, strengthens compliance and governance, aids in troubleshooting data issues, and enhances data trust and quality for business users.

OpenLineage events are emitted from PDI when supported transformations are executed by discovering input and output datasets and, when possible, generating column-level lineage.

The OpenLineage plugin emits events for:

* **Start**: transformation starts
* **Complete**: transformations ends
* **Abort**: transformation was stopped without errors
* **Fail**: transformation ended with errors

#### Compatibility matrix

OpenLineage plugin functionality is certified to work as intended for the following versions of PDI:

* 10.2.0.1 (SP1)
* 10.2.0.2 (SP2)
* 10.2.0.3 (SP3)
* 10.2.0.4 (SP4)
* 10.2.0.5 (SP5)
* 10.2.0.6 (SP6)
* 11.0

#### Setting up the plugin

Before you begin, verify that you have a valid license for the OpenLineage plugin.

For information about licenses, see [Acquire and install enterprise licenses](https://app.gitbook.com/s/qfaQ2p0JAZrP8b3cpM9a/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses).

To set up the OpenLineage plugin, you must complete the following tasks:

* [Download the plugin](#download-the-plugin)
* [Install the plugin](#install-the-plugin)
* [Create a configuration file for the plugin](#create-a-configuration-file-for-the-plugin)
* [Enable the plugin](#enable-the-plugin)
* [Validate the plugin works](#validate-the-plugin-works)

**Download the plugin**

Download the OpenLineage plugin from the Pentaho Support Portal.

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.
2. In the **Pentaho** card, click **Download**. The **Downloads** page opens.
3. In the **.x** list, click **Pentaho EE Marketplace Plugins Release**.
4. Scroll to the bottom of the page.
5. In the **Marketplace Plugins** section, click **Open Lineage**.
6. Download the `pdi-openlineage-plugin-<plugin_version>-<build number>.zip` file.

**Install the plugin**

Install the OpenLineage plugin in the PDI client and Pentaho Server by running commands appropriate for your operating system.

{% hint style="info" %}
**Note:** The plugin can be installed in the PDI client, Pentaho Server, or both.
{% endhint %}

Installation commands include the following placeholders that must be replaced:

* `<path-to-data-integration>`: Replace with full path to the PDI client.
* `<path-to-pentaho-server>`: Replace with full path to the Pentaho Server.
* `<version_check_option>`: Replace with one of the following options:
  * `none`: Installs the plugin on any version of Pentaho. If the Pentaho version is unsupported, an error is shown.
  * `loose`: Default option. Installs the plugin on certified and compatible, newer Pentaho versions.
  * `strict`: Installs plugin only on certified Pentaho versions.

To install the OpenLineage plugin, complete the following steps:

1. Stop the PDI client and Pentaho Server.
2. Extract the `pdi-openlineage-plugin-<plugin_version>-<build number>.zip` file to a folder on the computer where the PDI client or PDI Server is installed.
3. In the `pdi-openlineage-plugin-<plugin_version>-<build number>` folder, open a command prompt as an administrator.
4. In the command prompt, run the following installation commands for your operating system, replacing the placeholders for paths and version check options.
   * Windows
     * PDI client

       `install.bat -t <path-to-data-integration> --platformVersionCheck <version_check_option>`
     * PDI Server

       `install.bat -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>`
   * Linux
     * PDI client

       `./install.sh -t <path-to-data-integration> --platformVersionCheck <version_check_option>`
     * PDI Server

       `./install.sh -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>`
5. Start the PDI client and Pentaho Server.

**Generate an encrypted password**

If you plan to emit events to PDC, and want to secure your password so that it's not in plain text, you can generate an encrypted password to authenticate to PDC.

The encrypted password is used in the configuration file for the OpenLineage plugin.

1. On the computer where the PDI client or PDI Server is installed, open a command prompt.
2. Run one of the following commands for your operating system:

   * **Windows**
     * To generate a password using the default Pentaho encryption seed, run the following command:

       ```bash
       cd <path-to-data-integration> # or <path-to-pentaho-server>
       sh encr.bat <your_password>
       ```
     * To generate a password using your own custom encryption seed, run the following command:

       ```bash
       export KETTLE_TWO_WAY_PASSWORD_ENCODER_SEED=<your_custom_seed>your-custom-seed"
       cd <path-to-data-integration> # or <path-to-pentaho-server>
       sh encr.bat <your_password>
       ```
   * **Linux**
     * To generate a password using the default Pentaho encryption seed, run the following command:

       ```bash
       cd /<path-to-data-integration> # or <path-to-pentaho-server>
       sh encr.sh <your_password>
       ```
     * To generate a password using your own custom encryption seed, run the following command:

       ```bash
       export KETTLE_TWO_WAY_PASSWORD_ENCODER_SEED=<your_custom_seed>your-custom-seed"
       cd /<path-to-data-integration> # or <path-to-pentaho-server>
       sh encr.sh <your_password>
       ```

   An encrypted password is generated and displayed in the command prompt, like the following example:

   ```
   Encrypted 2be98afc86aa7f297a414ab3dce93bcc9
   ```

**Create a configuration file for the plugin**

After you install the plugin, create a configuration file that specifies where to send open lineage events.

You can create a simple configuration file for testing or a custom configuration to use in production.

1. In a text editor, create a configuration file with content from one of the following examples, based on your needs:
   * To create a simple configuration file that you can use to quickly validate that the plugin is working, include only the following content:

     ```
     version: 0.0.1
     consumers:
       console:
     ```
   * To create a custom configuration file that includes OpenLineage event consumers in your Pentaho deployment, such as a PDC Server, include the following content:

     ```
     version: 0.0.1
     localHostname: <localhostName>   # optional
     debugMode: false               # PDI client (Spoon) only
     consumers:
       console:
       file:
         - path: /<path_to_file>/openlineage.json
       http:
         - name: PDC
           url: https://<pdc_server_host_name>
           endpoint: /lineage/api/events
           authenticationParameters:
             endpoint: /keycloak/realms/pdc/protocol/openid-connect/token
             username: <pdc_server_username>
             password: <pdc_server_password>
             client_id: pdc-client
             scope: openid
     ```
2. Save the file as `openlineageConfig.yml` in the PDI directory that contains your user-specific configuration files.

   **Notes:**

   * By default, user-specific configuration files are stored in the `.kettle` directory, which is usually in one of the following locations:

     * Windows: `C:\Documents and Settings\example_user\.kettle`
     * Linux: `~/.kettle)`

     However, if you run PDI in a container, configuration files might resolve to the `/root/.kettle` directory.
   * You can add multiple http consumers in the configuration file.

**Enable the plugin**

After you install the OpenLineage plugin and create its configuration file, you must enable the plugin so that it can send open lineage events to the consumers you specified in the configuration file.

**Enable in PDI client**

Enable the plugin in the PDI client by completing the following steps:

1. Log into the PDI client and click **Edit** > **Edit the Kettle.properties file**. The Kettle properties window opens.
2. To make the plugin active, add the following variable and value: `KETTLE_OPEN_LINEAGE_ACTIVE=true`
3. To point PDI to your `openlineageConfig.yml` file, add the following variable with the `<path-to-config-file>` placeholder replaced by the full path to your configuration file directory: `KETTLE_OPEN_LINEAGE_CONFIG_FILE=/<path-to-config-file>/openlineageConfig.yml`
4. Click **OK**. The `kettle.properties` file is saved and the OpenLineage plugin is enabled.

**Enable in Pentaho Server**

Enable the client in the Pentaho Server, by completing the following steps:

1. Navigate to the `kettle.properties` file.

   **Note:** The `kettle.properties` file is usually in one of the following locations:

   * Windows: `C:\Documents and Settings\example_user\.kettle`
   * Linux: `~/.kettle)`

   If you run PDI in a container, the `kettle.properties` file is in the `/root/.kettle` directory.
2. Open the `kettle.properties` file in a text editor.
3. Enable the plugin with its configuration file by adding the following variables and values:

   `KETTLE_OPEN_LINEAGE_ACTIVE=true`

   `KETTLE_OPEN_LINEAGE_CONFIG_FILE=/<path-to-config-file>/openlineageConfig.yml`
4. Save the `kettle.properties` file.

**Validate the plugin works**

You can validate that the plugin is working by verifying that text related to OpenLineage appears in the appropriate logs and files.

To validate that the plugin is working, complete the following steps:

1. In the PDI client, click **File > Open**, and then navigate to sample transformations in your Pentaho folder. For example, in Windows the sampls are in `<path_to_Pentaho>\Pentaho\design-tools\data-integration\samples\transformations`.
2. Select the sample transformation, `TextInput and Output using variables.ktr`, and click **Open**.
3. To run the transformation click **Action** > **Run,** and then in the **Run Options** window, click **Run**. The transformation runs and **Execution Results** pane appears at the bottom of the PDI client.
4. Validate that consumers you have enabled are receiving OpenLineage events by taking one of the following actions:
   * If the `console` consumer is enabled, in the **Execution Results** pane of the PDI client, click the **Logging** tab and verify that the log contains lines with the text, "`OpenLineage-Plugin`".
   * If a `file` consumer is enabled, open the `openlineage.json` file in a text editor and verify that it contains lines with the text, "`OpenLineage-Plugin`". The `openlineage.json` file location is defined in the `openlineageConfig.yml` file.
   * If an `HTTP` consumer is enabled, confirm OpenLineage events are arriving for that consumer. For example, if the PDC is a configured consumer, verify the events arrive in PDC.

**Troubleshoot plugin**

If you are unable to validate that the plugin is working, perform the following troubleshooting actions:

* Verify dataset lineage (input text file -> output text file) and column lineage mappings.
* Validate that the `Kettle.properties` file contains the following variable and value: `KETTLE_OPEN_LINEAGE_ACTIVE=true`.
* Verify that the credentials specified in the `openlineageConfig.yml` file are correct.
* Check your network and firewall settings.

#### Supported steps

Note: This list of supported steps is for version 0.5.0 of the plugin.

**Steps that support dataset lineage and column-level lineage**

* Abort
* Append Streams
* Block this step until steps finish
* Blocking Step
* Data Grid
* Delay Row
* Delete
* Dummy
* Filter Rows
* Generate Rows
* Get Variables
* Group By
* Java Filter
* Mail
* Merge Join
* Microsoft Excel Input

  Lineage is supported for local files, AWS, Mineo, HCP, and other S3-compatible connections.
* Microsoft Excel Output (deprecated)

  Lineage is supported for local files, AWS, Mineo, HCP, and other S3-compatible connections. \[1]
* Microsoft Excel Writer

  Lineage is supported for local files, AWS, Mineo, HCP, and other S3-compatible connections. \[1]
* Prioritize streams
* S3 CSV Input
* S3 File Output \[1]
* Send message to syslog
* Set Variables
* Sort Rows
* Switch/Case
* Table input

  Lineage is supported for the following connections, using the listed SQL functions and clauses:

  * Connection types: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Google BigQuery, Redshift, and Generic Connection \[2]
  * SQL functions: aliases, joins, subqueries, functions, aggregations, constants, expressions, cases, window functions, CTEs, and the set operators: unions, intersects, and excepts.
  * Clauses: GROUP BY, ORDER BY, WHERE, WITH, and HAVING.
* Table output

  Lineage is supported for the following connections: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Redshift, and Generic Connection. \[2]
* Text file input

  Lineage is supported for local files, AWS, Mineo, HCP, and other S3- compatible connections. Fixed filetype is not supported.
* Text file output

  Lineage is supported for local files, AWS, Mineo, HCP, and other S3- compatible file systems. \[1] Fixed filetype is not supported.
* Write to Log

**Steps that support only dataset lineage, not column-level lineage**

* Combination lookup/update

  Lineage is supported for the following connections: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Redshift, and Generic Connection. \[2]
* CSV File Input
* Database Lookup

  Lineage is supported for the following connections: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Redshift, and Generic Connection. \[2]
* De-serialize from file
* Dimension lookup/update

  Lineage is supported for the following connections: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Redshift, and Generic Connection. \[2]
* Fixed file input
* Gzip Csv Input
* Insert/Update

  Lineage is supported for the following connections: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Redshift, and Generic Connection. \[2]
* JSON Input
* JSON Output \[1]
* LDIF Input
* Load file content in memory
* Property Input
* Properties Output \[1]
* Sql File Output \[1]
* Synchronize after merge

  Lineage is supported for the following connections: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Redshift, and Generic Connection. \[2]
* Update

  Lineage is supported for the following connections: MySQL, PostgreSQL, Denodo, Sybase, Oracle, Vertica, SQL Server, Snowflake, Redshift, and Generic Connection. \[2]
* XBase Input

**Notes:**

\[1] Step, which can create multiple files as its output, can be configured to add filenames to its results file so that the name of each file is recorded in lineage. If the `Add filenames to result` option is disabled for the step, only a single, generic target is recorded in lineage. For example, if the `Add filenames to result` option is enabled for the step, the output is recorded in lineage as `<filename>_001.csv`, `<filename>_002.csv`, `<filename>_003.csv`, and so on. But, if the option is disabled, the output is recorded as only `<filename>.csv`.

\[2] Step allows generic connections, but lineage works only with generic connections that are listed as supported.

{% hint style="info" %}
**Note:** The Google Big Query connection is not supported on table output step. An OpenLineage event won't have any dataset outputs from any Google Big Query storage.
{% endhint %}

#### Uninstall plugin

Uninstall the OpenLineage plugin from the PDI client and Pentaho Server by running commands appropriate for your operating system.

Before you begin, you must download the OpenLineage plugin from the Pentaho Support Portal, which contains script files for uninstalling the plugin. For details, see [Download the plugin](#download-the-plugin).

{% hint style="info" %}
**Note:** The plugin can be uninstalled from the PDI client, Pentaho Server, or both.
{% endhint %}

Commands for uninstalling the plugin include the following placeholders that must be replaced:

* `<path-to-data-integration>`: Replace with full path to the PDI client.
* `<path-to-pentaho-server>`: Replace with full path to the Pentaho Server.
* `<version_check_option>`: Replace with one of the following options:
  * `none`: Installs the plugin on any version of Pentaho. If the Pentaho version is unsupported, an error is shown.
  * `loose`: Default option. Installs the plugin on certified and compatible, newer Pentaho versions.
  * `strict`: Installs plugin only on certified Pentaho versions.

To uninstall the OpenLineage plugin, complete the following steps:

1. Stop the PDI client and Pentaho Server.
2. Extract the `pdi-openlineage-plugin-<plugin_version>-<build number>.zip` file to a folder on the computer where the PDI client or PDI Server is installed.
3. In the `pdi-openlineage-plugin-<plugin_version>-<build number>` folder, open a command prompt as an administrator.
4. In the command prompt, run the following installation commands for your operating system, replacing the placeholders for paths and version check options.
   * Windows
     * PDI client

       `uninstall.bat -t <path-to-data-integration> --platformVersionCheck <version_check_option>`
     * PDI Server

       `uninstall.bat -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>`
   * Linux
     * PDI client

       `./uninstall.sh -t <path-to-data-integration> --platformVersionCheck <version_check_option>`
     * PDI Server

       `./uninstall.sh -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>`
5. Start the PDI client and Pentaho Server.

#### Upgrade plugin

{% hint style="info" %}
**Important**: Do not install a new version of the OpenLineage plugin over an existing installation of the plugin.
{% endhint %}

To upgrade the OpenLineage plugin, you must uninstall the plugin and then download and install the new version of the plugin.

For details, see the following sections:

* [Uninstall the plugin](#uninstall-plugin)
* [Download the plugin](#download-the-plugin)
* [Install the plugin](#install-the-plugin)

</details>

### Archived source pages

These pages were merged into this single topic page:

* [Use Command Line Tools to Run Transformations and Jobs](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/loading-data-from-pdi-archive/use-command-line-tools-to-run-transformations-and-jobs)
* [Use Carte Clusters](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/loading-data-from-pdi-archive/use-carte-clusters)
* [Pentaho Data Services](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/loading-data-from-pdi-archive/pentaho-data-services)
* [OpenLineage Plugin](https://docs.pentaho.com/pdia-data-integration/archived-merged-pages/loading-data-from-pdi-archive/openlineage-plugin)
