# Source: https://docs.axonius.com/docs/yokogawa-cim.md

# Yokogawa CIM

Yokogawa CIM (Consolidated Instrumentation Management) is an industrial automation tool that provides centralized monitoring, management, and optimization of instrumentation and control systems.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

The adapter parameters are the same as the [CSV adapter parameters](/docs/csv), except for the **File contains users information**, **File contains installed software information**, and the **File contains database information** parameters. These fields are not part of the adapter configuration, as the adapter provides devices data only, without any information on the installed software.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Yokogawa CIM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Yokogawa%20CIM.png)

## Supported From Version

Supported from Axonius version 6.1.39.0