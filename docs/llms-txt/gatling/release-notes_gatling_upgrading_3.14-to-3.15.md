# Source: https://docs.gatling.io/release-notes/gatling/upgrading/3.14-to-3.15/index.md


## Feeder loading mode control was dropped

Previously, it was possible to force the loading mode of file based feeders with `eager` and `batch`.
The default behavior has been given ample satisfaction, so we are making it the only behavior and hence simplifying or SDKs.
