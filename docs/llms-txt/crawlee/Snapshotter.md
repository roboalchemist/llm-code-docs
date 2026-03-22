# Source: https://crawlee.dev/js/api/core/class/Snapshotter.md

# Snapshotter<!-- -->

Creates snapshots of system resources at given intervals and marks the resource as either overloaded or not during the last interval. Keeps a history of the snapshots. It tracks the following resources: Memory, EventLoop, API and CPU. The class is used by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class.

When running on the Apify platform, the CPU and memory statistics are provided by the platform, as collected from the running Docker container. When running locally, `Snapshotter` makes its own statistics by querying the OS.

CPU becomes overloaded locally when its current use exceeds the `maxUsedCpuRatio` option or when Apify platform marks it as overloaded.

Memory becomes overloaded if its current use exceeds the `maxUsedMemoryRatio` option. It's computed using the total memory available to the container when running on the Apify platform and a quarter of total system memory when running locally. Max total memory when running locally may be overridden by using the `CRAWLEE_MEMORY_MBYTES` environment variable.

Event loop becomes overloaded if it slows down by more than the `maxBlockedMillis` option.

Client becomes overloaded when rate limit errors (429 - Too Many Requests), typically received from the request queue, exceed the set limit within the set interval.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**client](#client)
* [**clientInterval](#clientInterval)
* [**clientSnapshotIntervalMillis](#clientSnapshotIntervalMillis)
* [**clientSnapshots](#clientSnapshots)
* [**config](#config)
* [**cpuSnapshots](#cpuSnapshots)
* [**eventLoopInterval](#eventLoopInterval)
* [**eventLoopSnapshotIntervalMillis](#eventLoopSnapshotIntervalMillis)
* [**eventLoopSnapshots](#eventLoopSnapshots)
* [**events](#events)
* [**lastLoggedCriticalMemoryOverloadAt](#lastLoggedCriticalMemoryOverloadAt)
* [**log](#log)
* [**maxBlockedMillis](#maxBlockedMillis)
* [**maxClientErrors](#maxClientErrors)
* [**maxMemoryBytes](#maxMemoryBytes)
* [**maxUsedMemoryRatio](#maxUsedMemoryRatio)
* [**memorySnapshots](#memorySnapshots)
* [**snapshotHistoryMillis](#snapshotHistoryMillis)

### Methods

* [**getClientSample](#getClientSample)
* [**getCpuSample](#getCpuSample)
* [**getEventLoopSample](#getEventLoopSample)
* [**getMemorySample](#getMemorySample)
* [**start](#start)
* [**stop](#stop)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L144)constructor

* ****new Snapshotter**(options): [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md)

- #### Parameters

  * ##### optionaloptions: [SnapshotterOptions](https://crawlee.dev/js/api/core/interface/SnapshotterOptions.md) = <!-- -->{}

    All `Snapshotter` configuration options.

  #### Returns [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md)

## Properties<!-- -->[**](#Properties)

### [**](#client)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L120)client

**client: [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

### [**](#clientInterval)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L137)clientInterval

**clientInterval: BetterIntervalID =

<!-- -->

...

### [**](#clientSnapshotIntervalMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L124)clientSnapshotIntervalMillis

**clientSnapshotIntervalMillis: number

### [**](#clientSnapshots)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L134)clientSnapshots

**clientSnapshots: ClientSnapshot\[] =

<!-- -->

\[]

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L121)config

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

### [**](#cpuSnapshots)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L131)cpuSnapshots

**cpuSnapshots: CpuSnapshot\[] =

<!-- -->

\[]

### [**](#eventLoopInterval)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L136)eventLoopInterval

**eventLoopInterval: BetterIntervalID =

<!-- -->

...

### [**](#eventLoopSnapshotIntervalMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L123)eventLoopSnapshotIntervalMillis

**eventLoopSnapshotIntervalMillis: number

### [**](#eventLoopSnapshots)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L132)eventLoopSnapshots

**eventLoopSnapshots: EventLoopSnapshot\[] =

<!-- -->

\[]

### [**](#events)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L122)events

**events: [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

### [**](#lastLoggedCriticalMemoryOverloadAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L139)lastLoggedCriticalMemoryOverloadAt

**lastLoggedCriticalMemoryOverloadAt: null | Date =

<!-- -->

null

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L119)log

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

### [**](#maxBlockedMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L126)maxBlockedMillis

**maxBlockedMillis: number

### [**](#maxClientErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L128)maxClientErrors

**maxClientErrors: number

### [**](#maxMemoryBytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L129)maxMemoryBytes

**maxMemoryBytes: number

### [**](#maxUsedMemoryRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L127)maxUsedMemoryRatio

**maxUsedMemoryRatio: number

### [**](#memorySnapshots)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L133)memorySnapshots

**memorySnapshots: MemorySnapshot\[] =

<!-- -->

\[]

### [**](#snapshotHistoryMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L125)snapshotHistoryMillis

**snapshotHistoryMillis: number

## Methods<!-- -->[**](#Methods)

### [**](#getClientSample)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L268)getClientSample

* ****getClientSample**(sampleDurationMillis): ClientSnapshot\[]

- Returns a sample of latest Client snapshots, with the size of the sample defined by the sampleDurationMillis parameter. If omitted, it returns a full snapshot history.

  ***

  #### Parameters

  * ##### optionalsampleDurationMillis: number

  #### Returns ClientSnapshot\[]

### [**](#getCpuSample)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L260)getCpuSample

* ****getCpuSample**(sampleDurationMillis): CpuSnapshot\[]

- Returns a sample of latest CPU snapshots, with the size of the sample defined by the sampleDurationMillis parameter. If omitted, it returns a full snapshot history.

  ***

  #### Parameters

  * ##### optionalsampleDurationMillis: number

  #### Returns CpuSnapshot\[]

### [**](#getEventLoopSample)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L252)getEventLoopSample

* ****getEventLoopSample**(sampleDurationMillis): EventLoopSnapshot\[]

- Returns a sample of latest event loop snapshots, with the size of the sample defined by the sampleDurationMillis parameter. If omitted, it returns a full snapshot history.

  ***

  #### Parameters

  * ##### optionalsampleDurationMillis: number

  #### Returns EventLoopSnapshot\[]

### [**](#getMemorySample)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L244)getMemorySample

* ****getMemorySample**(sampleDurationMillis): MemorySnapshot\[]

- Returns a sample of latest memory snapshots, with the size of the sample defined by the sampleDurationMillis parameter. If omitted, it returns a full snapshot history.

  ***

  #### Parameters

  * ##### optionalsampleDurationMillis: number

  #### Returns MemorySnapshot\[]

### [**](#start)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L192)start

* ****start**(): Promise\<void>

- Starts capturing snapshots at configured intervals.

  ***

  #### Returns Promise\<void>

### [**](#stop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L229)stop

* ****stop**(): Promise\<void>

- Stops all resource capturing.

  ***

  #### Returns Promise\<void>
