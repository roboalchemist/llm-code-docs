# Source: https://docs.datadoghq.com/security/application_security/security_signals/attacker_fingerprint.md

---
title: Attacker Fingerprint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Investigate Security
  Signals > Attacker Fingerprint
---

# Attacker Fingerprint

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

This topic describes a feature called **Datadog Attacker Fingerprint** to identify attackers beyond IP addresses.

## Overview{% #overview %}

Datadog Attacker Fingerprint identifies attackers beyond IP addresses. Datadog Attacker fingerprints are automatically computed and added to your traces on attack or login attempts when App and API Protection (AAP) is enabled on your service.

Datadog Attacker fingerprints are composed of several fragments:

- Endpoint Identifier
- Session Identifier
- Header Identifier
- Network Identifier

Each fragment identifies request specifics by looking for certain headers and query body fields, and by hashing cookie values and query parameters.

## Attacker Fingerprint fragment details{% #attacker-fingerprint-fragment-details %}

### Endpoint identifier{% #endpoint-identifier %}

The endpoint identifier fragment provides information about a specific endpoint, as well as the parameters used to call it. This fragments uses the following information:

- HTTP method
- Hash of request URI
- Hash of query parameter fields
- Hash of body fields

### Session identifier{% #session-identifier %}

The session identifier fragment tracks users based on their session information and whether they are authenticated. This fragment uses the following information:

- Hash of user ID
- Hash of cookie fields
- Hash of cookie values
- Hash of session ID

If all of the fields are unavailable, the fragment is omitted as it does not provide meaningful information.

### Header identifier{% #header-identifier %}

The header identifier fragment provides information about the headers used in the request. This particular fragment uses the following information:

- Presence of known headers: Referer, Connection, Accept-Encoding, etc.
- Hash of user agent
- The number of unknown headers
- Hash of unknown headers. The list of unknown headers excludes all XFF headers, cookies and x-datadog headers.

### Network identifier{% #network-identifier %}

The network identifier fragment provides information about the network part of the request. This fragment uses the following information:

- The number of IPs in the XFF header used by the caller to determine the client's IP.
- The presence or absence of the known XFF headers

## How to use Attacker Fingerprints{% #how-to-use-attacker-fingerprints %}

Fragments can be used as filters in the AAP Traces explorer by filtering on the desired fingerprint field. For example: `@appsec.fingerprint.header.ua_hash:e462fa45` will filter on all requests that have the same user agent hash.

Attacker fingerprints are used in the [Attacker Clustering](https://docs.datadoghq.com/security/application_security/security_signals/attacker_clustering) feature. If a significant portion of your traffic presents the same fingerprint attributes, attacker clustering will show it has a common attack attribute.

## Further reading{% #further-reading %}

- [Attacker Clustering](https://docs.datadoghq.com/security/application_security/security_signals/attacker_clustering)
