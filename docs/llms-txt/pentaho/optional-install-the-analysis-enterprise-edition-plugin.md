# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/install-the-ba-design-tools/optional-install-the-analysis-enterprise-edition-plugin.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-of-the-pentaho-design-tools/optional-install-the-analysis-enterprise-edition-plugin.md

# (Optional) Install the Analysis Enterprise Edition plugin

AUDIENCE: Advanced Mondrian users who want to distribute cached data across a self-managed cluster of peers.

The Analysis Enterprise Edition Plugin is distributed as a set of JAR archives and configuration files which must be deployed alongside an existing Mondrian installation. This plugin contains Analysis engine enhancements for large ROLAP deployments. When this JAR archive is deployed properly, it will register new features and make them available to Mondrian. For more information about using this plugin with Mondrian, see [Mondrian cache control](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control).

Follow the instructions below to install the Pentaho Analysis Enterprise Edition package:

1. If you have not already done so, retrieve the `pentaho-analysis-ee-10.2.0.zip` file from the Pentaho website.
2. Unpack the file to a temporary location.
3. Stop the Pentaho Server if it is running.
4. Copy the following JARs from the `/pentaho-analysis-ee/lib/` directory to the `/tomcat/webapps/pentaho/WEB-INF/lib/` directory.
   * `pentaho-analysis-ee-core-10.2.0-obf.jar`
   * `infinispan-commons-8.2.5.Final.jar`
   * `infinispan-core-8.2.5.Final.jar`
   * `jboss-logging-3.3.0.GA.jar`
   * `jboss-marshalling-osgi-1.4.10.Final.jar`
   * `jboss-transaction-api_1.1_spec-1.0.1.Final.jar`
   * `jgroups-3.6.7.Final.jar`
   * `memcached-0.0.1-PENTAHO.jar`
5. Copy all the configuration files (listed in the following table) from `/pentaho-analysis-ee/config/` to the `/tomcat/webapps/pentaho/WEB-INF/classes/` directory.

   | File                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | `pentaho-analysis-config.xml` | Defines the global behavior of the Pentaho Analysis Enterprise Edition plugin. Settings in this file enable you to define which segment cache configuration to use, and to turn off the segment cache altogether.                                                                                                                                                                                                                                                  |
   | `infinispan-config.xml`       | The InfinispanSegmentCache settings file. It configures the Infinispan system.                                                                                                                                                                                                                                                                                                                                                                                     |
   | `jgroups-tcp.xml`             | Configures the cluster backing the Infinispan cache. It defines how the nodes find each other and how they communicate. By default, Pentaho uses TCP and multicast discovery, which enables you to run many instances on a single machine or many instances on many machines. (There are examples of other communication setups included in the JAR archive.) This file is referenced by infinispan as specified in the`infinispan-config.xml` configuration file. |
   | `memcached-config.xml`        | Configures the Memcached-based segment cache. It is not used by default. To enable it, modify **SEGMENT\_CACHE\_IMPL** in: `pentaho-analysis-config.xml`                                                                                                                                                                                                                                                                                                           |
6. Depending on the installation type, there would not be a `pentaho.war` file.

   In archive-based installations and executable-based installations, the `pentaho.war` is already deployed and the application will show as: `/tomcat/webapps/pentaho/`
7. Remove the temporary `pentaho-analysis-ee` directory.
8. To enable the segment cache plugin, first follow the installation steps above.

   Once complete, open the file `WEB-INF/classes/pentaho-analysis-config.xml` and set the following property:

   ```

   <entry key="USE_SEGMENT_CACHE">true</entry>

   ```

   For more details see: <https://pentaho-community.atlassian.net/wiki/spaces/analysis/pages/1790804859/Pentaho+Analysis+EE>

Pentaho Analysis Enterprise Edition is now installed with the default Infinispan configuration.
