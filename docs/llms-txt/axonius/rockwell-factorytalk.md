# Source: https://docs.axonius.com/docs/rockwell-factorytalk.md

# Rockwell FactoryTalk AssetCentre

Rockwell FactoryTalk AssetCentre is a software solution that offers asset management, backup, and disaster recovery for automation environments.

This adapter uploads XML files.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

The adapter parameters are the same as the [CSV adapter parameters](/docs/csv), except for the **File contains users information**, **File contains installed software information**, and the **File contains database information** parameters. These fields are not part of the adapter configuration, as the adapter provides devices data only, without any information on the installed software.

![Rockwell FactoryTalk AssetCentre](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rockwell%20FactoryTalk%20AssetCentre.png)

## Supported From Version

Supported from Axonius version 6.1.39.0