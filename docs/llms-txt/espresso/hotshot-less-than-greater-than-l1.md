# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/interfaces/hotshot-less-than-greater-than-l1.md

# Espresso ↔ L1

Espresso interacts with the L1 via the sequencer contract, which validates HotShot consensus and provides a certified, trustless interface for other participants to check the sequence of blocks. Note that the contract only deals with short block commitments, not full blocks, in order to minimize the cost of sending data to the L1. Anyone who has verified a commitment against the contract can get the corresponding block—and authenticate it against the commitment—from the HotShot availability API.

Espresso interacts with the sequencer contract via an interface like:

{% code title="// HotShot.sol" %}

```solidity
struct QC { /* Fields omitted */ } 

// Root of a Merkle tree accumulating the verified sequence of block commitments.
bytes32 public commitmentsRoot;

// Event emitted when new blocks are sequenced.
event NewBlocks(uint firstBlockNumber, uint256[] commitments, bytes32[] frontier);
 
// Called to append a chain of new blocks, given proof that consensus has finalized them.
function newBlocks(QC[] calldata qcs, bytes calldata proof, bytes32[] calldata frontier) external;
```

{% endcode %}

The `newBlocks` method allows a sequencer node to append a list of newly sequenced block commitments to the log stored in the contract. It takes a list of quorum certificates, a validity proof, and a [Merkle frontier](https://iammichaelconnor.medium.com/timber-7db8a5130849) corresponding to `commitmentsRoot`, and it validates that

* Each QC extends from the previous QC in the chain (starting with the previously sequenced QC)
* Each QC is properly signed (the contract will need to store and keep up-to-date the stake table)
* There are enough QCs to prove finality for one or more block commitments. HotShot consensus currently requires a chain of at least 3 QCs before the first QC in the chain is considered finalized (an upcoming version of HotShot will only require a 2-chain of QCs)

If validation succeeds, it updates `commitmentsRoot`, which can then be used by other contracts to validate proofs of inclusion of block commitments in the sequence. On success, `newBlocks` emits a `NewBlocks` event informing clients (e.g. rollup provers) that new blocks have been appended. Those clients can read the new block commitments from the event logs using an Ethereum client. The event logs also include a snapshot of the Merkle frontier just before the new blocks were appended. A client can construct a Merkle path for any given commitment by appending commitments to the snapshotted frontier.

`newBlocks` will fail if the given batch has already been sequenced, since `qcs` will fail the check that it must extend from the last sequenced QC. This ensures that each batch of blocks will only be sequenced once — whoever calls this method first will be the one to sequence it. It is an open question whether the contract will explicitly incentivize sequencer nodes to call `newBlocks`.

To learn more about the sequencer contract, how it stores data, and how it validates QCs, read the section on [its internal functionality](https://github.com/EspressoSystems/gitbook/blob/main/espresso-sequencer-architecture/internal-functionality/sequencer-contract/README.md).
