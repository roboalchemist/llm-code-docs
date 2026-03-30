# Source: https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors/key-compromise.md

# Key Compromise

One of the more common attacks in the traditional info-sec world is to compromise private keys which are responsible for safeguarding data or value. In interoperability protocols, key compromise strikes at the root-of-trust, and allows attackers to compromise the verification mechanism itself.

In the interoperability category, the best example is the [Ronin Network Bridge Exploit](https://roninblockchain.substack.com/p/back-to-building-ronin-security-breach), which led to over $600M being stolen once 5-of-9 validator keys were breached.

## How They Work

Key compromise attacks are the most brute force way of compromising trust-network based systems. In [externally verified systems](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification) like multisigs, validator systems and oracle networks, a majority of keys being breached is sufficient to execute an attack on the system. In the common security adage — defense always has to be right, whereas offense only has to be right *once*.

There are two primary vectors that attackers probe to compromise keys — infrastructure vulnerabilities and social engineering.

### Infrastructure Vulnerabilities

Private keys in interoperability systems often are ["hot" keys](https://www.fireblocks.com/blog/hot-vs-warm-vs-cold-which-crypto-wallet-is-right-for-me/), which means that they are exposed to a public network (aka the internet) in order to be able to receive requests and sign messages without human intervention. Contrast this to "cold" keys which are often stored on a hardware device like a Ledger and require manual intervention to sign messages.

Naturally, hot key setups allows for greater speed and liveness guarantees in the context of bridging. However, the trade-off is that they need to expose an interface to the internet at all times.

This is precisely what attackers target in infrastructure attacks — they probe external verifiers' setups looking for a hole by which they can access and decrypt keyfiles, and sign messages without the honest verifiers' knowledge.&#x20;

### Social Engineering

Often, [phishing](https://en.wikipedia.org/wiki/Phishing) and other social engineering techniques are used to gain access to confidential information, which is then used to attack or compromise the system. While not as technically sophisticated as infrastructure attacks, social engineering maneuvers are often much cheaper and far more effective, as humans are more malleable and dynamic than computer systems.

Methods leveraged by attackers include:

* Posing as a coworker or friend and asking for sensitive information
* Exposing links that look authentic but lead to malware or spyware being installed
* Infiltrating organizations, building rapport, and accessing confidential information through clearance

These may seem farfetched, but per the Ronin Network attack described above, these attacks do happen and the ROI is extremely high for attackers. Once attackers socially engineer their way into accessing keys, the end result is the same as infra attacks — the system gets rugged.

## Defense

### Nomad's Revocation-Centric Design

Nomad's design is inherently defensive against key compromise by splitting responsibility across two classes of actors:

1. [**Updaters**](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater) — have the permissions to verify cross-chain messages
2. [**Watchers**](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) — have the permissions to revoke, or disconnect, applications from Replicas

The key insight here (pun yet again intended :drum:) is that Watchers cannot *permit* messages to be sent cross-chain. They only have *revocation* permissions. **Therefore, even if all Watcher keys in Nomad are compromised and collude with the Updater, as long as the honest Watcher operator has a backup key, they may always prevent fraud in Nomad.**

For example, let's examine a setup where Nomad has one Updater and 8 Watchers. A common question we get is, "isn't this functionally equivalent to a 9-of-9 multisig address?"

The answer is **no**. In the multisig setup, if all 9 keys are compromised, cross-chain messages can be corrupted. In Nomad, even if all 9 keys are compromised, as long as any one Watcher operator has a redundant setup with a copy of the key, they can still sign messages to flag fraud and protect the system.

The worst case scenario in Nomad is if all keys are compromised, then malicious Watcher keys may be used to temporarily grief or censor applications from messages. Once this Watcher key is rotated out, the system resumes normal operations. We cover this in greater detail in the[#watcher-griefing](https://docs.nomad.xyz/the-nomad-protocol/root-of-trust/liveness-assumptions#watcher-griefing "mention") sub-section.

### **Operational Security**

In addition to being designed to resist key compromise, the Nomad core team also follows security best practices to reduce the chances of any infrastructure or core team members being compromised.

From an infrastructure standpoint, we:

* Have an internal SRE team following best practices in key management
* Conduct regular internal audits on our systems
* Provision strict access to sensitive key material
* Run redundant setups of critical agents
* Are progressively decentralizing the system to include more agent operators

From a social standpoint, we:

* Remain vigilant and have internal guidance around social attacks
* Only give access to sensitive information on a need-to-know basis
* Conduct fake attacks to ensure team members are responding appropriately
* [Don't act a fool](https://www.youtube.com/watch?v=DJnKm6ftPu0)

For obvious reasons, we are only sparingly sharing details right now, while we determine what is acceptable to share. We will continue to add more details in the [operational-security](https://docs.nomad.xyz/operational-security "mention") section.
