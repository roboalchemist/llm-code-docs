# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/memory-optimization-for-the-geo-service-plugin.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-server-performance-tips/memory-optimization-for-the-geo-service-plugin.md

# Memory optimization for the Geo Service plugin

The Pentaho Geo Service enables Geo Map visualizations in Analyzer.

If you do not use Analyzer or use the Geo Service in Analyzer, you can free up approximately 200MB of RAM by removing the Geo Service plugin. Shut down the Pentaho Server and delete the `/pentaho/server/pentaho-server/pentaho-solutions/system/pentaho-geo/` directory.

If you frequently use the Geo Service, update the cache setting for `pentaho-geo roles` in the `ehcache.xml` file. This file can be found in the `/pentaho/server/pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes` directory. For example, if you add a large number of municipalities, you may want to increase the number of municipalities cached in memory or configure `overflowToDisk` for the `pentaho-geo-municipality` role.
