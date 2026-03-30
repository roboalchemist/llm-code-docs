# Source: https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md

# AutoscaledPoolOptions<!-- -->

## Index[**](#Index)

### Properties

* [**autoscaleIntervalSecs](#autoscaleIntervalSecs)
* [**desiredConcurrency](#desiredConcurrency)
* [**desiredConcurrencyRatio](#desiredConcurrencyRatio)
* [**isFinishedFunction](#isFinishedFunction)
* [**isTaskReadyFunction](#isTaskReadyFunction)
* [**log](#log)
* [**loggingIntervalSecs](#loggingIntervalSecs)
* [**maxConcurrency](#maxConcurrency)
* [**maxTasksPerMinute](#maxTasksPerMinute)
* [**maybeRunIntervalSecs](#maybeRunIntervalSecs)
* [**minConcurrency](#minConcurrency)
* [**runTaskFunction](#runTaskFunction)
* [**scaleDownStepRatio](#scaleDownStepRatio)
* [**scaleUpStepRatio](#scaleUpStepRatio)
* [**snapshotterOptions](#snapshotterOptions)
* [**systemStatusOptions](#systemStatusOptions)
* [**taskTimeoutSecs](#taskTimeoutSecs)

## Properties<!-- -->[**](#Properties)

### [**](#autoscaleIntervalSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L102)optionalautoscaleIntervalSecs

**autoscaleIntervalSecs?

<!-- -->

: number = 10

Defines in seconds how often the pool should attempt to adjust the desired concurrency based on the latest system status. Setting it lower than 1 might have a severe impact on performance. We suggest using a value from 5 to 20.

### [**](#desiredConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L60)optionaldesiredConcurrency

**desiredConcurrency?

<!-- -->

: number

The desired number of tasks that should be running parallel on the start of the pool, if there is a large enough supply of them. By default, it is `minConcurrency`.

### [**](#desiredConcurrencyRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L66)optionaldesiredConcurrencyRatio

**desiredConcurrencyRatio?

<!-- -->

: number = 0.90

Minimum level of desired concurrency to reach before more scaling up is allowed.

### [**](#isFinishedFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L38)optionalisFinishedFunction

**isFinishedFunction?

<!-- -->

: () => Promise\<boolean>

A function that is called only when there are no tasks to be processed. If it resolves to `true` then the pool's run finishes. Being called only when there are no tasks being processed means that as long as `isTaskReadyFunction()` keeps resolving to `true`, `isFinishedFunction()` will never be called. To abort a run, use the [AutoscaledPool.abort](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#abort) method.

***

#### Type declaration

* * **(): Promise\<boolean>

  - #### Returns Promise\<boolean>

### [**](#isTaskReadyFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L29)optionalisTaskReadyFunction

**isTaskReadyFunction?

<!-- -->

: () => Promise\<boolean>

A function that indicates whether `runTaskFunction` should be called. This function is called every time there is free capacity for a new task and it should indicate whether it should start a new task or not by resolving to either `true` or `false`. Besides its obvious use, it is also useful for task throttling to save resources.

***

#### Type declaration

* * **(): Promise\<boolean>

  - #### Returns Promise\<boolean>

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L129)optionallog

**log?

<!-- -->

: [Log](https://crawlee.dev/js/api/core/class/Log.md)

### [**](#loggingIntervalSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L94)optionalloggingIntervalSecs

**loggingIntervalSecs?

<!-- -->

: null | number = null | number

Specifies a period in which the instance logs its state, in seconds. Set to `null` to disable periodic logging.

### [**](#maxConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L53)optionalmaxConcurrency

**maxConcurrency?

<!-- -->

: number = 200

The maximum number of tasks running in parallel.

### [**](#maxTasksPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L127)optionalmaxTasksPerMinute

**maxTasksPerMinute?

<!-- -->

: number

The maximum number of tasks per minute the pool can run. By default, this is set to `Infinity`, but you can pass any positive, non-zero integer.

### [**](#maybeRunIntervalSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L87)optionalmaybeRunIntervalSecs

**maybeRunIntervalSecs?

<!-- -->

: number = 0.5

Indicates how often the pool should call the `runTaskFunction()` to start a new task, in seconds. This has no effect on starting new tasks immediately after a task completes.

### [**](#minConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L47)optionalminConcurrency

**minConcurrency?

<!-- -->

: number = 1

The minimum number of tasks running in parallel.

*WARNING:* If you set this value too high with respect to the available system memory and CPU, your code might run extremely slow or crash. If you're not sure, just keep the default value and the concurrency will scale up automatically.

### [**](#runTaskFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L21)optionalrunTaskFunction

**runTaskFunction?

<!-- -->

: () => Promise\<unknown>

A function that performs an asynchronous resource-intensive task. The function must either be labeled `async` or return a promise.

***

#### Type declaration

* * **(): Promise\<unknown>

  - #### Returns Promise\<unknown>

### [**](#scaleDownStepRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L80)optionalscaleDownStepRatio

**scaleDownStepRatio?

<!-- -->

: number = 0.05

Defines the amount of desired concurrency to be subtracted with each scaling down. The minimum scaling step is one.

### [**](#scaleUpStepRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L73)optionalscaleUpStepRatio

**scaleUpStepRatio?

<!-- -->

: number = 0.05

Defines the fractional amount of desired concurrency to be added with each scaling up. The minimum scaling step is one.

### [**](#snapshotterOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L114)optionalsnapshotterOptions

**snapshotterOptions?

<!-- -->

: [SnapshotterOptions](https://crawlee.dev/js/api/core/interface/SnapshotterOptions.md)

Options to be passed down to the [Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md) constructor. This is useful for fine-tuning the snapshot intervals and history.

### [**](#systemStatusOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L121)optionalsystemStatusOptions

**systemStatusOptions?

<!-- -->

: [SystemStatusOptions](https://crawlee.dev/js/api/core/interface/SystemStatusOptions.md)

Options to be passed down to the [SystemStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md) constructor. This is useful for fine-tuning the system status reports. If a custom snapshotter is set in the options, it will be used by the pool.

### [**](#taskTimeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L108)optionaltaskTimeoutSecs

**taskTimeoutSecs?

<!-- -->

: number = 0

Timeout in which the `runTaskFunction` needs to finish, given in seconds.
