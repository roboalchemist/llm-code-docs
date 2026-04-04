# Source: https://docs.silabs.com/openthread/3.0.0/using-secure-vault-openthread/03-security-handling-in-openthread.md

# Security Handling in OpenThread

Several cryptographic keys are described and used in the Thread protocol. These keys are stored in different modules in the OpenThread stack. All the keys, apart from the Thread Master Key and PSKc, are volatile and are not stored in non-volatile memory (NVM). OpenThread implements a Key Manager module to handle most of the keys required by the Thread protocol.

The following table lists the cryptographic keys used by the OpenThread stack and the module that handles these keys.

**Cryptographic keys in OpenThread stack**

|Key|Usage|Module|Storage location|
|---|---|---|---|
|Thread Master Key|Used to derive the MAC and MLE keys|Key Manager|NVM|
|Pre-shared Key for the Commissioner (PSKc)|Used to establish a commissioner session|Key Manager|NVM|
|MLE Key|Used for Mesh Link Establishment Used by MLE for transmit and receive operations|Key Manager|RAM|
|Temporary MLE key|Used to process received UDP packet, if the incoming packet has a different keySequence number than that used in the device.|Key Manager|RAM|
|Key Encryption Key|Used by MAC to process incoming and outgoing packets with keyIdMode0 as 802.15.4 security material|Key Manager|RAM|
|Pre-shared key for the device (PSKd)|Used in the DTLS exchange to verify the identity of the Joiner|Key Manager|RAM|
|MAC Previous Key|MAC key for **key sequence = current seq - 1**|MAC|RAM|
|MAC Current Key|MAC key for **key sequence = current seq**|MAC|RAM|
|MAC Next Key|MAC key for **key sequence = current seq + 1**|MAC|RAM|

OpenThread has a modular approach to security. Each layer of the stack has security implementations and uses common modules for the actual security processing. The current implementation of OpenThread in GitHub uses mbed TLS for all the security operations and, as such, uses all the keys in plaintext for these operations.

![Crypto Module Operation in OpenThread](/using-secure-vault-openthread/0.1/images/sld803-image2.png)