# Source: https://docs.aws.amazon.com/speke/latest/documentation/llms.txt

# Secure Packager and Encoder Key Exchange API Specification Partner and customer guide

> Secure Packager and Encoder Key Exchange (SPEKE) is part of the AWS Elemental content protection strategy for media services customers. SPEKE defines the standard for communication between our media services and digital rights management (DRM) system key servers. SPEKE is used to encrypt video on demand (VOD) content through AWS Elemental MediaConvert and for live and VOD content through AWS Elemental MediaPackage.

- [What is Secure Packager and Encoder Key Exchange?](https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html)
- [Are you new to SPEKE?](https://docs.aws.amazon.com/speke/latest/documentation/are-you-new-to-speke.html)
- [Customer onboarding](https://docs.aws.amazon.com/speke/latest/documentation/customer-onboarding.html)
- [Document history](https://docs.aws.amazon.com/speke/latest/documentation/doc-history.html)

## [SPEKE API specification](https://docs.aws.amazon.com/speke/latest/documentation/speke-api-specification.html)

- [Authentication required for SPEKE](https://docs.aws.amazon.com/speke/latest/documentation/authentication.html): SPEKE requires authentication for on-premises products and for services and features that run in the AWS Cloud.

### [SPEKE API v1](https://docs.aws.amazon.com/speke/latest/documentation/the-speke-api.html)

This is the REST API for Secure Packager and Encoder Key Exchange (SPEKE) v1.

- [SPEKE API v1 - Customizations and constraints to the DASH-IF specification](https://docs.aws.amazon.com/speke/latest/documentation/speke-constraints.html): Learn about the customizations and constraints applied by Secure Packager and Encoder Key Exchange to the DASH-IF CPIX specification.
- [SPEKE API v1 - Standard payload components](https://docs.aws.amazon.com/speke/latest/documentation/standard-payload-components.html): In any SPEKE request, the encryptor can request responses for one or more DRM systems.
- [SPEKE API v1 - Live workflow method call examples](https://docs.aws.amazon.com/speke/latest/documentation/live-workflow-methods.html): Request Syntax Example
- [SPEKE API v1 - VOD workflow method call examples](https://docs.aws.amazon.com/speke/latest/documentation/vod-workflow-methods.html): Request Syntax Example
- [SPEKE API v1 - Content key encryption](https://docs.aws.amazon.com/speke/latest/documentation/content-key-encryption.html): You can optionally add content key encryption to your SPEKE implementation.
- [SPEKE API v1 - Heartbeat](https://docs.aws.amazon.com/speke/latest/documentation/heartbeat.html): Request Syntax Example
- [SPEKE API v1 - Overriding the key identifier](https://docs.aws.amazon.com/speke/latest/documentation/kid-override.html): The encryptor creates a new key identifier (KID) each time that it rotates keys.

### [SPEKE API v2](https://docs.aws.amazon.com/speke/latest/documentation/the-speke-api-v2.html)

This is the REST API for Secure Packager and Encoder Key Exchange (SPEKE) v2.

- [SPEKE API v2 - Customizations and constraints to the DASH-IF specification](https://docs.aws.amazon.com/speke/latest/documentation/speke-constraints-v2.html): Learn about the customizations and constraints applied by Secure Packager and Encoder Key Exchange to the DASH-IF CPIX specification.
- [SPEKE API v2 - Standard payload components](https://docs.aws.amazon.com/speke/latest/documentation/standard-payload-components-v2.html): Through a single SPEKE request, the encryptor can request multiple content keys, together with the necessary manfest signaling for multiple packaging formats, according to the encryption contract that is defined for a given content.
- [SPEKE API v2 - Encryption contract](https://docs.aws.amazon.com/speke/latest/documentation/encryption-contract-v2.html): The encryption contract defines which content keys are protecting which tracks inside a given streamset, based on the tracks characteristics.
- [SPEKE API v2 - Live workflow method call examples](https://docs.aws.amazon.com/speke/latest/documentation/live-workflow-methods-v2.html): Request Syntax Example
- [SPEKE API v2 - VOD workflow method call examples](https://docs.aws.amazon.com/speke/latest/documentation/vod-workflow-method-v2.html): Request Syntax Example
- [SPEKE API v2 - Content key encryption](https://docs.aws.amazon.com/speke/latest/documentation/content-key-encryption-v2.html): You can optionally add content key encryption to your SPEKE implementation.
- [SPEKE API v2 - Overriding the key identifier](https://docs.aws.amazon.com/speke/latest/documentation/kid-override-v2.html): The encryptor creates a new key identifier (KID) each time that it rotates keys.
- [License for the SPEKE API specification](https://docs.aws.amazon.com/speke/latest/documentation/license.html)
