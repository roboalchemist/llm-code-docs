# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/reporting/dimensions.md

# Dimensions

| Dimension | API Variable Name | Example Values | Description |
|  --- | --- | --- | --- |
| Bot | bot | Apple GenericGmail  None | Identifies bot engagement with your emails. Bot engagement is classified as Apple, Gmail, Generic, or None. |
| Country | country |  US GB AU CA NL DE FR IN Unknown | Country identifies the country of origin for engagement data IPs. Only engagement data will display per country, all other data will show under the value âUnknownâ. Country codes use ISO 3166 country codes. |
| Domain | domain | mailgun.net yourdomain.com mg.yourdomain.com | Your sending domains. |
| IP Pool | ip_pool | Transactional IP PoolMarketing IP Pools | IP Pools enable you to group your dedicated IPs into customized "pools" to help manage your sending reputation for different mail-sending streams. |
| Sending IP | ip | 192.237.158.61159.135.234.21 166.78.71.1 69.72.42.3 | Your sending IPs. These may be dedicated or shared IPs. |
| Recipient Domain | recipient_domain | gmail.com outlook.com hotmail.com yahoo.com Other | The recipient domains youâve sent to, like Gmail.com, Outlook.com, and Yahoo.com. |
| Recipient Provider | recipient_provider | GmailGoogle WorkspaceOutlook 365Outlook USProtonYahoo USAppleChinese Outlook EUFrenchGermanOther EUCanadianUKOther USItalianOther | The recipient providers that youâve sent to. Recipient domains are aggregated to providers like Gmail, Google Workspace, or Outlook 365.[Click here](https://help.mailgun.com/hc/en-us/articles/23687761220635-Events-Logs-Recipient-Mailbox-Providers) to see the full list of Recipient Providers. |
| Subaccount | subaccount | Subaccount 1 Subaccount 2 | If youâve created subaccounts, you can use this dimension to view individual subaccount performance. |
| Tag | tag | Transactional Marketing Untagged | Tags are labels you attach to a message to identify or categorize your sending.By assigning a tag, youâre able to organize your email analytics so you have access to more precise and detailed insights. |
| Time | time | Mon, 19 Aug 2024 20:00:00+0000 Wed, 15 May 2024 19:00:00+0000 | The time that your events occured. The timezone in your account settings will be used for hourly data, but daily and monthly data will be aggregated using UTC time. Time uses the RFC 2822 format. |