# Source: https://docs.silabs.com/openthread/3.0.0/using-secure-vault-openthread/02-secure-vault.md

# Secure Vault

On Series 1 devices, the security features are implemented by the TRNG (if available) and CRYPTO peripherals.

All the security features on Silicon Labs Series 2 devices are implemented using Secure Engine and CRYPTOACC (if available). Types of secure engine implementations in Series 2 devices fall in one of the following categories:

- HSE - Hardware Secure Engine
- VSE - Virtual Secure Engine
- SE - Secure Engine (either HSE or VSE, in general)

The Secure Engine implements and extends all cryptography-related hardware accelerations. Three levels of Secure Vault feature support are available, depending on the part and SE implementation, as reflected in the following table:

**Table**: Cryptographic Hardware Acceleration Features on Silicon Labs Devices

|Level (1)|SE Support|Part (2)|
|---|---|---|
|Secure Vault High (SVH)|HSE only (HSE-SVH)|EFR32xG2yB (3)|
|Secure Vault Mid (SVM)|HSE (HSE-SVM)|EFR32xG2yA (3)|
|“|VSE|EFM32PG2y, EFR32xG2y (4)|
|Secure Vault Base (SVB)|N/A|MCU Series 1 and Wireless SoC Series 1|

**Notes**:

1. The features of different Secure Vault levels can be found in [https://www.silabs.com/security](https://www.silabs.com/security).
2. The x can be a letter B, F, M, or Z.
3. At the time of this writing, the y is a digit 1 for the HSE device.
4. At the time of this writing, the y is a digit 2 for the VSE device.

The Secure Vault Mid consists of two core security functions:

- Secure Boot: Process where the initial boot phase is executed from an immutable memory (such as ROM) and where code is authenticated before being authorized to be executed.
- Secure Debug access control: The ability to lock access to the debug ports for operational security, and to securely unlock them when access is required by an authorized entity.

The Secure Vault High offer additional security options as follows:

- Secure Key Storage: Protects cryptographic keys by “wrapping” or encrypting the keys using a root key known only to the HSE-SVH.
- Anti-Tamper protection: A configurable module to protect the device against tamper attacks.
- Device authentication: Functionality that uses a secure device identity certificate along with digital signatures to verify the source or target of device communications.

## Secure Key Storage

One of the main features of Secure Vault is secure key storage (see [Secure Key Storage](/openthread/{build-docspace-version}/efr32-secure-key-storage) for more information). The cryptographic keys are encrypted by the device’s root key before they are stored in memory for later use. These keys are then available only through the Cryptographic APIs and are referenced by the application with their unique key reference. This allows potentially unlimited secure key storage in any storage location. The keys themselves can be either non-volatile or temporary and the user can choose the key storage location using the attributes.

OpenThread uses the following mechanism to store and use keys available in the stack:

- The user generates the key and specifies the crypto operation that is allowed by the key and the access settings (whether the key can be exported).
- The application passes this key to Secure Vault. Secure Vault then wraps the key and stores it in the specified memory (volatile or non-volatile, based on user settings).
- The application then provides the user with a reference that can be used for Crypto operations.

### PSA Crypto

Platform Security Architecture (PSA) is designed by ARM to address the security requirements for IoT devices. It is made up of four stages:

- Threat modelling
- Predefined architectural choices
- Standardized implementation
- Certification

PSA Crypto is one of the standardized implementations of the features recommended by PSA. It implements low-level APIs for cryptographic operations, optimized for MCUs and Wireless SoCs. The PSA Crypto APIs provide easy-to-use interfaces for crypto primitives. These APIs are based on the idea of secure key storage. Access to keys is restricted to the Cryptographic APIs.

![PSA Functional APIs](/using-secure-vault-openthread/0.1/images/sld803-image1.png)
