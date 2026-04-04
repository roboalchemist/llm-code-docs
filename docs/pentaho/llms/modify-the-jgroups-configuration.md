# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/modify-the-jgroups-configuration.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/modify-the-jgroups-configuration.md

# Modify the JGroups configuration

The default Infinispan configuration uses JGroups to distribute the cache across all Mondrian instances it finds on the local network. If you want to modify how those communications are done, you must edit the JGroups configuration file.

**Note:** The segment cache features explained in this section are for very large OLAP deployments.

Each node might require a different configuration; the default configuration is highly portable.

If you are deploying this plugin on Amazon EC2, JGroups has a special configuration file that you copied to your `/WEB-INF/classes/` directory when you installed the Analysis Enterprise Edition package. Additionally, default JGroups configuration files are inside of the JAR archive.

**Note:** Fine-grained JGroups configuration is covered in the [JGroups documentation](http://www.jgroups.org/ug.html); you should read through it before making changes.

To switch implementations, edit `infinispan-config.xml` and make the modification appropriate to your communication method:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Communication Type</td><td>Configuration Entry</td></tr><tr><td>UDP communication</td><td><pre><code>&#x3C;property name="configurationFile" value="jgroups-udp.xml"/>
</code></pre></td></tr><tr><td>TCP communication</td><td><pre><code>&#x3C;property name="configurationFile" value="jgroups-tcp.xml"/>
</code></pre></td></tr><tr><td>Amazon EC2</td><td><pre><code>&#x3C;property name="configurationFile" value="jgroups-ec2.xml"/>
</code></pre></td></tr></tbody></table>
