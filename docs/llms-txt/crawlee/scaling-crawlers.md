# Source: https://crawlee.dev/js/docs/guides/scaling-crawlers.md

# Scaling our crawlers

Copy for LLM

As we build our crawler, we might want to control how many requests we do to the website at a time. Crawlee provides several options to fine tune how many parallel requests should be made at any time, how many requests should be done per minute, and how should scaling work based on the available system resources.

tip

All of these options are available on all crawlers Crawlee provides, but for this guide we'll be using the [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md). We can see all options that are available [`here`](https://crawlee.dev/js/api/cheerio-crawler/interface/CheerioCrawlerOptions.md).

## `maxRequestsPerMinute`[​](#maxrequestsperminute "Direct link to maxrequestsperminute")

This controls how many total requests can be made per minute. It counts the amount of requests done every second, to ensure there is not a burst of requests at the `maxConcurrency` limit followed by a long period of waiting. By default, it is set to `Infinity` which means the crawler will keep going up to the `maxConcurrency`. We would set this if we wanted our crawler to work at full throughput, but also not keep hitting the website we're crawling with non-stop requests.

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler({
    // Let the crawler know it can run up to 100 requests concurrently at any time
    maxConcurrency: 100,
    // ...but also ensure the crawler never exceeds 250 requests per minute
    maxRequestsPerMinute: 250,
});
```

## `minConcurrency` and `maxConcurrency`[​](#minconcurrency-and-maxconcurrency "Direct link to minconcurrency-and-maxconcurrency")

These control how many parallel requests can be run at any time. By default, crawlers will start with one parallel request at a time and scale up over time to a maximum of 200 requests at a time.

Don't set `minConcurrency` too high!

Setting this option too high compared to the available system resources will make your crawler run extremely slow or might even crash.

It's recommended to leave it at the default value that is provided and letting the crawler scale up and down automatically based on available resources instead.

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler({
    // Start the crawler right away and ensure there will always be 5 concurrent requests ran at any time
    minConcurrency: 5,
    // Ensure the crawler doesn't exceed 15 concurrent requests ran at any time
    maxConcurrency: 15,
});
```

## Advanced options[​](#advanced-options "Direct link to Advanced options")

While the options above should be enough for most users, if we wanted to get super deep into the configuration of the autoscaling pool (the internal utility in Crawlee that helps us allow crawlers to scale up and down), we can do so through the [`autoscaledPoolOptions`](https://crawlee.dev/js/api/cheerio-crawler/interface/CheerioCrawlerOptions.md#autoscaledPoolOptions) object available on crawler options.

Complex options up ahead!

This section is super advanced and, unless you test the changes extensively and know what you're doing, it's better to leave these options to their defaults, as they are most likely going to work fine without much fuss.

With that warning aside, if we're feeling adventurous, this is how we would pass these options when using a crawler:

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler({
    // Pass in advanced options by providing them in the autoscaledPoolOptions
    autoscaledPoolOptions: {
        // ...
    },
});
```

### `desiredConcurrency`[​](#desiredconcurrency "Direct link to desiredconcurrency")

This option specifies the amount of requests that should be running in parallel at the start of the crawler, assuming there are so many available. It defaults to the same value as `minConcurrency`.

### `desiredConcurrencyRatio`[​](#desiredconcurrencyratio "Direct link to desiredconcurrencyratio")

The minimum ratio of concurrency to reach before more scaling up is allowed (a number between `0` and `1`). By default, it is set to `0.95`.

We can think of this as the point where the autoscaling pool can attempt to scale up (or down), monitor if there's any changes, and correct them if necessary.

### `scaleUpStepRatio` and `scaleDownStepRatio`[​](#scaleupstepratio-and-scaledownstepratio "Direct link to scaleupstepratio-and-scaledownstepratio")

These values define the fractional amount of desired concurrency to be added or subtracted as the autoscaling pool scales up or down. Both of these values default to `0.05`.

Every time the autoscaled pool attempts to scale up or down, this value will be added or subtracted from the current concurrency, and, based on the [`desiredConcurrencyRatio`](#desiredconcurrencyratio) and [`maxConcurrency`](#minconcurrency-and-maxconcurrency), determines how many requests can run concurrently.

### `maybeRunIntervalSecs`[​](#mayberunintervalsecs "Direct link to mayberunintervalsecs")

Indicates how often the autoscaling pool should check if more requests can be started and, if that's true, starts a new request if there are any available. This value is represented in seconds, and defaults to `0.5`.

info

Changing this has no effect for requests that are fired immediately after the previous ones are finished. However, it will influence how fast new requests will be started after the autoscaled pool scales up.

### `loggingIntervalSecs`[​](#loggingintervalsecs "Direct link to loggingintervalsecs")

This option lets us control how often the autoscaled pool should log its current state (the current concurrency ratio, desired ratios, if the system is overloaded and so on).

We can disable logging altogether by setting this to `null`. By default, it is set to `60` seconds.

### `autoscaleIntervalSecs`[​](#autoscaleintervalsecs "Direct link to autoscaleintervalsecs")

This option lets us control how often the autoscaling pool should check if it can and should scale up or down. This value is represented in seconds, and defaults to `10`.

tip

It's recommended you keep this value between `5` and `20` seconds.

Be careful with how low, or high, you set this option

Setting this option to a value that's too low might have a severe impact on our crawling performance. And, in reverse, setting this to a value that's too high might mean we leave performance on the table that could've been used for crawling more requests instead.

With that said, if you configure this alongside [`scaleUpStepRatio` and `scaleDownStepRatio`](#scaleupstepratio-and-scaledownstepratio), you could make your crawler scale up at a slower interval, but with more requests at a time when it does.

### `maxTasksPerMinute`[​](#maxtasksperminute "Direct link to maxtasksperminute")

This controls how many total requests can be made per minute. It counts the amount of requests done every second, to ensure there is not a burst of requests at the `maxConcurrency` limit followed by a long period of waiting. By default, it is set to `Infinity` which means the crawler will keep going up to the `maxConcurrency`. We would set this if we wanted our crawler to work at full throughput, but also not keep hitting the website we're crawl with non-stop requests.

info

This option can be set by specifying [`maxRequestsPerMinute`](#maxrequestsperminute) in your crawler options too, as it is a shortcut for visibility and ease of access.
