# Source: https://docs.datadoghq.com/tracing/trace_collection/proxy_setup/httpd.md

---
title: Instrumenting Apache HTTP Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Tracing a Proxy > Instrumenting
  Apache HTTP Server
---

# Instrumenting Apache HTTP Server

Datadog provides an HTTPd [module](https://github.com/DataDog/httpd-datadog) to enhance [Apache HTTP Server](https://httpd.apache.org/) and [IHS HTTP Server](https://github.com/DataDog/httpd-datadog/blob/main/doc/configuration.md) capabilities with APM Tracing.

## Compatibility{% #compatibility %}

Since IHS HTTP Server is essentially a wrapper of the Apache HTTP Server, the module can also be used with IHS without any modifications.

## Installation{% #installation %}

{% alert level="danger" %}
**Note**: Only Apache HTTP Server 2.4.x for x86_64 architecture is supported.
{% /alert %}

The module is provided as a shared library for dynamic loading by HTTPd. Each supported platform and architecture has its own artifact hosted on [httpd-datadog's repository](https://github.com/DataDog/httpd-datadog).

To install the module:

1. Run the following script to download the latest version of the module:

   ```bash
   cd /tmp && \
       # Get latest release info using curl and basic text processing
       RELEASE_DATA=$(curl -s https://api.github.com/repos/DataDog/httpd-datadog/releases/latest) && \
   
       # Extract download URL for the zip file using grep and sed
       DOWNLOAD_URL=$(echo "$RELEASE_DATA" | grep '"browser_download_url".*mod_datadog_artifact.zip' | sed 's/.*"browser_download_url": *"\([^"]*\)".*/\1/') && \
   
       # Download and install
       curl -Lf -o mod_datadog_artifact.zip "$DOWNLOAD_URL" && \
       unzip -j mod_datadog_artifact.zip -d /usr/lib/apache2/modules/ && \
       rm mod_datadog_artifact.zip
   ```

This script downloads the latest release artifact zip file, extracts the `mod_datadog.so` shared library directly to the Apache modules directory, and cleans up the temporary files.

1. If you used a different installation method or need to place the file manually, ensure the `mod_datadog.so` file is in the directory where HTTPd searches for modules, typically `/usr/local/apache2/modules` or `/usr/lib/apache2/modules/`.

1. Load the module by adding the following line in the configuration file:

   ```nginx
   LoadModule datadog_module modules/mod_datadog.so
   ```

1. To enable the module, make sure to restart or reload HTTPd.

## Configuration{% #configuration %}

By default, all requests are traced and sent to the Datadog Agent.

To change the module default behavior, use `Datadog*` directives described in the Datadog module's [API documentation](https://github.com/DataDog/httpd-datadog/blob/main/doc/configuration.md).

For example, the following configuration sets the service name to `my-service` and the sampling rate to 10%:

```nginx
LoadModule datadog_module modules/mod_datadog.so

DatadogServiceName my-app
DatadogSamplingRate 0.1
```

## Further Reading{% #further-reading %}

- [Datadog Module for Apache HTTP Server](https://github.com/DataDog/httpd-datadog)
