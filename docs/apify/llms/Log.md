# Source: https://docs.apify.com/sdk/js/reference/class/Log.md

# externalLog<!-- -->

The log instance enables level aware logging of messages and we advise to use it instead of `console.log()` and its aliases in most development scenarios.

A very useful use case for `log` is using `log.debug` liberally throughout the codebase to get useful logging messages only when appropriate log level is set and keeping the console tidy in production environments.

The available logging levels are, in this order: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `OFF` and can be referenced from the `log.LEVELS` constant, such as `log.LEVELS.ERROR`.

To log messages to the system console, use the `log.level(message)` invocation, such as `log.debug('this is a debug message')`.

To prevent writing of messages above a certain log level to the console, simply set the appropriate level. The default log level is `INFO`, which means that `DEBUG` messages will not be printed, unless enabled.

**Example:**

```
import log from '@apify/log';

// importing from the Apify SDK or Crawlee is also supported:
// import { log } from 'apify';
// import { log } from 'crawlee';

log.info('Information message', { someData: 123 }); // prints message
log.debug('Debug message', { debugData: 'hello' }); // doesn't print anything

log.setLevel(log.LEVELS.DEBUG);
log.debug('Debug message'); // prints message

log.setLevel(log.LEVELS.ERROR);
log.debug('Debug message'); // doesn't print anything
log.info('Info message'); // doesn't print anything
log.error('Error message', { errorDetails: 'This is bad!' }); // prints message

try {
  throw new Error('Not good!');
} catch (e) {
  log.exception(e, 'Exception occurred', { errorDetails: 'This is really bad!' }); // prints message
}

log.setOptions({ prefix: 'My actor' });
log.info('I am running!'); // prints "My actor: I am running"

const childLog = log.child({ prefix: 'Crawler' });
log.info('I am crawling!'); // prints "My actor:Crawler: I am crawling"
```

Another very useful way of setting the log level is by setting the `APIFY_LOG_LEVEL` environment variable, such as `APIFY_LOG_LEVEL=DEBUG`. This way, no code changes are necessary to turn on your debug messages and start debugging right away.

To add timestamps to your logs, you can override the default logger settings:

```
log.setOptions({
    logger: new log.LoggerText({ skipTime: false }),
});
```

