# Source: https://docs.nomad.xyz/developers/node-operators/running-agents-guide.md

# Running Agents Guide

### Overview <a href="#overview" id="overview"></a>

Nomad agent processes observe and index on-chain events, interacting with multiple blockchains in order to facilitate cross-chain messaging.

{% hint style="info" %}
See the [Off-Chain Agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents) section for details on each agent role.
{% endhint %}

#### Home/Replica Model

Nomad channels are d*ual-simplex*. This simply means they are composite bi-directional communication channels between two given blockchains. Each composite channel is composed of a single data channel flowing in one direction paired with a corresponding data channel flowing in the opposite direction.  These data channels flow outward from the [Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) on each blockchain.&#x20;

Agents are architected in a Home-centric model, meaning that by default agents must be configured with secrets like signing keys and RPC endpoints for each blockchain that the configured Home has a Replica on.

This means if you want to facilitate bi-directional communication between two or more networks (or *Watch* both directions of a channel), *you must run one agent instance per Home.*

{% hint style="info" %}
If that didn't make much sense, go read [Cross-Chain Messaging](https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging) and come back.
{% endhint %}

### Configuring an Agent <a href="#configuring-an-agent" id="configuring-an-agent"></a>

Agents are simple Rust binaries that are easily run inside [Docker Containers](https://www.docker.com/). Agents read runtime configuration from a mix of JSON config files and environment variables.&#x20;

Configuration is loaded in the following order:&#x20;

1. Built-In Configuration&#x20;
2. Configuration File&#x20;
3. Environment Variables

#### Nomad Configuration Repository

Nomad publishes JSON configurations for each of the three public environments we operate, they can be found in the [Nomad Configuration Repository](https://github.com/nomad-xyz/config) on Github. These configs provide public network info such as contract addresses and chain finality settings which the agents consume.&#x20;

By default, agents get compiled with the JSON environment configuration that was available at compile-time, however this config can be optionally overridden at runtime via the `CONFIG_PATH` environment variable. &#x20;

#### Environment Variables&#x20;

The agent has specific required environment variables, but additionally supports specific additional configuration overrides. The key fields one must specify are detailed below.&#x20;

{% hint style="info" %}
Note:`DEFAULT`\_ values are only used if a network-specific override is not provided.
{% endhint %}

#### **Run Environment**

* `RUN_ENV`: Used to switch between built-in environments \
  `development`, `staging`, or `production`&#x20;

#### **Agent Home**

* `AGENT_HOME_NAME`: A network name which the agent will treat as *Home*, see [built-in configs](https://github.com/nomad-xyz/config) for details

#### **Agent Replicas**

* Specify networks:
  * `AGENT_REPLICA_0_NAME`, `AGENT_REPLICA_1_NAME`, `AGENT_REPLICA_2_NAME`, etc...
  * What replica(s) the agent will run against
* Default to all connected networks:
  * `AGENT_REPLICAS_ALL`
  * Expects all connected replicas if `true`
  * Expects specified networks if `false` or not set

#### **RPC Info**

* Network-specific:
  * `{network}_RPCSTYLE`: What RPC style `network` is; "ethereum" for all EVM chains
  * `{network}_CONNECTION_URL`: RPC endpoint url
* Default:
  * `DEFAULT_RPCSTYLE`: Default rpc style for any network not explicitly configured

#### **Transaction Submission Info**

* Network-specific:
  * Transaction Submission Type:
    * `{network}_SUBMITTER_TYPE`
    * `local` for local signing/submitting
    * `gelato` if you are integrated with Gelato Relay
  * Local Submission:
    * Transaction signer key:
      * Hex key:
        * `{network}_TXSIGNER_KEY`
        * Raw 0x-prefixed hex key
      * AWS Key:
        * `{network}_TXSIGNER_ID`
        * AWS key id
  * Gelato Submission (ignore if you do not plan on using Gelato Relay):
    * Sponsor signer:
      * Hex key:
        * `{network}_GELATO_SPONSOR_KEY`
        * Raw 0x-prefixed hex key
      * AWS Key:
        * `{network}_GELATO_SPONSOR_ID`
        * AWS key id
    * Fee token
      * `{network}_GELATO_SPONSOR_FEETOKEN`
      * 0x-prefixed token contract address
* Default:
  * Default for any network not explicitly configured
  * Same as network-specific (above) but replacing specific `{network}` with `DEFAULT`
  * Example:
    * `DEFAULT_SUBMITTER_TYPE=local`
    * `DEFAULT_TXSIGNER_ID=some_aws_id`
    * All networks use `local` transaction submission with the default txsigner key

#### **Attestation Signer (optional)**

* Required *only* for updater and watcher
* Hex key:
  * `ATTESTATION_SIGNER_KEY`
  * Raw 0x-prefixed hex key
* AWS Key:
  * `ATTESTATION_SIGNER_ID`
  * AWS key id<br>

**Agent Configuration Overrides (optional)**

Agents also have configuration settings that can be optionally overridden by environment variables. If present, these variables will override values given by configuration files.

#### **All Agents**

* Agent interval:
  * `{agent}_INTERVAL`
  * The frequency at which an agent runs its loop in milliseconds

#### **Kathy**

* Chat config:
  * Recipient:
    * `KATHY_CHAT_RECIPIENT`
    * 0x-prefixed recipient address
  * Message:
    * `KATHY_CHAT_MESSAGE`
    * A message string
  * Message list:
    * `KATHY_CHAT_MESSAGES`
    * A quoted, comma separated list of message strings
  * Random messages:
    * `KATHY_CHAT_RANDOM`
    * An integer value for the number of random messages to send

#### **Processor**

* Allowed senders:
  * `PROCESSOR_ALLOWED`
  * A comma separated list of 0x-prefixed sender addresses
* Denied senders:
  * `PROCESSOR_DENIED`
  * A comma separated list of 0x-prefixed sender addresses
* Subsidized remotes:
  * `PROCESSOR_SUBSIDIZED_REMOTES`
  * A comma separated list of network names
* S3 Bucket:
  * AWS Bucket:
    * `PROCESSOR_S3_BUCKET`
    * AWS bucket id
  * AWS Region:
    * `PROCESSOR_S3_REGION`
    * AWS region id

For an example of agent configuration overrides, please see our [example overrides env file](https://github.com/nomad-xyz/rust/blob/main/fixtures/env.test-agents).

### Running Agent <a href="#running-agent" id="running-agent"></a>

AWS Keys: Note that the AWS `key_id` field can be a key id, key name, alias name, or alias ARN, as documented in the [Rusoto KMS docs](https://docs.rs/rusoto_kms/latest/rusoto_kms/struct.GetPublicKeyRequest.html#structfield.key_id). For more information on configuring AWS credentials, please refer to the [Rusoto AWS credentials usage documentation](https://github.com/rusoto/rusoto/blob/master/AWS-CREDENTIALS.md#credentials).

For more info on our different run environments and key configuration/provisioning, please refer to our [agents operations page](https://docs.nomad.xyz/developers/node-operators/agent-operations).

You can see an example .env file below:

```
# Only runs agent for Ethereum <> Moonbeam channel (production)
RUN_ENV=production
AGENT_HOME_NAME=ethereum
AGENT_REPLICA_0_NAME=moonbeam

# can provide default rpc style for all networks, or specify network specific
# network-specific values always override the default
DEFAULT_RPCSTYLE=ethereum
ETHEREUM_RPCSTYLE=ethereum
MOONBEAM_RPCSTYLE=ethereum

# provide network-specific RPC endpoints
ETHEREUM_CONNECTION_URL=https://main-light.eth.linkpool.io/
MOONBEAM_CONNECTION_URL=https://rpc.api.moonbeam.network

# we will default to local transaction signing/submission
DEFAULT_SUBMITTER_TYPE=local

# can provide tx signer as hex key (for ethereum) or aws key (for moonbeam)
# again, default tx signer is overriden by network-specifics
DEFAULT_TXSIGNER_KEY=0x1111111111111111111111111111111111111111111111111111111111111111
ETHEREUM_TXSIGNER_KEY=0x1111111111111111111111111111111111111111111111111111111111111111
MOONBEAM_TXSIGNER_ID=dummy_id

# can provide attestation signer as aws or hex key
ATTESTATION_SIGNER_ID=dummy_id
```

If you would like to configure an agent to run against all connected networks (against all replicas the home is connected to), see [this example](https://github.com/nomad-xyz/rust/blob/main/fixtures/env.test). For more examples of .env files, see our [test fixtures folder](https://github.com/nomad-xyz/rust/tree/main/fixtures).

Once you have populated a .env file, running an agent is as simple as running the following command:

`env $(cat .env | xargs) cargo run --bin <AGENT>`

This will build the codebase and run the specified `<AGENT>` binary (updater, relayer, processor, or watcher) using the provided environment variables.

### Agents Release Process <a href="#agents-release-process" id="agents-release-process"></a>

Our release process follows a monthly cadence. We follow [Semantic Versioning](https://semver.org/), where breaking changes constitute changes that break agent configuration compatibility.

We manage releases through GitHub. You can find new per-agent releases [here](https://github.com/nomad-xyz/rust/releases).

### Production Builds <a href="#production-builds" id="production-builds"></a>

When making changes to the Rust codebase, it is important to ensure the Docker build used in production environments still works. You can check this automatically in CI as it is built on every PR ([see docker workflow here](https://github.com/nomad-xyz/rust/blob/main/.github/workflows/docker.yml)), however you can check it much faster usually by attempting to build it locally.

You can build the docker image by running the following script in the `rust` directory:

`./build.sh latest`

If that goes smoothly, you can rest assured it will most likely also work in CI.
