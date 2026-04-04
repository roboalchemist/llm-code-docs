# Source: https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater.md

# Updater

Updater Code: <https://github.com/nomad-xyz/rust/tree/main/agents/updater>

**The Updater is an off-chain agent that does the following:**

* Observe [the Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) on the origin chain
* Sign attestations to new roots
* Publish the signed attestation to the Home

The Home contract permissions an "updater" that must attest to the state of the message tree. The updater places a bond on the home chain and is required to periodically sign attestations (updates or U). Each attestation contains the root from the previous attestation (U\_prev), and a new root (U\_new).

### Performing Updates

The Updater maps logically to a single Home contract. Its entire job is to observe the Home to ensure that new messages (and hence new roots) are notarized such that they can be relayed to any number of Replicas.&#x20;

The Updater listens for events on the Home, and calls functions to perform its job.

#### Listening for New Roots

Cross-chain applications enqueue messages to be sent by calling [`dispatch`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L175) on the Home contract. Once the message is enqueued in the Home's message tree, the Home emits the following event:

```solidity
emit Dispatch(
    _messageHash,
    count() - 1,
    _destinationAndNonce(_destinationDomain, _nonce),
    committedRoot,
    _message
);
```

Updaters listen for these events, and after batching some number of messages (per their SLA), will sign an update over the old root and new root.

#### Publishing an Update

Updaters sign attestations off-chain and publish them by calling [`update`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L221) on the Home contract:

```solidity
function update(
    bytes32 _committedRoot,
    bytes32 _newRoot,
    bytes memory _signature
) external notFailed {
    // check that the update is not fraudulent;
    // if fraud is detected, Updater is slashed & Home is set to FAILED state
    if (improperUpdate(_committedRoot, _newRoot, _signature)) return;
    // clear all of the intermediate roots contained in this update from the queue
    while (true) {
        bytes32 _next = queue.dequeue();
        if (_next == _newRoot) break;
    }
    // update the Home state with the latest signed root & emit event
    committedRoot = _newRoot;
    emit Update(localDomain, _committedRoot, _newRoot, _signature);
}
```

Once the update has been performed, a [Relayer](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/relayer) may relay the new update to [Replica contracts](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica) on destination chains.

### Updater Selection

Updaters are selected and enrolled on the Home contract by the [UpdaterManager contract](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/UpdaterManager.sol), which is established at initialization time.&#x20;

The UpdaterManager can be changed by calling [`_setUpdaterManager`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L161). This function can only be called by the `owner` role, which belongs to [Nomad governance](https://docs.nomad.xyz/operational-security/governance).

At a given time, there is only one Updater enrolled per Home contract. This helps reduce overhead of verification, relative to externally verified systems that require many validators or guardians.

### Updater Slashing

If an Updater ever attempts to commit fraud (by attesting to an invalid root), the Home contract will be set to a failed state, at which point the Updater will be slashed:

```solidity
function _fail() internal {
    // set contract to FAILED
    state = States.Failed;
    // slash Updater
    updaterManager.slashUpdater(msg.sender);
    emit UpdaterSlashed(updater, msg.sender);
}
```

The [`slashUpdater`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/UpdaterManager.sol#L89) function in the UpdaterManager will be implemented when updater bonding and rotation are also implemented in the future.
