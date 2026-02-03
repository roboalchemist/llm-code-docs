# Source: https://docs.datadoghq.com/tracing/troubleshooting/go_compile_time.md

---
title: Troubleshooting Go Compile-Time Instrumentation
description: >-
  Debug Orchestrion build issues by preserving work trees, configuring logging,
  and examining transformed source files.
breadcrumbs: >-
  Docs > APM > APM Troubleshooting > Troubleshooting Go Compile-Time
  Instrumentation
---

# Troubleshooting Go Compile-Time Instrumentation

## Overview{% #overview %}

This guide explains how to troubleshoot builds that [Orchestrion](https://github.com/DataDog/orchestrion) manages. These procedures can help Datadog gather insights about build processes and can assist with bug reports.

{% alert level="danger" %}
The generated files may contain sensitive project information, such as source code and dependency names. If sharing such information publicly is a concern, contact Datadog support to share the data privately.
{% /alert %}

## Preserving the work tree{% #preserving-the-work-tree %}

Orchestrion records build transformations in the `go build` work tree. To prevent the `go` toolchain from cleaning this directory after building, use the `-work` flag:

```shell
orchestrion go build -work ./...
WORK=/tmp/go-build2455442813
```

The work tree location prints at the start of the build, marked with `WORK=`. This directory contains subdirectories for each built `go` package, which are called *stage directories*.

## Work tree contents{% #work-tree-contents %}

When Orchestrion injects code into a source file, it writes the modified file to the package's stage directory (`$WORK/b###`) in the `orchestrion/src` subdirectory. For modified package import configurations, the original file is preserved with a `.original` suffix. You can inspect these human-readable files to verify Orchestrion's actions. Contact Datadog support for help interpreting these files.

## Logging configuration{% #logging-configuration %}

### Log levels{% #log-levels %}

Control Orchestrion's logging output using the `ORCHESTRION_LOG_LEVEL` environment variable or `--log-level` flag:

| Level                   | Description                                  |
| ----------------------- | -------------------------------------------- |
| `NONE`, `OFF` (default) | No logging output                            |
| `ERROR`                 | Error information only                       |
| `WARN`                  | Errors and warnings                          |
| `INFO`                  | Errors, warnings, and informational messages |
| `DEBUG`                 | Detailed logging                             |
| `TRACE`                 | Extremely detailed logging                   |

{% alert level="danger" %}
Setting `ORCHESTRION_LOG_LEVEL` to the `DEBUG` or `TRACE` levels might have a significant impact on build performance. These settings are not recommended for normal operations.
{% /alert %}

### Log file output{% #log-file-output %}

Write logging messages to files instead of the console by setting the `ORCHESTRION_LOG_FILE` environment variable or `--log-file` flag with the desired file path.

{% alert level="info" %}
Setting `ORCHESTRION_LOG_FILE` changes the default value of `ORCHESTRION_LOG_LEVEL` to `WARN`.
{% /alert %}

The log file path can include `$PID` or `${PID}` tokens, which are replaced with the logging process's PID. This reduces file contention but creates multiple log files for large projects.

Logging appends to existing files rather than overwriting them, regardless of the presence of `$PID` in the file path.

## Further reading{% #further-reading %}

- [Tracing Go Applications](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/go/)
