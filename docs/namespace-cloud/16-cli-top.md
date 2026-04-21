# nsc top

Interactive process viewer for monitoring resource utilization.

## Overview

Starts an interactive process viewer allowing you to observe resource utilization of the target instance.

## Basic Usage

```bash
nsc top <instance-id>
```

## Description

This resource monitoring tool displays CPU, memory, and other resource metrics for the specified compute instance in real-time.

## Practical Example

```bash
# Create an instance
nsc create

# This returns an instance ID like hk99v6hn1tk9m

# Monitor the instance
nsc top hk99v6hn1tk9m
```

This launches an interactive monitoring interface where you can track:

- CPU usage and allocation
- Memory usage and allocation
- Disk I/O
- Network activity
- Process-level resource metrics

## Related Commands

- `nsc create` - Creates a new instance
- `nsc list` - Lists instances
