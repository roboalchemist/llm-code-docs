# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control.md

# Mondrian cache control

You can configure and control the cache infrastructure that the Pentaho Analyzer engine uses for OLAP data, which is useful for properly updating your OLAP cubes when your data warehouse is refreshed, and for performance-tuning.

Most of the advanced cache features explained here are for Enterprise Edition deployments only. Within that, most of the Enterprise Edition features of the Analysis engine are only beneficial to large, multi-node OLAP deployments that are performing poorly.

The Analysis engine does not ship with a segment cache, but it does have the ability to use third-party cache systems. If you've installed Pentaho Analysis Enterprise Edition, then you have a default configuration for the JBoss Infinispan distributed cache, though the actual Infinispan software is not included and must be downloaded separately. Infinispan supports a wide variety of sub-configurations and can be adapted to cache in memory, to the disk, to a relational database, or (the default setting) to a distributed cache cluster.

The Infinispan distributed cache is a highly scalable solution that distributes cached data across a self-managed cluster of Mondrian instances. Every Mondrian instance running the Analysis Enterprise Edition plugin on a local network will automatically discover each other using UDP multicast. An arbitrary number of segment data copies are stored across all available nodes. The total size of the cache will be the sum of all of the nodes' capacities, divided by the number of copies to maintain. This is all fully configurable; options are explained later in this section.

Other supported segment cache configurations include, but are not limited to:

* [Memcached](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-memcached-cp), which uses an established (extant) Memcached infrastructure to cache and share the segment data among Mondrian peers.
* [Segment Cache Architecture](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/segment-cache-architecture)
* [Cache Configuration Files](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/cache-configuration-files)
* [Modify the JGroups Configuration](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/modify-the-jgroups-configuration)
* [Switch to Another Cache Framework](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-another-cache-framework)
