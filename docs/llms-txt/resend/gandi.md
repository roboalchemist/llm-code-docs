# Source: https://resend.com/docs/knowledge-base/gandi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gandi

> Verify your domain on Gandi with Resend.

## Add Domain to Resend

First, log in to your [Resend Account](https://resend.com/login) and [add a domain](https://resend.com/domains).

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=418dd93c2f2ead0b0d83d1b7c2fb0970" data-og-width="3360" width="3360" data-og-height="2100" height="2100" data-path="images/dashboard-domains-resend-add-domain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=28a4feab47f2b86c34c7b1314f636f0c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bf121272193472fdd2c882fe4b29ced5 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=950e2318cb41511a6f7105afa50be42c 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=e5a7d9a4d237a3435e8fffb85c3650f1 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a4944168fa1595f1843c8789944f1ef3 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=17d0c63a766375cab10239e4025c8dac 2500w" />

<Tip>
  It is [best practice to use a
  subdomain](/knowledge-base/is-it-better-to-send-emails-from-a-subdomain-or-the-root-domain)
  (updates.example.com) instead of the root domain (example.com). Using a
  subdomain allows for proper reputation segmentation based on topics or purpose
  (e.g. marketing) and is especially important if receiving emails with Resend.
</Tip>

## Log in to Gandi

Log in to your [Gandi account](https://admin.gandi.net/domain/):

1. Choose your Domain from the `Domain` list.
2. Select the `DNS Records` tab to get to the page to manage DNS records.

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-domains.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=db72a28a42a006e10ca7617fc004ecb5" data-og-width="2963" width="2963" data-og-height="1847" height="1847" data-path="images/dashboard-domains-gandi-domains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-domains.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5b3d9b61e75f492a4e7efaef9b0434e1 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-domains.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=36804c011c62524b2457684ab70c7cce 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-domains.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=2dd05c09769b5b445fdaf34858447bb4 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-domains.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e4594f593fd3d2a2fda5d3779e9e0893 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-domains.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=4446530f8d14efc2baee977d500c15bd 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-domains.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c85dd37060ad5e0b866b3fc0112eb33d 2500w" />

## Add MX SPF Record

Select “Add record” on Gandi to copy and paste the values MX from Resend.

1. On the `Type` page, choose `MX`.
2. Use the default TTL of `10800`.
3. Type `send` for the `Name` of the record.
4. Use the default `Priority` of `10`.
5. Copy the MX Value from Resend into the `Hostname` field.
6. Select `Create`.

<Info>
  Gandi requires your MX record to have a trailing period when adding. Resend
  will include the trailing period when copying. Removing the period will cause
  the verification to fail.
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=41f5e1b53f159b7e8e05f4f1ffa7e5ad" data-og-width="2974" width="2974" data-og-height="1848" height="1848" data-path="images/dashboard-domains-gandi-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d9c6960f54e409d123ba9749da37ef89 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=35ca3c16ea77f7f6d589f64177d70eac 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=55f2f83b5a295894728995679b335cd8 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=af8022feef80a1fd59b4cb122de72f11 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2d9329e44b1d8a38d8d6edbffb2c835e 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a826325cc030c4784ca06c8084e5ba0c 2500w" />

Below is a mapping of the record fields from Resend to Gandi:

| Gandi    | Resend   | Example Value                            |
| -------- | -------- | ---------------------------------------- |
| Type     | Type     | `MX Record`                              |
| Name     | Name     | `send`                                   |
| Hostname | Value    | `feedback-smtp.us-east-1.amazonses.com.` |
| TTL      | -        | `10800`                                  |
| Priority | Priority | `10`                                     |

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use on another record, try a higher value `20` or `30`.
</Info>

## Add TXT SPF Record

In the same section, select “Add record” again.

1. On the `Type` page, choose `TXT`.
2. Use the default TTL of `10800`.
3. Type `send` for the `Name` of the record.
4. Copy the TXT Value Resend into the `Text value` field.
5. Select `Create`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=7f75828142bfae8186b3f577d379c910" data-og-width="2954" width="2954" data-og-height="1849" height="1849" data-path="images/dashboard-domains-gandi-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=0cb08cea4b3c9f69c72221bc1cbc0f1f 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=dbfffb14e602fea0c917e8253de2a4b6 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8b09d4de42a2053a22a001f7bbc7e36b 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=67f63c26c3df5057b33ac104f4203adb 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=3f7667317d6a6ee26be20ee6e4bfdae9 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-gandi-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb6cb830fca5df52a3f8e38ddca5f654 2500w" />

Below is a mapping of the record fields from Resend to Gandi:

| Gandi      | Resend | Example Value                         |
| ---------- | ------ | ------------------------------------- |
| Type       | Type   | `TXT Record`                          |
| Name       | Name   | `send`                                |
| Text value | Value  | `"v=spf1 include:amazonses.com ~all"` |
| TTL        | -      | `10800`                               |

## Add TXT DKIM Records

In the same section, select “Add record” again.

1. On the `Type` page, choose `TXT`.
2. Use the default TTL of `10800`.
3. Type `resend._domainkey` for the `Host name` of the record.
4. Copy the record value from Resend into the `TXT value` field.
5. Select `Create`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-dkim-txt.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=097889c1a13da8b1634cddadfe294887" data-og-width="2954" width="2954" data-og-height="1848" height="1848" data-path="images/dashboard-domains-gandi-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-dkim-txt.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=2225a7f06e29f58b58235426d04e9a5e 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-dkim-txt.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=9ca149853b529c8acc1cfbc09739ac8c 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-dkim-txt.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=110efce24a291ffd187509f1971a4265 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-dkim-txt.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=8b2c5af25d6a3bb42b14be71557168d8 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-dkim-txt.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ef650933721d359c3bdabcc5c4267593 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-gandi-dkim-txt.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=a624fae4abbf96f4d0773df3d9d9814d 2500w" />

Below is a mapping of the record fields from Resend to Gandi:

| Gandi      | Resend | Example Value                |
| ---------- | ------ | ---------------------------- |
| Type       | Type   | `TXT Record`                 |
| Name       | Name   | `send`                       |
| Text value | Value  | `p=example_demain_key_value` |
| TTL        | -      | `1 hour`                     |

## Receiving Emails

If you want to receive emails at your domain, toggle the "Receiving" switch on the domain details page.

<img alt="Enable Receiving Emails for a verified domain" src="https://mintcdn.com/resend/B7wTVm7aKL5pNT-6/images/inbound-domain-toggle.png?fit=max&auto=format&n=B7wTVm7aKL5pNT-6&q=85&s=46f6b4c142fb90e04b57861e338ed2d0" data-og-width="1980" width="1980" data-og-height="1244" height="1244" data-path="images/inbound-domain-toggle.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/B7wTVm7aKL5pNT-6/images/inbound-domain-toggle.png?w=280&fit=max&auto=format&n=B7wTVm7aKL5pNT-6&q=85&s=9ffcfe01f091c84e949e307e8524c98e 280w, https://mintcdn.com/resend/B7wTVm7aKL5pNT-6/images/inbound-domain-toggle.png?w=560&fit=max&auto=format&n=B7wTVm7aKL5pNT-6&q=85&s=040a52053e2b2e66924ee2d82a7f60b6 560w, https://mintcdn.com/resend/B7wTVm7aKL5pNT-6/images/inbound-domain-toggle.png?w=840&fit=max&auto=format&n=B7wTVm7aKL5pNT-6&q=85&s=0477716dc557a951ada6d6ccfe452feb 840w, https://mintcdn.com/resend/B7wTVm7aKL5pNT-6/images/inbound-domain-toggle.png?w=1100&fit=max&auto=format&n=B7wTVm7aKL5pNT-6&q=85&s=8a4c306e667be6092577793c18da1483 1100w, https://mintcdn.com/resend/B7wTVm7aKL5pNT-6/images/inbound-domain-toggle.png?w=1650&fit=max&auto=format&n=B7wTVm7aKL5pNT-6&q=85&s=33481622e755b8f0b54c3066b8e1a724 1650w, https://mintcdn.com/resend/B7wTVm7aKL5pNT-6/images/inbound-domain-toggle.png?w=2500&fit=max&auto=format&n=B7wTVm7aKL5pNT-6&q=85&s=590982f9cd50e9e277f1b82928d25fdb 2500w" />

<Warning>
  When you enable Inbound on a domain, Resend receives *all emails* sent to that
  specific domain depending on the priority of the MX record. For this reason,
  we strongly recommend verifying a subdomain (`subdomain.example.com`) instead
  of the root domain (`example.com`). Learn more about [avoiding conflicts with
  your existing MX
  records](/knowledge-base/how-do-i-avoid-conflicting-with-my-mx-records).
</Warning>

Select “Add record” on Gandi:

1. On the `Type` page, choose `MX`.
2. Use the default TTL of `10800`.
3. Type `inbound` (or whatever your subdomain is) for the `Name` of the record.
4. Use the default `Priority` of `10`.
5. Copy the MX Value from Resend into the `Hostname` field.
6. Select `Create`.

Below is a mapping of the record fields from Resend to Gandi:

| Gandi    | Resend   | Example Value                           |
| -------- | -------- | --------------------------------------- |
| Type     | Type     | `MX Record`                             |
| Name     | Name     | `inbound`                               |
| Hostname | Content  | `inbound-smtp.us-east-1.amazonaws.com.` |
| TTL      | -        | `10800`                                 |
| Priority | Priority | `10`                                    |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take a few hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Gandi to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
