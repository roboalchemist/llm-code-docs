# Source: https://documentation.mailgun.com/docs/validate/api-overview.md

# Source: https://documentation.mailgun.com/docs/inboxready/api-reference/api-overview.md

# Source: https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview.md

# API Overview

## Base URL

All API calls referenced in our documentation start with a base URL. Mailgun allows the ability to send and receive email in both US and EU regions. Be sure to use the appropriate base URL based on which region you have created for your domain.

It is also important to note that Mailgun uses URI versioning for our API endpoints, and some endpoints may have different versions than others. Please reference the version stated in the URL for each endpoint.

For domains created in our US region the base URL is:


```
https://api.mailgun.net/
```

For domains created in our EU region the base URL is:


```
https://api.eu.mailgun.net/
```

### Date Format

Mailgun returns JSON for all API calls. JSON does not have a built-in date type; dates are passed as strings encoded according to [RFC-2822](https://tools.ietf.org/html/rfc2822.html#page-14). This format is native to JavaScript and is also supported by most programming languages out of the box


```JSON
'Thu, 13 Oct 2011 18:02:00 +0000'
```

Warning!
Abbreviated time zones like (EST, CET, IST, HLC) may not result in the correct offset due to ambiguous nature. Use numerical offset (+0500) or GMT/UTC instead.

## API Response Codes

All of Mailgun's HTTP response codes follow standard HTTP definitions.

| Code | Description | Troubleshooting |
|  --- | --- | --- |
| **400** | Bad Request | Response typically contains a JSON "message" key with human-readable error details |
| **401** | Unauthorized | Invalid or missing API key. Check that your API key is correct and properly formatted in the Authorization header |
| **403** | Forbidden | Valid credentials but access denied. Ensure you have permissions for the requested resource |
| **404** | Not Found | Resource not found. May be temporal due to eventually-consistent system. Missing JSON response usually indicates incorrect endpoint |
| **429** | Rate Limited | Rate limits exceeded. Retry as defined in response headers defined below. Contact support if limits need adjustment |
| **500** | Internal Error | Mailgun server error. Retry with exponential backoff. Contact support if issue persists |


### Rate Limit Headers

Mailgun APIs include the following headers to indicate rate limiting state for the current API being called:

| Header | Description |
|  --- | --- |
| **X-RateLimit-Limit** | Total calls that can be made in each time window |
| **X-RateLimit-Remaining** | Calls remaining in the given time window |
| **X-RateLimit-Reset** | Unix milliseconds (UTC) until the limit resets. Used for back-off logic on a HTTP 429 response |


Time windows may vary by API depending on resource usage.

## Mailgun Regions

Using a single account and billing plan, you can choose to provision new sending domains in the EU environment. It is important to note that message data never leaves the region in which it is processed. Only a limited amount of account data is replicated globally, giving you a single account from which to manage domains in both the US and the EU.

Here are the specifics on the type of data that is replicated globally versus what is region-bound:

| **Global** | **Region-Bound (US / EU)** |
|  --- | --- |
| Account Information, User Accounts, Billing Details (invoices/plan information), API Keys, Domain Names | Domain Metadata (e.g., SMTP credentials), Messages, Event Logs, Suppressions, Mailing Lists, Tags, Statistics, Routes, IP Addresses |


Below are the endpoints you will use for sending/receiving/tracking messages in the EU:

| **Service** | **US Endpoint** | **EU Endpoint** |
|  --- | --- | --- |
| REST API | api.mailgun.net | api.eu.mailgun.net |
| Outgoing SMTP Server | smtp.mailgun.org | smtp.eu.mailgun.org |
| Inbound SMTP Server (Routes) | mxa.mailgun.org | mxa.eu.mailgun.org |
| Inbound SMTP Server (Routes) | mxb.mailgun.org | mxb.eu.mailgun.org |
| Open/Click Tracking Endpoint | mailgun.org | eu.mailgun.org |