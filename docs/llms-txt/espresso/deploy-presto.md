# Source: https://docs.espressosys.com/network/guides/dapp/deploy-presto.md

# Deploy and Use Presto, a Crosschain Minting Framework

Presto is a crosschain framework that lets users mint NFTs on one chain (the destination chain) while paying on another (the source chain). Crucially, this requires **no manual bridging of liquidity**. Instead, the user simply pays on the source chain, and the destination chain is securely convinced that these funds have been paid.

In this tutorial, you will learn how to deploy the Presto framework.

## Before Your Begin

* Clone the [composables-xchain-mint GitHub repository](https://github.com/EspressoSystems/composables-xchain-mint). \*\*This the original GitHub repo, which contains the contracts, scripts and configurations files.
* Clone the [presto-deployment-example GitHub repository](https://github.com/enoldev), which contains simplified version the configuration files you will use.
* Install the [Hyperlane CLI](https://docs.hyperlane.xyz/docs/reference/developer-tools/cli).
* Install [Docker](https://docs.docker.com/engine/install/) and Docker Compose.
* Install [Foundry](https://getfoundry.sh/).

In this tutorial, you will work with two different repositories: `composables-xchain-mint` contains the source code of Presto, docs, and many utility scripts. `presto-deployment-example` tries to abstract the complexity by focusing only on the necessary to deploy a simple version of Presto. However, you will still need to compile the contracts from the original source code using Foundry.

## Presto Architecture

For a complete overview of Presto's architecture, please [check out this Medium article](https://docs.espressosys.com/network/guides/dapp/deploy-presto). It is important to get familiar with the flow and the contracts involved before you start deploying.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-da06de2e4090553acfa0c6c71fca08dc64f8199a%2Fpresto-architecture.png?alt=media" alt=""><figcaption></figcaption></figure>

## Deployment

**IMPORTANT:** In this tutorial, you will deploy a bidirectional minting flow (`source -> destination` and `destination -> source`). However, you may only deploy one path.

### Overview

Deploying Presto involves several components that work together across chains:

**- Hyperlane Core Contracts:** the standard contracts required by Hyperlane to relay messages across chains (e.g., Mailbox, ProxyAdmin, ISM). You can either deploy your own instances or use Hyperlane’s canonical deployments on each chain.

**- Hyperlane Warp Routes:** contracts used to bridge value via Hyperlane. They convert native tokens on the source chain into synthetic representations on the destination chain (i.e., a representation of the source chain’s native token).

**- Hyperlane Warp Routes Upgrade:** Presto relies on a modified version of the Warp Routes contracts. After deploying the standard Warp Routes, they must be upgraded to use the Espresso-specific implementations.

**- NFT Contract:** the NFT contract deployed on the destination chain. This should be a standard ERC721 implementation.

**- Hyperlane Validator and Relayer:** the off-chain Hyperlane services responsible for observing messages on the source chain and delivering them to the destination chain. These components perform the actual cross-chain message passing.

### `.env` file

Throughout the tutorial, you will need to add the required addresses to the `.env` of the `presto-deployment-example` repo. Later, you will copy the file to `composables-xchain-mint/contracts`. This will be necessary to run the scripts and Foundry commands later.

At this moment, complete the following env variables:

* `DEPLOYER_ADDRESS`: address that you will use to deploy the contracts.
* `DEPLOYER_PRIVATE_KEY`: the private key of the deployer.
* `SOURCE_CHAIN_RPC_URL`: source chain's RPC.
* `DESTINATION_CHAIN_RPC_URL`: destination chain's RPC.
* `SOURCE_CHAIN_ID`: source chain's ID.
* `DESTINATION_CHAIN_ID`: destination chain's ID.
* `VALIDATOR_ADDRESS`: the address used by the validator to sign messages.

### Hyperlane Core Contracts

**NOTE:** If Hyperlane is officially deployed in both chains, you can skip this part and use Hyperlane's canonical Mailboxes and other contracts. However, for the purpose of this tutorial, it is recommended that you deploy everything from scratch.

1. In the `hyperlane/chains` folder of `presto-deployment-example` you will find the configuration file for both source and destination chain (in this case, Rari and Apechain).
2. If you want to deploy on different chains, update accordingly the `metadata.yaml` file with the correct RPC and metadata for your chain. **Move this `metadata.yaml` files to your Hyperlane path (usually, at `~/.hyperlane/chains`). This is where Hyperlane looks for chain configurations**
3. In the `core-config.yaml`, replace `<YOUR_OWNER_ADDRESS>` with the actual address that you will use as owner of the Hyperlane contract. The `core-config.yaml` file is the configuration file for the Hyperlane core contracts.
4. Deploy the Hyperlane core contracts (source chain) using the previous configuration files.

```bash
hyperlane core deploy  --config hyperlane/chains/source/core-config.yaml
```

4. Deploy the Hyperlane core contracts (destination chain) using the previous configuration files.

```bash
hyperlane core deploy  --config hyperlane/chains/destination/core-config.yaml
```

For both deployments, you will get the addresses of the deployed contracts. Include those addresses in the `.env` file:

* `SOURCE_MAILBOX_ADDRESS`
* `DESTINATION_MAILBOX_ADDRESS`
* `SOURCE_PROXY_ADMIN_ADDRESS`
* `DESTINATION_PROXY_ADMIN_ADDRESS`

You can also find the addresses in the `addresses.yaml` file that was generated.

### Hyperlane Warp Routes

Now, you will deploy the standard Hyperlane Warp Routes contracts, which you will later upgrade with the Espresso-specific versions.

1. In the `deployments/warp_routes/ETH` directory, you will find the deploy configurations for the Warp Routes.
2. Update the configuration files (`destination-deploy.yaml` and `source-deploy.yaml`) to include your owner address, the relayer address and the proxy admin address.
3. From the root directory (`presto-deployment-example`), run the following command to deploy the routes

```bash
hyperlane warp deploy  --registry hyperlane
```

**NOTE:** Run it two times: one for the source chain and another one for the destination chain.

4. As a result, you will get two files, `source-config.yaml` and `destination-config.yaml`, which include the addresses of the contract that were deployed.
5. In the `destination-config.yaml` file, you will find the source chain's `HypNative` contract and the destination's chain `HypSynthentic` contracts.

```yaml
# Native contract on source chain
- addressOrDenom: "<SOURCE_NATIVE_TOKEN_ADDRESS>"
    chainName: source
    ...
    standard: EvmHypNative
    symbol: ECWETH
```

```yaml
# Synthetic contract address on destination chain
- addressOrDenom: "<DESTINATION_SYNC_TOKEN_ADDRESS>"
    chainName: destination
    ...
    standard: EvmHypSynthetic
    symbol: ECWETH
```

The `source-config.yaml` file contains the address for the opposite flow (destination to source).

Include the addresses in the `.env` file:

```bash
DESTINATION_NATIVE_TOKEN_ADDRES=
DESTINATION_SYN_TOKEN_ADDRES=

SOURCE_NATIVE_TOKEN_ADDRESS=
SOURCE_SYN_TOKEN_ADDRESS=
```

### NFTs

**IMPORTANT:** First, move to the `composables-xchain-mint/contracts` folder (in the source code repository) and copy the `.env` file of the `presto-deployment-example` repo. The environment variables will be used for the deployment of the contracts.

Deploy the NFT contracts. In this case, you will deploy a very simple `MockERC721` contract.

1. Move to the `composables-xchain-mint/contracts` folder and build the contracts with Foundry (`forge build`).
2. Deploy the Mock contract on the source chain:

```bash
forge create MockERC721 --rpc-url $SOURCE_CHAIN_RPC_URL --private-key $PRIVATE_KEY --broadcast --via-ir --constructor-args $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export SOURCE_MARKETPLACE_ADDRESS=
```

3. Deploy the Mock contract on the destination chain:

```bash
forge create MockERC721 --rpc-url $DESTINATION_CHAIN_RPC_URL --private-key $PRIVATE_KEY --broadcast --via-ir --constructor-args $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export DESTINATION_MARKETPLACE_ADDRESS=
```

### Upgrade Warp Contracts

Now, you will replace the standard `HypNative` and `HypERC20` contracts with the Espresso-modified versions.

#### Upgrade the Source -> Destination Path

1. Deploy the `EspHypNative` contract on the source chain:

```bash
forge create src/EspHypNative.sol:EspHypNative \
  --private-key $DEPLOYER_PRIVATE_KEY --broadcast --via-ir --rpc-url $SOURCE_CHAIN_RPC_URL \
  --constructor-args 1 $SOURCE_MAILBOX_ADDRESS
```

Include the resulting address in the `.env` file:

```bash
export SOURCE_NATIVE_ADDRESS=
```

2. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata "initializeV2(uint256,uint32)" \
  $NFT_SALE_PRICE_WEI $DESTINATION_CHAIN_ID)
```

3. Perform the actual upgrade:

```bash
cast send $SOURCE_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $SOURCE_NATIVE_TOKEN_ADDRESS $SOURCE_NATIVE_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $SOURCE_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY
```

4. Deploy the `EspHypERC20` contract:

```bash
forge create src/EspHypERC20.sol:EspHypERC20 --private-key $DEPLOYER_PRIVATE_KEY  --broadcast --via-ir --rpc-url $DESTINATION_CHAIN_RPC_URL --constructor-args 18 1 $DESTINATION_MAILBOX_ADDRESS --from $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export DESTINATION_ERC20_ADDRESS=
```

5. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata "initializeV2(address,address,uint32,uint256)" \
  "$DESTINATION_MARKETPLACE_ADDRESS" \
  "$TREASURY_ADDRESS" \
  "$SOURCE_CHAIN_ID" \
  "$BRIDGE_BACK_PAYMENT_AMOUNT_WEI")
```

6. Perform the actual upgrade of the `EspHypERC20`:

```bash
cast send $DESTINATION_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $DESTINATION_SYN_TOKEN_ADDRES $DESTINATION_ERC20_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $DESTINATION_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY \
  --value 0
```

#### Upgrade the Destination -> Source Path

1. Deploy the `EspHypNative` contract on the destination chain:

```bash
forge create src/EspHypNative.sol:EspHypNative \
  --private-key $DEPLOYER_PRIVATE_KEY --broadcast --via-ir --rpc-url $DESTINATION_CHAIN_RPC_URL \
  --constructor-args 1 $DESTINATION_MAILBOX_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export DESTINATION_NATIVE_ADDRESS=
```

2. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata "initializeV2(uint256,uint32)" \
  $NFT_SALE_PRICE_WEI $SOURCE_CHAIN_ID)
```

3. Perform the actual upgrade:

```bash
cast send $DESTINATION_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $DESTINATION_NATIVE_TOKEN_ADDRES $DESTINATION_NATIVE_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $DESTINATION_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY \
  --value 0
```

4. Deploy the `EspHypERC20` contract on the source chain:

```bash
forge create src/EspHypERC20.sol:EspHypERC20 --private-key $DEPLOYER_PRIVATE_KEY --broadcast --via-ir --rpc-url $SOURCE_CHAIN_RPC_URL --constructor-args 18 1 $SOURCE_MAILBOX_ADDRESS --from $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export SOURCE_ERC20_ADDRESS=
```

5. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata \
  "initializeV2(address,address,uint32,uint256)" \
  "$SOURCE_MARKETPLACE_ADDRESS" \
  "$TREASURY_ADDRESS" \
  "$DESTINATION_CHAIN_ID" \
  "$BRIDGE_BACK_PAYMENT_AMOUNT_WEI")
```

6. Perform the actual upgrade:

```bash
cast send $SOURCE_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $SOURCE_SYN_TOKEN_ADDRESS $SOURCE_ERC20_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $SOURCE_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY \
  --value 0
```

### Hyperlane Validator and Relayer

Now, you will need to set up the validator and relayers nodes, which are Docker images.

1. Move to the `validator-relayer-setup` folder, which contains all the files needed to deploy the infra.
2. Update the `config/agent.json` file with all the needed configurations (Hyperlane address, validator private key, chain IDs and RPC URLs).
3. Run the Docker Compose command:

```bash
docker compose up -d
```

## Front-end Integration

Once you have the contracts deployed, you can easily create a front-end application that listens for the specific contract events, which will allow you to track the progress of a mint.

### Source Chain

1. Initialize the mint on the `initiateCrossChainNftPurchase` function of `EspHypNative` contract. You will need to provide the receipt address of the NFT (on the destination chain). Note that the caller address must have enough funds to pay for the NFT and gas fees.
2. Track the `TransferRemote` event from the `EspHypNative` contract and the `DispatchId` event from the Hyperlane Mailbox. **Save the Hyperlane's message ID in your application's state**.

By tracking the events above, you will know if writing the message to the Hyperlane Mailbox has succeded. Then, the validator and relayer must pick up the message and write to the destination chain.

### Destination Chain

1. Listen for `Transfer` events on the NFT contracts. For every `Transfer` event, check out `ProcessId` event (from Hyperlane's mailbox) event, which contains the message ID received.
2. Match the `ProcessId` event with the message ID that you saved previously.
