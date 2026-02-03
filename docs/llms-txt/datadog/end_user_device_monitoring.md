# Source: https://docs.datadoghq.com/infrastructure/end_user_device_monitoring.md

---
title: End User Device Monitoring
description: >-
  Monitor employee desktops and laptops to detect performance, connectivity, and
  application issues across your organization.
breadcrumbs: Docs > Infrastructure > End User Device Monitoring
---

# End User Device Monitoring

{% callout %}
##### Join the Preview!

End User Device Monitoring is in Preview. To enroll, click Request Access.

[Request Access](https://www.datadoghq.com/product-preview/end-user-device-monitoring/)
{% /callout %}

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/end_user_device_monitoring/end_user_devices.2eb3db8db0f01c36bf82f67b191541f3.png?auto=format"
   alt="End User Devices page showing four healthy devices, charts for device types and operating systems, and a device table with one laptop marked for system crashes." /%}

End User Device Monitoring gives IT teams visibility into the health and performance of employee desktops and laptops, both physical and virtual. It helps identify performance and connectivity issues affecting employees and provides a unified view of device, network, and application health across your workforce.

## How it works{% #how-it-works %}

End User Device Monitoring uses the Datadog Agent to collect data directly from employee desktops, laptops, and workstations. The Agent gathers system metrics, network information, and logs from each device and sends the data to Datadog, where it can be monitored and visualized.

The [End User Devices](https://app.datadoghq.com/end-user-devices) page provides built-in dashboards and metrics that summarize health and performance across your organization's devices. You can view summary metrics for all devices and detailed metrics for individual ones, including CPU, memory, and network usage.

Use [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/) to manage the Agents installed on those devices, including checking version status, verifying configuration consistency, and ensuring that the necessary integrations are enabled.

## Key capabilities{% #key-capabilities %}

| Capability                        | Description                                                                                                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Device performance monitoring** | Monitor overall system health metrics such as CPU, memory, disk, and network utilization to identify underperforming devices.                                                                                                                         |
| **Process visibility**            | Use [Live Processes](https://docs.datadoghq.com/infrastructure/process) to monitor resource usage by individual processes and identify applications affecting device performance.                                                                     |
| **Logs collection**               | Use [Logs](https://docs.datadoghq.com/logs/) to collect and explore logs from end-user devices and applications for troubleshooting crashes, errors, and performance issues.                                                                          |
| **Wi-Fi monitoring**              | Monitor Wi-Fi metrics such as signal quality, transmission rate, and access point transitions with the [WiFi/WLAN integration](https://docs.datadoghq.com/integrations/wlan/), which helps identify connectivity issues and overloaded access points. |
| **Windows crash detection**       | Detect Blue Screen of Death (BSOD) events on Windows devices with the [Windows Crash Detection integration](https://docs.datadoghq.com/integrations/wincrashdetect/), which generates Datadog events showing when system crashes occur.               |
| **Network path analysis**         | Use [Network Path](https://docs.datadoghq.com/network_monitoring/network_path/) to trace network traffic from an end-user device to its destination and identify where latency or connectivity issues occur.                                          |

## Further reading{% #further-reading %}

- [Set up End User Device Monitoring](https://docs.datadoghq.com/infrastructure/end_user_device_monitoring/setup)
