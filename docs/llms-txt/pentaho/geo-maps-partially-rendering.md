# Source: https://docs.pentaho.com/pba/9.3-analytics/analysis-issues/geo-maps-partially-rendering.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/analysis-issues/geo-maps-partially-rendering.md

# Geo Maps partially rendering

If your Geo Map visualizations in Analyzer are not correctly displaying, the Pentaho Server is not giving them enough time to fully render.

The Pentaho Server has a static length of time it waits for a Geo Map to finish rendering before the image is captured. This delay allows for all map tiles to be downloaded and points to be plotted. The default wait time is 1200 milliseconds, and it is set through the `<map-export-javascript-delay>` node in the `pentaho-solutions/system/pentaho-geo/settings.xml` file, as shown in the following sample line of code:

```javascript
<map-export-javascript-delay>1200</map-export-javascript-delay>

```

The following instructions show how to extend the cache value for Geo Maps:

1. Locate the `pentaho-server/tomcat/webapps/pentaho/WEB-INF/classes` directory and open `ehcache.xml` in a text editor.
2. Look for the `cache` element and increase the value for `maxElementsInMemory` as shown in the following example:

   ```xml
   <cache
       name="pentaho-geo-{CUSTOM_ROLE_TYPE}"
       maxElementsInMemory="1000"
       eternal="false"
       overflowToDisk="true"
       timeToIdleSeconds="0"
       timeToLiveSeconds="0"
       diskPersistent="false"
       diskExpiryThreadIntervalSeconds="120"
     />
   ```
3. Save and close the `ehcache.xml` file.
4. Restart the Pentaho Server.
