# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-openlineage-plugin.md

# PDI OpenLineage Plugin

The Pentaho Data Integration (PDI) OpenLineage plugin enables PDI to emit rich, standardized OpenLineage events that can be consumed by Pentaho Data Catalog (PDC) to capture how data moves and is transformed in PDI ETL pipelines. PDC uses information it captures to provide visual end-to-end transparency of data flows, which improves data observability, strengthens compliance and governance, aids in troubleshooting data issues, and enhances data trust and quality for business users.

OpenLineage events are emitted from PDI when supported transformations are executed by discovering input and output datasets and, when possible, generating column-level lineage.

The OpenLineage plugin emits events for:

* Start: transformation starts
* Complete: transformation ends
* Abort: transformation was stopped without errors
* Fail: transformation ended with errors

### Compatibility matrix

OpenLineage plugin functionality is certified to work as intended for the following versions of PDI:

* 10.2.0.1 (SP1)
* 10.2.0.2 (SP2)
* 10.2.0.3 (SP3)
* 10.2.0.4 (SP4)
* 10.2.0.5 (SP5)
* 10.2.0.6 (SP6)
* 11.0

### Setting up the plugin

Before you begin, verify that you have a valid license for the OpenLineage plugin. For information about licenses, see Acquire and install enterprise licenses: <https://docs.pentaho.com/install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses>

To set up the OpenLineage plugin, complete the following tasks:

* Download the plugin
* Install the plugin
* Create a configuration file for the plugin
* Enable the plugin
* Validate the plugin works

### Installation and setup procedures

{% stepper %}
{% step %}

### Download the plugin

Download the OpenLineage plugin from the Pentaho Support Portal.

Steps:

1. On the Support Portal home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet: <https://support.pentaho.com/hc/en-us>
2. In the Pentaho card, click Download. The Downloads page opens.
3. In the .x list, click Pentaho EE Marketplace Plugins Release.
4. Scroll to the bottom of the page.
5. In the Marketplace Plugins section, click Open Lineage.
6. Download the pdi-openlineage-plugin-\<plugin\_version>-.zip file: <https://download.pentaho.com/PDI/Marketplace+Plugins+10.2/Open+Lineage#>
   {% endstep %}

{% step %}

### Install the plugin

Install the OpenLineage plugin in the PDI client and/or Pentaho Server.

Notes:

* The plugin can be installed in the PDI client, Pentaho Server, or both.
* Installation commands include placeholders:
  * : full path to the PDI client.
  * : full path to the Pentaho Server.
  * \<version\_check\_option>: one of:
    * `none`: Installs the plugin on any version of Pentaho. If the Pentaho version is unsupported, an error is shown.
    * `loose`: Default option. Installs the plugin on certified and compatible, newer Pentaho versions.
    * `strict`: Installs plugin only on certified Pentaho versions.

Steps:

1. Stop the PDI client and Pentaho Server.
2. Extract the pdi-openlineage-plugin-\<plugin\_version>-.zip file to a folder on the computer where the PDI client or PDI Server is installed.
3. In the extracted pdi-openlineage-plugin-\<plugin\_version>- folder, open a command prompt as an administrator.
4. Run the following installation commands for your OS, replacing placeholders:

* Windows
  * PDI client

    ```
    install.bat -t <path-to-data-integration> --platformVersionCheck <version_check_option>
    ```
  * PDI Server

    ```
    install.bat -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>
    ```
* Linux
  * PDI client

    ```
    ./install.sh -t <path-to-data-integration> --platformVersionCheck <version_check_option>
    ```
  * PDI Server

    ```
    ./install.sh -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>
    ```

5. Start the PDI client and Pentaho Server.
   {% endstep %}

{% step %}

### Generate an encrypted password

If you plan to emit events to PDC and want to secure your password, generate an encrypted password to authenticate to PDC. Use the encrypted password in the plugin configuration file.

Steps:

1. On the computer where the PDI client or PDI Server is installed, open a command prompt.
2. Run one of the following commands for your OS.

* Windows
  * To generate a password using the default Pentaho encryption seed:

    ```
    cd \<path-to-data-integration> # or <path-to-pentaho-server>
    sh encr.bat <your_password>
    ```
  * To generate a password using your own custom encryption seed:

    ```
    export KETTLE_TWO_WAY_PASSWORD_ENCODER_SEED=<your_custom_seed>your-custom-seed"
    cd \<path-to-data-integration> # or <path-to-pentaho-server>
    sh encr.bat <your_password>
    ```
* Linux
  * To generate a password using the default Pentaho encryption seed:

    ```
    cd /<path-to-data-integration> # or <path-to-pentaho-server>
    sh encr.sh <your_password>
    ```
  * To generate a password using your own custom encryption seed:

    ```
    export KETTLE_TWO_WAY_PASSWORD_ENCODER_SEED=<your_custom_seed>your-custom-seed"
    cd /<path-to-data-integration> # or <path-to-pentaho-server>
    sh encr.sh <your_password>
    ```

An encrypted password is generated and displayed in the command prompt, for example:

```
Encrypted 2be98afc86aa7f297a414ab3dce93bcc9
```

{% endstep %}

{% step %}

### Create a configuration file for the plugin

After installing the plugin, create a configuration file that specifies where to send OpenLineage events. You can create a simple configuration for testing or a custom configuration for production.

1. In a text editor, create a configuration file with content from one of the following examples:

* Simple configuration (quick validation):

```
version: 0.0.1
consumers:
  console:
```

* Custom configuration (includes OpenLineage event consumers like a PDC Server):

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

2. Save the file as openlineageConfig.yml in the PDI directory that contains your user-specific configuration files.

Notes:

