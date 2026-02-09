# Source: https://resend.com/docs/knowledge-base/godaddy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GoDaddy

> Verify your domain on GoDaddy with Resend.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

Prefer watching a video? Check out our video walkthrough below.

<YouTube id="eT4JZH6CHHo" />

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

## Log in to GoDaddy

Log in to your [GoDaddy account](https://sso.godaddy.com):

1. Select `DNS` from the left navigation
2. Find your domain in the list and select the domain
3. This will take you to the DNS management page for the domain

<img alt="Domain Details" src="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-manage.png?fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=544f608675414a8e562ee15665a9b102" data-og-width="2982" width="2982" data-og-height="1865" height="1865" data-path="images/dashboard-domains-godaddy-manage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-manage.png?w=280&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=a3fde3bf0f3edd540c9efd926c045730 280w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-manage.png?w=560&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=980de3f64856243e8b68932c471e108a 560w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-manage.png?w=840&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=89191ebf59ad185ae8b20b866abd1d4e 840w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-manage.png?w=1100&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=3c20e11c04393091098c5d7047a51c89 1100w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-manage.png?w=1650&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=e99fd2b29b79fb4d33ee8cc24debc9aa 1650w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-manage.png?w=2500&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=2c7e57037e4d00ce3b012f8f8e23d4a9 2500w" />

## Add MX SPF Record

Copy and paste the values MX in Resend to GoDaddy.

1. Click `Add New Record` to create a new record
2. Set the Type to `MX`.
3. Type `send` for the `Name` of the record.
4. Copy the MX Value from Resend into the `Value` field.
5. Add `10` for the `Priority`.
6. Set the TTL to `600` (or use the default).
7. Click `Save`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=bb0db2dd2809135194cfb62b695225cd" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=a95639f0752fdbaefd0eae3b93ec6255 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9e579bee139584def82c0a8688466681 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=80c20d31f9598b0f8aeb4b267725b4fe 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=f66dc758dec3ac85919063c4bb66f4d5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=187033c1e79e5f6f3b47fa0466def756 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-mx.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=2a0531e4d1d25117efaef896d40331e3 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-mx.png?fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=22442a78539dc70a959a152a396e8508" data-og-width="2983" width="2983" data-og-height="1865" height="1865" data-path="images/dashboard-domains-godaddy-spf-mx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-mx.png?w=280&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=91ab67e13d65058aab2dc1de7967744f 280w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-mx.png?w=560&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=628655b88dda8bbe256111674632b91a 560w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-mx.png?w=840&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=9a771fd482f4ee23ac1f59cb6a6a3aa5 840w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-mx.png?w=1100&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=7f8c319d48cdef1108258f1725eaf2ab 1100w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-mx.png?w=1650&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=bc9cfbaf5f3e5f64095f1a1697bfa8b3 1650w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-mx.png?w=2500&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=32eb62297d4403f7a3c35ea9b212f874 2500w" />

Below is a mapping of the record fields from Resend to GoDaddy:

| GoDaddy  | Resend   | Example Value                           |
| -------- | -------- | --------------------------------------- |
| Type     | Type     | `MX Record`                             |
| Name     | Name     | `send`                                  |
| Value    | Value    | `feedback-smtp.us-east-1.amazonses.com` |
| TTL      | -        | `600` (or use default)                  |
| Priority | Priority | `10`                                    |

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use on another record, try a higher value `20` or `30`.
</Info>

## Add TXT SPF Record

In the same section, add another record in GoDaddy.

1. Click `Add New Record` to create a new record
2. Set the Type to `TXT`.
3. Type `send` for the `Name` of the record.
4. Copy the TXT Value from Resend into the `Value` field.
5. Set the TTL to `600` (or use the default).
6. Click `Save`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=747425d0a224baeee2846c9a707d5bbc" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/dashboard-domains-resend-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=04f13a4953c918b5ffa05474c6e6190c 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=fa09e290427c24278edb3306e241e2f0 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=4e796dc0356e2176d0dfa9467aa9af8f 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=5e27ef23ba82f5fe62d483849c5a8ec5 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=991e5fe09e65097107fafe4de36c0bda 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-spf-txt.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=6fd70252df24dce6a9768e38d5c75ae0 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-txt.png?fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=849bd76a0e5c14daa2f727ed2f284036" data-og-width="2983" width="2983" data-og-height="1847" height="1847" data-path="images/dashboard-domains-godaddy-spf-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-txt.png?w=280&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=db820d035e89d6b4bc9efc0b5fc3f30b 280w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-txt.png?w=560&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=13d4eea2eedef074c874c62529a69021 560w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-txt.png?w=840&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=de38877e526354d314145b56c7ab1be1 840w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-txt.png?w=1100&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=64dcef44efc884970eb705a02fa530bb 1100w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-txt.png?w=1650&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=087cd0a989824abff261ec4b4408ca7f 1650w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-spf-txt.png?w=2500&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=cbec0833b912433b58eb163ffaad7d5a 2500w" />

Below is a mapping of the record fields from Resend to GoDaddy:

| GoDaddy | Resend | Example Value                         |
| ------- | ------ | ------------------------------------- |
| Type    | Type   | `TXT Record`                          |
| Name    | Name   | `send`                                |
| Value   | Value  | `"v=spf1 include:amazonses.com ~all"` |
| TTL     | -      | `600` (or use default)                |

## Add TXT DKIM Records

In the same section, add another record in GoDaddy.

1. Click `Add New Record` to create a new record
2. Set the Type to `TXT`.
3. Type `resend._domainkey` for the `Name` of the record.
4. Copy the record value from Resend into the `Value` field.
5. Set the TTL to `600` (or use the default).
6. Click `Save`.

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

<img alt="Domain Details" src="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=345d1dc6b7c138dbd92bd6928c634bd9" data-og-width="2992" width="2992" data-og-height="1868" height="1868" data-path="images/dashboard-domains-resend-dkim.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=280&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=37e5d282deda4e727e9f002cf5b8f0dd 280w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=560&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=978f4a7f13387c0d721acd80a944123c 560w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=840&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=cd473e4cdd467d31c1e2d4a507f5d914 840w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1100&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=784706a47cae7451a0200c461831bc30 1100w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=1650&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=9780d5ff17771270ed33a0176bd7bd55 1650w, https://mintcdn.com/resend/JHWt09hsc7E33HK2/images/dashboard-domains-resend-dkim.png?w=2500&fit=max&auto=format&n=JHWt09hsc7E33HK2&q=85&s=46f59e55a1a791b4a32e13bc49e5f0cd 2500w" />

<img alt="Domain Details" src="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-dkim-txt.png?fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=2df8ab88c72f0944f8071121e95295aa" data-og-width="2984" width="2984" data-og-height="1847" height="1847" data-path="images/dashboard-domains-godaddy-dkim-txt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-dkim-txt.png?w=280&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=2ce5344e8ca51fa6ed6c52f17a87fdb3 280w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-dkim-txt.png?w=560&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=9c488053cf998382384294f639fff907 560w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-dkim-txt.png?w=840&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=28952546f29ab7997ab9c46b968cbf63 840w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-dkim-txt.png?w=1100&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=58996c1b87dc7798efc0bb9c8478a517 1100w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-dkim-txt.png?w=1650&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=024d786eb73d77fe2527b4eb57dec148 1650w, https://mintcdn.com/resend/lQ2IedTbqKrTHWy8/images/dashboard-domains-godaddy-dkim-txt.png?w=2500&fit=max&auto=format&n=lQ2IedTbqKrTHWy8&q=85&s=6f5fd9f8d52afbc50b4cf53b140e28b0 2500w" />

Below is a mapping of the record fields from Resend to GoDaddy:

| GoDaddy | Resend | Example Value                |
| ------- | ------ | ---------------------------- |
| Type    | Type   | `TXT Record`                 |
| Name    | Name   | `resend._domainkey`          |
| Value   | Value  | `p=example_demain_key_value` |
| TTL     | -      | `600` (or use default)       |

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

Click `Add New Record` to create a new record:

1. Set the Type to `MX`.
2. Type `inbound` (or whatever your subdomain is) for the `Name` of the record.
3. Copy the MX Value from Resend into the `Value` field.
4. Add `10` for the `Priority`.
5. Set the TTL to `600` (or use the default).
6. Click `Save`.

Below is a mapping of the record fields from Resend to GoDaddy:

| GoDaddy  | Resend   | Example Value                          |
| -------- | -------- | -------------------------------------- |
| Type     | Type     | `MX Record`                            |
| Name     | Name     | `inbound`                              |
| Value    | Content  | `inbound-smtp.us-east-1.amazonaws.com` |
| TTL      | -        | `600` (or use default)                 |
| Priority | Priority | `10`                                   |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take a few hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to GoDaddy to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
