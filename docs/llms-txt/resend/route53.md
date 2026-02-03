# Source: https://resend.com/docs/knowledge-base/route53.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS Route 53

> Verify your domain on Route 53 with Resend.

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

## Log in to Route 53

Then, log in to your [AWS Management Console, and open Route 53 console](https://console.aws.amazon.com/route53/), then click on your domain name. From there, click on `Create Record`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-createrecord.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=93d90903872f328b3f593e933d29f4fe" data-og-width="1510" width="1510" data-og-height="908" height="908" data-path="images/dashboard-domains-route53-createrecord.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-createrecord.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f157974546c8ac8cd07262b8fdab45a5 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-createrecord.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6caee08a6cf8d5a949ad1aae3fe6dd38 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-createrecord.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=421baff4e1d4371491d7ec453e23e1a1 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-createrecord.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4fee560a03261e4848eb423f1dde74cc 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-createrecord.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8380bdcb997d868690442bde7ec1e6ea 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-createrecord.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=17d29e4a7e487e2505c4f05f18acf55d 2500w" />

## Add MX SPF Record

1. Type in `send` for the `Record name`.
2. Select the `Record type` dropdown, and choose `MX`.
3. Copy the MX Value from your domain in Resend into the `Value` field.
4. Be sure to include the `10` in the `Value` field, as seen in the screenshot.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8b798e983ecec8edb48c777143edfce5" data-og-width="1512" width="1512" data-og-height="909" height="909" data-path="images/dashboard-domains-route53-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4ca4c23bb9f9b18be5116fc7008839ce 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37225bcc1842c60201f98742d53b11b2 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=7319e53b05ce4b6151c9f6f26a6d5cd8 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=52013e3042894a27e412e6a912c3a6a4 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=7661a013018e9118ef4c56c3a4d625ee 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=18af999a962838f89a4f02bb796d6851 2500w" />

Below is a mapping of the record fields from Resend to Route 53:

| Route 53       | Resend           | Example Value                              |
| -------------- | ---------------- | ------------------------------------------ |
| Record Type    | Type             | `MX Record`                                |
| Record name    | Name             | `send`                                     |
| Value          | Value & Priority | `10 feedback-smtp.us-east-1.amazonses.com` |
| TTL            | TTL              | `Use Route 53 Default (300)`               |
| Routing policy | -                | `Simple routing`                           |

<Info>
  Route 53 does not label the `priority` column, and you will need to add this
  in to the `Value` section, as shown in the screenshot. Do not use the same
  priority for multiple records. If Priority `10` is already in use, try a
  number slightly higher like `11` or `12`.
</Info>

## Add TXT SPF Record

In the same section, choose `Add another record`:

1. Type in `send` for the `Record name`.
2. Click the `Record type` dropdown.
3. Select the `Record type` dropdown, and choose `TXT`.
4. Copy TXT Value from your domain in Resend into the `Value` field.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=79d4f534f637964bc06005f34cafe92b" data-og-width="1509" width="1509" data-og-height="908" height="908" data-path="images/dashboard-domains-route53-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6d717b2919bf295508e8e8f9ff1f9598 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=128c1c173c00d7a60a4d81bd58bfd453 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=b9b42bc3a7182b042d3c467a17853cd2 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d0b6b17d05cd06a1534d21793e87d8c3 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a198633b1b07f28040b3b4086836e474 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=65273710240e189d588886d4a4bfcc9b 2500w" />

Below is a mapping of the record fields from Resend to Route 53:

| Route 53       | Resend | Example Value                         |
| -------------- | ------ | ------------------------------------- |
| Record type    | Type   | `TXT Record`                          |
| Record name    | Name   | `send`                                |
| Value          | Value  | `"v=spf1 include:amazonses.com ~all"` |
| TTL            | TTL    | `Use Route 53 Default (300)`          |
| Routing policy | -      | `Simple routing`                      |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

## Add TXT DKIM Records

In the same section, choose `Add another record`:

1. Type in `resend._domainkey` for the `Record name`.
2. Change the `Record Type` to `TXT`.
3. Copy the TXT Value value from your domain in Resend to the `Value` text box.
4. Click on `Create Records`.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-dkim-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=00e9fa493cb8a6541fa0d16323b1a7af" data-og-width="1513" width="1513" data-og-height="912" height="912" data-path="images/dashboard-domains-route53-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-dkim-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=619baf1427240a166a744fef9ca74a42 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-dkim-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=36af0efabddd9748dd777d9bc596e41c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-dkim-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=14c0f4ecf37ed85b4641fd84ec2857b4 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-dkim-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=94372258a3c022a4bce9e85a0bdc4442 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-dkim-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=85645af66181e8c4d50e32b83e1c29d7 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-route53-dkim-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=283bcdf7d90228749ed25774ddafe286 2500w" />

Below is a mapping of the record fields from Resend to Route 53:

| Route 53       | Resend | Example Value                |
| -------------- | ------ | ---------------------------- |
| Record type    | Type   | `TXT Record`                 |
| Record name    | Name   | `resend._domainkey`          |
| Value          | Value  | `p=example_demain_key_value` |
| TTL            | TTL    | `Use Route 53 Default (300)` |
| Routing policy | -      | `Simple routing`             |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

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

In the Route 53 console, click `Create Record`:

1. Type in `inbound` (or whatever your subdomain is) for the `Record name`.
2. Select the `Record type` dropdown, and choose `MX`.
3. Copy the MX Value from your domain in Resend into the `Value` field.
4. Be sure to include the `10` in the `Value` field (e.g., `10 inbound-smtp.us-east-1.amazonaws.com`).

Below is a mapping of the record fields from Resend to Route 53:

| Route 53       | Resend             | Example Value                             |
| -------------- | ------------------ | ----------------------------------------- |
| Record Type    | Type               | `MX Record`                               |
| Record name    | Name               | `inbound`                                 |
| Value          | Content & Priority | `10 inbound-smtp.us-east-1.amazonaws.com` |
| TTL            | TTL                | `Use Route 53 Default (300)`              |
| Routing policy | -                  | `Simple routing`                          |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take up to 5 hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Route 53 to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
