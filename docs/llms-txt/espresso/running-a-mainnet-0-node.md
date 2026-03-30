# Source: https://docs.espressosys.com/network/releases/mainnet-0/running-a-mainnet-0-node.md

# Running a Mainnet 0 Node

{% hint style="warning" %}
Note: during Mainnet 0 only a fixed set of preregistered operators can run a node. The Espresso Network will upgrade to proof-of-stake in a later release.
{% endhint %}

{% hint style="info" %}
🫵 TL;DR: For operator running Decaf nodes, the critical changes from that configuration are as follows:

* All URLs supplied by Espresso have changed
* The new container image version is `20250228-patch3`
* The JSON-RPC endpoints specified by `ESPRESSO_SEQUENCER_L1_PROVIDER` and `ESPRESSO_SEQUENCER_L1_WS_PROVIDER` should be Ethereum mainnet endpoints instead of Sepolia
  {% endhint %}

The container image to use for this deployment is

* `ghcr.io/espressosystems/espresso-sequencer/sequencer:20250228-patch3` (if using Espresso's images)
* built off of the branch `20250228-patch3` (if building from source)

{% hint style="info" %}
The configuration for all node types includes `ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml`. This file is built into the official Docker images. Operators building their own images will need to ensure [this file](https://github.com/EspressoSystems/espresso-network/blob/20241120-patch5/data/genesis/mainnet.toml) is included and their nodes are pointed at it.
{% endhint %}

## 1. Regular Node

#### Command

```
sequencer -- http -- catchup -- status
```

Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-kdrhoi6lwz.main.net.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics and healthchecks
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to store consensus state
ESPRESSO_SEQUENCER_STORAGE_PATH # e.g. /mount/sequencer/store/

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

**Volumes**

* `$ESPRESSO_SEQUENCER_STORAGE_PATH`
* `$ESPRESSO_SEQUENCER_KEY_FILE`

## 2. DA Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

#### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-kdrhoi6lwz.main.net.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_POSTGRES_PRUNE="true"
ESPRESSO_SEQUENCER_IS_DA="true"
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and DA API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

#### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

#### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query -- state`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-kdrhoi6lwz.main.net.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_IS_DA=true
ESPRESSO_SEQUENCER_ARCHIVE=true
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and query API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

#### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

## Hardware requirements

Hardware requirements are still in flux, but for now we recommend the following:

**Non-DA Node**: 1 Core CPU, 2GB memory\
\
**DA Node**: (Sequencer) 4 core CPU, 8GB memory + (Database) 2 Core, 4GB memory.

**Storage (DA node):** 1.2 TB SSD minimum, ability to scale on demand.

**Storage (non-DA Node):** Negligible, kilobytes
