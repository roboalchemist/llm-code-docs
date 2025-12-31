# Source: https://resend.com/docs/knowledge-base/porkbun.md

# Porkbun

> Verify your domain on Porkbun with Resend.

## Add Domain to Resend

First, log in to your [Resend Account](https://resend.com/login) and [add a domain](https://resend.com/domains).

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=418dd93c2f2ead0b0d83d1b7c2fb0970" data-og-width="3360" width="3360" data-og-height="2100" height="2100" data-path="images/dashboard-domains-resend-add-domain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=28a4feab47f2b86c34c7b1314f636f0c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bf121272193472fdd2c882fe4b29ced5 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=950e2318cb41511a6f7105afa50be42c 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=e5a7d9a4d237a3435e8fffb85c3650f1 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a4944168fa1595f1843c8789944f1ef3 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-add-domain.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=17d0c63a766375cab10239e4025c8dac 2500w" />

<Tip>
  It is [best practice to use a
  subdomain](/knowledge-base/is-it-better-to-send-emails-from-a-subdomain-or-the-root-domain)
  (updates.example.com) instead of the root domain (example.com). This allows
  for proper reputation segmentation based on topics or purpose (e.g.
  transactional and marketing).
</Tip>

## Log in to Porkbun

Log in to your [Porkbun account](https://porkbun.com/account/domainsSpeedy):

1. Select the `DNS` option under your domain to manage DNS records.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-domains.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=44389c4ae53707e508d38a34a794cec3" data-og-width="2903" width="2903" data-og-height="1785" height="1785" data-path="images/dashboard-domains-porkbun-domains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-domains.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cc9c832c81685f06f20dbd7cddc98669 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-domains.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=ff19806fd165a02910ab3273472e929b 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-domains.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=60b377fcb40fd2c6329de35257ce33fa 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-domains.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=397075911c8f098744e83827c1635eb6 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-domains.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9c293b0c0eb90b18c88324382303dd67 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-domains.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=16b20ab3226b3cfffd49f80e669bd1a8 2500w" />

## Add MX SPF Record

In the `DNS` section on Porkbun copy and paste the values MX from Resend:

1. On the `Type` page, choose `MX`.
2. Type `send` for the `Host` of the record.
3. Copy the MX Value from Resend into the `Answer / Value` field.
4. Use the default TTL of `600`.
5. In the `Priority` field enter `10`.
6. Select `Add`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=65428888fca00600f2bdf31d14db8eaf" data-og-width="2897" width="2897" data-og-height="1767" height="1767" data-path="images/dashboard-domains-porkbun-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=455d3859b20fe99882c7e797368a7721 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=580144f74230de368512157f9fdc95ff 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=7471801ed082038ff0761015c1a2eb8d 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=da6279c2660e33551f131c3c0129e021 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d67a9117ccb90fc39974bdf69d9f9218 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=619d5c492cc7a788bc58c2f55db786fd 2500w" />

Below is a mapping of the record fields from Resend to Porkbun:

| Porkbun        | Resend   | Example Value                           |
| -------------- | -------- | --------------------------------------- |
| Type           | Type     | `MX Record`                             |
| Host           | Name     | `send`                                  |
| Answer / Value | Value    | `feedback-smtp.us-east-1.amazonses.com` |
| TTL            | -        | `600`                                   |
| Priority       | Priority | `10`                                    |

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use on another record, try a number slightly higher like `11` or `12`.
</Info>

## Add TXT SPF Record

On the same section:

1. On the `Type` page, choose `TXT`.
2. Type `send` for the `Host` of the record.
3. Copy the TXT Value Resend into the `Answer / Value` field.
4. Use the default TTL of `600`.
5. Select `Add Record`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=7ef4c8c51fd01d854c6404b96b2a1a27" data-og-width="2904" width="2904" data-og-height="1767" height="1767" data-path="images/dashboard-domains-porkbun-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=423790234c4fae56acd004d451eabd36 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=e706b958a400e2337c684f04521fbdb6 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=68d70f69fea553d8e8bb05ff32952cde 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=355db2ca034675d3a9d3717813b12548 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8e44103c79a4cf97e623d29d9f4d0cf7 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=3d709d0d408729cb05c4d1a4f62ee16e 2500w" />

Below is a mapping of the record fields from Resend to Porkbun:

| Porkbun        | Resend | Example Value                         |
| -------------- | ------ | ------------------------------------- |
| Type           | Type   | `TXT Record`                          |
| Host           | Name   | `send`                                |
| Answer / Value | Value  | `"v=spf1 include:amazonses.com ~all"` |
| TTL            | -      | `600`                                 |

## Add TXT DKIM Records

On the same `Create Record` section:

1. On the `Type` page, choose `TXT`.
2. Type `resend._domainkey` for the `Host` of the record.
3. Copy the TXT Value Resend into the `Answer / Value` field.
4. Use the default TTL of `600`.
5. Select `Add Record`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-dkim-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9f3a33882f02d34489d5adc55f28c7b8" data-og-width="2903" width="2903" data-og-height="1768" height="1768" data-path="images/dashboard-domains-porkbun-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-dkim-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=3948c85bf162952c3465b31d2b68188c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-dkim-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=11e0f58cbbdfa689a287578bc5a683a8 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-dkim-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f7414f834dea9dc3a07391a697cbed 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-dkim-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5b75bb5d73f6161b689fb57a03359f8f 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-dkim-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=3b3b0dcbf31194aa7f9571e1ad781fcc 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-porkbun-dkim-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=b458486c52924670d4c459e460ab2159 2500w" />

Below is a mapping of the record fields from Resend to Porkbun:

| Porkbun        | Resend | Example Value                |
| -------------- | ------ | ---------------------------- |
| Type           | Type   | `TXT Record`                 |
| Host           | Name   | `send`                       |
| Answer / Value | Value  | `p=example_demain_key_value` |
| TTL            | -      | `600`                        |

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take a few hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Porkbun to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
