# Migration Guide

## Migrating from v6 to v7

web3.py follows Semantic Versioning [http://semver.org], which means that
version 7 introduced backwards-incompatible changes. If you’re upgrading from
web3.py `v6` or earlier, you can expect to need to make some changes. Refer
to this guide for a summary of breaking changes when updating from `v6` to
`v7`. If you are more than one major version behind, you should also review
the migration guides for the versions in between.

### Provider Updates

#### WebSocketProvider

`WebsocketProviderV2`, introduced in web3.py `v6`, has taken priority over the
legacy `WebsocketProvider`. The `LegacyWebSocketProvider` has been deprecated in
`v7` and is slated for removal in the next major version of the library. In summary:

-

`WebsocketProvider` -> `LegacyWebSocketProvider` (and deprecated)

-

`WebsocketProviderV2` -> `WebSocketProvider`

If migrating from `WebSocketProviderV2` to `WebSocketProvider`, you can expect the
following changes:

-

Instantiation no longer requires the `persistent_websocket` method:

```
# WebsocketsProviderV2:
AsyncWeb3.persistent_websocket(WebsocketProviderV2('...'))

# WebSocketProvider:
AsyncWeb3(WebSocketProvider('...'))

```
