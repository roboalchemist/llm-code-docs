# Source: https://docs.statsig.com/statsig-warehouse-native/features/incremental-reloads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Incremental Reloads

Incremental reloads save state from the last load, and load from the latest data read with a small buffer to ensure completeness. This job wipes data since the last load, plus that buffer, and then appends all new data to the staging datasets before calculating results for changed days.

This is the recommended way to load active experiments, and is used for ongoing, daily loads -- especially when datasets are large.


Built with [Mintlify](https://mintlify.com).