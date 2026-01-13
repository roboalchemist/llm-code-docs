# Source: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/python.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/enabling/python.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/symdb/python.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/library_config/python.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/compatibility/python.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/opentracing/python.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/python.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python.md

---
title: Tracing Python Applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Add the Datadog Tracing Library >
  Tracing Python Applications
source_url: https://docs.datadoghq.com/trace_collection/dd_libraries/python/index.html
---

# Tracing Python Applications

## Compatibility requirements{% #compatibility-requirements %}

For a full list of Datadog's Python version and framework support (including legacy and maintenance versions), read the [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/python) page.

## Getting started{% #getting-started %}

Before you begin, make sure you've already [installed and configured the Agent](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/?tab=datadoglibraries#install-and-configure-the-agent).

### Instrument your application{% #instrument-your-application %}

After you install and configure your Datadog Agent, the next step is to add the tracing library directly in the application to instrument it. Read more about [compatibility information](https://docs.datadoghq.com/tracing/compatibility_requirements/python).

To begin tracing applications written in Python, install the Datadog Tracing library, `ddtrace`, using pip:

```python
pip install ddtrace
```

**Note:** This command requires pip version `18.0.0` or greater. For Ubuntu, Debian, or another package manager, update your pip version with the following command:

```python
pip install --upgrade pip
```

Then to instrument your Python application use the included `ddtrace-run` command. To use it, prefix your Python entry-point command with `ddtrace-run`.

For example, if your application is started with `python app.py` then:

```shell
ddtrace-run python app.py
```

Once you've finished setup and are running the tracer with your application, you can run `ddtrace-run --info` to check that configurations are working as expected. Note that the output from this command does not reflect configuration changes made during runtime in code.

## Configuration{% #configuration %}

The tracing library can be configured through environment variables. This is the recommended approach for setting the Agent host, port, and other settings.

For a comprehensive list of configuration options, including Unified Service Tagging, see the [Library Configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/python/) documentation.

## Upgrading to dd-trace-py v4{% #upgrading-to-dd-trace-py-v4 %}

Version 4.0.0 drops support for Python 3.8, removes deprecated APIs, and changes default behaviors for frameworks like Django.

For a complete migration guide, see [Migrate to dd-trace-py v4](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/migrate/python/v4).

## Upgrading to dd-trace-py v3{% #upgrading-to-dd-trace-py-v3 %}

Version 3.0.0 drops support for Python 3.7, removes deprecated APIs, and cleans up configuration names.

For a complete migration guide, see [Migrate to dd-trace-py v3](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/migrate/python/v3).

## Further reading{% #further-reading %}

- [Source code](https://github.com/DataDog/dd-trace-py)
- [API Docs](https://ddtrace.readthedocs.io/en/stable/)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/glossary/)
- [Advanced Usage](https://docs.datadoghq.com/tracing/)
