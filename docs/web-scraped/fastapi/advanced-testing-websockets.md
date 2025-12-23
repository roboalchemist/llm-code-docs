# Source: https://fastapi.tiangolo.com/advanced/testing-websockets/

# Testing WebSockets[&para;](#testing-websockets)

You can use the same `TestClient` to test WebSockets.

For this, you use the `TestClient` in a `with` statement, connecting to the WebSocket:

Python 3.9+

Note

For more details, check Starlette's documentation for [testing WebSockets](https://www.starlette.dev/testclient/#testing-websocket-sessions).