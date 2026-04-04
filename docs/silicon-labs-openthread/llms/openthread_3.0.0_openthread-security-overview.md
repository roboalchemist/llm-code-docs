# Source: https://docs.silabs.com/openthread/3.0.0/openthread-security-overview/index.md

# Security

Silicon Labs offers a range of security features depending on the part you are using and your application and production needs. As well as the security features available, this section describes security issues specific to OpenThread.

- [**IoT Security Fundamentals**](/openthread/3.0.0/iot-endpoint-security-fundamentals): Introduces the security concepts that must be considered when implementing an Internet of Things (IoT) system. Using the ioXt Alliance's eight security principles as a structure, it clearly delineates the solutions Silicon Labs provides to support endpoint security and what you must do outside of the Silicon Labs framework.
- [**Using Silicon Labs Secure Vault Features with OpenThread**](/openthread/3.0.0/using-secure-vault-openthread):  Describes how Secure Vault features are leveraged in OpenThread applications. It focuses on specific PSA features and emphasizes how these are integrated into the OpenThread stack.
- [**Series 2 and Series 3 Secure Debug**](/openthread/3.0.0/series2-secure-debug): Explains the different debug lock and unlock features available in Series 2 and Series 3 devices and their capabilities.
- [**Production Programming of Series 2 and Series 3 Devices**](/openthread/3.0.0/prod-programming-series2-and-series3): Demonstrates how to properly program, provision, and configure Series 2 and Series 3 devices in a production environment.
- [**Anti-Tamper Protection Configuration and Use**](/openthread/3.0.0/efr32-secure-vault-tamper): Describes how to program, provision, and configure the Secure Engine anti-tamper module. The anti-tamper module is only available on Secure Vault High and Series 3 Secure Vault devices.
- [**Authenticating Silicon Labs Devices using Device Certificates**](/openthread/3.0.0/authenticating-devices-using-device-certificates): Shows how to authenticate an EFR32 Series 2 device with Secure Vault, using secure device certificates and signatures.
- [**Secure Key Storage**](/openthread/3.0.0/efr32-secure-key-storage): Explains how to securely "wrap" keys in EFR32 Series 2 devices with Secure Vault, so they can be stored in non-volatile storage.
- [**Programming Series 2 Devices Using the DCI and SWD**](/openthread/3.0.0/efr32-dci-swd-programming): Describes how to provision and configure Series 2 devices through the DCI and SWD.
- [**Integrating Crypto Functionality with PSA Crypto vs. Mbed TLS**](/openthread/3.0.0/mbedtls-psa-crypto-porting-guide): Describes how to integrate crypto functionality into applications using PSA Crypto compared to Mbed TLS.
- [**Series 2 TrustZone**](/openthread/3.0.0/series2-trustzone): Provides background and information on implementing TrustZone on series 2 devices.