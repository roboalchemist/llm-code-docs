# Source: https://crawlee.dev/js/api/core/interface/StatisticsOptions.md

# StatisticsOptions<!-- -->

Configuration for the [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md) instance used by the crawler

## Index[**](#Index)

### Properties

* [**config](#config)
* [**keyValueStore](#keyValueStore)
* [**log](#log)
* [**logIntervalSecs](#logIntervalSecs)
* [**logMessage](#logMessage)
* [**persistenceOptions](#persistenceOptions)
* [**saveErrorSnapshots](#saveErrorSnapshots)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L465)optionalconfig

**config?

<!-- -->

: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

Configuration instance to use

### [**](#keyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L459)optionalkeyValueStore

**keyValueStore?

<!-- -->

: [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)

Key value store instance to persist the statistics. If not provided, the default one will be used when capturing starts

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L453)optionallog

**log?

<!-- -->

: [Log](https://crawlee.dev/js/api/core/class/Log.md) = [Log](https://crawlee.dev/js/api/core/class/Log.md)

Parent logger instance, the statistics will create a child logger from this.

### [**](#logIntervalSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L441)optionallogIntervalSecs

**logIntervalSecs?

<!-- -->

: number = 60

Interval in seconds to log the current statistics

### [**](#logMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L447)optionallogMessage

**logMessage?

<!-- -->

: string = ‘Statistics’

Message to log with the current statistics

### [**](#persistenceOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L470)optionalpersistenceOptions

**persistenceOptions?

<!-- -->

: [PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)

Control how and when to persist the statistics.

### [**](#saveErrorSnapshots)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L476)optionalsaveErrorSnapshots

**saveErrorSnapshots?

<!-- -->

: boolean = false

Save HTML snapshot (and a screenshot if possible) when an error occurs.
