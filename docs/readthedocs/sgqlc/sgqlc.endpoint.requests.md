# sgqlc.endpoint.requests module

## Synchronous HTTP Endpoint using python-requests

This endpoint implements GraphQL client using the `requests` [https://3.python-requests.org/api/#module-requests] library.

This module provides command line utility:

```
$ python3 -m sgqlc.endpoint.requests http://server.com/ '{ query { ... } }'

```