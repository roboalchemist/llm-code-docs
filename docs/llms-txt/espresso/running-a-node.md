# Source: https://docs.espressosys.com/network/releases/testnets/cappuccino-testnet-release/running-a-node.md

# Source: https://docs.espressosys.com/network/releases/testnets/decaf-testnet/running-a-node.md

# Running a Node

{% hint style="warning" %}
Decaf node operators are limited to a select group. If you are interested in running a node in a future release of Espresso, [contact us](https://y3at7jy5knf.typeform.com/to/KgayxNsX?typeform-source=webflow.com).
{% endhint %}

This page give the configuration used to run different types of nodes in the Decaf testnet. For general information on running an Espresso node, see <https://docs.espressosys.com/network/guides/node-operators/running-a-sequencer-node>.

All nodes in Decaf use the `ghcr.io/espressosystems/espresso-sequencer/sequencer:20251106-patch1` Docker image, or an equivalent image built from source. Depending on the type of node, the configuration varies.

{% hint style="info" %}
The configuration for all node types includes `ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml`. This file is built into the official Docker images. Operators building their own images will need to ensure [this file](https://github.com/EspressoSystems/espresso-network/blob/20250910-patch1/data/genesis/decaf.toml) is included and their nodes are pointed at it.
{% endhint %}

## Staking

Regardless of the type of node being operated, if you are starting a node for the first time, it will need to be registered in the stake table and have some stake delegated to it in order to participate in consensus.

{% hint style="info" %}
With the initial release of Proof-of-stake, participation is limited to a dynamic, permissionless set of 100 nodes. In each epoch (period of roughly 24 hours) the 100 nodes with the most delegated stake form the active participation set.
{% endhint %}

### Registering a Node

In order for a node to participate, it must be registered in the stake table contract on Ethereum Sepolia. During this process, the node's consensus keys are associated with a unique Ethereum address. This Ethereum address will receive commission, but does not exist on the node itself.

Interfacing with the stake table can be done using the `staking-cli`. Here is the command to use to register a node in the stake table:

```bash
docker run -e L1_PROVIDER -e STAKE_TABLE_ADDRESS -e MNEMONIC -e ACCOUNT_INDEX \
	-e CONSENSUS_PRIVATE_KEY -e STATE_PRIVATE_KEY \
	ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
	staking-cli register-validator \
	--commission $COMMISSION
```

Where:

| Environment Variable    | Meaning                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `L1_PROVIDER`           | The RPC provider URL to use when interacting with the L1. This should be an Ethereum Sepolia endpoint for Decaf                                                                                      |
| `STAKE_TABLE_ADDRESS`   | The Decaf stake table address. This is `0x40304fbe94d5e7d1492dd90c53a2d63e8506a037`                                                                                                                  |
| `MNEMONIC`              | The Ethereum mnemonic to use in combination with `ACCOUNT_INDEX` to derive an Ethereum keypair unique to this node                                                                                   |
| `ACCOUNT_INDEX`         | The Ethereum account index to use in combination with `MNEMONIC` to derive an Ethereum keypair unique to this node                                                                                   |
| `CONSENSUS_PRIVATE_KEY` | The node's staking-specific consensus key. This key looks something like: `BLS_SIGNING_KEY~...`                                                                                                      |
| `STATE_PRIVATE_KEY`     | The node's state-specific consensus key. This key looks something like: `SCHNORR_SIGNING_KEY~...`                                                                                                    |
| `COMMISSION`            | The proportion of rewards that the validator will earn, expressed as a decimal between 0 and 1 with up to two decimal places. The remaining rewards will be distributed proportionally to delegators |

Here are some additional requirements:

* Each Ethereum account used (derived from `MNEMONIC` + `ACCOUNT_INDEX`) must have enough gas funds on the L1 to call the registration method of the contract.
* Each BLS (Espresso) key can be registered only once.
* The commission cannot be changed later. One would need to deregister the validator, register another one, and direct delegators to redelegate in order to change it.
* Remember, each Ethereum account can only be used to register a single validator once. For multiple validators, at a minimum, different account indices (or mnemonics) must be used.

\
The output of a successful register transaction command should be of the following form:

{% code overflow="wrap" %}

```
2025-04-08T13:47:14.516160Z  INFO staking_cli: Registering validator 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 with commission 12.34 %
2025-04-08T13:47:14.829268Z  INFO staking_cli: Success! transaction hash: 0xa632dfea882d80855d2cc5e6713d9fc839cdd5df5aa29f6e9ce8d5a5ec8da615
```

{% endcode %}

### Deregistering a Node

At any time after registration, you may choose to stop participating by deregistering. This will automatically remove all of your delegators.

```bash
docker run \
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER \
    -e STAKE_TABLE_ADDRESS=0x40304fbe94d5e7d1492dd90c53a2d63e8506a037 \
    -e ESP_TOKEN_ADDRESS=0xb3e655a030e2e34a18b72757b40be086a8f43f3b \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        staking-cli deregister-validator
```

### Delegation

In order for a node to participate after it is registered, it must have Espresso tokens delegated to it. These can come from any users who hold Espresso tokens and wish to secure the network and earn rewards through staking. To bootstrap, it is possible for the node operator themselves to delegate to their own node, if they hold Espresso tokens.

To delegate to a registered node, the `staking-cli`can also be used:

```bash
docker run \
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER \
    -e STAKE_TABLE_ADDRESS=0x40304fbe94d5e7d1492dd90c53a2d63e8506a037 \
    -e ESP_TOKEN_ADDRESS=0xb3e655a030e2e34a18b72757b40be086a8f43f3b \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        delegate --validator-address $ADDRESS --amount $DELEGATION_AMOUNT
```

The delegation can always be removed using the `undelegate`command with the same arguments.

### More commands (+ Ledger support)

For more information on the staking CLI (including information on how to use it with a Ledger device), visit the README [here](https://github.com/EspressoSystems/espresso-network/blob/1fce836c0fcef7e0a2d0a2e981a22f122c22950a/staking-cli/README.md).

## Environment

When starting a node for the first time, set `ESPRESSO_SEQUENCER_CONFIG_PEERS`to the URL of a trusted node. This is used to fetch configuration required to join the P2P network. For example, this could be set to `https://cache.decaf.testnet.espresso.network` to use the Espresso Systems-operated nodes to fetch the config.

Once your node has successfully joined the network once, it should store the config locally, and this parameter will not be required on future restarts.

## 1. Regular Node

### Command

`sequencer -- http -- catchup -- status`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-UZAFTUIMZOT.decaf.testnet.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.decaf.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml
RUST_LOG="warn,hotshot_libp2p_networking=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.decaf.testnet.espresso.network
```

#### Chosen by operators

```
# An HTTP JSON-RPC endpoint for Sepolia testnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Sepolia testnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://sepolia.infura.io/v3/<API-KEY>

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

Note: Instead of using the above variable `$ESPRESSO_SEQUENCER_KEY_FILE` to load your keys from a file, you can also set the following two individually:

* `$ESPRESSO_SEQUENCER_PRIVATE_STAKING_KEY` -> `BLS_SIGNING_KEY~...`
* `$ESPRESSO_SEQUENCER_PRIVATE_STATE_KEY` -> `SCHNORR_SIGNING_KEY~...`

## 2. DA Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-UZAFTUIMZOT.decaf.testnet.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.decaf.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml
ESPRESSO_SEQUENCER_POSTGRES_PRUNE="true"
ESPRESSO_SEQUENCER_IS_DA="true"

RUST_LOG="warn,hotshot_libp2p_networking=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.decaf.testnet.espresso.network
```

#### Chosen by operators

```
# An HTTP JSON-RPC endpoint for Sepolia testnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Sepolia testnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://sepolia.infura.io/v3/<API-KEY>

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

### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

## Archival Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-UZAFTUIMZOT.decaf.testnet.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.decaf.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml
ESPRESSO_SEQUENCER_IS_DA=true
ESPRESSO_SEQUENCER_ARCHIVE=true

RUST_LOG="warn,hotshot_libp2p_networking=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.decaf.testnet.espresso.network
```

#### Chosen by operators

```
# An HTTP JSON-RPC endpoint for Sepolia testnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Sepolia testnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://sepolia.infura.io/v3/<API-KEY>

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

**Volumes**

* `$ESPRESSO_SEQUENCER_STORAGE_PATH`
* `$ESPRESSO_SEQUENCER_KEY_FILE`

Note: Instead of using the above variable `$ESPRESSO_SEQUENCER_KEY_FILE` to load your keys from a file, you can also set the following two individually:

* `$ESPRESSO_SEQUENCER_PRIVATE_STAKING_KEY` -> `BLS_SIGNING_KEY~...`
* `$ESPRESSO_SEQUENCER_PRIVATE_STATE_KEY` -> `SCHNORR_SIGNING_KEY~...`

## TCP optimizations

We ask also that operators perform some TCP optimizations to improve the networking performance of their nodes. Listed below are the different ways to apply them depending on how your node is set up:

### When using Docker Compose

Add the following to your `sequencer` service:

```
sysctls:
    net.ipv4.tcp_congestion_control: "bbr"
    net.ipv4.tcp_rmem: "8192 262144 67108864"
    net.ipv4.tcp_wmem: "4096 16384 536870912"
    net.ipv4.tcp_adv_win_scale: "0"
    net.ipv4.tcp_notsent_lowat: "131072"
    net.ipv4.tcp_slow_start_after_idle: "0"
```

### When just using Docker

Modify your `docker run` command like so:

```
docker run \
    --sysctl net.ipv4.tcp_congestion_control="bbr" \
    --sysctl net.ipv4.tcp_rmem="8192 262144 67108864" \
    --sysctl net.ipv4.tcp_wmem="4096 16384 536870912" \
    --sysctl net.ipv4.tcp_adv_win_scale="0" \
    --sysctl net.ipv4.tcp_notsent_lowat="131072" \
    --sysctl net.ipv4.tcp_slow_start_after_idle="0" \	
    ..
```

### When running natively

1. Create a file at `/etc/sysctl.d/espresso-opts.conf`
2. Add the following to it:

   ```
   net.ipv4.tcp_congestion_control=bbr
   net.ipv4.tcp_rmem=8192 262144 67108864
   net.ipv4.tcp_wmem=4096 16384 536870912 
   net.ipv4.tcp_adv_win_scale=0
   net.ipv4.tcp_notsent_lowat=131072
   net.ipv4.tcp_slow_start_after_idle=0
   ```
3. Run this command to apply the new settings without rebooting:

   ```
   sudo sysctl -p /etc/sysctl.d/espresso-opts.conf
   ```

Note: this will apply the TCP optimizations to *all* TCP connections on your machine.

## Hardware requirements

Hardware requirements are still in flux, but for now we recommend the following:

**Non-DA Node**: 1 Core CPU, 2GB memory\
\
**DA Node**: (Sequencer) 4 core CPU, 8GB memory + (Database) 2 Core, 4GB memory.

**Storage (DA node):** 1.2 TB SSD minimum, ability to scale on demand.

**Storage (non-DA Node):** Negligible, kilobytes
