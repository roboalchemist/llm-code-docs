# Source: https://docs.infrahub.app/python-sdk/reference/templating.md

# Python SDK Templating

Filters can be used when defining [computed attributes](https://docs.infrahub.app/guides/computed-attributes) or [Jinja2 Transforms](https://docs.infrahub.app/guides/jinja2-transform) within Infrahub.

## Builtin Jinja2 filters[​](#builtin-jinja2-filters "Direct link to Builtin Jinja2 filters")

The following filters are those that are [shipped with Jinja2](https://jinja.palletsprojects.com/en/stable/templates/#list-of-builtin-filters) and enabled within Infrahub. The trusted column indicates if the filter is allowed for use with Infrahub's computed attributes when the server is configured in strict mode.

| Name           | Trusted |
| -------------- | ------- |
| abs            | ✅      |
| attr           | ❌      |
| batch          | ❌      |
| capitalize     | ✅      |
| center         | ✅      |
| count          | ✅      |
| d              | ✅      |
| default        | ✅      |
| dictsort       | ❌      |
| e              | ✅      |
| escape         | ✅      |
| filesizeformat | ✅      |
| first          | ✅      |
| float          | ✅      |
| forceescape    | ✅      |
| format         | ✅      |
| groupby        | ❌      |
| indent         | ✅      |
| int            | ✅      |
| items          | ❌      |
| join           | ✅      |
| last           | ✅      |
| length         | ✅      |
| list           | ✅      |
| lower          | ✅      |
| map            | ❌      |
| max            | ✅      |
| min            | ✅      |
| pprint         | ❌      |
| random         | ❌      |
| reject         | ❌      |
| rejectattr     | ❌      |
| replace        | ✅      |
| reverse        | ✅      |
| round          | ✅      |
| safe           | ❌      |
| select         | ❌      |
| selectattr     | ❌      |
| slice          | ✅      |
| sort           | ❌      |
| string         | ✅      |
| striptags      | ✅      |
| sum            | ✅      |
| title          | ✅      |
| tojson         | ❌      |
| trim           | ✅      |
| truncate       | ✅      |
| unique         | ❌      |
| upper          | ✅      |
| urlencode      | ✅      |
| urlize         | ❌      |
| wordcount      | ✅      |
| wordwrap       | ✅      |
| xmlattr        | ❌      |

## Netutils filters[​](#netutils-filters "Direct link to Netutils filters")

The following Jinja2 filters from [Netutils](https://netutils.readthedocs.io) are included within Infrahub.

| Name                               | Trusted |
| ---------------------------------- | ------- |
| abbreviated\_interface\_name       | ✅      |
| abbreviated\_interface\_name\_list | ✅      |
| asn\_to\_int                       | ✅      |
| bits\_to\_name                     | ✅      |
| bytes\_to\_name                    | ✅      |
| canonical\_interface\_name         | ✅      |
| canonical\_interface\_name\_list   | ✅      |
| cidr\_to\_netmask                  | ✅      |
| cidr\_to\_netmaskv6                | ✅      |
| clean\_config                      | ✅      |
| compare\_version\_loose            | ✅      |
| compare\_version\_strict           | ✅      |
| config\_compliance                 | ✅      |
| config\_section\_not\_parsed       | ✅      |
| delimiter\_change                  | ✅      |
| diff\_network\_config              | ✅      |
| feature\_compliance                | ✅      |
| find\_unordered\_cfg\_lines        | ✅      |
| fqdn\_to\_ip                       | ❌      |
| get\_all\_host                     | ❌      |
| get\_broadcast\_address            | ✅      |
| get\_first\_usable                 | ✅      |
| get\_ips\_sorted                   | ✅      |
| get\_nist\_urls                    | ✅      |
| get\_nist\_vendor\_platform\_urls  | ✅      |
| get\_oui                           | ✅      |
| get\_peer\_ip                      | ✅      |
| get\_range\_ips                    | ✅      |
| get\_upgrade\_path                 | ✅      |
| get\_usable\_range                 | ✅      |
| hash\_data                         | ✅      |
| int\_to\_asdot                     | ✅      |
| interface\_range\_compress         | ✅      |
| interface\_range\_expansion        | ✅      |
| ip\_addition                       | ✅      |
| ip\_subtract                       | ✅      |
| ip\_to\_bin                        | ✅      |
| ip\_to\_hex                        | ✅      |
| ipaddress\_address                 | ✅      |
| ipaddress\_interface               | ✅      |
| ipaddress\_network                 | ✅      |
| is\_classful                       | ✅      |
| is\_fqdn\_resolvable               | ❌      |
| is\_ip                             | ✅      |
| is\_ip\_range                      | ✅      |
| is\_ip\_within                     | ✅      |
| is\_netmask                        | ✅      |
| is\_network                        | ✅      |
| is\_reversible\_wildcardmask       | ✅      |
| is\_valid\_mac                     | ✅      |
| longest\_prefix\_match             | ✅      |
| mac\_normalize                     | ✅      |
| mac\_to\_format                    | ✅      |
| mac\_to\_int                       | ✅      |
| mac\_type                          | ✅      |
| name\_to\_bits                     | ✅      |
| name\_to\_bytes                    | ✅      |
| name\_to\_name                     | ✅      |
| netmask\_to\_cidr                  | ✅      |
| netmask\_to\_wildcardmask          | ✅      |
| normalise\_delimiter\_caret\_c     | ✅      |
| paloalto\_panos\_brace\_to\_set    | ✅      |
| paloalto\_panos\_clean\_newlines   | ✅      |
| regex\_findall                     | ❌      |
| regex\_match                       | ❌      |
| regex\_search                      | ❌      |
| regex\_split                       | ❌      |
| regex\_sub                         | ❌      |
| sanitize\_config                   | ✅      |
| section\_config                    | ✅      |
| sort\_interface\_list              | ✅      |
| split\_interface                   | ✅      |
| uptime\_seconds\_to\_string        | ✅      |
| uptime\_string\_to\_seconds        | ✅      |
| version\_metadata                  | ✅      |
| vlanconfig\_to\_list               | ✅      |
| vlanlist\_to\_config               | ✅      |
| wildcardmask\_to\_netmask          | ✅      |

## Known issues[​](#known-issues "Direct link to Known issues")

### Unable to combine the map and sort filters (<https://github.com/pallets/jinja/issues/2081>)[​](#unable-to-combine-the-map-and-sort-filters-httpsgithubcompalletsjinjaissues2081 "Direct link to unable-to-combine-the-map-and-sort-filters-httpsgithubcompalletsjinjaissues2081")

When using the `map` filter with the `sort` filter, you may encounter the following error:

```
TypeError: 'async_generator' object is not iterable
```

**As a workaround you can use the `list` filter between `map` and `sort` filter.**
