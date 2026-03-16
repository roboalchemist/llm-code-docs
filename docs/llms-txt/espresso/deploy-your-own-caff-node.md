# Source: https://docs.espressosys.com/network/guides/rollup-developers/nitro/deploy-your-own-caff-node.md

# Deploy Your Own Orbit Chain Caff Node

This guide introduces a Go project that reads from the Espresso Network and monitors for specific transactions, filtering them by value and sender address. You can imagine this project as being a bot that alerts you when your wallet gets drained.

## Overview

The hackathon-example [repository](https://github.com/EspressoSystems/hackathon-example/) provides a foundation for building applications that interact with the Espresso Network. You can use this project as a starting point for developing applications or more sophisticated monitoring and analysis tools.

## Prerequisites

Before proceeding with this guide, you'll need:

* A running Arbitrum Orbit chain integrated with the Espresso Network, either locally or in the cloud
* Access to a Caffeinated node, which serves as your interface to the Espresso Network

For convenience, the Caffeinated node setup is available in the same espresso-build-something-real [repository](https://github.com/EspressoSystems/espresso-build-something-real) as the previous guide, under the `caff-node` directory. If you've already deployed your rollup following the earlier instructions, you're ready to proceed with this monitoring project.

## The Caffeinated Node

The Caffeinated node is a full node and your interface to the Espresso Network. It processes Hotshot blocks, maintains state, and provides a JSON-RPC endpoint for monitoring transactions. The monitoring tool we'll build uses these capabilities to track specific transactions based on sender address and value.

## Setup Instructions

Navigate to the [espresso-build-something-real](https://github.com/EspressoSystems/espresso-build-something-real) repository and follow these steps to configure and run your caffeinated node locally:

#### 1. Update the config

Update the `caff-node/config/caff_node.json` file with:

```json
{
  "chain": {
      "id": 1000000,
      ...
  },
  ...
  "next-hotshot-block": 9999,
  "namespace": 1000000,
  "parent-chain-node-url": "WEBSOCKET_ARBITRUM_SEPOLIA_RPC_URL",
}   
```

* **Namespace and Chain ID**: Both should match your rollup chain ID. Update both values.
* **Next Hotshot Block**:
  * Find the latest Hotshot block height at <https://explorer.decaf.testnet.espresso.network/>. Update this value just before running the Caffeinated node to avoid resyncing the entire chain.
* **Parent Chain Node URL**: Enter your Arbitrum Sepolia or mainnet RPC URL (must be a WebSocket URL).

  > 📝 **Note:** We recommend using a different RPC URL for the caff node to avoid hitting rate limits (free tier should be enough).

#### 2. Set Up and Run

1. **Copy Configuration Files**:

   * Copy the `l2_chain_info.json` file into the `caff-node/config` folder

   * Copy the `database` folder from the repository root to the `caff-node` directory.

   > 📝 **Note:** Make sure the node is not running when you do this.
2. **Start the Services**:
   * First, run `docker compose up` at the root of the repository.
   * Then, run `docker compose up` in the `caff-node` folder.

## Setting Up the Example Project

Instructions can be found on the [README](https://github.com/EspressoSystems/hackathon-example/blob/main/README.md) to set this project up but we will go over the steps here in more detail.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/EspressoSystems/hackathon-example --recursive
   cd hackathon-example
   ```

   If you've already cloned the repository without the `--recursive` flag (e.g., through your IDE), you can fetch the go-ethereum submodule with:

   ```bash
   git submodule update --init --recursive
   ```

   The reason we are doing this is because we want to use a forked version of the go-ethereum library from offchainlabs to interact with the caffeinated node.
2. **Install Dependencies**

   ```bash
   go mod tidy
   ```
3. **Configure the Application**

   You should configure the following settings in the `/config/config.json` file:

   ```json
   {
       "caff_node_url": "http://YOUR_HOST:8550",
       "polling_interval": 1,
       "value": 1,
       "from": "0x0000000000000000000000000000000000000000"
   }
   ```

   * **caff\_node\_url**: Change `YOUR_HOST` to either:
     * `localhost` if running locally.
     * Your EC2 instance's IPv4 address if running on the cloud.

   * **polling\_interval**:
     * Controls how frequently the application checks for new transactions.
     * Adjust based on your needs, but keep it low enough to avoid missing transactions.

   * **value**: Set the minimum transaction value (in wei) that you want to monitor.

   * **from**: Enter the Ethereum address you want to monitor transactions from.

   > 📝 **Note:** The docker setup exposes the Caffeinated node on port 8550. 📝 **Note:** The code divides the polling value by 2 to determine the actual polling interval.
4. **Run the Application** At the root of the repository, run the following command:

   ```terminal
   go run .
   ```

   This will start the application and monitor the Espresso Network for transactions that match your rollup and the specified criteria.

   > 📝 **Note:** This monitoring tool simply logs matching transactions to the console. You can extend it to perform more complex actions when transactions are detected.
5. **Send Transactions**

   Now that you have both your rollup and Caffeinated node running, you can send test transactions to your rollup. You have two options:

   * Use a simple command-line transaction:

   ```bash
   cast send ANY_ADDRESS --value 1 --private-key YOUR_PRIVATE_KEY_WITH_FUNDS --rpc-url http://127.0.0.1:8547
   ```

   * Use the transaction generator script in the `espresso-build-something-real/tx-generator` directory, which can continuously generate test transactions. See the [README](https://github.com/EspressoSystems/espresso-build-something-real/blob/main/tx-generator/README.md) in that repository for detailed instructions.

   These transactions will be processed by your rollup and should appear in the monitoring tool's output if they match your configured criteria.

   > 📝 **Note:** The block number shown in the logs is not the latest block height of the espresso network but the latest block processed by your rollup.

## Troubleshooting

If you've followed the guide carefully and paid attention to the notes, you shouldn't encounter many issues. However, here are solutions to some common problems:

#### Normal Warning Messages

The following logs are normal and not cause for concern:

```bash
2025-02-27 13:29:11 WARN [02-27|18:29:11.645] unable to get next message               err="no message found"
2025-02-27 13:29:13 WARN [02-27|18:29:13.273] failed to fetch the transactions         err="no majority consensus reached"
```

These messages simply indicate that the node is listening to the rollup but there are no new transactions to process.

#### Transaction Detection Messages

The following logs indicate that the node is correctly listening to the rollup and has detected a new transaction:

```bash
2025-03-06 INFO [03-06|21:38:50.671] Added message to queue message=487
...
2025-03-06 INFO [03-06|21:38:50.765] Now processing hotshot block "block number"=2,056,058
...
2025-03-06 INFO [03-06|21:38:52.099] Initial State lastBlockHash=6033cf..9f3bef lastBlockStateRoot=35ca02..3749dc
2025-03-06 INFO [03-06|21:38:52.103] Produced block block=751811..23907a blockNumber=487 receipts=2
```

#### Syncing to the Latest Hotshot Block

If you see many logs like these at startup, your Caffeinated node is simply syncing to the latest Hotshot block:

```bash
2025-02-27 11:22:32 INFO [02-27|16:22:32.835] No transactions found in the hotshot block "block number"=1,850,985
2025-02-27 11:22:32 INFO [02-27|16:22:32.835] Now processing hotshot block             "block number"=1,850,986
```

**Solution**: To reduce syncing time, update the `next-hotshot-block` value in `caff-node/config/caff_node.json` to the latest block height from the [espresso explorer](https://explorer.decaf.testnet.espresso.network/) before starting the node.

#### Restarting Docker Containers

If you stop and restart both your rollup and Caffeinated node, you might need to recopy the database folder to your `/caff-node` folder. Failing to do this can cause your rollup and Caffeinated node to fall out of sync.

> 📝 **Note:** This can result in transactions not being detected by the monitoring tool.

#### Rate Limiting Issues

If you're experiencing rate limiting from your RPC provider, you can adjust polling intervals in the configuration files:

```json
// In caff-node/config/caff_node.json
"caff-node-config": {
    "hotshot-polling-interval": "1ms",
    "retry-time": "2s",
},

// In config/full_node.json
"staker": {
    "staker-interval": "120s",
    "make-assertion-interval": "120s",
}
"parent-chain-reader": {
    "poll-interval": "120s"
}
```

Increasing these intervals will reduce the frequency of RPC calls, helping you stay within rate limits.

#### Monitoring Issue

If you don't see logs indicating successful block processing, your Caffeinate node might not be properly connected to or in sync with the rollup. This often happens when the database directory isn't properly configured. You should see logs like:

```bash
2025/03/01 10:00:00 Searching for transaction at last processed block number: 123456
```

If these logs are missing, check that:

* Your repository structure is correct.
* The docker-compose.yml file is properly configured and indented.
* Your caffeinated node is properly syncing with the rollup.

## Update for Listening to Mainnet

To ensure your setup is ready for Arbitrum and Espresso mainnet, you'll need to make the following changes in addition to those described in the `Deploying Your Rollup on Mainnet` [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#deploying-your-rollup-on-mainnet) in the previous guide:

1. **Update Caffeinated Node Configuration**: In `caff-node/config/caff_node.json`, update the following values:

   ```json
   parent-chain-node-url: "WEBSOCKET_ARBITRUM_MAINNET_RPC_URL",
   espresso-tee-verifier-addr: "0xE68c322e548c3a43C528091A3059F3278e0274Ed",
   hotshot-url: "https://query.main.net.espresso.network/v0"
   ```

   > 📝 **Note:** Make sure to use a WebSocket URL (starting with `wss://`) for your Arbitrum mainnet RPC provider.
2. **Update Hotshot Block Height**: Find the latest Hotshot block height at the [mainnet espresso explorer](https://explorer.main.net.espresso.network/) and update the `next-hotshot-block` value in your configuration.

## Deploying your caffeinated node on the cloud

Similarly to the preceding guide, the next step would be to deploy your caffeinated node on the cloud. You can follow the instructions in the `Cloud Configuration` [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#cloud-configuration) of the previous guide for building your EC2 instance and installing the required docker configs. Here are the steps to migrate your caffeinated node to the cloud:

1. Start off from the `Set Up and Run` [section](#2-set-up-and-run) of this guide. The steps on how to run your rollup in the cloud have been covered in the previous guide. You can use the same rollup config files.
2. **Create and configure the caff-node directory structure on your EC2 instance**:

   ```bash
   # Create directory structure
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST "mkdir -p ~/rollup/caff-node/{config,database,wasm}"

   # Set permissions for directories that need write access
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST "sudo chown -R 1000:1000 ~/rollup/caff-node/database ~/rollup/caff-node/wasm"
   ```

   > 📝 **Note:**
   >
   > * The `config` directory remains owned by ec2-user for configuration files
   > * `database` and `wasm` directories need write permissions for the Docker container user (1000:1000)
3. **Transfer the config files to your EC2 instance**: From the root of the repository, run the following command:

   ```bash
   scp -i ~/.ssh/your-key.pem -r ./caff-node/config/* ec2-user@YOUR_HOST:~/rollup/caff-node/config/
   ```
4. **Copy the database from your rollup to the caff-node directory**: From outside the EC2 instance, run the following command:

   ```bash
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST "cp -r ~/rollup/database ~/rollup/caff-node/database"
   ```

   Or from inside the EC2 instance, run the following command:

   ```bash
   cp -r ~/rollup/database ~/rollup/caff-node/database
   ```

   > 📝 **Note:** Make sure you sync and stop the rollup service before copying the database. This step is crucial and is often the cause of issues.
5. **Enable CloudWatch Logging (Optional)**:

   If you want to monitor your caffeinated node logs in CloudWatch:

   * Create a log group for your caffeinated node in the CloudWatch console, similar to how you created log groups in the `Setting up CloudWatch logging` [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#setting-up-cloudwatch-logging-optional) of the previous guide.
   * Modify your `caff-node/docker-compose.yml` file to include CloudWatch logging:

     ```yaml
      version: '2.2'
      services:
      caff_node:
         image: ghcr.io/espressosystems/nitro-espresso-integration/nitro-node@sha256:bf63374a00a5d6676ca39af79ac4b0f053128cb7438bcdaa746dba6656c12658
         container_name: caff_node
         ports:
            - "8550:8547"
            - "8551:8548"
            - "8552:8549"
         command: --conf.file /config/caff_node.json
         volumes:
            - ./config:/config
            - ./wasm:/home/user/wasm/
            - ./database:/home/user/.arbitrum
         logging:
           driver: "awslogs"
           options:
             awslogs-region: "us-east-2" # Update to your EC2 instance's region
             awslogs-group: "caff-node-logs"
             awslogs-stream: "caff-node"
     ```

     > 📝 **Note:** Make sure to update the `awslogs-region` to match your EC2 instance's region.

   Whether you enabled logging or not, you can now transfer the `docker-compose.yml` file inside your instance. From outside the EC2 instance, run the following command:

   ```bash
   scp -i ~/.ssh/your-key.pem ./caff-node/docker-compose.yml ec2-user@YOUR_HOST:~/rollup/caff-node/
   ```

   > 📝 **Note:** Your rollup folder structure should be very similar to the repository structure of the espresso-build-something-real [repository](https://github.com/EspressoSystems/espresso-build-something-real). 📝 **Note:** You can always update the docker-compose.yml file using nano or by copying again the file from the repository.
6. **Connect to your EC2 instance and start the services**:

   ```bash
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST
   cd rollup
   docker-compose up -d
   cd caff-node
   docker-compose up -d
   ```

> 📝 **Note:** Do not forget to update the latest hotshot block height in the `caff-node/config/caff_node.json` from the [espresso explorer](https://explorer.main.net.espresso.network/) to avoid resyncing the entire chain. 📝 **Note:** You can stop the services by running `docker compose down` in the `rollup` and `caff-node` directories. 📝 **Note:** You can remove the `-d` flag to run see the logs of the containers in the terminal.

## Run the monitoring application

Once your caffeinated node is running on the cloud, update the `caff_node_url` in the hackathon-example repository's config to point to your EC2 instance's public IP address. Then try running the application with the updated config.

**Configuring Network Access**

If you encounter connection timeouts when trying to access your EC2 instance (e.g., `dial tcp YOUR_HOST:8550: i/o timeout`), you need to open the required ports in your EC2 security group:

1. In the AWS EC2 Console, navigate to your instance
2. Select the "Security" tab in the bottom panel
3. Click on the security group ID (e.g., "sg-0123456789abcdef")
4. In the security group page, select the "Inbound rules" tab
5. Click "Edit inbound rules"
6. Add two new rules:
   * Type: Custom TCP, Port range: 8547, Source: Custom 0.0.0.0/0 (or your IP for better security)
   * Type: Custom TCP, Port range: 8550, Source: Custom 0.0.0.0/0 (or your IP for better security)
7. Click "Save rules"

This enables external connections to your Caffeinated node (port 8550) and rollup node (port 8547).
