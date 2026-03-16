# Source: https://docs.espressosys.com/network/guides/rollup-developers/nitro/migrate-orbit-chains-to-espresso.md

# Migrate an Existing Orbit Chain to Espresso

## Espresso Nitro Integration

{% hint style="info" %}
You may wish to familiarize yourself with the [security audits](https://github.com/EspressoSystems/espresso-audits/blob/main/external-reviews/EspressoNitroIntegration-2025.pdf) for this integration.
{% endhint %}

The target audience for this document are developers who would like to migrate an existing Arbitrum Orbit chain to use Espresso's Global Confirmation Layer (GCL). The document should also be interesting for developers who are thinking of deploying a new Arbitrum Orbit chain that uses Espresso's GCL.

The goal of this document is to describe how to migrate an Arbitrum Orbit chain to using Espresso's global confirmation layer for fast confirmations. By leveraging Espresso's fast confirmations, a rollup will only accept a batch after it has been finalized by Espresso. This integration ensures that each batch processed by the rollup is consistent with HotShot-finalized blocks within its namespace.

### Quickstart

The quickest way to get familiar with what the migration entails is to run through our [migration test](https://github.com/EspressoSystems/nitro-testnode/blob/integration/espresso-tests/migration-test.bash).

The script creates up an ephemeral Nitro chain on the local computer and migrates it to using Espresso's Global Confirmation Layer (also running locally on the computer). This test mocks out the TEE part by using a mocked TEE verifier contract and configured the batch poster to bypass the TEE interactions. Thereby it's possible to run through the migration locally, without requiring a special CPU and extra software to support the TEE.

{% hint style="warning" %}
For a safe production deployment the TEE is required and the real TEE verifier contract must be deployed.
{% endhint %}

The test requires [Docker](https://docs.docker.com/engine/install/), [Foundry](https://book.getfoundry.sh/getting-started/installation), [Yarn](https://classic.yarnpkg.com/lang/en/docs/install), `openssl` and `jq` to be installed.

For convenience the nix package manager can take care of installing all dependencies except for Docker. Nix can be installed by running

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

To run the test first some setup:

```bash
git clone --recursive https://github.com/EspressoSystems/nitro-testnode
cd nitro-testnode
git checkout integration
nix develop # omit if you have foundry, yarn, jq, openssl installed already
```

Now you can run the test itself.

```bash
espresso-tests/migration-test.bash
```

You may need to run the following command to ensure the submodules are initialized:

```bash
git submodule update --init --recursive
```

You should see substantial output. The first time you run this, it can take up to 15-20 minutes due to initial setup steps like installing dependencies. Subsequent runs should take less than 10 minutes.

After some time, if successful, you should see **Migration successfully completed!**.

> **⚠️ Warning:** If you see "Waiting for confirmed nodes" logs for more than 60 seconds, it's recommended to restart the process.

It's encouraged to read through the [migration test](https://github.com/EspressoSystems/nitro-testnode/blob/integration/espresso-tests/migration-test.bash) to get an idea of all the steps involved and what information is required for each step. For the real migration using `.env` files instead of environment variables to provide the necessary inputs may be more convenient.

Once familiar, you might run some commands to further your understanding. Transfer some eth, for example:

```bash
cast send $RECIPIENT_ADDRESS --value 1ether --rpc-url $CHILD_CHAIN_RPC_URL --private-key $PRIVATE_KEY
```

### Assumptions

Before attempting a migration please verify that the assumptions listed here make sense for your nitro deployment. If not, please get in touch with us via our [contact form](https://y3at7jy5knf.typeform.com/to/KgayxNsX?typeform-source=www.espressosys.com).

1. The Orbit chain to be migrated is using vanilla Nitro stack, or Celestia DA via the [Celestia fork of nitro](https://github.com/celestiaorg/nitro). If your Orbit chain is using Celestia for DA you need to use the `celestia-integration` branches of Espresso's nitro forks.
2. You are able to run the batch poster in an SGX TEE environment. This is required to provide TEE attestations that the L2 transactions have been finalized by Espresso. These attestations are verified in the TEE verifier smart contract on the parent chain as part of the batch submission.

### Production Setup Requirements

For production migrations, you will need the following system requirements (note: these are not needed for running the test migration):

* SGX
* Gramine
* [16GB RAM](https://docs.arbitrum.io/run-arbitrum-node/run-full-node#minimum-hardware-configuration)

You will also need these Espresso projects. Depending on whether you use celestia DA or not, you will need either the `integration` branch or `celestia-integration` branch. Please take the time to review each project's respective README.

* <https://github.com/EspressoSystems/nitro-espresso-integration>
* <https://github.com/EspressoSystems/nitro-contracts>
* <https://github.com/EspressoSystems/nitro-testnode>
* <https://github.com/EspressoSystems/orbit-actions>
* <https://github.com/EspressoSystems/gsc>

As well as [Espresso's nitro-node](https://github.com/EspressoSystems/nitro-espresso-integration/pkgs/container/nitro-espresso-integration%2Fnitro-node) docker image:

```
 ghcr.io/espressosystems/nitro-espresso-integration/nitro-node:v3.3.2-fcd633f
```

## Migration Flow

{% hint style="info" %}
This flow is more precisely defined in our [migration test](https://github.com/EspressoSystems/nitro-testnode/blob/integration/espresso-tests/migration-test.bash). Since that script is intended for testing migrations, it does not not require SGX. Therefore it should not be use for production deployments.
{% endhint %}

1. Run the new batch poster inside SGX and get the `MREnclave` and `MRSigner` values (which is the hash of the code running inside the SGX). These values are needed to deploy the EspressoTEEVerifier contract.
2. Deploy the `EspressoTEEVerifier` contract.
3. Stop Nitro node with the batch poster and copy the batch poster's databases files to the TEE.
4. Perform the sequencer inbox migration.
5. Run new Batch poster. You will notice it starts catching up messages and building up state.

{% hint style="info" %}
Please also be aware of [steps to revert a migration](https://github.com/EspressoSystems/orbit-actions/tree/integration/migration#5-reverting) should you need them.
{% endhint %}

### Verify SGX Setup

{% hint style="info" %}
Setup of SGX TEE is beyond the scope of this document. We have had success with [Azure SGX VMs](https://learn.microsoft.com/en-us/azure/confidential-computing/virtual-machine-solutions-sgx)
{% endhint %}

First verify you have linux version with in-kernel SGX. To ensure you have in-kernel SGX run the following command to verify you are running a Linux kernel greater than version `5.11`.

```bash
uname -r
```

Ensure that your machine has an [Intel SGX2](https://www.intel.com/content/www/us/en/architecture-and-technology/software-guard-extensions.html) (Software Guard Extensions) enabled CPU to run our batch poster (See [here](https://www.kernel.org/doc/html/next/x86/sgx.html) and [here](https://github.com/intel/SGXDataCenterAttestationPrimitives/blob/main/driver/linux/README.kernel.md#transition-from-dcap-driver-to-kernel)). You can verify if your CPU supports SGX2 on Linux by inspecting CPU information:

```
grep -i sgx /proc/cpuinfo
```

If your CPU supports SGX, the output should resemble the following. If it does not, your CPU either doesn't support SGX2, or it isn't enabled in the BIOS.

```
 SGX2 supported                           = true
```

### Install Gramine

To install gramine follow the following instructions:

1. Install [software packages](https://gramine.readthedocs.io/projects/gsc/en/latest/#software-packages)
2. Setup [host configuration](https://gramine.readthedocs.io/projects/gsc/en/latest/#host-configuration)
3. Install the [SGX software stack](https://gramine.readthedocs.io/en/stable/devel/building.html#install-dependencies)
4. If your machine is running on Microsoft Azure, you can refer to [this document](https://learn.microsoft.com/en-us/azure/security/fundamentals/trusted-hardware-identity-management) for configuring aesm.

You don't need to follow the [build gramine steps](https://gramine.readthedocs.io/en/stable/devel/building.html#build-gramine) as we will be using [Gramine Shielded Containers (GSC)](https://gramine.readthedocs.io/projects/gsc/en/latest/#host-configuration)

At this point `systemctl status aesmd` should report a healthy service (**Active: active (running)**).

If you see any errors here, ensure your `aesmd` is configured properly. If your machine is running on Microsoft Azure, you can refer to [this document](https://learn.microsoft.com/en-us/azure/security/fundamentals/trusted-hardware-identity-management) for configuring `aesm`.

### Running the Batch Poster Inside SGX

#### Building the Poster Image

{% hint style="warning" %}
These steps need to happen inside SGX
{% endhint %}

Use our default [`Dockerfile.sgx-poster`](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/Dockerfile.sgx-poster) or the Celestia [`Dockerfile.sgx-poster`](https://github.com/EspressoSystems/nitro-espresso-integration/blob/celestia-integration/Dockerfile.sgx-poster) to build the sgx-poster Docker image.

First obtain the source:

```
git clone https://github.com/EspressoSystems/nitro-espresso-integration
cd nitro-espresso-integration
```

* Alternative 1: using default Nitro stack

  ```
    git checkout integration
  ```
* Alternative 2: using Celestia DA

  ```
    git checkout celestia-integration
  ```

Then build the image.

```bash
docker build -f Dockerfile.sgx-poster -t sgx-poster .
```

#### Building the Gramine Image

Once the docker image is built, you need to build a Gramine Shielded Container (GSC) image.

The `gsc` python script requires a few python packages. For ubuntu 24.04 run

```bash
sudo apt-get install -y python3 python3-docker python3-jinja2 python3-tomli python3-tomli-w python3-yaml
```

For more information see the [GSC docs](https://gramine.readthedocs.io/projects/gsc/en/latest/#software-packages).

Clone Espresso's `gsc` repo and build the Gramine image:

```
git clone https://github.com/EspressoSystems/gsc.git
cd gsc
git checkout master
cp config.yaml.template config.yaml
./gsc build sgx-poster ./nitro-espresso.manifest
```

Now before building the gramine image, you need to edit your `poster_config.json` file to include the following fields (given parent chain is arbitrum sepolia):

```
"batch-poster": {
    "hotshot-url": "https://query.decaf.testnet.espresso.network/v0",
    "light-client-address": "0x08d16cb8243b3e172dddcdf1a1a5dacca1cd7098",
    "resubmit-espresso-tx-deadline": "2m"
},
"transaction-streamer": {
    "user-data-attestation-file": "/dev/attestation/user_report_data",
    "quote-file": "/dev/attestation/quote"
}
```

You need the sha256 hash of your poster\_config.json file. You can get the hash using the following command:

```bash
sha256sum poster_config.json
```

Replace the `nitro-espresso.manifest` in the gsc with these contents and replace the `<YOUR_SHA256_HERE>` with the sha256 of your poster\_config.json file.

```
sys.enable_extra_runtime_domain_names_conf = true
sgx.edmm_enable = true
sgx.remote_attestation = "dcap"
sgx.use_exinfo = true
sys.experimental__enable_flock = true
fs.mounts = [
    { path = "/home/user/.arbitrum/", uri = "file:/home/user/.arbitrum"},
    { path = "/config/", uri = "file:/config"}
]
sgx.allowed_files = ["file:/home/user/.arbitrum"]
[[sgx.trusted_files]]
uri = "file:/home/user/kzg10-aztec20-srs-1048584.bin"
sha256 = "cded83e82e4b49fee4cb2e0f374f996954fe12548ad39100432ee493069ef09d"
[[sgx.trusted_files]]
uri = "file:/config/poster_config.json"
sha256 = "<YOUR_SHA256_HERE>"
```

Next we will need to sign the image in order to run this container inside the SGX enclave.

Generate the signing key (if you don't already have one).

```
openssl genrsa -3 -out enclave-key.pem 3072
```

**PLEASE KEEP THIS KEY SAFE in some local private storage, but delete it from the server after you have signed.**

Sign the container

```
./gsc sign-image sgx-poster enclave-key.pem
```

The final step is to run the container inside the SGX enclave. This requires a `config` folder which contains the `poster_config.json` file (available from the legacy batch poster).

Finally we also need a `.arbitrum` folder which contains the state of the batch poster. At this point it can be an empty folder but once the legacy batch poster is shut down, we should fill this up with the contents of the legacy batch poster and re-start the poster.

Run the batch poster using the following command, replacing `$CONFIG_PATH` with the actual path to these folders on your host machine.

{% hint style="info" %}
These folders are mounted in the docker container, so any changes to them on the host change them in the container.
{% endhint %}

```bash
docker run \
    --device=/dev/sgx_enclave \
    -v /var/run/aesmd/aesm.socket:/var/run/aesmd/aesm.socket \
    -v $CONFIG_PATH/.arbitrum:/home/user/.arbitrum \
    -v $CONFIG_PATH/config:/config \
    gsc-sgx-poster
```

At this stage, you will see an attestation report similar to the following. The hex value, is the report data which contains the `MR_ENCLAVE` (the hash of the code running inside SGX) and the `MR_SIGNER`. After you see the attestation report, you can shut down the batch poster.

```
0e0e100fffff010000000000000000000100000000000000000000000000
0000000000000000000000000000000000000500000000000000e7000000
000000001f43237dce5a5deecd51d834e6467af7cc9856c7455dcabab6bb
2e7a2012c4c8000000000000000000000000000000000000000000000000
00000000000000000458a0e62674775ca9a048016f817f39b0bd40153000
aceb44a5128ded30555e0000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000888ae654e178
b8fa82cc685faa45a521000000000000000000000000000000009cc8bb48
d11c1dd7039a0ceadbdc1c77
Successfully read attestation report.
```

You can decode all this information using the following steps:

1. Create a `report.txt` file with the hex value and create a bin file as follows:

   ```bash
   xxd -r -p report.txt report.bin
   ```
2. Use [this](https://github.com/EspressoSystems/nitro-espresso-integration/blob/celestia-integration/decode_report_data.sh) bash script to decode the binary, it will print out the `MR_ENCLAVE` and `MR_SIGNER`.

### Deploying the `EspressoTEEVerifier` contract

#### Contract Deployment

You will need to use our version of [nitro contracts](https://github.com/EspressoSystems/nitro-contracts/tree/celestia-integration). The instructions below assume you are using celestia for DA. If not, simply checkout on `integration` branch instead.

Please clone this repo at the given branch to follow the next steps.

```
git clone --recurse-submodules git@github.com:EspressoSystems/nitro-contracts.git
git checkout celestia-integration
```

To run this script to deploy a rollup on arbSepolia follow the given steps:

**Compile the contracts using `yarn`**

```
yarn install && forge install
yarn build:all
```

**Create a `.env` file with variables from the previous steps**

```
DEVNET_PRIVKEY="" # Private key with funds on Arbitrum Sepolia.
MR_ENCLAVE="MR_ENCLAVE_VALUE" # MR_ENCLAVE value from the last step
MR_SIGNER="MR_SIGNER_VALUE" # MR_SIGNER value from the last step
ARBISCAN_API_KEY="" # [Arbscan API Key](https://docs.arbiscan.io/getting-started/viewing-api-usage-statistics)
```

**Deploy the contract**

```
npx hardhat run scripts/deployEspressoTEEVerifier.ts --network arbSepolia
```

#### Sequencer Inbox Migration

**Obtain the Contracts**

In this section we will be working out of our `orbit-actions`repo. Again the choice of `integration` or `celestia-integration` depends on DA.

```
git clone git@github.com:EspressoSystems/nitro-contracts.git
```

Be aware that the contract to deploy the sequencer inbox needs to locally deploy a mock ArbitrumChecker to prevent foundry from declaring calls to precompiles as invalid opcodes. This shouldn't affect on chain deployment from these scripts, nor should it affect the onchain execution of the migration action.

**Configuration**

Create a `.env` file in the orbit-actions directory that contains the following values:

```
#The private key for use during the migration. This should be the rollup owner's private key for steps involving performing the migration.
PRIVATE_KEY=""
# Environment variables for chain name and rpc_url
# These are essential for the upgrade
PARENT_CHAIN_CHAIN_ID=""
PARENT_CHAIN_RPC_URL=""
# Addresses to the upgrade executors on both chains.
# These are essential for the upgrade
PARENT_CHAIN_UPGRADE_EXECUTOR=""
# Environment variables for the sequencer inbox migration action contract
ROLLUP_ADDRESS=""
PROXY_ADMIN_ADDRESS=""

# The reader address should be set to the zero address for orbit chains, for other chains, set this to the same address as your current reader for the sequencer inbox
READER_ADDRESS="0x0"
IS_USING_FEE_TOKEN=""

MAX_DATA_SIZE="104857" #for orbit chains, use this value, for chains posting to ethereum, use 117964
# The old batch poster address will be removed from the sequencer inbox proxy to ensure only the batch poster running in the TEE will be allowed to post batches.
OLD_BATCH_POSTER_ADDRESS=""
NEW_BATCH_POSTER_ADDRESS=""
# The new batch poster address and batch poster manager address will be provided to you to run the migration.
BATCH_POSTER_MANAGER_ADDRESS=""
# This should be the address of the contract you deployed in the last step.
ESPRESSO_TEE_VERIFIER_ADDRESS=""
# This will allow you to deploy a reverting sequencer inbox migration action if desired (there are additional steps in the migration readme)
IS_REVERT=""
```

Source it.

```
source ./.env
```

Install all dependencies.

```
yarn
yarn prepare
yarn build
```

**Run the migration deployment scripts**

Run the migration deployment scripts for the parent chain. Including both `DeployAndInitEspressoSequencerInbox.s.sol`, and `DeployEspressoSequencerInboxMigrationAction.s.sol`. From the base directory of the orbit actions repo, you can use the following commands to run these scripts:

**`DeployAndInitEspressoSequencerInbox.s.sol`**

```
forge script --chain $PARENT_CHAIN_CHAIN_ID contracts/parent-chain/espresso-migration/DeployAndInitEspressoSequencerInbox.s.sol:DeployAndInitEspressoSequencerInbox --rpc-url $PARENT_CHAIN_RPC_URL --broadcast -vvvv --skip-simulation
```

**Before you proceed:** make sure to store the address of the new SequencerInbox in the environment variable `NEW_SEQUENCER_INBOX_IMPL_ADDRESS`

**`DeployEspressoSequencerInboxMigrationAction.s.sol`**

```
forge script --chain $PARENT_CHAIN_CHAIN_ID contracts/parent-chain/espresso-migration/DeployEspressoSequencerMigrationAction.s.sol:DeployEspressoSequencerMigrationAction --rpc-url $PARENT_CHAIN_RPC_URL --broadcast -vvvv --skip-simulation
```

**Before you proceed:** make sure to store the address of the new SequencerInbox in the environment variable `SEQUENCER_MIGRATION_ACTION`

**Execute the Upgrade**

The final step for executing the migration involves using cast to call the `perform()` function of the sequencer inbox migration action via the upgrade executor. You can use the following command to accomplish this:

```
cast send $PARENT_CHAIN_UPGRADE_EXECUTOR "execute(address, bytes)" $SEQUENCER_MIGRATION_ACTION $(cast calldata "perform()") --rpc-url $PARENT_CHAIN_RPC_URL --private-key $PRIVATE_KEY
```

After running this command, your rollup contracts should be set up to accept batches from your new batch poster.

#### Run the Batch Poster with Legacy State

[As stated in upstream documentation](https://docs.arbitrum.io/node-running/faq#how-can-i-migrate-the-date-of-one-synced-node-to-a-new-one), you need to copy the contents of the `.arbitrum` folder of the legacy batch poster to the `.arbitrum` folder of the new

Then re-start the batch poster.

#### Verify the Migration

You should be able to see `batch sent` logs once the batcher starts posting batches. This would indicate that the batcher has started successfully.
