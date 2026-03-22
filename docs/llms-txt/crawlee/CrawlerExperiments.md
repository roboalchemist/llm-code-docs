# Source: https://crawlee.dev/js/api/basic-crawler/interface/CrawlerExperiments.md

# CrawlerExperiments<!-- -->

A set of options that you can toggle to enable experimental features in Crawlee.

NOTE: These options will not respect semantic versioning and may be removed or changed at any time. Use at your own risk. If you do use these and encounter issues, please report them to us.

## Index[**](#Index)

### Properties

* [**requestLocking](#requestLocking)

## Properties<!-- -->[**](#Properties)

### [**](#requestLocking)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L423)optionalrequestLocking

**requestLocking?

<!-- -->

: boolean

* **@deprecated**

  This experiment is now enabled by default, and this flag will be removed in a future release. If you encounter issues due to this change, please:

  * report it to us: <https://github.com/apify/crawlee>
  * set `requestLocking` to `false` in the `experiments` option of the crawler
