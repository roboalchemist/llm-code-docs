# Source: https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/fraud-recovery.md

# Fraud Recovery

The ideal scenario is that fraud never happens. In the event that it does however, Nomad has a built-in mechanism via the [optimistic timeout period](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period) to prevent it. Once fraud has been prevented, the system will need to be recovered and set back into normal operations. This section covers that process from a high level.

Post-fraud, the state on-chain is as follows:

* The [Home](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) where fraud was flagged is in the `FAILED` state. This means that the Home can no longer accept new Updates.
* Replicas are un-enrolled in the xAppConnectionManager for all xApps. Replicas CAN accept new Updates, but message processing is paused for all xApps.

### How does Nomad Recover?

When Fraud has occurred, there are three main categories of action that must be taken to recover the channel:

1. [Block Further Fraud](#block-further-fraud)
2. [Erase Past Fraud](#erase-past-fraud)
3. [Restore the Channel](#revive-the-system)&#x20;

{% hint style="info" %}
**Note:** In this document, Fraud Recovery is defined / considered within the context of one single Updater’s lifecycle.
{% endhint %}

### Block Further Fraud&#x20;

[Fraud](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud) being detected implies that Updater is either malicious, compromised, or (unfortunately) the victim of a large re-org on the origin chain. In any case, the Updater must be removed from their position of power, in order to prevent them from submitting any further fraudulent Updates in the future.

**Home**

* The Home is in a `FAILED` state, and the fraudulent Updater can no longer submit any Updates&#x20;
* Therefore, further Fraud from this Updater is automatically blocked

**Replica**

* The Updater can keep submitting Updates indefinitely while they still hold the Updater role&#x20;
* In order to block ongoing fraud attempts from a malicious Updater, they must be un-seated from their privileged role
* This must be done **before** attempting to erase past fraud; otherwise, there is no definitive cap on the amount of fraudulent state that must be erased

### Erase Past Fraud

**Home**

* By definition, fraudulent roots cannot be stored on the Home — data availability on the home guarantees that it will be [detected by the smart contract and automatically prevented](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L228)
  * Therefore, “erasing fraud” is irrelevant within the context of the Home

**Replica**

* Fraudulent roots CAN be submitted to the Replica at any time
* As long as a fraudulent root is set in the [`confirmAt`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Replica.sol#L42) mapping on the Replica, it is or will soon be possible to attempt to prove messages against it
* Once the Updater has been un-seated from their role, they can no longer continue to submit fraudulent updates
* Therefore, there is a finite number of fraudulent roots *from that Updater* which can be present on the Replica
* In order to restore the integrity of the Replica, Nomad governance must erase fraudulent Updates from all Replicas affected
* When this is done, the state on the Replica will once again appropriately reflect the state of the Home
* At this point, processing messages from the Replica is once again safe

### Restore the Channel&#x20;

Once the attempted damage done by a fraudulent Updater has been mitigated, it is safe to allow the system to continue operating. In order to do so, we must rotate the Updater role to a new key, with which the system can have a renewed sense of (optimistic) trust.

**Home**

* We must rotate the Updater role to a new, un-compromised public key
* We must transition the Home contract state from `FAILED` to `ACTIVE`
* This will allow the Home contract to begin to accept Updates from the new Updater, such that the channel can continue operating as normal

**Replica**&#x20;

* Applications must re-enroll the Replica on their xAppConnectionManager contract&#x20;
* This will allow processing of messages for the xApp to resume as usual
