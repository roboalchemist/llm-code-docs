# Source: https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/frequently_asked_questions.md

# Frequently Asked Questions

> Common questions about GitGuardian's secrets detection engine, including how detectors work, false positives, and custom detection.

At any point when reading this FAQ section you can use our [glossary](./glossary.md) to find some useful definitions.

### How does GitGuardian's detection engine work, roughly speaking?

For an extensive response, you can consult [this page](./quick_start.md). GitGuardian's detection engine revolves around the concept of detectors. A detector is a set of instructions that our detection engine will execute on a given input document to catch secrets in it. The flow of instructions is always the same:

- Pre-Validation: discard documents as early as possible if they are of no interest for secrets detection.
- Matching: look for a given pattern.
- Post-Validation: apply some validation steps to select only relevant secrets.
  All these steps are performed using a combination of regular expressions and heuristics based on contextual information.

### What is the difference between generic and specific detectors?

Simply put, a **specific detector** is designed to find a well identified type of secret whereas a **generic detector** yields secrets that are not associated with a given provider. For a bit more details, you can refer to this [documentation on detectors](./detectors/introduction.md).

### Does GitGuardian check the validity of credentials?

When possible, **GitGuardian will check the validity of the detected credentials**. To do so, GitGuardian performs the **least intrusive call as possible** to the service. We favor HEAD requests, or GET requests when we cannot. We also select endpoints that do not return any personal information. Once this is done, the secret will be labelled as either:

- valid: the service call was successful and confirms the secret is **valid**.
- invalid: the service call was successful and confirms the secret is **invalid**.
- failed to check: the service call was not successful, so we can't tell whether the secret is valid or not.

There are a few situations which can lead to "failed to check". For example, this happens when the service is internal and thus not reachable from our servers. Another common example is if the service was down at the time we tried to call it. We can't tell whether the secret is valid or invalid so we remain cautious and report the incident.

### Why do some detectors only report incidents for valid secrets?

The format of some secrets makes it impossible to create a detector with a good enough precision. This is the case for example if the secret has no prefix, no suffix and no fixed length. Reporting all matching potential secrets would produce too many false positives. To avoid that, we only report the secret if it has been confirmed valid by a check.
Detectors for these secrets are marked as "Only valid secrets raise an alert".

### What do you call a false positive exactly in the context of secrets detection?

In the context of secrets detection, a false positive occurs when our detection engine raises an alert for a secret that is not one and has never been one.
For more details on false positives, recall and precision, we highly recommend reading this [blog post](https://blog.gitguardian.com/secrets-detection-accuracy-precision-recall-explained/).

### How to properly test GitGuardian detection capabilities?

To properly test our engine, we recommend reading this documentation carefully, and especially looking at detector's examples that will provide you with some good test cases.
You can also use this [example repository](https://github.com/GitGuardian/sample_secrets) to get familiar with our detection engine's behavior.
If a secret is not detected by one of our detectors, you can refer to [this question](#did-not-detect) to get some explanations.

### Why didn't GitGuardian detect my secret?

First of all, we recommend building your test cases by following our detector's [documentation](./detectors/supported_credentials.md). For each detector, we provide a set of examples that are detected by our engine. Here are also some possible reasons why we did not raise an alert for your secret:

- The associated detector is checked, and your secret is not valid anymore. In that case, the secret is labelled as invalid and no alert is raised.
- You somehow obfuscated your secret to test our detection capabilities, and that's a good practice. But you may have broken the pattern of the key in the process: make sure you kept an identical length and charset.
- Your secret could not pass our pre-validation steps: for certain detectors we ban markdown files, or we require a given context for the detection to occur. You can refer to the concerned detector's documentation [here](./detectors/supported_credentials.md).
- Your secret is not part of the required [assignment](./glossary.md#assignment-and-assigned-variable). Look at the detector's examples to see what patterns are detected.

### Weâve seen real credentials in .md files in the past already, why do some of your detectors drop .md files?

At GitGuardian one of our biggest challenges is to achieve a detection with the highest precision and the best recall possible, in other words squaring the circle. To do so, we battle test our algorithms on GitHub's live data feed. We also permanently monitor our detector's performance by looking at explicit feedback from developers or from our checkers, as well as implicit feedback: e.g. secrets removal.
Thanks to this feedback, we decided to drop markdown files in certain detectors in an effort to reduce alert fatigue and increase our precision. To know which detectors are concerned, you can refer to detectors' pre-validation steps' documentation.

### Are cryptographic keys sensitive objects?

**Cryptographic Keys**

Cryptographic algorithms are tools used to secure communications over public channels such as the Internet. Based on mathematical hard problems, they are the building blocks of protocols such as TLS (for secure internet browsing via https) or SSH (for secure remote access to servers). The different security features provided by cryptography are authentication, authorization, and encryption. To this end, cryptographic algorithms are bound to cryptographic keys that are used to unlock or lock these functions.

We distinguish two types of keys, symmetric or asymmetric keys:

- A symmetric key is shared between the communicating entities.
- Asymmetric keys are composed of a public and a private key. The public key is distributed to everyone to initiate a communication or a protocol and the private key is used to verify and carry on the communication or the protocol.
  Having access to someone's symmetric key or asymmetric private key can have devastating consequences. A malicious adversary could then impersonate an entity, tamper its communications, or simply have access to all its secure data.

**How we detect private keys**

After the introduction of the series of IETF RFC [1421](https://tools.ietf.org/html/rfc1421), [1422](https://tools.ietf.org/html/rfc1422), [1423](https://tools.ietf.org/html/rfc1423), and [1424](https://tools.ietf.org/html/rfc1424) most implementation libraries involving cryptography (such as OpenSSL) use a shared format to store the cryptographic keys called PEM (stands for Privacy-Enhanced Mail). This format has a very structured form, always starting with the same pattern. This is very convenient for detection as it implies a high recall on the different implemented detectors. We based our family of cryptographic key detectors on the particularity of the PEM format to get very efficient and precise detectors. Here is the list of the detectors currently implemented in our suite:

- [Generic private key](./detectors/specifics/private_key_generic.md).
- [DSA private key](./detectors/specifics/private_key_dsa.md).
- [Elliptic curve private key](./detectors/specifics/private_key_elliptic.md).
- [RSA private key](./detectors/specifics/private_key_rsa.md).
- [OpenSSH private key](./detectors/specifics/private_key_openssh.md).
- [PGP private key](./detectors/specifics/private_key_pgp.md).
- [Encrypted private key](./detectors/specifics/private_key_encrypted.md).
- [Putty private key](./detectors/specifics/putty_private_key.md).

We targeted the main cryptographic algorithms or protocols, which are the most commonly used ones and referenced one by standard entities. For each of those algorithms, we implemented a detector for both the PEM format form and the Base64 encoded version.

**What about public key certificates?**
One frequently asked question by the public and our customers is about the sensitivity of a certificate. Public-key certificates are used in TLS protocols in order to establish authenticated and secure communication channels when browsing the web, displayed as https and a green lock on the website. They are in essence just public keys augmented with a signature that everyone can access to (simply click on the lock). As such, they have no sensitivity and the augmented signatures just provide trust to users that this certificate was issued by a trusted party. The trusted party is usually referenced by either the browser or the OS (Linux, Windows, macOS, etc) during installation.
