# Source: https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/liveness-assumptions.md

# Liveness Assumptions

All interoperability systems have safety and liveness assumptions, and Nomad is no exception. By safety and liveness, we mean the following:

* **Safety:** The property of a system that ensures that only the rightful owner of any funds or data can decide what to do with it.
  * I.e. Bob cannot send Alice's money through Nomad to his account.
* **Liveness:** The property of a system that ensures that the owner of any funds or data can access them at any given time.
  * I.e. Alice can *always* send her money through Nomad.

The previous sections largely focused on safety assumptions, and this one will focus on liveness.

The bulk of Nomad's liveness assumptions are around its [off-chain agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents). Since these agents are responsible for ensuring that messages get safely shuttled between chains, Nomad seeks to minimize any liveness issues occurring from negligent or malicious agent behavior.

### Agent Liveness Assumptions

#### Updater

Updaters are permissioned.

Nomad reduces the overhead of cross-chain communication by only relying on one external party, [the Updater](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater), to verify state. The downside of this is that if the Updater suffers downtime, its associated [Home](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) can no longer receive updates, leading to a liveness failure on the outbound channel.

This will be mitigated by adding Updater downtime slashing, where an Updater that has failed to sign for some number of blocks may have their bond slashed. Additionally, an Updater rotation model may be considered to enable standby Updaters to step in if a primary Updater is experiencing downtime. A rotation may also be performed manually through governance.

#### Watcher

Watchers are permissioned.

Nomad's core security assumption is that *at least* one honest Watcher maintain liveness and be ready to flag fraud in the event of a malicious Updater.&#x20;

Watcher liveness failures in isolation are not an issue, as there will be multiple other Watchers running at any given time. However, all Watchers experiencing liveness failures is a massive risk to the system as the Updater's signatures would be taken as word after the optimistic timeout period.

For this reason, we recommend that all Watcher operators run multiple redundant setups, where the same Watcher key may be used. This ensures that even if any key enclave is breached, that there is another setup running the Watcher hot key which can still be used to flag fraud. Unlike validator-based systems, there is also no risk of equivocation or double-signing faults.

We address [watcher griefing attacks](#undefined) in the section below.

**Relayer**

Relayers are fully permission-less and trust-less — they are functionally similar to IBC relayers.

All Relayers experiencing downtime will cause liveness failures on any channels the Relayers are supporting. As long as one party spins up a relayer and maintains liveness, this issue is mitigated.&#x20;

#### Processor

Processors are fully permission-less and trust-less.

All Processors experiencing downtime will prevent messages from being proven against Replicas' updated state, and dispatched the end xApp. Processors, similar to Relayers, are convenience agents. If Processors experience downtime, *anyone* may spin up a Processor, or manually process their messages.

### Watcher Griefing

One of the criticisms of Nomad is that malicious Watchers can "grief", or cause liveness failures to Nomad channels. While this is not entirely correct, critics are right to point out in that Nomad's current design, an adversarial Watcher *can* prevent applications from processing messages even if no fraud actually occurred.

Nomad's current Watcher design requires that Watchers [publish occurrence of fraud on the Replica](https://docs.nomad.xyz/the-nomad-protocol/security/fraud#publishing-fraud-on-the-replica). In this model, any application that delegates permissions to the Watcher publishing fraud will automatically halt processing messages from the Replica, aka become disconnected from the Replica.

If fraud did occur, then the application would be protected. In the event that fraud did *not* occur, the application would then be prevented from processing honest messages, constituting a liveness failure for its users. **However, channel-wide liveness failures are not possible.**

Under the [app-governed root of trust model](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/app-governed-root-of-trust), applications delegate Watcher disconnection permissions per their xAppConnectionManager contract. If a Watcher publishes fraud on a Replica, it may still continue to get Updates from an Updater. This ensures that an adversarial watcher can never cause total liveness failures on a channel.

If an application is disconnected from the Replica by a malicious watcher, it can leverage its own governance to remove the watcher from its permissioned set and re-establish connection.
