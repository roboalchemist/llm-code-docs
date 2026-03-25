# Source: https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/zk-attestation-verification.md

# ZK Attestation Verification

Our rollup integrations now use on-chain verifiable zero-knowledge proofs for TEE attestation reports on AWS Nitro. This improves on our [previous design](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup#high-level-integration-flow), where TEE attestation proofs were verified directly on-chain.

### Introduction

TEE attestation report verification for AWS Nitro was extremely expensive on-chain in our previous design, costing around **63 million gas** to validate an attestation when no certificates had been previously verified.

After the Fusaka upgrade and the resulting changes to gas costs for certain opcodes, on-chain attestation verification became infeasible for L2s and L3s. To address this, we integrated with **Automata Network’s AWS Nitro ZK proof generation** [**SDK**](https://github.com/automata-network/aws-nitro-enclave-attestation/tree/main), which enables the creation of zero-knowledge proofs for verification of TEE attestation reports, and their **NitroEnclaveVerifier** [**contract**](https://github.com/automata-network/aws-nitro-enclave-attestation/blob/main/contracts/src/NitroEnclaveVerifier.sol), which allows these ZK proofs to be verified on-chain.

Under the hood, Automata uses **Succinct’s SP1** for proof [generation](https://docs.succinct.xyz/docs/sp1/getting-started/install) and **sp1-**[**contracts**](https://github.com/succinctlabs/sp1-contracts) for on-chain ZK proof verification. This integration reduced gas costs from **63 million to approximately 260k**, representing roughly a \~240× improvement

### High Level Integration Flow

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2FX3ngkMs1gBMMIba5Hx2c%2Fzk_attestation.png?alt=media&#x26;token=3890df01-2947-4470-a118-86bb003eaf3a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: Our previous flow can be found [here](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup#high-level-integration-flow)
{% endhint %}

**Updated Flow:**

* The batch poster running inside a TEE creates a TEE attestation and sends it to Espresso’s attestation verifier service.
* The attestation verifier service calls Automata’s Nitro ZK Attestation SDK, which gathers all required inputs and calls the Succinct Network to generate a zero-knowledge proof over the verification of the TEE attestation
* The Succinct Network returns the proof, which Espresso’s Attestation SDK then passes back to the batch poster.
* The batch poster submits the ZK proof to L1 along with other batch data, where it is verified by a set of on-chain contracts.

### Requirements & Trust Dependencies

With this new flow, we require the rollups/RaaS providers to have a few new trust dependencies and requirements

**Trust Dependencies**

* Succinct Network
* Automata’s Nitro ZK Attestation SDK

**Requirements**

* Rollup/RaaS needs to run Espresso’s Attestation Verifier service
* Succinct Network tokens in-order for the network to generate the ZK Proof. It is estimated to cost around 0.3 PROVE tokens for each request. New request will be made every time there is a new code update or a new restart ( the restart requirement will be removed soon) and batcher needs to generate a new TEE attestation.

### On-chain Cost Analysis

Cost analysis based on prices on Jan 8th, 2026.&#x20;

```
Base Fee on Ethereum: 0.53 GWEI
Ether Price: 3,091.47USD
Prove token prices: $0.4349 USD
```

\
**Calculations based on every code update**

| Design                                             | On-chain Costs                                         | Additional Costs         | Total Cost  |
| -------------------------------------------------- | ------------------------------------------------------ | ------------------------ | ----------- |
| AWS Nitro attestation report Verification on-chain | (63 million \* 0.53 GWEI) \~ 0.03 Ether \~ 93 USD      | None                     | \~ 93 USD   |
| ZK Proof Verification on-chain                     | <p>(270k  \* 0.53 GWEI) <br>0.0001378 ETH \~ $0.4 </p> | 0.3 PROVE token \~ $0.13 | \~$0.53 USD |