You can customize your logging further by extending or replacing the default logger instances with your own implementations.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**LEVELS](#LEVELS)

### Methods

* [**debug](#debug)
* [**deprecated](#deprecated)
* [**error](#error)
* [**exception](#exception)
* [**getLevel](#getLevel)
* [**getOptions](#getOptions)
* [**child](#child)
* [**info](#info)
* [**internal](#internal)
* [**perf](#perf)
* [**setLevel](#setLevel)
* [**setOptions](#setOptions)
* [**softFail](#softFail)
* [**warning](#warning)
* [**warningOnce](#warningOnce)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L136)externalconstructor

* ****new Log**(options): [Log](https://docs.apify.com/sdk/js/sdk/js/reference/class/Log.md)

- #### Parameters

  * ##### externaloptionaloptions: Partial<[LoggerOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/LoggerOptions.md)>

  #### Returns [Log](https://docs.apify.com/sdk/js/sdk/js/reference/class/Log.md)

## Properties<!-- -->[**](#Properties)

### [**](#LEVELS)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L133)externalreadonlyLEVELS

**LEVELS: typeof [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md)

Map of available log levels that's useful for easy setting of appropriate log levels. Each log level is represented internally by a number. Eg. `log.LEVELS.DEBUG === 5`.

## Methods<!-- -->[**](#Methods)

### [**](#debug)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L195)externaldebug

* ****debug**(message, data): void

- Logs a `DEBUG` message. By default, it will not be written to the console. To see `DEBUG` messages in the console, set the log level to `DEBUG` either using the `log.setLevel(log.LEVELS.DEBUG)` method or using the environment variable `APIFY_LOG_LEVEL=DEBUG`. Data are stringified and appended to the message.

  ***

  #### Parameters

  * ##### externalmessage: string
  * ##### externaloptionaldata: AdditionalData

  #### Returns void

### [**](#deprecated)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L204)externaldeprecated

* ****deprecated**(message): void

- Logs given message only once as WARNING. It's used to warn user that some feature he is using has been deprecated.

  ***

  #### Parameters

  * ##### externalmessage: string

  #### Returns void

### [**](#error)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L173)externalerror

* ****error**(message, data): void

- Logs an `ERROR` message. Use this method to log error messages that are not directly connected to an exception. For logging exceptions, use the `log.exception` method.

  ***

  #### Parameters

  * ##### externalmessage: string
  * ##### externaloptionaldata: AdditionalData

  #### Returns void

### [**](#exception)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L178)externalexception

* ****exception**(exception, message, data): void

- Logs an `ERROR` level message with a nicely formatted exception. Note that the exception is the first parameter here and an additional message is only optional.

  ***

  #### Parameters

  * ##### externalexception: Error
  * ##### externalmessage: string
  * ##### externaloptionaldata: AdditionalData

  #### Returns void

### [**](#getLevel)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L144)externalgetLevel

* ****getLevel**(): number

- Returns the currently selected logging level. This is useful for checking whether a message will actually be printed to the console before one actually performs a resource intensive operation to construct the message, such as querying a DB for some metadata that need to be added. If the log level is not high enough at the moment, it doesn't make sense to execute the query.

  ***

  #### Returns number

### [**](#getOptions)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L164)externalgetOptions

* ****getOptions**(): Required<[LoggerOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/LoggerOptions.md)>

- Returns the logger configuration.

  ***

  #### Returns Required<[LoggerOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/LoggerOptions.md)>

### [**](#child)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L168)externalchild

* ****child**(options): [Log](https://docs.apify.com/sdk/js/sdk/js/reference/class/Log.md)

- Creates a new instance of logger that inherits settings from a parent logger.

  ***

  #### Parameters

  * ##### externaloptions: Partial<[LoggerOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/LoggerOptions.md)>

  #### Returns [Log](https://docs.apify.com/sdk/js/sdk/js/reference/class/Log.md)

### [**](#info)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L188)externalinfo

* ****info**(message, data): void

- Logs an `INFO` message. `INFO` is the default log level so info messages will be always logged, unless the log level is changed. Data are stringified and appended to the message.

  ***

  #### Parameters

  * ##### externalmessage: string
  * ##### externaloptionaldata: AdditionalData

  #### Returns void

### [**](#internal)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L156)externalinternal

* ****internal**(level, message, data, exception): void

- #### Parameters

  * ##### externallevel: [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md)
  * ##### externalmessage: string
  * ##### externaloptionaldata: any
  * ##### externaloptionalexception: any

  #### Returns void

### [**](#perf)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L196)externalperf

* ****perf**(message, data): void

- #### Parameters

  * ##### externalmessage: string
  * ##### externaloptionaldata: AdditionalData

  #### Returns void

### [**](#setLevel)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L155)externalsetLevel

* ****setLevel**(level): void

- Sets the log level to the given value, preventing messages from less important log levels from being printed to the console. Use in conjunction with the `log.LEVELS` constants such as

  ```
  log.setLevel(log.LEVELS.DEBUG);
  ```

  Default log level is INFO.

  ***

  #### Parameters

  * ##### externallevel: [LogLevel](https://docs.apify.com/sdk/js/sdk/js/reference/enum/LogLevel.md)

  #### Returns void

### [**](#setOptions)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L160)externalsetOptions

* ****setOptions**(options): void

- Configures logger.

  ***

  #### Parameters

  * ##### externaloptions: Partial<[LoggerOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/LoggerOptions.md)>

  #### Returns void

### [**](#softFail)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L179)externalsoftFail

* ****softFail**(message, data): void

- #### Parameters

  * ##### externalmessage: string
  * ##### externaloptionaldata: AdditionalData

  #### Returns void

### [**](#warning)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L183)externalwarning

* ****warning**(message, data): void

- Logs a `WARNING` level message. Data are stringified and appended to the message.

  ***

  #### Parameters

  * ##### externalmessage: string
  * ##### externaloptionaldata: AdditionalData

  #### Returns void

### [**](#warningOnce)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@apify/log/src/index.d.ts#L200)externalwarningOnce

* ****warningOnce**(message): void

- Logs a `WARNING` level message only once.

  ***

  #### Parameters

  * ##### externalmessage: string

  #### Returns void
