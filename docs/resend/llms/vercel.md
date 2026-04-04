# Source: https://resend.com/docs/knowledge-base/vercel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel

> Verify your domain on Vercel with Resend.

<Note>
  This guide helps you verify your domain on Vercel with Resend. We also have
  [an official integration for
  Vercel](https://resend.com/blog/vercel-integration) that helps you set up your
  API keys on Vercel projects so you can start sending emails with Resend. [View
  the integration here](https://vercel.com/resend/~/integrations/resend).
</Note>

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

## Log in to Vercel

Log in to your [Vercel account](https://vercel.com/login) and select the `Domains` tab.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-domains.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4b4ab73110a36775175b39587eea68f0" data-og-width="1200" width="1200" data-og-height="676" height="676" data-path="images/dashboard-domains-vercel-domains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-domains.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=868b49719974b2a5a7cf1e4317f9d987 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-domains.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=eba99de72c3d9a9d9e3e37fc595055f4 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-domains.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=7ddd25da707cccce4df92145b2275ebc 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-domains.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=dd8cd592b4f1b4bad66917ae1f75ce9c 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-domains.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=95272ce43d4cc7a03710f307312137e3 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-domains.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=821b432b4b171a6fa1f562275dcaae07 2500w" />

## Add MX SPF Record

Copy and paste the values in Resend to Vercel.

1. Type `send` for the `Name` of the record in Vercel.
2. Expand the `Type` dropdown and select `MX`.
3. Copy the record value from Resend into the `Value` field in Vercel.
4. Add `10` for the `Priority`.
5. Select `Add`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9d91de47106d0bd4005bac0cfe68779e" data-og-width="1200" width="1200" data-og-height="676" height="676" data-path="images/dashboard-domains-vercel-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a15788a1c7a677819fa30090d833408f 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8e8d118f8a334dfcdd4fb33992eca135 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fc309c65c06824e96d52c897345095ba 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cf368fb5e6d3e0a692943cb5de5c5619 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=dc10e67a9d132c1e8529ca52182cca3f 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=e7189a5702cc345501239d5ea8c0ffcc 2500w" />

Below is a mapping of the record fields from Resend to Vercel:

| Vercel   | Resend   | Example Value                           |
| -------- | -------- | --------------------------------------- |
| Type     | Type     | `MX Record`                             |
| Name     | Name     | `send`                                  |
| Value    | Value    | `feedback-smtp.us-east-1.amazonses.com` |
| TTL      | TTL      | `Use Vercel default (60)`               |
| Priority | Priority | `10`                                    |

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use on another record, try a higher value `20` or `30`.
</Info>

## Add TXT SPF Record

In the same section, add another record in Vercel.

1. Type `send` for the `Name` of the record.
2. Expand the `Type` dropdown and select `TXT`.
3. Copy the `TXT` record value from Resend into the `Value` field in Vercel.
4. Use the default TTL of `60`.
5. Select `Add`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=27b350fc1a7745dd47c623fdaf9a2df4" data-og-width="1200" width="1200" data-og-height="676" height="676" data-path="images/dashboard-domains-vercel-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a991246f8e4adcaa35f5788868e9bdc6 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2af46aaacb4543bfe8cbe85b612d0e17 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=7508d7938fa2d77a16bd3b97db944b7c 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=1f19f53e80a9dc88ab3eb96b40d5a020 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cb8ab4b1eaa2ade06e6742aed45972da 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=03bedfa6fbfb1862fd2e2e58c2fa43d1 2500w" />

Below is a mapping of the record fields from Resend to Vercel:

| Vercel | Resend | Example Value                         |
| ------ | ------ | ------------------------------------- |
| Type   | Type   | `TXT Record`                          |
| Name   | Name   | `send`                                |
| Value  | Value  | `"v=spf1 include:amazonses.com ~all"` |
| TTL    | TTL    | `Use Vercel default (60)`             |

## Add TXT DKIM Records

In the same section, add another record in Vercel.

1. Type `resend._domainkey` for the `Name` of the record.
2. Expand the `Type` dropdown and select `TXT`.
3. Copy the record value from Resend into the `Value` field in Vercel.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-dkim-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8553d093e572970b0335c1fe9b83e003" data-og-width="1200" width="1200" data-og-height="676" height="676" data-path="images/dashboard-domains-vercel-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-dkim-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=18d7072f83f5c00bf9614c140ae32208 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-dkim-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9dc50e33021748be6f5c096b04168281 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-dkim-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9c36637c6ed2aa1b442f4538a32b3125 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-dkim-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=11fdf9662ffafb207e26fe564000598b 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-dkim-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8b4748250865923f5010bf5443fd6218 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-vercel-dkim-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e1844e679ea459fdb8a8e9325980165 2500w" />

Below is a mapping of the record fields from Resend to Vercel:

| Vercel | Resend | Example Value                |
| ------ | ------ | ---------------------------- |
| Type   | Type   | `TXT Record`                 |
| Name   | Name   | `resend._domainkey`          |
| Value  | Value  | `p=example_demain_key_value` |
| TTL    | TTL    | `Use Vercel default (60)`    |

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

Copy and paste the values in Resend to Vercel:

1. Type `inbound` (or whatever your subdomain is) for the `Name` of the record in Vercel.
2. Expand the `Type` dropdown and select `MX`.
3. Copy the MX Value from Resend into the `Value` field in Vercel.
4. Add `10` for the `Priority`.
5. Select `Add`.

Below is a mapping of the record fields from Resend to Vercel:

| Vercel   | Resend   | Example Value                          |
| -------- | -------- | -------------------------------------- |
| Type     | Type     | `MX Record`                            |
| Name     | Name     | `inbound`                              |
| Value    | Content  | `inbound-smtp.us-east-1.amazonaws.com` |
| TTL      | TTL      | `Use Vercel default (60)`              |
| Priority | Priority | `10`                                   |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take a few hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Vercel to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
