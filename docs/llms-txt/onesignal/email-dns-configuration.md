# Source: https://documentation.onesignal.com/docs/en/email-dns-configuration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email DNS configuration

> Step-by-step guide to set up your sending domain and authenticate email using DNS records via OneSignal and Cloudflare.

This guide walks you through setting up DNS records provided by OneSignal to authenticate your sending domain. In most cases, DNS can be auto-configured from the OneSignal dashboard as described in the [Email Setup](./email-setup) guide.

## Requirements

If you need to manually set up your sending domain DNS recordss, you must:

* Own the sending domain.
* Have access to DNS settings via your provider.

If you don’t own a domain, we recommend purchasing one via Cloudflare. This guide will use Cloudflare as an example but most DNS providers work the same.

<Accordion title="Registering your domain with Cloudflare" icon="circle-chevron-down">
  Create an account at [Cloudflare.com](https://www.cloudflare.com/).

  Go to **Domain Registration > Register Domains**.

  <Frame caption="Cloudflare's Domain Registration Page">
    <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/738ee09-Register_a_Domain.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=327f5030dcc96a69aacf608556573bad" width="1300" height="775" data-path="images/docs/738ee09-Register_a_Domain.png" />
  </Frame>

  Search for an available name and purchase it.

  <Frame caption="Cloudflare's Domain Purchase Page">
    <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/914f661-Purchase_Domain.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=b81467e17066a8937256778554c2d014" width="1386" height="542" data-path="images/docs/914f661-Purchase_Domain.png" />
  </Frame>

  Once purchased, your domain will appear under **Domain Registration > Managed Domains**.

  <Frame caption="Cloudflare's Domain Management Page">
    <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/64857b3-Domain_Active.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=a3354c52a0f2442467d289d9e8071872" width="1303" height="817" data-path="images/docs/64857b3-Domain_Active.png" />
  </Frame>
</Accordion>

## Email DNS configuration

Complete the [Email Setup](./email-setup) steps until you're prompted to add DNS records, then return here or use the **Auto-Configure DNS** button.

From the OneSignal dashboard:

* ⚠️ means the current DNS record does not match
* ✅ means the current DNS record matches

Each DNS record needs to be added to your DNS provider with the exception of the MX record. You must have MX records set up, but they may point to a different server.

<Frame caption="Copy DNS records from OneSignal into your DNS provider">
  <img src="https://mintcdn.com/onesignal/2-gyvU4UfJHiycCa/images/dashboard/dns-manual-configure.png?fit=max&auto=format&n=2-gyvU4UfJHiycCa&q=85&s=f9d2428369c011d44bfe9a3c8ef3a003" width="1912" height="1056" data-path="images/dashboard/dns-manual-configure.png" />
</Frame>

In your DNS provider’s interface (e.g., Cloudflare), go to **DNS > Records** and add each record.

Correctly configuring DNS authentication helps ensure your emails are delivered and not flagged as spam. Here’s a breakdown of the DNS records you will add:

### TXT records

* **Type:** `TXT`
* **Name:** OneSignal "Hostname"
* **Content:** OneSignal "Value"
* **TTL:** Auto or lowest
* **Priority:** `10` (if required)

<Warning>
  If you already have an SPF TXT record, append additional `include:` records like:

  `v=spf1 include:spf.onesignal.email include:mailgun.org include:your-other-spf-records ~all`
</Warning>

<Frame caption="Cloudflare's TXT DNS record interface">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/476fea15213effba6c92f335f940246d1fc7d214233e5feee83b9f8a0f6390b2-Screenshot_2024-10-23_at_10.31.55_AM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=73f5e5388f8b6d5f3728aed32f03741a" width="2540" height="1062" data-path="images/docs/476fea15213effba6c92f335f940246d1fc7d214233e5feee83b9f8a0f6390b2-Screenshot_2024-10-23_at_10.31.55_AM.png" />
</Frame>

#### SPF (Sender Policy Framework)

Verifies the sending IP is authorized to send emails on your domain’s behalf.

#### DMARC

Adds policy enforcement for SPF/DKIM failures. **DMARC is required for secure email sending.** Learn more: [Email Sender Guidelines](https://support.google.com/mail/answer/81126)

<Warning>
  OneSignal uses the value `v=DMARC1; p=none;` for the DMARC record. If you already have a DMARC record, make sure this is included and not set multiple times.
</Warning>

### CNAME records

Used for open, click, and unsubscribe tracking.

* **Type:** `CNAME`
* **Name:** OneSignal "Hostname"
* **Target:** OneSignal "Value"
* **TTL:** Auto or lowest
* **Proxy:** DNS only
* **Flattening:** Off
* **Priority:** `10` (if required)

<Frame caption="Cloudflare's CNAME DNS record interface">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2e304d0eeb876a92bd325eeb490a7f8e5a7ba53d381bdc86009143146f7e6405-Screenshot_2024-10-23_at_10.36.52_AM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=c268cad031c5d52f44cd5fce1e81b105" width="2540" height="1062" data-path="images/docs/2e304d0eeb876a92bd325eeb490a7f8e5a7ba53d381bdc86009143146f7e6405-Screenshot_2024-10-23_at_10.36.52_AM.png" />
</Frame>

#### DKIM (DomainKeys Identified Mail)

Verifies the message’s content was not altered and was sent by you. The public key is included in the DNS record from OneSignal.

### MX records

Receives email responses or bounces. Even if you're only sending, these help avoid domain verification errors.

<Warning>
  If you already use another email provider (e.g. Gmail), do not overwrite existing MX records.
</Warning>

* **Type:** `MX`
* **Name:** OneSignal "Hostname"
* **Mail server:** OneSignal "Value"
* **TTL:** Auto or lowest
* **Priority:** `10`

<Frame caption="Cloudflare's MX DNS record interface">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f267f956723811f57b5a7d5db5190619a44c7641699a0bf5b3511f617597ada1-Screenshot_2024-10-23_at_10.50.19_AM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=538fb5cd52395b619b641eeb23f4a610" width="2540" height="884" data-path="images/docs/f267f956723811f57b5a7d5db5190619a44c7641699a0bf5b3511f617597ada1-Screenshot_2024-10-23_at_10.50.19_AM.png" />
</Frame>

***

## DNS verification & troubleshooting

After adding records:

1. Return to your OneSignal dashboard.
2. Click **Check Records** or refresh button.

Verified records show green check marks ✅.

All records should be verified (✅) in OneSignal with the exception of the MX records as long as your MX records are pointing somewhere else (like Google Mail).

<Frame caption="Verified DNS records in your OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/2-gyvU4UfJHiycCa/images/dashboard/dns-check-records.png?fit=max&auto=format&n=2-gyvU4UfJHiycCa&q=85&s=74380955130736264e42e26f2ae14a39" width="2250" height="1290" data-path="images/dashboard/dns-check-records.png" />
</Frame>

<Warning>
  Verification typically takes just a few minutes but can take up to 48 hours.
</Warning>

### Troubleshoot DNS propagation

1. Use [whatsmydns.net](https://www.whatsmydns.net/) to check propagation if any records are pending.
2. For records that show ⚠️, copy-paste the hostname from the OneSignal dashboard into the search bar and set the DNS type.
3. Check the results.

Green check marks ✅ mean the record is verified and red cross marks ❌ mean the record is not verified.
You can also see the current value of the record. If this is different from what OneSignal provides, you need to check your DNS provider's interface and update the record to match what is in OneSignal.

In this example, we see the TXT records are mostly green, with only a few that have not been updated yet.

<Frame caption="Check DNS propagation with whatsmydns.net">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a3011bc8b7477b7a1e18cb16cfd69bba03cc1f19cf623ccddd1926722bfc585c-Screenshot_2024-10-23_at_11.02.59_AM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=6b259000725c32c495332ec81842db00" width="2578" height="1492" data-path="images/docs/a3011bc8b7477b7a1e18cb16cfd69bba03cc1f19cf623ccddd1926722bfc585c-Screenshot_2024-10-23_at_11.02.59_AM.png" />
</Frame>

If verification fails:

* Confirm the domain is correct.
* Double-check each record was added exactly as shown in the dashboard.

#### Common errors & solutions

* **TXT SPF record isn't verified**
  * You likely have an SPF record already. You should only have 1 SPF record and add multiple `include:` records to it's value.
  * See above [TXT records](#txt-records) section for more details.
* **DNS not fully propagated**
  * When checking the DNS record in [whatsmydns.net](https://www.whatsmydns.net/) you may see many green check marks ✅ but also a lot of red cross marks ❌
  * This means the records are not fully propagated to the internet yet and may take up to 48 hours.
  * Either wait and check again or contact your DNS provider to help you troubleshoot.
* **DNS value not matching OneSignal**
  * If the values in [whatsmydns.net](https://www.whatsmydns.net/) do not match what we provide, then there are a couple things to check:
  * If MX records, that is ok. You can have the MX records point somewhere else as long as the are ✅ in [whatsmydns.net](https://www.whatsmydns.net/)
  * Check the URL is correct in [whatsmydns.net](https://www.whatsmydns.net/) and in your DNS provider. `mail.yourdomain.com` is not the same as `yourdomain.com`.
  * Contact your DNS provider to help you troubleshoot.

<Check>
  Return to [Email Setup](./email-setup) to complete configuration and begin sending emails.
</Check>

***

Built with [Mintlify](https://mintlify.com).
