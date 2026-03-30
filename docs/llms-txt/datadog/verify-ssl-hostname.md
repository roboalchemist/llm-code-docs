# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-security/verify-ssl-hostname.md

---
title: Always verify SSL/TLS hostnames when validating certificates
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Always verify SSL/TLS hostnames when validating certificates
---

# Always verify SSL/TLS hostnames when validating certificates

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-security/verify-ssl-hostname`

**Language:** Kotlin

**Severity:** Error

**Category:** Security

**CWE**: [297](https://cwe.mitre.org/data/definitions/297.html)

## Description{% #description %}

This rule enforces the secure verification of SSL/TLS hostnames when validating certificates. In secure communication, this step is crucial to prevent Man-In-The-Middle (MITM) attacks. In such a case, an attacker could intercept the communication, present a fraudulent certificate, and if hostname verification is not implemented or is improperly implemented, the client might accept it.

Developers sometimes disable hostname verification for testing purposes or to bypass certain network restrictions. This practice opens up a serious security vulnerability when used in production code. You must ensure that you do not override the hostname verifier to return `true` for all hostnames, because this accepts any certificate, even if it's not valid for the server you're connecting to.

To avoid violating this rule, always use the default hostname verification provided by the SSL/TLS library (such as `OkHttpClient`, `HttpsURLConnection`, or `SSLContext`). These libraries have secure hostname verification enabled by default; do not disable or modify it. If you need to handle exceptions for certain hostnames, you can use a custom hostname verifier that checks the hostname against a list of allowed exceptions instead of accepting all hostnames.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
import javax.net.ssl.*
import java.net.URL
import okhttp3.OkHttpClient
import java.security.cert.X509Certificate

class InsecureConnections {
    // Pattern 1: OkHttpClient with disabled verification
    fun createInsecureOkHttpClient(): OkHttpClient {
        return OkHttpClient.Builder()
            .hostnameVerifier { _, _ -> true }  // Insecure: accepts any hostname
            .build()
    }

    // Pattern 2: OkHttpClient with disabled verification
    fun createInsecureOkHttpClient2(): OkHttpClient {
        val builder2 = OkHttpClient.Builder()
        builder2.hostnameVerifier(object : HostnameVerifier {
            override fun verify(hostname: String?, session: SSLSession?): Boolean { // Insecure: accepts any hostname
                return true
            }
        })
    }

    // Pattern 3: HttpsURLConnection with disabled verification
    fun createInsecureUrlConnection(urlString: String): HttpsURLConnection {
        val url = URL(urlString)
        val connection = url.openConnection() as HttpsURLConnection
        connection.hostnameVerifier = HostnameVerifier { _, _ -> true }  // Insecure
        return connection
    }

    // Pattern 4: SSLSocketFactory with disabled verification
    fun createInsecureSSLContext(): SSLContext {
        val trustAllCerts = arrayOf<TrustManager>(object : X509TrustManager {
            override fun getAcceptedIssuers(): Array<X509Certificate> = arrayOf()
            override fun checkClientTrusted(chain: Array<X509Certificate>, authType: String) {}
            override fun checkServerTrusted(chain: Array<X509Certificate>, authType: String) {}
        })

        return SSLContext.getInstance("TLS").apply {
            init(null, trustAllCerts, java.security.SecureRandom())
        }.also { context ->
            HttpsURLConnection.setDefaultSSLSocketFactory(context.socketFactory)
            // Insecure: Disables hostname verification globally
            HttpsURLConnection.setDefaultHostnameVerifier { _, _ -> true }
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class SecureConnections {
    // Pattern 1: OkHttpClient with default verification
    fun createSecureOkHttpClient(): OkHttpClient {
        return OkHttpClient.Builder()
            // No custom hostname verifier = uses default secure verification
            .build()
    }

    // Pattern 2: HttpsURLConnection with default verification
    fun createSecureUrlConnection(urlString: String): HttpsURLConnection {
        val url = URL(urlString)
        return url.openConnection() as HttpsURLConnection
        // Default hostname verifier is secure
    }

    // Pattern 3: SSLSocketFactory with default verification
    fun createSecureSSLContext(): SSLContext {
        return SSLContext.getInstance("TLS").apply {
            init(null, null, null) // Uses system default security providers
        }
        // Default hostname verification remains intact
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
