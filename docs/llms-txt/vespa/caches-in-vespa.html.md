# Source: https://docs.vespa.ai/en/performance/caches-in-vespa.html.md

# Caches

 

## Content node summary cache

The summary cache caches summary requests and is enabled by [proton tuning configuration](../reference/applications/services/content.html#summary). When enabling a proton summary cache, one should also change the way proton reads summary data from mmap to directio as done below. The summary cache saves IO and cpu spent on decompressing of chunked blocks (default 64 KB) of summary data.

Note that the summary cache is shared across multiple document types.

By default, the cache is enabled, using up to 5% of available memory - configuration example:

```
```
<content id="music" version="1.0">
  <engine>
    <proton>
      <tuning>
        <searchnode>
          <summary>
            <io>
              <read>directio</read>
            </io>
            <store>
              <cache>
                <maxsize-percent>5</maxsize-percent><!--percentage of available memory on the content node-->
              </cache>
            </store>
          </summary>
        </searchnode>
      </tuning>
    </proton>
  </engine>

</content>
```
```

 **Note:** If the requested document-summary only contains fields that are[attributes](../content/attributes.html), the summary store (and cache) is not used.

## Protocol phases caches

_ranking.queryCache_ and _groupingSessionCache_described in the [Query API reference](../reference/api/query.html)are only caching data in between phases for a given a query, so other queries do not get any benefits, but these caches saves container - content node(s) round-trips for a _given_ query.

 Copyright © 2025 - [Cookie Preferences](#)

