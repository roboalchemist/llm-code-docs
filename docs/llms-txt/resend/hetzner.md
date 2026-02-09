# Source: https://resend.com/docs/knowledge-base/hetzner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hetzner

> Verify your domain on Hetzner with Resend.

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

## Log in to Hetzner

Log in to your [Hetzner account](https://dns.hetzner.com):

1. Choose your Domain from the `Your Zones` list.
2. Select the `Records` tab to get to the page to manage DNS records.

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-domains.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=145c6cbd9d047e33dd8daad7b07bff8c" data-og-width="2984" width="2984" data-og-height="1849" height="1849" data-path="images/dashboard-domains-Hetzner-domains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-domains.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=b1dd6db0f84de9b493ea15d3313ff5da 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-domains.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=acbe872539f23beca55a52c75c769f96 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-domains.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=039ce781e54822500280c96d2cb6a015 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-domains.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c3f93dd1a358b4b0246245da7645f067 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-domains.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=fa81adb44768c414cc8705f5a96c6703 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-domains.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ec8850a903520deb211fdaa0dd0849a2 2500w" />

## Add MX SPF Record

In the `Create Record` section on Hetzner copy and paste the values MX from Resend:

1. On the `Type` page, choose `MX`.
2. Type `send` for the `Name` of the record.
3. Select the `Value` field.
4. Use the default `Priority` of `10`.
5. Copy the MX Value from Resend into the `Mail server` field.
6. Select the TTL of `1800`.
7. Select `Add Record`.

<Info>
  Hetzner requires your MX record to have a trailing period when adding. Resend
  will include the trailing period when copying. Removing the period will cause
  the verification to fail.
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-mx.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=db6f4da36c4e408a86c54ca3e42d6ea9" data-og-width="2984" width="2984" data-og-height="1848" height="1848" data-path="images/dashboard-domains-Hetzner-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-mx.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=9f3500e1b465041d87616d751a8714f6 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-mx.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=22bd1875ea3344e07ac1390278d1c52c 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-mx.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ec7fca39828a3be91b0d988ec6e56997 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-mx.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=069767874b22888a024c4c7ddcc57157 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-mx.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=964c5a3df8c67efcc710de95f40d8865 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-mx.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=86816bbb998b9a46ecef897f90964786 2500w" />

Below is a mapping of the record fields from Resend to Hetzner:

| Hetzner     | Resend   | Example Value                            |
| ----------- | -------- | ---------------------------------------- |
| Type        | Type     | `MX Record`                              |
| Name        | Name     | `send`                                   |
| Mail server | Value    | `feedback-smtp.us-east-1.amazonses.com.` |
| TTL         | TTL      | `1800`                                   |
| Priority    | Priority | `10`                                     |

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use on another record, try a higher value `20` or `30`.
</Info>

## Add TXT SPF Record

On the same `Create Record` section:

1. On the `Type` page, choose `TXT`.
2. Type `send` for the `Name` of the record.
3. Copy the TXT Value Resend into the `Value` field.
4. Select the TTL of `1800`.
5. Select `Add Record`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-txt.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=89bce49d989f8a9006f8cf465202a2ca" data-og-width="2986" width="2986" data-og-height="1848" height="1848" data-path="images/dashboard-domains-Hetzner-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-txt.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=9b8cbf76a4d4da7245897625da6adcc3 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-txt.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=8a4de9180615452171eae02c36151174 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-txt.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=a20a13bdd450688f5c92ebef1b1ae4b3 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-txt.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=1eae44919f1c2e1389583c6564f4fee9 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-txt.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=d21e0b2da4ddcfb7e79ffd198cd359d1 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-spf-txt.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=32e3d8fedcd1c6972a3d277b3f224029 2500w" />

Below is a mapping of the record fields from Resend to Hetzner:

| Hetzner | Resend | Example Value                         |
| ------- | ------ | ------------------------------------- |
| Type    | Type   | `TXT Record`                          |
| Name    | Name   | `send`                                |
| Value   | Value  | `"v=spf1 include:amazonses.com ~all"` |
| TTL     | TTL    | `10800`                               |

## Add TXT DKIM Records

On the same `Create Record` section:

1. On the `Type` page, choose `TXT`.
2. Type `resend._domainkey` for the `Name` of the record.
3. Copy the TXT Value Resend into the `Value` field.
4. Select the TTL of `1800`.
5. Select `Add Record`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-dkim-txt.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=3a29ae90720d7d9c31cc7cfa5892cd57" data-og-width="2984" width="2984" data-og-height="1848" height="1848" data-path="images/dashboard-domains-Hetzner-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-dkim-txt.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c79be8ade8a523b225f6ed7953a5ecb1 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-dkim-txt.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=b4847bddef413b0f57d0b55ac348e5e7 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-dkim-txt.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=d10467a8782ffab990e77efbcf0f6317 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-dkim-txt.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=251b7397e65b888dc26b5fd721384634 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-dkim-txt.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=19f8f907d69dcc7665816cfc6fa27cdc 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-Hetzner-dkim-txt.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e958c09b975347b558b3c570485a08b7 2500w" />

Below is a mapping of the record fields from Resend to Hetzner:

| Hetzner | Resend | Example Value                |
| ------- | ------ | ---------------------------- |
| Type    | Type   | `TXT Record`                 |
| Name    | Name   | `send`                       |
| Value   | Value  | `p=example_demain_key_value` |
| TTL     | TTL    | `1 hour`                     |

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

In the `Create Record` section on Hetzner:

1. On the `Type` page, choose `MX`.
2. Type `inbound` (or whatever your subdomain is) for the `Name` of the record.
3. Select the `Value` field.
4. Use the default `Priority` of `10`.
5. Copy the MX Value from Resend into the `Mail server` field.
6. Select the TTL of `1800`.
7. Select `Add Record`.

Below is a mapping of the record fields from Resend to Hetzner:

| Hetzner     | Resend   | Example Value                           |
| ----------- | -------- | --------------------------------------- |
| Type        | Type     | `MX Record`                             |
| Name        | Name     | `inbound`                               |
| Mail server | Content  | `inbound-smtp.us-east-1.amazonaws.com.` |
| TTL         | TTL      | `1800`                                  |
| Priority    | Priority | `10`                                    |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take a few hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Hetzner to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
