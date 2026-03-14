# sgqlc.endpoint module

## Access GraphQL endpoints using Python

This package provide the following modules:

- 

`sgqlc.endpoint.base`: with abstract class
`sgqlc.endpoint.base.BaseEndpoint` and helpful logging
utilities to transform errors into JSON objects.

- 

`sgqlc.endpoint.http`: concrete
`sgqlc.endpoint.http.HTTPEndpoint` using
`urllib.request.urlopen()` [https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen].

- 

`sgqlc.endpoint.requests`: concrete
`sgqlc.endpoint.requests.RequestsEndpoint` using
`requests` [https://3.python-requests.org/api/#module-requests] .

- 

`sgqlc.endpoint.websocket`: concrete
`sgqlc.endpoint.websocket.WebSocketEndpoint` using
`websocket._core.create_connection()` [https://websocket-client.readthedocs.io/en/latest/core.html#websocket._core.create_connection].