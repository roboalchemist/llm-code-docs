# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/segment-cache-architecture/cache-control-and-propagation.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/segment-cache-architecture/cache-control-and-propagation.md

# Cache control and propagation

The CacheControl API allows you to modify the contents of the cache of a particular node. It controls both the data cache and the OLAP schema member cache. The API is documented in the Mondrian project documentation at [http://mondrian.pentaho.com](http://mondrian.pentaho.com/).

When flushing a segment region on a node, that node will propagate the change to the external cache by using the **SegmentCache SPI**. If the nodes are not using the local cache space, then the next node to pick up a query requiring that segment data will likely fetch it again through SQL. Once the data is loaded from SQL, it will again be stored in the external segment cache.

You should not use the local cache space when you are using the external cache. For this reason, it is disabled by default in Pentaho Analysis Enterprise Edition.

Using the local cache space on a node can improve performance with increased data locality, but it also means that all the nodes have to be notified of that change. Mondrian nodes do not propagate the cache control operations among the members of a cluster. If you deploy a cluster of Mondrian nodes and do not propagate the change manually across all of them, then some nodes will answer queries with stale data.
