# Source: https://docs.axonius.com/docs/honeywell-experion.md

# Honeywell Experion

Honeywell Experion is an industrial automation platform that provides control, monitoring, and data analytics for optimizing manufacturing, process control, and industrial operations.

This adapter uploads XML files.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

The adapter parameters are the same as the [CSV adapter parameters](/docs/csv), except for the **File contains users information**, **File contains installed software information**, and the **File contains database information** parameters. These fields are not part of the adapter configuration, as the adapter provides devices data only, without any information on the installed software.

![Honeywell Experion](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Honeywell%20Experion.png)

## Supported From Version

Supported from Axonius version 6.1.37.0