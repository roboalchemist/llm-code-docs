# Source: https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud.md

# Fraud

As described in the section on [optimistic verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification), Nomad's design introduces the possibility of the [Updater](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater) committing fraud.

Though this possibility exists, Nomad minimizes the chance of fraud by guaranteeing that:

1. Fraud is easily observed by anyone
2. Fraud is costly. Anyone can slash a fraudulent updater
3. Fraud will be blocked. Permissioned Watchers can block Fraud before it takes effect in order to protect applications.

Because honest Watchers have time to observe and react to fraud, Nomad ensures the safety of the system while preserving other desirable properties like low cost and extensibility.

### What Constitutes Fraud?

The Updater is the only actor in the Nomad system that can commit fraud in an attempt to cause safety failures. By fraud, we simply mean any case where an Updater signs an attestation to a merkle root that did not actually exist on the Home chain.

For example:

* The canonical merkle root is `0xabcd...1234` — it reflects a commitment to all honest messages enqueued by applications and their users.
* The Updater signs a fraudulent update attesting to merkle root `0xefgh...6789` — this root contains a malicious inserted message which sends all the funds escrowed in the[Nomad token bridge](https://docs.nomad.xyz/token-bridge) to the Updater's address.

If the latter fraudulent state root is submitted to a Replica contract, then the malicious message can be authenticated against it after the optimistic timeout, which would enable the Updater to abscond with all of the escrowed funds.

{% hint style="info" %}
For more details on Updaters, including their role and purpose in Nomad, please check out the[Updater documentation](https://docs.nomad.xyz/off-chain-agents/updater#updater-selection).
{% endhint %}

### Preventing Fraud

In order to prevent the malicious message from taking effect, Nomad enforces a dispute window during which all submitted roots remain pending. During this window, any honest [Watcher](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) can block the Replica from processing messages, which prevents the malicious message from settling.

#### Detecting Fraud

Detecting fraud is Nomad is very simple. Per the example above, fraud is easily noticed on the Home by observing for two distinct forms of fraud:

1. **Improper updates** — where the Updater commits to an entirely invalid update
2. **Double updates** — where the Updater commits to two conflicting updates

Double updates are easy to detect — if the Updater ever signs two updates where the old root is the same, but new roots conflict, this constitutes fraud.

Improper updates are also easy to detect. The Home contract maintains a [queue of roots](https://docs.nomad.xyz/smart-contracts/home#queue-of-roots) which contains every root generated — one for each message enqueued. If the Updater signs a root which isn't contained in this queue, this also constitutes fraud.

The reason fraud is easy to detect in Nomad is we only need to check that state on remote chains is equal to the canonical state on the origin chain. Fundamentally, all we're doing is checking equivalence and inclusion of hashes, both of which can be done very quickly.

#### Proving Fraud on the Home

Importantly, fraud can always be **proven** to the Home contract on the origin chain. The Home contains the canonical message tree and the queue of roots, so any fraud attempted by the Updater can be proven deterministically on-chain and punished.

Thus, the Updater must submit a bonded stake on the origin chain which can be slashed as punishment. Anyone can permissionlessly prove fraud.

#### Blocking Fraud on the Replica

Unfortunately, certain types of fraud can't be objectively proven on the receiving chain; Replicas can't know which messages were sent on the origin chain and therefore can't check message tree validity in all cases.

Therefore, we rely on permissioned Watchers to **block** fraud on the Replica. Blocking Fraud simply involves unenrolling a Replica with a fraudulent root from the application's xAppConnectionManager contract, which disconnects the applications from receiving messages from that Replica. This effectively pauses message passing until Fraud has been remediated, keeping the application (and any funds or sensitive permissions therein) safe.

To learn more about how xApps disconnect from Replicas, please read more on [App-Governed Root of Trust](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/app-governed-root-of-trust).
