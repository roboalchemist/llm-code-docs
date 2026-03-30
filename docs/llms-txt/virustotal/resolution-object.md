# Source: https://virustotal.readme.io/reference/resolution-object.md

# Resolutions

Domain-IP resolutions.

Resolution objects include the following attributes:

* `date`: <*integer*> date when the resolution was made (UTC timestamp).
* `host_name`: <*string*> domain or subdomain requested to the resolver.
* `host_name_last_analysis_stats`: <*dictionary*> last detection stats from the resolution's domain. Similar to the [domains](https://virustotal.readme.io/reference/domains-object)'s last\_analysis\_stats attribute.
* `ip_address`: <*string*> IP address the domain was resolved to.
* `ip_address_last_analysis_stats`: <*dictionary*> last detection stats from the resolution's IP address. Similar to the [IP address](https://virustotal.readme.io/reference/ip-object)' last\_analysis\_stats attribute.
* `resolver`: <*string*> source of the resolution.

```json Resolution object
{
  "type": "resolution",
  "id": <string>,
  "attributes": {
        "date": <timestamp>,
        "host_name": <string>,
        "host_name_last_analysis_stats": <dict>,
        "ip_address": <string>,
        "ip_address_last_analysis_stats": <dict>,
        "resolver": <string>
    },
 "links": {
    "self": <string>
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "date": 1599471348,
      "host_name": "example.com",
      "host_name_last_analysis_stats": {
        "harmless": 77,
        "malicious": 0,
        "suspicious": 0,
        "undetected": 8,
        "timeout": 0
      },
      "ip_address": "111.222.33.44",
      "ip_address_last_analysis_stats": {
        "harmless": 75,
        "malicious": 0,
        "suspicious": 0,
        "undetected": 10,
        "timeout": 0
      },
      "resolver": "VirusTotal"
    },
    "id": "111.222.33.44example.com",
    "links": {
      "self": "https://www.virustotal.com/api/v3/resolutions/111.222.33.44example.com"
    },
    "type": "resolution"
  }
}
```