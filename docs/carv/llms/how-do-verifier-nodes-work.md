# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work.md

# How do Verifier Nodes Work

## Overview

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FCAYwqEiIvXKa6MYJqVgd%2Fcarv_protocol_contract_overview.png?alt=media&#x26;token=457cc0f4-e03e-4650-9183-d80b98843a2d" alt=""><figcaption><p>CARV Smart Contract Design</p></figcaption></figure>

The CARV Protocol consists of five key modules, each corresponding to a separate smart contract: **Proxy**, **Service**, **Vault**, **VRF Manager**, and **Settings**. Each module serves a specific function within the system:

* **Vault Contract:** The Vault contract is responsible for managing the assets within the CARV Protocol. It supports three distinct roles: **CARV Treasury**, **veCARV Reward Pool**, and each role is limited to specific operations that can be executed only through predefined methods. The Vault also defines the **reward release curve**, which governs and restricts how reward funds are handled.
* **Settings Contract**: This contract manages all the configurations within the CARV Protocol.
* **VRF Manager Contract**: The VRF Manager is used to obtain random numbers by calling services like **Chainlink** or **CARVLink** and processing their callbacks. It ensures that logic contracts can access random numbers in a **decoupled** way, allowing smooth upgrades to the random number generation logic without disrupting the system.
* **NFT Contract:** This contract oversees the purchase and redemption of NFTs by users. The ETH from NFT purchases is stored in the NFT account within the Vault. Upon redemption, 80% of the ETH is returned to the user (with the remaining 20% serving as a channel fee) or exchanged for an equivalent amount of CARV, which is then linearly released back to the user. The exchange of ETH for CARV is managed by the foundation, completed by the Vault contract, and based on Chainlink exchange rates.
* **Protocol Service Contract:** This contract handles the majority of the business logic and includes several components:
  * **Access Management**: Manages different roles such as admin, TEE (Trusted Execution Environment), and slash roles.
  * **System Parameter Management**: Governs system parameters through the Settings contract.
  * **Verifier Operations**: Includes actions like entering, exiting, reporting activity, applying slashes, and managing commissions and claimers.
  * **Delegation Operations**: Includes delegation, redelegation, and undelegation processes.
  * **Report Operations**: Manages attestations and verifications.
  * **Claim Operations**: Handles verifier claims and NFT token ID claims.

## Verifier Nodes Workflow

1. Upon completing data processing, TEE nodes submit the data verification, AI model training result and the TEE attestation to smart contracts on the execution layer.
2. The smart contracts employ a Verifiable Random Function (VRF) to randomly choose a subset of verifiers for attestation validation.

   > In cryptography, a verifiable random function (VRF) is a random number generator (RNG) that generates an output that can be cryptographically verified as random. Verifiable randomness is essential to many blockchain applications because its tamper-proof unpredictability enables exciting gameplay, rare NFTs, and unbiased outcomes. As the name suggests, a verifiable random function is defined by its core features: Verifiable, Random, Function.
3. Verifiers monitor events from the smart contract to initiate the verification process.
4. Verifiers assess the authenticity of the attestation. For more details, please check [sgx-attestation-verification](https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work/sgx-attestation-verification "mention")
5. Based on the outcome, verifiers relay their findings to the smart contract:
   * If the attestation is invalid, the smart contract penalizes the responsible TEE node by slashing its stake, which is then allocated to the verifiers as additional rewards.
6. When the attestation is confirmed as valid with over 50% of designated Verifiers, the smart contract distributes not only the consumers' fees but also on-chain rewards among the TEE nodes, verifiers, and data providers.
