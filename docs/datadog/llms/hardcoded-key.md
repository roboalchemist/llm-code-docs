# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-security/hardcoded-key.md

---
title: Prevent usage of hardcoded keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent usage of hardcoded keys
---

# Prevent usage of hardcoded keys

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-security/hardcoded-key`

**Language:** Apex

**Severity:** Warning

**Category:** Security

**CWE**: [321](https://cwe.mitre.org/data/definitions/321.html)

## Description{% #description %}

This rule aims to prevent the use of hardcoded keys or initialization vectors (IVs) in cryptographic operations. Hardcoding sensitive cryptographic material directly in the source code poses significant security risks, as it makes keys easily discoverable and vulnerable to unauthorized access.

To comply with this rule, developers should generate encryption keys and IVs dynamically at runtime using secure methods or retrieve them securely from protected storage mechanisms. For example, instead of `Blob key = Blob.valueOf('0000000000000000');`, a compliant approach would be `Blob key = Blob.valueOf(getRandomValue());` where `getRandomValue()` produces a secure, random key.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
class NotCompliant {

    public void notCompliant() {
        Blob data = Blob.valueOf('some data');
        Blob encrypted = Crypto.encrypt('AES128', '0000000000000000', 'Hardcoded IV 123', data);
    }
}
```

```
class NotCompliant {

    public void notCompliant() {
        Blob encryptedText = Blob.valueOf('Some encrypted cipher text');
        Blob IV = Blob.valueOf(generateEncryptionIV());
        Blob key = Blob.valueOf('0000000000000000');
        Blob encrypted = Crypto.encrypt('AES128', key, IV, data);
    }
}
```

```
class NotCompliant {

    public void compliant() {
        Blob encryptedCipherText = Blob.valueOf('some encrypted text');
        Blob hardCodedIV = Blob.valueOf('my IV');
        Blob key = Blob.valueOf(generateEncryptionKey());
        Blob encrypted = Crypto.encrypt('AES128', key, hardCodedIV, data);
    }
}
```

```
class NotCompliant {

    public void badCryptoDecryption() {
        Blob encryptedCipherText = Blob.valueOf('some text');
        Blob hardCodedIV = Blob.valueOf('hardcoded iv');
        Blob hardCodedKey = Blob.valueOf('0000000000000000');
        Blob decryptedCipherText = Crypto.decrypt('AES128', hardCodedKey, hardCodedIV, encryptedCipherText);
    }
}
```

```
class NotCompliant {

    public void notCompliant() {
        Blob IV = Blob.valueOf(generateEncryptionIV());
        Blob hardCodedKey = Blob.valueOf('0000000000000000');
        Blob data = Blob.valueOf('Data to be encrypted');
        Blob encrypted = Crypto.encrypt('AES128', hardCodedKey, IV, data);
    }
}
```

```
class NotCompliant {

    public void notCompliant() {
        Blob hardCodedIV = Blob.valueOf('Hardcoded IV 123');
        Blob key = Blob.valueOf(generateEncryptionKey());
        Blob data = Blob.valueOf('Data to be encrypted');
        Blob encrypted = Crypto.encrypt('AES128', key, hardCodedIV, data);
    }
}
```

```
class NotCompliant {

    public void notCompliant() {
        Blob hardCodedIV = Blob.valueOf('Hardcoded IV 123');
        Blob hardCodedKey = Blob.valueOf('0000000000000000');
        Blob data = Blob.valueOf('Data to be encrypted');
        Blob encrypted = Crypto.encrypt('AES128', hardCodedKey, hardCodedIV, data);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
class Compliant {
    public void compliantExample() {
        Blob encryptedText = Blob.valueOf('foobar');
        Blob IV = Blob.valueOf(generateEncryptionIV());
        Blob key = Blob.valueOf(getRandomValue());
        Blob encrypted = Crypto.encrypt('AES128', key, IV, data);
    }
}
```

```
class NotCompliant {

    public void goodCryptoEncryption() {
        Blob IV = Blob.valueOf(getRandomValue());
        Blob key = Blob.valueOf(getRandomValue());
        Blob data = Blob.valueOf('Data to be encrypted');
        Blob encrypted = Crypto.encrypt('AES128', key, IV, data);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
