# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api/status-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api/status-api.md

# Status API

This API provides insight into the inner workings of consensus. It is primarily useful to the operator of the node, as many of the metrics provided here make for useful [alerts](https://github.com/EspressoSystems/gitbook/blob/main/guides/running-a-sequencer-node.md#monitoring).

## Endpoints

### GET `/status/block-height`

The last known block height of the chain.

#### Returns `integer`

### GET `/status/success-rate`

The view success rate since genesis. This equals the number of views completed divided by the number of successful views, i.e. the block height.

#### Returns `float`

### GET `/status/time-since-last-decide`

The elapsed time, in seconds, since consensus last decided on a block. Useful to alert when consensus is stalled or this node has been disconnected from consensus.

#### Returns `integer`

### GET `/status/metrics`

Exposes all metrics recorded by consensus in Prometheus format.
