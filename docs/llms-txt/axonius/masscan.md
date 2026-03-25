# Source: https://docs.axonius.com/docs/masscan.md

# Masscan

Masscan is a free internet port scanner utility.

The Mascan adapter is able to import Masscan JSON files with information about devices.

The adapter parameters are as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except for the **File contains users information** and the **File contains installed software information** parameters. These fields are not part of the Masscan adapter configuration, as the adapter provides devices data only, without any information on the installed software.

The functionality of this adapter is as same as the [CSV adapter](/docs/csv).

<Callout icon="📘" theme="info">
  Note

  It  is recommended to comment out the masscan configuration "output-status=all"
  You should use version 1.3.2 or higher of Masscan.
</Callout>