# Source: https://docs.datadoghq.com/developers/guide/custom-python-package.md

---
title: Adding a Custom Python Package to the Agent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Developers > Developer Guides > Adding a Custom Python Package to the
  Agent
---

# Adding a Custom Python Package to the Agent

{% tab title="Linux" %}
The Agent contains an embedded Python environment at `/opt/datadog-agent/embedded/`. Common binaries such as `python` and `pip` are contained within `/opt/datadog-agent/embedded/bin/`.

Python packages can be installed with the embedded `pip`:

```shell
sudo -Hu dd-agent /opt/datadog-agent/embedded/bin/pip install <PACKAGE_NAME>
```

{% /tab %}

{% tab title="macOS" %}
The Agent contains an embedded Python environment at `/opt/datadog-agent/embedded/`. Common binaries such as `python` and `pip` are contained within `/opt/datadog-agent/embedded/bin/`.

Python packages can be installed with the embedded `pip`:

```shell
sudo /opt/datadog-agent/embedded/bin/pip install <PACKAGE_NAME>
```

{% /tab %}

{% tab title="Windows" %}
Custom Python packages can be installed using the Agent's embedded Python using the following command in an **elevated** (run as admin) PowerShell command line:

For Agent versions >= 6.12:

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\embedded<PYTHON_MAJOR_VERSION>\python" -m pip install <PACKAGE_NAME>
```

For Agent versions <= 6.11:

```powershell
& "$env:ProgramFiles\Datadog\Datadog Agent\embedded\python" -m pip install <PACKAGE_NAME>
```

Or the package can be added in the library zipped folder that can be found at

```
%ProgramFiles%\Datadog\Datadog Agent\files
```

then [restart your Agent](https://docs.datadoghq.com/agent/basic_agent_usage/windows/).

{% image
   source="https://datadog-docs.imgix.net/images/agent/windows_python_package.967cbc0e4a76446b3aafda95fec7c47b.png?auto=format"
   alt="windows python package" /%}

{% /tab %}

## Further Reading{% #further-reading %}

- [Collect your logs](https://docs.datadoghq.com/logs/)
- [Collect your processes](https://docs.datadoghq.com/infrastructure/process/)
- [Collect your traces](https://docs.datadoghq.com/tracing/)
