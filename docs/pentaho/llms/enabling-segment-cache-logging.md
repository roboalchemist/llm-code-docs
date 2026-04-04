# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/olap-log-output/enabling-segment-cache-logging.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/olap-log-output/enabling-segment-cache-logging.md

# Enabling segment cache logging

The Pentaho Server allows you to view engine segment cache logs by opening the log window from within Analyzer.

If you are using Analyzer with a standalone Mondrian engine, cache log information is available through `log4j`. Edit your `log4j` configuration as explained in [Analysis SQL output logging](https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/olap-log-output/broken-reference), and set the value of `com.pentaho.analysis.segmentcache` to `DEBUG`. The table below lists other `log4j` categories that can help you diagnose configuration and performance problems.

| Class Name                                            | Cache System                                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `com.pentaho.​analysis.segmentcache.​impl.infinispan` | Outputs information related to the Infinispan implementation of the segment cache.      |
| `com.pentaho.​analysis.segmentcache.​impl.memcached`  | Outputs information related to the Memcached implementation of the segment cache.       |
| `com.pentaho.​analysis.segmentcache.​impl.pentaho`    | Outputs information related to the Pentaho BI Platform Delegating Cache implementation. |
