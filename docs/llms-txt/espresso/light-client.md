# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/light-client.md

# Light Client Contract

{% hint style="info" %}
The source code for the light client contract can be found on [GitHub](https://github.com/EspressoSystems/espresso-sequencer/blob/b1884c4bea3246a86cbd430853a5a69e4def0f0a/contracts/src/LightClient.sol).
{% endhint %}

The *light client contract* is responsible for maintaining state about HotShot consensus on the layer 1 blockchain that Espresso (and L2 rollups) checkpoint to.

`LightClient` validates the HotShot state through cryptographic proofs (SNARK proofs). Rollups can use the new `finalizedState` from the contract to confirm the validity and finality of transactions that have been bundled and processed.

```solidity
LightClientState public finalizedState;
```

## Light Client State

This `LightClientState` includes information such as:

* the latest view number, `viewNum`, and block height, `blockHeight`, of the finalized HotShot chain
* the Merkle root of finalized block commitments, `blockCommRoot`

```solidity
struct LightClientState {
    uint64 viewNum;
    uint64 blockHeight;
    BN254.ScalarField blockCommRoot;
}
```

The most important part of the LightClientState is the `blockCommRoot`, which is the root of an [append-only Merkle tree](https://iammichaelconnor.medium.com/timber-7db8a5130849) of all blocks sequenced by Espresso. This root is public, allowing other contracts to use succinct Merkle proofs to verify the inclusion of a certain block commitment at a certain height and to update the root when new blocks are appended.

At any given time, the `LightClientState` contains Espresso block commitments from height 0 up to (but not including) the current block height, `blockHeight`. All commitments for heights greater or equal to `blockHeight` are not present — the corresponding leaf is empty in the tree.

There's another struct, `StakeTableState`, which is used to store the initial stake table commitments. The stake table is currently fixed, meaning it is initialized once and stored in the `genesisStakeTableState` variable when the Light Client contract is first deployed. The initial stake table commitments include the BLS and Schnorr verification keys and the amounts the validators staked.

```solidity
    struct StakeTableState {
        uint256 threshold;
        BN254.ScalarField blsKeyComm;
        BN254.ScalarField schnorrKeyComm;
        BN254.ScalarField amountComm;
    }
```

However, in future versions, the stake table is will become dynamic. This will allow validators' stake commitments and key information to be updated in real-time, allowing the system to adjust to changes in stake amounts, the registration of new validators, or the withdrawal of existing ones.

### Rollups and the Light Client Contract

Rollup contracts on L1 must use the `blockCommRoot` when validating a state transition to ensure that the rollup block claimed to have been executed is indeed the next block in the canonical sequence.

The proposer of a rollup state transition must provide a proof, relative to `blockCommRoot`, showing that the Espresso state commitment at a specified height is consistent with the rollup block commitment.

For rollups to integrate with Espresso, they need to modify their contract on L1 to prove that their state is derived from the Espresso state. For instance, consider a scenario where the Espresso prover pushes a new Espresso state commitment to the light client contract every 1 minute, and the rollup prover submits a new rollup block commitment every 10 minutes to their rollup contract. The rollup prover needs to prove that the block commitment it publishes to the rollup contract corresponds to all its rollup transactions contained in the Espresso blocks during the 10-minute period.

Each Espresso block commitment also commits to a list of rollup transactions (among other metadata) which facilitates lightweight proofs with transaction granularity for arbitrarily old rollup blocks. This approach allows for the verification of these rollups blocks on Espresso's chain and enables the light client contract to operate with a constant amount of storage, irrespective of the HotShot chain's length.

### Data Availability

Since the actual block commitments (let alone the full blocks) are not stored on-chain, it is important to understand the data availability properties ensuring that clients can always retrieve an old block, block commitment, or a block's Merkle proof.

Clients can fetch a Merkle proof for any block from an archival query service and authenticate it against the block root in the light client state. Failing that, they can fetch the individual blocks from [HotShot DA](https://docs.espressosys.com/network/concepts/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer/how-it-works) and extract the proof themselves.

### ZK Proofs, SNARK Proofs, and ZK Circuits

A circuit defines the computation to be proven. Zero-knowledge proof (ZKP) systems can generate cryptographic proofs attesting to the validity of statements described by the circuit without revealing underlying witness. In our context, we rely on SNARK proofs (a special kind of ZKP), whose succinct nature is especially valuable for verifying computation in smart contracts where gas costs are a critical concern. Irrespective of the number of signatures/consensus votes, the size and verification cost of the proof remain constant.

In a zero-knowledge protocol there are two main roles: (i) the *prover* and (ii) the *verifier*.

The *prover* uses a combination of secret inputs (HotShot nodes' Schnorr signatures), also called witnesses, public inputs (the `LightClientState`), and a circuit description in order to generate a SNARK proof.

The *verifier* uses the public inputs and the SNARK proof to verify that the rules defined by the ZK circuit are satisfied. In this case, the `LightClient` contract acts as the verifier for this ZK proof via the `verifyProof` method which is invoked within the `newFinalizedState` function.

Finally, both the prover and verifier use some public parameters. These public parameters are derived from the circuit and a structured reference string (SRS) that requires a trusted setup to be generated but can be reused for other circuits.

### The Light Client Circuit

Let the following circuit $$\mathcal{C}\_{\sf qc}$$ over prime field $$\mathbb{F}\_p$$, the corresponding Jubjub curve group $$\mathbb{G}=\langle g\rangle$$ whose scalar field is $$\mathbb{F}\_r$$ and base field is exactly $$\mathbb{F}\_p$$, so that each group element $$\in \mathbb{F}\_p \times\mathbb{F}\_p$$.

* Public input:
  * stake table commitment: $$\mathsf{cm}\_\mathcal{T} \in \mathbb{F}\_p$$
    * A stake table entry now composes of a triple $$(bls\_ver\_key, schnorr\_ver\_key, stake\_amount)$$. BLS verification key is under `ark_bn254::Fq`, Schnorr verification key is under `ark_bn254::Fr`, and the stake amount is within the range of `ark_bn254::Fr`. The commitment should be computed in the following way: first serialize all BLS keys into elements of `ark_bn254::Fr`, follows by a list of Schnorr keys and then the stake amount. The commitment is the rescue hash of this list.
  * quorum Threshold: $$T \in \mathbb{F}\_p$$
  * attested new finalized hotshot state: $$m:=(v, h, \mathsf{root\_{cm}, cm\_{ledger}, cm\_{stake\_table}}) \in \mathbb{F}\_p^5$$
    * the merkle tree for block commitments can use any hash function (e.g. SHA2) and best if there is an injective mapping between the root value to a $$\mathbb{F}\_p$$ element.
* Secret witness:
  * signers indicator vector: $$\vec{v}\_S$$
  * stake table vector (consists of public key, weight pair): $$\mathcal{T}=\[(pk\_i \in\mathbb{G}, w\_i \in \mathbb{F}*p)]*{i\in\[n]}$$
  * list of schnorr signatures: $${\sigma\_i = (s\_i, R\_i) \in \mathbb{F}*r \times \mathbb{G}}*{i\in \[n]}$$
* Relation:
  * the input signers indicator vector $$\vec{v}\_S$$ is a bit vector
  * correct stake table commitment: $$\mathsf{cm}\_\mathcal{T}= \mathtt{commit}(\mathcal{T})$$
    * we use Rescue-based commitment, thus all operations are native
  * accumulated weighted sum exceeds threshold: $$\sum\_{i\in S}{w\_i} > T$$
    * assumption: there’s no overflow!! NOTE: outside the circuit, the client software that’s in charge of stake table management needs to check the accumulated sum does not exceed modulus $$p$$ AT ALL TIMES! ⚠️
  * signature verification (on each): $$\mathsf{Vfy}(pk\_i, m, \sigma\_i) = 1$$ for all $$\forall i\in \[n]$$.
    * $$c = H(R, m, ..)$$: rescue-based hash to get challenge
    * $$x = g^s$$: a fixed-base scalar mul
      * internally, involves bit-decomposition of $$s$$ and elliptic curve addition based on the bits.
    * $$y = R + pk^c$$: a variable-base scalar multiplication + an elliptic curve addition.
    * $$x\overset{?}{=}y$$: point equality check

### Updating and Verifying LightClientState

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-be6a855187b3742ee4fcbab0096e185e4567a9a6%2FLightClientWorkflow.png?alt=media" alt=""><figcaption></figcaption></figure>

The `LightClientState` is updated by any state prover that submits valid updates to the `LightClient` contract via the `newFinalizedState` method which sets the latest `finalizedState`.

```solidity
function newFinalizedState(
    LightClientState memory newState,
    IPlonkVerifier.PlonkProof memory proof
) external {
  //...
}
```

We assume an *altruistic, honest prover* for now and leave the design of prover market to future work.

For replicas:

* upon receiving new QC from the leader, generate a Schnorr signature over the updated finalized HotShot state, and send it over to the CDN *and* store it locally for a while.
* the local storage for the Schnorr signatures (for each block) can be a sliding window of a fixed size where older signatures got pruned. The window size can be set based on the expected interval for on-chain update plus some buffer accounting for temporarily failing prover.

For the altruistic prover:

* will continuously listen passively for the HotShot state changes, e.g. when a new block has been decided
* periodically requests the Schnorr signatures from the DA layer by sending a request on a specific view $$v$$. This will be the signature for the new finalized state from the consensus nodes
  * For convenience of signature collection, prover will first fetch from CDN (we refer to as the relay server) for the list of Schnorr signatures, if failed, then ask each individual replica (note: not small DA committee, or VID, but each node individually).
* Once a sufficient amount of valid signatures is collected, some provers can then generate a SNARK proof which is submitted alongside the new finalized state to the light client contract.

{% hint style="warning" %}
The contract has the ability to be in permissioned mode where it only accepts proofs from one prover. For the next release, only a permissioned prover, doing the computations, will call this function.
{% endhint %}

Replica nodes update the snapshot of the stake table at the beginning of an epoch and this snapshot is used to define the set of stakers for the next epoch. The light client state must be updated at least once per epoch.

{% hint style="warning" %}
For the next release, we are not using epochs so `numBlockPerEpoch` is set to `type(uint32).max` during deployment.
{% endhint %}

## HotShot state authentication via Schnorr signatures

When a set of HotShot nodes reach consensus and the finalized HotShot state has been updated, they each sign a Schnorr signature on this updated HotShot state. These signatures assert that the signer agrees with the state of each proposed block. The signatures are stored locally on the DA layer, and to save space, older signatures are pruned using a sliding window mechanism. The window size can be set based on the expected interval for on-chain update plus some buffer accounting for a temporarily failing prover.

When a prover (an entity that confirms the truth of a claim) retrieves these signatures, a SNARK proof is then generated. This proof, is used by the `LightClient` contract to efficiently verify these Schnorr signatures. The state of the sequencer contract can be updated only if a correct SNARK proof is provided. This is a critical step that ensures the validity and security of state updates in Espresso's consensus protocol⁠.

The proof of the Schnorr signatures is sent to the `newFinalizedState` function of the `LightClient` contract.

## Verifying the Signatures and Light Client State

The `LightClient` contract also does the work of verifying the proof that is sent by the prover on L1. The `verifyProof` method accepts the proof and a set of public inputs (the `LightClientState`) to check whether the proof correctly verifies the new state being submitted.

```solidity
function verifyProof(LightClientState memory state, IPlonkVerifier.PlonkProof memory proof)
        internal
        virtual
    {
        IPlonkVerifier.VerifyingKey memory vk = VkLib.getVk();
        uint256[] memory publicInput = preparePublicInput(state);

        if (!PlonkVerifier.verify(vk, publicInput, proof, bytes(""))) {
            revert InvalidProof();
        }
    }
```

Verifying a SNARK proof requires a constant amount of space and computation, no matter how many HotShot node signatures are involved. This is unlike verifying the signatures directly, which would require space and computation proportional to the number of signers.

The proof itself contains the HotShot state, the stake table info and the list of Schnorr signatures of the HotShot nodes that formed a Quorum and came to consensus on that state.

This `verifyProof` method is executed when the `newFinalizedState` method is called so that the new state is accepted only if the proof succeeds.

## Escape Hatch Functionality

Rollup contracts keep track of their rollup VM states and depend on our Light Client contract for finalized consensus states. They usually support escape hatches in case of liveness failures on L2. Since different rollups impose different predicates when deciding whether L2 is down, our Light Client contract provides some helper functions to detect delays in HotShot updates. The Rollup contracts can then implement their escape hatch logic based on this info.

Two such helper functions are:

* `function getHotShotCommitment(uint256 hotShotBlockHeight)`
  * Returns the root of the HotShot block commitment tree, where each leaf contains the HotShot block commitment at a new height
* `function lagOverEscapeHatchThreshold(uint256 blockNumber, uint256 threshold)`
  * Returns whether there has been delay between updates
  * Checks if the HotShot state updates lag behind the specified threshold based on the provided L1 block number.
  * The rollup chooses the threshold based on their liveness criteria.
  * HotShot would be considered down if the gap between two consecutive updates where the provided L1 block number should have been recorded, exceeds the specified threshold

Periodically, the light client contract is updated with the latest validated HotShot state. We store a 10 day sliding window of historical Hotshot state roots, `stateHistoryCommitments`, so that optimistic rollups' dispute handling contracts can access required HotShot commitment data during disputes (which is usually during 7 day windows).

## Public Write Methods

### newFinalizedState

This method updates the latest finalized light client state. It is updated per epoch. An update for the last block for every epoch has to be submitted before any newer state can be accepted since the stake table commitments of that block become the snapshots used for vote verifications later on.

*The contract has the ability to be in permissioned mode where there is only one prover that has the ability to call this function. In the next release, only a permissioned prover doing the computations will call this function*

```solidity
function newFinalizedState(LightClientState memory newState, IPlonkVerifier.PlonkProof memory proof)
    external;
```

**Parameters**

| Name       | Type                        | Description            |
| ---------- | --------------------------- | ---------------------- |
| `newState` | `LightClientState`          | new light client state |
| `proof`    | `IPlonkVerifier.PlonkProof` | Plonk proof            |

### computeStakeTableComm

Given the light client state, compute the short commitment of the stake table

```solidity
function computeStakeTableComm(LightClientState memory state) public pure returns (bytes32);
```

## Light Client Contract UML

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-acabb82289537ab480c9f08761d3772ccf0a81ec%2FLightClientUML.png?alt=media" alt=""><figcaption></figcaption></figure>

## Light Client Contract Interaction Diagram

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-6207ed1a69b78ce511f7f54b819b4cf88e790f50%2FLightClientGraph.png?alt=media" alt=""><figcaption></figcaption></figure>
