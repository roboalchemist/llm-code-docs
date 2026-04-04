# Source: https://resend.com/docs/knowledge-base/hostinger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hostinger

> Verify your domain on Hostinger with Resend.

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

## Log in to Hostinger

Log in to your [Hostinger account](https://auth.hostinger.com/login):

1. Select the `Domains` tab
2. Choose your Domain from the `Domain portfolio` list.
3. Select the `DNS / Nameservers` to get to the page to manage DNS records.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-domains.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d7fcfa6f62bc4c8eb8c7eccbc12068c3" data-og-width="2983" width="2983" data-og-height="1848" height="1848" data-path="images/dashboard-domains-hostinger-domains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-domains.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=42922b010762c4f3b6bc7fa9c6b887b1 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-domains.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=3799d276f1994502b533f97da7c98f42 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-domains.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d284dccbb31a44a441e52d845383bbd4 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-domains.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=53581e974864b508da5c127c84f495c6 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-domains.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6d699394a23afc4181dda401fcbd2544 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-domains.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9774143e76ba327c0352da3fc033a196 2500w" />

## Add MX SPF Record

Copy and paste the values MX in Resend to Hostinger.

1. Set the Type to `MX`.
2. Type `send` for the `Name` of the record.
3. Copy the MX Value from Resend into the `Mail Server` field.
4. Add `10` for the `Priority`.
5. Set the TTL to `3600`.
6. Select `Add Record`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d9600d2ba927c8ee8a3222139280d396" data-og-width="2984" width="2984" data-og-height="1849" height="1849" data-path="images/dashboard-domains-hostinger-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9c6fbafa2370231a9fe754c413f9d034 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a58ed744a5aaf6b702373396c2c4ebb1 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=1ff25d2c3794b514903f748d58b589fa 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8041cbc7155fb88ea3a7ff64d37e75d6 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a947eada3bfcd86bb0774dab7ac5563d 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=b1c65f01a55b3424558c61eaac2c1f7d 2500w" />

Below is a mapping of the record fields from Resend to Hostinger:

| Hostinger   | Resend   | Example Value                           |
| ----------- | -------- | --------------------------------------- |
| Type        | Type     | `MX Record`                             |
| Name        | Name     | `send`                                  |
| Mail Server | Value    | `feedback-smtp.us-east-1.amazonses.com` |
| TTL         | -        | `Set to 3660`                           |
| Priority    | Priority | `10`                                    |

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use on another record, try a higher value `20` or `30`.
</Info>

## Add TXT SPF Record

In the same section, add another record in Hostinger.

1. Set the Type to `TXT`.
2. Type `send` for the `Name` of the record.
3. Copy the TXT Value Resend into the `TXT value` field.
4. Set the TTL to `3600`.
5. Select `Add Record`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8854129a0f11574f79016d5ad56a0ed2" data-og-width="2985" width="2985" data-og-height="1848" height="1848" data-path="images/dashboard-domains-hostinger-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cb9b47019b7c4b65239afdf02773ed77 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=71ef6eb98429bc7c183c530426c4792e 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f152e06618c8f27b259b76898b6bc027 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=b2d186d8d5b2d846ace569bb264b85b7 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=3e202d12e04d96cf0143548a39cd2fb5 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4b9a15c02924b6e7144323ae8ebf5ac1 2500w" />

Below is a mapping of the record fields from Resend to Hostinger:

| Hostinger | Resend | Example Value                         |
| --------- | ------ | ------------------------------------- |
| Type      | Type   | `TXT Record`                          |
| Name      | Name   | `send`                                |
| TXT value | Value  | `"v=spf1 include:amazonses.com ~all"` |
| TTL       | -      | `Set to 3600`                         |

## Add TXT DKIM Records

In the same section, add another record in Hostinger.

1. Set the Type to `TXT`.
2. Type `resend._domainkey` for the `Name` of the record.
3. Copy the record value from Resend into the `TXT value` field.
4. Set the TTL to `3600`.
5. Select `Add Record`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-dkim-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=31350bb523d1959c348a0fde5f8d5734" data-og-width="2984" width="2984" data-og-height="1848" height="1848" data-path="images/dashboard-domains-hostinger-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-dkim-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4dad2da32e35e7a727077447aa9838ca 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-dkim-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9a67618054c354f65519db52f96dfaf6 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-dkim-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2facef63a7248ff778690971032eabcd 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-dkim-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a289d55386ed613ef210b3a48c9fca88 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-dkim-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=426dda85472f75bd4985fa6c038d4da0 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-hostinger-dkim-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=548c0537b3491028d6f40a330c622022 2500w" />

Below is a mapping of the record fields from Resend to Hostinger:

| Hostinger | Resend | Example Value                |
| --------- | ------ | ---------------------------- |
| Type      | Type   | `TXT Record`                 |
| Name      | Name   | `send`                       |
| TXT value | Value  | `p=example_demain_key_value` |
| TTL       | -      | `Set to 3600`                |

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

Copy and paste the values MX in Resend to Hostinger:

1. Set the Type to `MX`.
2. Type `inbound` (or whatever your subdomain is) for the `Name` of the record.
3. Copy the MX Value from Resend into the `Mail Server` field.
4. Add `10` for the `Priority`.
5. Set the TTL to `3600`.
6. Select `Add Record`.

Below is a mapping of the record fields from Resend to Hostinger:

| Hostinger   | Resend   | Example Value                          |
| ----------- | -------- | -------------------------------------- |
| Type        | Type     | `MX Record`                            |
| Name        | Name     | `inbound`                              |
| Mail Server | Content  | `inbound-smtp.us-east-1.amazonaws.com` |
| TTL         | -        | `Set to 3660`                          |
| Priority    | Priority | `10`                                   |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take a few hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Hostinger to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
