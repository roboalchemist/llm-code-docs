# Source: https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-encryption/application-level-encryption.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Application-Level Encryption

Aptible's built-in [Database Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/overview) is sufficient to comply with most data regulations, including HIPAA Technical Safeguards 45 C.F.R. § 164.312 (e)(2)(ii), but we strongly recommend also implementing application-level encryption in your App to further protect sensitive data.

The idea behind application-level encryption is simple: rather than store plaintext in your database, store encrypted data, then decrypt it on the fly in your app when fetching it from the database.

Using application-level encryption ensures that should an attacker get access to your database (e.g. through a SQL injection vulnerability in your app), they won't be able to extract data you encrypted unless they **also** compromise the keys you use to encrypt data at the application level.

The main downside of application-level encryption is that you cannot easily implement indices to search for this data. This is usually an acceptable tradeoff as long as you don't attempt to use application-level encryption on **everything**. There are, however, techniques that allow you to potentially work around this problem, such as [Homomorphic Encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption).

> 📘 Don't roll your own encryption. There are a number of libraries for most application frameworks that can be used to implement application-level encryption.

# Key Rotation

Application-level encryption provides two main benefits over Aptible's built-in [Database Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/overview) and [Custom Database Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/custom-database-encryption) regarding rotating encryption keys.

## Key rotations are faster

Odds are, not all data is sensitive in your database.

If you are using application-level encryption, you only need to re-encrypt sensitive data when rotating the key, as opposed to having to re-encrypt **everything in your Database**.

This can be orders of magnitude faster than re-encrypting the disk. Indeed, consider that your Database stores a lot of things on disk which isn't strictly speaking data, such as indices, etc., which will inevitably be re-encrypted if you don't use application-level encryption.

## Zero-downtime key rotations are possible

Use the following approach to perform zero-downtime key rotations:

* Update your app so that it can **read** data encrypted with 2 different keys (the *old key*, and the *new key*). At this time, all your data remains encrypted with the *old key*.
* Update your app so that all new **writes** are encrypted using the *new key*.
* In the background, re-encrypt all your data with the *new key*. Once complete, all your data is now encrypted with the *new key*.
* Remove the *old key* from your app. At this stage, your app can no longer need any data encrypted with the *old key*, but that's OK because you just re-encrypted everything.
* Make sure to retain a copy of the *old key* so you can access data in backups that were performed before the key rotation
