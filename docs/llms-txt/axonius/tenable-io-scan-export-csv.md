# Source: https://docs.axonius.com/docs/tenable-io-scan-export-csv.md

# Tenable.io Scan Export CSV

Tenable Vulnerability Management CSV File (Formerly Tenable.io) provides the ability to import a Tenable Vulnerability Management (Formerly Tenable.io)  scan CSV.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

The adapter parameters are as same as the [CSV adapter parameters](/docs/csv), except for the **File contains users information** and the **File contains installed software information** parameters. These fields are not part of the adapter configuration, as the adapter provides devices data only, without any information on the installed software.

## Required Permissions

ReadOnly permissions are required in  order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                  | Supported | Notes |
| ---------------------------------------- | --------- | ----- |
| Tenable Vulnerability Management V 1.0.0 | Yes       |       |