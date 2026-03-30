# Source: https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup.md

# Optimistic Rollup Integration

In this section, we will outline how an optimistic rollup can be adapted to use fast and secure confirmations from the Espresso Network.

### High-level Optimistic Rollup Architecture

In an optimistic rollup, user transactions are first received by the sequencer, which orders them and produces blocks. These blocks are then sent to the batch poster, which compresses them and posts the batches to the parent chain. The batches are subsequently verified by validators, resulting in a new finalized rollup state.

### High Level Integration Flow

In our integration, the sequencer/batch poster sends blocks to the Espresso network. Once the network confirms them, the batch poster retrieves those blocks, assembles them into batches, and submits the batches to the parent chain. To ensure the data posted to the parent chain matches what the Espresso network confirmed, we run the batch poster inside a Trusted Execution Environment (TEE). With each batch, the poster includes a TEE attestation (proof), which a contract on the parent chain verifies to confirm that the batcher is indeed running inside a TEE.

![Arbitrum Nitro integration flow with Espresso](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-947cd4624c7f64ab388c04f20c95b5b53898b276%2Foptimistic-rollup-overview.png?alt=media)

### Reading Espresso Confirmations

We’ve also built **Caff Nodes**, which are rollup full nodes that get data from the Espresso Network. Bridges and apps can use them to read the rollup state.

![Reading confirmations from the Espresso Network](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-49037a7e6df5756582bde5d816809c47def0ecac%2Fcaff-node.png?alt=media)
