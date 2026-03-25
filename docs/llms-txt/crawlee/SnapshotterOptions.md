# Source: https://crawlee.dev/js/api/core/interface/SnapshotterOptions.md

# SnapshotterOptions<!-- -->

## Index[**](#Index)

### Properties

* [**clientSnapshotIntervalSecs](#clientSnapshotIntervalSecs)
* [**eventLoopSnapshotIntervalSecs](#eventLoopSnapshotIntervalSecs)
* [**maxBlockedMillis](#maxBlockedMillis)
* [**maxClientErrors](#maxClientErrors)
* [**maxUsedMemoryRatio](#maxUsedMemoryRatio)
* [**snapshotHistorySecs](#snapshotHistorySecs)

## Properties<!-- -->[**](#Properties)

### [**](#clientSnapshotIntervalSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L31)optionalclientSnapshotIntervalSecs

**clientSnapshotIntervalSecs?

<!-- -->

: number = 1

Defines the interval of checking the current state of the remote API client.

### [**](#eventLoopSnapshotIntervalSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L24)optionaleventLoopSnapshotIntervalSecs

**eventLoopSnapshotIntervalSecs?

<!-- -->

: number = 0.5

Defines the interval of measuring the event loop response time.

### [**](#maxBlockedMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L38)optionalmaxBlockedMillis

**maxBlockedMillis?

<!-- -->

: number = 50

Maximum allowed delay of the event loop in milliseconds. Exceeding this limit overloads the event loop.

### [**](#maxClientErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L52)optionalmaxClientErrors

**maxClientErrors?

<!-- -->

: number = 1

Defines the maximum number of new rate limit errors within the given interval.

### [**](#maxUsedMemoryRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L45)optionalmaxUsedMemoryRatio

**maxUsedMemoryRatio?

<!-- -->

: number = 0.9

Defines the maximum ratio of total memory that can be used. Exceeding this limit overloads the memory.

### [**](#snapshotHistorySecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L59)optionalsnapshotHistorySecs

**snapshotHistorySecs?

<!-- -->

: number = 60

Sets the interval in seconds for which a history of resource snapshots will be kept. Increasing this to very high numbers will affect performance.
