# Source: https://docs.axonius.com/docs/steel-cloud.md

# SteelCloud

SteelCloud is an automated compliance and configuration management tool designed to quickly implement and maintain security policies, such as STIGs and CIS benchmarks, for enterprise and government systems.

This adapter downloads zip files that contain JSON files.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

The adapter parameters are the same as the [CSV adapter parameters](/docs/csv), except for the **File contains users information**, **File contains installed software information**, and the **File contains database information** parameters. These fields are not part of the adapter configuration, as the adapter provides devices data only, without any information on the installed software.

![SteelCloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SteelCloud.png)

## Supported From Version

Supported from Axonius version 6.1.37.0