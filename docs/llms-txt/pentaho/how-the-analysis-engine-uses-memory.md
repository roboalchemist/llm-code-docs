# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/segment-cache-architecture/how-the-analysis-engine-uses-memory.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/segment-cache-architecture/how-the-analysis-engine-uses-memory.md

# How the Analysis engine uses memory

This is the order in which Mondrian will try to obtain data for a required segment once a query is received:

1. The node will parse the query and figure out which segments it must load to answer that particular query
2. It checks into the local cache, if enabled.
3. If the data could not be loaded from the local cache, it checks into the external segment cache, provided by the Pentaho Analysis plugin, and it places a copy inside the query cache.
4. If the data is not available from the external cache, it loads the data form SQL and places it into the query cache.
5. If the data was loaded form SQL, it places a copy in the query cache and it sends it to the external cache to be immediately shared with the other Mondrian nodes.
6. The node can now answer the query.
7. Once the query is answered, Mondrian will release the data from the query cache.
8. If the local cache is enabled, a weak reference to the data is kept there.

![How the Analysis Engine Used Memory](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-ec3df32e6c3b764fd5c638682e412b0582a91230%2FMondrianSegmentCacheSPI_new.png?alt=media)
