# Source: https://docs.axonius.com/docs/stig.md

# STIG

STIG is a framework that defines standardized security configurations and compliance requirements for IT systems and software. It retrieves compliance data for security controls to assess adherence to defined requirements.

This adapter uploads CKL and CKLB files.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

The adapter parameters are the same as the [CSV adapter parameters](/docs/csv), except for the File contains users information, File contains installed software information, and the File contains database information parameters. These fields are not part of the adapter configuration, as the adapter provides devices data only, without any information on the installed software.

![STIG](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/STIG.png)

## Supported From Version

Supported from Axonius version 6.1.45.0