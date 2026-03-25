# Source: https://docs.mailcow.email/post_installation/firststeps-ssl-dns/

Title: SSL with DNS Challenge - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/post_installation/firststeps-ssl-dns/

Markdown Content:
Let's Encrypt with DNS-01 Challenge[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#lets-encrypt-with-dns-01-challenge "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------------------------

Introduction[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#introduction "Permanent link")
---------------------------------------------------------------------------------------------------------------

### What is DNS-01 Challenge?[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#what-is-dns-01-challenge "Permanent link")

DNS-01 is an alternative ACME (Automated Certificate Management Environment) validation method that proves domain ownership through DNS TXT records instead of HTTP requests. When you request a certificate using DNS-01:

1.   The ACME server (Let's Encrypt) provides a unique token
2.   Your mailcow server automatically creates a DNS TXT record `_acme-challenge.yourdomain.com` with that token
3.   Let's Encrypt queries DNS to verify the record exists
4.   Once verified, your certificate is issued

mailcow uses [acme.sh](https://github.com/acmesh-official/acme.sh) to handle DNS-01 validation, supporting over 150 DNS providers through their APIs.

### When to Use DNS Challenge[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#when-to-use-dns-challenge "Permanent link")

Consider using DNS-01 challenge if you need:

*   **Wildcard certificates** (`*.example.com`) - HTTP-01 cannot issue wildcard certificates
*   **Firewalled servers** - Port 80 (HTTP) is blocked or not publicly accessible
*   **Complex reverse proxy setups** - HTTP validation would hit the wrong server
*   **Multiple servers sharing a domain** - HTTP challenge might reach a different server
*   **Reduced external exposure** - No need to expose port 80 to the internet

### When NOT to Use DNS Challenge[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#when-not-to-use-dns-challenge "Permanent link")

Stick with the default HTTP-01 challenge if:

*   You have a simple single-server setup with public HTTP access (easier to configure)
*   Your DNS provider doesn't offer API access or isn't supported by acme.sh
*   You cannot automate DNS API access due to organizational restrictions
*   You don't need wildcard certificates

Default Method

mailcow uses HTTP-01 challenge by default, which works great for most installations. Only switch to DNS-01 if you have a specific need for it.

* * *

Prerequisites[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#prerequisites "Permanent link")
-----------------------------------------------------------------------------------------------------------------

Before enabling DNS-01 challenge, ensure you have:

1.   **mailcow version 2026-03 or later**
2.   **A supported DNS provider** with API access (see [Supported DNS Providers](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#supported-dns-providers))
3.   **API credentials** from your DNS provider with permission to edit DNS records
4.   **Understanding of your DNS zone structure** (which domains/subdomains need certificates)

* * *

Configuration[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#configuration "Permanent link")
-----------------------------------------------------------------------------------------------------------------

### Step 1: Enable DNS Challenge in mailcow.conf[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#step-1-enable-dns-challenge-in-mailcowconf "Permanent link")

Edit `/opt/mailcow-dockerized/mailcow.conf` and add or modify these parameters:

```
# Enable DNS-01 challenge (instead of HTTP-01)
ACME_DNS_CHALLENGE=y

# Specify your DNS provider plugin (see provider list below)
# Example: dns_servercow for Servercow, dns_cf for CloudFlare, dns_aws for AWS Route53
ACME_DNS_PROVIDER=dns_servercow

# Email address for ACME account registration
ACME_ACCOUNT_EMAIL=admin@example.com
```

Important Settings

*   When `ACME_DNS_CHALLENGE=y`, mailcow will **ignore**`SKIP_HTTP_VERIFICATION` (it's implied)
*   Port 80 is **not required** for DNS challenge
*   All domains in your mailcow installation will use DNS-01 (you cannot mix HTTP-01 and DNS-01)

### Step 2: Configure DNS Provider Credentials[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#step-2-configure-dns-provider-credentials "Permanent link")

Create or edit `/opt/mailcow-dockerized/data/conf/acme/dns-01.conf`:

```
# Servercow example
SERVERCOW_API_Username="servercow-api-username"
SERVERCOW_API_Password="servercow-api-password"
```

### Step 3: Apply Configuration[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#step-3-apply-configuration "Permanent link")

Restart the acme-mailcow container to apply changes:

docker compose (Plugin) docker-compose (Standalone)

```
cd /opt/mailcow-dockerized
docker compose up -d
```

```
cd /opt/mailcow-dockerized
docker-compose up -d
```

### Step 4: Monitor Certificate Request[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#step-4-monitor-certificate-request "Permanent link")

Watch the logs to verify DNS challenge is working:

docker compose (Plugin) docker-compose (Standalone)

```
docker compose logs -f acme-mailcow
```

```
docker-compose logs -f acme-mailcow
```

* * *

Supported DNS Providers[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#supported-dns-providers "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------

mailcow uses acme.sh DNS API plugins. Over 150 providers are supported.

### Tier 1: Fully Tested & Recommended[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#tier-1-fully-tested-recommended "Permanent link")

| Provider | Plugin Name | Required Credentials | Documentation |
| --- | --- | --- | --- |
| **Servercow** | `dns_servercow` | `SERVERCOW_API_Username`, `SERVERCOW_API_Password` | [Servercow API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_servercow) |
| **CloudFlare** | `dns_cf` | `CF_Token`, `CF_Account_ID` | [CloudFlare DNS API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_cf) |
| **AWS Route53** | `dns_aws` | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | [Route53 API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_aws) |
| **Azure DNS** | `dns_azure` | `AZUREDNS_SUBSCRIPTIONID`, `AZUREDNS_TENANTID`, `AZUREDNS_APPID`, `AZUREDNS_CLIENTSECRET` | [Azure API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_azure) |
| **Google Cloud DNS** | `dns_gcloud` | `CLOUDSDK_ACTIVE_CONFIG_NAME` | [GCloud API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_gcloud) |
| **DigitalOcean** | `dns_dgon` | `DO_API_KEY` | [DigitalOcean API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#dns_dgon) |

| Provider | Plugin Name | Notes |
| --- | --- | --- |
| **Hetzner** | `dns_hetzner` | Popular in Germany/Europe |
| **OVH** | `dns_ovh` | European provider |
| **Namecheap** | `dns_namecheap` | Requires DDNS password, not standard API |
| **GoDaddy** | `dns_gd` | API key + API secret required |
| **Linode** | `dns_linode` | API token |
| **DNSimple** | `dns_dnsimple` | API token |

**Full Provider List:**[acme.sh DNS API Documentation](https://github.com/acmesh-official/acme.sh/wiki/dnsapi) (150+ providers)

Provider Not Listed?

If your provider supports DNS API and is listed in the acme.sh documentation, it should work with mailcow. Check the [acme.sh wiki](https://github.com/acmesh-official/acme.sh/wiki/dnsapi) for configuration details.

* * *

Wildcard Certificates[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#wildcard-certificates "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------

DNS-01 challenge is the **only way** to obtain wildcard certificates from Let's Encrypt.

### Configuration Example[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#configuration-example "Permanent link")

Edit `mailcow.conf`:

```
MAILCOW_HOSTNAME=mail.example.com
ADDITIONAL_SAN=*.example.com,example.com
ACME_DNS_CHALLENGE=y
ACME_DNS_PROVIDER=dns_servercow
```

Wildcard Limitations

*   `*.example.com` covers `mail.example.com`, `webmail.example.com`, `smtp.example.com`, etc.
*   `*.example.com` does **NOT** cover `example.com` (the apex/root domain)
*   You must explicitly add both: `ADDITIONAL_SAN=*.example.com,example.com`

* * *

Configuration Examples[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#configuration-examples "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

### Example 1: Servercow with Wildcard[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#example-1-servercow-with-wildcard "Permanent link")

**Scenario:** mailcow hosted at Servercow, single domain with wildcard certificate

**mailcow.conf:**

```
MAILCOW_HOSTNAME=mail.example.com
ADDITIONAL_SAN=*.example.com,example.com

# DNS-01 Challenge Configuration
ACME_DNS_CHALLENGE=y
ACME_DNS_PROVIDER=dns_servercow
ACME_ACCOUNT_EMAIL=admin@example.com
```

**data/conf/acme/dns-01.conf:**

```
# Servercow API Credentials
# Get from: https://cp.servercow.de
# API > API Users > Create new user or use existing
SERVERCOW_API_Username="your-servercow-api-username"
SERVERCOW_API_Password="your-servercow-api-password"
```

**Create Servercow API User:**

1.   Log into [Servercow Control Panel](https://cp.servercow.de/)
2.   Navigate to **API**>**API Users**
3.   Click **Create API User** or use existing API user
4.   Note the username and password
5.   Ensure the API user has DNS management permissions

* * *

### Example 2: CloudFlare with Wildcard[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#example-2-cloudflare-with-wildcard "Permanent link")

**Scenario:** Small business, single domain, want wildcard certificate for all subdomains

**mailcow.conf:**

```
MAILCOW_HOSTNAME=mail.example.com
ADDITIONAL_SAN=*.example.com,example.com

# DNS-01 Challenge Configuration
ACME_DNS_CHALLENGE=y
ACME_DNS_PROVIDER=dns_cf
ACME_ACCOUNT_EMAIL=admin@example.com
```

**data/conf/acme/dns-01.conf:**

```
# CloudFlare API Token (NOT Global API Key!)
# Create at: https://dash.cloudflare.com/profile/api-tokens
# Permissions: Zone > DNS > Edit for zone 'example.com'
CF_Token="your_cloudflare_api_token_here"
CF_Account_ID="your_cloudflare_account_id"
```

**Create CloudFlare API Token:**

1.   Go to [CloudFlare Dashboard](https://dash.cloudflare.com/profile/api-tokens)
2.   Click "Create Token"
3.   Use template "Edit zone DNS" or create custom token with:
4.   Permissions: `Zone > DNS > Edit`
5.   Zone Resources: `Include > Specific zone > example.com`
6.   Copy the token (shown only once!)

* * *

### Example 3: Hetzner (Germany)[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#example-3-hetzner-germany "Permanent link")

**Scenario:** German hosting provider, popular in Europe

**mailcow.conf:**

```
MAILCOW_HOSTNAME=mail.example.de
ADDITIONAL_SAN=*.example.de

ACME_DNS_CHALLENGE=y
ACME_DNS_PROVIDER=dns_hetzner
ACME_ACCOUNT_EMAIL=admin@example.de
```

**data/conf/acme/dns-01.conf:**

```
# Hetzner DNS API Token
# Create at: https://dns.hetzner.com/settings/api-token
HETZNER_Token="your-hetzner-api-token-here"
```

* * *

### Example 4: IONOS (Germany)[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#example-4-ionos-germany "Permanent link")

**Scenario:** IONOS (formerly 1&1), German provider

**mailcow.conf:**

```
MAILCOW_HOSTNAME=mail.example.de
ADDITIONAL_SAN=*.example.de

ACME_DNS_CHALLENGE=y
ACME_DNS_PROVIDER=dns_ionos
ACME_ACCOUNT_EMAIL=admin@example.de
```

**data/conf/acme/dns-01.conf:**

```
# IONOS API Key
# Get from: IONOS customer area under Developer Tools
IONOS_API_KEY="your-ionos-api-key"
```

* * *

### Example 5: AWS Route53 (Multi-Domain)[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#example-5-aws-route53-multi-domain "Permanent link")

**Scenario:** Multiple domains hosted on AWS, corporate setup

**mailcow.conf:**

```
MAILCOW_HOSTNAME=mail.company.com
ADDITIONAL_SAN=smtp.company.com,mail.division.org

ACME_DNS_CHALLENGE=y
ACME_DNS_PROVIDER=dns_aws
ACME_ACCOUNT_EMAIL=admin@company.com
```

**data/conf/acme/dns-01.conf:**

```
# AWS IAM User Credentials
# IAM User: mailcow-acme-dns
# Policy: Attached custom policy (see below)
AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
```

**Recommended IAM Policy (least privilege):**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "route53:GetChange",
        "route53:ListHostedZones"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "route53:ChangeResourceRecordSets"
      ],
      "Resource": "arn:aws:route53:::hostedzone/Z1234567890ABC"
    }
  ]
}
```

Replace `Z1234567890ABC` with your actual hosted zone ID.

* * *

Additional Resources[¶](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/#additional-resources "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------

*   [acme.sh DNS API Documentation](https://github.com/acmesh-official/acme.sh/wiki/dnsapi) - Full list of 150+ supported DNS providers with configuration examples
*   [Let's Encrypt Challenge Types](https://letsencrypt.org/docs/challenge-types/) - Official documentation explaining HTTP-01 vs DNS-01
*   [Let's Encrypt Rate Limits](https://letsencrypt.org/docs/rate-limits/) - Certificate issuance limits
*   [mailcow SSL Documentation (HTTP-01)](https://docs.mailcow.email/post_installation/firststeps-ssl/) - Standard HTTP-based certificate issuance
*   [mailcow Reverse Proxy Setup](https://docs.mailcow.email/post_installation/reverse-proxy/r_p/) - Using mailcow behind reverse proxies
*   [mailcow DNS Prerequisites](https://docs.mailcow.email/getstarted/prerequisite-dns/) - DNS records required for mail operation
