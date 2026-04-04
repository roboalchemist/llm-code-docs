# Source: https://docs.asapp.com/security/warning-about-customerinfo-and-sensitive-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Warning about CustomerInfo and Sensitive Data

> Learn how to securely handle Customer Information.

<Warning>
  Do not send sensitive data via `CustomerInfo`, `custom_params`, or `customer_params`.
</Warning>

ASAPP implements strict controls to ensure the confidentiality and security of ALL data  we handle on behalf of our customers. For **sensitive data**, ASAPP employs an even more stringent level of control. ("Sensitive data" includes such categories as Personal Health Information, Personally Identifiable Information, and financial/PCI data.)

In general, ASAPP recommends that customers ONLY send sensitive data in specified fields, and where ASAPP expects to receive such data.

ASAPP treats all customer data securely. By default, however, ASAPP may not apply the strictest levels of controls that we maintain for **sensitive data** for content submitted via `CustomerInfo`, `custom_params`, or `customer_params`.

## What is CustomerInfo?

Certain calls available via ASAPP APIs and SDKs provide a parameter that supports the inclusion of arbitrary data with the call.

We'll refer to such fields as **"CustomerInfo"** here, even though different ASAPP interfaces may call them "custom\_params", "customer\_params", and "CustomerInfo".

CustomerInfo is typically a JSON object containing a set of key:value pairs that ASAPP and ASAPP customers can use in multiple ways. For example, as context input for use in the ASAPP Web SDK:

```javascript  theme={null}
"CustomerInfo": {
    "Inflight": true,
    "TierLevel": "Gold"
}
```

## Do not send sensitive data as cleartext via CustomerInfo

ASAPP strongly recommends that our customers do NOT send sensitive data using CustomerInfo.

If customer requirements dictate that sensitive data must be sent via CustomerInfo, CUSTOMERS MUST ENCRYPT SENSITIVE DATA BEFORE SENDING. The customer should encrypt any sensitive data before sending via CustomerInfo, using a private encryption mechanism (i.e. a mechanism not known to ASAPP).

This practice will ensure that ASAPP never has access to the customer's sensitive data, so that data will remain securely protected while in transit through ASAPP systems.

Additionally, ASAPP strongly recommends that our customers use strong encryption. Specifically, we insist that customers use one of the following configurations:

* **Symmetric Encryption Model:** use AES-GCM-256 (authenticated encryption) with a random [salt](https://en.wikipedia.org/wiki/Salt_\(cryptography\)) to provide data integrity, confidentiality and enhanced security. Each combination of salt+associated data should be unique.
* **Asymmetric Encryption Model:** use a key size of 2048, and use RSA as an algorithm. ASAPP recommends setting a key expiration date of less than two years. ASAPP and the customer should both have mechanisms in place to update the key being used. Temporarily retain private keys which are rotated for the purposes of accessing previously encrypted data.

In extraordinary circumstances, ASAPP can make exceptions to these requirements. Please contact your ASAPP account team to discuss options if you have a compelling business need to have ASAPP implement an exception.
