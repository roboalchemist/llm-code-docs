# sgqlc.endpoint.http module

## Synchronous HTTP Endpoint

This endpoint implements GraphQL client using
`urllib.request.urlopen()` [https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen] or compatible function.

This module provides command line utility:

```
$ python3 -m sgqlc.endpoint.http http://server.com/ '{ queryHere { ... } }'

```