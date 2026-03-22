# Source: https://crawlee.dev/js/docs/guides/configuration.md

# Configuration

Copy for LLM

​[`Configuration`](https://crawlee.dev/js/api/core/class/Configuration.md) is a class holding Crawlee configuration parameters. By default, you don't need to set or change any of them, but for certain use cases you might want to do so, e.g. in order to change the default storage directory, or enable verbose error logging, and so on.

There are three ways of changing the configuration parameters:

* adding `crawlee.json` file to your project
* setting environment variables
* using the `Configuration` class

You could also combine all the above, but you should keep in mind, that the precedence for these 3 options is the following: ***`crawlee.json`*** < ***constructor options*** < ***environment variables***.

`crawlee.json` is a baseline. The options provided in the `Configuration` constructor will override the options provided in the JSON. Environment variables will override both.

## `crawlee.json`[​](#crawleejson "Direct link to crawleejson")

The first option you could use for configuring Crawlee is `crawlee.json` file. The only thing you need to do is specify the [`ConfigurationOptions`](https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md) in the file, place the file in the root of your project, and Crawlee will use provided options as global configuration.

crawlee.json

```
{
  "persistStateIntervalMillis": 10000,
  "logLevel": "DEBUG"
}
```

With `crawlee.json` you don't need to do anything else in the code:

```
import { CheerioCrawler, sleep } from 'crawlee';
// We are not importing nor passing
// the Configuration to the crawler.
// We are not assigning any env vars either.
const crawler = new CheerioCrawler();

crawler.router.addDefaultHandler(async ({ request }) => {
    // for the first request we wait for 5 seconds,
    // and add the second request to the queue
    if (request.url === 'https://www.example.com/1') {
        await sleep(5_000);
        await crawler.addRequests(['https://www.example.com/2'])
    }
    // for the second request we wait for 10 seconds,
    // and abort the run
    if (request.url === 'https://www.example.com/2') {
        await sleep(10_000);
        process.exit(0);
    }
});

await crawler.run(['https://www.example.com/1']);
```

If you run this example (assuming you placed the `crawlee.json` file with `persistStateIntervalMillis` and `logLevel` specified there in the root of your project), you will find the `SDK_CRAWLER_STATISTICS` file in default Key-Value store, which would show, that there's 1 finished request and crawler runtime was \~10 seconds. This confirms that the state was persisted after 10 seconds, as it was set in `crawlee.json`. Besides, you should see `DEBUG` logs in addition to `INFO` ones in your terminal, as `logLevel` was set to `DEBUG` in the `crawlee.json`, meaning Crawlee picked both provided options correctly.

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Another way of configuring Crawlee is setting environment variables. The following is a list of the environment variables used by Crawlee that are available to the user.

### Important env vars[​](#important-env-vars "Direct link to Important env vars")

The following environment variables have large impact on the way Crawlee works and its behavior can be changed significantly by setting or unsetting them.

#### `CRAWLEE_STORAGE_DIR`[​](#crawlee_storage_dir "Direct link to crawlee_storage_dir")

Defines the path to a local directory where [`KeyValueStore`](https://crawlee.dev/js/api/core/class/KeyValueStore.md), [`Dataset`](https://crawlee.dev/js/api/core/class/Dataset.md), and [`RequestQueue`](https://crawlee.dev/js/api/core/class/RequestQueue.md) store their data. By default, it is set to `./storage`.

#### `CRAWLEE_DEFAULT_DATASET_ID`[​](#crawlee_default_dataset_id "Direct link to crawlee_default_dataset_id")

The default dataset has ID `default`. Setting this environment variable overrides the default dataset ID with the provided value.

#### `CRAWLEE_DEFAULT_KEY_VALUE_STORE_ID`[​](#crawlee_default_key_value_store_id "Direct link to crawlee_default_key_value_store_id")

The default key-value store has ID `default`. Setting this environment variable overrides the default key-value store ID with the provided value.

#### `CRAWLEE_DEFAULT_REQUEST_QUEUE_ID`[​](#crawlee_default_request_queue_id "Direct link to crawlee_default_request_queue_id")

The default request queue has ID `default`. Setting this environment variable overrides the default request queue ID with the provided value.

#### `CRAWLEE_PURGE_ON_START`[​](#crawlee_purge_on_start "Direct link to crawlee_purge_on_start")

Storage directories are purged by default. If set to `false` - local storage directories would not be purged automatically at the start of the crawler run or before opening of some storage explicitly (e.g. via `Dataset.open()`). Useful if we're trying e.g. to add more items to dataset with each next run (and keep the previously saved/scraped items).

#### `CRAWLEE_CONTAINERIZED`[​](#crawlee_containerized "Direct link to crawlee_containerized")

This variable is only effective when the systemInfoV2 experiment is enabled. Changes how crawlee measures its CPU and Memory usage and limits. If unset, crawlee will determine if it is containerised using common features of containerized environments using the `isContainerized` utility function.

* A file at `/.dockerenv`.
* A file at `/proc/self/cgroup` containing `docker`.
* A value for the `KUBERNETES_SERVICE_HOST` environment variable. If `isLambda` returns true, `isContainerized` will return false regardless of these other checks.

When this variable is set, it is used in place of `isContainerized`.

### Convenience env vars[​](#convenience-env-vars "Direct link to Convenience env vars")

The next group includes env vars that can help achieve certain goals without having to change our code, such as temporarily switching log level to DEBUG or enabling verbose logging for errors.

#### `CRAWLEE_HEADLESS`[​](#crawlee_headless "Direct link to crawlee_headless")

If set to `1`, web browsers launched by Crawlee will run in the headless mode. We can still override this setting in the code, e.g. by passing the `headless: true` option to the [`launchPuppeteer()`](https://crawlee.dev/js/api/puppeteer-crawler/function/launchPuppeteer.md) function. By default, the browsers are launched in headful mode, i.e. with windows.

#### `CRAWLEE_LOG_LEVEL`[​](#crawlee_log_level "Direct link to crawlee_log_level")

Specifies the minimum log level, which can be one of the following values (in order of severity): `DEBUG`, `INFO`, `WARNING`, `ERROR` and `OFF`. By default, the log level is set to `INFO`, which means that `DEBUG` messages are not printed to console. See the [`utils.log`](https://crawlee.dev/js/api/core/class/Log.md) namespace for logging utilities.

#### `CRAWLEE_VERBOSE_LOG`[​](#crawlee_verbose_log "Direct link to crawlee_verbose_log")

Enables verbose logging if set to `true`. If not explicitly set to `true` - for errors thrown from inside request handler a warning with only error message will be logged as long as we know the request will be retried. Same applies to some known errors (such as timeout errors). Disabled by default.

#### `CRAWLEE_MEMORY_MBYTES`[​](#crawlee_memory_mbytes "Direct link to crawlee_memory_mbytes")

Sets the amount of system memory in megabytes to be used by the [`AutoscaledPool`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md). It is used to limit the number of concurrently running tasks. By default, the max amount of memory to be used is set to one quarter of total system memory, i.e. on a system with 8192 MB of memory, the autoscaling feature will only use up to 2048 MB of memory.

## Configuration class[​](#configuration-class "Direct link to Configuration class")

The last option to adjust Crawlee configuration is to use the [`Configuration`](https://crawlee.dev/js/api/core/class/Configuration.md) class in the code.

### Global Configuration[​](#global-configuration "Direct link to Global Configuration")

By default, there is a global singleton instance of `Configuration` class, it is used by the crawlers and some other classes that depend on a configurable behavior. In most cases you don't need to adjust any options there, but if needed - you can get access to it via [`Configuration.getGlobalConfig()`](https://crawlee.dev/js/api/core/class/Configuration.md#getGlobalConfig) function. Now you can easily [`get`](https://crawlee.dev/js/api/core/class/Configuration.md#get) and [`set`](https://crawlee.dev/js/api/core/class/Configuration.md#set) the [`ConfigurationOptions`](https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md).

```
import { CheerioCrawler, Configuration, sleep } from 'crawlee';

// Get the global configuration
const config = Configuration.getGlobalConfig();
// Set the 'persistStateIntervalMillis' option
// of global configuration to 10 seconds
config.set('persistStateIntervalMillis', 10_000);

// Note, that we are not passing the configuration to the crawler
// as it's using the global configuration
const crawler = new CheerioCrawler();

crawler.router.addDefaultHandler(async ({ request }) => {
    // For the first request we wait for 5 seconds,
    // and add the second request to the queue
    if (request.url === 'https://www.example.com/1') {
        await sleep(5_000);
        await crawler.addRequests(['https://www.example.com/2'])
    }
    // For the second request we wait for 10 seconds,
    // and abort the run
    if (request.url === 'https://www.example.com/2') {
        await sleep(10_000);
        process.exit(0);
    }
});

await crawler.run(['https://www.example.com/1']);
```

This is pretty much the same example we used for showing `crawlee.json` usage, but now we're using the global configuration, which is the only difference. If you run this example - you will find the `SDK_CRAWLER_STATISTICS` file in default Key-Value store as before, which would show the same number of finishes requests (one) and the same crawler runtime (\~10 seconds). This confirms that provided parameters worked: the state was persisted after 10 seconds, as it was set in the global configuration.

note

After running the same example with commented two lines of code related to `Configuration` there will be no `SDK_CRAWLER_STATISTICS` file stored in the default Key-Value store: as we did not change the `persistStateIntervalMillis`, Crawlee used the default value of 60 seconds, and the crawler was forcefully aborted after \~15 seconds of run time before it persisted the state for the first time.

### Custom configuration[​](#custom-configuration "Direct link to Custom configuration")

Alternatively, you can create a custom configuration. In this case you need to pass it to the class that is going to use it, e.g. to the crawler. Let's adjust the previous example:

```
import { CheerioCrawler, Configuration, sleep } from 'crawlee';

// Create new configuration
const config = new Configuration({
    // Set the 'persistStateIntervalMillis' option to 10 seconds
    persistStateIntervalMillis: 10_000,
});

// Now we need to pass the configuration to the crawler
const crawler = new CheerioCrawler({}, config);

crawler.router.addDefaultHandler(async ({ request }) => {
    // for the first request we wait for 5 seconds,
    // and add the second request to the queue
    if (request.url === 'https://www.example.com/1') {
        await sleep(5_000);
        await crawler.addRequests(['https://www.example.com/2'])
    }
    // for the second request we wait for 10 seconds,
    // and abort the run
    if (request.url === 'https://www.example.com/2') {
        await sleep(10_000);
        process.exit(0);
    }
});

await crawler.run(['https://www.example.com/1']);
```

If you run this example - it would work exactly the same as before, with the same `SDK_CRAWLER_STATISTICS` file in default Key-Value store after the run, showing the same number of finished requests and the same crawler run time.

note

If you would not pass the configuration to the crawler, there again will be no `SDK_CRAWLER_STATISTICS` file stored in the default Key-Value store, this time for a different reason though. Since we did not pass the configuration to the crawler, the crawler will use the global configuration, which is using the default `persistStateIntervalMillis`. So again, the run was aborted before the state was persisted for the first time.
