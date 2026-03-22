# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/interfaces/rollup-less-than-greater-than-l1.md

# Rollup ↔ L1

Each rollup communicates with the L1 via its own rollup contract, which can have a unique public interface. In order to verify state updates sent from the rollup (either proactively with validity proofs in the case of ZK-rollups, or when presented with a fraud proof in the case of optimistic rollups), each rollup contract must have access to the certified sequence of blocks which led to the claimed state update.

When using Espresso, the authoritative sequence of blocks is the output of HotShot, which is replicated to the L1 and certified by the HotShot contract. Therefore, rollup contracts will interface with the HotShot contract. The interface which allows rollup contracts to query the certified sequence of block commitments is very simple: the sequencer contract provides a public `sequencedCommitments` field, which is an array of block commitments which have been verified by the contract.
