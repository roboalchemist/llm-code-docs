# Source: https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments.md

# Override monitor arguments

## Overview

StackState provides [monitors out of the box](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-monitors), which provide monitoring on common issues that can occur in a Kubernetes cluster. Those monitors work with certain default arguments that suit most of the use cases but sometimes there's need to adapt its behaviour by overriding some of such default arguments like `threshold` or `failureState`. The mechanism to declare the overrides is via kubernetes resource annotations that denote to which monitor and component they should apply. For example we could override the `failureState` for the `Available service endpoints` monitor for a specific service where we want to signal a `CRITICAL` state when it fails rather than the default `DEVIATING`.

## How to

* [Build an override annotation](#build-an-override-annotation)
* [What monitors allow overriding arguments?](#what-monitor-allows-overriding)
* [Build an override for a custom monitor](#build-an-override-for-a-custom-monitor)

As an example the steps will override the arguments for the `Available service endpoints` monitor of Kubernetes HTTP services.

## How to build my annotation

The override annotations keys for StackState monitors follow the following convention:

```
monitor.${owner}.stackstate.io/${monitorShorName}
```

The `owner` property represents who created such a monitor, for the out of the box monitors is `kubernetes-v2`, and the `monitorShorName` property represents the id of the monitor and can be extracted from the `identifier` property of a monitor which can be read from the cli when listing or inspecting monitors

```
sts monitor list

ID              | STATUS  | IDENTIFIER                                                                          | NAME                                        | FUNCTION ID     | TAGS                                                                                  
8051105457030   | ENABLED | urn:stackpack:kubernetes-v2:shared:monitor:kubernetes-v2:service-available-endpoint | Available service endpoints                 | 233276809885571 | [services]         
```

In our example the identifier is `urn:stackpack:kubernetes-v2:shared:monitor:kubernetes-v2:service-available-endpoint` and the `monitorShorName` corresponds to the very last segment as in `service-available-endpoint` therefore the annotation key is:

```bash
monitor.kubernetes-v2.stackstate.io/service-available-endpoint
```

the annotation payload is a JSON object where the following optional arguments can be defined:

* `threshold`: optional.A numeric threshold to compare against.
* `failureState`: optional. Either "CRITICAL" or "DEVIATING". "CRITICAL" will show as read in StackState and "DEVIATING" as orange, to denote different severity.
* `enabled`: optional. Boolean that determines if the monitor would produce a health state for that component.

The full annotation then would look like

```bash
    monitor.kubernetes-v2.stackstate.io/service-available-endpoint: |-
      {
        "threshold": 0.0,
        "failureState": "CRITICAL",
        "enabled": true
      }
```

## What monitors allow overriding arguments?

* [Available service endpoints](https://archivedocs.stackstate.com/kubernetes-monitors#available-service-endpoints)
* [Cpu limits resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#cpu-limits-resourcequota)
* [Cpu requests resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#cpu-requests-resourcequota)
* [Memory limits resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#memory-limits-resourcequota)
* [Memory requests resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#memory-requests-resourcequota)
* [Node Disk Pressure](https://archivedocs.stackstate.com/kubernetes-monitors#node-disk-pressure)
* [Node Memory Pressure](https://archivedocs.stackstate.com/kubernetes-monitors#node-memory-pressure)
* [Node PID Pressure](https://archivedocs.stackstate.com/kubernetes-monitors#node-pid-pressure)
* [Node Readiness](https://archivedocs.stackstate.com/kubernetes-monitors#node-readiness)
* [Out of memory for containers](https://archivedocs.stackstate.com/kubernetes-monitors#out-of-memory-for-containers)

## Build an override for a custom monitor

Any custom threshold monitor created using the guide at [Add a threshold monitor to components using the CLI](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-add-monitors-cli) is suitable to override arguments, as [the example shows](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-add-monitors-cli#write-the-outline-of-the-monitor) an identifier for a custom monitor is structured as `urn:custom:monitor:{monitorShortName}`and the override annotation key for such an identifier is expected to be

```bash
monitor.custom.stackstate.io/${monitorShortName}
```

The example uses the identifier `urn:custom:monitor:deployment-has-replicas` therefore the annotation key would be

```bash
monitor.custom.stackstate.io/deployment-has-replicas
```

And the full annotation would look like

```bash
    monitor.custom.stackstate.io/deployment-has-replicas: |-
      {
        "threshold": 0.0,
        "failureState": "CRITICAL"
        "enabled": true
      }
```
