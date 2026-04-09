# sgqlc.endpoint.base module

## Base Endpoint

Base interface for endpoints.

See concrete implementations:

- 

`sgqlc.endpoint.http.HTTPEndpoint` using
`urllib.request.urlopen()` [https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen].

- 

`sgqlc.endpoint.requests.RequestsEndpoint` using
`requests` [https://3.python-requests.org/api/#module-requests].

- 

`sgqlc.endpoint.websocket.WebSocketEndpoint` using
`websocket._core.create_connection()` [https://websocket-client.readthedocs.io/en/latest/core.html#websocket._core.create_connection].