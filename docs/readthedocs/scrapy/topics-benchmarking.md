# Benchmarking

Scrapy comes with a simple benchmarking suite that spawns a local HTTP server
and crawls it at the maximum possible speed. The goal of this benchmarking is
to get an idea of how Scrapy performs in your hardware, in order to have a
common baseline for comparisons. It uses a simple spider that does nothing and
just follows links.

To run it use:

```
scrapy bench

```