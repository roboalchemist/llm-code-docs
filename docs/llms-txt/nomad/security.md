# Source: https://docs.nomad.xyz/the-nomad-protocol/security.md

# Security

{% hint style="info" %}

#### **Pre-requisite Reading**

The following material assumes an understanding of how cross-chain communication works and specifically how messages are verified.

If you are not familiar with these concepts, it is highly recommended that you read the section on [Verification Mechanisms](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms) before jumping into this section, which covers security in detail.
{% endhint %}

Security is paramount for Nomad. As described in the section on [Optimistic Verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification), Nomad's design philosophy centers around trust-minimization and a bias towards safety, which are core components of security when it comes to addressing[ root of trust insecurity](https://docs.nomad.xyz/verification-mechanisms/background-on-verification#root-of-trust-insecurity).

This section will cover the three following topics:

1. [**Nomad's Root of Trust**](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust)\
   Our goal with Nomad is to create cross-chain communication that is resilient against critical attack vectors. Accordingly, this topic will cover the advanced aspects of Nomad's verification mechanism design, including fraud prevention, app-specific design, and liveness assumptions.

2. [**Attack Vectors**<br>](https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors)This section will cover the common attack vectors used to compromise interoperability protocols, including compromising keys, economic attacks, and smart contract vulnerabilities unrelated to a compromised root-of-trust.<br>

3. [**Long-term Security**](https://docs.nomad.xyz/the-nomad-protocol/security/long-term-security)\
   We believe that for crypto to take on the responsibility of onboarding the world's users and becoming the primary rails for finance, we need to think long-term. This means considering financial controls and other common security measures taken in traditional finance. This section is more exploratory in nature.

Note that this Security documentation primarily focuses on protocol security and Nomad's design. To learn more details about Nomad's operational security, check out the [Operational Security ](https://docs.nomad.xyz/operational-security)section.
