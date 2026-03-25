# Source: https://docs.espressosys.com/network/guides/rollup-developers/op.md

# Optimism

Espresso is developing an integration for [OP Chains](https://docs.optimism.io/stack/getting-started). Here we provide an overview of the integration and details on how to deploy or migrate an existing chain will be provided shortly.

## Integration overview

The Espresso-OP Stack integration ensures that each batch processed by the rollup is consistent with Espresso-finalized blocks.

To ensure that the batch has been finalized by Espresso, the following checks are performed:

1. **Namespace validation:** Namespacing allows multiple chains to use Espresso’s fast confirmation layer simultaneously by associating each chain’s transactions with a unique namespace within Espresso blocks. This check ensures that the set of transactions in an OP batch corresponds to the correct namespace.
2. **Espresso finalization check:** Confirms that the OP batch maps to a valid Espresso finalized block.

The flow is as follows:

1. A user submits either a deposit transaction to the L1 or an L2 transaction.
2. The rollup node (`op-node`, running in sequencer mode) fetches any deposit transactions from L1.
3. The rollup node constructs the payload attributes and sends them to `op-geth`, which executes them to create blocks.
4. The `op-batcher` queries the blocks and creates batches accordingly.
5. The batcher then submits these batches to HotShot for finalization via the [submit API](https://github.com/EspressoSystems/gitbook/blob/main/guides/api-reference/espresso-api/submit-api.md).
6. Periodically, the batcher also calls the [availability API](https://docs.espressosys.com/sequencer/api-reference/espresso-api/availability-api) to check for finalized HotShot blocks containing these batches and performs batch consistency checks.
7. The batcher signs the transaction calldata that would be sent to the `Batch Inbox` contract.
8. In the integration, the `Batch Inbox` address is converted from an EOA to a contract containing only a fallback function. This fallback function receives all transactions sent to the contract and verifies the signature to ensure it originates from the trusted batcher:

A small change to the derivation pipeline filters out transactions sent to the batch inbox that caused the contract to revert.

This approach involves running an `op-batcher` in a TEE environment (such as Intel SGX). The batcher signs the transaction calldata. In case the TEE is broken, the batch poster can't impact the safety of the chain. It could, however, temporarily halt the chain's progress, thereby breaking liveness. Bridges relying on Espresso confirmations for faster settlement however need to trust the TEE as well in this integration. In a future update the dependency on TEEs will be removed entirely.
