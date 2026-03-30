# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/cache-configuration-files.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/cache-configuration-files.md

# Cache Configuration Files

You can configure the Pentaho analysis cache frameworks by editing specific settings files.

The following files contain configuration settings for Pentaho analysis cache frameworks. All of them are in the same directory inside of the deployed `pentaho.war`: `/WEB-INF/classes/`.

* `pentaho-analysis-config.xml`: Defines the global behavior of the Pentaho Analysis Enterprise Edition plugin. Settings in this file enable you to define which segment cache configuration to use, and to turn off the segment cache altogether.
* `infinispan-config.xml`: The **InfinispanSegmentCache** settings file. It configures the Infinispan system.
* `jgroups-udp.xml`: Configures the cluster backing the Infinispan cache. It defines how the nodes find each other and how they communicate. By default, Pentaho uses UDP and multicast discovery, which enables you to run many instances on a single machine or many instances on many machines. There are examples of other communication setups included in the JAR archive. This file is referenced by infinispan as specified in the `infinispan-config.xml` configuration file.
* `memcached-config.xml`: Configures the Memcached-based segment cache. It is not used by default. To enable it, modify **SEGMENT\_CACHE\_IMPL** in `pentaho-analysis-config.xml`.
