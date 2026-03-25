# AutoThrottle extension

This is an extension for automatically throttling crawling speed based on load
of both the Scrapy server and the website you are crawling.

## Design goals

- 

be nicer to sites instead of using default download delay of zero

- 

automatically adjust Scrapy to the optimum crawling speed, so the user
doesn’t have to tune the download delays to find the optimum one.
The user only needs to specify the maximum concurrent requests
it allows, and the extension does the rest.

## How it works

Scrapy allows defining the concurrency and delay of different download slots,
e.g. through the `DOWNLOAD_SLOTS` setting. By default requests are
assigned to slots based on their URL domain, although it is possible to
customize the download slot of any request.

The AutoThrottle extension adjusts the delay of each download slot dynamically,
to make your spider send `AUTOTHROTTLE_TARGET_CONCURRENCY` concurrent
requests on average to each remote website.

It uses download latency to compute the delays. The main idea is the
following: if a server needs `latency` seconds to respond, a client
should send a request each `latency/N` seconds to have `N` requests
processed in parallel.

Instead of adjusting the delays one can just set a small fixed
download delay and impose hard limits on concurrency using
`CONCURRENT_REQUESTS_PER_DOMAIN`. It will provide a similar
effect, but there are some important differences:

- 

because the download delay is small there will be occasional bursts
of requests;

- 

often non-200 (error) responses can be returned faster than regular
responses, so with a small download delay and a hard concurrency limit
crawler will be sending requests to server faster when server starts to
return errors. But this is an opposite of what crawler should do - in case
of errors it makes more sense to slow down: these errors may be caused by
the high request rate.

AutoThrottle doesn’t have these issues.

## Throttling algorithm

AutoThrottle algorithm adjusts download delays based on the following rules:

- 

spiders always start with a download delay of
`AUTOTHROTTLE_START_DELAY`;

- 

when a response is received, the target download delay is calculated as
`latency / N` where `latency` is a latency of the response,
and `N` is `AUTOTHROTTLE_TARGET_CONCURRENCY`.

- 

download delay for next requests is set to the average of previous
download delay and the target download delay;

- 

latencies of non-200 responses are not allowed to decrease the delay;

- 

download delay can’t become less than `DOWNLOAD_DELAY` or greater
than `AUTOTHROTTLE_MAX_DELAY`

Note

The AutoThrottle extension honours the standard Scrapy settings for
concurrency and delay. This means that it will respect
`CONCURRENT_REQUESTS_PER_DOMAIN` and
never set a download delay lower than `DOWNLOAD_DELAY`.