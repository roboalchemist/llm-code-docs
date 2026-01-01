# Source: https://documentation.mailgun.com/docs/validate/single-valid-ir.md

# Single Validation

Info
The Validation feature is rate limited to a set number of active requests at a time. If you receive a 429 error, please wait and try again.


```
GET /v4/address/validate
```

Given an arbitrary address, verifies address based off defined checks.

| Parameter | Description |
|  --- | --- |
| address | An email address to verify. (Maximum: 512 characters) |



```
POST /v4/address/validate
```

Given an arbitrary address, verifies address based off defined checks.

| Form-Data | Description |
|  --- | --- |
| address | An email address to verify. (Maximum: 512 characters) |


## Request Examples

Verify a single email address using the GET method.


```JSON
curl -s --user 'api:YOUR_API_KEY' \
    'https://api.mailgun.net/v4/address/validate?address=foo@mailgun.com'
```

Verify a single email address using the POST method.


```JSON
curl -s --user 'api:YOUR_API_KEY' -X POST \
    'https://api.mailgun.net/v4/address/validate' \
    -d 'address=foo@mailgun.com'
}
```

Example of a failed mailbox verification result.


```JSON
{
"address":"nonexistentemail@realdomain.com",
"is_disposable_address":false,
"is_role_address":false,
"reason":["mailbox_does_not_exist"],
"result":"undeliverable",
"risk":"high"
}
```

Example of successful mailbox verification result.


```JSON
{
"address":"existingemail@realdomain.com",
"is_disposable_address":false,
"is_role_address":false,
"reason":[],
"result":"deliverable",
"risk":"low"
}
```

## Field Explanation

| Parameter | Type | Description |
|  --- | --- | --- |
| address | string | Email address being verified |
| did_you_mean | string | (Optional) Null if nothing, however if a potential typo is made to the domain, the closest suggestion is provided |
| engagement | object | Contains the boolean fields is_bot and engaged as well as, the string field engagement which lists the type of engagment with the given email |
| is_disposable_address | boolean | If the domain is in a list of disposable email addresses, this will be appropriately categorized |
| is_role_address | boolean | Checks the mailbox portion of the email if it matches a specific role type ('admin', 'sales', 'webmaster') |
| reason | array | List of potential reasons why a specific validation may be unsuccessful. |
| result | string | Either deliverable, undeliverable, do_not_send, catch_all, or unknown. Please see the Result Types section below for details on each result type. |
| risk | string | high, medium, low, or unknown Depending on the evaluation of all aspects of the given email. |
| root_address | string | (Optional) If the address is an alias; this will contain the root email address with alias parts removed. |


The provider lookup query parameter provides users with the control to allow or prevent Mailgun from reaching out to the mailbox provider.


```
GET /v4/address/validate?address=test123@test.com&provider_lookup=true
```


```
POST /v4/address/validate?provider_lookup=true
```

'true' (default state) - A provider lookup will be performed if Mailgun's internal analysis is insufficient.

'false' - A provider lookup will not be performed. If Mailgun does not have information on the recipient address, the API will return the following response:


```JSON
{
"address":"address@domain.com",
"is_disposable_address":false,
"is_role_address":false,
"reason":["no_data"],
"result":"unknown",
"risk":"unknown"
}
```

## Reason Explanation

| Reason | Description |
|  --- | --- |
| unknown_provider | The MX provider is an unknown provider. |
| no_mx / No MX host found | The recipient domain does not have a valid MX host. *Note: this reason will be consolidated to only "no_mx" in the future.* |
| high_risk_domain | Information obtained about the domain indicates it is high risk to send email to. |
| subdomain_mailer | The recipient domain is identified to be a subdomain and is not on our exception list. Subdomains are considered to be high risk as many spammers and malicious actors utilize them. |
| immature_domain | The domain is newly created based on the WHOIS information. |
| tld_risk | The domain has a top-level-domain (TLD) that has been identified as high risk. |
| mailbox_does_not_exist | The mailbox is undeliverable or does not exist. |
| mailbox_is_disposable_address | The mailbox has been identified to be a disposable address. Disposable address are temporary, generally one time use, addresses. |
| mailbox_is_role_address | The mailbox is a role based address (ex. support@â¦, marketing@â¦). |
| catch_all | The validity of the recipient address cannot be determined as the provider accepts any and all email regardless of whether or not the recipient's mailbox exists. |
| accept_all | The validity of the recipient address cannot be determined because the mail server accepts all email addresses regardless of whether the mailbox exists. Invalid addresses may generate delayed bounce notifications after delivery is attempted. |
| long_term_disposable | The mailbox has been identified as a long term disposable address. Long term disposable addresses can be quickly and easily deactivated by users, but they will not expire without user intervention. |
| failed custom grammar check | The mailbox failed our custom ESP local-part grammar check. |
| mailbox_quota_exceeded | The mailbox is full and cannot accept more mail. |
| smtp_error | An error was returned while attempting to validate the address. |
| smtp_timeout | The MX host did not respond within our expected timeframe. |


## Result Types

| Result | Description |
|  --- | --- |
| deliverable | The recipient address is considered to be valid and should accept email. |
| undeliverable | The recipient address is considered to be invalid and will result in a bounce if sent to. |
| do_not_send | The recipient address is considered to be highly risky and will negatively impact sending reputation if sent to. |
| catch_all | The validity of the recipient address cannot be determined as the provider accepts any and all email regardless of whether or not the recipient's mailbox exists. |
| unknown | The validity of the recipient address cannot be determined for a variety of potential reasons. Please refer to the associated 'reason' array returned in the response. |