# Source: https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-encryption/database-encryption.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Encryption at Rest

This section covers Aptible's default managed encryption. For more information about encryption using AWS Key Management Service, see [Custom Database Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/custom-database-encryption).

Aptible automatically and transparently encrypts data at rest.

[Database](/core-concepts/managed-databases/overview) encryption uses eCryptfs, and the algorithm used is either AES-192 or AES-256.

> 📘 You can determine whether your Database uses AES-192 or AES-256 for disk encryption through the Dashboard. New Databases will automatically use AES-256.

# Key Rotation

Aptible encrypts your data at the disk level. This means that to rotate the key used to encrypt your data, all data needs to be rewritten on disk using a new key. If you're not using [Custom Database Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/custom-database-encryption), you can do so by dumping the data from your database, then writing it to a new database, which will use a different key.

However, rotating keys this way will inevitably cause downtime while you dump and restore your data. This may take a long time if you have a lot of data.

Therefore, if you must conform to a strict key rotation schedule, we recommend implementing [Application-Level Encryption](/core-concepts/managed-databases/managing-databases/database-encryption/application-level-encryption).
