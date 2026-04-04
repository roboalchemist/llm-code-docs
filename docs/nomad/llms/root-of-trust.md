# Source: https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust.md

# Root of Trust

The root of trust is the lynchpin of an interoperability protocol's security. As the name suggests, it lies at the heart of the system — any trust assumptions are only as strong as the root of trust itself.

Nomad's [optimistic verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification) mechanism is its root of trust. The mechanism ensures that state is not corrupted, and must be bulletproof for any application building on top of Nomad.

There are two primary components when it comes to Nomad's root of trust security:

1. [**Fraud Detection**](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud) — Nomad enables Watchers to monitor the system and flag fraud if they detect anything abnormal. Nomad **requires only one honest** **Watcher** to maintain liveness to protect the system. This ensures that malicious Updaters are not able to confirm corrupt messages within Nomad.
2. [**App-Governed Root of Trust**](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/app-governed-root-of-trust) — Unlike other cross-chain messaging systems that offer monolithic security for all applications, Nomad enables application governance to decide which Watchers they permit to flag fraud and notify their application on-chain.

This section and its associated pages will break down the various components of Nomad's root of trust including:

* How fraud is prevented with the optimistic mechanism
* Why application governed root of trust returns consent to users
* Inherent liveness and economic security assumptions of optimistic verification
