# Source: https://docs.vespa.ai/en/operations/self-managed/live-upgrade.html.md

# Live-upgrading Vespa

 

This document describes how to live upgrade a Vespa instance. Use this procedure to upgrade without disruption to read or write traffic.

1. **Before upgrading**
  - If upgrading to a **new major version**: Upgrade to the latest version on the current major first, then read the release notes for the new major before progressing. 
  - If upgrading to a new minor version [you should upgrade to a version that is less than 2 months older than the one you are running](../../learn/releases.html#versions) When upgrading a config server this is verified by checking that the minor version number bump is less than 30, otherwise the config server refuses to start. This behavior can be overridden at your own risk by setting environment variable _VESPA\_SKIP\_UPGRADE\_CHECK=true_ on config servers before upgrading. 
  - Redundancy: For availability, there must be sufficient capacity to take one node per cluster out of service at the time. If the clusters have redundancy=1, or searchable-copies=1, some data will not be available during the upgrade (reduced coverage). 
  - To reduce node downtime, download the new Vespa version to all hosts in advance. 

2. **Detach the application nodes**Not necessary in Vespa 8, for upgrading between Vespa 7 versions see [Vespa 8 release notes](../../reference/release-notes/vespa8.html#upgrade-procedure).
3. **Upgrade config servers**
  - Install the new Vespa version on the config servers and [restart](admin-procedures.html#vespa-start-stop-restart) them one by one. Wait until it is up again, look in vespa log for "Changing health status code from 'initializing' to 'up'" or use [health checks](configuration-server.html#troubleshooting). 
  - Redeploy and activate the application: 
```
$[vespa](../../clients/vespa-cli.html#deployment)prepare <app> && vespa activate
```
  - The other nodes in the system will not receive config until they are upgraded to the new version (there will be warnings in vespa log containing "Request callback failed: UNKNOWN\_VESPA\_VERSION" until the node is upgraded). This is to make sure that no new, possibly incompatible, config is served. 

4. **Upgrade all other nodes one by one** - for each of the other nodes in the system: 
  - [Stop services](admin-procedures.html#vespa-start-stop-restart) on the node. 
  - Install the new Vespa version.
  - [Start services](admin-procedures.html#vespa-start-stop-restart) on the node.
  - Wait until the node is fully up before doing the next node - metrics/interfaces to be used to evaluate if the next node can be stopped: 
    - Check if a node is up using [/state/v1/health](../../reference/api/state-v1.html#state-v1-health). 
    - Check the `vds.idealstate.merge_bucket.pending.average` metric on content nodes. When 0, all buckets are in sync - see [example](../metrics.html). 

### Troubleshooting
See [config server troubleshooting](configuration-server.html#troubleshooting).

 Copyright © 2025 - [Cookie Preferences](#)

