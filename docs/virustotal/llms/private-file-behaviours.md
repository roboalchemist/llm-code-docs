# Source: https://virustotal.readme.io/reference/private-file-behaviours.md

# 🔒 Private Files Behaviours

Information about private file behaviours

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Private file behaviours are identical to [file behaviours](https://virustotal.readme.io/reference/file-behaviour-summary), but they summarize the behaviour of a [private file](https://virustotal.readme.io/reference/private-files). They can be only seen by the users who uploaded the original file.

## Additional attributes

* `html_report_link`: <*string*> download URL of the reports's HTML report (if present).
* `pcap_link`: <*string*> download URL of the report's PCAP file (if present).
* `evtx_link`: <*string*> download URL of the report's EVTX file (if present).
* `memdump_link`: <*string*> download URL of the report's memdump file (if present).

## Relationships

In addition to the previously described attributes, private file behaviour objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section.

The following table shows a summary of available relationships.

| Relationship       | Return object type                                 |
| :----------------- | :------------------------------------------------- |
| attack\_techniques | List of [Attack Techniques](https://virustotal.readme.io/reference/attack-techniques) |
| file               | A single [Private File](https://virustotal.readme.io/reference/private-files)         |