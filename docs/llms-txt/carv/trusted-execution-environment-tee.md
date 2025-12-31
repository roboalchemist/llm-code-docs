# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work/trusted-execution-environment-tee.md

# Trusted Execution Environment (TEE)

* **Role Assignment**: The **TEE role** can only be assigned by the **admin** of the Service contract, ensuring that only trusted entities manage sensitive operations.
* **Attestation Submission**: Only **users or nodes** with TEE permissions are authorized to submit **attestations**, ensuring a controlled and secure submission process.
* **Privacy and Security**: **TEE nodes** are responsible for processing **encrypted data**, ensuring that sensitive information remains secure throughout the execution process. This guarantees the **privacy of user data**, allowing operations to be performed without exposing any confidential information.
* **Batching and On-Chain Attestation**: **TEE nodes** play a critical role in **batching and submitting attestations** on-chain. They collect, verify, and consolidate multiple attestations, then post them in batches to the blockchain. This approach ensures that the data is verifiable and transparent while also maintaining efficiency by reducing on-chain transaction costs.
