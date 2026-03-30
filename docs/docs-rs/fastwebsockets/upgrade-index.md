fastwebsockets

# Module upgrade

Source Available on **crate feature `upgrade`** only.

## Structs§

IncomingUpgradeUpgradeFutA future that resolves to a websocket stream when the associated HTTP upgrade completes.

## Functions§

is_upgrade_requestCheck if a request is a websocket upgrade request.upgradeTry to upgrade a received `hyper::Request` to a websocket connection.
