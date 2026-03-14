# Source: https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms.md

# Verification Mechanisms

Nomad's primary design difference from other cross-chain messaging protocols is its usage of [**optimistic verification**](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification).

By leveraging an optimistic mechanism, Nomad reduces the trust assumptions relative to [externally verified systems](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification) (eg. multisig, PoS, and oracle based designs). While these systems require an honest majority (k-of-n) to function safely, Nomad only requires **a single honest watcher (1-of-n).**&#x20;

This section will provide:

* [A background on verification in the context of cross-chain communications](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/background-on-verification)
* A description of the different verification mechanisms:
  * [Native verification — why it is the ideal, but impractical](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification)
  * [External verification — why it has proliferated, but is insecure](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification)
  * [Optimistic verification — how it reaches a via media, and what it trades off](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification)
* [A comparison of the different mechanisms and popular constructions](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/comparing-mechanisms)&#x20;
