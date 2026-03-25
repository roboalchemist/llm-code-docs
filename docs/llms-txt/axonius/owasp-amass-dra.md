# Source: https://docs.axonius.com/docs/owasp-amass-dra.md

# OWASP Amass

## Overview

The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.

The Axonius OWASP Amass adapter imports subdomain, IP address, and related host data exported by OWASP Amass in JSON format. This enables organizations to leverage domain enumeration and external asset discovery data for security and compliance use cases within Axonius

### Use Cases the Adapter Solves

* Aggregates and analyzes externally discovered assets, such as domains and IPs, to identify shadow IT and unmanaged environments.
* Enriches your asset inventory with reconnaissance data to verify security coverage across all exposed infrastructure.

### Asset Types Fetched

* Devices

***

## Before You Begin

**Authentication Method**

No authentication is required; the adapter ingests data from JSON files locally produced by the OWASP Amass tool.

### Permissions

The following permissions are required:

* Read access to the exported JSON files produced by amass.

#### Supported From Version

Supported from Axonius version 6.1.9

### Setting Up OWASP Amass to Work with Axonius

1. Download and install OWASP Amass from the [official GitHub repository](https://github.com/OWASP/Amass).
2. Run the enumeration using a command such as:
   ```
   amass enum -d example.com -json amass-output.json
   ```
3. Save the resulting JSON file to a location accessible by Axonius.
4. When creating an adapter in Axonius, upload the exported JSON file as required by the connection parameters.

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **OWASP Amass**, and click on the adapter tile.
Click **Add Connection**.

The adapter parameters are as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except for the **File contains users information** and the **File contains installed software information** parameters. These fields are not part of the OWASP Amass adapter configuration, as the adapter provides devices data only.

The functionality of this adapter is as same as the [CSV adapter](/docs/csv).

<br />

<br />

<br />