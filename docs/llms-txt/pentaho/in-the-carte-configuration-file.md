# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/change-jetty-server-parameters/in-the-carte-configuration-file.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/change-jetty-server-parameters/in-the-carte-configuration-file.md

# In the Carte Configuration file

To change the Jetty server parameters in the carte-slave-config.xml file, complete these steps.

1. In the `/pentaho/design-tools/` directory, open the `carte-slave-config.xml` and add these lines between the *\<slave\_config>* *\</slave\_config>* tags.

   ```xml
   <slave_config>
   ...
       <!-- Carte uses an embedded jetty server. Include this next section only if you want to change the default jetty configuration options.-->
       <jetty_options>
           <acceptors>2</acceptors>
           <acceptQueueSize>2</acceptQueueSize>
           <lowResourcesMaxIdleTime>2</lowResourcesMaxIdleTime>
       </jetty_options>
   </slave_config>
   ```
2. Adjust the values for the parameters as necessary, then save and close the file.
