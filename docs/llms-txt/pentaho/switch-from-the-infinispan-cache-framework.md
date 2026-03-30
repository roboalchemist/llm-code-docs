# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-memcached-cp/switch-from-the-infinispan-cache-framework.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-memcached-cp/switch-from-the-infinispan-cache-framework.md

# Switch from the Infinispan cache framework

If you already use the Memcached cache framework in your organization and would like to hook it up to the Pentaho Analyzer OLAP engine, follow the directions below to switch from the default Infinispan cache framework configuration.

**Note:** Pentaho and Mondrian developers recommend against using Memcached. You are almost certain to have better performance with Infinispan.

Perform the following steps to switch from Infinispan to Memcached:

1. If the Pentaho Server or standalone Mondrian engine are running, shut them down now.
2. Verify the required JARs are present in the `/WEB-INF/lib/` directory inside of your deployed `pentaho.war` or Mondrian engine.

   If you performed a default install of the Pentaho Analysis Enterprise Edition package, then you should have all of the required JARs installed to the Pentaho or Mondrian Server. If you are not sure, the required JARs are:

   * `pentaho-analysis-ee`
   * `commons-lang`
   * `commons-io`
   * `commons-codec`
   * `pentaho-ee-dsc-core`
   * `memcached`
3. Edit the `pentaho-analysis-config.xml` in the `/WEB-INF/classes/` directory inside the deployed `pentaho.war` or Mondrian engine, and change the value of `SEGMENT_CACHE_IMPL` to match the class name referenced below:

   ```
   <entry key="SEGMENT_CACHE_IMPL">com.pentaho.​analysis.segmentcache.​impl.memcached.​MemcachedSegmentCache</entry>
   ```
4. Edit the `memcached-config.xml` in the `/WEB-INF/classes/` directory inside the deployed `pentaho.war` or Mondrian engine, and change the values of `SALT`, `SERVERS`, and `WEIGHT` to match your preference:

   ```
   <entry key="SALT">YOUR SECRET SALT VALUE HERE</entry>
   <entry key="SERVERS">192.168.0.1:1642,192.168.0.2:1642</entry>
   <entry key="WEIGHTS">1,1</entry>
   ```

Your Pentaho Analysis Enterprise Edition instance is now configured to use Memcached for OLAP segment caching.
