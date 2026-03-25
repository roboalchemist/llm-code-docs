# Source: https://docs.axonius.com/docs/alien-vault-adapter.md

# AlienVault

AT\&T Cybersecurity (formerly AlienVault) is a managed detection and response product.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

The adapter parameters are as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except for the **File contains users information** and the **File contains installed software information** parameters, which are not part of this adapter.

Using this adapter you can upload CSV files, where devices may be multiple rows in the CSV file. If  different rows have the same host name all these rows are aggregated internally and presented as 1 device.

You can also upload details of the  devices and the software CVEs on them.
For the Software CVE use the structure [here](/docs/legacy-remote-file-configuration-csv#which-fields-are-imported-with-a-software-applications-file)