# Source: https://docs.near.org/data-infrastructure/tutorials/listen-function-calls.md

---
id: listen-function-calls
title: "Tutorial: Simple Indexer"
description: "This tutorial will guide you through building a simple indexer using the NEAR Lake Framework. The indexer will listen for FunctionCalls on a specific contract and log the details of each call."
---





In this tutorial, we will build a simple indexer using the NEAR Lake Framework. The indexer will listen for FunctionCalls on a specific contract and log the details of each call.

The full source code for the indexer is available in the [GitHub repository](https://github.com/near-examples/indexer-near-lake-framework?tab=readme-ov-file).

:::info
Using NEAR Lake Framework, we can subscribe to the stream of blocks from the NEAR Lake data source. The source of data are JSON files stored in an AWS S3 bucket by [NEAR Lake Indexer](https://github.com/aurora-is-near/near-lake-indexer). The NEAR Lake Framework takes care of downloading and parsing the data for users, but **the reader is paying the costs**. More details about technical limitations and **estimating costs** can be found [here](../near-lake-framework.md#comparison-with-near-indexer-framework).
:::

---

## Initialization

Let's start by initializing the NEAR Lake Framework.

<hr class="subsection" />

### AWS Credentials

To access the data provided by [NEAR Lake](../lake-framework/near-lake) you need to provide valid AWS credentials in order to be charged by the AWS for the S3 usage.

:::info AWS credentials

Please note that using your own AWS Credentials is the only way to access the data provided by [NEAR Lake](../lake-framework/near-lake) ecosystem.

:::


AWS default profile configuration with aws configure looks similar to the following:

```
~/.aws/credentials
```

```
[default]
aws_access_key_id=<YOUR_AWS_ACCESS_KEY_ID>
aws_secret_access_key=<YOUR_AWS_ACCESS_KEY>
```

[AWS docs: Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

<hr class="subsection" />

### Lake Configuration

To initialize the NEAR Lake Framework, we need to provide the following basic settings:

- The S3 bucket name: the bucket where the NEAR Lake data is stored. The value is `near-lake-data-testnet` for the testnet and `near-lake-data-mainnet` for the mainnet.
- The S3 region: The AWS region where the S3 bucket is located. The default value is `eu-central-1`.
- Start block height: The block height from which the indexer will start processing blocks.


<Tabs groupId="code-tabs">
    <TabItem value="rust" label="🦀 Rust" default>
      The Rust package provides a way to use the default configuration for testnet/mainnet and requires only to choose network and set the start block height which in the example we pass as command line argument. 

      ```
    // Parse the command line arguments
    let opts: Opts = Opts::parse();

    // Configure the lake
    let lake_config = near_lake_framework::LakeConfigBuilder::default()
        .testnet()
        .start_block_height(opts.block_height)
        .build()
        .expect("Failed to build LakeConfig");

```
    </TabItem>
    <TabItem value="js" label="🌐 JavaScript">
      In JavaScript/TypeScript, we will just create the configuration object manually. Block height is passed as a command line argument.

      ```
// Parse command line arguments
const argv = yargs(hideBin(process.argv)).parse();
const blockHeight = argv.blockHeight;

// Configure the lake
const lakeConfig: types.LakeConfig = {
    s3BucketName: "near-lake-data-testnet", // "near-lake-data-mainnet" for the mainnet
    s3RegionName: "eu-central-1",
    startBlockHeight: blockHeight,
};

```
    </TabItem>
    <TabItem value="python" label="🐍 Python" default>
      In Python, we will create the configuration object manually and then set `s3_bucket_name` and `s3_region_name` properties. Block height is passed as a command line argument. 

      ```
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='NEAR Lake Framework Indexer')
    parser.add_argument('--accounts', type=str, help='Comma-separated list of accounts to filter')
    parser.add_argument('--block-height', type=int, help='Starting block height')

    args = parser.parse_args()
    start_height = args.block_height

    # Configure the lake
    config = LakeConfig(
        network=Network.TESTNET,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        start_block_height=start_height
    )
    config.s3_bucket_name = "near-lake-data-testnet"
    config.s3_region_name = "eu-central-1"

```
    </TabItem>
</Tabs>

## Running the Indexer

To run the indexer, we need to create a function that will handle every message from the stream. In this function, we can access the block data and process it as needed.

<Tabs groupId="code-tabs">
    <TabItem value="rust" label="🦀 Rust" default>
      ```
/// The main listener function the will be reading the stream of blocks `StreamerMessage`
async fn listen_blocks(
    mut stream: mpsc::Receiver<near_indexer_primitives::StreamerMessage>,
    watching_list: Vec<near_indexer_primitives::types::AccountId>,
) {
    // This will be a map of correspondence between transactions and receipts
    let mut tx_receipt_ids = HashMap::<String, String>::new();
    // This will be a list of receipt ids we're following
    let mut wanted_receipt_ids = HashSet::<String>::new();

    // Handle the messages from the stream
    while let Some(streamer_message) = stream.recv().await {
        parse_message(
            &streamer_message,
            &watching_list,
            &mut tx_receipt_ids,
            &mut wanted_receipt_ids,
        );
    }
}

```
    </TabItem>
    <TabItem value="js" label="🌐 JavaScript">
      ```
// Start the stream
(async () => {
    await startStream(lakeConfig, parseMessage);
})();

```
    </TabItem>
    <TabItem value="python" label="🐍 Python">
      ```
async def listen_blocks(streamer_messages_queue, watching_accounts):
    # Dictionary to map the transaction receipt ids to the transaction hash we should track
    tx_receipt_ids = {}
    # List of receipt ids to track
    wanted_receipt_ids = []

    while True:
        streamer_message = await streamer_messages_queue.get()
        parse_message(streamer_message, watching_accounts, tx_receipt_ids, wanted_receipt_ids)

```
    </TabItem>
</Tabs>

## Parsing the Block Data

From the block data, we can access the transactions, their receipts and actions. In this example, we will look for FunctionCall actions on a specific contract and log the details of each call.

<Tabs groupId="code-tabs">
    <TabItem value="rust" label="🦀 Rust" default>
      ```
/// The method that will be called for each message from the stream
fn parse_message(
    streamer_message: &near_indexer_primitives::StreamerMessage,
    watching_list: &[near_indexer_primitives::types::AccountId],
    tx_receipt_ids: &mut HashMap<String, String>,
    wanted_receipt_ids: &mut HashSet<String>,
) {
    eprintln!("Block height: {}", streamer_message.block.header.height);
    // Iterate over the shards in the block
    for shard in streamer_message.shards.clone() {
        let chunk = if let Some(chunk) = shard.chunk {
            chunk
        } else {
            continue;
        };

        // Iterate over the transactions in the chunk
        for transaction in chunk.transactions {
            // Check if transaction receiver id is one of the list we are interested in
            if is_tx_receiver_watched(&transaction, &watching_list) {
                // Extract receipt_id transaction was converted into
                let converted_into_receipt_id = transaction
                    .outcome
                    .execution_outcome
                    .outcome
                    .receipt_ids
                    .first()
                    .expect("`receipt_ids` must contain one Receipt Id")
                    .to_string();
                // Add `converted_into_receipt_id` to the list of receipt ids we are interested in
                wanted_receipt_ids.insert(converted_into_receipt_id.clone());
                // Add key value pair of transaction hash and in which receipt id it was converted for further lookup
                tx_receipt_ids.insert(
                    converted_into_receipt_id,
                    transaction.transaction.hash.to_string(),
                );
            }
        }

        // Iterate over the execution outcomes in the shard
        for execution_outcome in shard.receipt_execution_outcomes {
            // Check if the receipt id is in the list of receipt ids to track
            if let Some(receipt_id) =
                wanted_receipt_ids.take(&execution_outcome.receipt.receipt_id.to_string())
            {
                // Log the transaction hash, the receipt id and the status
                println!(
                    "\nTransaction hash {:?} related to {} executed with status {:?}",
                    tx_receipt_ids.get(receipt_id.as_str()),
                    &execution_outcome.receipt.receiver_id,
                    execution_outcome.execution_outcome.outcome.status
                );
                if let near_indexer_primitives::views::ReceiptEnumView::Action {
                    signer_id, ..
                } = &execution_outcome.receipt.receipt
                {
                    // Log the signer id
                    eprintln!("{}", signer_id);
                }

                if let near_indexer_primitives::views::ReceiptEnumView::Action { actions, .. } =
                    execution_outcome.receipt.receipt
                {
                    // Iterate over the actions in the receipt
                    for action in actions.iter() {
                        // If the action is a function call, log the decoded arguments
                        if let near_indexer_primitives::views::ActionView::FunctionCall {
                            args,
                            ..
                        } = action
                        {
                            if let Ok(args_json) =
                                serde_json::from_slice::<serde_json::Value>(&args)
                            {
                                eprintln!("{:#?}", args_json);
                            }
                        }
                    }
                }
                // Remove the receipt id from the map of receipt ids to transaction hashes because we have processed it
                tx_receipt_ids.remove(receipt_id.as_str());
            }
        }
    }
}

```
    </TabItem>
    <TabItem value="js" label="🌐 JavaScript">
      ```
async function parseMessage(
  block: types.Block,
  /* context: types.LakeContext */ // In this case we don't use the context, but it is available if needed
): Promise<void> {
  console.log(`Block height: ${block.header().height}`); 
  // Iterate over the shards in the block
  for (const shard of block.streamerMessage.shards) {
    const chunk = shard.chunk;
    // Iterate over the transactions in the chunk
    for (const transaction of chunk.transactions) {
      // Check if transaction receiver id is one of the list we are interested in
      if (isTxReceiverWatched(transaction.transaction.receiverId, watchingAccounts)) {
        // Extract receipt_id transaction was converted into
        const receiptId = transaction.outcome.executionOutcome.outcome.receiptIds[0];
        // Add receipt id to the list of receipt ids we are interested in
        wantedReceiptIds.push(receiptId);
        // Add key value pair of transaction hash and in which receipt id it was converted for further lookup
        txReceiptIds[receiptId] = transaction.transaction.hash;
      }
    }
    // Iterate over the execution outcomes in the shard
    for (const executionOutcome of shard.receiptExecutionOutcomes) {
      // Check if the receipt id is in the list of receipt ids to track
      if (wantedReceiptIds.includes(executionOutcome.receipt.receiptId)) {
        const receiptIdIdx = wantedReceiptIds.indexOf(executionOutcome.receipt.receiptId);
        // Remove the receipt id from the list of receipt ids because we have processed it
        wantedReceiptIds.splice(receiptIdIdx, 1);
        
        // Get the status of the execution outcome
        let status: string;
        
        if (typeof executionOutcome.executionOutcome.outcome.status === 'string') {
          status = 'Postponed';
        } else if ('SuccessValue' in executionOutcome.executionOutcome.outcome.status) {
          status = 'SuccessValue';
        } else if ('SuccessReceiptId' in executionOutcome.executionOutcome.outcome.status) {
          status = 'SuccessReceiptId';
        } else if ('Failure' in executionOutcome.executionOutcome.outcome.status) {
          status = 'Failure';
        } else {
          status = 'Unknown';
        }

        // Log the transaction hash, the receipt id and the status
        console.log(`\nTransaction hash ${txReceiptIds[executionOutcome.receipt.receiptId]} related to ${executionOutcome.receipt.receiptId} executed with status \"${status}\"`);

        if ('Action' in executionOutcome.receipt.receipt) {
          // Log the signer id
          console.log(`${executionOutcome.receipt.receipt.Action.signerId}`);

          // Iterate over the actions in the receipt
          for (const action of executionOutcome.receipt.receipt.Action.actions) {
            // If the action is a function call, log the decoded arguments
            if (typeof action === 'object' && action !== null && 'FunctionCall' in action) {
              const decodedArgs = Buffer.from(action.FunctionCall.args, 'base64').toString('utf-8');
              console.log(`${decodedArgs}`);
            }
          }
        } 

        // Remove the receipt id from the map of receipt ids to transaction hashes because we have processed it
        delete txReceiptIds[executionOutcome.receipt.receiptId];
      }
    }
  }
}

