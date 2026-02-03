# Source: https://docs.vespa.ai/en/operations/self-managed/procedure-change-attribute-index.html.md

# Procedure: Change from attribute to index

 

Changing between `index` and `attribute` is a common field change operation to optimize performance. Use the [reindexing](../reindexing.html) feature to safely migrate data to/from index structures.

Changing from attribute to index can be seen as "drop attribute" and "add index". When the attribute aspect of a field is removed, the field's data is not queryable after deployment. The reindexing process will populate the field's index structure, but this takes time, depending on corpus size.

Another approach is to run with both attribute and index in the transition, keeping data available for queries. The gist of this procedure is to add `index`, run a reindex - then remove `attribute` aspect:

```
# field configuration at start
field artist type string {
    indexing: summary | attribute
}

->

# intermediate step to populate index structure, keeping the data in the attribute
field artist type string {
    indexing: summary | attribute | index
    match: word
    stemming: none
}

->

# final configuration, migrated to index
field artist type string {
    indexing: summary | index
    match: word
    stemming: none
}
```

 **Note:** If the field is used as a filter only (i.e. no ranking), consider adding `rank: filter`, see example in[feature-tuning](../../performance/feature-tuning.html).

## Procedure

1. Test this using the [quick-start](../../basics/deploy-an-application-local.html), changing the `artist` field to an attribute before running. Also add a [validation override](../../reference/applications/validation-overrides.html) in `src/main/application/validation-overrides.xml`: 

2. Run the quick start, stop after feeding documents. Run a query to validate data can be queried: 

3. Add index aspect and match/stemming settings to the field, deploy and observe output 

4. Wait for the new configuration generation to be activated on the config server(s) - this is normally quite immediate. After that, allow up to 3 minutes for the config servers to set reindexing ready, track this using the `reindexing` endpoint: 

5. When ready, deploy again to start reindexing, wait for it to complete (use the loop in previous step): 

6. Dumping the index structures now shows artist both in index and attribute, and there is an entry in vespa.log. Verify the query still works: 

7. As data is now reindexed into the index data structures, deploy without attribute. (Observe changes to index files, "artist" is now in index only). Test query after restart: 

8. Optional: restart Vespa - a restart will reclaim memory from the attribute: 

Notes:

- The match/stemming settings above are set to the same at default attribute settings

## Appendix

To inspect attribute and index data (can be useful when troubleshooting), use [vespa-proton-cmd](../../reference/operations/self-managed/tools.html#vespa-proton-cmd), then list files:

```
$ docker exec vespa vespa-proton-cmd --local triggerFlush
$ docker exec vespa find /opt/vespa/var/db/vespa/search/cluster.music/n0/documents/music/0.ready
```

 Copyright © 2026 - [Cookie Preferences](#)

