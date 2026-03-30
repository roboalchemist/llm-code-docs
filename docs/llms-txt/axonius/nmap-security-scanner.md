# Source: https://docs.axonius.com/docs/nmap-security-scanner.md

# Nmap Security Scanner

Nmap Security Scanner is a free and open source utility for network discovery and security auditing.

The Nmap Security Scanner adapter is able to import Nmap XML files with information about devices.

The adapter parameters are as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except for the **File contains users information** and the **File contains installed software information** parameters. These fields are not part of the Nmap Security Scanner adapter configuration, as the adapter provides devices data only, without any information on the installed software.

The functionality of this adapter is as same as the [CSV adapter](/docs/csv).

Note the following changes to CSV configuration:
**Path to resource (SMB/URL/Folder path)** (optional) - Specify an SMB share path, HTTP(S) URL, FTP URL, or folder path where a file can be fetched for this connection.  This   must be the entire PATH plus the FILE to pull from in order to work.
**File Name** - Any text can be entered in this field

## Asset Types Fetched

* Devices
  , Aggregated Security Findings
  , Software
  , SaaS Applications

## Fetching .xml Files Recursively

In Nmap you can fetch xml files recursively from a remote AWS S3 directory.

To configure this do the following:

1. In **Amazon S3 object location (key)** enter the path of the S3 directory.
2. Fill in all the AWS credentials in the following fields:

   * **Amazon S3 Access Key ID**
   * **Amazon S3 Secret Access Key**
   * **Amazon S3 bucket name**

The system will now fetch all Nmap .xml fields (recursively) that exist under the S3 directory path.

<Image border={false} src="https://files.readme.io/9e0c37c84d32b8542e36442084618f8a9ea5665da866310c9fcea4141ab87a51-image.png" />

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Parse identifiers from an IP Hostname** - When selected, the adapter will parse the ID and Host Name identifiers if the hostname contains an IP.