```
    </TabItem>
    <TabItem value="python" label="🐍 Python">
      ```
def parse_message(streamer_message, watching_accounts, tx_receipt_ids, wanted_receipt_ids):
    print(f"Block height: {streamer_message.block.header.height}")

    # Iterate over the shards in the block
    for shard in streamer_message.shards:
        chunk = shard.chunk
        # Iterate over the transactions in the chunk
        for tx in chunk.transactions:
            if tx.transaction.receiver_id in watching_accounts:
                # Extract receipt_id transaction was converted into
                receipt_id = tx.outcome.execution_outcome.outcome.receipt_ids[0]
                # Add receipt id to the list of receipt ids we are interested in
                wanted_receipt_ids.append(receipt_id)
                # Add key value pair of transaction hash and in which receipt id it was converted for further lookup
                tx_receipt_ids[receipt_id] = tx.transaction.hash

        # Iterate over the execution outcomes in the shard
        for execution_outcome in shard.receipt_execution_outcomes:
            # Check if the receipt id is in the list of receipt ids to track
            if execution_outcome.receipt.receipt_id in wanted_receipt_ids:
                # Remove the receipt id from the list of receipt ids because we have processed it
                wanted_receipt_ids.remove(execution_outcome.receipt.receipt_id)

                if isinstance(execution_outcome.execution_outcome.outcome.status, str):
                  status = 'Postponed'
                elif 'SuccessValue' in execution_outcome.execution_outcome.outcome.status:
                  status = 'SuccessValue'
                elif 'SuccessReceiptId' in execution_outcome.execution_outcome.outcome.status:
                  status = 'SuccessReceiptId'
                elif 'Failure' in execution_outcome.execution_outcome.outcome.status:
                  status = 'Failure'
                else:
                  status = 'Unknown'

                # Log the transaction hash, the receipt id and the status
                print(f"Transaction hash {tx_receipt_ids[execution_outcome.receipt.receipt_id]} related to {execution_outcome.receipt.receipt_id} executed with status {status}")

                if ('Action' in execution_outcome.receipt.receipt):
                  # Log the signer id
                  print(execution_outcome.receipt.receipt['Action']['signer_id'])

                  # Iterate over the actions in the receipt
                  for action in execution_outcome.receipt.receipt['Action']['actions']:
                    # If the action is a function call, log the decoded arguments
                    if action['FunctionCall']:
                      decoded_args = json.loads(base64.b64decode(action['FunctionCall']['args']))
                      print(decoded_args)

```
    </TabItem>
</Tabs>

The example of logged data:
```bash
Block height: 214692896

Transaction hash HQsRK16ABEQWtKpHKWMbPgUreXCD95ZpKw47YkHxGsEc related to 6QpDUkd5n2xJ6mTjkdzXDbvMFo5mEzANS1t4Hfr76SAY executed with status "SuccessValue"
aha_6.testnet
{"contract_id":"3vaopJ7aRoivvzZLngPQRBEd8VJr2zPLTxQfnRCoFgNX"}
```

<MovingForwardSupportSection />

:::note Versioning for this article

At the time of this writing, this example works with the following versions:

- near-lake-framework (Rust): `0.7.13`
- @near-lake/framework (JS): `0.1.5`
- near-lake-framework (Python): `0.1.3`
- rustc: `1.86.0`
- node: `22.18.0`
- python: `3.13.5`

:::