# Source: https://docs.silabs.com/openthread/3.0.0/using-secure-vault-openthread/04-updates-to-openthread-to-include-psa-crypto-apis.md

# Updates to OpenThread to Include PSA Crypto APIs

The OpenThread stack supports crypto operations using either literal keys or key references. This can be configured using the macro **OPENTHREAD_CONFIG_PLATFORM_KEY_REFERENCES_ENABLE**. Also, Openthread stack now supports PSA or mbedTLS APIs for Crypto operations. The stack defaults to using mbedTLS APIs, but it can be configured to use PSA using **OPENTHREAD_CONFIG_CRYPTO_LIB**.

> **Note**: The OpenThread sample apps provided in the SDK have the PSA Crypto with key references enabled by default, except for radio co-processor (RCP) and network co-processor (NCP) applications.

In general, the following points highlight the general changes in OpenThread stack to integrate PSA Crypto API usage.

- All the keys stored in the `key_manager` and `sub_mac` modules are replaced with key references.
- When `key_manager` and `sub_mac` receive security keys, they pass the keys to the PSA abstraction for storage, and only retain the references to these keys.
- The packets in any Rx or Tx events are updated with the relevant key references so that PSA Crypto modules can use them to perform security processing.

![Crypto Module Operation in OpenThread with PSA](/using-secure-vault-openthread/0.1/images/sld803-image3.png)

All keys are wrapped before storing and all the keys are stored in volatile memory (RAM), apart from **Thread Master Key** and **PSKc.** These are stored in NVM, to be retained and re-used in the future. The following table lists the security keys stored in Secure Vault along with their corresponding PSA attributes.

**Cryptographic Keys in the OpenThread Stack**

|Key|Type|Usage|Persistence|
|---|---|---|---|
|Thread Master Key|PSA_KEY_TYPE_HMAC|PSA_KEY_USAGE_SIGN_HASH PSA_KEY_USAGE_EXPORT|PSA_KEY_LIFETIME_PERSISTENT|
|PSKc|PSA_KEY_TYPE_RAW_DATA|PSA_KEY_USAGE_EXPORT|PSA_KEY_LIFETIME_PERSISTENT|
|MLE Key|PSA_KEY_TYPE_AES|PSA_KEY_USAGE_ENCRYPT PSA_KEY_USAGE_DECRYPT|PSA_KEY_LIFETIME_ VOLATILE|
|Temp MLE key|PSA_KEY_TYPE_AES|PSA_KEY_USAGE_ENCRYPT PSA_KEY_USAGE_DECRYPT|PSA_KEY_LIFETIME_ VOLATILE|
|Key Encryption Key|PSA_KEY_TYPE_AES|PSA_KEY_USAGE_ENCRYPT PSA_KEY_USAGE_DECRYPT PSA_KEY_USAGE_EXPORT|PSA_KEY_LIFETIME_ VOLATILE|
|MAC Previous Key|PSA_KEY_TYPE_AES|PSA_KEY_USAGE_ENCRYPT PSA_KEY_USAGE_DECRYPT|PSA_KEY_LIFETIME_ VOLATILE|
|MAC Current Key|PSA_KEY_TYPE_AES|PSA_KEY_USAGE_ENCRYPT PSA_KEY_USAGE_DECRYPT|PSA_KEY_LIFETIME_ VOLATILE|
|MAC Next Key|PSA_KEY_TYPE_AES|PSA_KEY_USAGE_ENCRYPT PSA_KEY_USAGE_DECRYPT|PSA_KEY_LIFETIME_ VOLATILE|

> **Note**: The keys part of the dataset are still stored in the NVM and are only copied into Secure Vault.

Crypto modules in OpenThread are updated to support the PSA APIs. These APIs use the key references provided by the stack to perform security processing on the incoming/outgoing messages.

## Security Manager

A new platform abstraction has also been introduced to abstract some of the security operations from the core stack. This abstraction acts as an interface to the PSA module and extends PSA interfaces to the stack.

> **Note**: As the PSA does not yet support the PBKDF2, the stack uses mbed TLS APIs for these operations.