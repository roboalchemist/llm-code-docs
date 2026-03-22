# Source: https://crawlee.dev/js/api/core/interface/SystemInfo.md

# SystemInfo<!-- -->

Represents the current status of the system.

## Index[**](#Index)

### Properties

* [**clientInfo](#clientInfo)
* [**cpuInfo](#cpuInfo)
* [**eventLoopInfo](#eventLoopInfo)
* [**isSystemIdle](#isSystemIdle)
* [**memCurrentBytes](#memCurrentBytes)
* [**memInfo](#memInfo)

## Properties<!-- -->[**](#Properties)

### [**](#clientInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L16)clientInfo

**clientInfo: [ClientInfo](https://crawlee.dev/js/api/core/interface/ClientInfo.md)

### [**](#cpuInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L15)cpuInfo

**cpuInfo: [ClientInfo](https://crawlee.dev/js/api/core/interface/ClientInfo.md)

### [**](#eventLoopInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L14)eventLoopInfo

**eventLoopInfo: [ClientInfo](https://crawlee.dev/js/api/core/interface/ClientInfo.md)

### [**](#isSystemIdle)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L12)isSystemIdle

**isSystemIdle: boolean

If false, system is being overloaded.

### [**](#memCurrentBytes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L17)optionalmemCurrentBytes

**memCurrentBytes?

<!-- -->

: number

### [**](#memInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L13)memInfo

**memInfo: [ClientInfo](https://crawlee.dev/js/api/core/interface/ClientInfo.md)
