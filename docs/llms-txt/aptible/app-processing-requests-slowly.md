# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/app-processing-requests-slowly.md

# App Processing Requests Slowly

## Cause

If your app is processing requests slowly, it's possible that it is receiving more requests than it can efficiently handle at its current scale (due to hitting maxes with [CPU](/core-concepts/scaling/cpu-isolation) or [Memory](/core-concepts/scaling/memory-limits)).

## Resolution

First, consider deploying an [Application Performance Monitoring](/how-to-guides/observability-guides/setup-application-performance-monitoring) solution in your App in order to get a better understanding of why it's running slow.

Then, if needed, see [Scaling](/core-concepts/scaling/overview) for instructions on how to resize your App [Containers](/core-concepts/architecture/containers/overview).
