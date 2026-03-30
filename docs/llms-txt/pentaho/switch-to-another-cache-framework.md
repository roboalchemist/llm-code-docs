# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-another-cache-framework.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-another-cache-framework.md

# Switch to another cache framework

Pentaho ships with configuration files that assume a JBoss Infinispan deployment.

**Note:** The segment cache features explained in this section are for very large OLAP deployments.

Instructions are provided below for switching to the Pentaho Platform Delegating Cache or Memcached. Also in this section is a brief overview of how to create a Java class to implement your own custom cache system:

**Note:** Pentaho strongly recommends Infinispan over Memcached for maximum OLAP performance.

* [Switch to Memcached](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-memcached-cp)
* [Switch to Pentaho Platform Delegating Cache](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-another-cache-framework/switch-to-pentaho-platform-delegating-cache)
* [Use a Custom SegmentCache SPI](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-another-cache-framework/use-a-custom-segmentcache-spi)
