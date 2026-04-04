# Source: https://resend.com/docs/knowledge-base/strato.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Strato

> Verify your domain on Strato with Resend.

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

## Log in to Strato

Log in to your [Strato account](https://www.strato.es/apps/CustomerService):

1. In the left-hand navigation, go to Domains > Manage Domain.

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-domain-manager.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=684004473fd6679100907921ce2767df" data-og-width="2676" width="2676" data-og-height="1556" height="1556" data-path="images/dashboard-domains-strato-domain-manager.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-domain-manager.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8ee1ca43277416aad511bc02c0645a22 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-domain-manager.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=b31c4767e2c4b763f9c2e85b9f33863b 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-domain-manager.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5f862d4cae80d302482316c1fa53c8d6 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-domain-manager.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=406ee02fefe9f482a0e369991962df06 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-domain-manager.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=412b6303f288d15ffcb2a2167cfe67d4 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-domain-manager.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=74d186e01e0a9784081c61fc7ac15901 2500w" />

## Add MX SPF Record

1. On the domain page, click on the gear icon to redirect to Settings.
2. Create a new subdomain named `send`.
3. Navigate to the subdomain settings.
4. Go to the `DNS` tab, you'll see a list of DNS records you can update. Click on `manage` MX record.
5. Select own mail server.
6. Copy MX value from Resend into `Server` field.
7. Use the default priority `Low`.
8. Save settings.

<Info>
  By default, Strato domains use Strato mail server which uses `mail` as their
  send path. You will need to bypass this default behavior by creating a
  subdomain and setting the MX record there.
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9c884d56f98f468503cb10d28b6cd60f" data-og-width="2676" width="2676" data-og-height="1542" height="1542" data-path="images/dashboard-domains-strato-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8b24e49a7ea899b205f83b1c33cb50d3 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=35e741a5c70583dd89bb139455f51fec 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=ff97f297c4265a67c28ee0e158b22d80 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=feca11b40b1dd13d6260bd953201ee97 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=3c2851e92716db04d8440e4c4b9b556a 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=ae00fe866d20320ce48755d28ed3d052 2500w" />

Below is a mapping of the record fields from Resend to Strato:

| Strato      | Resend   | Example Value                            |
| ----------- | -------- | ---------------------------------------- |
| Type        | Type     | `MX Record`                              |
| Name        | Name     | `send`                                   |
| Mail server | Value    | `feedback-smtp.eu-west-1.amazonses.com.` |
| Priority    | Priority | `Low`                                    |

## Add TXT SPF Record

On the base domain settings:

1. Go to the `DNS` tab.
2. Manage TXT and CNAME records.
3. On the bottom, click `Create another record`.
4. Choose `TXT` type.
5. Add `send` for the `name` record.
6. For `value` input `v=spf1 include:amazonses.com ~all`.
7. Save settings.

<Info>
  Strato provides a standard DMARC record similar to Resend's recommended value:
  `v=DMARC1;p=reject;`.
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d3484aaa1f6eda375fce393939d69ada" data-og-width="1458" width="1458" data-og-height="933" height="933" data-path="images/dashboard-domains-strato-spf-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=327048341c74c44148c929533bedf240 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8e49b30305b73da1752c044eced85510 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9b990bff9396ae9b4e480941d95e9043 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=1962985af4b2105ab83333fc00bb6bf5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9494f3f61da603afb96dffd6768830d2 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4182c3c716cb8dde28c0ef5d48a4cff3 2500w" />

Below is a mapping of the record fields from Resend to Strato:

| Strato | Resend | Example Value                       |
| ------ | ------ | ----------------------------------- |
| Type   | Type   | `TXT Record`                        |
| Name   | Name   | `send`                              |
| Value  | Value  | `v=spf1 include:amazonses.com ~all` |

## Add TXT DKIM Records

On the same TXT and CNAME manage page:

1. Click `Create another record`.
2. Choose `TXT` type.
3. Add `resend._domainkey` for the `Name` record.
4. Copy the record value from Resend into the TXT value field.
5. Save settings.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=d3484aaa1f6eda375fce393939d69ada" data-og-width="1458" width="1458" data-og-height="933" height="933" data-path="images/dashboard-domains-strato-spf-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=327048341c74c44148c929533bedf240 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=8e49b30305b73da1752c044eced85510 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9b990bff9396ae9b4e480941d95e9043 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=1962985af4b2105ab83333fc00bb6bf5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9494f3f61da603afb96dffd6768830d2 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-strato-spf-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4182c3c716cb8dde28c0ef5d48a4cff3 2500w" />

Below is a mapping of the record fields from Resend to Strato:

| Strato | Resend | Example Value                |
| ------ | ------ | ---------------------------- |
| Type   | Type   | `TXT Record`                 |
| Name   | Name   | `send`                       |
| Value  | Value  | `p=example_demain_key_value` |

<Info>
  Copy DKIM value using the small copy icon in Resend. DKIM records are
  case-sensitive and must match up exactly.
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

1. Create a new subdomain named `inbound` (or whatever your subdomain is).
2. Navigate to the subdomain settings.
3. Go to the `DNS` tab and click on `manage` MX record.
4. Select own mail server.
5. Copy MX value from Resend into `Server` field.
6. Use the default priority `Low`.
7. Save settings.

Below is a mapping of the record fields from Resend to Strato:

| Strato      | Resend   | Example Value                           |
| ----------- | -------- | --------------------------------------- |
| Type        | Type     | `MX Record`                             |
| Name        | Name     | `inbound`                               |
| Mail server | Content  | `inbound-smtp.us-east-1.amazonaws.com.` |
| Priority    | Priority | `Low`                                   |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take a few hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Strato to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
