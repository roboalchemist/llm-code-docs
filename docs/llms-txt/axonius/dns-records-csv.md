# Source: https://docs.axonius.com/docs/dns-records-csv.md

# CSV - DNS Records

The DNS CSV adapter enables the discovery of SaaS applications based on the organizations web browsing records.

The adapter parameters are the same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv). Since the CSV - DNS Records adapter provides data about DNS Records only, unlike the generic CSV adapter, there is no option to configure the adapter to contain information about  Devices.

The functionality of this adapter is the same as the [CSV adapter](/docs/legacy-remote-file-configuration-csv).

Note that the Accepted CSV fields names are case insensitive.

## Which fields are imported with a  DNS records file?

The following data is imported as part of the DNS records file.

| Field       | Accepted CSV Field Name(s)                                                                     | Notes                        | Required? |
| :---------- | :--------------------------------------------------------------------------------------------- | :--------------------------- | :-------- |
| Domain      | URL, Domain                                                                                    | Relation to SaaS Application | Yes       |
| Access time | Date, DateTime, Time, Access Time, Access Date, Usage Date, Usage Time, Query Date, Query Time |                              | Yes       |
| MAC address | MAC, MAC Address                                                                               | Relation to Device           | No        |
| User        | User, User Email, Usermail, Email, Mail                                                        | Relation to SaaS User        | No        |