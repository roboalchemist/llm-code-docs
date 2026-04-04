# Source: https://crawlee.dev/js/api/core/interface/SystemStatusOptions.md

# SystemStatusOptions<!-- -->

## Index[**](#Index)

### Properties

* [**currentHistorySecs](#currentHistorySecs)
* [**maxClientOverloadedRatio](#maxClientOverloadedRatio)
* [**maxCpuOverloadedRatio](#maxCpuOverloadedRatio)
* [**maxEventLoopOverloadedRatio](#maxEventLoopOverloadedRatio)
* [**maxMemoryOverloadedRatio](#maxMemoryOverloadedRatio)
* [**snapshotter](#snapshotter)

## Properties<!-- -->[**](#Properties)

### [**](#currentHistorySecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L40)optionalcurrentHistorySecs

**currentHistorySecs?

<!-- -->

: number = 5

Defines max age of snapshots used in the [SystemStatus.getCurrentStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md#getCurrentStatus) measurement.

### [**](#maxClientOverloadedRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L68)optionalmaxClientOverloadedRatio

**maxClientOverloadedRatio?

<!-- -->

: number = 0.3

Sets the maximum ratio of overloaded snapshots in a Client sample. If the sample exceeds this ratio, the system will be overloaded.

### [**](#maxCpuOverloadedRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L61)optionalmaxCpuOverloadedRatio

**maxCpuOverloadedRatio?

<!-- -->

: number = 0.4

Sets the maximum ratio of overloaded snapshots in a CPU sample. If the sample exceeds this ratio, the system will be overloaded.

### [**](#maxEventLoopOverloadedRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L54)optionalmaxEventLoopOverloadedRatio

**maxEventLoopOverloadedRatio?

<!-- -->

: number = 0.6

Sets the maximum ratio of overloaded snapshots in an event loop sample. If the sample exceeds this ratio, the system will be overloaded.

### [**](#maxMemoryOverloadedRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L47)optionalmaxMemoryOverloadedRatio

**maxMemoryOverloadedRatio?

<!-- -->

: number = 0.2

Sets the maximum ratio of overloaded snapshots in a memory sample. If the sample exceeds this ratio, the system will be overloaded.

### [**](#snapshotter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L73)optionalsnapshotter

**snapshotter?

<!-- -->

: [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md)

The `Snapshotter` instance to be queried for `SystemStatus`.
