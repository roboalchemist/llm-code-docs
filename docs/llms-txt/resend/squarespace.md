# Source: https://resend.com/docs/knowledge-base/squarespace.md

# Squarespace

> Verify your domain on Squarespace with Resend.

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

## Log in to Squarespace

Log in to your [Squarespace domains page](https://account.squarespace.com/domains) and click on your domain.

<img alt="Domain Details" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-domains-main.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=8362f1932f033cb983149883a9a459b6" data-og-width="3808" width="3808" data-og-height="2128" height="2128" data-path="images/squarespace-domains-main.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-domains-main.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=2cfa2630897112928ce232a48172fa3a 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-domains-main.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=641174111e56fc6637626fc803605cda 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-domains-main.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=f98c1e7d95c5738c78d7194f763ff2b8 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-domains-main.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=2ea6b44129e47e10b447d2adafdeffdb 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-domains-main.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=abba6bf36e054e1f1ef314caf904ae21 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-domains-main.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1e26b1739de84904edccd309a17fe8d5 2500w" />

## Add MX SPF Record

Scroll down to the **Custom records** section and select `Add record` on Squarespace.

1. Type `send` for the `Host` of the record.
2. Set the `Type` to `MX`.
3. Set the `Priority` to `10`.
4. Use the Default 4 hours for `TTL`.
5. Copy the MX Value from Resend into the `Mail Server` field
6. Select `Save`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-mx.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1222dfd2f85a612e61a52f15c2ac9818" data-og-width="3760" width="3760" data-og-height="2080" height="2080" data-path="images/squarespace-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-mx.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=57997b35909a2444d42950b6fe38b3c6 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-mx.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=adb6c9f2f806b66059441757d543f182 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-mx.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=8b67b3af818b09e029134f251f3dbc91 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-mx.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=4a4a248cefac6d882119b5496f18cb4f 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-mx.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=be2097df4c882c59e004058354d716f4 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-mx.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c6811425bbfebd859c0f05539108dbef 2500w" />

Below is a mapping of the record fields from Resend to Squarespace:

| Squarespace | Resend   | Example Value                           |
| ----------- | -------- | --------------------------------------- |
| Type        | Type     | `MX`                                    |
| Host        | Name     | `send`                                  |
| TTL         | -        | `4 hrs` (default)                       |
| Mail Server | Value    | `feedback-smtp.us-east-1.amazonses.com` |
| Priority    | Priority | `10`                                    |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use, try a number slightly higher like `11` or `12`.
</Info>

## Add TXT SPF Record

In the same **Custom records** section, select `Add Record` on Squarespace.

1. Type `send` for the `Host` of the record.
2. Set the `Type` to `TXT`.
3. Use the Default 4 hours for `TTL`.
4. Copy the TXT Value from Resend into the `Text` field
5. Select `Save`.

Add the **TXT Record** from your domain in Resend to Squarespace and click "Save".

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<br />

<img alt="Domain Details" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-txt.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=13d1b0604c22b16161d1b99e9bc2f8d8" data-og-width="3808" width="3808" data-og-height="2128" height="2128" data-path="images/squarespace-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-txt.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c024badbaf6d991dbd41e383c098431c 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-txt.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=a830dad19bc8133f259f863adb36ab93 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-txt.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=9d227072d138968d89b2dea3f3ccfe4d 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-txt.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=321a0bce5df0f7da026b74aed2a2e83c 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-txt.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=8176975bed1c18a10f54fdc0c87f1b68 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-spf-txt.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=77dc840c794b2a7ccfdc8210510ae320 2500w" />

Below is a mapping of the record fields from Resend to Squarespace:

| Squarespace | Resend | Example Value                         |
| ----------- | ------ | ------------------------------------- |
| Type        | Type   | `TXT`                                 |
| Host        | Name   | `send`                                |
| TTL         | -      | `4 hrs` (default)                     |
| Text        | Value  | `"v=spf1 include:amazonses.com ~all"` |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

## Add TXT DKIM Records

In the same **Custom records** section, select `Add Record` on Squarespace.

1. Type `resend._domainkey` for the `Host` of the record.
2. Set the `Type` to `TXT`.
3. Use the Default 4 hours for `TTL`.
4. Copy the TXT Value from Resend into the `Text` field
5. Select `Save`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-dkim-txt.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=119a6ade9688e65297e2dbff30e8256d" data-og-width="3808" width="3808" data-og-height="2128" height="2128" data-path="images/squarespace-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-dkim-txt.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=2cad01947e7fd0a574f1d0a792a075d0 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-dkim-txt.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6d08868ad91b6f64a81f9cb707077312 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-dkim-txt.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1ab2bf39649d6306dd574c0fc1be5c5f 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-dkim-txt.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=e94c27d41e5ed94bdb3e196214f1f9a1 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-dkim-txt.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=49a665af8c596915b38d56e13d679ca6 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/squarespace-dkim-txt.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=70510620dfff16e005fc60e184ea1d38 2500w" />

Below is a mapping of the record fields from Resend to Squarespace:

| Squarespace | Resend | Example Value                |
| ----------- | ------ | ---------------------------- |
| Type        | Type   | `TXT`                        |
| Host        | Name   | `resend._domainkey`          |
| TTL         | -      | `4 hrs` (default)            |
| Text        | Value  | `p=example_demain_key_value` |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take up to 72 hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Squarespace to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
