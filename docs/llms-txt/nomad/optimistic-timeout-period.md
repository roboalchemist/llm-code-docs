# Source: https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period.md

# Optimistic Timeout Period

Nomad's optimistic design assumes a window during which honest watchers can submit fraud proofs on-chain and prevent fraud from being settled within the system.

This section aims to cover common questions that are asked around the timeout period design.

### What happens during the timeout to prove fraud?

As described in the [parent section on Fraud](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud), Nomad requires Watchers to inform both the Home and Replica contracts about fraud.

The current Watcher response to fraud is as follows:

1. Fraud occurs on any Replica
2. Watcher observes the fraud
3. Watcher submits transaction on origin chain, slashing the Updater and shutting down the Home contract
4. Watcher submits transaction on all destination chains, shutting down message processing from Replicas

The optimistic timeout period is enforced on the Replica, expressed as [`optimisticSeconds`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Replica.sol#L38). Step #4 needs to be completed within the optimistic window.

### How long is the timeout period right now?

Currently, the window is configured to be 30 minutes for all chains. This is conservatively parameterized and anchored against the assumption that it is not economically feasible for an adversary to censor transactions on any chain Nomad is deployed on for over 30 minutes.

### How is it calculated?

When calculating the timeout period, we must ask a few questions:

* For any given chain, what is the **uncensorable period**? I.e. how long must we wait for it to be highly unlikely that an adversary could block a Watcher’s transaction proving fraud?
  * In other words, can the adversary purchase the blockspace on this chain for longer than the timeout period? If so, it is insufficient.
  * How much of the gas token, in dollars, can we reasonably expect a Watcher to lock up in their hot key to submit transactions? I.e. what is the maximum capital requirement?
  * What is the max `gasPrice` we can configure to submit the transaction blocking fraud, given the amount of capital we can lock up?
* What is the **buffer time** that a Watcher must be given to to observe fraud ahead of submitting a transaction?
  * This can be automated and shaved down over time, but we must be conservative initially.

Given that a watcher must submit a proof on both the Home and the Replica, as described in the previous section, then our calculation depends on three values for any given chain pair (X, Y):

1. Buffer (C) - a small constant to provide buffer for the Watcher to observe fraud
2. Uncensorable period for origin chain X (U\_x)
3. Uncensorable period for destination chain Y (U\_y)

Therefore, we posit that the fraud period can be calculated using:

*Replica(X, Y) = max(U\_x, U\_y) + C*

### Why doesn't it have to be 7 days like optimistic rollups?

Optimistic rollups like Optimism or Arbitrum, and Nomad share a common lineage of using optimistic mechanics with fraud games.

Both systems attempt to post state transitions from one domain to another.

* *Optimistic rollups*: state transitions on L2; source of truth on L1
* *Optimistic interoperability*: state transitions on origin domain; source of truth on destination domain. Note that this implies an L1 or L2 on either end.

In optimistic interoperability, **state transitions happen at the source of truth**. Therefore, fraud games are simple; incorrect state transitions can be easily compared to the canonical state transitions on the origin chain, which is also the source of truth and has full data availability.

In rollups, fraud games are way more complicated. Any incorrect state transitions must go through an intense proving process on the L1, which doesn’t have a record of the state transitions, but is the source of truth.

This is why the 7 day period exists for rollups -- not because of any computational time limit, but rather to allow for social consensus on what the truth is, since it cannot be verified on L1. Comparatively, Nomad's fraud period can be 30 minutes or shorter since data availability exists on the origin, allowing for a quick equivalence check off-chain, followed by instant on-chain fraud proving.

Additionally, because of the difference in complexity here, fraud games for rollups are more difficult to implement. Rollups like Optimism initially launched without fraud games being implemented. In Nomad however, fraud games have already been implemented and have been live in production since day 1.
