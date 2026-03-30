# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-reporting-performance-tips/cache-report-content.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-reporting-performance-tips/cache-report-content.md

# Cache report content

You can cache the result sets of parameterized reports so that every time you change a parameter during your user session (all caching is on a per-session basis) you do not have to retrieve a new result set. By default, Pentaho Reporting has result set caching turned on, but you may find some advantage in turning it off or changing the cache thresholds and settings.

**Note:** When you publish a report to the Pentaho Server, you switch cache and engine configurations from the local Report Designer versions of `ehcache.xml` and `classic-engine.properties` to the server's version inside the Pentaho WAR. These configurations may not be the same, so if you have made changes to the result set cache settings locally, you may want to port those changes over to the Pentaho Server as well.

## Result set caching

When rendered, a parameterized report must account for every dataset required for every parameter. Every time a parameter field changes, every dataset is recalculated, which can negatively impact performance.

You can avoid gratuitous dataset recalculations by caching parameter datasets. This is accomplished through the EHcache framework built into the Pentaho Server. You can configure specific settings for published reports by editing the `ehcache.xml` file in the `/WEB-INF/classes/` folder inside of the `pentaho.war`. The relevant element is:

Anything containing complex objects is not cached (CLOB and BLOB data types). These are results coming from a scripting dataset, a Java method call, a table data source, an external data source (computed in an action sequence), or a CDA data source. In all cases, either no point in caching exists because it would be more expensive than recalculating, or because not enough hints are available in the involved parameters.

```
<!--
    Defines a cache used by the reporting engine to hold small datasets.
    This cache can be configured to have a separate instance for each
logged in user via the
    global report configuration. This per-user cache is required if role
or other security and
    filter information is used in ways invisible for the reporting
engine.
  -->
  <cache name="report-dataset-cache"
        maxElementsInMemory="50"
        eternal="false"
        overflowToDisk="false"
        timeToIdleSeconds="300"
        timeToLiveSeconds="600"
        diskPersistent="false"
        diskExpiryThreadIntervalSeconds="120"
    />
```

However, if a cache exists for too long, it may not reflect in the report output because it is still using old data. So there is a balance between performance and accuracy that you must tailor to your needs.

## Result set cache options

These `classic-engine.properties` options control result set caching in parameterized reports.

| Option                                                                              | Purpose                                                                                                                                                   | Possible Values                 |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **org.pentaho.reporting​.platform.plugin.cache.​PentahoDataCache.CachableRowLimit** | Number of rows in the dataset that will be cached; the higher the number, the larger the cache and the more disk space is used while the cache is active. | Integer; default value is: 1000 |
