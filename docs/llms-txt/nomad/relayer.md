# Source: https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/relayer.md

# Relayer

{% hint style="info" %}
Relayers are **permission-less and trust-less**. This means that anyone can operate a Relayer for channels they are interested in.
{% endhint %}

The relayer forwards updates from the home to one or more replicas.

**It is an off-chain actor that does the following:**

* Observe the home
* Observe 1 or more replicas
* Polls home for new signed updates (since replica's current root) and submits them to replica
* Polls replica for confirmable updates (that have passed their optimistic time window) and confirms if available (updating replica's current root)
