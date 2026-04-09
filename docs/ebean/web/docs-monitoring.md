# Source: https://ebean.io/docs/monitoring

Title: Introduction

URL Source: https://ebean.io/docs/monitoring

Markdown Content:
Ebean collects metrics for transactions, queries and cache hits. These metrics are then available to collect and report.

The fast way to see what metrics are collected is to have them dumped when the server is shutdown via `dumpMetricsOnShutdown` (typically after running all the tests).

ebean:
  dumpMetricsOnShutdown: true
  dumpMetricsOptions: loc,sql,hash
  test:
    platform: h2 # h2, postgres, mysql, oracle, sqlserver, sqlite
    ddlMode: dropCreate # none | dropCreate | migrations | create
    dbName: my_app

Below is small example output with options of `loc,sql,hash`.

-- Dumping metrics for db --
txn.main                                        count:10       total:117459   mean:11745    max:32894

-- ORM queries --
query:CustomerFinder.findByName                 count:1        total:4089     mean:4089     max:4089
hash:8c314fa1f6dbecfcdd449ccd021c8980
loc:CustomerFinder.findByName(CustomerFinder.kt:17)

sql:select t0.id, t0.name from customer t0 where lower(t0.name) like ? escape'|'

query:ProductFinder.findMapBySku                count:1        total:2364     mean:2364     max:2364
hash:aeda919cc69bea1026543d5307276eeb
loc:ProductFinder.findMapBySku(ProductFinder.kt:12)

sql:select t0.id, t0.sku, t0.name, t0.version, t0.when_created, t0.when_modified from product t0

...

We can obtain the metrics via _MetaInfoManager_. When we call _collectMetrics()_ the non-empty metrics are returned and the metric counters are reset.
