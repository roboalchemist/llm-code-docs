# Source: https://docs.espressosys.com/network/releases/mainnet-1/rollup-migration-guide.md

# Rollup Migration Guide

If you have a rollup using the Espresso network version 0 for confirmations, some changes are necessary in order to be compatible with version 1. These changes should be minimal. They must be completed before April 15 for the Decaf testnet. There is no date yet for upgrading Mainnet rollups.

**Estimated Effort:** 1 engineer-day

## Rust Integrations

1. Update dependencies:

<pre class="language-toml"><code class="lang-toml">hotshot-types = { git = "https://github.com/EspressoSystems/espresso-network", default-features = false, tag = "20250412-dev-node-pos-preview" }
<strong>hotshot-query-service = { git = "https://github.com/espressosystems/espresso-network", tag = "20250412-dev-node-pos-preview" }
</strong>espresso-types = { git = "https://github.com/espressosystems/espresso-network", tag = "20250412-dev-node-pos-preview" }
</code></pre>

2. The following types have been moved to different modules, so you may have to adjust some import statements:

```rust
use hotshot_query_service::VidCommon;
use hotshot_types::{data::VidCommitment, light_client::hash_bytes_to_field};
```

## Go Integrations

1. Update the Espresso Go SDK:

```go-module
require github.com/EspressoSystems/espresso-network-go v0.0.35
```

## All Integrations

1. Change the API you use to connect to the Espresso query service from `v0`to `v1`(as in `https://query.decaf.testnet.espresso.network/v1`or `https://query.main.net.espresso.network/v1`.
2. Test your integration with the new version of Espresso. You can run a local Espresso network in `v1`mode using a fork of the Espresso dev node, with the usual options: `ghcr.io/espressosystems/espresso-sequencer/espresso-dev-node:20250412-dev-node-pos-preview`
