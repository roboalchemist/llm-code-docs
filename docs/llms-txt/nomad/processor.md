# Source: https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/processor.md

# Processor

{% hint style="info" %}
Processors are **permission-less and trust-less**. This means that anyone can operate a Processor for channels they are interested in.
{% endhint %}

The processor proves the validity of pending messages and sends them to end recipients.

**It is an off-chain actor that does the following:**

* Observe the home
* Maintain local merkle tree with all leaves
* Observe 1 or more replicas
* Maintain list of messages corresponding to each leaf
* Generate and submit merkle proofs for pending (unproven) messages
* Dispatch proven messages to end recipients
