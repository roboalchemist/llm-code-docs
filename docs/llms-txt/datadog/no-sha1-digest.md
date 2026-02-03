# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/no-sha1-digest.md

---
title: Avoid SHA1 to generate hashes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid SHA1 to generate hashes
---

# Avoid SHA1 to generate hashes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/no-sha1-digest`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [328](https://cwe.mitre.org/data/definitions/328.html)

## Description{% #description %}

The rule "Avoid SHA1 to generate hashes" is important as it helps to maintain the integrity and security of your data. SHA1 is a widely used cryptographic hash function that produces a 160-bit hash value, however, it is no longer considered secure against well-funded attackers. In 2005, cryptanalysts found attacks on SHA1 suggesting that the algorithm might not be secure enough for ongoing use.

The weakness of SHA1 lies in its inability to avoid hash collisions, which occur when two different inputs produce the same hash output. This can be exploited by attackers to mimic a data piece without having its actual content, leading to potential security risks and data integrity issues.

To avoid violating this rule, use more secure hash functions such as SHA256 or SHA3. In Ruby, you can use `Digest::SHA256.hexdigest 'foo'` or `OpenSSL::Digest::SHA256.new` to generate a SHA256 hash. Similarly, for HMAC, use `OpenSSL::HMAC.hexdigest("SHA256", key, data)`. By using these more secure hash functions, you can ensure the integrity and security of your data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
require 'digest'
class Bad_md5
    def bad_md5_code()
        sha = Digest::SHA1.hexdigest 'foo'
        sha = Digest::SHA1.new
        sha = Digest::SHA1.base64digest 'foo'
        sha = Digest::SHA1.digest 'foo'

        digest = OpenSSL::Digest::SHA1.new
        digest = OpenSSL::Digest::SHA1.hexdigest 'foo'
        digest = OpenSSL::Digest::SHA1.new
        digest = OpenSSL::Digest::SHA1.base64digest 'foo'
        digest = OpenSSL::Digest::SHA1.digest 'foo'
        digest = OpenSSL::Digest.new('SHA1').digest 'foo'
        OpenSSL::HMAC.hexdigest("sha1", key, data)
    end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
require 'digest'
class Good_sha256
    def good_sha256_code()
        sha = Digest::SHA256.hexdigest 'foo'
        sha = Digest::SHA256.new
        sha = Digest::SHA256.base64digest 'foo'
        sha = Digest::SHA256.digest 'foo'

        digest = OpenSSL::Digest::SHA256.new
        digest = OpenSSL::Digest::SHA256.hexdigest 'foo'
        digest = OpenSSL::Digest::SHA256.new
        digest = OpenSSL::Digest::SHA256.base64digest 'foo'
        digest = OpenSSL::Digest::SHA256.digest 'foo'
        digest = OpenSSL::Digest.new("SHA256").digest 'foo'
        OpenSSL::HMAC.hexdigest("sha256", key, data)
    end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 