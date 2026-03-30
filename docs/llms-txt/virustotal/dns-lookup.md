# Source: https://virustotal.readme.io/reference/dns-lookup.md

# dns_lookups

DNS queries

`dns_lookups` attribute contains a list of **domain name resolutions performed** by a given file. It is a *list of dictionaries*, each one containing the following fields:

* `hostname` <*string*>: hostname of DNS query.
* `resolved_ips` <*list of strings*>: all resolved IP addresses, may be empty on NX domain.

```json DNS lookups
{
    "data": {
        "attributes": {
            "dns_lookups": [
                {
                    "hostname": "<string>",
                    "resolved_ips": [
                        "<string>",...
                    ]
                },...
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "dns_lookups": [
                {
                    "hostname": "blablabla.com",
                    "resolved_ips": [
                        "66.66.66.66"
                    ]
                },
                {
                    "hostname": "example.com",
                }
            ]
        }
    }
}
```