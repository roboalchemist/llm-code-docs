# Source: https://crawlee.dev/js/api/core/class/SystemStatus.md

# SystemStatus<!-- -->

Provides a simple interface to reading system status from a [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md) instance. It only exposes two functions [SystemStatus.getCurrentStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md#getCurrentStatus) and [SystemStatus.getHistoricalStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md#getHistoricalStatus). The system status is calculated using a weighted average of overloaded messages in the snapshots, with the weights being the time intervals between the snapshots. Each resource is calculated separately and the system is overloaded whenever at least one resource is overloaded. The class is used by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class.

[SystemStatus.getCurrentStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md#getCurrentStatus) returns a boolean that represents the current status of the system. The length of the current timeframe in seconds is configurable by the `currentHistorySecs` option and represents the max age of snapshots to be considered for the calculation.

[SystemStatus.getHistoricalStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md#getHistoricalStatus) returns a boolean that represents the long-term status of the system. It considers the full snapshot history available in the [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md) instance.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**getCurrentStatus](#getCurrentStatus)
* [**getHistoricalStatus](#getHistoricalStatus)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L128)constructor

* ****new SystemStatus**(options): [SystemStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md)

- #### Parameters

  * ##### options: [SystemStatusOptions](https://crawlee.dev/js/api/core/interface/SystemStatusOptions.md) = <!-- -->{}

  #### Returns [SystemStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md)

## Methods<!-- -->[**](#Methods)

### [**](#getCurrentStatus)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L176)getCurrentStatus

* ****getCurrentStatus**(): [SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md)

- Returns an [SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md) object with the following structure:

  ```
  {
      isSystemIdle: Boolean,
      memInfo: Object,
      eventLoopInfo: Object,
      cpuInfo: Object
  }
  ```

  Where the `isSystemIdle` property is set to `false` if the system has been overloaded in the last `options.currentHistorySecs` seconds, and `true` otherwise.

  ***

  #### Returns [SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md)

### [**](#getHistoricalStatus)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L196)getHistoricalStatus

* ****getHistoricalStatus**(): [SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md)

- Returns an [SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md) object with the following structure:

  ```
  {
      isSystemIdle: Boolean,
      memInfo: Object,
      eventLoopInfo: Object,
      cpuInfo: Object
  }
  ```

  Where the `isSystemIdle` property is set to `false` if the system has been overloaded in the full history of the [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md) (which is configurable in the [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md)) and `true` otherwise.

  ***

  #### Returns [SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md)
