# Source: https://docs.vespa.ai/en/writing/indexing-paged-vectors.html.md

# Indexing paged vectors

 

Most of the data of a vector (tensor) index is the vectors themselves. The vector data must be accessed to calculate true distances both when querying the index and when adding vectors to it, and due to the high dimensionality these accesses are effectively random. While it is viable to [page](../content/attributes.html#paged-attributes)indexed vector attributes to disk for _queries_ if somewhat higher latency can be tolerated, it does not allow a large vector index to be built at reasonable speed: To create a high quality index, each vector insert must make many distance calculations, which results in low write throughput when the vectors in the index do not reside in RAM.

To build vector indexes larger than available memory efficiently the procedure described here can be used. This is suitable when:

- You want to build an index for vector retrieval (not just store the vectors for ranking/brute force NN), with a vector data set that doesn't fit in memory across the content nodes you want to deploy for it.
- The vector data in question is mostly write-once (frequent writes to other fields is fine), and rescaling of the content cluster will not be necessary.

## Steps

1. Declare the vector field(s) to be indexed as `paged`.

2. Calculate how much data you can fit in memory:

3. Create one document type per data subset which fits in memory under the calculation above.

4. Add all the subtypes to the content cluster you want in services.xml:
```
<content id="myClusterId" version="1.0">
        <documents>
            <document type="docs2021" mode="index" />
            <document type="docs2022" mode="index" />
            ...
        </documents>
```
5. Feed each of the types completely one by one, without applying queries at the same time.
6. Once all the types are written, you can apply query traffic. Vespa will search across all the types by default, but it is possible to restrict to a subset using the [restrict](../reference/api/query.html#model.restrict) query parameter.

 Copyright © 2026 - [Cookie Preferences](#)

