# Source: https://resend.com/docs/knowledge-base/cloudflare.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloudflare

> Verify your domain on Cloudflare with Resend.

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

## Automatic Setup (Recommended)

The fastest way to verify your domain on Cloudflare is using the **Sign in to Cloudflare** button on Resend. This uses Domain Connect to automatically configure your DNS records.

1. Go to your [Domains page](https://resend.com/domains) in Resend.
2. (Optional) If you want to receive emails, select `Manual setup` and toggle the "Receiving" switch on the domain details page. ([Learn more below](#receiving-emails))
3. Click **Sign in to Cloudflare** button.
4. Authorize Resend to access your Cloudflare DNS settings.
5. The DNS records will be added automatically.

<video autoPlay loop src="https://cdn.resend.com/posts/cloudflare-domain-connect-guide.mp4" aria-label="Cloudflare Domain Connect Setup" />

That's it. Your domain will be verified within a few minutes.

## Manual Setup

If you prefer to add DNS records manually, follow these steps.

### Log in to Cloudflare

Log in to your [Cloudflare account](https://cloudflare.com) and go to the DNS Records of your domain.

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-main.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ffd61997133f0af6f4ba8d14df82dcdc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-cloudflare-main.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-main.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=affd5781bb82c0dcef75131a8b765cf2 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-main.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=4cf4848114666458a854d83b21222d0a 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-main.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=0861617efcdd0a5952ef775c20d13dd7 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-main.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=f146598d076eb6032d4bcb7563fc61a8 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-main.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=fb782bc227891b7c0389f47c83a2914e 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-main.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=f9369a51dca91695ab42523500163c69 2500w" />

### Add MX SPF Record

Click "Add Record" on Cloudflare:

1. Set the Type to `MX`.
2. Type `send` for the `Name` of the record.
3. Copy the MX Value from Resend into the `Mail Server` field.
4. Use the default `Auto` for `TTL`.
5. Add `10` for the `Priority`.
6. Select `Save`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<br />

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-mx.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=372024c515c4b6924e5a1314ad831b6f" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-cloudflare-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-mx.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=1416fbcccc6fd9f2185d85a9a8d7ef04 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-mx.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=6173e8d149b3aa86e65891b960e4fe21 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-mx.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ad3c6e2f38266674ce7469665734bb93 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-mx.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=f0c3403290df643ea1f9878c4172826c 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-mx.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=b7a7ef34344fd16322a43c7b63d41620 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-mx.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5ec4fafda8fa91b9be2f2c90f8372d1a 2500w" />

Below is a mapping of the record fields from Resend to Cloudflare:

| Cloudflare  | Resend   | Example Value                           |
| ----------- | -------- | --------------------------------------- |
| Type        | Type     | `MX`                                    |
| Name        | Name     | `send`                                  |
| Mail Server | Value    | `feedback-smtp.us-east-1.amazonses.com` |
| Priority    | Priority | `10`                                    |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use, try a higher value `20` or `30`.
</Info>

### Add TXT SPF Record

Click "Add Record" on Cloudflare:

1. Set the Type to `TXT`.
2. Type `send` for the `Name` of the record.
3. Copy the TXT Value Resend into `Content` field.
4. Use the default `Auto` for `TTL`.
5. Select `Save`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<br />

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-txt.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=3a20409e0c792c602f4eb636dcfbc3ac" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-cloudflare-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-txt.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=4659299904959af3e372c7921bf268bb 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-txt.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=cf10b3dcc0f51677bb488debb69e9ff6 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-txt.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5638e631689875e90a37279279992ab7 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-txt.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c903bd8dbaf56c7212e77894db96f1c1 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-txt.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=3f86c3423a87944cccbcb0a7782d6256 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-spf-txt.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=453cb0fef075adb84fc1e4d66d9bab5d 2500w" />

Below is a mapping of the record fields from Resend to Cloudflare:

| Cloudflare | Resend  | Example Value                         |
| ---------- | ------- | ------------------------------------- |
| Type       | Type    | `TXT`                                 |
| Name       | Name    | `send`                                |
| Content    | Content | `"v=spf1 include:amazonses.com ~all"` |
| TTL        | -       | `Auto`                                |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

### Add TXT DKIM Records

Click "Add Record" on Cloudflare:

1. Set the Type to `TXT`.
2. Type `resend._domainkey` for the `Name` of the record.
3. Copy the TXT Value Resend into `Content` field.
4. Use the default `Auto` for `TTL`.
5. Select `Save`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<br />

<img alt="Domain Details" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-dkim-txt.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=dafb2d6d5050da130371a2b7a8390abd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-cloudflare-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-dkim-txt.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ab8407167de633f0001600e6e91551f2 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-dkim-txt.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=8dd410afef4ef516a78b439ee066b096 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-dkim-txt.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=1a4d4d31008c2d0f540a21058e010b2a 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-dkim-txt.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=6a9b5752b9a41aa10a7ab96388d0389e 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-dkim-txt.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=7901593487e28a81b33fc9114b627aff 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/dashboard-domains-cloudflare-dkim-txt.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5cfa304334a91bd6f42270e16b7b6076 2500w" />

Below is a mapping of the record fields from Resend to Cloudflare:

| Cloudflare   | Resend | Example Value                |
| ------------ | ------ | ---------------------------- |
| Type         | Type   | `TXT`                        |
| Name         | Name   | `resend._domainkey`          |
| Target       | Value  | `p=example_demain_key_value` |
| Proxy Status | -      | `DNS Only (disabled)`        |
| TTL          | -      | `Auto`                       |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

### Receiving Emails

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

Click “Add Record” on Cloudflare:

1. Set the Type to `MX`.
2. Type `inbound` (or whatever your subdomain is) for the `Name` of the record.
3. Copy the MX Value from Resend into the `Mail Server` field.
4. Use the default `Auto` for `TTL`.
5. Add `10` for the `Priority`.
6. Select `Save`.

Below is a mapping of the record fields from Resend to Cloudflare:

| Cloudflare  | Resend   | Example Value                          |
| ----------- | -------- | -------------------------------------- |
| Type        | Type     | `MX`                                   |
| Name        | Name     | `inbound`                              |
| Mail Server | Content  | `inbound-smtp.us-east-1.amazonaws.com` |
| Priority    | Priority | `10`                                   |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

### Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take up to 72 hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Cloudflare returns 'Code: 1004' when adding CNAME Records.">
    Confirm your proxy settings are set to `DNS Only` on the record you are adding.
  </Accordion>

  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Cloudflare to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
