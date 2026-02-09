# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managed TLS

When an [Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) requires a Certificate to perform SSL / TLS termination on your behalf, you can opt to let Aptible provision and renew certificates on your behalf. To do so, enable Managed HTTPS when creating your Endpoint. You'll need to provide Aptible with the [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) name you intend to use so Aptible knows what certificate to provision. Aptible-provisioned certificates are valid for 90 days and are renewed automatically by Aptible.

Alternatively, you can provide your own with a [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate).

# Managed HTTPS Validation Records

Managed HTTPS uses [Let's Encrypt](https://letsencrypt.org) under the hood. There are two mechanisms Aptible can use to authorize your domain with Let's Encrypt, and provision certificates on your behalf:

For either of these to work, you'll need to create some CNAMEs in the DNS provider you use for your Custom Domain. The CNAMEs you need to create are listed in the Dashboard.

## http-01

> 📘  http-01 verification only works for Endpoints with [External Placement](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#endpoint-placement) that do **not** use [IP Filtering](/core-concepts/apps/connecting-to-apps/app-endpoints/ip-filtering). Wildcard domains are not supported either.

HTTP verification relies on Let's Encrypt sending an HTTP request to your app and receiving a specific response (presenting that the response is handled by Aptible).

For this to work, you must have a setup a CNAME from your [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) to the [Endpoint Hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname) provided by Aptible.

## dns-01

> 📘 Unlike http-01 verification, dns-01 verification works with all Endpoints.

DNS verification relies on Let's Encrypt checking for the existence of a DNS TXT record with specific contents under your domain.

For this to work, you must have created a CNAME from `_acme-challenge.$DOMAIN` (where `$DOMAIN` is your [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain)) to an Aptible-provided validation name. This name is provided in the Dashboard (it's the `acme` subdomain of the [Endpoint's Hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname)). The `acme` subdomain has the TXT record containing the challenge token that Let's Encrypt is looking for.

> ❗️ If you have a TXT record defined for `_acme-challenge.$DOMAIN` then Let's Encrypt will use this value instead of the value on the `acme` subdomain and it will not issue a certificate.

> 📘 If you are using a wildcard domain, then `$DOMAIN` above should be your domain name, but without the leading `*.` portion.

# Wildcard Domains

Managed TLS supports wildcard domains, which you'll have to verify using [dns-01](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls#dns-01).

Aptible automatically creates a SAN certificate for the wildcard and its apex when using a wildcard domain. In other words, if you use `*.$DOMAIN`, then your certificate will be valid for any subdomain of `$DOMAIN`, as well as for `$DOMAIN` itself.

> ❗️ A single wildcard domain can only be used by one Endpoint at a time. This is due to the fact that the dns-01 validation record for all Endpoints using the domain will have the same `_acme-challenge` hostname but each requires different data to in the record. Therefore, only the Endpoint with the matching record will be able to renew its certificate. If you would like to use the same wildcard certificate with multiple Enpdoints you should acquire the certificate from a trusted certificate authority and use it as a [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) on all of the Endpoints.

# Rate Limits

Let's Encrypt enforces a number of rate limits on certificate generation. In particular, Let's Encrypt limits the number of certificates you can provision per domain every week. See the [Let's Encrypt Rate Limits](https://letsencrypt.org/docs/rate-limits) documentation for details.

> ❗️ When you enable Managed TLS on an Endpoint, Aptible will provision an individual certificate for this Endpoint. If you create an Endpoint, provision a certificate for it via Managed TLS, then deprovision the Endpoint, this certificate will count against your weekly Let's Encrypt weekly rate limit.

# Creating CAA Records

If you want to set up a [CAA record](https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization) for your domain, please add Let's Encrypt to the list of allowed certificate authorities. Aptible uses Let's Encrypt to provision certificates for your custom domain.
