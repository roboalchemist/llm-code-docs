---
---
title: Operating Guidelines
description: "Learn about our guidelines for operation when self-hosting external Relays."
---
---

This page reviews our guidelines for operation when self-hosting external Relays, that is, Relays that run on your hardware and forward events to `sentry.io`.

## General Considerations

- We recommend [running Relay](/product/relay/getting-started/) using the officially provided Docker image (`getsentry/relay`) found on [DockerHub](https://hub.docker.com/r/getsentry/relay/) and tagged with its Git revision identifier, rather than building from source.

- We recommend running at least two Relay instances (containers) with a reverse proxy (such as [HAProxy](https://www.haproxy.org/) or [Nginx](https://nginx.org)) in front of them for improved availability, simplified Relay updates, and SSL/TLS support.

- To monitor your Relay setup, configure [Logging](/product/relay/monitoring/#logging), [Metrics](/product/relay/monitoring/#metrics), and [Health Checks](/product/relay/monitoring/#health-checks).

## System Requirements and Recommendations

The following recommendations assume that Relay is run in Docker.

| Resource | Recommendations                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CPU      | - **Required**: x86-64 (amd64) or AArch64 (arm64) CPU architecture<br/> - Multi-core CPU [[1]](#multi-core-cpu)                                                                                                                                                                                                                                                                                                                                                          |
| Memory   | - At least 2GB of RAM per Relay container is recommended.                                                                                                                                                                                                                                                                                                                                                                                             |
| Network  | - Bandwidth: Make sure you have enough capacity to receive and forward the planned data volume. Relay compresses all upstream requests to `sentry.io` by default, but the compression rate might vary depending on the types and shapes of the submitted events.<br/> - Latency: Relay can tolerate network delays up to a certain point. It is however recommended to make sure that the round-trip time to the upstream stays lower than 5 seconds. |
| Storage  | - Disk storage is only required if [Spooling](/product/relay/options/#spooling) is configured. See the `spool.envelopes.max_memory_size` configuration option. Otherwise, Relay does not require disk storage.                                                                                                                                                                                                                                        |

<p id="multi-core-cpu">

[[1]](#multi-core-footnote) Relay is a multi-threaded application that tries to leverage all available CPU cores. As a result, Sentry highly recommends running Relay on multi-core CPUs. If your setup is expected to handle more than 100 requests per second, we recommend running Relay on at least four (4) CPU cores. By default, every Relay instance will use the total number of available cores to adjust the sizes of its thread pools. Adjust this behavior by configuring the `limits.max_thread_count`.

</p>

## Relay Binary

Every release of Relay also provides a set of binaries that are built for the Operating Systems listed below.

| Operating System | Version                   |
|------------------|---------------------------|
| Ubuntu x64       | 20.04                     |
| Ubuntu ARM       | 22.04                     |
| macOS            | macOS Sonoma (version 14) |
| Windows          | Windows Server 2022       |

We will support Ubuntu binaries 2 years after the official LTS support has ended to allow customers with extended
support to continue using Relay.

Windows and macOS binaries are built using GitHub Runners. We will support the versions for those Operating Systems
as long as GitHub supports them.

## Example Configuration

This example configuration sets up basic logging and metrics settings, as well as changes the default concurrency level.

```yaml