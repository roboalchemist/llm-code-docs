# Source: https://docs.asapp.com/reporting/secure-data-retrieval.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Secure Data Retrieval

> Learn how to set up secure communication between ASAPP and your real-time event API.

# Secure Data Retrieval

TLS, specifically Mutual-TLS (mTLS), secures communication between ASAPP and a customer's real-time event API endpoint. This document provides details on the expected configuration of the mTLS-secured connection between ASAPP and the customer application.

## Overview

Mutual TLS requires that both server and client authenticate using digital certificates. The mTLS-secured integration with ASAPP relies on public certificate authorities (CAs). In this scenario, clients and servers host certificates issued by trusted public CAs (like Digicert, Symantec, etc.).

## Certificate Configuration

To further secure the connection, ASAPP requires the following additional configurations:

1. ASAPP's client certificate will contain a unique identifier in the "Subject" field. Customers can use this identifier to confirm that the presented certificate is from a legitimate ASAPP service. This identifier will be based on client identification conventions mutually agreed upon by ASAPP and the customer (e.g., UUIDs, namespaces).

2. Both server and client certificates will have validities of less than 3 years, in accordance with industry best practices.

3. Server certificates must have the "Extended Key Usage" field support "TLS Web Server Authentication" only. Client certificates must have the "Extended Key Usage" field support "TLS Web Client Authentication" only.

4. Minimum key sizes for client/server certificates should be:
   * 3072-bit for RSA
   * 256-bit for AES

## TLS/HTTPS Settings

REST endpoints must only support TLSv1.3 when setting up HTTPS connections. Older versions support weak ciphers that can be broken if a sufficient number of packets are captured.

### Supported Ciphers

Ensure that each endpoint supports only the following ciphers (or equivalent):

* TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256
* TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256
* TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305
* TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256
* TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305

### Session Limits

TLS settings should limit each session to a short period. TLS libraries like OpenSSL set this to 300 seconds by default, which is sufficiently secure. A short session limits the usage of per-session AES keys, preventing potential brute-force analysis by attackers who capture session packets.

<Note>
  Qualys provides a free tool called SSLTest ([https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)) to check for common issues in server TLS configuration. We recommend using this tool to test your public TLS endpoints before deploying to production.
</Note>
