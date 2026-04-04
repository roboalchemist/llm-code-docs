# Source: https://docs.espressosys.com/network/releases/mainnet-1/running-a-mainnet-1-node.md

# Running a Mainnet 1 Node

{% hint style="info" %}
🫵 TL;DR: For operator running Mainnet 0 nodes, the critical changes from that configuration are as follows:

* The new container image version is <https://github.com/EspressoSystems/espresso-network/pkgs/container/espresso-sequencer%2Fsequencer/703041349?tag=20260223>
* Use v1 APIs for all peer URLs
* The `state`API module is now required. It will be enabled automatically and should no longer be specified on the command line.
* Both `ESPRESSO_SEQUENCER_L1_PROVIDER` and `ESPRESSO_SEQUENCER_L1_WS_PROVIDER` now need to be provided. See the variables listed below for details
  {% endhint %}

The container image to use for this deployment is

* [Tag 20260302](https://github.com/EspressoSystems/espresso-network/pkgs/container/espresso-sequencer%2Fsequencer/713568135?tag=20260302)
* Which is built of the branch: [release-mainnet-1.0.1-rc](https://github.com/EspressoSystems/espresso-network/tree/release-mainnet-1.0.1-rc) if you are building from source

{% hint style="info" %}
The configuration for all node types includes `ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml`. This file is built into the official Docker images. Operators building their own images will need to ensure [this file](https://github.com/EspressoSystems/espresso-network/blob/20241120-patch5/data/genesis/mainnet.toml) is included and their nodes are pointed at it.
{% endhint %}

## Staking

Regardless of the type of node being operated, if you are starting a node for the first time, it will need to be registered in the stake table and have some stake delegated to it in order to participate in consensus.

{% hint style="info" %}
With the initial release of Mainnet 1, participation is limited to a dynamic, permissionless set of 100 nodes. In each epoch (period of roughly 24 hours) the 100 nodes with the most delegated stake form the active participation set.
{% endhint %}

### Registering a Node

In order for a node to participate, it must be registered in the stake table contract on Ethereum. During this process, the node's consensus keys are associated with a unique Ethereum address. This Ethereum address will receive commission, but does not exist on the node itself.

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
| `L1_PROVIDER`           | The RPC provider URL to use when interacting with the L1                                                                                                                                             |
| `STAKE_TABLE_ADDRESS`   | The Mainnet stake table address. This is 0xCeF474D372B5b09dEfe2aF187bf17338Dc704451                                                                                                                  |
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
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER -e ESP_TOKEN_ADDRESS=0x031De51F3E8016514Bd0963d0B2AB825A591Db9A \
    -e STAKE_TABLE_ADDRESS=0xCeF474D372B5b09dEfe2aF187bf17338Dc704451 \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        staking-cli deregister-validator
```

### Delegation

In order for a node to participate after it is registered, it must have Espresso tokens delegated to it. These can come from any users who hold Espresso tokens and wish to secure the network and earn rewards through staking. To bootstrap, it is possible for the node operator themselves to delegate to their own node, if they hold Espresso tokens.

To delegate to a registered node, the `staking-cli`can also be used:

```bash
docker run \
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER -e ESP_TOKEN_ADDRESS=0x031De51F3E8016514Bd0963d0B2AB825A591Db9A \
    -e STAKE_TABLE_ADDRESS=0xCeF474D372B5b09dEfe2aF187bf17338Dc704451 \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        delegate --validator-address $ADDRESS --amount $DELEGATION_AMOUNT
```

The delegation can always be removed using the `undelegate`command with the same arguments.

### More commands (+ Ledger support)

For more information on the staking CLI (including information on how to use it with a Ledger device), visit the README [here](https://github.com/EspressoSystems/espresso-network/blob/1fce836c0fcef7e0a2d0a2e981a22f122c22950a/staking-cli/README.md).

## Environment

When starting a node for the first time, set `ESPRESSO_SEQUENCER_CONFIG_PEERS`to the URL of a trusted node. This is used to fetch configuration required to join the P2P network. For example, this could be set to `https://cache.main.net.espresso.network` to use the Espresso Systems-operated nodes to fetch the config.

Once your node has successfully joined the network once, it should store the config locally, and this parameter will not be required on future restarts.

## 1. Regular Node

#### Command

```
sequencer -- http -- catchup -- status
```

Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_EMBEDDED_DB=true
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

# Path in container to store sqlite database
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
Requires operator to additionally run a Postgres server. There is no need to run a DA node unless you are included in the DA committee. Most operators can ignore this.
{% endhint %}

#### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_POSTGRES_PRUNE="true"
ESPRESSO_SEQUENCER_IS_DA="true"
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network/v1
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network/v1
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

`sequencer -- storage-sql -- http -- catchup -- status -- query`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_IS_DA=true
ESPRESSO_SEQUENCER_ARCHIVE=true
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network/v1
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network/v1
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

Note: Instead of using the above variable `$ESPRESSO_SEQUENCER_KEY_FILE` to load your keys from a file, you can also set the following two individually:

* `$ESPRESSO_SEQUENCER_PRIVATE_STAKING_KEY` -> `BLS_SIGNING_KEY~...`
* `$ESPRESSO_SEQUENCER_PRIVATE_STATE_KEY` -> `SCHNORR_SIGNING_KEY~...`

## Hardware requirements

Hardware requirements are still in flux, but for now we recommend the following:

**Non-DA Node**: 1 Core CPU, 8GB memory\
\
**DA Node**: (Sequencer) 4 core CPU, 8GB memory + (Database) 2 Core, 4GB memory.

**Storage (DA node):** 1.2 TB SSD minimum, ability to scale on demand.

**Storage (Pruning DA node):** 100 GB

**Storage (non-DA Node):** Negligible, kilobytes