* By default, user-specific configuration files are stored in the .kettle directory, usually:
  * Windows: C:\Documents and Settings\example\_user.kettle
  * Linux: \~/.kettle
* If you run PDI in a container, configuration files might resolve to /root/.kettle.
* You can add multiple http consumers in the configuration file.
  {% endstep %}

{% step %}

### Enable the plugin

After installing the plugin and creating its configuration file, enable the plugin so it can send OpenLineage events to the configured consumers.

Enable in PDI client:

1. Log into the PDI client and click Edit > Edit the Kettle.properties file.
2. Add:

```
KETTLE_OPEN_LINEAGE_ACTIVE=true
```

3. To point PDI to your openlineageConfig.yml file, add (replace placeholder with full path):

```
KETTLE_OPEN_LINEAGE_CONFIG_FILE=/<path-to-config-file>/openlineageConfig.yml
```

4. Click OK to save kettle.properties.

Enable in Pentaho Server:

1. Locate the kettle.properties file (usually in the same .kettle locations as noted earlier; containers use /root/.kettle).
2. Open kettle.properties in a text editor.
3. Add:

```
KETTLE_OPEN_LINEAGE_ACTIVE=true
KETTLE_OPEN_LINEAGE_CONFIG_FILE=/<path-to-config-file>/openlineageConfig.yml
```

4. Save kettle.properties.
   {% endstep %}

{% step %}

### Validate the plugin works

Validate that the plugin is working by checking logs and files for OpenLineage-related text.

Steps:

1. In the PDI client, click File > Open and navigate to sample transformations (e.g., on Windows: \<path\_to\_Pentaho>\Pentaho\design-tools\data-integration\samples\transformations).
2. Open the sample transformation TextInput and Output using variables.ktr.
3. Run the transformation (Action > Run, then Run). Execution Results appears.
4. Validate consumers are receiving OpenLineage events:
   * If the console consumer is enabled: in Execution Results pane, Logging tab, verify log lines contain "OpenLineage-Plugin".
   * If a file consumer is enabled: open the openlineage.json file (location defined in openlineageConfig.yml) and verify it contains lines with "OpenLineage-Plugin".
   * If an HTTP consumer is enabled: confirm OpenLineage events are arriving for that consumer (for example, in PDC).
     {% endstep %}

{% step %}

### Troubleshoot plugin

If validation fails:

* Verify dataset lineage (input text file -> output text file) and column lineage mappings.
* Validate kettle.properties contains:

  ```
  KETTLE_OPEN_LINEAGE_ACTIVE=true
  ```
* Verify credentials in openlineageConfig.yml are correct.
* Check network and firewall settings.
  {% endstep %}
  {% endstepper %}

### Supported steps

Note: This list of supported steps is for version 0.5.0 of the plugin.

Steps that support dataset lineage and column-level lineage

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

  Lineage is supported for local files, AWS, Mineo, HCP, and other S3-compatible connections. Fixed filetype is not supported.
* Text file output

  Lineage is supported for local files, AWS, Mineo, HCP, and other S3-compatible file systems. \[1] Fixed filetype is not supported.
* Write to Log

Steps that support only dataset lineage, not column-level lineage

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

Notes: \[1] Step which can create multiple files as its output can be configured to add filenames to its results file so each filename is recorded in lineage. If the Add filenames to result option is disabled, only a single, generic target is recorded in lineage. For example, with filenames enabled the outputs may be recorded as \_001.csv, \_002.csv, \_003.csv; with filenames disabled the output is recorded as .csv.

\[2] Step allows generic connections, but lineage works only with generic connections that are listed as supported.

Note: The Google Big Query connection is not supported on table output step. An OpenLineage event won't have any dataset outputs from any Google Big Query storage.

### Uninstall plugin

Uninstall the OpenLineage plugin from the PDI client and Pentaho Server by running commands appropriate for your operating system.

Before you begin, download the OpenLineage plugin from the Pentaho Support Portal, which contains script files for uninstalling the plugin. See Download the plugin above.

Notes:

* The plugin can be uninstalled from the PDI client, Pentaho Server, or both.
* Uninstall commands include placeholders:
  * : full path to the PDI client.
  * : full path to the Pentaho Server.
  * \<version\_check\_option>: one of `none`, `loose`, or `strict` (as described earlier).

To uninstall:

1. Stop the PDI client and Pentaho Server.
2. Extract the pdi-openlineage-plugin-\<plugin\_version>-.zip file to a folder on the computer where the PDI client or PDI Server is installed.
3. In the extracted pdi-openlineage-plugin-\<plugin\_version>- folder, open a command prompt as an administrator.
4. Run the following uninstall commands for your OS, replacing placeholders:

* Windows
  * PDI client

    ```
    uninstall.bat -t <path-to-data-integration> --platformVersionCheck <version_check_option>
    ```
  * PDI Server

    ```
    uninstall.bat -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>
    ```
* Linux
  * PDI client

    ```
    ./uninstall.sh -t <path-to-data-integration> --platformVersionCheck <version_check_option>
    ```
  * PDI Server

    ```
    ./uninstall.sh -t <path-to-pentaho-server> --platformVersionCheck <version_check_option>
    ```

5. Start the PDI client and Pentaho Server.

### Upgrade plugin

Important: Do not install a new version of the OpenLineage plugin over an existing installation. To upgrade, uninstall the plugin and then download and install the new version. See:

* Uninstall the plugin (above)
* Download the plugin (above)
* Install the plugin (above)

Last updated: 1 minute ago

Links referenced in this page:

* Acquire and install enterprise licenses: <https://docs.pentaho.com/install/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses>
* Pentaho Support Portal: <https://support.pentaho.com/hc/en-us>
* Plugin download: <https://download.pentaho.com/PDI/Marketplace+Plugins+10.2/Open+Lineage#>
