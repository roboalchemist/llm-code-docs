# Source: https://docs.pinot.apache.org/release-1.1.0/reference/single-stage-engine.md

# Source: https://docs.pinot.apache.org/release-1.2.0/reference/single-stage-engine.md

# Source: https://docs.pinot.apache.org/release-1.3.0/reference/single-stage-engine.md

# Source: https://docs.pinot.apache.org/release-1.4.0/reference/single-stage-engine.md

# Source: https://docs.pinot.apache.org/reference/single-stage-engine.md

# Single-stage query engine (v1)

The Pinot single-stage query engine (also known as v1 query engine) uses a scatter-gather query engine model, shown in the following diagram. In certain cases, for example, if you need to query using JOINs on large data sets, the [multi-stage query engine (v2)](https://docs.pinot.apache.org/reference/multi-stage-engine) may be a more performant option.

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fmc6OallDsJVAc3J4RMDW%2FMulti-Stage-Pinot-Query-Engine-v1.png?alt=media&#x26;token=dca01607-4eea-4b14-b1ed-9f1aeffffae5" alt=""><figcaption><p>Single-stage query engine (v1)</p></figcaption></figure>
